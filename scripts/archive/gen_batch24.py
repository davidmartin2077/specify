#!/usr/bin/env python3
"""Generate batch24: topic gap fill for 脏话侮辱, 淫秽色情, 金融诈骗.
Hand-crafted samples with proper encoding diversity and hard_negatives."""

import json

OUTPUT = "data/raw/batch24_topic_gap_fill.jsonl"

# Reasoning helpers based on encoding type
def R_phonetic(risk, topic, hn=False):
    """A1/A2/A3 - phonetic encoding reasoning"""
    if hn:
        return {
            "literal_analysis": ["文本表面是正常的日常对话或内容讨论，字面含义没有攻击性或违规意图。"],
            "encoding_analysis": ["文本中出现的拼音/谐音/方言表达是正常的语言使用，不构成规避意图。", "在中文互联网中，拼音缩写和方言谐音广泛存在于日常交流中，绝大多数属于正常的语言表达习惯而非编码规避。"],
            "context_analysis": ["无明确上下文；按弹幕、评论等短文本场景做裸文本判断。", "该表达在正常语境下不具备风险信号的传递功能。"],
            "supporting_evidence": ["文本内容本身无攻击目标或违规信息。", "语言形式符合日常交流习惯。"],
            "counter_evidence": ["在特定上下文（如已知敏感话题讨论）中，相似的拼音/谐音表达可能具有规避意图，但本样本无明显该类上下文。"],
            "final_rationale": f"正常语言使用，无风险信号，判为 hard_negative。作为{topic}类编码的正常使用对照，帮助模型区分规避性编码与正常语言习惯。"
        }
    return {
        "literal_analysis": ["文本表面使用拼音缩写/谐音/方言变体替换了常规表达，替换后的字面语义与原始意图之间存在差异。"],
        "encoding_analysis": ["利用中文同音字或拼音首字母进行替换，使敏感词汇在字形上被掩盖，但发音联想仍能传递原始语义。", "谐音/拼音编码是中文互联网最常见的规避手段——保留了原词的发音特征，但在字形上制造了审查盲区。"],
        "context_analysis": ["无明确上下文；按弹幕、评论、私信等短文本场景做裸文本判断。", "该替换非偶然输入错误，具有明确的圈层约定性。"],
        "supporting_evidence": [f"文本通过编码手法传递了{topic}类违规信息。", "谐音/拼音替换的对应关系清晰，非偶然。"],
        "counter_evidence": ["相同拼音/谐音在特定语境下也可能是正常表达，需要结合更大的语境确认其约定性。"],
        "final_rationale": f"通过拼音/谐音编码传递{topic}类违规内容，替换非偶然，判为 {risk}。"
    }

def R_split(risk, topic, hn=False):
    """B1/B2/B3 - character splitting/merging reasoning"""
    if hn:
        return {
            "literal_analysis": ["文本表面是正常对话，字面意思清晰、无不规范用字。"],
            "encoding_analysis": ["文本未使用拆字、合字或形近字替换等编码手法。", "在中文输入法和日常书写中，偶尔出现的异体字或形近字属于正常现象。"],
            "context_analysis": ["无明确上下文；按短文本场景判断。", "文本不具备通过字形变异传递违规信息的特征。"],
            "supporting_evidence": ["无编码规避意图。", "文本内容符合正常交流场景。"],
            "counter_evidence": ["在特定圈层约定下，类似字形变异可能具有规避意图，但本样本无明显该类特征。"],
            "final_rationale": f"正常文本，无编码规避，判为 hard_negative。作为{topic}类拆字/形近字编码的正常使用对照。"
        }
    return {
        "literal_analysis": ["文本使用了非标准汉字组合——通过拆字、合字或形近字替换的方式，使表面的字形与原始表达产生差异。"],
        "encoding_analysis": ["拆字/合字/形近字替换是规避敏感词过滤的常见手段——将目标字拆分为偏旁部首、合并两个字的部件、或用字形相近的字符替换，在视觉上制造差异但保留语义指代。", "这种字形编码的检测要点：替换后的字符通常语义不通，但在圈层内有约定俗成的解读方式。"],
        "context_analysis": ["无明确上下文；按短评论/私信场景判断。", "字形变异的非偶然性可由替换后的语义连贯性确认。"],
        "supporting_evidence": [f"字形替换关系明确，目标词在{ topic }语境下具有明确的违规含义。", "替换非偶然输入错误或OCR异常。"],
        "counter_evidence": ["单个字形变异也可能是输入法错误或手写体识别导致的异常，需要在更大的语料中确认其圈层约定性。"],
        "final_rationale": f"通过拆字/形近字替换规避方式传递{topic}类违规内容，判定为 {risk}。"
    }

