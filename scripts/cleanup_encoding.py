#!/usr/bin/env python3
"""
清理 encoding_primary / encoding_secondary 字段：
1. 统一使用 canonical 编码分类（与 encoding_taxonomy.md 一致）
2. 合并重复/不一致的标签
3. 修正错位分类编号

Canonical 分类体系：

A类_语音编码:
  A1_普通谐音, A2_拼音/首字母缩写, A3_方言谐音, A4_外语谐音/跨语言音译

B类_字形编码:
  B1_拆字, B2_合字/拼字, B3_形近字替换, B4_符号/空格/Unicode 干扰

C类_语义编码:
  C1_历史人物类比, C2_历史事件影射, C3_数字代指
  C4_典故/物品/符号借用, C5_概念替换

D类_修辞编码:
  D1_反讽, D2_隐喻, D3_借代, D4_双关

E类_语境编码:
  E1_平台黑话, E2_时间节点触发, E3_互动/热点触发, E4_热点绑定

F类_组合编码:
  F_组合编码

其他:
  literal_keyword, none
"""

import json
import shutil
from collections import Counter
from pathlib import Path

DATA_PATH = Path("data/processed/combined_candidates.jsonl")
BACKUP_PATH = DATA_PATH.with_suffix(".jsonl.bak")

# ─── Canonical taxonomy ─────────────────────────────────────
CANONICAL = frozenset({
    "A1_普通谐音",
    "A2_拼音/首字母缩写",
    "A3_方言谐音",
    "A4_外语谐音/跨语言音译",
    "B1_拆字",
    "B2_合字/拼字",
    "B3_形近字替换",
    "B4_符号/空格/Unicode 干扰",
    "C1_历史人物类比",
    "C2_历史事件影射",
    "C3_数字代指",
    "C4_典故/物品/符号借用",
    "C5_概念替换",
    "D1_反讽",
    "D2_隐喻",
    "D3_借代",
    "D4_双关",
    "E1_平台黑话",
    "E2_时间节点触发",
    "E3_互动/热点触发",
    "E4_热点绑定",
    "F_组合编码",
    "literal_keyword",
    "none",
})

# ─── Non-canonical → canonical mapping ──────────────────────
PRIMARY_MAP = {
    # A类 — 合并命名变体
    "A1_谐音": "A1_普通谐音",
    "A1_普通谐音": "A1_普通谐音",
    "A2_拼音缩写": "A2_拼音/首字母缩写",
    "A2_拼音/首字母缩写": "A2_拼音/首字母缩写",

    # B类 — 无变体

    # C类 — 合并命名变体
    "C1_人物代指": "C1_历史人物类比",
    "C1_历史人物类比": "C1_历史人物类比",
    "C3_数字符号代指": "C3_数字代指",
    "C3_数字代指": "C3_数字代指",
    "C4_典故/符号借用": "C4_典故/物品/符号借用",
    "C4_典故/物品/符号借用": "C4_典故/物品/符号借用",

    # D类 — 修正错位编号
    "D2_夸张/反话": "D1_反讽",  # 夸张/反话本质上是反讽
    "D3_反讽": "D1_反讽",       # 反讽是D1，不是D3

    # E类 — 修正错位编号 & 统一命名
    "E2_社会议题话语": "E4_热点绑定",  # 社会议题讨论往往绑定当前热点
    "E3_话题/热点触发": "E3_互动/热点触发",  # 统一命名
    "E3_历史事件影射": "C2_历史事件影射",  # 错位，历史事件影射是C2
    "E4_审查规避讨论": "E4_热点绑定",  # 审查规避是时效性话题
}

SECONDARY_MAP = {
    # 同上 + 额外清理
    "A1_谐音": "A1_普通谐音",
    "A2_拼音缩写": "A2_拼音/首字母缩写",
    "C1_人物代指": "C1_历史人物类比",
    "C2_地点代指": "D3_借代",           # 用地点代指实体/事件 → 借代
    "C3_数字/代码": "C3_数字代指",       # 统一命名
    "C3_数字符号代指": "C3_数字代指",
    "C4_拼音缩写": "A2_拼音/首字母缩写",  # 拼音缩写归类到A2
    "C4_典故/符号借用": "C4_典故/物品/符号借用",
    "D1_威胁": "E1_平台黑话",           # 线上威胁是平台语境行为
    "D2_夸张/反话": "D1_反讽",
    "D3_反讽": "D1_反讽",
    "D5_影射": "D3_借代",              # D5不存在；影射是一种借代
    "E2_社会议题话语": "E4_热点绑定",
    "E3_话题/热点触发": "E3_互动/热点触发",
    "E3_历史事件影射": "C2_历史事件影射",
    "E3_上下文/互动触发": "E3_互动/热点触发",
    "E4_审查规避讨论": "E4_热点绑定",
    "C1_地理位置暴露": "D3_借代",        # 用地理位置信息代指身份 → 借代
}


