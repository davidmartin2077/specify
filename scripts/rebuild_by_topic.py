#!/usr/bin/env python3
"""Rebuild data/by_topic/ from combined_candidates.jsonl with multi-topic support.

Each sample can belong to multiple topics. The sample's `context.topics` list
determines which topic files it appears in. Samples with no topics go to `未分类.jsonl`.
"""
from __future__ import annotations

import json
import os
import shutil
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "data/processed/combined_candidates.jsonl"
BY_TOPIC = ROOT / "data/by_topic"


def main() -> int:
    # Load all samples
    with open(CANDIDATES, encoding="utf-8") as f:
        samples = [json.loads(line) for line in f if line.strip()]

    # Clear existing by_topic
    if BY_TOPIC.exists():
        for fname in os.listdir(BY_TOPIC):
            if fname.endswith(".jsonl"):
                os.remove(BY_TOPIC / fname)
    else:
        BY_TOPIC.mkdir(parents=True, exist_ok=True)

    # Group by topics
    topic_buckets: dict[str, list[dict]] = {}
    unclassified = []

    for s in samples:
        ctx = s.get("context", {})
        topics = ctx.get("topics", []) if isinstance(ctx, dict) else []

        if not topics:
            unclassified.append(s)
            continue

        for topic in topics:
            # Sanitize topic name for filesystem
            safe_name = topic.replace("/", "_").replace("\\", "_")
            if safe_name not in topic_buckets:
                topic_buckets[safe_name] = []
            topic_buckets[safe_name].append(s)

    # Write topic files
    total_written = 0
    for topic, bucket in sorted(topic_buckets.items()):
        fname = f"{topic}.jsonl"
        with open(BY_TOPIC / fname, "w", encoding="utf-8") as f:
            for s in bucket:
                f.write(json.dumps(s, ensure_ascii=False) + "\n")
        total_written += len(bucket)

    # Write unclassified
    if unclassified:
        with open(BY_TOPIC / "未分类.jsonl", "w", encoding="utf-8") as f:
            for s in unclassified:
                f.write(json.dumps(s, ensure_ascii=False) + "\n")

    # Stats
    print(f"Total samples: {len(samples)}")
    print(f"Total entries written (with duplication): {total_written}")
    print(f"Duplication factor: {total_written / len(samples):.2f}x")
    print(f"Topics: {len(topic_buckets)}")
    print(f"Unclassified: {len(unclassified)}")

    # Topic size distribution
    sizes = Counter({t: len(b) for t, b in topic_buckets.items()})
    print(f"\nSingles (1 sample): {sum(1 for c in sizes.values() if c == 1)}")
    print(f"Small (2-5): {sum(1 for c in sizes.values() if 2 <= c <= 5)}")
    print(f"Medium (6-20): {sum(1 for c in sizes.values() if 6 <= c <= 20)}")
    print(f"Large (21+): {sum(1 for c in sizes.values() if c >= 21)}")

    # List singles
    singles = [(t, c) for t, c in sizes.items() if c == 1]
    if singles:
        print(f"\nSingle-sample topics:")
        for t, c in sorted(singles):
            print(f"  {t}: {c}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
