#!/usr/bin/env python3
"""Validate a Kid Activity Lab parent-test evidence intake."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys


ACTIVITIES = {
    "Ramp Detective",
    "Bridge Rescue",
    "Shadow Builder",
    "Windproof Tower",
    "Tiny Boat Cargo Test",
}

FIELDS = (
    "Evidence status",
    "Activity",
    "Test date",
    "Observer",
    "Setup minutes",
    "Engagement minutes",
    "Fast yes or hesitation",
    "Exact child quote",
    "Instruction confusion",
    "Child-led change",
    "Mess and cleanup",
    "Repeatability",
    "Evidence assets",
    "Next version",
    "Additional notes",
    "Observed in a real session",
)

PLACEHOLDER_RE = re.compile(r"^<.*>$")


def parse_fields(text: str) -> tuple[dict[str, str], list[str]]:
    values: dict[str, str] = {}
    errors: list[str] = []
    for field in FIELDS:
        matches = re.findall(rf"^{re.escape(field)}:\s*(.*)$", text, re.MULTILINE)
        if len(matches) != 1:
            errors.append(f"{field}: expected exactly one field, found {len(matches)}")
            continue
        values[field] = matches[0].strip()
    return values, errors


def validate_minutes(field: str, value: str, errors: list[str]) -> None:
    if value == "UNKNOWN":
        return
    if not value.isdigit() or not 0 <= int(value) <= 1440:
        errors.append(f"{field}: use UNKNOWN or a whole number from 0 to 1440")


def validate_completed(values: dict[str, str], errors: list[str]) -> None:
    for field in ("Setup minutes", "Engagement minutes"):
        if not values[field].isdigit():
            errors.append(f"{field}: completed evidence requires whole minutes")

    explicit_fields = (
        "Fast yes or hesitation",
        "Exact child quote",
        "Instruction confusion",
        "Child-led change",
        "Mess and cleanup",
        "Evidence assets",
        "Next version",
        "Additional notes",
    )
    for field in explicit_fields:
        value = values[field]
        if value in {"UNKNOWN", "NOT_OBSERVED"} or PLACEHOLDER_RE.match(value):
            errors.append(
                f"{field}: completed evidence requires an observed value or NONE"
            )

    if values["Repeatability"] == "UNKNOWN":
        errors.append("Repeatability: completed evidence requires YES, NO, or MAYBE")


def validate(path: Path, template_mode: bool) -> list[str]:
    values, errors = parse_fields(path.read_text(encoding="utf-8"))
    if errors:
        return errors

    status = values["Evidence status"]
    attestation = values["Observed in a real session"]
    if status not in {"DRAFT", "OBSERVED"}:
        errors.append("Evidence status: use DRAFT or OBSERVED")
    if attestation not in {"NO", "YES"}:
        errors.append("Observed in a real session: use NO or YES")
    if (status, attestation) not in {("DRAFT", "NO"), ("OBSERVED", "YES")}:
        errors.append("Evidence status and real-session attestation must agree")
    if template_mode and (status, attestation) != ("DRAFT", "NO"):
        errors.append("Template mode only validates a DRAFT with a NO attestation")

    activity = values["Activity"]
    if not template_mode and activity not in ACTIVITIES:
        errors.append("Activity: use one of the five activity names in the test pack")

    test_date = values["Test date"]
    if not template_mode:
        try:
            parsed_date = date.fromisoformat(test_date)
            if parsed_date > date.today():
                errors.append("Test date: cannot be in the future")
        except ValueError:
            errors.append("Test date: use a real ISO date in YYYY-MM-DD format")

    observer = values["Observer"]
    if not template_mode and (not observer or PLACEHOLDER_RE.match(observer)):
        errors.append("Observer: replace the placeholder with a name or role")

    validate_minutes("Setup minutes", values["Setup minutes"], errors)
    validate_minutes("Engagement minutes", values["Engagement minutes"], errors)

    if values["Repeatability"] not in {"YES", "NO", "MAYBE", "UNKNOWN"}:
        errors.append("Repeatability: use YES, NO, MAYBE, or UNKNOWN")

    for field in FIELDS:
        if not values[field]:
            errors.append(f"{field}: value cannot be blank")

    if not template_mode:
        if status != "OBSERVED":
            errors.append("Completed evidence must be OBSERVED with a YES attestation")
        else:
            validate_completed(values, errors)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--template",
        action="store_true",
        help=(
            "Validate a DRAFT/NO blank template while allowing activity, date, "
            "and observer placeholders."
        ),
    )
    args = parser.parse_args()

    if not args.path.is_file():
        print(f"ERROR: file not found: {args.path}", file=sys.stderr)
        return 2

    errors = validate(args.path, args.template)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"PASS: {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