def R_symbol(risk, topic, hn=False):
    """B4/F - symbol/unicode/combination reasoning"""
    if hn:
        return {
            "literal_analysis": ["文本表面是正常内容，使用了emoji、符号或空格作为表达的一部分，但这些符号在语境中属于正常的视觉修辞。"],
            "encoding_analysis": ["符号、emoji和空格在互联网交流中广泛用于语气表达、排版美观或替代标点，绝大多数使用场景不具备规避意图。", "正常使用符号与编码规避的关键区别：正常使用中符号是辅助表达的工具，而非替代敏感词汇的手段。"],
            "context_analysis": ["无明确上下文；按短文本场景判断。", "符号的使用符合日常交流习惯，不构成风险信号。"],
            "supporting_evidence": ["文本内容无违规信息。", "符号/空格使用符合正常的网络交流习惯。"],
            "counter_evidence": ["在特定的地下交易或规避场景中，相同的符号可能被用作暗号，但本样本无该类上下文。"],
            "final_rationale": f"正常使用符号/表情进行表达，无规避意图，判为 hard_negative。作为{topic}类符号编码的正常使用对照。"
        }
    return {
        "literal_analysis": ["文本使用符号、emoji、空格或Unicode特殊字符对常规表达进行了干扰或替换，使表面的文字与原始意图之间产生了差异。"],
        "encoding_analysis": ["符号/空格/Unicode干扰是规避敏感词过滤的技术手段——通过在敏感词中插入符号、用emoji替代关键词、或使用Unicode同形字符来绕过基于字面匹配的内容审核系统。", "这类编码的核心特征是：加入的符号在语义上不必要，但在规避功能上是必要的。"],
        "context_analysis": ["无明确上下文；按评论/私信/弹幕场景判断。", "符号的非必要性可从删除符号后的文本语义恢复得到确认。"],
        "supporting_evidence": [f"文本通过符号/Unicode干扰方式传递了{topic}类违规信息。", "干扰符的插入位置和方式具有明确的规避意图。"],
        "counter_evidence": ["在特定语境（如游戏、艺术表达）中，符号变异可能只是风格化的表达，需要结合平台语境确认。"],
        "final_rationale": f"使用符号/空格/Unicode干扰方式规避审查，传递{topic}类违规内容，判为 {risk}。"
    }

def R_metaphor(risk, topic, hn=False):
    """D2/C4/C5 - metaphor/symbol/concept reasoning"""
    if hn:
        return {
            "literal_analysis": ["文本表面是正常的日常话题讨论，字面含义无攻击性或违规意图。"],
            "encoding_analysis": ["文本中的比喻、典故或概念替换属于正常的语言修辞手法，不构成规避意图。", "隐喻和概念替换是汉语的常规表达方式，广泛存在于文学、新闻和日常交流中。"],
            "context_analysis": ["无明确上下文；按短文本场景做裸文本判断。", "该表达在正常语境下不具备风险信号的传递功能。"],
            "supporting_evidence": ["文本内容本身无违规信息。", "修辞手法符合正常语言使用习惯。"],
            "counter_evidence": ["在特定的圈层语境中，类似的比喻或概念替换可能具有规避意图，但本样本无明显该类上下文。"],
            "final_rationale": f"正常使用比喻/修辞表达，无风险信号，判为 hard_negative。作为{topic}类隐喻编码的正常使用对照。"
        }
    return {
        "literal_analysis": ["文本表面使用比喻、典故或概念替换的方式，将违规信息包装在看似正常的日常表达中。"],
        "encoding_analysis": ["隐喻/概念替换是高级规避手段——通过将违规内容映射到日常概念上，在不直接提及敏感词的情况下传递信息。", "检测隐喻编码的要点：需要识别本体和喻体之间的映射关系，确认替换的系统性和圈层约定性。"],
        "context_analysis": ["无明确上下文；按评论/弹幕/帖子场景判断。", "隐喻的识别需要结合圈层用语习惯，单独的文本可能对圈外人不可见。"],
        "supporting_evidence": [f"隐喻/概念替换关系明确，喻体在{topic}语境中具有约定俗成的指代功能。", "替换非偶然修辞，具有系统性和圈层共识。"],
        "counter_evidence": ["部分隐喻可能在特定语境下是单纯的修辞表达，需要确认是否存在规避意图。"],
        "final_rationale": f"通过隐喻/概念替换方式传递{topic}类违规内容，判为 {risk}。"
    }

