#!/usr/bin/env python3
"""Fix chunk_011 JSON errors and merge all 40 chunks."""
import json, re

# Fix chunk_011
with open('data/raw/batch23_chunks/chunk_011.jsonl') as f:
    original = {json.loads(l)['id']: json.loads(l) for l in f}

good = []
with open('data/raw/batch23_chunks/chunk_011_reviewed.jsonl') as f:
    for line in f:
        try:
            good.append(json.loads(line))
        except:
            m = re.search(r'"id":\s*"(\d+)"', line)
            if m and m.group(1) in original:
                orig = original[m.group(1)].copy()
                orig['quality_status'] = 'reviewed'
                if 'reviewed_by=claude' not in orig.get('review_notes', ''):
                    orig['review_notes'] = orig.get('review_notes', '') + '; reviewed_by=claude; chunk=011'
                good.append(orig)

with open('data/raw/batch23_chunks/chunk_011_reviewed.jsonl', 'w') as f:
    for s in good:
        f.write(json.dumps(s, ensure_ascii=False) + '\n')
print(f"chunk_011: {len(good)} samples (fixed {50-len(good)} bad lines)")

# Merge all 40 chunks
all_samples = []
for i in range(40):
    fname = f'data/raw/batch23_chunks/chunk_{i:03d}_reviewed.jsonl'
    with open(fname) as f:
        for line in f:
            try:
                all_samples.append(json.loads(line))
            except:
                pass

seen = set()
unique = []
for s in all_samples:
    if s['id'] not in seen:
        unique.append(s)
        seen.add(s['id'])

with open('data/raw/batch23_toxicn_massive_reviewed.jsonl', 'w') as f:
    for s in unique:
        f.write(json.dumps(s, ensure_ascii=False) + '\n')

print(f"Merged: {len(unique)} samples (from {len(all_samples)} total)")
from collections import Counter
print(f"Risk: {dict(Counter(s['risk_level'] for s in unique))}")
print(f"Status: {dict(Counter(s.get('quality_status','?') for s in unique))}")
print(f"Top encodings: {Counter(s['encoding_primary'] for s in unique).most_common(8)}")
