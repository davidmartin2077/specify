#!/usr/bin/env python3
"""Split annotated candidates while keeping related template groups together."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


DEFAULT_RATIOS = (0.8, 0.1, 0.1)
SPLITS = ("train", "validation", "test")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {exc.msg}") from exc
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


def parse_review_notes(notes: Any) -> dict[str, str]:
    parsed: dict[str, str] = {}
    if not isinstance(notes, str):
        return parsed

    for raw_part in notes.split(";"):
        part = raw_part.strip()
        if not part or "=" not in part:
            continue
        key, value = part.split("=", 1)
        parsed[key.strip()] = value.strip()
    return parsed


def id_source(sample_id: str) -> str:
    if sample_id.startswith("GROK_"):
        return "grok"
    if sample_id.startswith("USER_"):
        return "user"
    if sample_id.startswith("MEME_EXPAND_"):
        return "meme_expansion"
    if sample_id.startswith("GEMINI_EXPAND_"):
        return "gemini_expansion"
    if sample_id.startswith("LEXICON_SEED_"):
        return "sensitive_lexicon_seed"
    if sample_id.startswith("PHASE2_SEED_"):
        return "phase2_seed"
    if sample_id.startswith("PHASE3_W1_"):
        return "phase3_first_wave"
    return "unknown"


def source_for(sample: dict[str, Any], notes: dict[str, str]) -> str:
    return notes.get("source") or id_source(str(sample.get("id", "")))


def group_key_for(sample: dict[str, Any]) -> str:
    """Return a stable leakage-prevention group.

    Explicit meme clusters are grouped across sources, because MEME and GEMINI
    expansions can share the same semantic template family. Lexicon seed rows
    are grouped by category. Phase2 and phase3 generated rows use their
    explicit template metadata so contrast/template siblings cannot straddle
    train, validation, and test. Rows without an explicit cluster fall back to
    source id, which keeps manual examples available for balancing without
    inventing unverified semantic clusters.
    """

    sample_id = str(sample.get("id", ""))
    notes = parse_review_notes(sample.get("review_notes", ""))
    if notes.get("meme_cluster"):
        return f"meme_cluster:{notes['meme_cluster']}"
    source = source_for(sample, notes)
    if source == "sensitive_lexicon_seed":
        return f"lexicon_category:{notes.get('category', 'unknown')}"
    if source == "phase2_seed" and notes.get("cluster"):
        return f"phase2_template:{notes.get('axis', 'unknown')}:{notes['cluster']}"
    if source == "phase3_first_wave" and notes.get("cluster"):
        return (
            f"phase3_template:{notes.get('category', 'unknown')}:"
            f"{notes['cluster']}:{notes.get('contrast_mode', 'unknown')}"
        )
    if notes.get("semantic_cluster"):
        return f"semantic_cluster:{notes['semantic_cluster']}"
    return f"singleton:{sample_id}"


def stable_group_order(groups: dict[str, list[dict[str, Any]]], seed: int) -> list[tuple[str, list[dict[str, Any]]]]:
    def order_key(item: tuple[str, list[dict[str, Any]]]) -> tuple[int, str]:
        key, rows = item
        digest = hashlib.sha256(f"{seed}:{key}".encode("utf-8")).hexdigest()
        return (-len(rows), digest)

    return sorted(groups.items(), key=order_key)


def split_groups(
    groups: dict[str, list[dict[str, Any]]],
    ratios: tuple[float, float, float],
    seed: int,
) -> dict[str, list[dict[str, Any]]]:
    total = sum(len(rows) for rows in groups.values())
    targets = {split: total * ratio for split, ratio in zip(SPLITS, ratios)}
    assigned: dict[str, list[dict[str, Any]]] = {split: [] for split in SPLITS}

    for group_key, rows in stable_group_order(groups, seed):
        candidates = []
        for split in SPLITS:
            projected = len(assigned[split]) + len(rows)
            fill_ratio = projected / targets[split] if targets[split] else float("inf")
            candidates.append((fill_ratio, len(assigned[split]), split))
        _, _, chosen_split = min(candidates)
        for row in rows:
            copied = dict(row)
            copied["split"] = chosen_split
            assigned[chosen_split].append(copied)

    return assigned


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    risk = Counter(row.get("risk_level", "unknown") for row in rows)
    parsed_notes = [parse_review_notes(row.get("review_notes", "")) for row in rows]
    source = Counter(source_for(row, notes) for row, notes in zip(rows, parsed_notes))
    groups = Counter(group_key_for(row) for row in rows)
    phase3_category = Counter(
        notes["category"]
        for row, notes in zip(rows, parsed_notes)
        if source_for(row, notes) == "phase3_first_wave" and notes.get("category")
    )
    phase3_contrast_mode = Counter(
        notes["contrast_mode"]
        for row, notes in zip(rows, parsed_notes)
        if source_for(row, notes) == "phase3_first_wave" and notes.get("contrast_mode")
    )
    return {
        "count": len(rows),
        "risk_level": dict(sorted(risk.items())),
        "source": dict(sorted(source.items())),
        "hard_negative": sum(bool(row.get("hard_negative")) for row in rows),
        "context_required": sum(bool(row.get("context_required")) for row in rows),
        "group_count": len(groups),
        "largest_groups": groups.most_common(10),
        "phase3_category": dict(sorted(phase3_category.items())),
        "phase3_contrast_mode": dict(sorted(phase3_contrast_mode.items())),
    }


def build_report(
    assigned: dict[str, list[dict[str, Any]]],
    groups: dict[str, list[dict[str, Any]]],
    ratios: tuple[float, float, float],
    seed: int,
) -> dict[str, Any]:
    group_to_split: dict[str, str] = {}
    for split, rows in assigned.items():
        for row in rows:
            group_to_split[group_key_for(row)] = split

    leaked = []
    seen: dict[str, set[str]] = defaultdict(set)
    for split, rows in assigned.items():
        for row in rows:
            seen[group_key_for(row)].add(split)
    for key, splits in sorted(seen.items()):
        if len(splits) > 1:
            leaked.append({"group": key, "splits": sorted(splits)})

    return {
        "input_count": sum(len(rows) for rows in assigned.values()),
        "ratios": dict(zip(SPLITS, ratios)),
        "seed": seed,
        "group_count": len(groups),
        "leaked_groups": leaked,
        "splits": {split: summarize(rows) for split, rows in assigned.items()},
        "group_assignments": dict(sorted(group_to_split.items())),
    }


def parse_ratios(value: str) -> tuple[float, float, float]:
    parts = [float(part) for part in value.split(",")]
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("ratios must contain three comma-separated numbers")
    total = sum(parts)
    if total <= 0:
        raise argparse.ArgumentTypeError("ratios must sum to a positive number")
    return tuple(part / total for part in parts)  # type: ignore[return-value]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create train/validation/test splits without leaking explicit semantic/template groups."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/processed/combined_candidates.jsonl"),
        help="Annotated JSONL dataset to split.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/processed/splits"),
        help="Directory for split JSONL/JSON files and split_report.json.",
    )
    parser.add_argument(
        "--ratios",
        type=parse_ratios,
        default=DEFAULT_RATIOS,
        help="Comma-separated train,validation,test ratios. Default: 0.8,0.1,0.1.",
    )
    parser.add_argument("--seed", type=int, default=20260604, help="Stable seed for group ordering.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    rows = load_jsonl(args.input)
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[group_key_for(row)].append(row)

    assigned = split_groups(groups, args.ratios, args.seed)
    for split in SPLITS:
        rows_for_split = assigned[split]
        write_jsonl(rows_for_split, args.output_dir / f"{split}.jsonl")
        write_json(rows_for_split, args.output_dir / f"{split}.json")

    report = build_report(assigned, groups, args.ratios, args.seed)
    with (args.output_dir / "split_report.json").open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)

    print(f"Wrote splits to {args.output_dir}")
    for split in SPLITS:
        summary = report["splits"][split]
        print(
            f"{split}: {summary['count']} rows, "
            f"{summary['group_count']} groups, "
            f"risk={summary['risk_level']}"
        )
    if report["leaked_groups"]:
        print(f"WARNING: {len(report['leaked_groups'])} groups appear in multiple splits")
    else:
        print("No grouped leakage detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