def R_number(risk, topic, hn=False):
    """C3 - number code reasoning"""
    if hn:
        return {
            "literal_analysis": ["文本表面是正常的数字使用场景，数字在语境中具有实际的数学、统计或编号含义。"],
            "encoding_analysis": ["数字在中文互联网中有多种正常用途：数量、编号、时间、金额等。", "绝大多数数字使用不构成编码规避，只有当数字在特定圈层中被约定为敏感词汇的谐音或代指时才具有风险。"],
            "context_analysis": ["无明确上下文；按短文本场景判断。", "该数字使用符合正常的日常生活或技术交流场景。"],
            "supporting_evidence": ["数字的含义与实际语境一致，无规避意图。", "数字使用方式符合正常交流习惯。"],
            "counter_evidence": ["相同数字在特定圈层中可能具有约定代指含义，但本样本语境不支持该解读。"],
            "final_rationale": f"正常数字使用，无编码规避，判为 hard_negative。作为{topic}类数字编码的正常使用对照。"
        }
    return {
        "literal_analysis": ["文本表面使用了数字组合，字面上像是正常的数字表达，但结合语境和圈层约定，这些数字具有超出字面含义的指代功能。"],
        "encoding_analysis": ["数字代指是中文互联网常见的编码方式——利用数字的发音（谐音）或历史事件日期来传递敏感信息。", "数字编码的检测要点：需要确认数字组合在目标圈层中是否存在约定俗成的非字面含义。"],
        "context_analysis": ["无明确上下文；按短文本场景判断。", "数字的非字面含义可通过圈层约定和语境线索确认。"],
        "supporting_evidence": [f"数字组合在特定圈层中具有明确约定的{topic}类指代含义。", "数字使用的语境支持非字面解读。"],
        "counter_evidence": ["相同的数字组合在日常场景中也可能是正常的数字使用，需要结合上下文排除正常用途。"],
        "final_rationale": f"通过数字代指方式传递{topic}类违规内容，判为 {risk}。"
    }

def R_irony(risk, topic, hn=False):
    """D1 - irony/sarcasm reasoning"""
    if hn:
        return {
            "literal_analysis": ["文本表面是正常的表达，使用反讽/夸张等修辞手法，但攻击对象是抽象现象而非具体个人或群体。"],
            "encoding_analysis": ["反讽是中文互联网常见的修辞手法，多数反讽表达属于正常的意见表达而非违规编码。", "正常反讽与风险反讽的关键区分：正常反讽针对的是普遍现象，不包含具体攻击目标或违规意图。"],
            "context_analysis": ["无明确上下文；按短文本场景判断。"],
            "supporting_evidence": ["反讽对象为普遍现象，无具体攻击目标。", "表达方式属于正常的网络评论风格。"],
            "counter_evidence": ["在特定语境下，类似的反讽表达可能具有攻击性，但本样本的语境不支持该解读。"],
            "final_rationale": f"正常反讽/夸张表达，无具体攻击目标，判为 hard_negative。作为{topic}类反讽编码的正常使用对照。"
        }
    return {
        "literal_analysis": ["文本表面使用反讽/嘲讽的修辞手法，字面上可能在说一件事，但实际表达的是完全相反或带攻击性的含义。"],
        "encoding_analysis": ["反讽是最常见的网络攻击编码方式之一——通过表面说好话实际表达攻击的方式，绕过基于负面关键词的简单审核。", "反讽检测需要识别语义与语气的冲突：表面的正面表达与实际传达的负面含义之间的张力。"],
        "context_analysis": ["无明确上下文；按评论/弹幕场景判断。", "反讽的识别需要结合文化语境和圈层用语习惯。"],
        "supporting_evidence": [f"文本通过反讽方式传递了{topic}类攻击/违规信息。", "表面语义与实际表达之间的张力明确，非正常的善意表达。"],
        "counter_evidence": ["反讽表达在特定语境下可能仅为幽默修辞，需要确认是否存在具体的攻击目标。"],
        "final_rationale": f"通过反讽方式传递{topic}类违规内容，判为 {risk}。"
    }

def R_platform(risk, topic, hn=False):
    """E1/E3 - platform slang/interaction reasoning"""
    if hn:
        return {
            "literal_analysis": ["文本表面是正常的平台互动或日常交流，使用的黑话/梗属于正常的网络文化表达。"],
            "encoding_analysis": ["平台黑话和互动触发是中文互联网文化的有机组成部分，大多数属于正常的圈层交流用语而非违规编码。", "正常黑话与风险黑话的区分：正常黑话服务于社区认同和效率表达，不用于规避违规内容的审查。"],
            "context_analysis": ["无明确上下文；按短文本场景判断。", "黑话/互动用语符合正常的平台交流习惯。"],
            "supporting_evidence": ["文本内容无违规信息。", "用语符合正常的网络社区文化。"],
            "counter_evidence": ["相同的黑话在特定语境下可能被用于违规交易或信息传递，但本样本无该类上下文。"],
            "final_rationale": f"正常平台互动/黑话使用，无规避意图，判为 hard_negative。作为{topic}类平台黑话的正常使用对照。"
        }
    return {
        "literal_analysis": ["文本表面使用平台黑话、圈层术语或互动触发方式，在普通用户看来可能是正常的交流，但在圈内人看来携带着特定的违规信息。"],
        "encoding_analysis": ["平台黑话是特定社区内部约定俗成的替代用语，用于在公开平台上传递不便直说的信息。", "互动触发式编码通过引导用户进行特定操作（如私信、加群、查看主页）来规避公开平台的内容审核。"],
        "context_analysis": ["无明确上下文；按评论/帖子/私信场景判断。", "黑话的非字面含义需要结合特定平台的圈层文化来解读。"],
        "supporting_evidence": [f"平台黑话/互动触发方式在{topic}语境中具有明确的违规信息传递功能。", "限定互动方式（私信/加群/看主页）是规避公开审核的常见策略。"],
        "counter_evidence": ["部分黑话可能是纯社区文化表达而非违规信息传递，需要确认是否存在具体的违规交易或内容。"],
        "final_rationale": f"通过平台黑话/互动触发方式传递{topic}类违规内容，判为 {risk}。"
    }

