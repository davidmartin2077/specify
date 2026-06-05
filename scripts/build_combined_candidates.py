#!/usr/bin/env python3
"""Build reviewed JSONL candidates from raw user and Grok notes."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
GROK_PATH = ROOT / "data/raw/grok_candidates_50.txt"
USER_PATH = ROOT / "data/raw/user_candidates_1.txt"
OUTPUT_PATH = ROOT / "data/processed/combined_candidates.jsonl"


RISK_OVERRIDES = {
    "GROK_001": "low",
    "GROK_004": "high",
    "GROK_006": "high",
    "GROK_008": "high",
    "GROK_013": "low",
    "GROK_018": "medium",
    "GROK_025": "low",
    "GROK_031": "low",
    "GROK_038": "medium",
    "GROK_040": "high",
    "GROK_046": "low",
    "USER_003": "medium",
}

EVIDENCE_BY_RISK = {
    "high": "strong",
    "medium": "moderate",
    "low": "weak",
    "none": "weak",
}

AMBIGUITY_BY_RISK = {
    "high": "medium",
    "medium": "medium",
    "low": "high",
    "none": "low",
}


def parse_grok(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        r"(?P<number>\d+)\.\s+text:\s*(?P<text>.*?)\n"
        r"\s+platform:\s*(?P<platform>.*?)\n"
        r"\s+context:\s*(?P<context>.*?)\n"
        r"\s+suspected_encoding:\s*(?P<encoding>.*?)\n"
        r"\s+suspected_risk:\s*(?P<risk>.*?)\n"
        r"\s+note:\s*(?P<note>.*?)(?=\n\n\d+\. text:|\Z)",
        re.S,
    )
    rows = []
    for match in pattern.finditer(text):
        number = int(match.group("number"))
        rows.append(
            {
                "source": "grok",
                "source_id": f"GROK_{number:03d}",
                "text": match.group("text").strip(),
                "platform": match.group("platform").strip(),
                "context": match.group("context").strip(),
                "suspected_encoding": match.group("encoding").strip(),
                "suspected_risk": match.group("risk").strip(),
                "note": " ".join(match.group("note").strip().split()),
            }
        )
    return rows


def parse_user(path: Path) -> list[dict[str, str]]:
    blocks = [block.strip() for block in path.read_text(encoding="utf-8").split("\n\n") if block.strip()]
    rows = []
    for index, block in enumerate(blocks, start=1):
        row = {
            "source": "user",
            "source_id": f"USER_{index:03d}",
            "text": "",
            "platform": "",
            "context": "",
            "suspected_encoding": "",
            "suspected_risk": "",
            "note": "",
        }
        for line in block.splitlines():
            if "：" not in line:
                continue
            key, value = line.split("：", 1)
            key = key.strip()
            value = value.strip()
            if key == "suspected":
                key = "suspected_encoding"
            if key in row:
                row[key] = value
        rows.append(row)
    return rows


def normalize_platform(platform: str) -> str:
    if not platform or platform.lower() == "all":
        return "unknown"
    return platform.replace("Twitter/X", "X")


def normalize_risk(source_id: str, suspected_risk: str) -> str:
    if source_id in RISK_OVERRIDES:
        return RISK_OVERRIDES[source_id]
    risk = suspected_risk.strip().lower()
    return risk if risk in {"high", "medium", "low", "none"} else "medium"


def infer_encoding(risk_level: str, suspected_encoding: str, note: str) -> str:
    if risk_level == "none":
        return "none"

    signal = f"{suspected_encoding} {note}"
    if any(token in signal for token in ["谐音", "细颈瓶", "河蟹", "耗子尾汁"]):
        return "A1_普通谐音"
    if any(token in signal for token in ["拆字"]):
        return "B1_拆字"
    if any(token in signal for token in ["日期", "101", "一百"]):
        return "C3_数字代指"
    if any(token in signal for token in ["历史", "崇祯", "司马懿", "林彪", "王洪文", "胡锦涛", "邓小平"]):
        return "C1_历史人物类比"
    if any(token in signal for token in ["事件", "四通桥", "纪念日", "悼念", "敏感历史"]):
        return "C2_历史事件影射"
    if any(token in signal for token in ["隐喻", "代称", "代指", "黑称", "品牌", "食物", "小粉红", "赵家人", "蛤蟆", "猪", "狗", "瓶子", "庆丰", "蜡烛"]):
        return "C4_典故/物品/符号借用"
    if any(token in signal for token in ["反讽", "阴阳", "讽刺"]):
        return "D1_反讽"
    if any(token in signal for token in ["平台黑话", "黑话", "加速"]):
        return "E1_平台黑话"
    if any(token in signal for token in ["时间", "秋天"]):
        return "E2_时间节点触发"
    return "D2_隐喻"


def infer_secondary(primary: str, risk_level: str, suspected_encoding: str, context: str) -> list[str]:
    secondary: list[str] = []
    signal = f"{suspected_encoding} {context}"
    if risk_level in {"high", "medium"} and "时政" in signal:
        secondary.append("E1_平台黑话")
    if risk_level in {"high", "medium"} and any(token in signal for token in ["评论", "群", "弹幕", "视频"]):
        secondary.append("E3_回复链/互动触发")
    if "反讽" in signal and primary != "D1_反讽":
        secondary.append("D1_反讽")
    return secondary


def is_hard_negative(risk_level: str, note: str, context: str) -> bool:
    if "hard negative" in note.lower():
        return True
    if risk_level in {"none", "low"} and any(token in note + context for token in ["普通", "正常", "真实", "无害", "爱好", "美食", "宠物", "商品", "职场"]):
        return True
    return False


def context_required(risk_level: str, text: str, context: str, encoding: str) -> bool:
    if risk_level in {"high", "medium"}:
        return True
    if any(token in text for token in ["懂", "又到了", "不能说", "101", "五月三十五", "勇士", "蜡烛"]):
        return True
    return encoding != "none" and bool(context)


def make_reasoning(row: dict[str, str], risk_level: str, primary: str, hard_negative: bool) -> dict[str, Any]:
    text = row["text"]
    context = row["context"] or "未提供上下文"
    encoding = row["suspected_encoding"] or "未提供候选编码"
    note = row["note"] or "无补充说明"

    literal = [f"字面上是在表达：{text}"]
    encoding_analysis = [] if primary == "none" else [f"候选编码机制为：{encoding}。", f"按项目分类暂归为 {primary}。"]
    context_analysis = [f"可用上下文：{context}。"]

    if risk_level == "high":
        supporting = [f"原始说明提示：{note}", "文本与上下文共同支持非字面解读。"]
        counter = ["仍需避免直接还原具体对象，最终训练输出应保留匿名化或概括表述。"]
    elif risk_level == "medium":
        supporting = [f"原始说明提示：{note}", "存在可疑编码或语境信号。"]
        counter = ["目标指向或上下文证据仍不充分，普通解释仍可能成立。"]
    elif risk_level == "low":
        supporting = ["存在弱暗示、关键词撞车或候选编码痕迹。"]
        counter = [f"上下文更支持普通解释：{context}。", "证据不足以升为 medium 或 high。"]
    else:
        supporting = []
        counter = [f"上下文支持普通解释：{context}。", "未发现足够的编码机制或风险语境。"]

    if hard_negative and "hard negative" not in " ".join(counter).lower():
        counter.append("该样本适合作为 hard negative，训练模型避免关键词误杀。")

    return {
        "literal_analysis": literal,
        "encoding_analysis": encoding_analysis,
        "context_analysis": context_analysis,
        "supporting_evidence": supporting,
        "counter_evidence": counter,
        "final_rationale": f"综合文本、上下文和反证，暂标为 {risk_level}；该条仍需人工复核后进入正式训练集。",
    }


def make_sample(row: dict[str, str], index: int) -> dict[str, Any]:
    risk_level = normalize_risk(row["source_id"], row["suspected_risk"])
    primary = infer_encoding(risk_level, row["suspected_encoding"], row["note"])
    hard_negative = is_hard_negative(risk_level, row["note"], row["context"])
    sample_id = f"{row['source_id']}_{risk_level.upper()}"

    return {
        "id": sample_id,
        "split": "train",
        "source_type": "synthetic",
        "platform": normalize_platform(row["platform"]),
        "text": row["text"],
        "context": {
            "title": row["context"],
            "description": "",
            "parent_comment": "",
            "reply_chain": [],
            "time": "",
            "topic": row["suspected_encoding"],
        },
        "risk_level": risk_level,
        "encoding_primary": primary,
        "encoding_secondary": infer_secondary(primary, risk_level, row["suspected_encoding"], row["context"]),
        "context_required": context_required(risk_level, row["text"], row["context"], primary),
        "ambiguity": AMBIGUITY_BY_RISK[risk_level],
        "evidence_strength": EVIDENCE_BY_RISK[risk_level],
        "freshness": "stable",
        "hard_negative": hard_negative,
        "target_known": risk_level == "high",
        "target_reference": "匿名化目标对象或事件" if risk_level in {"high", "medium"} else "",
        "should_explain_target": False,
        "reasoning": make_reasoning(row, risk_level, primary, hard_negative),
        "quality_status": "needs_revision",
        "review_notes": f"source={row['source']}; source_id={row['source_id']}; original_risk={row['suspected_risk']}; original_note={row['note']}",
    }


def main() -> int:
    rows = parse_grok(GROK_PATH) + parse_user(USER_PATH)
    samples = [make_sample(row, index) for index, row in enumerate(rows, start=1)]
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        for sample in samples:
            handle.write(json.dumps(sample, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"Wrote {len(samples)} samples to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
