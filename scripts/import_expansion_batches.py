#!/usr/bin/env python3
"""Preview or apply approved raw expansion batches to processed candidates.

By default this script writes an independent merge preview. Pass --apply only
after the preview has been reviewed. Existing expansion ids are removed before
re-adding current raw batches, making the merge idempotent.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE = ROOT / "data/processed/combined_candidates.jsonl"
DEFAULT_BATCHES = [
    ROOT / "data/raw/phase2_seed_candidates.jsonl",
    ROOT / "data/raw/phase3_first_wave_candidates.jsonl",
]
PREVIEW_JSONL = ROOT / "data/processed/combined_candidates_expansion_preview.jsonl"
PREVIEW_JSON = ROOT / "data/processed/combined_candidates_expansion_preview.json"
PROCESSED_JSONL = ROOT / "data/processed/combined_candidates.jsonl"
PROCESSED_JSON = ROOT / "data/processed/combined_candidates.json"
MANAGED_PREFIXES = ("PHASE2_SEED_", "PHASE3_W1_")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_number}: expected object")
            rows.append(value)
    return rows


def write_jsonl(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_json(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(rows, handle, ensure_ascii=False, indent=2)


def prepare_batch_row(row: dict[str, Any]) -> dict[str, Any]:
    result = dict(row)
    notes = str(result.get("review_notes", ""))
    notes = notes.replace("; not_merged", "; merged_processed").replace("not_merged", "merged_processed")
    result["review_notes"] = notes
    return result


def build_merge(base: list[dict[str, Any]], batches: list[list[dict[str, Any]]]) -> list[dict[str, Any]]:
    retained = [
        row for row in base if not str(row.get("id", "")).startswith(MANAGED_PREFIXES)
    ]
    additions = [prepare_batch_row(row) for batch in batches for row in batch]
    merged = retained + additions
    ids = [str(row.get("id", "")) for row in merged]
    duplicates = [item for item, count in Counter(ids).items() if count > 1]
    if duplicates:
        raise ValueError(f"Duplicate ids after merge: {duplicates[:10]}")
    return merged


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Preview or apply phase2/phase3 expansion batches.")
    parser.add_argument("--base", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--batch", type=Path, action="append", dest="batches")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply the merge to data/processed/combined_candidates.* instead of preview files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    batch_paths = args.batches or DEFAULT_BATCHES
    base = load_jsonl(args.base)
    batches = [load_jsonl(path) for path in batch_paths]
    merged = build_merge(base, batches)

    if args.apply:
        output_jsonl = PROCESSED_JSONL
        output_json = PROCESSED_JSON
    else:
        output_jsonl = PREVIEW_JSONL
        output_json = PREVIEW_JSON

    write_jsonl(merged, output_jsonl)
    write_json(merged, output_json)
    print(f"Base rows: {len(base)}")
    print(f"Batch rows: {sum(len(batch) for batch in batches)}")
    print(f"Merged rows: {len(merged)}")
    print(f"Mode: {'apply' if args.apply else 'preview'}")
    print(f"Wrote {output_jsonl}")
    print(f"Wrote {output_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