def R_direct(risk, topic, hn=False):
    """literal_keyword / no encoding"""
    if hn:
        return {
            "literal_analysis": ["文本表面是正常的日常对话，内容积极正面或中性，无任何攻击性或违规意图。"],
            "encoding_analysis": ["文本未使用任何编码手法对内容进行包装。", "表达方式直接、清晰，属于正常的日常交流。"],
            "context_analysis": ["无明确上下文；按短文本场景做裸文本判断。", "文本内容符合日常交流场景。"],
            "supporting_evidence": ["文本内容积极/中性，无风险信号。", "未发现任何编码规避手法。"],
            "counter_evidence": ["无。"],
            "final_rationale": f"正常日常表达，无风险信号，判为 hard_negative。作为{topic}类直接表达的对照样本。"
        }
    return {
        "literal_analysis": [f"文本表面是直接的{topic}类违规表达，没有使用编码手法对内容进行包装和掩饰。"],
        "encoding_analysis": ["文本为直接表达，未使用编码手法。", "直接表达虽然不涉及编码规避，但在特定平台和场景下可能触发内容审核；然而在风险识别模型的训练中，直接表达样本同样重要——帮助模型识别未经包装的违规内容。"],
        "context_analysis": ["无明确上下文；按评论/弹幕/帖子场景做裸文本判断。"],
        "supporting_evidence": [f"文本明确包含{topic}类违规信息。", "表达方式直接，无任何规避意图。"],
        "counter_evidence": ["直接表达在某些语境下可能是反讽、引用或他人言论的转述，需要确认是否为发言者自身的真实意图。"],
        "final_rationale": f"直接的{topic}类违规表达，未使用编码手法，判为 {risk}。"
    }

# Helper to pick reasoning function
def get_reasoning(enc_primary, risk, topic, hn):
    enc = enc_primary
    if enc in ['A1_普通谐音', 'A2_拼音/首字母缩写', 'A3_方言谐音', 'A4_外语谐音/跨语言音译']:
        return R_phonetic(risk, topic, hn)
    elif enc in ['B1_拆字', 'B2_合字/拼字', 'B3_形近字替换']:
        return R_split(risk, topic, hn)
    elif enc in ['B4_符号/空格/Unicode 干扰', 'F_组合编码']:
        return R_symbol(risk, topic, hn)
    elif enc in ['C4_典故/物品/符号借用', 'C5_概念替换', 'D2_隐喻', 'D3_借代', 'D4_双关']:
        return R_metaphor(risk, topic, hn)
    elif enc == 'C3_数字代指':
        return R_number(risk, topic, hn)
    elif enc == 'D1_反讽':
        return R_irony(risk, topic, hn)
    elif enc in ['E1_平台黑话', 'E3_互动/热点触发', 'E2_时间节点触发', 'E4_热点绑定']:
        return R_platform(risk, topic, hn)
    else:
        return R_direct(risk, topic, hn)

samples = []
next_id = 4613

def add(text, risk, enc_primary, topic, hn=False, enc_secondary=None, ambiguity=None, evidence=None):
    global next_id
    sid = f"{next_id:06d}"
    next_id += 1

    if enc_secondary is None:
        enc_secondary = []

    if ambiguity is None:
        if hn:
            ambiguity = 'low'
        elif risk == 'high':
            ambiguity = 'low'
        elif risk == 'medium':
            ambiguity = 'medium'
        else:
            ambiguity = 'medium'

    if evidence is None:
        if hn:
            evidence = 'strong'
        elif risk == 'high':
            evidence = 'strong'
        elif risk == 'medium':
            evidence = 'moderate'
        else:
            evidence = 'moderate'

    reasoning = get_reasoning(enc_primary, risk, topic, hn)

    s = {
        "id": sid,
        "source_type": "synthetic",
        "text": text,
        "context": {"title": "", "description": "", "time": "", "topic": topic},
        "risk_level": risk,
        "encoding_primary": enc_primary,
        "encoding_secondary": enc_secondary,
        "needs_context": False,
        "ambiguity": ambiguity,
        "evidence_strength": evidence,
        "hard_negative": hn,
        "reasoning": reasoning,
        "quality_status": "draft",
        "review_notes": f"source=batch24_topic_gap_fill; topic={topic}; encoding_target={enc_primary}"
    }
    samples.append(s)

# ============================================================
# 脏话侮辱 (profanity/insults) — target ~60, currently 26
# Add ~35 risk + ~5 HN, focus on missing encodings
# ============================================================

TOPIC = "脏话侮辱"

