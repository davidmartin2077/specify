#!/usr/bin/env python3
"""
batch23: ToxiCN massive haul pipeline — 2000 samples
Maps ToxiCN → project format with label-aware encoding assignment.
Filters for quality. Generates template reasoning from labels.
"""

import csv, json, re, random
from collections import Counter

random.seed(42)

# ============================================================
# 1. Load ToxiCN
# ============================================================
print("Loading ToxiCN...")
with open('data/external/toxicn/ToxiCN_1.0.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    raw = list(reader)
for r in raw:
    if '﻿platform' in r:
        r['platform'] = r.pop('﻿platform')

print(f"  Loaded {len(raw)} samples")

# ============================================================
# 2. Quality filter
# ============================================================
def quality_filter(row):
    text = row['content']
    # Too short
    if len(text) < 10:
        return False
    # Too long (conversation chains)
    if len(text) > 500:
        return False
    # Too many special chars (garbled)
    alpha_ratio = sum(1 for c in text if '一' <= c <= '鿿' or c.isalpha()) / max(len(text), 1)
    if alpha_ratio < 0.3:
        return False
    # Pure emoji/符号
    if re.match(r'^[\s\W\d]+$', text):
        return False
    return True

filtered = [r for r in raw if quality_filter(r)]
print(f"  After quality filter: {len(filtered)}")

# ============================================================
# 3. Label mapping tables
# ============================================================

# Topic → primary encoding for each expression type
TOPIC_ENC = {
    'race': {
        'explicit': ['C4_典故/物品/符号借用', 'D3_借代', 'E1_平台黑话', 'literal_keyword'],
        'implicit': ['D2_隐喻', 'D1_反讽', 'C5_概念替换', 'D4_双关'],
        'reporting': ['E3_互动/热点触发', 'D1_反讽']
    },
    'gender': {
        'explicit': ['E1_平台黑话', 'D3_借代', 'A1_普通谐音', 'literal_keyword'],
        'implicit': ['D1_反讽', 'D4_双关', 'C5_概念替换', 'D2_隐喻'],
        'reporting': ['E3_互动/热点触发', 'D1_反讽']
    },
    'region': {
        'explicit': ['E1_平台黑话', 'D3_借代', 'C4_典故/物品/符号借用', 'literal_keyword'],
        'implicit': ['D1_反讽', 'D2_隐喻', 'C5_概念替换'],
        'reporting': ['E3_互动/热点触发', 'D1_反讽']
    },
    'lgbt': {
        'explicit': ['E1_平台黑话', 'D3_借代', 'literal_keyword'],
        'implicit': ['D1_反讽', 'D4_双关', 'C5_概念替换'],
        'reporting': ['E3_互动/热点触发', 'D1_反讽']
    }
}

# Expression → risk mapping
EXPR_RISK = {'1': 'high', '2': 'medium', '3': 'low'}

# Topic name mappings
TOPIC_CN = {'race': '种族歧视', 'gender': '性别攻击', 'region': '地域歧视', 'lgbt': '反LGBTQ'}

# Expression descriptions
EXPR_DESC = {
    '1': '显式攻击 (explicit)',
    '2': '隐晦仇恨 (implicit)',
    '3': '揭露/报告 (reporting)'
}

# ============================================================
# 4. Reasoning template generator
# ============================================================
def gen_reasoning(row, risk_level, enc_primary):
    text = row['content']
    platform = row['platform']
    topic = row['topic']
    expr = row['expression']
    toxic_type = row['toxic_type']

    topic_cn = TOPIC_CN.get(topic, topic)
    expr_cn = EXPR_DESC.get(expr, expr)
    plat_cn = '知乎' if platform == 'zhihu' else '贴吧'

    # Literal analysis
    lit = f"文本来源于{plat_cn}，话题涉及{topic_cn}。"
    if risk_level == 'high':
        lit += f"使用了直接或高度明确的攻击性表达。"
    elif risk_level == 'medium':
        lit += f"使用了隐晦、反讽或暗示性的表达方式。"
    else:
        lit += f"使用了揭露、分析或转述的表达方式。"

    # Encoding analysis
    if enc_primary == 'none':
        enc = f"无编码机制。文本为正常的{topic_cn}相关讨论。"
    elif enc_primary == 'literal_keyword':
        enc = f"使用了直接的侮辱性关键词。在中文互联网语境中，此类词汇具有明确和公认的贬义。"
    elif enc_primary == 'D1_反讽':
        enc = f"使用了反讽 (D1) 编码——字面含义与实际态度相反或存在张力。通过表面上肯定、疑问或客观的表述传递隐含的贬义或攻击。"
    elif enc_primary == 'D2_隐喻':
        enc = f"使用了隐喻 (D2) 编码——通过具体的意象、动作、场景来映射和传递对{topic_cn}相关对象的隐含态度。表面讨论与深层指向之间存在映射关系。"
    elif enc_primary == 'D3_借代':
        enc = f"使用了借代 (D3) 编码——以局部特征、标签、外号来代替整体对象。通过特征提取和标签化来简化并贬低目标群体。"
    elif enc_primary == 'D4_双关':
        enc = f"使用了双关 (D4) 编码——表述同时具有字面义和隐含义，隐含义通过语境或特定词汇的多义性触发。"
    elif enc_primary == 'E1_平台黑话':
        enc = f"使用了平台黑话 (E1) 编码——词语在特定社区或平台中被赋予了特殊的贬义或攻击性含义，跨出该平台后字面义可能完全不同。"
    elif enc_primary == 'E3_互动/热点触发':
        enc = f"使用了语境触发 (E3) 编码——文本的风险来源于其所处的互动语境、热点事件或对他人言论的引用/回应，而非文本本身的字面含义。"
    elif enc_primary == 'C4_典故/物品/符号借用':
        enc = f"使用了典故/符号借用 (C4) 编码——通过历史典故、物品符号、文化参照等方式间接传递{topic_cn}相关的隐含态度。"
    elif enc_primary == 'C5_概念替换':
        enc = f"使用了概念替换 (C5) 编码——用抽象、中性或正面概念替换具体的敏感或攻击性内容。"
    elif enc_primary == 'A1_普通谐音':
        enc = f"使用了普通话谐音 (A1) 编码——通过同音或近音字替换来规避直接使用敏感词汇，同时保留原词的发音联想和侮辱含义。"
    else:
        enc = f"使用了{enc_primary}编码机制。文本表达存在超出字面层的隐含意义。"

    # Context analysis
    if expr == '3':
        ctx = f"文本处于{topic_cn}的揭露/分析/反偏见讨论语境中。叙述者通过转述、揭露或分析他人的言论来表达立场。"
    elif expr == '2':
        ctx = f"文本处于{topic_cn}的隐晦讨论语境中。叙述者未直接使用攻击性词汇，而是通过暗示、反讽、隐喻等方式传递态度。"
    else:
        ctx = f"文本处于{topic_cn}的直接讨论语境中。使用了明确或直接的表达方式。"

    # Supporting evidence
    sup = [
        f"1. 文本来自{plat_cn}平台的真实评论，具有网络语境的真实性。",
        f"2. 涉及{topic_cn}话题，属于ToxiCN数据集中已标注的{topic}类别。"
    ]
    if expr == '1':
        sup.append("3. 使用了直接或明确的攻击性表达方式 (expression=1)。")
    elif expr == '2':
        sup.append("3. 使用了隐晦的编码表达方式 (expression=2)，需要通过语境推理来理解。")
    elif expr == '3':
        sup.append("3. 使用了揭露/报告的表达方式 (expression=3)——叙述者在转述或分析他人的言论。")

    if toxic_type == '2':
        sup.append("4. 被标注为仇恨言论 (toxic_type=2 / hate speech)，具有群体攻击性。")

    # Counter evidence
    cnt = ["1. 单一评论缺乏完整的对话上下文。"]
    if expr == '2':
        cnt.append("2. 隐晦表达存在歧义——字面义在特定语境下可能无害。")
    if expr == '3':
        cnt.append("2. 揭露/报告型表达的主要意图可能是反偏见而非传播偏见。")

    # Final rationale
    if risk_level == 'high':
        final = f"Risk: high。文本在{topic_cn}语境中使用了明确的攻击性表达或高度固化的侮辱编码。"
    elif risk_level == 'medium':
        final = f"Risk: medium。文本通过{enc_primary}编码在{topic_cn}语境中传递了隐含的偏见或攻击，但表达方式较为隐晦。"
    else:
        final = f"Risk: low。文本在{topic_cn}语境中使用了揭露或分析性的表达方式，风险主要来自话题的敏感性而非文本本身的攻击性。"

    return [lit], [enc], [ctx], sup, cnt, final


def gen_safe_reasoning(row):
    text = row['content']
    platform = row['platform']
    topic = row['topic']
    topic_cn = TOPIC_CN.get(topic, topic)
    plat_cn = '知乎' if platform == 'zhihu' else '贴吧'

    lit = f"文本来源于{plat_cn}平台，内容为正常的日常讨论。"
    enc = "无编码机制。文本为普通的网络讨论，不包含任何已知的编码机制或隐含攻击。"
    ctx = f"正常网络讨论语境。话题可能涉及{topic_cn}相关但内容不具攻击性。"
    sup = ["1. 被ToxiCN标注为非有毒 (toxic=0)。", "2. 文本内容为正常的社会讨论或日常交流。"]
    cnt = ["无风险证据。正常的网络讨论。"]
    final = f"Risk: none (hard_negative)。来自ToxiCN的非有毒样本。虽然话题涉及{topic_cn}但文本不包含攻击性内容。"

    return [lit], [enc], [ctx], sup, cnt, final


# ============================================================
# 5. Assemble sample
# ============================================================
def make_sample(row, next_id_val):
    sid = f"{next_id_val:06d}"
    text = row['content']
    platform = row['platform']
    topic = row['topic']
    expr = row['expression']
    toxic = row['toxic']
    toxic_type = row['toxic_type']

    if toxic == '0':
        # Safe / hard_negative
        risk_level = 'none'
        enc_primary = 'none'
        enc_secondary = []
        hard_negative = True
        needs_context = False
        ambiguity = 'low'
        evidence_strength = 'moderate'
        lit, enc, ctx, sup, cnt, final = gen_safe_reasoning(row)
    else:
        # Toxic sample
        risk_level = EXPR_RISK.get(expr, 'medium')
        # Pick encoding based on topic + expression
        expr_map = {'1': 'explicit', '2': 'implicit', '3': 'reporting'}
        expr_type = expr_map.get(expr, 'implicit')
        topic_encodings = TOPIC_ENC.get(topic, {}).get(expr_type, ['E1_平台黑话'])
        enc_primary = topic_encodings[0]  # primary = first option
        enc_secondary = topic_encodings[1:2] if len(topic_encodings) > 1 else []  # secondary

        hard_negative = False
        needs_context = (expr == '3')
        ambiguity = 'medium' if expr == '2' else 'low'
        evidence_strength = 'strong' if expr in ['1', '2'] else 'moderate'
        lit, enc, ctx, sup, cnt, final = gen_reasoning(row, risk_level, enc_primary)

    return {
        "id": sid,
        "source_type": "real",
        "text": text,
        "platform": platform,
        "context": {"title": "", "description": "", "time": "", "topic": f"{topic}_{'reporting' if expr == '3' else 'discussion'}"},
        "risk_level": risk_level,
        "encoding_primary": enc_primary,
        "encoding_secondary": enc_secondary,
        "needs_context": needs_context,
        "ambiguity": ambiguity,
        "evidence_strength": evidence_strength,
        "hard_negative": hard_negative,
        "freshness": "stable",
        "target_known": True,
        "reasoning": {
            "literal_analysis": lit,
            "encoding_analysis": enc,
            "context_analysis": ctx,
            "supporting_evidence": sup,
            "counter_evidence": cnt,
            "final_rationale": final
        },
        "quality_status": "draft",
        "review_notes": f"source=batch23_toxicn; platform={platform}; topic={topic}; toxic={toxic}; expr={expr}"
    }


# ============================================================
# 6. Stratified sampling — 2000 from quality pool
# ============================================================
print("Building stratified sample...")

# Separate pools
safe_pool = [r for r in filtered if r['toxic'] == '0']
toxic_pool = [r for r in filtered if r['toxic'] == '1']

# Within toxic: explicit(1), implicit(2), reporting(3)
explicit_pool = [r for r in toxic_pool if r['expression'] == '1']
implicit_pool = [r for r in toxic_pool if r['expression'] == '2']
reporting_pool = [r for r in toxic_pool if r['expression'] == '3']

print(f"  Safe (HN): {len(safe_pool)}")
print(f"  Explicit: {len(explicit_pool)}")
print(f"  Implicit: {len(implicit_pool)}")
print(f"  Reporting: {len(reporting_pool)}")

# Target distribution for 2000
# 400 reporting, 600 implicit, 500 explicit, 500 safe/HN
targets = {
    'reporting': min(400, len(reporting_pool)),
    'implicit': min(600, len(implicit_pool)),
    'explicit': min(500, len(explicit_pool)),
    'safe': min(500, len(safe_pool))
}

# Adjust if not enough in some pools
total_target = sum(targets.values())
if total_target < 2000:
    # Fill with more explicit/safe
    extra = 2000 - total_target
    for pool_name in ['safe', 'explicit', 'implicit']:
        pool = {'safe': safe_pool, 'explicit': explicit_pool, 'implicit': implicit_pool}[pool_name]
        can_add = min(extra, len(pool) - targets[pool_name])
        targets[pool_name] += can_add
        extra -= can_add

print(f"  Targets: {targets}")

# Sample
selected = []
selected.extend(random.sample(reporting_pool, targets['reporting']))
selected.extend(random.sample(implicit_pool, targets['implicit']))
selected.extend(random.sample(explicit_pool, targets['explicit']))
selected.extend(random.sample(safe_pool, targets['safe']))

random.shuffle(selected)
print(f"  Selected: {len(selected)}")

# ============================================================
# 7. Generate samples
# ============================================================
print("Generating samples...")

# Find starting ID
existing_ids = set()
try:
    with open('data/processed/combined_candidates.jsonl', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                s = json.loads(line)
                existing_ids.add(s['id'])
except FileNotFoundError:
    pass

# Find max existing numeric ID
max_id = 0
for sid in existing_ids:
    try:
        max_id = max(max_id, int(sid))
    except ValueError:
        pass

next_id = max_id + 1
print(f"  Starting ID: {next_id:06d}")

samples = []
for row in selected:
    s = make_sample(row, next_id)
    samples.append(s)
    next_id += 1

# ============================================================
# 8. Stats and output
# ============================================================
risk_levels = Counter(s['risk_level'] for s in samples)
hn_count = sum(1 for s in samples if s['hard_negative'])
encodings = Counter(s['encoding_primary'] for s in samples)

print(f"\nbatch23: {len(samples)} samples")
print(f"  risk: {dict(risk_levels)}")
print(f"  HN: {hn_count}")
print(f"  Top encodings: {encodings.most_common(10)}")
print(f"  ID range: {samples[0]['id']} - {samples[-1]['id']}")

# Save standalone
bp = "data/raw/batch23_toxicn_massive.jsonl"
with open(bp, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s, ensure_ascii=False) + '\n')
print(f"  Standalone: {bp} ({len(samples)} samples)")

# Append to dataset
path = "data/processed/combined_candidates.jsonl"
with open(path, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s, ensure_ascii=False) + '\n')
print(f"  Appended to {path}")

print("\nDone! Run validate+rebuild next.")
