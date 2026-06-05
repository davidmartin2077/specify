#!/usr/bin/env python3
"""Validate risk-reasoning JSONL datasets.

The validator is intentionally dependency-free so it can run in a fresh
workspace. It checks the fields defined in schemas/sample_schema.json plus a
few project-specific quality rules from docs/annotation_guideline.md.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = {
    "id",
    "text",
    "risk_level",
    "encoding_primary",
    "context_required",
    "ambiguity",
    "evidence_strength",
    "hard_negative",
    "reasoning",
}

REQUIRED_REASONING_FIELDS = {
    "literal_analysis",
    "encoding_analysis",
    "context_analysis",
    "supporting_evidence",
    "counter_evidence",
    "final_rationale",
}

ENUMS = {
    "split": {"train", "validation", "val", "test", "eval", "holdout"},
    "source_type": {"synthetic", "real", "synthetic_or_real", "mixed", "unknown"},
    "risk_level": {"high", "medium", "low", "none"},
    "ambiguity": {"low", "medium", "high"},
    "evidence_strength": {"weak", "moderate", "strong"},
    "freshness": {"stable", "recent", "expired"},
    "quality_status": {"draft", "reviewed", "approved", "rejected", "needs_revision"},
}

STRING_FIELDS = {
    "id",
    "split",
    "source_type",
    "platform",
    "text",
    "risk_level",
    "encoding_primary",
    "ambiguity",
    "evidence_strength",
    "freshness",
    "target_reference",
    "quality_status",
    "review_notes",
}

BOOLEAN_FIELDS = {
    "context_required",
    "hard_negative",
    "target_known",
    "should_explain_target",
}

LIST_OF_STRING_FIELDS = {
    "encoding_secondary",
}

REASONING_LIST_FIELDS = {
    "literal_analysis",
    "encoding_analysis",
    "context_analysis",
    "supporting_evidence",
    "counter_evidence",
}


@dataclass
class ValidationMessage:
    path: Path
    line_number: int
    message: str


def is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_string_list(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def add_error(errors: list[ValidationMessage], path: Path, line_number: int, message: str) -> None:
    errors.append(ValidationMessage(path=path, line_number=line_number, message=message))


def validate_context(sample: dict[str, Any], path: Path, line_number: int, errors: list[ValidationMessage]) -> None:
    if "context" not in sample:
        return

    context = sample["context"]
    if not isinstance(context, dict):
        add_error(errors, path, line_number, "`context` must be an object when present.")
        return

    for field in ("title", "description", "parent_comment", "time", "topic"):
        if field in context and not isinstance(context[field], str):
            add_error(errors, path, line_number, f"`context.{field}` must be a string.")

    if "reply_chain" in context and not is_string_list(context["reply_chain"]):
        add_error(errors, path, line_number, "`context.reply_chain` must be an array of strings.")


def validate_reasoning(sample: dict[str, Any], path: Path, line_number: int, errors: list[ValidationMessage]) -> None:
    reasoning = sample.get("reasoning")
    if not isinstance(reasoning, dict):
        add_error(errors, path, line_number, "`reasoning` must be an object.")
        return

    missing = sorted(REQUIRED_REASONING_FIELDS - reasoning.keys())
    if missing:
        add_error(errors, path, line_number, f"`reasoning` is missing required fields: {', '.join(missing)}.")

    for field in REASONING_LIST_FIELDS:
        if field in reasoning and not is_string_list(reasoning[field]):
            add_error(errors, path, line_number, f"`reasoning.{field}` must be an array of strings.")

    counter_evidence = reasoning.get("counter_evidence")
    if isinstance(counter_evidence, list) and not counter_evidence:
        add_error(errors, path, line_number, "`reasoning.counter_evidence` must contain at least one item.")

    final_rationale = reasoning.get("final_rationale")
    if "final_rationale" in reasoning and not is_non_empty_string(final_rationale):
        add_error(errors, path, line_number, "`reasoning.final_rationale` must be a non-empty string.")


def validate_sample(sample: Any, path: Path, line_number: int, seen_ids: set[str], errors: list[ValidationMessage]) -> None:
    if not isinstance(sample, dict):
        add_error(errors, path, line_number, "Line must contain a JSON object.")
        return

    missing = sorted(REQUIRED_FIELDS - sample.keys())
    if missing:
        add_error(errors, path, line_number, f"Missing required fields: {', '.join(missing)}.")

    sample_id = sample.get("id")
    if "id" in sample:
        if not is_non_empty_string(sample_id):
            add_error(errors, path, line_number, "`id` must be a non-empty string.")
        elif sample_id in seen_ids:
            add_error(errors, path, line_number, f"Duplicate id: {sample_id}.")
        else:
            seen_ids.add(sample_id)

    if "text" in sample and not is_non_empty_string(sample["text"]):
        add_error(errors, path, line_number, "`text` must be a non-empty string.")

    if "encoding_primary" in sample and not is_non_empty_string(sample["encoding_primary"]):
        add_error(errors, path, line_number, "`encoding_primary` must be a non-empty string.")

    for field in STRING_FIELDS:
        if field in sample and not isinstance(sample[field], str):
            add_error(errors, path, line_number, f"`{field}` must be a string.")

    for field in BOOLEAN_FIELDS:
        if field in sample and not isinstance(sample[field], bool):
            add_error(errors, path, line_number, f"`{field}` must be a boolean.")

    for field in LIST_OF_STRING_FIELDS:
        if field in sample and not is_string_list(sample[field]):
            add_error(errors, path, line_number, f"`{field}` must be an array of strings.")

    for field, allowed_values in ENUMS.items():
        if field in sample and sample[field] not in allowed_values:
            allowed = ", ".join(sorted(allowed_values))
            add_error(errors, path, line_number, f"`{field}` must be one of: {allowed}.")

    validate_context(sample, path, line_number, errors)
    validate_reasoning(sample, path, line_number, errors)

    if sample.get("risk_level") == "none" and sample.get("encoding_primary") != "none":
        add_error(errors, path, line_number, "`risk_level=none` should use `encoding_primary=none`.")

    if sample.get("hard_negative") is True and sample.get("risk_level") not in {"none", "low"}:
        add_error(errors, path, line_number, "`hard_negative=true` should only be used with `risk_level` none or low.")


def validate_jsonl(path: Path) -> list[ValidationMessage]:
    errors: list[ValidationMessage] = []
    seen_ids: set[str] = set()

    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue

            try:
                sample = json.loads(line)
            except json.JSONDecodeError as exc:
                add_error(errors, path, line_number, f"Invalid JSON: {exc.msg}.")
                continue

            validate_sample(sample, path, line_number, seen_ids, errors)

    return errors


def collect_jsonl_files(inputs: list[Path]) -> list[Path]:
    files: list[Path] = []

    for input_path in inputs:
        if input_path.is_dir():
            files.extend(sorted(input_path.rglob("*.jsonl")))
        elif input_path.is_file():
            files.append(input_path)
        else:
            raise FileNotFoundError(f"Path does not exist: {input_path}")

    return files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate risk-reasoning JSONL files against the project annotation rules."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="JSONL files or directories containing JSONL files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    files = collect_jsonl_files(args.paths)

    if not files:
        print("No JSONL files found.")
        return 1

    all_errors: list[ValidationMessage] = []
    for file_path in files:
        all_errors.extend(validate_jsonl(file_path))

    if all_errors:
        print(f"Validation failed: {len(all_errors)} error(s) found.")
        for error in all_errors:
            print(f"{error.path}:{error.line_number}: {error.message}")
        return 1

    print(f"Validation passed: {len(files)} file(s) checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
