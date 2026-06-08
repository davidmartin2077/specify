#!/usr/bin/env python3
"""Compare coverage before and after phase-3 second wave raw candidates."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import analyze_risk_coverage as coverage


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data/processed/combined_candidates.jsonl"
PHASE3_W2 = ROOT / "data/raw/phase3_second_wave_candidates.jsonl"
OUTPUT_JSON = ROOT / "data/processed/phase3_second_wave_coverage_delta.json"
OUTPUT_MD = ROOT / "docs/phase3_second_wave_coverage_delta.md"


def delta(before: dict[str, int], after: dict[str, int]) -> dict[str, int]:
    keys = sorted(set(before) | set(after))
    return {key: after.get(key, 0) - before.get(key, 0) for key in keys}


def build_report() -> dict[str, Any]:
    processed = coverage.load_jsonl(PROCESSED)
    phase3_w2 = coverage.load_jsonl(PHASE3_W2)
    before = coverage.sample_summary(processed)
    after = coverage.sample_summary(processed + phase3_w2)
    return {
        "inputs": {
            "processed": len(processed),
            "phase3_second_wave": len(phase3_w2),
        },
        "before": before,
        "after": after,
        "delta": {
            "count": after["count"] - before["count"],
            "risk_counts": delta(before["risk_counts"], after["risk_counts"]),
            "hard_negative": after["hard_negative"] - before["hard_negative"],
            "category_counts": delta(before["category_counts"], after["category_counts"]),
            "category_hard_negative": delta(
                before["category_hard_negative"], after["category_hard_negative"]
            ),
            "mechanism_group_counts": delta(
                before["mechanism_group_counts"], after["mechanism_group_counts"]
            ),
        },
    }


def render_markdown(report: dict[str, Any]) -> str:
    before = report["before"]
    after = report["after"]
    change = report["delta"]
    lines = [
        "# Phase3 第二波覆盖增益报告",
        "",
        "## 总体变化",
        "",
        f"- 候选池：{before['count']} -> {after['count']}（+{change['count']}）",
        f"- hard negative：{before['hard_negative']} -> {after['hard_negative']}（+{change['hard_negative']}）",
        "",
        "## 风险分布变化",
        "",
        "| 风险等级 | 加入前 | 加入后 | 增量 |",
        "|---|---:|---:|---:|",
    ]
    for risk in ("high", "medium", "low", "none"):
        lines.append(
            f"| {risk} | {before['risk_counts'].get(risk, 0)} | "
            f"{after['risk_counts'].get(risk, 0)} | +{change['risk_counts'].get(risk, 0)} |"
        )
    lines.extend(
        [
            "",
            "## 类别覆盖变化",
            "",
            "| 类别 | 加入前 | 加入后 | 增量 | hard negative 增量 |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for category, count_delta in sorted(
        change["category_counts"].items(), key=lambda item: (-item[1], item[0])
    ):
        if count_delta <= 0:
            continue
        lines.append(
            f"| {coverage.CATEGORY_NAMES.get(category, category)} | "
            f"{before['category_counts'].get(category, 0)} | {after['category_counts'].get(category, 0)} | "
            f"+{count_delta} | +{change['category_hard_negative'].get(category, 0)} |"
        )
    lines.extend(
        [
            "",
            "## 机制覆盖变化",
            "",
            "| 机制组 | 加入前 | 加入后 | 增量 |",
            "|---|---:|---:|---:|",
        ]
    )
    for mechanism, count_delta in sorted(
        change["mechanism_group_counts"].items(), key=lambda item: (-item[1], item[0])
    ):
        lines.append(
            f"| {mechanism} | {before['mechanism_group_counts'].get(mechanism, 0)} | "
            f"{after['mechanism_group_counts'].get(mechanism, 0)} | +{count_delta} |"
        )
    lines.extend(
        [
            "",
            "## 解释",
            "",
            "Phase3 第二波仍是 raw 候选，本报告只用于入库前能力地图评估。",
            "这些数字基于 review_notes、上下文和关键词启发式推断，不是最终人工标签统计。",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    OUTPUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(f"Wrote phase-3 second-wave coverage delta to {OUTPUT_JSON}")
    print(f"Wrote readable phase-3 second-wave coverage delta to {OUTPUT_MD}")
    print(f"Candidate pool: {report['before']['count']} -> {report['after']['count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
