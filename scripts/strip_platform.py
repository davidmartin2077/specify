#!/usr/bin/env python3
"""Remove 'platform' field from all annotation JSONL files and SFT output."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ANNOTATION_FILES = [
    "data/processed/combined_candidates.jsonl",
    "data/processed/splits/train.jsonl",
    "data/processed/splits/validation.jsonl",
    "data/processed/splits/test.jsonl",
    "data/raw/batch1_natural_replacements.jsonl",
    "data/raw/batch2_natural_replacements.jsonl",
]

SFT_FILE = "data/processed/sft/sft_candidates.jsonl"


def main():
    for rel in ANNOTATION_FILES:
        path = ROOT / rel
        if not path.exists():
            print(f"SKIP: {rel}")
            continue
        with path.open(encoding="utf-8") as f:
            samples = [json.loads(line) for line in f if line.strip()]
        for s in samples:
            s.pop("platform", None)
            ctx = s.get("context")
            if isinstance(ctx, dict):
                ctx.pop("platform", None)
        with path.open("w", encoding="utf-8") as f:
            for s in samples:
                f.write(json.dumps(s, ensure_ascii=False, separators=(",", ":")) + "\n")
        print(f"OK: {rel} ({len(samples)} samples)")

    # SFT format — strip "平台:" line from input text
    sft_path = ROOT / SFT_FILE
    if sft_path.exists():
        with sft_path.open(encoding="utf-8") as f:
            sft = [json.loads(line) for line in f if line.strip()]
        for s in sft:
            inp = s.get("input", "")
            lines = inp.split("\n")
            if lines and lines[0].startswith("平台:"):
                lines = lines[1:]
            s["input"] = "\n".join(lines)
            # platform was encoded in metadata too
            meta = s.get("metadata")
            if isinstance(meta, dict):
                meta.pop("platform", None)
        with sft_path.open("w", encoding="utf-8") as f:
            for s in sft:
                f.write(json.dumps(s, ensure_ascii=False, separators=(",", ":")) + "\n")
        print(f"OK: {SFT_FILE} ({len(sft)} samples)")


if __name__ == "__main__":
    main()
