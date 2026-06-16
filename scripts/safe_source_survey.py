#!/usr/bin/env python3
"""Create a safe survey of source files without printing raw risky lexicon terms."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_JSON = ROOT / "data/processed/source_survey_report.json"
OUTPUT_MD = ROOT / "docs/source_survey_report.md"

CANONICAL = ROOT / "data/processed/combined_candidates.jsonl"
SFT = ROOT / "data/processed/sft/sft_candidates.jsonl"
SPLITS = ROOT / "data/processed/splits"
RAW = ROOT / "data/raw"
LEXICON = ROOT / "data/raw/third_party/Sensitive-lexicon/Vocabulary"
SLANG_FILES = [
    ROOT / "中国大陆网络用语列表整理.md",
    ROOT / "中国大陆网络用语列表整理_v2.md",
    ROOT / "docs/中国大陆网络用语列表_维基学院完整版.md",
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


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


def count_field(rows: list[dict[str, Any]], field: str) -> dict[str, int]:
    return dict(sorted(Counter(str(row.get(field, "")) for row in rows).items()))


def parse_review_source(notes: Any) -> str:
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


def jsonl_summary(path: Path) -> dict[str, Any]:
    rows = load_jsonl(path)
    summary: dict[str, Any] = {
        "path": display(path),
        "sha256": sha256_file(path),
        "rows": len(rows),
    }
    if rows and "risk_level" in rows[0]:
        summary.update(
            {
                "risk_level": count_field(rows, "risk_level"),
                "encoding_primary": count_field(rows, "encoding_primary"),
                "source_type": count_field(rows, "source_type"),
                "quality_status": count_field(rows, "quality_status"),
                "hard_negative": sum(bool(row.get("hard_negative")) for row in rows),
                "needs_context": sum(bool(row.get("needs_context")) for row in rows),
                "review_source": dict(sorted(Counter(parse_review_source(row.get("review_notes")) for row in rows).items())),
            }
        )
    if rows and "metadata" in rows[0]:
        metadata = [row.get("metadata", {}) for row in rows if isinstance(row.get("metadata"), dict)]
        summary.update(
            {
                "metadata_risk_level": dict(sorted(Counter(str(row.get("risk_level", "")) for row in metadata).items())),
                "metadata_encoding_primary": dict(sorted(Counter(str(row.get("encoding_primary", "")) for row in metadata).items())),
            }
        )
    return summary


def text_file_safe_summary(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    lines = raw.splitlines()
    nonempty = [line.strip() for line in lines if line.strip()]
    lengths = [len(line) for line in nonempty]
    bullet_like = sum(1 for line in nonempty if line.startswith(("-", "*", "|")))
    table_rows = sum(1 for line in nonempty if line.startswith("|") and line.endswith("|"))
    return {
        "path": display(path),
        "sha256": sha256_file(path),
        "bytes": path.stat().st_size,
        "lines": len(lines),
        "nonempty_lines": len(nonempty),
        "bullet_or_table_like_lines": bullet_like,
        "markdown_table_rows": table_rows,
        "length_min": min(lengths) if lengths else 0,
        "length_p50": sorted(lengths)[len(lengths) // 2] if lengths else 0,
        "length_max": max(lengths) if lengths else 0,
    }


def lexicon_file_summary(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    terms = [line.strip() for line in raw.splitlines() if line.strip()]
    lengths = [len(term) for term in terms]
    asciiish = sum(1 for term in terms if re.fullmatch(r"[\x00-\x7f]+", term))
    with_digit = sum(1 for term in terms if any(ch.isdigit() for ch in term))
    with_latin = sum(1 for term in terms if re.search(r"[A-Za-z]", term))
    with_symbol = sum(1 for term in terms if re.search(r"[^\w\u4e00-\u9fff]", term))
    return {
        "path": display(path),
        "sha256": sha256_file(path),
        "terms": len(terms),
        "length_min": min(lengths) if lengths else 0,
        "length_p50": sorted(lengths)[len(lengths) // 2] if lengths else 0,
        "length_max": max(lengths) if lengths else 0,
        "ascii_only_terms": asciiish,
        "terms_with_digits": with_digit,
        "terms_with_latin": with_latin,
        "terms_with_symbols": with_symbol,
    }


def render_md(report: dict[str, Any]) -> str:
    canonical = report["canonical_dataset"]
    lines = [
        "# Source Survey Report",
        "",
        "This report is generated without printing raw sensitive lexicon terms. It is safe to paste into a strict downstream API.",
        "",
        "## Canonical Dataset",
        "",
        f"- Rows: {canonical['rows']}",
        f"- SHA256: `{canonical['sha256']}`",
        f"- Risk: `{canonical.get('risk_level', {})}`",
        f"- Source type: `{canonical.get('source_type', {})}`",
        f"- Hard negative: {canonical.get('hard_negative', 0)}",
        f"- Needs context: {canonical.get('needs_context', 0)}",
        "",
        "## Derived Artifacts",
        "",
        f"- SFT rows: {report['sft_dataset']['rows']}",
        f"- Split rows: train {report['splits']['train']['rows']} / validation {report['splits']['validation']['rows']} / test {report['splits']['test']['rows']}",
        "",
        "## Raw Batches",
        "",
    ]
    for item in report["raw_batches"]:
        lines.append(f"- `{item['path']}`: {item['rows']} rows")
    lines.extend(["", "## Sensitive Lexicon Files", ""])
    for item in report["third_party_lexicons"]:
        lines.append(
            f"- `{item['path']}`: {item['terms']} terms, length p50={item['length_p50']}, "
            f"digits={item['terms_with_digits']}, latin={item['terms_with_latin']}, symbols={item['terms_with_symbols']}"
        )
    lines.extend(["", "## Slang Reference Files", ""])
    for item in report["slang_references"]:
        lines.append(
            f"- `{item['path']}`: {item['nonempty_lines']} nonempty lines, "
            f"table rows={item['markdown_table_rows']}, sha256=`{item['sha256']}`"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    raw_batches = sorted(path for path in RAW.glob("*.jsonl") if path.is_file())
    lexicon_files = sorted(path for path in LEXICON.glob("*.txt") if path.is_file()) if LEXICON.exists() else []
    report = {
        "note": "Raw lexicon terms are intentionally omitted to avoid triggering downstream content filters.",
        "canonical_dataset": jsonl_summary(CANONICAL),
        "sft_dataset": jsonl_summary(SFT),
        "splits": {
            split: jsonl_summary(SPLITS / f"{split}.jsonl")
            for split in ("train", "validation", "test")
        },
        "raw_batches": [jsonl_summary(path) for path in raw_batches],
        "third_party_lexicons": [lexicon_file_summary(path) for path in lexicon_files],
        "slang_references": [text_file_safe_summary(path) for path in SLANG_FILES if path.exists()],
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(render_md(report), encoding="utf-8")
    print(f"Wrote {display(OUTPUT_JSON)}")
    print(f"Wrote {display(OUTPUT_MD)}")
    print(f"Canonical rows: {report['canonical_dataset']['rows']}")
    print(f"Sensitive lexicon files summarized: {len(report['third_party_lexicons'])}")
    print("Raw risky terms were not printed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
