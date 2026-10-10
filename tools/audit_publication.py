#!/usr/bin/env python3
"""Fail closed when a directory contains material unsafe for publication.

This utility uses only the Python standard library. It intentionally scans every
entry except .git; ignore files do not suppress checks.
"""

from __future__ import annotations

import argparse
import os
import re
import stat
import sys
from pathlib import Path
from typing import Iterator

DEFAULT_MAX_BYTES = 1_048_576

# Names that should never be present in a publication candidate. Comparisons are
# case-insensitive. The suffix rules below cover common generated data as well.
EXCLUDED_NAMES = {
    ".ds_store",
    "thumbs.db",
    "desktop.ini",
    "id_rsa",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
    "credentials",
    "credentials.json",
    "secrets.json",
    "backup",
    "backups",
    "log",
    "logs",
    "internal_notes.md",
    "private_notes.md",
}
EXCLUDED_SUFFIXES = {
    ".bak",
    ".backup",
    ".db",
    ".dump",
    ".key",
    ".log",
    ".old",
    ".orig",
    ".p12",
    ".pem",
    ".pfx",
    ".sqlite",
    ".sqlite3",
    ".swp",
    ".tmp",
}

# Assemble high-risk literals so this scanner does not report its own source.
DRIVE_HOST = "drive" + ".google.com"
DOCS_HOST = "docs" + ".google.com"
PRIVATE_KEY_MARKER = "BEGIN " + "PRIVATE KEY"
EXCLUDED_TERMS = (
    "do not " + "publish",
    "not for " + "public release",
    "internal " + "only",
    "company " + "confidential",
    "strictly " + "confidential",
)

SECRET_PATTERNS = (
    ("private-key marker", re.compile(re.escape(PRIVATE_KEY_MARKER), re.IGNORECASE)),
    ("AWS access key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("GitHub access token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,255}\b")),
    ("GitHub fine-grained token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{40,255}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("Bearer token", re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/=-]{20,}")),
    (
        "assigned secret",
        re.compile(
            r"(?i)\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|"
            r"password|passwd|secret[_-]?key)\b\s*[:=]\s*['\"]?"
            r"(?!example\b|placeholder\b|replace[_-]?me\b|your[_-]?)"
            r"[A-Za-z0-9._~+/=-]{12,}"
        ),
    ),
)

DRIVE_URL_RE = re.compile(
    r"(?i)https?://(?:www\.)?(?:" + re.escape(DRIVE_HOST) + "|" + re.escape(DOCS_HOST) + r")(?:/|\b)"
)
DRIVE_ID_RE = re.compile(
    r"(?i)\b(?:google[_ -]?)?drive[_ -]?(?:file[_ -]?)?id\b\s*[:=]\s*['\"]?"
    r"[A-Za-z0-9_-]{20,}"
)
PRIVATE_PATH_PATTERNS = (
    re.compile(r"(?:^|[\s'\"(=])/(?:home|Users|root)/[^/\s'\")]+(?:/[^\s'\")]+)*"),
    re.compile(r"(?i)(?:^|[\s'\"(=])[A-Z]:\\Users\\[^\s'\"]+"),
    re.compile(r"(?i)file:///(?:home|Users)/[^\s'\")]+"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="candidate repository (default: current directory)")
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=DEFAULT_MAX_BYTES,
        help=f"largest allowed file in bytes (default: {DEFAULT_MAX_BYTES})",
    )
    args = parser.parse_args()
    if args.max_bytes < 1:
        parser.error("--max-bytes must be positive")
    return args


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix() or "."
    except ValueError:
        return str(path)


def walk(root: Path) -> Iterator[tuple[Path, OSError | None]]:
    """Yield every entry without following symlinks, excluding only .git."""
    stack = [root]
    while stack:
        directory = stack.pop()
        try:
            entries = sorted(os.scandir(directory), key=lambda item: item.name.casefold(), reverse=True)
        except OSError as exc:
            yield directory, exc
            continue
        for entry in entries:
            if entry.name == ".git":
                continue
            path = Path(entry.path)
            yield path, None
            try:
                if entry.is_dir(follow_symlinks=False) and not entry.is_symlink():
                    stack.append(path)
            except OSError:
                # The normal inspection below will report an inaccessible entry.
                pass


