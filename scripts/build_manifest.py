#!/usr/bin/env python3
"""Build a dataset manifest for reproducible training artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANDIDATES = ROOT / "data/processed/combined_candidates.jsonl"
DEFAULT_SFT = ROOT / "data/processed/sft/sft_candidates.jsonl"
DEFAULT_SPLITS_DIR = ROOT / "data/processed/splits"
DEFAULT_COVERAGE = ROOT / "data/processed/risk_coverage_report.json"
DEFAULT_PHASE3_PLAN = ROOT / "data/processed/phase3_sampling_plan.json"
DEFAULT_OUTPUT = ROOT / "data/processed/manifest.json"

FIELDS_TO_COMPARE = (
    "risk_level",
    "encoding_primary",
    "needs_context",
    "ambiguity",
    "evidence_strength",
    "hard_negative",
    "quality_status",
)


def display_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(ROOT))
    except ValueError:
        return str(path)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_number}: expected JSON object")
            rows.append(value)
    return rows


def count_values(rows: list[dict[str, Any]], field: str) -> dict[str, int]:
    return dict(sorted(Counter(str(row.get(field, "")) for row in rows).items()))


def parse_source(notes: Any) -> str:
    if not isinstance(notes, str):
        return "unknown"
    for part in notes.split(";"):
        part = part.strip()
        if "=" not in part:
            continue
        key, value = part.split("=", 1)
        if key.strip() in {"source", "batch"}:
            return value.strip()
    return "unknown"


def candidate_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "count": len(rows),
        "risk_level": count_values(rows, "risk_level"),
        "source_type": count_values(rows, "source_type"),
        "quality_status": count_values(rows, "quality_status"),
        "encoding_primary": count_values(rows, "encoding_primary"),
        "evidence_strength": count_values(rows, "evidence_strength"),
        "ambiguity": count_values(rows, "ambiguity"),
        "hard_negative": sum(bool(row.get("hard_negative")) for row in rows),
        "needs_context": sum(bool(row.get("needs_context")) for row in rows),
        "review_source": dict(sorted(Counter(parse_source(row.get("review_notes")) for row in rows).items())),
    }


def sft_summary(path: Path, candidates_by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    records = load_jsonl(path)
    ids: list[str] = []
    mismatches: Counter[str] = Counter()
    examples: list[dict[str, Any]] = []

    for record in records:
        metadata = record.get("metadata", {})
        if not isinstance(metadata, dict):
            mismatches["metadata"] += 1
            continue
        sample_id = str(metadata.get("id", ""))
        ids.append(sample_id)
        candidate = candidates_by_id.get(sample_id)
        if candidate is None:
            mismatches["extra_in_sft"] += 1
            continue
        for field in FIELDS_TO_COMPARE:
            if candidate.get(field) != metadata.get(field):
                mismatches[field] += 1
                if len(examples) < 10:
                    examples.append(
                        {
                            "id": sample_id,
                            "field": field,
                            "candidate": candidate.get(field),
                            "sft_metadata": metadata.get(field),
                        }
                    )

    missing_ids = sorted(set(candidates_by_id) - set(ids))
    duplicate_ids = sorted(sample_id for sample_id, count in Counter(ids).items() if count > 1)

    return {
        "path": display_path(path),
        "sha256": sha256_file(path),
        "count": len(records),
        "missing_candidate_ids": missing_ids[:20],
        "missing_candidate_count": len(missing_ids),
        "duplicate_id_count": len(duplicate_ids),
        "duplicate_ids": duplicate_ids[:20],
        "metadata_mismatch_counts": dict(sorted(mismatches.items())),
        "metadata_mismatch_examples": examples,
        "is_synced_with_candidates": not missing_ids and not duplicate_ids and not mismatches,
    }


def split_summary(splits_dir: Path, candidates_by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    total = 0
    mismatched_rows = 0

    for split in ("train", "validation", "test"):
        path = splits_dir / f"{split}.jsonl"
        rows = load_jsonl(path)
        total += len(rows)
        field_mismatches: Counter[str] = Counter()
        missing = 0
        for row in rows:
            candidate = candidates_by_id.get(str(row.get("id", "")))
            if candidate is None:
                missing += 1
                continue
            row_mismatched = False
            for field in FIELDS_TO_COMPARE:
                if candidate.get(field) != row.get(field):
                    field_mismatches[field] += 1
                    row_mismatched = True
            if row_mismatched:
                mismatched_rows += 1
        result[split] = {
            "path": display_path(path),
            "sha256": sha256_file(path),
            "count": len(rows),
            "risk_level": count_values(rows, "risk_level"),
            "quality_status": count_values(rows, "quality_status"),
            "missing_from_candidates": missing,
            "field_mismatch_counts": dict(sorted(field_mismatches.items())),
        }

    split_report = splits_dir / "split_report.json"
    if split_report.exists():
        report = json.loads(split_report.read_text(encoding="utf-8"))
        result["split_report"] = {
            "path": display_path(split_report),
            "sha256": sha256_file(split_report),
            "input_count": report.get("input_count"),
            "group_count": report.get("group_count"),
            "leaked_group_count": len(report.get("leaked_groups", [])),
        }

    result["total_count"] = total
    result["mismatched_row_count"] = mismatched_rows
    result["is_synced_with_candidates"] = total == len(candidates_by_id) and mismatched_rows == 0
    return result


def artifact_info(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"path": display_path(path), "exists": False}
    return {
        "path": display_path(path),
        "exists": True,
        "sha256": sha256_file(path),
        "bytes": path.stat().st_size,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build manifest for dataset and derived training artifacts.")
    parser.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--sft", type=Path, default=DEFAULT_SFT)
    parser.add_argument("--splits-dir", type=Path, default=DEFAULT_SPLITS_DIR)
    parser.add_argument("--coverage", type=Path, default=DEFAULT_COVERAGE)
    parser.add_argument("--phase3-plan", type=Path, default=DEFAULT_PHASE3_PLAN)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    candidates = load_jsonl(args.candidates)
    candidates_by_id = {str(row.get("id", "")): row for row in candidates}
    duplicate_candidate_ids = [
        sample_id for sample_id, count in Counter(str(row.get("id", "")) for row in candidates).items() if count > 1
    ]

    manifest = {
        "dataset_name": "semantic_risk_reasoning",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": {
            "path": display_path(args.candidates),
            "sha256": sha256_file(args.candidates),
            "duplicate_id_count": len(duplicate_candidate_ids),
            "duplicate_ids": sorted(duplicate_candidate_ids)[:20],
            "summary": candidate_summary(candidates),
        },
        "artifacts": {
            "sft": sft_summary(args.sft, candidates_by_id),
            "splits": split_summary(args.splits_dir, candidates_by_id),
            "coverage_report": artifact_info(args.coverage),
            "phase3_sampling_plan": artifact_info(args.phase3_plan),
        },
        "training_guardrail": {
            "canonical_source": display_path(args.candidates),
            "do_not_train_on_stale_sft": True,
            "sft_synced_with_canonical_source": False,
            "splits_synced_with_canonical_source": False,
        },
    }

    manifest["training_guardrail"]["sft_synced_with_canonical_source"] = bool(
        manifest["artifacts"]["sft"]["is_synced_with_candidates"]
    )
    manifest["training_guardrail"]["splits_synced_with_canonical_source"] = bool(
        manifest["artifacts"]["splits"]["is_synced_with_candidates"]
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote manifest to {display_path(args.output)}")
    print(f"Samples: {len(candidates)}")
    print(f"SFT synced: {manifest['training_guardrail']['sft_synced_with_canonical_source']}")
    print(f"Splits synced: {manifest['training_guardrail']['splits_synced_with_canonical_source']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
