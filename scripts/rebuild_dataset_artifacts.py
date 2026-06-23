#!/usr/bin/env python3
"""Rebuild all derived dataset artifacts from the canonical candidates file."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


STEPS = (
    ("validate canonical dataset", ("scripts/validate_dataset.py", "data/processed/combined_candidates.jsonl")),
    ("build SFT dataset", ("scripts/build_sft_dataset.py",)),
    ("build train/validation/test splits", ("scripts/split_dataset.py",)),
    ("analyze coverage", ("scripts/analyze_risk_coverage.py",)),
    ("rebuild by_topic", ("scripts/rebuild_by_topic.py",)),
    ("build fine-tune datasets", ("scripts/build_fine_tune.py",)),
    ("build manifest", ("scripts/build_manifest.py",)),
)


def main() -> int:
    for label, args in STEPS:
        print(f"\n==> {label}", flush=True)
        completed = subprocess.run((sys.executable, *args), cwd=ROOT)
        if completed.returncode != 0:
            print(f"\nFAILED: {label}", file=sys.stderr)
            return completed.returncode
    print("\nRebuilt derived dataset artifacts successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