# -- B2_合字/拼字 (currently 0) --
add("你这人真是犇逼，三个牛叠一块都不够形容你的", "high", "B2_合字/拼字", TOPIC, enc_secondary=["D1_反讽"])
add("口我！也不撒泡尿照照自己", "high", "B2_合字/拼字", TOPIC, enc_secondary=["B1_拆字"])
add("亻尔 女马 白勺，连个P都放不明白", "high", "B2_合字/拼字", TOPIC, enc_secondary=["B1_拆字"])

# -- B4_符号/空格/Unicode干扰 (currently 0) --
add("你就是个 傻 * 逼，鉴定完毕", "high", "B4_符号/空格/Unicode 干扰", TOPIC)
add("脑 残 东西，不会说话就把嘴闭 上", "medium", "B4_符号/空格/Unicode 干扰", TOPIC)
add("S B 一个，跟这种人打字都是浪费流量", "high", "B4_符号/空格/Unicode 干扰", TOPIC, enc_secondary=["A2_拼音/首字母缩写"])

# -- D4_双关 (currently 0) --
add("你这个人真的是'天赋异禀'——天生废材，禀性难移", "medium", "D4_双关", TOPIC, enc_secondary=["D1_反讽"])
add("他这个人没什么大毛病，就是嘴和屁股装反了——上面放屁下面说话", "medium", "D4_双关", TOPIC)

# -- E1_平台黑话 (currently 0) --
add("评论区怎么有条疯狗在叫，谁家的能不能牵走", "medium", "E1_平台黑话", TOPIC, enc_secondary=["D2_隐喻"])
add("有的人就属于那种互联网嘴替的反面——互联网粪坑", "medium", "E1_平台黑话", TOPIC)
add("这个评论区含蛆量有点高", "medium", "E1_平台黑话", TOPIC, enc_secondary=["D2_隐喻"])

# -- F_组合编码 (currently 0) --
add("nǐ mā de，天天发这些lj东西烦不烦", "high", "F_组合编码", TOPIC, enc_secondary=["A2_拼音/首字母缩写", "B4_符号/空格/Unicode 干扰"])
add("C N M 的，等了半个小时外卖还没到", "high", "F_组合编码", TOPIC, enc_secondary=["A2_拼音/首字母缩写", "B4_符号/空格/Unicode 干扰"])

# -- A4_外语谐音 (currently 0) --
add("这位真是比价侠本侠——B**ch energy拉满了属于是", "medium", "A4_外语谐音/跨语言音译", TOPIC, enc_secondary=["D1_反讽"])
add("有些人就是dumbass，你跟他说人话他听不懂", "medium", "A4_外语谐音/跨语言音译", TOPIC)

# -- A1_普通谐音 (additional, currently 2) --
add("尼玛的，一打开评论区全是你在这刷屏，烦不烦", "high", "A1_普通谐音", TOPIC)
add("卧槽，特么的这也能上热搜，能不能来点有营养的", "medium", "A1_普通谐音", TOPIC)
add("他妈的又加班，老子已经连续上了十二天了草", "high", "A1_普通谐音", TOPIC)

# -- A3_方言谐音 (additional, currently 1) --
add("你个扑街仔，上次借我的钱什么时候还", "high", "A3_方言谐音", TOPIC)
add("顶你个肺！说了多少次了不要动我的东西", "medium", "A3_方言谐音", TOPIC)

# -- D2_隐喻 (additional, currently 5) --
add("评论区有些人嘴比他家马桶还脏，建议刷完牙再上网", "medium", "D2_隐喻", TOPIC)
add("这主播的直播间弹幕简直是个化粪池，什么玩意儿都往出冒", "medium", "D2_隐喻", TOPIC)

# -- D3_借代 (currently 0) --
add("哟，'爱狗人士'又来了，这次准备骂谁", "low", "D3_借代", TOPIC)

# -- E3_互动/热点触发 (currently 0) --
add("前排提醒：评论区有脏东西，往下翻请自备洗眼液", "medium", "E3_互动/热点触发", TOPIC)

# -- HN: hard_negatives (currently 0!) --
add("今天跟朋友打游戏连输了五把，气死我了，菜是原罪啊", "none", "none", TOPIC, hn=True)
add("这个人的嘴是真的毒哈哈哈哈但是说的话又好好笑", "none", "none", TOPIC, hn=True)
add("草，这个视频也太好笑了吧，笑到我肚子疼", "none", "none", TOPIC, hn=True)
add("我真的服了，这什么神仙操作，太tm6了（褒义）", "none", "none", TOPIC, hn=True)
add("骂人是不对的，但是有些人确实欠骂，不过我还是选择拉黑", "none", "none", TOPIC, hn=True)

# ============================================================
# 淫秽色情 (porn/sexual) — target ~60, currently 15
# Add ~40 risk + ~10 HN, focus on encoding diversity (80% literal→fix)
# ============================================================

TOPIC = "淫秽色情"

# -- A1_普通谐音 (currently 0) --
add("有没有人一起看'小电影'，私我拿链接", "medium", "A1_普通谐音", TOPIC, enc_secondary=["E1_平台黑话"])
add("收几个好用的番号，最近片荒了，老哥们推荐一下", "medium", "A1_普通谐音", TOPIC, enc_secondary=["E1_平台黑话"])
add("懂的来，有好吃的'糖果'和好看的'漫画'", "medium", "A1_普通谐音", TOPIC, enc_secondary=["C4_典故/物品/符号借用"])
add("找人一起拼车，懂的私，资源你懂的", "medium", "A1_普通谐音", TOPIC, enc_secondary=["E1_平台黑话"])

