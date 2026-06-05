#!/usr/bin/env python3
"""Analyze lexicon coverage against current processed and phase-2 candidates.

The lexicon is treated as a capability map and sampling pool, not as a list to
expand one term at a time.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LEXICON_TERMS = ROOT / "data/processed/lexicon_terms.jsonl"
LEXICON_SEEDS = ROOT / "data/processed/lexicon_seed_terms.jsonl"
LEXICON_PLAN = ROOT / "data/processed/lexicon_sampling_plan.json"
PROCESSED = ROOT / "data/processed/combined_candidates.jsonl"
PHASE2 = ROOT / "data/raw/phase2_seed_candidates.jsonl"
REPORT_JSON = ROOT / "data/processed/risk_coverage_report.json"
PHASE3_PLAN_JSON = ROOT / "data/processed/phase3_sampling_plan.json"
REPORT_MD = ROOT / "docs/risk_coverage_report.md"


CATEGORY_NAMES = {
    "cyber_abuse": "网络黑产/安全风险",
    "gambling": "赌博",
    "illegal_goods": "违禁交易",
    "insulting_abuse": "辱骂/群体攻击",
    "mixed_unknown": "混合未知",
    "platform_censorship_evasion": "平台规避/审查黑话",
    "political_history": "政治历史/鉴证梗",
    "public_affairs": "公共事务",
    "sexual_content": "色情低俗",
    "spam_ads_fraud": "广告/诈骗/导流",
    "violence_extremism": "暴力极端",
    "weapons_explosives": "枪爆武器",
}

CATEGORY_HINTS = {
    "cyber_abuse": ["黑客", "木马", "盗号", "撞库", "漏洞", "攻击", "号库", "网络安全"],
    "gambling": ["赌博", "赌球", "博彩", "盘口", "水位", "赔率", "下注", "彩票", "牌局", "底分"],
    "illegal_goods": ["违禁", "毒品", "冰毒", "大麻", "麻醉", "迷药", "药物/违禁"],
    "insulting_abuse": ["辱骂", "攻击", "地域", "地图炮", "群体攻击", "骂人"],
    "platform_censorship_evasion": [
        "平台黑话",
        "平台规避",
        "审查",
        "敏感词",
        "别写全",
        "不能说",
        "首字母",
        "谐音",
        "符号",
        "空格",
        "unicode",
    ],
    "political_history": [
        "政治",
        "历史",
        "鉴证",
        "现实人物",
        "人物代指",
        "历史影射",
        "日期代指",
        "时间节点",
        "公共事件",
    ],
    "public_affairs": ["公共事务", "政策", "维权", "民生", "公共议题", "组织会议"],
    "sexual_content": ["色情", "低俗", "成人", "擦边", "同城夜生活", "健康教育"],
    "spam_ads_fraud": [
        "诈骗",
        "刷单",
        "招聘",
        "贷款",
        "退款",
        "荐股",
        "广告",
        "导流",
        "兼职",
        "账号交易",
        "公益/诈骗",
    ],
    "violence_extremism": ["暴恐", "极端", "暴力", "动员", "线下冲突", "恐怖"],
    "weapons_explosives": ["枪爆", "武器", "爆炸", "炸药", "零件", "化学安全"],
}

MECHANISM_GROUPS = {
    "phonetic_or_initials": {"A1_普通谐音", "A2_拼音/首字母缩写", "A3_方言谐音", "A4_外语谐音/跨语言音译"},
    "shape_or_symbol": {"B1_拆字", "B2_合字/拼字", "B3_形近字替换", "B4_符号/空格/Unicode 干扰"},
    "semantic_mapping": {
        "C1_历史人物类比",
        "C2_历史事件影射",
        "C3_数字代指",
        "C4_典故/物品/符号借用",
    },
    "rhetorical": {"D1_反讽", "D2_夸张/反话", "D2_隐喻", "D3_借代"},
    "contextual": {"E1_平台黑话", "E2_时间节点触发", "E3_话题/热点触发"},
    "combined": {"F_组合编码"},
    "literal_keyword": {"literal_keyword", "none"},
}


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


def parse_notes(notes: Any) -> dict[str, str]:
    parsed: dict[str, str] = {}
    if not isinstance(notes, str):
        return parsed
    for part in notes.split(";"):
        part = part.strip()
        if "=" in part:
            key, value = part.split("=", 1)
            parsed[key.strip()] = value.strip()
    return parsed


def normalize(text: str) -> str:
    return re.sub(r"\s+", "", text).lower()


def searchable_text(sample: dict[str, Any]) -> str:
    values = [str(sample.get("text", ""))]
    context = sample.get("context", {})
    if isinstance(context, dict):
        for field in ("title", "description", "parent_comment", "topic"):
            values.append(str(context.get(field, "")))
        replies = context.get("reply_chain", [])
        if isinstance(replies, list):
            values.extend(str(item) for item in replies)
    notes = parse_notes(sample.get("review_notes", ""))
    values.extend(notes.get(key, "") for key in ("meme_cluster", "category", "cluster", "axis"))
    return " ".join(values)


def categories_for(sample: dict[str, Any]) -> set[str]:
    notes = parse_notes(sample.get("review_notes", ""))
    explicit = notes.get("category", "")
    if explicit in CATEGORY_NAMES:
        return {explicit}

    haystack = searchable_text(sample).lower()
    matched = {
        category
        for category, hints in CATEGORY_HINTS.items()
        if any(hint.lower() in haystack for hint in hints)
    }

    source = notes.get("source", "")
    if source in {"meme_expansion", "gemini_expansion", "grok", "user"}:
        cluster = notes.get("meme_cluster", "") + " " + notes.get("original_note", "")
        if any(hint in cluster for hint in CATEGORY_HINTS["political_history"]):
            matched.add("political_history")
    return matched or {"mixed_unknown"}


def mechanisms_for(sample: dict[str, Any]) -> set[str]:
    values = {str(sample.get("encoding_primary", "none"))}
    secondary = sample.get("encoding_secondary", [])
    if isinstance(secondary, list):
        values.update(str(item) for item in secondary)
    return values


def ngram_index(samples: list[dict[str, Any]], min_len: int = 2, max_len: int = 20) -> set[str]:
    index: set[str] = set()
    for sample in samples:
        text = normalize(searchable_text(sample))
        length = len(text)
        for size in range(min_len, min(max_len, length) + 1):
            for start in range(0, length - size + 1):
                index.add(text[start : start + size])
    return index


def sample_summary(samples: list[dict[str, Any]]) -> dict[str, Any]:
    category_counts: Counter[str] = Counter()
    category_risk: dict[str, Counter[str]] = defaultdict(Counter)
    category_hard_negative: Counter[str] = Counter()
    mechanism_counts: Counter[str] = Counter()
    mechanism_groups: Counter[str] = Counter()
    source_counts: Counter[str] = Counter()

    for sample in samples:
        notes = parse_notes(sample.get("review_notes", ""))
        source_counts[notes.get("source", "unknown")] += 1
        for category in categories_for(sample):
            category_counts[category] += 1
            category_risk[category][str(sample.get("risk_level", "unknown"))] += 1
            category_hard_negative[category] += bool(sample.get("hard_negative"))
        for mechanism in mechanisms_for(sample):
            mechanism_counts[mechanism] += 1
            for group, members in MECHANISM_GROUPS.items():
                if mechanism in members:
                    mechanism_groups[group] += 1

    return {
        "count": len(samples),
        "source_counts": dict(sorted(source_counts.items())),
        "category_counts": dict(sorted(category_counts.items())),
        "category_risk": {
            category: dict(sorted(counts.items())) for category, counts in sorted(category_risk.items())
        },
        "category_hard_negative": dict(sorted(category_hard_negative.items())),
        "mechanism_counts": dict(sorted(mechanism_counts.items())),
        "mechanism_group_counts": dict(sorted(mechanism_groups.items())),
        "risk_counts": dict(sorted(Counter(str(item.get("risk_level", "unknown")) for item in samples).items())),
        "hard_negative": sum(bool(item.get("hard_negative")) for item in samples),
    }


def lexicon_term_coverage(
    terms: list[dict[str, Any]],
    samples: list[dict[str, Any]],
) -> tuple[dict[str, Any], set[str]]:
    index = ngram_index(samples)
    covered_keys: set[str] = set()
    category_total: Counter[str] = Counter()
    category_covered: Counter[str] = Counter()
    bucket_total: Counter[str] = Counter()
    bucket_covered: Counter[str] = Counter()
    mechanism_total: Counter[str] = Counter()
    mechanism_covered: Counter[str] = Counter()

    for term in terms:
        key = normalize(str(term.get("normalized_key", term.get("term", ""))))
        category = str(term.get("category", "mixed_unknown"))
        features = term.get("features", {})
        bucket = "obfuscated_or_variant" if isinstance(features, dict) and features.get("likely_obfuscated") else "literal_or_direct"
        category_total[category] += 1
        bucket_total[bucket] += 1
        tags = term.get("mechanism_tags", [])
        if not isinstance(tags, list):
            tags = []
        for tag in tags:
            mechanism_total[str(tag)] += 1
        if 2 <= len(key) <= 20 and key in index:
            covered_keys.add(key)
            category_covered[category] += 1
            bucket_covered[bucket] += 1
            for tag in tags:
                mechanism_covered[str(tag)] += 1

    categories = {}
    for category, total in sorted(category_total.items()):
        covered = category_covered[category]
        categories[category] = {
            "lexicon_terms": total,
            "exact_or_normalized_term_hits": covered,
            "hit_rate": round(covered / total, 4) if total else 0,
        }

    mechanisms = {}
    for mechanism, total in sorted(mechanism_total.items()):
        covered = mechanism_covered[mechanism]
        mechanisms[mechanism] = {
            "lexicon_terms": total,
            "exact_or_normalized_term_hits": covered,
            "hit_rate": round(covered / total, 4) if total else 0,
        }

    return (
        {
            "note": (
                "Term hit rate measures literal/normalized occurrence only. Low hit rate is expected and does not "
                "mean the model must receive one sample per term."
            ),
            "categories": categories,
            "buckets": {
                bucket: {
                    "lexicon_terms": total,
                    "exact_or_normalized_term_hits": bucket_covered[bucket],
                    "hit_rate": round(bucket_covered[bucket] / total, 4) if total else 0,
                }
                for bucket, total in sorted(bucket_total.items())
            },
            "mechanisms": mechanisms,
        },
        covered_keys,
    )


def priority_for(
    category: str,
    target: int,
    sample_count: int,
    risk_counts: dict[str, int],
    hard_negative: int,
) -> tuple[str, list[str], int]:
    reasons = []
    gap = max(target - sample_count, 0)
    if sample_count < 20:
        reasons.append("当前语境样本少于 20 条")
    if risk_counts.get("high", 0) + risk_counts.get("medium", 0) < 10:
        reasons.append("风险/复核样本不足")
    if hard_negative < 5 and category not in {"violence_extremism", "weapons_explosives"}:
        reasons.append("语境反证或 hard negative 不足")
    if gap >= 100 or len(reasons) >= 2:
        priority = "P0"
    elif gap >= 50 or reasons:
        priority = "P1"
    else:
        priority = "P2"
    quota = min(max(gap, 20 if reasons else 0), 100)
    return priority, reasons, quota


def usable_representative_seed(term: str) -> bool:
    key = normalize(term)
    if len(key) < 2:
        return False
    if re.fullmatch(r"[a-z0-9]+", key) and len(key) <= 4:
        return False
    if re.fullmatch(r"[\W_]+", key):
        return False
    return True


def phase3_plan(
    sampling_plan: dict[str, Any],
    summary: dict[str, Any],
    seeds: list[dict[str, Any]],
    covered_keys: set[str],
) -> dict[str, Any]:
    categories = []
    seed_by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for seed in seeds:
        seed_by_category[str(seed.get("category", "mixed_unknown"))].append(seed)

    for item in sampling_plan.get("category_sampling_plan", []):
        category = str(item.get("category"))
        if category == "mixed_unknown":
            continue
        target = int(item.get("target_candidate_samples", 0))
        sample_count = int(summary["category_counts"].get(category, 0))
        risk_counts = summary["category_risk"].get(category, {})
        hard_negative = int(summary["category_hard_negative"].get(category, 0))
        priority, reasons, quota = priority_for(category, target, sample_count, risk_counts, hard_negative)
        first_wave_quota = min(quota, 25 if priority == "P0" else 15)
        representatives = []
        for seed in seed_by_category.get(category, []):
            term = str(seed.get("term", ""))
            key = normalize(term)
            if key not in covered_keys and usable_representative_seed(term):
                representatives.append(
                    {
                        "term": term,
                        "bucket": seed.get("bucket", ""),
                        "mechanism_tags": seed.get("mechanism_tags", []),
                        "recommended_use": seed.get("recommended_use", ""),
                    }
                )
            if len(representatives) >= 8:
                break
        categories.append(
            {
                "category": category,
                "name": CATEGORY_NAMES.get(category, category),
                "priority": priority,
                "current_inferred_samples": sample_count,
                "current_risk_counts": risk_counts,
                "current_hard_negative": hard_negative,
                "reference_target": target,
                "recommended_phase3_quota": quota,
                "recommended_first_wave_quota": first_wave_quota,
                "reasons": reasons or ["已有基础覆盖，继续补长尾机制和真实语境"],
                "representative_uncovered_seeds": representatives,
                "required_contrast_set": [
                    "direct_or_clear_risk",
                    "obfuscated_or_black_slang",
                    "contextual_medium_or_low",
                    "news_education_or_ordinary_hard_negative",
                ],
            }
        )

    categories.sort(key=lambda item: (item["priority"], -item["recommended_phase3_quota"], item["category"]))
    return {
        "objective": (
            "Use lexicon gaps to expand reasoning capabilities. Do not create one training sample per lexicon term."
        ),
        "important_caveat": (
            "Lexicon category assignment and representative seeds are heuristic. Manually review seeds before "
            "generation; a term's category is not a training label."
        ),
        "input_candidate_count": summary["count"],
        "recommended_total_phase3_quota": sum(item["recommended_phase3_quota"] for item in categories),
        "recommended_first_wave_total": sum(item["recommended_first_wave_quota"] for item in categories),
        "categories": categories,
        "mechanism_priorities": [
            {
                "mechanism_group": "phonetic_or_initials",
                "priority": "P0",
                "reason": "词库中拼音/首字母变体很多，需要更多真实语境和普通缩写对照。",
            },
            {
                "mechanism_group": "shape_or_symbol",
                "priority": "P0",
                "reason": "词库中符号/空格变体很多，需要覆盖规避意图与正常排版边界。",
            },
            {
                "mechanism_group": "semantic_mapping",
                "priority": "P0",
                "reason": "互联网鉴证梗和人物/历史映射不能从敏感词面直接学习，需要定向构造。",
            },
            {
                "mechanism_group": "contextual",
                "priority": "P0",
                "reason": "高召回工具仍需识别平台、话题、时间与回复链如何改变风险。",
            },
        ],
        "generation_rule": (
            "Each selected seed represents a mechanism cluster. Generate contrast sets, not mechanical term expansion."
        ),
    }


def render_markdown(report: dict[str, Any], plan: dict[str, Any]) -> str:
    summary = report["candidate_summary"]
    lines = [
        "# 风险词覆盖分析报告",
        "",
        "## 结论",
        "",
        f"当前分析覆盖正式候选与 phase2 raw，共 {summary['count']} 条。词库含 {report['lexicon_summary']['unique_terms']:,} 个去重词条。",
        "",
        "词库的作用是发现能力缺口、选择代表性风险簇、生成对照样本和构建压力测试；低词面命中率是正常现象，不应逐词扩写。",
        "",
        "**重要提醒：词库类别和代表 seed 是粗分类结果，可能含错配或普通词。使用前必须人工复核，不能直接把词库类别当训练标签。**",
        "",
        "## 当前候选风险分布",
        "",
    ]
    for risk, count in summary["risk_counts"].items():
        lines.append(f"- {risk}: {count}")
    lines.extend(["", f"- hard negative: {summary['hard_negative']}", "", "## 类别覆盖与第三阶段建议", ""])
    lines.append("| 优先级 | 类别 | 当前推断样本 | high/medium/low/none | hard negative | 第一波 | 完整阶段缺口 |")
    lines.append("|---|---|---:|---|---:|---:|---:|")
    for item in plan["categories"]:
        risks = item["current_risk_counts"]
        risk_text = "/".join(str(risks.get(risk, 0)) for risk in ("high", "medium", "low", "none"))
        lines.append(
            f"| {item['priority']} | {item['name']} | {item['current_inferred_samples']} | "
            f"{risk_text} | {item['current_hard_negative']} | {item['recommended_first_wave_quota']} | "
            f"{item['recommended_phase3_quota']} |"
        )
    lines.extend(
        [
            "",
            "## 优先机制",
            "",
        ]
    )
    for item in plan["mechanism_priorities"]:
        lines.append(f"- **{item['mechanism_group']} ({item['priority']})**: {item['reason']}")
    lines.extend(
        [
            "",
            "## 使用风险词库的方法",
            "",
            "1. 从缺口类别中挑少量代表词和变体。",
            "2. 每个代表词构造明确风险、隐晦黑话、上下文边界和正常语境对照。",
            "3. 将词库变体用于压力测试，检查模型是否漏判空格、符号、拼音和数字规避。",
            "4. 不把五万词逐个转换成训练样本。",
            "",
            "详细机器可读报告见 `data/processed/risk_coverage_report.json` 和 `data/processed/phase3_sampling_plan.json`。",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    terms = load_jsonl(LEXICON_TERMS)
    seeds = load_jsonl(LEXICON_SEEDS)
    processed = load_jsonl(PROCESSED)
    phase2 = load_jsonl(PHASE2)
    samples = processed + phase2
    sampling_plan = json.loads(LEXICON_PLAN.read_text(encoding="utf-8"))

    summary = sample_summary(samples)
    term_coverage, covered_keys = lexicon_term_coverage(terms, samples)
    plan = phase3_plan(sampling_plan, summary, seeds, covered_keys)
    report = {
        "inputs": {
            "processed": str(PROCESSED.relative_to(ROOT)),
            "phase2": str(PHASE2.relative_to(ROOT)),
            "lexicon_terms": str(LEXICON_TERMS.relative_to(ROOT)),
            "lexicon_seeds": str(LEXICON_SEEDS.relative_to(ROOT)),
        },
        "lexicon_summary": sampling_plan.get("summary", {}),
        "candidate_summary": summary,
        "literal_term_coverage": term_coverage,
        "interpretation": {
            "important": (
                "Literal term coverage is not the training objective. The objective is mechanism and context coverage."
            ),
            "high_recall": (
                "High recall should be learned through risk/medium contrast sets and obfuscation variants, while "
                "retaining enough hard negatives to prevent pure keyword matching."
            ),
        },
    }

    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    PHASE3_PLAN_JSON.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    REPORT_MD.write_text(render_markdown(report, plan), encoding="utf-8")

    print(f"Analyzed {len(samples)} candidates against {len(terms)} lexicon terms.")
    print(f"Wrote coverage report to {REPORT_JSON}")
    print(f"Wrote phase-3 sampling plan to {PHASE3_PLAN_JSON}")
    print(f"Wrote readable report to {REPORT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
