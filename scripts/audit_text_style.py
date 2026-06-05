#!/usr/bin/env python3
"""Audit candidate text style without modifying the dataset."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


REVIEWER_VOICE = (
    "建议人工",
    "建议复核",
    "管理员看",
    "这条评论",
    "审核一下",
    "风险较高",
    "风险较低",
    "证据不足",
    "证据还不够",
    "借代证据",
    "普通解释",
    "需要进一步核验",
    "需确认授权",
    "暂无线索证明",
    "尚无明确",
    "不能自动关联",
    "不能直接认定",
    "不能只看",
    "不一定为了规避",
    "先保留风险召回",
)


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


def parse_source(notes: Any) -> str:
    if not isinstance(notes, str):
        return "unknown"
    for part in notes.split(";"):
        part = part.strip()
        if part.startswith("source="):
            return part.removeprefix("source=")
    return "unknown"


def flags_for(text: str) -> list[str]:
    flags = []
    if len(text) <= 10:
        flags.append("very_short_review_not_auto_rewrite")
    if any(phrase in text for phrase in REVIEWER_VOICE):
        flags.append("reviewer_voice")
    if len(re.findall(r"\s", text)) >= 8:
        flags.append("excessive_spacing")
    if len(text) >= 55:
        flags.append("long_expository_text")
    return flags


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit text style without rewriting records.")
    parser.add_argument("--input", type=Path, default=Path("data/processed/combined_candidates.jsonl"))
    parser.add_argument("--output", type=Path, default=Path("data/raw/combined_candidates_text_style_audit.json"))
    args = parser.parse_args()

    rows = load_jsonl(args.input)
    flagged = []
    counts: Counter[str] = Counter()
    for row in rows:
        flags = flags_for(str(row.get("text", "")))
        counts.update(flags)
        if flags:
            flagged.append(
                {
                    "id": row.get("id", ""),
                    "source": parse_source(row.get("review_notes", "")),
                    "risk_level": row.get("risk_level", ""),
                    "text": row.get("text", ""),
                    "flags": flags,
                }
            )

    report = {
        "input": str(args.input),
        "total": len(rows),
        "flag_counts": dict(sorted(counts.items())),
        "important_note": (
            "very_short_review_not_auto_rewrite is a review cue, not an error; "
            "short internet memes and coded references may need to stay short."
        ),
        "flagged": flagged,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
    print(f"Wrote text-style audit for {len(rows)} rows to {args.output}")
    print(f"Flag counts: {dict(counts)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
