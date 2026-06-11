#!/usr/bin/env python3
"""Replace oldest/worst synthetic samples with new natural-voice batches."""

import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "data/processed/combined_candidates.jsonl"
BATCHES = [
    ROOT / "data/raw/batch1_natural_replacements.jsonl",
    ROOT / "data/raw/batch2_natural_replacements.jsonl",
    ROOT / "data/raw/batch3_natural_replacements.jsonl",
    ROOT / "data/raw/batch4_natural_replacements.jsonl",
    ROOT / "data/raw/batch5_gap_fill.jsonl",
]

REPLACE_PRIORITY = [
    "grok",
    "meme_expansion",
    "gemini_expansion",
    "phase2_seed",
    "sensitive_lexicon_seed",
    "phase3_first_wave",
    "phase3_second_wave",
    "user",
]


def parse_source(notes):
    if isinstance(notes, str):
        for part in notes.split(";"):
            if "source=" in part:
                return part.split("source=")[1].split(";")[0].strip()
    return "unknown"


def main():
    # Load current
    with MAIN.open(encoding="utf-8") as f:
        current = [json.loads(line) for line in f if line.strip()]

    # Load replacements
    replacements = []
    for batch_path in BATCHES:
        if not batch_path.exists():
            continue
        with batch_path.open(encoding="utf-8") as f:
            replacements.extend(json.loads(line) for line in f if line.strip())

    print(f"Current samples: {len(current)}")
    print(f"New batch samples: {len(replacements)}")

    # Separate: real, existing-batch, old-synthetic
    def is_batch(sample):
        notes = sample.get("review_notes", "")
        return isinstance(notes, str) and "source=batch" in notes

    batch_existing = [s for s in current if is_batch(s)]
    real = [s for s in current if s.get("source_type") == "real" and not is_batch(s)]
    synthetic = [s for s in current if s.get("source_type") != "real" and not is_batch(s)]

    print(f"  Real: {len(real)}, Existing batch: {len(batch_existing)}, Old synthetic: {len(synthetic)}")

    # Sort old synthetic by replacement priority (worst first)
    def priority(sample):
        src = parse_source(sample.get("review_notes", ""))
        try:
            return REPLACE_PRIORITY.index(src)
        except ValueError:
            return len(REPLACE_PRIORITY)

    synthetic.sort(key=priority)

    # Existing batch samples free up slots: they get replaced by new batch samples.
    # Additional old synthetics to remove = len(replacements) - len(batch_existing)
    extra_to_remove = max(0, len(replacements) - len(batch_existing))
    extra_to_remove = min(extra_to_remove, len(synthetic))

    removed = synthetic[:extra_to_remove]
    kept_synthetic = synthetic[extra_to_remove:]

    removed_sources = Counter(parse_source(s.get("review_notes", "")) for s in removed)
    print(f"\nReplacing {len(batch_existing)} existing batch + removing {len(removed)} old synthetic:")
    for src, count in removed_sources.most_common():
        print(f"  {src}: {count}")

    # Build: real + kept_old_synthetic + new_batch
    new_combined = real + kept_synthetic + replacements

    # Risk distribution check
    risk_dist = Counter(s["risk_level"] for s in new_combined)
    print(f"\nNew combined dataset: {len(new_combined)} samples")
    print(f"Risk: {dict(risk_dist)}")
    print(f"Hard negative: {sum(1 for s in new_combined if s.get('hard_negative'))}")

    # Write
    with MAIN.open("w", encoding="utf-8") as f:
        for rec in new_combined:
            f.write(json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n")

    print(f"Wrote {len(new_combined)} samples to {MAIN}")


if __name__ == "__main__":
    main()
