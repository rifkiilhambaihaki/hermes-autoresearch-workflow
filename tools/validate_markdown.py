#!/usr/bin/env python3
"""Validate Markdown structure and publication-safe link targets.

Checks all Markdown files recursively, excluding .git. The implementation uses
only the Python standard library and returns a nonzero status for any finding.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})(.*)$")
HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*$")
SETEXT_RE = re.compile(r"^\s{0,3}(?:=+|-+)\s*$")
INLINE_LINK_RE = re.compile(
    r"!?\[[^\]]*\]\(\s*(<[^>]*>|[^\s)]+)"
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
REFERENCE_TARGET_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(?:<([^>]+)>|(\S+))")
DRIVE_HOSTS = {"drive" + ".google.com", "docs" + ".google.com"}
PRIVATE_UNIX_RE = re.compile(r"^/(?:home|Users)/[^/]+(?:/|$)")
PRIVATE_WINDOWS_RE = re.compile(r"(?i)^[A-Z]:[\\/](?:Users|Documents and Settings)[\\/]")
URI_SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="repository root (default: current directory)")
    return parser.parse_args()


def markdown_files(root: Path) -> tuple[list[Path], list[str]]:
    files: list[Path] = []
    findings: list[str] = []
    for current, dirs, names in os.walk(root, topdown=True, followlinks=False):
        dirs[:] = sorted((name for name in dirs if name != ".git"), key=str.casefold)
        current_path = Path(current)
        for name in sorted(names, key=str.casefold):
            path = current_path / name
            if path.suffix.casefold() != ".md":
                continue
            if path.is_symlink():
                findings.append(f"{path.relative_to(root).as_posix()}: Markdown file is a symlink")
            else:
                files.append(path)
    return files, findings


def visible_lines(lines: list[str], rel: str) -> tuple[list[tuple[int, str]], list[str]]:
    """Return lines outside code fences and report malformed fences."""
    visible: list[tuple[int, str]] = []
    findings: list[str] = []
    open_char: str | None = None
    open_length = 0
    open_line = 0
    for number, line in enumerate(lines, 1):
        match = FENCE_RE.match(line)
        if open_char is None:
            if match:
                marker = match.group(1)
                open_char = marker[0]
                open_length = len(marker)
                open_line = number
            else:
                visible.append((number, line))
        elif match:
            marker = match.group(1)
            # Closing fences use the same character, are at least as long, and
            # may be followed only by whitespace.
            if marker[0] == open_char and len(marker) >= open_length and not match.group(2).strip():
                open_char = None
                open_length = 0
                open_line = 0
    if open_char is not None:
        findings.append(f"{rel}:{open_line}: unclosed {open_char * open_length} code fence")
    return visible, findings


def clean_destination(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    return target


def destination_findings(target: str, source: Path, root: Path, line: int) -> list[str]:
    rel = source.relative_to(root).as_posix()
    prefix = f"{rel}:{line}"
    target = clean_destination(target)
    if not target:
        return [f"{prefix}: empty link target"]

    decoded = unquote(target)
    parsed = urlsplit(decoded)
    host = (parsed.hostname or "").casefold()
    if any(host == base or host.endswith("." + base) for base in DRIVE_HOSTS):
        return [f"{prefix}: Google Drive/Docs link is not allowed: {target}"]

    path_part = parsed.path
    if parsed.scheme.casefold() == "file":
        return [f"{prefix}: absolute file link is not allowed: {target}"]
    if PRIVATE_UNIX_RE.match(path_part) or PRIVATE_WINDOWS_RE.match(decoded):
        return [f"{prefix}: absolute private path is not allowed: {target}"]
    if decoded.startswith("/") or decoded.startswith("\\\\"):
        return [f"{prefix}: absolute local path is not allowed: {target}"]

    # Other schemes, protocol-relative URLs, and in-document anchors are not
    # local filesystem references.
    if URI_SCHEME_RE.match(decoded) or decoded.startswith("//") or decoded.startswith("#"):
        return []

    local_path = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not local_path:
        return []
    local_path = local_path.replace("/", os.sep)
    candidate = source.parent / local_path
    try:
        candidate.resolve(strict=False).relative_to(root.resolve())
    except ValueError:
        return [f"{prefix}: local target escapes repository root: {target}"]
    if not candidate.exists():
        return [f"{prefix}: local target does not exist: {target}"]
    return []


def normalized_heading(text: str) -> str:
    text = re.sub(r"\s+#+\s*$", "", text).strip()
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[*_~`]", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return " ".join(text.casefold().split())


def validate_file(path: Path, root: Path) -> list[str]:
    rel = path.relative_to(root).as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return [f"{rel}: cannot read as UTF-8: {exc}"]

    visible, findings = visible_lines(text.splitlines(), rel)
    headings: list[tuple[int, str]] = []
    for index, (line_number, line) in enumerate(visible):
        # Remove inline code before looking for Markdown links so examples do
        # not become filesystem requirements.
        link_text = re.sub(r"`[^`]*`", "", line)
        for match in INLINE_LINK_RE.finditer(link_text):
            findings.extend(destination_findings(match.group(1), path, root, line_number))
        reference = REFERENCE_TARGET_RE.match(link_text)
        if reference:
            findings.extend(destination_findings(reference.group(1) or reference.group(2), path, root, line_number))
        heading = HEADING_RE.match(line)
        if heading:
            headings.append((line_number, normalized_heading(heading.group(2))))
        elif SETEXT_RE.match(line) and index > 0:
            previous_number, previous_line = visible[index - 1]
            # A Setext underline applies only to the immediately preceding
            # nonblank line outside a code fence.
            if previous_number == line_number - 1 and previous_line.strip():
                headings.append((previous_number, normalized_heading(previous_line)))

    if path.parent == root and path.name.casefold() == "readme.md":
        counts = Counter(text for _, text in headings if text)
        for heading, count in sorted(counts.items()):
            if count > 1:
                locations = ", ".join(str(number) for number, text in headings if text == heading)
                findings.append(
                    f"{rel}:{locations}: duplicate README heading {heading!r} ({count} occurrences)"
                )
    return findings


def validate(root: Path) -> list[str]:
    if not root.exists():
        return [f"candidate does not exist: {root}"]
    if not root.is_dir():
        return [f"candidate is not a directory: {root}"]
    files, findings = markdown_files(root)
    for path in files:
        findings.extend(validate_file(path, root))
    return sorted(set(findings), key=str.casefold)


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser().absolute()
    findings = validate(root)
    if findings:
        print(f"Markdown validation failed with {len(findings)} finding(s):", file=sys.stderr)
        for finding in findings:
            print(f"- {finding}", file=sys.stderr)
        return 1
    print(f"Markdown validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
