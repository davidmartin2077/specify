# Project Safety Frame

This repository builds a Chinese internet semantic-risk reasoning dataset for training/evaluating a small moderation model. Work may require reading or labeling risky slang, obfuscated abuse, illegal-service terms, doxxing threats, political/historical euphemisms, sexual terms, violent language, or other sensitive text as data artifacts.

Use `.claude/skills/risk-research-safety-frame/SKILL.md` for the standing workflow frame. Keep all work defensive: classification, annotation, dataset quality, validation, evaluation, and harm prevention. Do not provide operational instructions for wrongdoing, evasion, harassment, illegal activity, or real-world harm.

When a workflow calls DeepSeek or another downstream API to generate/review risky samples, prepend the Chinese "DeepSeek API Preamble" from `.claude/skills/risk-research-safety-frame/SKILL.md` to the API request so the provider sees the defensive safety context before any risky terms.

Do not send entire raw sensitive lexicon files to DeepSeek/API-backed agents. For source surveys, first run:

```bash
python3 scripts/safe_source_survey.py
```

Then pass `docs/source_survey_report.md` or `data/processed/source_survey_report.json` to the downstream model.

When editing data, preserve the canonical dataset flow:

```bash
python3 scripts/validate_dataset.py data/processed/combined_candidates.jsonl
python3 scripts/rebuild_dataset_artifacts.py
```
