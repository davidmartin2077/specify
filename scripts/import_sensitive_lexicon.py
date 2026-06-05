#!/usr/bin/env python3
"""Build a categorized sampling plan from the Sensitive-lexicon repository.

This script does not convert the lexicon into training samples directly. The
lexicon is treated as a recall source and a stratified sampling pool.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LEXICON_ROOT = ROOT / "data/raw/third_party/Sensitive-lexicon"
VOCAB_DIR = LEXICON_ROOT / "Vocabulary"
OUTPUT_TERMS_PATH = ROOT / "data/processed/lexicon_terms.jsonl"
OUTPUT_PLAN_PATH = ROOT / "data/processed/lexicon_sampling_plan.json"
OUTPUT_SEEDS_PATH = ROOT / "data/processed/lexicon_seed_terms.jsonl"


SOURCE_CATEGORY_HINTS = {
    "政治": "political_history",
    "反动": "political_history",
    "GFW": "platform_censorship_evasion",
    "新思想": "political_history",
    "色情": "sexual_content",
    "暴恐": "violence_extremism",
    "涉枪涉爆": "weapons_explosives",
    "广告": "spam_ads_fraud",
    "非法网址": "spam_ads_fraud",
    "贪腐": "public_affairs",
    "民生": "public_affairs",
    "COVID": "public_affairs",
    "其他": "mixed_unknown",
    "补充": "mixed_unknown",
    "网易": "mixed_unknown",
    "零时": "mixed_unknown",
}

CONTENT_CATEGORY_HINTS = [
    ("spam_ads_fraud", ["http", "www", ".com", ".cn", "qq", "微信", "客服", "兼职", "代办", "贷款", "发票", "报码", "六合彩"]),
    ("gambling", ["博彩", "赌博", "赌场", "赌球", "六合彩", "开奖", "投注", "赔率", "老虎机", "百家乐"]),
    ("cyber_abuse", ["黑客", "木马", "盗号", "撞库", "ddos", "抓鸡", "免杀", "钓鱼网站"]),
    ("sexual_content", ["成人", "色情", "裸", "淫", "性", "妓", "嫖", "援交", "av", "乳", "屄", "屌", "穴", "奸", "嫩"]),
    ("weapons_explosives", ["枪", "子弹", "弹药", "炸药", "炸弹", "爆炸", "爆破", "火药", "弓单", "木仓"]),
    ("violence_extremism", ["恐怖", "暴恐", "圣战", "基地组织", "塔利班", "袭击"]),
    ("illegal_goods", ["毒品", "冰毒", "海洛因", "大麻", "麻醉", "迷药", "摇头丸", "k粉"]),
    ("platform_censorship_evasion", ["gfw", "翻墙", "封锁", "审查", "敏感词", "无界", "自由门"]),
    ("public_affairs", ["贪污", "腐败", "维权", "上访", "强拆", "民生", "疫情", "covid"]),
    ("insulting_abuse", ["傻", "狗", "贱", "逼", "滚", "死"]),
    ("political_history", ["党", "政府", "主席", "民主", "宪政", "独裁", "六四", "台湾", "西藏", "新疆"]),
]


def read_terms_from_file(path: Path) -> list[str]:
    terms: list[str] = []
    for raw_line in path.read_text(encoding="utf-8-sig", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        terms.append(line)
    return terms


def source_category(path: Path) -> str:
    name = path.name
    for hint, category in SOURCE_CATEGORY_HINTS.items():
        if hint in name:
            return category
    return "mixed_unknown"


def content_category(term: str, fallback: str) -> str:
    lowered = term.lower()
    if re.search(r"(https?://|www\.|[a-z0-9][a-z0-9.-]*\.(com|cn|net|org|info|cc|tk|tv|us|jp|tw|in|biz|xyz|me)\b)", lowered):
        return "spam_ads_fraud"
    if re.fullmatch(r"[+\d][\d\s().-]{5,}", term):
        return "spam_ads_fraud"
    for category, hints in CONTENT_CATEGORY_HINTS:
        if any(hint in lowered or hint in term for hint in hints):
            return category
    return fallback


def normalize_key(term: str) -> str:
    return re.sub(r"\s+", "", term).lower()


def features(term: str) -> dict[str, Any]:
    latin = bool(re.search(r"[A-Za-z]", term))
    digit = bool(re.search(r"\d", term))
    symbol = bool(re.search(r"[^\w\u4e00-\u9fff]", term))
    whitespace = bool(re.search(r"\s", term))
    mixed_script = latin and bool(re.search(r"[\u4e00-\u9fff]", term))
    return {
        "length": len(term),
        "contains_latin": latin,
        "contains_digit": digit,
        "contains_symbol": symbol,
        "contains_whitespace": whitespace,
        "mixed_script": mixed_script,
        "likely_obfuscated": latin or digit or symbol or whitespace or mixed_script,
    }


def mechanism_tags(term: str) -> list[str]:
    tags: list[str] = []
    term_features = features(term)
    if term_features["contains_latin"]:
        tags.append("A2_拼音/首字母缩写")
    if term_features["contains_digit"]:
        tags.append("C3_数字代指")
    if term_features["contains_symbol"] or term_features["contains_whitespace"]:
        tags.append("B4_符号/空格/Unicode 干扰")
    if term_features["mixed_script"]:
        tags.append("F_组合编码")
    if not tags:
        tags.append("literal_keyword")
    return tags


def build_terms() -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = {}
    for path in sorted(VOCAB_DIR.glob("*.txt")):
        fallback_category = source_category(path)
        for term in read_terms_from_file(path):
            key = normalize_key(term)
            if not key:
                continue
            category = content_category(term, fallback_category)
            if key not in grouped:
                grouped[key] = {
                    "term": term,
                    "normalized_key": key,
                    "category": category,
                    "source_files": [],
                    "mechanism_tags": mechanism_tags(term),
                    "features": features(term),
                }
            grouped[key]["source_files"].append(path.name)

            # Prefer a specific content-derived category over mixed_unknown.
            if grouped[key]["category"] == "mixed_unknown" and category != "mixed_unknown":
                grouped[key]["category"] = category

    terms = list(grouped.values())
    for item in terms:
        item["source_files"] = sorted(set(item["source_files"]))
    terms.sort(key=lambda item: (item["category"], item["normalized_key"]))
    return terms


def bucket_for_term(item: dict[str, Any]) -> str:
    category = item["category"]
    tags = set(item["mechanism_tags"])
    if item["features"]["likely_obfuscated"]:
        return "obfuscated_or_variant"
    if category in {"spam_ads_fraud", "illegal_goods", "gambling", "cyber_abuse"}:
        return "transactional_risk"
    if category in {"political_history", "public_affairs", "platform_censorship_evasion"}:
        return "context_sensitive"
    if category in {"sexual_content", "violence_extremism", "weapons_explosives"}:
        return "direct_policy_risk"
    if "literal_keyword" in tags:
        return "literal_keyword"
    return "mixed_review"


def choose_seed_terms(terms: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in terms:
        by_category[item["category"]].append(item)

    seeds: list[dict[str, Any]] = []
    for category, items in sorted(by_category.items()):
        by_bucket: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for item in items:
            by_bucket[bucket_for_term(item)].append(item)

        for bucket, bucket_items in sorted(by_bucket.items()):
            bucket_items.sort(key=lambda item: (not item["features"]["likely_obfuscated"], item["features"]["length"], item["term"]))
            for item in bucket_items[:20]:
                seeds.append(
                    {
                        "term": item["term"],
                        "category": category,
                        "bucket": bucket,
                        "mechanism_tags": item["mechanism_tags"],
                        "source_files": item["source_files"],
                        "recommended_use": recommended_use(category, bucket),
                    }
                )
    return seeds


def recommended_use(category: str, bucket: str) -> str:
    if bucket == "context_sensitive":
        return "generate high/medium/low/none context contrast set"
    if bucket == "obfuscated_or_variant":
        return "generate normalization and obfuscation recognition set"
    if bucket == "transactional_risk":
        return "generate solicitation vs ordinary-commerce hard-negative set"
    if bucket == "direct_policy_risk":
        return "generate direct-risk and educational/news hard-negative set"
    if category == "mixed_unknown":
        return "manual review before sample generation"
    return "generate literal keyword and hard-negative set"


def build_plan(terms: list[dict[str, Any]], seeds: list[dict[str, Any]]) -> dict[str, Any]:
    category_counts = Counter(item["category"] for item in terms)
    source_counts = Counter(source for item in terms for source in item["source_files"])
    bucket_counts = Counter(bucket_for_term(item) for item in terms)
    mechanism_counts = Counter(tag for item in terms for tag in item["mechanism_tags"])
    obfuscated_count = sum(1 for item in terms if item["features"]["likely_obfuscated"])

    category_plan = []
    for category, count in sorted(category_counts.items()):
        seed_count = sum(1 for item in seeds if item["category"] == category)
        if category == "mixed_unknown":
            target_samples = 0
            note = "先人工复核，不直接生成训练样本。"
        elif count >= 1000:
            target_samples = 160
            note = "大类，只抽机制代表样本和 hard negative，不逐词扩写。"
        elif count >= 200:
            target_samples = 100
            note = "中等类，覆盖直接命中、变体、上下文和误杀。"
        else:
            target_samples = 60
            note = "小类，优先覆盖典型语境和反证。"
        category_plan.append(
            {
                "category": category,
                "unique_terms": count,
                "seed_terms": seed_count,
                "target_candidate_samples": target_samples,
                "note": note,
            }
        )

    return {
        "source": {
            "repo": "https://github.com/konsheng/Sensitive-lexicon",
            "local_path": str(LEXICON_ROOT.relative_to(ROOT)),
            "input_dir": str(VOCAB_DIR.relative_to(ROOT)),
        },
        "summary": {
            "unique_terms": len(terms),
            "source_files": len(source_counts),
            "obfuscated_or_mixed_terms": obfuscated_count,
        },
        "category_counts": dict(sorted(category_counts.items())),
        "bucket_counts": dict(sorted(bucket_counts.items())),
        "mechanism_counts": dict(sorted(mechanism_counts.items())),
        "source_file_counts": dict(sorted(source_counts.items())),
        "category_sampling_plan": category_plan,
        "next_steps": [
            "人工快速复核 lexicon_seed_terms.jsonl 的类别和可用性。",
            "按 category_sampling_plan 生成少量候选样本，而不是全量逐词扩写。",
            "每个类别同时生成 direct risk、context-sensitive、low/none hard negative。",
            "词库命中只作为召回证据，训练标签仍以文本语境和反证为准。",
        ],
    }


def main() -> int:
    if not VOCAB_DIR.exists():
        raise FileNotFoundError(f"Missing lexicon directory: {VOCAB_DIR}")

    terms = build_terms()
    seeds = choose_seed_terms(terms)
    plan = build_plan(terms, seeds)

    OUTPUT_TERMS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_TERMS_PATH.open("w", encoding="utf-8") as handle:
        for item in terms:
            handle.write(json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n")

    with OUTPUT_SEEDS_PATH.open("w", encoding="utf-8") as handle:
        for item in seeds:
            handle.write(json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n")

    with OUTPUT_PLAN_PATH.open("w", encoding="utf-8") as handle:
        json.dump(plan, handle, ensure_ascii=False, indent=2)

    print(f"Wrote {len(terms)} unique lexicon terms to {OUTPUT_TERMS_PATH}")
    print(f"Wrote {len(seeds)} seed terms to {OUTPUT_SEEDS_PATH}")
    print(f"Wrote sampling plan to {OUTPUT_PLAN_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