def filename_finding(path: Path) -> str | None:
    name = path.name.casefold()
    if name == ".env" or name.startswith(".env."):
        return "environment file"
    if name in EXCLUDED_NAMES:
        return "excluded filename"
    if any(name.endswith(suffix) for suffix in EXCLUDED_SUFFIXES):
        return "excluded file type"
    if "credential" in name or "secret" in name:
        return "sensitive filename"
    stem = path.stem.casefold()
    if stem.startswith(("backup_", "backup-", "internal_", "internal-", "private_", "private-")):
        return "excluded filename term"
    if stem.endswith(("_backup", "-backup")):
        return "backup filename"
    return None


def content_findings(text: str) -> list[str]:
    findings: list[str] = []
    for label, pattern in SECRET_PATTERNS:
        if pattern.search(text):
            findings.append(label)
    if DRIVE_URL_RE.search(text):
        findings.append("Google Drive URL")
    if DRIVE_ID_RE.search(text):
        findings.append("Google Drive file ID")
    if any(pattern.search(text) for pattern in PRIVATE_PATH_PATTERNS):
        findings.append("absolute private path")
    folded = text.casefold()
    for term in EXCLUDED_TERMS:
        if term in folded:
            findings.append(f"excluded term: {term!r}")
    return findings


def audit(root: Path, max_bytes: int) -> list[str]:
    findings: list[str] = []
    if root.is_symlink():
        return [".: candidate root is a symlink"]
    if not root.exists():
        return [f".: candidate does not exist: {root}"]
    if not root.is_dir():
        return [f".: candidate is not a directory: {root}"]

    for path, scan_error in walk(root):
        rel = relative(path, root)
        if scan_error is not None:
            findings.append(f"{rel}: cannot scan directory: {scan_error}")
            continue
        try:
            mode = path.lstat().st_mode
        except OSError as exc:
            findings.append(f"{rel}: cannot inspect: {exc}")
            continue
        if stat.S_ISLNK(mode):
            findings.append(f"{rel}: symbolic link is not allowed")
            continue
        name_issue = filename_finding(path)
        if name_issue:
            findings.append(f"{rel}: {name_issue}")
        if stat.S_ISDIR(mode):
            continue
        if not stat.S_ISREG(mode):
            findings.append(f"{rel}: special file is not allowed")
            continue

        try:
            size = path.stat().st_size
        except OSError as exc:
            findings.append(f"{rel}: cannot determine size: {exc}")
            continue
        if size > max_bytes:
            findings.append(f"{rel}: file is too large ({size} bytes; limit {max_bytes})")
            continue
        try:
            raw = path.read_bytes()
        except OSError as exc:
            findings.append(f"{rel}: cannot read: {exc}")
            continue
        if b"\x00" in raw:
            findings.append(f"{rel}: binary file (NUL byte detected)")
            continue
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            findings.append(f"{rel}: not valid UTF-8 ({exc})")
            continue
        if any(ord(char) < 32 and char not in "\t\n\r\f" for char in text):
            findings.append(f"{rel}: binary/control characters detected")
            continue
        for issue in content_findings(text):
            findings.append(f"{rel}: {issue}")
    return sorted(set(findings), key=str.casefold)


def main() -> int:
    args = parse_args()
    # Keep the final path component unresolved so a symlink used as the
    # candidate root is detected rather than silently followed.
    root = Path(args.root).expanduser().absolute()
    findings = audit(root, args.max_bytes)
    if findings:
        print(f"Publication audit failed with {len(findings)} finding(s):", file=sys.stderr)
        for finding in findings:
            print(f"- {finding}", file=sys.stderr)
        return 1
    print(f"Publication audit passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
