#!/usr/bin/env python3
from __future__ import annotations

import argparse
import pathlib
import re
import sys


REQUIRED_HEADINGS = [
    "## 1. Task Restatement",
    "## 2. Task Classification",
    "## 3. Repository Evidence",
    "## 4. What Seems In Scope",
    "## 5. What Seems Out of Scope",
    "## 6. Key Ambiguities",
    "## 7. Likely Impacted Areas",
    "## 8. Risks and Invariants",
    "## 9. Scope Boundaries",
    "## 10. Implementation Contract",
    "## 11. Validation Plan",
    "## 12. Readiness Decision",
    "## 13. Notes",
]

VALID_READINESS = {
    "ready-for-implementation",
    "needs-user-clarification",
    "needs-codebase-investigation",
    "not-safe-to-proceed",
}

PLACEHOLDER_PATTERNS = [
    re.compile(r"^\s*-\s*\.\.\.\s*$", re.MULTILINE),
    re.compile(r"^\s*-\s*What is being requested.*$", re.MULTILINE),
    re.compile(r"^\s*-\s*Bug fix / enhancement / refactor / migration / investigation / cleanup / other\s*$", re.MULTILINE),
    re.compile(r"^\s*-\s*ready-for-implementation / needs-user-clarification / needs-codebase-investigation / not-safe-to-proceed\s*$", re.MULTILINE),
]


def extract_sections(content: str) -> dict[str, str]:
    heading_pattern = re.compile(r"^##\s+\d+\.\s+.+$", re.MULTILINE)
    matches = list(heading_pattern.finditer(content))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(content)
        sections[match.group(0).strip()] = content[start:end].strip()
    return sections


def validate_summary(path: pathlib.Path) -> list[str]:
    errors: list[str] = []
    content = path.read_text(encoding="utf-8")

    sections = extract_sections(content)

    for heading in REQUIRED_HEADINGS:
        if heading not in sections:
            errors.append(f"Missing required heading: {heading}")

    if errors:
        return errors

    for heading in REQUIRED_HEADINGS:
        body = sections[heading]
        if not body:
            errors.append(f"Section is empty: {heading}")

    for pattern in PLACEHOLDER_PATTERNS:
        if pattern.search(content):
            errors.append(f"Template placeholder still present: {pattern.pattern}")

    readiness_body = sections["## 12. Readiness Decision"]
    readiness_values = {
        line.strip()[2:].strip()
        for line in readiness_body.splitlines()
        if line.strip().startswith("- ")
    }
    if len(readiness_values) != 1:
        errors.append("Readiness Decision must contain exactly one bullet with one decision value.")
    else:
        readiness_value = next(iter(readiness_values))
        if readiness_value not in VALID_READINESS:
            errors.append(
                "Readiness Decision must be one of: "
                + ", ".join(sorted(VALID_READINESS))
            )

    repo_evidence = sections["## 3. Repository Evidence"]
    if "Confirmed files" in repo_evidence or "Important unknowns" in repo_evidence:
        errors.append("Repository Evidence still contains template label text.")

    validation_plan = sections["## 11. Validation Plan"]
    required_validation_keys = ["lint:", "typecheck:", "tests:", "manual validation:", "docs/config review:"]
    for key in required_validation_keys:
        if key not in validation_plan:
            errors.append(f"Validation Plan is missing key: {key}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a clarification summary produced by task-clarification-harness."
    )
    parser.add_argument("summary_path", help="Path to the markdown summary file")
    args = parser.parse_args()

    path = pathlib.Path(args.summary_path)
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 1

    errors = validate_summary(path)
    if errors:
        print("Clarification summary is invalid:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Clarification summary is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