def map_primary(val: str) -> str:
    """将 encoding_primary 映射到 canonical 值。"""
    mapped = PRIMARY_MAP.get(val, val)
    if mapped not in CANONICAL:
        print(f"  ⚠️  映射后仍非 canonical: {val!r} → {mapped!r}")
    return mapped


def map_secondary(val: str) -> str:
    """将单个 encoding_secondary 映射到 canonical 值。"""
    mapped = SECONDARY_MAP.get(val, val)
    if mapped not in CANONICAL:
        print(f"  ⚠️  secondary 映射后仍非 canonical: {val!r} → {mapped!r}")
    return mapped


def cleanup_secondary(vals) -> list:
    """清洗 encoding_secondary 列表：去重、排序、映射。"""
    if not vals:
        return []
    if isinstance(vals, str):
        vals = [vals]
    mapped = [map_secondary(v) for v in vals if v]
    # 去重（有序）
    seen = set()
    deduped = []
    for v in mapped:
        if v not in seen:
            seen.add(v)
            deduped.append(v)
    return sorted(deduped)


def main():
    # 备份
    if DATA_PATH.exists():
        shutil.copy2(DATA_PATH, BACKUP_PATH)
        print(f"  ✅ 已备份到 {BACKUP_PATH}")

    # 读取
    records = []
    with open(DATA_PATH) as f:
        for line in f:
            d = json.loads(line)
            records.append(d)

    print(f"\n  共读取 {len(records)} 条记录\n")

    # ── 统计变更 ──
    pri_changes = Counter()
    sec_changes = Counter()
    bad_secondary_canonical = Counter()  # 清理后仍存在的非 canonical

    # ── 逐条清洗 ──
    for d in records:
        old_pri = d.get("encoding_primary", "")
        new_pri = map_primary(old_pri)
        if new_pri != old_pri:
            pri_changes[f"{old_pri} → {new_pri}"] += 1
        d["encoding_primary"] = new_pri

        old_sec = d.get("encoding_secondary", [])
        new_sec = cleanup_secondary(old_sec)
        old_sec_str = str(sorted(old_sec)) if isinstance(old_sec, list) else str(old_sec)
        new_sec_str = str(new_sec)
        if new_sec_str != old_sec_str:
            sec_changes[f"{old_sec_str} → {new_sec_str}"] += 1
        d["encoding_secondary"] = new_sec

        # 检查 secondary 中是否还有非 canonical 值
        for v in new_sec:
            if v not in CANONICAL:
                bad_secondary_canonical[v] += 1

    # ── 写回 ──
    with open(DATA_PATH, "w") as f:
        for d in records:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    print(f"  ✅ 写回 {DATA_PATH}\n")

    # ── 报告 ──
    print("=" * 60)
    print("  encoding_primary 变更统计")
    print("=" * 60)
    for k, v in sorted(pri_changes.items(), key=lambda x: -x[1]):
        print(f"  {k:55s}  {v:4d}条")

    print(f"\n{'=' * 60}")
    print("  encoding_secondary 变更统计")
    print("=" * 60)
    for k, v in sorted(sec_changes.items(), key=lambda x: -x[1]):
        if v >= 2:
            print(f"  {k:65s}  {v:4d}条")
    remaining_sec = sum(v for k, v in sec_changes.items() if v < 2)
    if remaining_sec:
        print(f"  (其余 {remaining_sec} 条单次变更)")

    # 验证 final 分布
    print(f"\n{'=' * 60}")
    print("  清洗后 encoding_primary 分布")
    print("=" * 60)
    final_pri = Counter()
    final_sec = Counter()
    for d in records:
        final_pri[d["encoding_primary"]] += 1
        for v in d.get("encoding_secondary", []):
            final_sec[v] += 1
    for k, v in sorted(final_pri.items(), key=lambda x: -x[1]):
        ok = "✅" if k in CANONICAL else "❌"
        print(f"  {k:45s}  {v:4d}条  {ok}")

    print(f"\n  清洗后 encoding_secondary 分布")
    print("-" * 40)
    for k, v in sorted(final_sec.items(), key=lambda x: -x[1]):
        ok = "✅" if k in CANONICAL else "❌"
        print(f"  {k:45s}  {v:4d}条  {ok}")

    if bad_secondary_canonical:
        print(f"\n  ⚠️  仍有非 canonical secondary 值:")
        for k, v in bad_secondary_canonical.items():
            print(f"    {k!r}: {v}条")

    print("\n  ✅ 清洗完成！")
    print(f"  备份文件: {BACKUP_PATH}")


if __name__ == "__main__":
    main()