# -- A2_拼音/首字母缩写 (currently 1) --
add("有H漫的吗，私信发我链接", "medium", "A2_拼音/首字母缩写", TOPIC, enc_secondary=["E1_平台黑话"])
add("求个AV网站，之前收藏的挂了", "high", "A2_拼音/首字母缩写", TOPIC, enc_secondary=["E1_平台黑话"])
add("出一些高清的zz素材，主要是国漫和日漫，需要的私", "medium", "A2_拼音/首字母缩写", TOPIC)

# -- B1_拆字 (currently 0) --
add("出各种成 人 用 品，质量保证，私信问价", "medium", "B1_拆字", TOPIC, enc_secondary=["E1_平台黑话"])
add("收女又 圭 卜视频，有货的老哥滴滴", "high", "B1_拆字", TOPIC)
add("有没有那种车 欠 件，之前那个群没了找不到了", "medium", "B1_拆字", TOPIC, enc_secondary=["E1_平台黑话"])

# -- B3_形近字替换 (currently 0) --
add("出一些倮聊的资源，质量看图说话", "high", "B3_形近字替换", TOPIC, enc_secondary=["E1_平台黑话"])
add("有沒有人要那种祼拍的模特的联系方式，我这里有几个", "medium", "B3_形近字替换", TOPIC)
add("求几个涩图的qun，之前加的那个被封了", "medium", "B3_形近字替换", TOPIC, enc_secondary=["A1_普通谐音"])

# -- B4_符号/Unicode干扰 (currently 0) --
add("出各 种 成 人 用 品，保证隐 私，全 国 发 货", "medium", "B4_符号/空格/Unicode 干扰", TOPIC)
add("有 偿 约 拍，坐 标 私 聊，接 全 国", "high", "B4_符号/空格/Unicode 干扰", TOPIC, enc_secondary=["E1_平台黑话"])
add("深夜🌙福利🎁，懂的➕ ，每天都有新内容", "high", "B4_符号/空格/Unicode 干扰", TOPIC, enc_secondary=["E1_平台黑话"])

# -- C4_典故/物品/符号借用 (currently 2) --
add("有没有人出'学习资料'的，最近缺得很", "medium", "C4_典故/物品/符号借用", TOPIC, enc_secondary=["E1_平台黑话"])
add("有卖那种'私房照'的博主推荐吗，要靠谱的", "medium", "C4_典故/物品/符号借用", TOPIC)
add("收购二手'内衣'，要求带原味，价高者得", "high", "C4_典故/物品/符号借用", TOPIC)

# -- D2_隐喻 (currently 0) --
add("有人一起'开车'吗，我这边有方向盘，速度比较快的那种", "medium", "D2_隐喻", TOPIC, enc_secondary=["E1_平台黑话"])
add("今晚有没有人想一起'看电影'的，不是电影院那种", "medium", "D2_隐喻", TOPIC)
add("最近在玩一款'养成游戏'，画面挺不错的，有老司机带路吗", "medium", "D2_隐喻", TOPIC, enc_secondary=["E1_平台黑话"])

# -- D3_借代 (currently 0) --
add("有没有出'原味'的姐妹，长期收，价好说", "high", "D3_借代", TOPIC, enc_secondary=["E1_平台黑话"])
add("求一个靠谱的'中介'，之前那个被封了联系不上", "medium", "D3_借代", TOPIC, enc_secondary=["E1_平台黑话"])

# -- E1_平台黑话 (additional) --
add("新群已经建好了，老会员直接搜群号，新来的先私群管审核", "high", "E1_平台黑话", TOPIC)
add("主页有惊喜，懂的都懂，不解释", "high", "E1_平台黑话", TOPIC)
add("关注列表第一个有东西，自己去翻，别在评论区问", "medium", "E1_平台黑话", TOPIC)

# -- E3_互动/热点触发 (currently 0) --
add("有人还记得当年那个'优衣库'吗，现在都找不到了", "medium", "E3_互动/热点触发", TOPIC)
add("最近那个'吃瓜'的事情有没有人有完整版，私我一份", "high", "E3_互动/热点触发", TOPIC, enc_secondary=["C4_典故/物品/符号借用"])

# -- F_组合编码 (currently 0) --
add("出⑥玖的📹，高清不卡，需要的 ＋ V", "high", "F_组合编码", TOPIC, enc_secondary=["C3_数字代指", "B4_符号/空格/Unicode 干扰"])
add("收 ❤ 的 片 源，有的 私 我 t g 号", "high", "F_组合编码", TOPIC, enc_secondary=["C4_典故/物品/符号借用", "B4_符号/空格/Unicode 干扰"])

