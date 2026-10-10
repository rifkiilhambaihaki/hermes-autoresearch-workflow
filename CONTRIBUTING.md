# Contributing

Thank you for helping improve this documentation project.

## Before you begin

- Open an issue before proposing a substantial change.
- Keep contributions focused on the workflow, prompts, templates, checklists, or supporting documentation.
- Do not add datasets, model weights, generated experiment artifacts, personal information, credentials, or proprietary material.
- Submit only work that you have the right to license under the repository's MIT License.

## Making a change

1. Fork the repository and create a focused branch.
2. Follow the existing Markdown style: descriptive headings, short paragraphs, and fenced code blocks with a language where appropriate.
3. Keep examples generic. Use obvious placeholders instead of live identifiers, paths, links, or access values.
4. Check every relative link and image reference.
5. Run the local checks from the repository root:

   ```bash
   python3 tools/audit_publication.py .
   python3 tools/validate_markdown.py .
   ```

6. Submit a pull request explaining what changed, why it changed, and how it was checked.

## Pull-request expectations

A contribution should be clear, self-contained, and consistent with the project's docs-only scope. Reviewers may request changes for accuracy, safety, licensing, accessibility, or maintainability. Please keep unrelated edits in separate pull requests.

## Reporting security concerns

Do not put sensitive details in an issue or pull request. Follow [SECURITY.md](SECURITY.md) instead.

## Code of conduct

Be respectful, constructive, and welcoming. Harassment, discrimination, and abusive behavior are not acceptable in project spaces.