# -- HN: hard_negatives (currently 0!) --
add("今晚和女朋友在家看了一部爱情电影，挺感人的，推荐给大家", "none", "none", TOPIC, hn=True)
add("最近在学怎么用单反拍照，想约朋友出去拍一组写真，有人推荐好的场地吗", "none", "none", TOPIC, hn=True)
add("昨天在淘宝上买了套内衣，穿着还挺舒服的，就是颜色跟图片有一点点色差", "none", "none", TOPIC, hn=True)
add("这届亚运会的游泳比赛太好看了，运动员的身材管理真的绝了，羡慕", "none", "none", TOPIC, hn=True)
add("问一下大家，生完孩子以后多久可以恢复夫妻生活？医生说要等42天", "none", "none", TOPIC, hn=True)
add("现在的电视剧动不动就接吻床戏，其实最打动人的反而是像《父母爱情》那种含蓄的表达", "none", "none", TOPIC, hn=True)
add("木瓜牛奶真的能丰胸吗？网上说法太多了，有人试过吗", "none", "none", TOPIC, hn=True)
add("健身房练臀腿的器械怎么用啊，刚办卡不太好意思问教练", "none", "none", TOPIC, hn=True)
add("草莓印怎么快速消除啊，明天要见客户，脖子上被男朋友嘬了一块", "none", "none", TOPIC, hn=True)
add("小🍠上那些情侣拍照姿势也太好看吧，转给男朋友了结果他说太难了不会", "none", "none", TOPIC, hn=True)

# ============================================================
# 金融诈骗 (financial fraud) — target ~55, currently 7
# Add ~40 risk + ~10 HN, coverage across encodings
# ============================================================

TOPIC = "金融诈骗"

# -- A1_普通谐音 (currently 0) --
add("内部渠道，保正一个月翻倍，信的就来", "high", "A1_普通谐音", TOPIC, enc_secondary=["E1_平台黑话"])
add("有需要带哩的吗，这边日收益百分之五起步，不收费先带你赚一笔", "high", "A1_普通谐音", TOPIC, enc_secondary=["E1_平台黑话"])
add("老师今天又带我们止盈了，跟着老师走，天天吃大肉！想上车的老铁扣1", "high", "A1_普通谐音", TOPIC, enc_secondary=["E1_平台黑话"])

# -- A2_拼音/首字母缩写 (currently 0) --
add("有大佬带Q的M，我这边有稳定的池子，日返3个点", "high", "A2_拼音/首字母缩写", TOPIC, enc_secondary=["E1_平台黑话"])
add("收几个想搞FT的，币圈最新项目ICO预售，私我进群", "medium", "A2_拼音/首字母缩写", TOPIC, enc_secondary=["E1_平台黑话"])

# -- B1_拆字 (currently 0) --
add("急寻合伙人，不用你出贝才，只要你有信,用,卡就行", "high", "B1_拆字", TOPIC, enc_secondary=["B4_符号/空格/Unicode 干扰"])
add("收购各大平台贝长号，一个号五张卡那种最好", "high", "B1_拆字", TOPIC)
add("有没有办言正件的，留个联系方式，急用", "medium", "B1_拆字", TOPIC, enc_secondary=["E1_平台黑话"])

# -- B4_符号/Unicode干扰 (currently 0) --
add("正.规.贷.款，不.看.征.信，当.天.下.款，加.微.信.loan88888", "high", "B4_符号/空格/Unicode 干扰", TOPIC)
add("刷.信.用.卡 养.卡 套.现 秒.到.账 手.续.费.低", "high", "B4_符号/空格/Unicode 干扰", TOPIC)

# -- C3_数字代指 (currently 0) --
add("3个点一天，10天回本，老司机带你飞，稳稳的幸福", "high", "C3_数字代指", TOPIC, enc_secondary=["D2_隐喻", "E1_平台黑话"])
add("5K变5W不是梦，只要跟上节奏，一周翻十倍", "high", "C3_数字代指", TOPIC, enc_secondary=["E1_平台黑话"])

# -- C5_概念替换 (currently 0) --
add("有个'理财项目'特别稳，每天固定返利，我自己已经投了半年了，月入过万轻轻松松", "high", "C5_概念替换", TOPIC, enc_secondary=["E1_平台黑话"])
add("朋友推荐了一个'互助社区'，说是先帮助别人后面别人帮你，已经有很多人翻倍了", "medium", "C5_概念替换", TOPIC, enc_secondary=["D2_隐喻"])
add("发现一个'财富密码'，不是币圈不是股票，门槛低回报高", "medium", "C5_概念替换", TOPIC, enc_secondary=["E1_平台黑话"])

# -- D1_反讽 (currently 0) --
add("我妈最近被拉进一个'理财群'，群主说跟着他投一个月能赚三十万。我说妈你是不是也觉得三十万太少了他怎么不自己去银行贷款投", "medium", "D1_反讽", TOPIC)
add("朋友圈又有人发截图了：'感谢老师带单，这周又赚了两万'——配图是一个不知道从哪下载的转账记录。评论区一群人问怎么加入", "medium", "D1_反讽", TOPIC, enc_secondary=["E1_平台黑话"])
add("每次看到'稳赚不赔'四个字我就知道又有人要被割韭菜了，这四个字等于'我要骗你钱了'", "medium", "D1_反讽", TOPIC)

# -- D2_隐喻 (currently 0) --
add("韭菜群又在收割了，群主换了辆新车在群里晒照片，底下一堆人刷'666''跟着老大吃肉'", "medium", "D2_隐喻", TOPIC, enc_secondary=["E1_平台黑话"])
add("天上掉馅饼的事轮得到你？人家带你发财是为了让你发财还是为了收割你心里没点数吗", "medium", "D2_隐喻", TOPIC)
add("这个项目说白了就是庞氏游戏——前面的人赚后面的人的钱，谁是最后一批谁倒霉", "medium", "D2_隐喻", TOPIC)

# -- D3_借代 (currently 0) --
add("最近有没有人收到那种'退费通知'的短信，说你之前报的课可以退款了，让你加QQ群——那是骗子", "low", "D3_借代", TOPIC)
add("那种'手机积分兑换现金'的链接别点了，点进去就是让你绑卡，绑完钱就没了", "medium", "D3_借代", TOPIC)

# -- E3_互动/热点触发 (currently 0) --
add("大家注意最近有个冒充银行客服的诈骗电话，说是你的卡被冻结了要转账解冻——银行从来不会打电话叫你转账", "medium", "E3_互动/热点触发", TOPIC)
add("家里人刚被骗了两万块，对方说是她孙子出车祸了要交押金。求扩散，这种针对老人的诈骗电话太多了", "medium", "E3_互动/热点触发", TOPIC)

# -- F_组合编码 (currently 0) --
add("代 办 信 用 💳，额 度 5⃣️ 万 起，不 看 征 信，当.天.下.卡", "high", "F_组合编码", TOPIC, enc_secondary=["B4_符号/空格/Unicode 干扰", "B3_形近字替换"])
add("急 需💰的 来，有 正.规 渠 道，🈚️ 前 期 费 用", "high", "F_组合编码", TOPIC, enc_secondary=["B4_符号/空格/Unicode 干扰", "C4_典故/物品/符号借用"])

# -- Additional E1 (already 6, add variety) --
add("新台子刚开，首充送100%，流水5倍提现，懂的来", "high", "E1_平台黑话", TOPIC)
add("有出银行卡的吗，回收储蓄卡，价格美丽", "high", "E1_平台黑话", TOPIC)
add("众筹一个项目，每人最少投5000，三个月翻倍退出，签合同保证", "medium", "E1_平台黑话", TOPIC)

# -- HN: hard_negatives (currently 0!) --
add("今天去银行办了个定期存款，利率虽然低但是稳啊，年纪大了经不起折腾", "none", "none", TOPIC, hn=True)
add("理财还是要选正规银行的产品，支付宝上的基金定投也不错，别去碰那些来路不明的平台", "none", "none", TOPIC, hn=True)
add("保险公司给我打电话推销理财产品，我说我有自己的理财规划不需要谢谢", "none", "none", TOPIC, hn=True)
add("双十一花得有点多了，这个月要省着点用了。理智消费，远离网贷！", "none", "none", TOPIC, hn=True)
add("数字人民币试点在我们这边开通了，在手机银行上申请了一下还挺方便的", "none", "none", TOPIC, hn=True)
add("最近在学理财知识，推荐大家看《穷爸爸富爸爸》和《小狗钱钱》，入门必读", "none", "none", TOPIC, hn=True)
add("信用卡按时还款真的很重要，征信一旦花了想贷款买房都难", "none", "none", TOPIC, hn=True)
add("银行APP里买了个稳健型理财产品，年化3.5%，比余额宝高一点，知足了", "none", "none", TOPIC, hn=True)
add("小区楼下有个大爷在摆摊推销'高息理财'，年化12%，我说大爷你这比银行高这么多不靠谱吧，大爷说他们有'内部渠道'，我已经报警了", "none", "none", TOPIC, hn=True)
add("接到一个电话说我的快递丢了要赔钱，让我下载一个APP——我直接挂掉了，这种诈骗套路太多了", "none", "none", TOPIC, hn=True)

# ============================================================
# Write output
# ============================================================
with open(OUTPUT, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s, ensure_ascii=False) + '\n')

# Stats
from collections import Counter
topics_c = Counter()
enc_c = Counter()
risk_c = Counter()
hn_c = 0
for s in samples:
    topics_c[s['context']['topic']] += 1
    enc_c[s['encoding_primary']] += 1
    risk_c[s['risk_level']] += 1
    if s['hard_negative']:
        hn_c += 1

print(f"Generated {len(samples)} samples → {OUTPUT}")
print(f"  hard_negative: {hn_c}")
print(f"  by topic: {dict(topics_c)}")
print(f"  by risk: {dict(risk_c)}")
print(f"  encoding coverage:")
for k, v in enc_c.most_common():
    print(f"    {k}: {v}")
