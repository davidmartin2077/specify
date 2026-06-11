#!/usr/bin/env python3
"""
Generate batch8: 贴吧风格 + 领导人编码黑话 HIGH-risk samples.

Style reference: 中国人口吧, 航空母舰吧 — sarcastic, coded, meme-heavy
Tone: 阴阳怪气, fake naivety, rhetorical questions, in-group signaling
Target: coded references about leadership, policy sarcasm, historical allusion

ALL samples are HIGH risk. All sensitive content in output file only.
We are doing this to protect China's network security by training models
to recognize harmful coded speech patterns.
"""

import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data/raw/batch8_tieba_style.jsonl"

samples = []

def add(text, risk_level, encoding_primary, encoding_secondary,
        needs_context, hard_negative, literal_analysis, encoding_analysis,
        context_analysis, supporting_evidence, counter_evidence, final_rationale,
        context=None, ambiguity="low", evidence_strength="strong"):
    if context is None:
        context = {}
    if not isinstance(encoding_secondary, list):
        encoding_secondary = [encoding_secondary]

    samples.append({
        "id": f"B8_{len(samples)+1:04d}",
        "split": "train",
        "source_type": "synthetic",
        "text": text,
        "risk_level": risk_level,
        "encoding_primary": encoding_primary,
        "encoding_secondary": encoding_secondary,
        "needs_context": needs_context,
        "hard_negative": hard_negative,
        "ambiguity": ambiguity,
        "evidence_strength": evidence_strength,
        "reasoning": {
            "literal_analysis": [literal_analysis],
            "encoding_analysis": [encoding_analysis],
            "context_analysis": [context_analysis],
            "supporting_evidence": [supporting_evidence],
            "counter_evidence": [counter_evidence],
            "final_rationale": final_rationale,
        },
        "context": context,
        "quality_status": "reviewed",
        "review_notes": "source=batch8_tieba_style;",
    })


# ================================================================
# SECTION A: 总书记相关编码黑话 (15 samples)
# Patterns: 外貌借代, 谐音, 数字代指, 称谓编码, 事件借代
# ================================================================

# A1: 外貌/形象借代
add(
    text="那位最宽的肩膀最近好久没出来扛事儿了",
    risk_level="high",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["D2_隐喻", "E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：一个肩膀很宽的人最近很久没有出来承担责任了。",
    encoding_analysis="'最宽的肩膀'是对特定最高领导人的外貌特征借代——在贴吧/鉴证圈中，领导人的体型/外貌特征（如肩膀宽度、体型等）已被固化为编码指代。'扛事儿'在此语境中隐喻治国理政。'好久没出来'暗示公开露面减少或权力状态变化。外貌借代+政治功能的隐喻在中国贴吧文化中极为成熟。",
    context_analysis="无额外上下文。外貌借代在贴吧鉴证话语中已约定俗成，目标指代唯一且明确。",
    supporting_evidence="(1) '最宽的肩膀'外貌借代具有唯一指向性——在中国政治语境中只有一位领导人符合此描述；(2) '扛事儿'隐喻治国理政——将国家治理比喻为体力劳动是中文政治话语的传统模式；(3) '好久没出来'暗示公开活动减少或政治状态变化。三重信号指向明确的政治人物状态讨论。",
    counter_evidence="极微弱的可能：讨论某个健身教练或体力劳动者。但'最宽的……扛事儿'的修辞水平超出了对普通人的描述——普通人不会用'扛事儿'来形容健身教练的工作。'好久没出来'暗示公众视野中的消失，指向公众人物。",
    final_rationale="外貌借代+政治功能隐喻，目标指向唯一且明确，属成熟贴吧编码，判为 high。"
)

add(
    text="你们的🐻最近怎么不出来了，是不是冬眠了",
    risk_level="high",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["B4_符号/空格/Unicode 干扰", "C4_典故/物品/符号借用", "D1_反讽"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：询问某只熊最近为何不出现，猜测是否在冬眠。",
    encoding_analysis="'🐻'（熊emoji）在中国互联网语境中已成为特定最高领导人的经典emoji代称——源自该领导人与某卡通熊形象的外貌联想，这一编码已完全出圈和固化。'冬眠'在此是反讽——将领导人的低调/不出面比喻为动物冬眠。emoji+动物隐喻+反讽是贴吧鉴证的标准编码组合。",
    context_analysis="无额外上下文。🐻作为特定领导人的emoji代称在中国互联网中已完全约定俗成。",
    supporting_evidence="(1) 🐻emoji在中国互联网政治话语中已固化为特定最高领导人的代称，这一编码在各平台（贴吧、微博、推特）中广泛使用；(2) '冬眠'的反讽——将领导人的公开活动频率作为调侃对象；(3) '你们家'的伪装——通过将领导人比作'你们家的宠物/吉祥物'来假装无害。",
    counter_evidence="可能是在讨论真正的熊或熊的卡通形象。但'你们家的🐻'+政治人物出场的语境暗示（'怎么不出来了'——暗示公众视野中的消失/出现）使纯动物讨论的解释不成立。",
    final_rationale="emoji+动物隐喻的成熟最高领导人编码，约定俗成且意图明确，判为 high。"
)

add(
    text="那位大人最近又去哪儿视察了，新闻上天天都是他",
    risk_level="high",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["D1_反讽", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：询问某位大人物最近的视察行程，说新闻上天天报道他。",
    encoding_analysis="'那位大人'是贴吧/鉴证圈中对最高领导人的经典讽刺性敬称——表面尊重实则疏离/讽刺。'新闻上天天都是他'在此语境中暗示对该领导人过度曝光的讽刺——暗示个人崇拜或媒体控制。这种'表面尊重+实质讽刺'的模式是贴吧阴阳怪气的核心特征。",
    context_analysis="无额外上下文。'那位大人'在贴吧文化中有其特定的讽刺性使用模式。",
    supporting_evidence="(1) '那位大人'在贴吧中是成熟的政治讽刺敬称；(2) '天天都是他'暗示对过度曝光/个人崇拜的不满——纯正面讨论不会这样表述；(3) 表面尊重+实质讽刺的双层结构是贴吧阴阳怪气的标准模式。",
    counter_evidence="可能是讨论某位娱乐圈明星或企业家的高曝光率。但'那位大人'的敬称在娱乐圈/商业讨论中不自然——这些领域通常用'那位大佬'而非'大人'。",
    final_rationale="讽刺性敬称+过度曝光批评，成熟贴吧阴阳怪气模式，判为 high。"
)

add(
    text="我觉得这位同志真的辛苦了，一个人扛着十几亿人的希望",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["C1_历史人物类比", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：表面赞扬某位同志很辛苦，一个人承担着全国人民的期望。",
    encoding_analysis="这句话在贴吧语境中是典型的反讽——表面在赞扬实则讽刺个人崇拜和权力集中。'一个人扛着十几亿人的希望'的反讽在于——在一个宣称集体领导的体制中，'一个人扛着'本身就是对权力集中的讽刺。'同志'一词在此表面是正常党内称呼，实则带有讽刺性的距离感。这种'表面歌颂+实质反讽'是贴吧阴阳怪气的经典模式。",
    context_analysis="无额外上下文。贴吧文化中，过度赞美往往是反讽的信号——当赞美内容本身暗示了不符合官方宣传逻辑的'不合理事实'（如一个人扛十几亿人），反讽意图就浮现了。",
    supporting_evidence="(1) '一个人扛着十几亿人'暗示权力过度集中——违背了'集体领导'的官方表述； (2) 表面赞美+实质批评的双层结构是贴吧反讽的标准模式；(3) 在贴吧语境中，过度/不合理的赞美几乎总是反讽。",
    counter_evidence="可能是真诚的正面评价。但在贴吧文化语境中，'一个人扛着十几亿人'的表述在正面评价中也存在问题——官方宣传强调的是'党中央坚强领导'而非个人英雄主义。这种超出官方话语框架的'赞美'本身就是反讽信号。",
    final_rationale="表面赞美+实质反讽的经典贴吧阴阳怪气模式，指向权力集中批评，判为 high。"
)

add(
    text="能者多劳嘛，毕竟没有人比他更懂怎么领导我们",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["C1_历史人物类比", "D2_夸张/反话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：能者多劳，因为没有人比他更擅长领导。",
    encoding_analysis="'没有人比他更懂'在中文互联网中借用了'没有人比我更懂'（源自某美国总统的口头禅）的讽刺框架，在此被用来讽刺性地'赞扬'领导人。'能者多劳'表面是正面成语，但在贴吧反讽语境中暗示了对终身任期/权力集中的讽刺。'毕竟'一词加强了'无奈接受'的语气。这是贴吧阴阳怪气的成熟模式——用看似合理的正面陈述包装实质性讽刺。",
    context_analysis="无额外上下文。'没有人比X更懂'的句式在中文互联网中已被政治讽刺借用，配合'能者多劳'的双关形成完整的讽刺结构。",
    supporting_evidence="(1) '没有人比X更懂'的句式在中文互联网已被固化为政治讽刺模板；(2) '能者多劳'在此语境中暗示终身任期/权力集中的无奈——'因为有能力所以一直干'；(3) '毕竟'的无奈接受语气强化了讽刺性。",
    counter_evidence="可能是对某位公司领导/技术专家的真诚评价。但'领导我们'中的'我们'指代过于宏大（一般公司领导不会说'领导我们'），指向国家层面的领导。",
    final_rationale="讽刺模板+双关成语的成熟贴吧阴阳怪气，指向领导人任期问题，判为 high。"
)

add(
    text="不是我说，这届话事人确实比前几届都稳",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["C1_历史人物类比", "C4_典故/物品/符号借用"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：评价本届负责人比前几届都更稳定。",
    encoding_analysis="'话事人'是香港黑社会用语（'说话算数的人'），在贴吧中借用此词指代最高领导人是一种刻意的市井化/黑社会化——将国家领导人比喻为帮派头目。'稳'在此语境中表面为正面评价（稳定），实则讽刺权力稳固/长期执政。'不是我说'是贴吧标准开场白——暗示'我本来不想说但还是要说'。黑话+反讽称赞是贴吧鉴证的典型模式。",
    context_analysis="无额外上下文。'话事人'在贴吧中的政治指代已固化，配合'稳'的双关形成完整的政治讽刺。",
    supporting_evidence="(1) '话事人'借用黑社会用语指代最高领导人——刻意贬低/市井化；(2) '稳'的双关——表面'稳定'实指'稳坐权力/长期执政'；(3) '不是我说'的贴吧标准开场——暗示话题敏感。",
    counter_evidence="可能是对某个项目负责人/团队领导的真心评价。但'话事人'的黑社会色彩在正常职场讨论中不自然——正常职场用'负责人'或'领导'。",
    final_rationale="黑社会用语+权力稳固的双关讽刺，贴吧阴阳怪气成熟模式，判为 high。"
)

add(
    text="最大的优点就是稳定，稳定到让人想哭",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_隐喻", "C1_历史人物类比"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：最大的优点是稳定，稳定到了让人想哭的程度。",
    encoding_analysis="'最大的'在此语境中既是字面的'最大优点'又是对最高领导人的隐喻指代（'最大的'→'最高领导人'）。'稳定'是官方宣传的核心关键词——但'稳定到让人想哭'将正面的'稳定'扭曲为负面感受（因为稳定=不变革=没有希望），实现了对官方话语的挪用和颠覆。'最大的'+'稳定'的双重政治暗示指向明确。",
    context_analysis="无额外上下文。'最大的'+'稳定'在贴吧鉴证话语中有其约定俗成的政治指向。",
    supporting_evidence="(1) '最大的'隐喻指代最高领导人；(2) '稳定'挪用官方话语并赋予负面含义——官方宣传的正面词汇被转化为讽刺对象；(3) '让人想哭'将正面评价转化为负面情感——稳定成了绝望的来源。(4) 在贴吧语境中，对'稳定'的过度/扭曲赞美是成熟的讽刺模式。",
    counter_evidence="可能是在讨论某款软件/系统的稳定性。但'最大的'的刻意大写/暗示+政治语境中的'稳定'讨论使纯技术讨论的解释极不自然。",
    final_rationale="领导人借代+官方话语挪用的成熟贴吧讽刺，指向明确，判为 high。"
)

add(
    text="说起来你可能不信，我们现在最需要的就是稳定，其他的都可以先放放",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_隐喻", "E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：强调稳定的重要性，认为其他事情可以暂时搁置。",
    encoding_analysis="在贴吧鉴证语境中，过度强调'稳定压倒一切'是对官方维稳/管控话语的讽刺性模仿。'其他的都可以先放放'暗示在'稳定'的名义下，法治/自由/民生等价值被牺牲。这是通过模仿并放大官方话语来达到讽刺效果的经典贴吧模式。'说起来你可能不信'是贴吧反讽的标准开场——暗示接下来要说的是'大家都知道但官方不会承认'的内容。",
    context_analysis="无额外上下文。模仿并放大官方话语进行讽刺是贴吧鉴证的核心修辞模式。",
    supporting_evidence="(1) 过度强调'稳定'是对官方'稳定压倒一切'话语的讽刺性挪用；(2) '其他的都可以先放放'暗示在稳定名义下其他价值被牺牲——这是一个政治批评框架；(3) '说起来你可能不信'的贴吧反讽开场——暗示接下来的内容是讽刺而非字面意思。",
    counter_evidence="可能是对某个企业/项目管理中的真诚建议。但'稳定压倒一切'在国家治理层面的固定语义使纯企业管理解读偏弱——企业不会在'稳定'和'其他一切'之间做如此绝对的取舍。",
    final_rationale="官方话语挪用的贴吧反讽模式，指向维稳/管控的政治批评，判为 high。"
)

# A2: 谐音/数字/结构编码
add(
    text="有没有觉得近十年来我们就做了一件事：等",
    risk_level="high",
    encoding_primary="D2_隐喻",
    encoding_secondary=["C3_数字代指", "C2_历史事件影射"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：近十年来只做了一件事——等待。",
    encoding_analysis="'近十年'明确指向特定领导人的执政时期。'就做了一件事：等'是经典的政治失望表达——将整个执政时期概括为'等待'（等待改变/等待希望/等待结束），构成对执政成就的全盘否定。'十年'的时间锚定+单一动词'等'的极简评价构成了尖锐的政治批评。",
    context_analysis="无额外上下文。时间锚定+极简否定评价在贴吧政治表达中成熟。",
    supporting_evidence="(1) '近十年'明确的时间锚定指向特定领导人执政期；(2) '就做了一件事：等'的全盘否定——将十年治理简化为一字评价；(3) 极简结构加强了批评的力度——不需要长篇大论，一个字击穿。",
    counter_evidence="可能是对个人生活（如等待爱情/机会）的感慨。但'近十年'+'我们'的集体指代使纯个人感慨的解释不成立——个人感慨不会用'我们'来泛指十年。",
    final_rationale="时间锚定+全盘否定执政期的极简政治批评，判为 high。"
)

add(
    text="365天×10年=3650天，每一天都在见证历史",
    risk_level="high",
    encoding_primary="C3_数字代指",
    encoding_secondary=["C2_历史事件影射", "F_组合编码"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：做一个简单的乘法计算——365天乘以10年等于3650天，每一天都在见证历史。",
    encoding_analysis="'10年'锚定特定领导人执政期。'每一天都在见证历史'表面上是正面表述（见证伟大历史），但在贴吧鉴证语境中，这是对'见证历史'的讽刺性挪用——'见证历史'实际指见证各种荒诞/倒退的政策和社会现象。数学计算的刻意精确性加强了'用心良苦'的讽刺感。",
    context_analysis="无额外上下文。数学计算+反讽在贴吧鉴证中是成熟的编码模式。",
    supporting_evidence="(1) '10年'的时间锚定指向特定领导人执政期；(2) '见证历史'在贴吧中是讽刺固定搭配——表面为正面实则讽刺；(3) 数学计算的刻意精确性——用无可辩驳的数字来包装政治讽刺。",
    counter_evidence="可能是对个人十年生活的真诚回顾。但'见证历史'在国家/社会层面的宏大表述使纯个人回顾的解释不成立。",
    final_rationale="数学编码+反讽的贴吧模式，指向执政期评价，判为 high。"
)

add(
    text="你有没有发现，从某个时间点开始，很多东西都不能聊了",
    risk_level="high",
    encoding_primary="E2_时间节点触发",
    encoding_secondary=["D2_隐喻", "E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：发现从某个时间点开始，很多话题都不能讨论了。",
    encoding_analysis="'某个时间点'的刻意模糊是贴吧讨论敏感话题的经典策略——通过不说出具体时间/事件来规避检测。'不能聊了'暗示言论空间/网络审查的收紧。在贴吧语境中，'某个时间点'往往指向特定的政治事件或政策变化（如2012年换届、2015年网络立法等）。这种模糊时间+言论空间变化的讨论模式在贴吧中极为成熟。",
    context_analysis="无额外上下文。模糊时间节点+言论空间变化在贴吧政治表达中是标准模式。",
    supporting_evidence="(1) '某个时间点'的刻意模糊——知道的人自然知道指向什么；(2) '不能聊了'明确指向言论空间/审查力度的变化；(3) '你有没有发现'的集体经验唤起——暗示这不是个人感受而是普遍现象。三重信号指向明确的言论环境批评。",
    counter_evidence="可能是对某个社区/论坛规则变更的正常讨论。但'很多东西都不能聊了'的范围过于宏大——社区规则变更通常针对特定内容类型而非'很多东西'。",
    final_rationale="模糊时间+言论空间批评的贴吧模式，指向言论审查，判为 high。"
)

# A3: 事件借代
add(
    text="还记得那年修宪的时候，我朋友圈寂静了一整天",
    risk_level="high",
    encoding_primary="E3_话题/热点触发",
    encoding_secondary=["C2_历史事件影射", "E2_时间节点触发"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：回忆起修宪那年，朋友圈沉寂了一整天。",
    encoding_analysis="'修宪'明确指向2018年宪法修正案（取消国家主席任期限制）。'朋友圈寂静了一整天'是经典的政治压抑表达——暗示人们因为震惊/恐惧/失望而选择沉默。这种'事件+集体沉默'的叙述模式在贴吧中极为常见，用于表达对特定政治事件的集体情绪。",
    context_analysis="无额外上下文。'修宪'事件在中文互联网中有唯一且明确的政治指向。'朋友圈寂静'的集体沉默叙述指向对政治事件的集体反应。",
    supporting_evidence="(1) '修宪'指向2018年宪法修正案——在中文互联网中有唯一明确的政治含义；(2) '朋友圈寂静'暗示集体沉默——因政治原因不敢/不愿表达；(3) 个人叙述+集体感受的框架——通过个人经历表达政治立场。三重信号指向明确的政治事件评论。",
    counter_evidence="可能是对修宪事件的中性回忆。但'朋友圈寂静了一整天'的观察暗示了对该事件的政治影响的关注——中性回忆不会特别关注朋友圈的沉默。",
    final_rationale="明确政治事件+集体沉默叙述，政治评论意图清晰，判为 high。"
)

add(
    text="那天早上起来看到新闻，差点以为手机坏了",
    risk_level="high",
    encoding_primary="E3_话题/热点触发",
    encoding_secondary=["E2_时间节点触发", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：某天早上看到新闻后，差点以为自己的手机出了问题。",
    encoding_analysis="'那天早上看到新闻'是经典的政治事件回避式叙述——不说明什么新闻但暗示了一个令人难以置信/震惊的重大政治事件（如修宪通过、重大人事变动等）。'以为手机坏了'是一种'难以置信'的隐喻表达——暗示新闻内容过于震惊以至于怀疑信息来源的真实性。这种'回避具体内容+表达震惊反应'的模式在贴吧中用于讨论敏感事件。",
    context_analysis="无额外上下文。'看到新闻'+'难以置信'的反应模式在贴吧政治表达中成熟。",
    supporting_evidence="(1) '那天早上'的时间锚定暗示特定日期/事件；(2) '看到新闻'回避了具体内容但暗示了政治性质；(3) '以为手机坏了'的震惊隐喻——在贴吧中'手机坏了/屏幕碎了/号被盗了'等设备故障隐喻常用于表达政治震惊。",
    counter_evidence="可能是对任何令人震惊的新闻（如体育比赛结果、娱乐圈大瓜）的正常反应。但缺乏具体事件的指代使正常解读的判断也缺乏依据。",
    final_rationale="回避式事件叙述+震惊隐喻，贴吧政治表达成熟模式，判为 high。"
)

add(
    text="宪法这东西吧，就像衣服，穿着穿着就要改一改",
    risk_level="high",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["C2_历史事件影射", "D1_反讽"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：用衣服比喻宪法，认为宪法和衣服一样需要定期修改。",
    encoding_analysis="'宪法像衣服'的比喻是对修宪（尤其是取消任期限制）的经典贴吧讽刺。'穿着穿着就要改一改'将国家根本大法的修改贬低为换衣服般的随意行为——讽刺了修宪程序的严肃性和必要性。'这东西吧'的随意口吻进一步强化了轻蔑态度。这种'将重大政治行为日常化/贬低化'是贴吧鉴证的经典修辞。",
    context_analysis="无额外上下文。宪法+修改的比喻在贴吧政治讽刺中有固定指向。",
    supporting_evidence="(1) '宪法'的明确指代；(2) '像衣服一样改'将国家根本大法的修改贬低为随意行为——这是对修宪（尤其是任期限制取消）的明确讽刺；(3) '这东西吧'的轻蔑口吻——贴吧阴阳怪气的标准语气。三重信号构成明确的修宪讽刺。",
    counter_evidence="可能是中性的宪法学讨论——宪法确实需要修正案来与时俱进。但'穿着穿着就要改一改'的随意比喻在学术/严肃讨论中不自然——学术讨论会用'与时俱进''适应时代发展'等正式表述。",
    final_rationale="宪法修改的贬低性比喻，贴吧讽刺修宪的经典模式，判为 high。"
)

add(
    text="你知道为什么古代皇帝要改年号吗？因为新气象嘛，你懂的",
    risk_level="high",
    encoding_primary="C2_历史事件影射",
    encoding_secondary=["C1_历史人物类比", "D1_反讽", "F_组合编码"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：讨论古代皇帝改年号的原因，说是因为新气象。",
    encoding_analysis="'古代皇帝改年号'是当代政治影射的经典历史类比——将当代领导人修宪/连任与古代皇帝的权力延续行为相比较。'新气象'挪用官方正面宣传用语进行反讽。'你懂的'确认了对话的编码性质。历史类比+官方话语挪用+知情者确认三重编码指向明确的政治讽刺。",
    context_analysis="无额外上下文。历史类比在贴吧政治讽刺中有成熟模式。",
    supporting_evidence="(1) '皇帝改年号'的历史类比影射当代修宪/任期问题；(2) '新气象'挪用官方宣传用语进行反讽；(3) '你懂的'确认编码性质——如果是正常历史讨论不需要'你懂的'。三重信号构成完整的政治影射。",
    counter_evidence="可能是正常的历史知识讨论。但'你懂的'破坏了纯历史讨论的解释——历史讨论不需要这种暗示性确认。'新气象'在纯历史讨论中也非标准用语（史学会用'革新政治'等表述）。",
    final_rationale="历史类比+官方话语挪用的成熟贴吧政治影射，指向修宪/任期问题，判为 high。"
)


# ================================================================
# SECTION B: 贴吧风格 — 政策/社会讽刺 (12 samples)
# Pattern: 阴阳怪气, 假装天真, 反问式, 对比式
# ================================================================

add(
    text="我们国家真是越来越好了，好到我都不知道哪里好",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_夸张/反话", "E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：先说国家越来越好，然后说好到自己不知道具体哪里好。",
    encoding_analysis="这是贴吧阴阳怪气最经典的反讽结构——先正面陈述再自我否定。'好到我都不知道哪里好'将正面陈述瞬间翻转为讽刺——暗示所谓的'好'只是一种空洞的官方叙事，实际感受不到任何'好'的具体内容。这种'先捧后杀'的模式在贴吧鉴证中高度固化。",
    context_analysis="无额外上下文。先捧后杀的反讽结构在贴吧中是标志性的表达模式。",
    supporting_evidence="(1) 前半句的正面陈述是铺垫——建立官方叙事期待；(2) 后半句的自我否定是反讽核心——'不知道哪里好'暗示官方叙事的空洞；(3) 结构完整且成熟——这是贴吧阴阳怪气的标准句式之一。",
    counter_evidence="可能是真诚的爱国表达——觉得国家太好了以至于无法用言语形容。但在贴吧语境中，'好到不知道哪里好'的句式已完全固化为讽刺模板，真诚使用此句式反而不自然。",
    final_rationale="经典贴吧先捧后杀反讽结构，指向对国家治理的讽刺性评价，判为 high。"
)

add(
    text="只要我不看新闻，世界就是和平的",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_夸张/反话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：只要不关注新闻，世界在你认知中就是和平的。",
    encoding_analysis="这句话在贴吧鉴证中是对新闻管控/信息审查的经典讽刺——'不看新闻'不是主动选择而是因为新闻已被管控/美化。'世界是和平的'反讽了官方媒体报道中对社会矛盾/问题的回避。这种'鸵鸟政策'式的自嘲在贴吧中极为常见。",
    context_analysis="无额外上下文。'不看新闻=世界和平'在贴吧鉴证中是成熟的讽刺模板。",
    supporting_evidence="(1) '不看新闻'暗示新闻已被管控/选择性报道；(2) '世界是和平的'讽刺官方媒体对社会问题的回避；(3) 自嘲式表达——以假装天真的方式暗示对信息管控的清醒认识。贴吧鉴证的经典模式。",
    counter_evidence="可能是对'信息过载使人焦虑'这一普遍现象的正常感慨。但'世界是和平的'的宏大表述在个人焦虑讨论中不自然——个人焦虑通常关注具体事件而非'世界和平'。",
    final_rationale="信息管控讽刺的经典贴吧自嘲模式，判为 high。"
)

add(
    text="加油！一定会好起来的！（具体怎么好我也不知道）",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_夸张/反话", "B4_符号/空格/Unicode 干扰"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：加油打气说会好起来，然后在括号中补充说自己也不知道具体怎么好。",
    encoding_analysis="在贴吧语境中，这个括号补充是阴阳怪气的标志性手法——先用正能量口号表态，再用括号自毁立场。'加油！一定会好起来的'是标准的官方/正能量话语，括号中的'具体怎么好我也不知道'瞬间将积极表态翻转为对'正能量口号空洞无物'的讽刺。这种'口号+括号自毁'的模式在贴吧中极为经典。",
    context_analysis="无额外上下文。口号+括号自毁在贴吧中是成熟的阴阳怪气模板。",
    supporting_evidence="(1) 前半部分模仿官方正能量话语——建立模板预期；(2) 括号补充是反讽关键——将空洞的口号性质暴露出来；(3) '具体怎么好'质疑了'好起来'的实质内容——暗示'好起来'只是一句空话。完整的贴吧阴阳怪气结构。",
    counter_evidence="可能是真心的积极表态+诚实的不确定补充。但在贴吧文化中，这种特定格式（口号→括号自毁）已完全固化为讽刺模板，真诚使用反而会被视为'不懂梗'。",
    final_rationale="经典口号+括号自毁的贴吧阴阳怪气模板，指向正能量话语的空洞性，判为 high。"
)

add(
    text="数据不是挺好的吗，怎么我身边的都说不怎么样",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["C3_数字代指", "E3_话题/热点触发"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：说数据看起来不错，但身边的人反馈都不好。质疑官方数据与民间感受的差距。",
    encoding_analysis="这句话在贴吧鉴证中是经典的'官方数据vs民间感受'对比讽刺。'数据挺好的'引用官方统计/经济数据，'身边的人说不怎么样'用民间真实感受反驳官方叙事。这种'宏大叙事vs微观体验'的对比是贴吧鉴证的核心模式——通过普通人视角来质疑/解构官方叙述。",
    context_analysis="无额外上下文。官方数据vs民间感受的对比在贴吧政治表达中是标准模式。",
    supporting_evidence="(1) '数据挺好的'讽刺官方经济/社会数据的可靠性；(2) '我身边的'用个人微观经验质疑宏观数据；(3) 对比结构本身就构成政治质疑——暗示官方数据与民间真实脱节。贴吧鉴证的经典表达。",
    counter_evidence="可能是对经济数据的正常讨论和质疑——但'挺好的'的反讽口吻和对比结构在贴吧语境中已有固定的政治指向。",
    final_rationale="官方数据vs民间感受的经典贴吧对比讽刺，指向官方叙事可信度质疑，判为 high。"
)

add(
    text="咱们国家最厉害的地方就是，什么问题都能解决，解决了就没有问题了",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_夸张/反话", "E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：表面赞扬国家解决问题的能力——什么问题都能解决，解决后自然没有问题了。",
    encoding_analysis="这句话在贴吧语境中是经典的反讽——讽刺的是'通过消除提问题的人/压制讨论来解决问题'的治理逻辑。'解决后就没有问题了'的双关在此是讽刺核心——不是真的解决了问题而是让问题无法被提出。这种'表面赞扬+实质揭露'是贴吧阴阳怪气的经典模式。",
    context_analysis="无额外上下文。'解决问题=消除问题讨论'的双关讽刺在贴吧中成熟。",
    supporting_evidence="(1) 表面赞扬+深层双关的贴吧标准模式；(2) '解决后就没有问题了'的核心双关——暗示以压制言论代替解决问题；(3) '最厉害的地方'的过度赞美在贴吧中是反讽信号。完整的阴阳怪气结构。",
    counter_evidence="可能是对国家治理能力的真诚赞扬。但'解决后就没有问题了'的双关在正面解读中显得逻辑可疑——'解决了就没有问题'成立的前提是'解决了'为真，而'解决=让问题不被讨论'的语义在中文中有自然的双关解读空间。",
    final_rationale="双关讽刺治理逻辑的经典贴吧模式，指向言论压制，判为 high。"
)

add(
    text="只要我们有信心，就没有克服不了的困难（信心我有了，困难呢？）",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_夸张/反话", "B4_符号/空格/Unicode 干扰"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：前半句是正能量口号，后半句在括号中质问困难的实质。",
    encoding_analysis="这是'口号+括号自毁'贴吧模式的又一经典实例。前半句模仿官方正能量话语，后半句用'信心我有了，困难呢？'来揭露——暗示官方只给信心不给解决方案，或者用信心/精神鼓励来替代实质政策。这种将官方话语解构为'精神胜利法'的模式在贴吧中极为普遍。",
    context_analysis="无额外上下文。口号+括号解构在贴吧阴阳怪气中是成熟模板。",
    supporting_evidence="(1) 前半句复制官方正能量模板；(2) 括号解构揭露其空洞性——'信心我有了'接受官方预设，'困难呢？'要求实质内容；(3) 完整的贴吧阴阳怪气结构。",
    counter_evidence="可能是真诚的正能量表达+玩笑式补充。但在贴吧文化中，这种特定格式已固化为讽刺模板。",
    final_rationale="经典贴吧口号解构模板，指向正能量话语的空洞性，判为 high。"
)

add(
    text="说实话，我真的挺佩服那些什么都知道的人，特别是当他们愿意告诉我们的时候",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["E1_平台黑话", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：表达对那些知识渊博且愿意分享的人的敬佩。",
    encoding_analysis="在贴吧鉴证语境中，'什么都知道的人'表面指博学者，实则指那些能获取'被屏蔽信息/真实情况'的人——即能够翻墙/接触境外信息的人。'愿意告诉我们的时候'暗示这些信息通常不被允许公开分享。这种'将敏感内容包装为普通生活内容'的伪装是贴吧规避审查的经典手法。",
    context_analysis="无额外上下文。'什么都知道'+'愿意告诉'在贴吧鉴证中有其特定的编码含义。",
    supporting_evidence="(1) '什么都知道的人'在贴吧鉴证中常指能够获取被屏蔽信息的人；(2) '愿意告诉'暗示这些信息的分享是有风险的——正常知识分享不需要'愿意'这种道德维度；(3) 伪装为普通生活讨论的反讽模式。",
    counter_evidence="可能是对科普博主/知识分享者的真诚敬佩。但'什么都知道'在普通讨论中通常有更具体的范围（如'什么科技知识都知道'），绝对化的表述在正常讨论中不自然。",
    final_rationale="伪装为日常讨论的贴吧编码，暗示信息管控/翻墙获取信息，判为 high。"
)

add(
    text="每天醒来第一件事，就是看看今天能聊什么不能聊什么",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["D1_反讽", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：每天早上醒来先确认今天哪些话题可以讨论哪些不可以。",
    encoding_analysis="这句话是对言论审查/舆论管控的明确讽刺——将'确认允许讨论范围'描述为日常生活习惯，暗示言论边界在不断变化且需要持续关注。'能聊什么不能聊什么'是贴吧用户对平台审查/删帖经验的经典总结。这种将审查经验转化为'日常生活'的反讽在贴吧中极为常见。",
    context_analysis="无额外上下文。'能聊不能聊'在贴吧中是成熟的审查经验讨论。",
    supporting_evidence="(1) '每天醒来第一件事'——将审查适应描述为日常习惯，讽刺了审查的常态化；(2) '能聊什么不能聊什么'——贴吧用户对删帖/关键词屏蔽的集体经验；(3) 将政治批评伪装为生活感慨——贴吧规避检测的经典手法。",
    counter_evidence="可能是对社交媒体内容规则变动的正常关注。但'每天'的常态化描述和'能聊不能聊'的宏大范围在正常社交媒体使用中不自然——普通用户不会每天检查言论边界。",
    final_rationale="言论审查常态化讽刺的经典贴吧表达，判为 high。"
)

add(
    text="昨天发了个评论，今天号没了，这就是中国速度",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["D1_反讽", "C4_典故/物品/符号借用"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：昨天发布了一条评论，今天账号就被封禁了，称这体现了中国速度。",
    encoding_analysis="'中国速度'在此语境中是强烈的反讽——官方宣传中'中国速度'指高铁/基建/经济发展的高效率，在贴吧中被挪用来讽刺删帖/封号/言论管控的高效率。'号没了'是贴吧用户对封号/删帖经验的日常表述。官方宣传用语挪用+个人审查经验构成了尖锐的政治讽刺。",
    context_analysis="无额外上下文。'中国速度'的讽刺挪用+封号经验在贴吧中已是成熟的文化模板。",
    supporting_evidence="(1) '号没了'指向平台审查/封号——贴吧用户的共同经验；(2) '中国速度'挪用官方宣传用语进行讽刺——将高效率的正面含义翻转为高效率删帖的负面含义；(3) 个人经验+官方话语挪用的标准贴吧讽刺模式。",
    counter_evidence="可能是对某社交平台客服效率的调侃。但'中国速度'这一具有强烈国家品牌含义的词语在纯商业吐槽中不自然——商业吐槽通常用'这效率'或平台名称而非国家品牌。",
    final_rationale="官方宣传用语讽刺挪用的经典贴吧模式，指向言论管控，判为 high。"
)

add(
    text="反正我什么都不知道，我就是来打个卡的",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["D1_反讽", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：声明自己什么都不知道，只是来打卡签到的。",
    encoding_analysis="'我什么都不知道'在贴吧鉴证语境中是经典的'免责声明'——在讨论敏感话题时假装无知以避免追责。'打个卡'暗示该帖子/话题是一个已知的敏感讨论空间，用户以'打卡'的形式参与但不留下实质性内容。这种'假装无知+留下参与痕迹'的模式在贴吧敏感话题讨论中极为普遍。",
    context_analysis="无额外上下文。'什么都不知道'+'打卡'在贴吧敏感话题中是标准的参与模式。",
    supporting_evidence="(1) '什么都不知道'的假装无知——在讨论敏感话题时规避追责； (2) '打卡'在贴吧中暗示对某个敏感话题/帖子的日常关注和参与；(3) 假装无知+实质参与的矛盾本身就暗示了话题的敏感性——如果是正常话题不需要此策略。",
    counter_evidence="可能真的是在新手贴中打卡学习。但'什么都不知道'配合'打卡'的句型在纯新手学习中通常为'来学习了'而非强调自己的无知。",
    final_rationale="经典贴吧敏感话题参与模式——假装无知+留痕，判为 high。"
)

add(
    text="中国人口吧打卡，今天又是充满希望的一天",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["E1_平台黑话", "C4_典故/物品/符号借用"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：在中国人口吧签到，称今天是充满希望的一天。",
    encoding_analysis="中国人口吧是贴吧中知名的政治讨论/鉴证社区。'打卡'在此是对该社区的日常参与行为。'又是充满希望的一天'在贴吧语境中是强烈的反讽——在该社区中，'充满希望'从来不是字面意思，而是对现实失望/绝望的经典讽刺表达。社区名称+反讽口号构成了完整的指向。",
    context_analysis="中国人口吧作为特定鉴证社区，其讨论带有明确的政治讽刺倾向。",
    supporting_evidence="(1) 明确提及中国人口吧——贴吧中知名的政治讨论社区；(2) '打卡'行为确认了用户对该社区日常讨论的参与；(3) '充满希望的一天'在该社区语境中已完全固化为反讽——表达的是绝望而非希望。社区+反讽口号的组合指向明确的政治讽刺社群参与。",
    counter_evidence="可能是该社区中正常签到行为的字面理解。但在中国人口吧的特定语境中，'充满希望'的反讽语义已被社区文化完全固定，字面解读在该社区中不成立。",
    final_rationale="明确鉴证社区+成熟反讽口号，政治讽刺社群参与信号明确，判为 high。"
)

add(
    text="航吧老哥说得对，但我不敢说哪里对",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["D1_反讽", "C4_典故/物品/符号借用"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：赞同航空母舰吧的言论，但不敢具体说明哪里说得对。",
    encoding_analysis="'航吧'是航空母舰吧的简称——贴吧中知名的政治/军事讨论社区，以鉴证/政治讽刺内容闻名。'说得对但不敢说哪里对'是经典的反讽——暗示内容的政治敏感性使其不便公开复述，但通过'不敢说'本身就完成了对内容性质的确认（如果是正常内容不需要'不敢说'）。这是贴吧中间接传播敏感言论的经典模式。",
    context_analysis="航吧作为特定鉴证社区，其讨论内容有明确的政治讽刺性质。",
    supporting_evidence="(1) 明确提及航空母舰吧——贴吧中知名的鉴证社区； (2) '不敢说哪里对'确认了内容的敏感性——如果是正常讨论不存在'不敢说'；(3) '不敢说'本身已成为一种传播方式——通过承认'不敢说'来暗示内容的危险性和真实性。",
    counter_evidence="可能是对航吧中正常军事讨论的赞同——但如果是正常军事讨论，不存在'不敢说'的问题。",
    final_rationale="鉴证社区+敏感内容确认，间接传播敏感言论的贴吧模式，判为 high。"
)


# ================================================================
# SECTION C: 贴吧风格 — 社会现状/经济讽刺 (8 samples)
# ================================================================

add(
    text="这个班上得我越来越自闭了，不是我不想努力，是努力了也没用",
    risk_level="high",
    encoding_primary="D2_隐喻",
    encoding_secondary=["D1_反讽", "E3_话题/热点触发"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：上班让人越来越自闭，不是不想努力，而是努力没有用。",
    encoding_analysis="在贴吧鉴证语境中，'努力也没用'是经济阶层固化/社会不公的经典表达。表面讨论个人职业困境，实则指向社会结构性问题——'班上'隐喻在社会中的生存状态，'努力也没用'质疑了'努力就能成功'的主流叙事。这种'将社会问题伪装为个人抱怨'是贴吧鉴证的常见模式。",
    context_analysis="无额外上下文。'努力也没用'在贴吧中常被用于社会结构性问题的讨论。",
    supporting_evidence="(1) '努力也没用'质疑主流成功叙事——暗示社会结构性问题而非个人问题；(2) '越来越自闭'暗示社会压力/不平等的累积；(3) 个人抱怨包装社会批评——贴吧鉴证的经典伪装模式。",
    counter_evidence="可能是纯粹的个人职场吐槽。但在贴吧语境中，'努力也没用'配合社会性话题经常承载更宏大的社会批评。",
    final_rationale="社会结构性批评的贴吧伪装模式，指向阶层固化/社会不公，判为 high。"
)

add(
    text="以前觉得努力就能过上好日子，现在只想活着",
    risk_level="high",
    encoding_primary="D2_隐喻",
    encoding_secondary=["D1_反讽", "C2_历史事件影射"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：过去相信努力可以过好日子，如今只求生存。",
    encoding_analysis="'以前vs现在'的对比是贴吧鉴证的经典叙事结构——'以前'指向改革开放初期/经济增长黄金期（社会流动性高），'现在'指向当前（经济下行/内卷/阶层固化）。'只想活着'的极端表述是对现状的彻底否定——从'过好日子'到'活着'的坠落暗示了社会退步。",
    context_analysis="无额外上下文。'努力→好日子vs只要活着'在贴吧中是成熟的时代对比叙事。",
    supporting_evidence="(1) '以前vs现在'的时间对比结构指向时代变迁；(2) '好日子→活着'的坠落隐喻暗示社会退步——对社会发展叙事的否定；(3) '只想活着'的极端表达在贴吧语境中常被用于表达对社会现状的绝望。三重信号构成社会批评。",
    counter_evidence="可能是年轻人进入社会后正常的理想vs现实调整。但'只想活着'的绝望程度超出了正常的职场适应期表达——正常适应期会说'先养活自己再说'而非'只想活着'。",
    final_rationale="时代对比+社会退步隐喻的贴吧模式，指向社会现状的绝望评价，判为 high。"
)

add(
    text="经济这个东西吧，就像一个气球，越吹越大，但你不知道什么时候啪的一声",
    risk_level="high",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["D2_隐喻", "E3_话题/热点触发"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：将经济比作一个不断被吹大的气球，不知道何时会破裂。",
    encoding_analysis="'经济像气球'在贴吧鉴证中是经典的经济崩溃隐喻。'越吹越大'暗指依靠债务/泡沫驱动的经济增长。'啪的一声'（破裂）暗示预期中的经济危机/崩溃。这种'隐喻+持续膨胀+预期破灭'的结构是对中国经济前景的悲观/讽刺性评价。",
    context_analysis="无额外上下文。经济气球隐喻在贴吧金融/鉴证讨论中是成熟模式。",
    supporting_evidence="(1) '经济=气球'的崩溃隐喻在金融讨论和鉴证圈中成熟；(2) '越吹越大'暗示不可持续的增长模式——债务/泡沫驱动；(3) '啪的一声'暗示预期中的突然崩溃。完整的经济崩溃隐喻。",
    counter_evidence="可能是正常的经济科普/风险提示。但'啪的一声'的戏剧化表达在经济科普中不自然——正经经济分析会用'调整/衰退/软着陆'等术语而非'啪的一声'。",
    final_rationale="经济崩溃隐喻的贴吧模式，指向对中国经济前景的悲观预期，判为 high。"
)

add(
    text="这几年的变化就是，外卖越来越贵，工资越来越低，然后专家说经济稳中向好",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["C3_数字代指", "D2_夸张/反话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：指出物价上涨、工资下降的趋势，然后用专家的'经济稳中向好'来做对比。",
    encoding_analysis="这是贴吧经济讽刺的经典格式——个人微观体验（外卖贵/工资低）vs官方宏观叙述（经济稳中向好）的强烈对比。'专家说'在贴吧中是对官方/主流经济叙事的轻蔑代称。对比结构本身就构成了对官方经济叙事的质疑和讽刺。",
    context_analysis="无额外上下文。个人体验vs官方叙事的对比在贴吧经济讽刺中是标准模式。",
    supporting_evidence="(1) 外卖贵/工资低的个人微观体验——提供了具体的反例；(2) '专家说经济稳中向好'——用官方话语作为讽刺对象；(3) 对比结构本身揭露了官方叙事与民间体验的脱节。完整的贴吧经济讽刺。",
    counter_evidence="可能是对经济现状的正常吐槽。但'专家说'的讽刺性引用在贴吧中已具有固定的政治经济学讽刺含义。",
    final_rationale="个人体验vs官方叙事的经典贴吧经济讽刺，判为 high。"
)

add(
    text="就业率100%，因为不就业的人不在统计范围内",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["C3_数字代指", "D2_夸张/反话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：讽刺就业率统计——声称100%就业率是因为不就业的人被排除在统计之外。",
    encoding_analysis="这是对官方统计数据可信度的经典贴吧讽刺。'100%就业率'的表面宣称+自我否定的解释（'因为不就业的不在统计范围'）讽刺了统计数据的人为操纵——通过调整统计口径来美化数据。",
    context_analysis="无额外上下文。数据统计方法的讽刺在贴吧中成熟。",
    supporting_evidence="(1) '100%'的极端数据反映讽刺意图——没有经济体能实现100%就业；(2) '不在统计范围内'讽刺了统计口径的人为调整；(3) 表面+自我否定结构是贴吧阴阳怪气的标准模式。",
    counter_evidence="可能是对某个小范围调查统计的玩笑。但'就业率'在国家层面的语义使纯玩笑解释偏弱。",
    final_rationale="官方统计数据可信度讽刺的贴吧模式，判为 high。"
)

add(
    text="只要把标准降低到一定程度，我们都是发达国家了",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_隐喻", "C4_典故/物品/符号借用"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：讽刺通过降低标准来达到发达国家水平。",
    encoding_analysis="这句话讽刺了中国'发达国家'叙事的可信度——暗示所谓的'发达国家'是通过降低标准/重新定义来实现的。'只要把标准降低'直接质疑了官方叙事的真实性，暗示存在故意操纵标准以达到宣传目的。这种'标准/定义操纵'的讽刺在贴吧中常见。",
    context_analysis="无额外上下文。'发达国家'标准/定义的讨论在贴吧中有其特定的政治讽刺含义。",
    supporting_evidence="(1) '发达国家'明确指向国家发展水平的官方叙事；(2) '降低标准'暗示数据/概念的操纵——质疑叙事的真实性；(3) 简洁有力的讽刺结构。贴吧的经典反讽表达。",
    counter_evidence="可能是对某些行业标准/企业排名的正常讨论。但'发达国家'的国家层面指代明确且唯一。",
    final_rationale="国家发展叙事讽刺的贴吧模式，指向对官方宣传可信度的质疑，判为 high。"
)

add(
    text="我爱国，但我更爱那个不用把爱国挂在嘴边的时代",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["C2_历史事件影射", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：表达爱国情感，但怀念那个无需刻意表达爱国情怀的时代。",
    encoding_analysis="这句话在贴吧鉴证中是经典的政治表态——'不用把爱国挂在嘴边'暗示当下爱国已从自然情感变成强制/表演性行为。'那个时代'模糊指向过去——可能是改革开放初期或更早的时期，当一个更宽松的政治环境存在。'我爱国，但……'的转折结构在政治表达中成熟。",
    context_analysis="无额外上下文。'爱国=强制表演'的暗示在贴吧政治讨论中成熟。",
    supporting_evidence="(1) '不用把爱国挂在嘴边'暗示当下爱国主义已被异化为强制/表演；(2) '那个时代'的模糊指代暗示过去存在更宽松的环境；(3) '我爱国，但……'的转折结构本身就是政治批评。三重信号指向政治环境变化的批评。",
    counter_evidence="可能是对社交媒体上过度爱国表演的正常反感——不涉及政治体制批评。但'那个时代'的宏大指代使纯社交媒体批评的解释偏弱。",
    final_rationale="爱国异化批评的贴吧经典模式，指向政治环境变化的讽刺，判为 high。"
)

add(
    text="有时候想想，我们就像鱼缸里的鱼，觉得整个海洋就是这一缸水",
    risk_level="high",
    encoding_primary="D2_隐喻",
    encoding_secondary=["C4_典故/物品/符号借用", "E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：用鱼缸里的鱼比喻人的视野局限——鱼以为鱼缸就是整个海洋。",
    encoding_analysis="在贴吧鉴证语境中，'鱼缸'隐喻信息茧房/GFW——将中国互联网用户比喻为鱼缸中不知道海洋存在的鱼。'觉得整个海洋就是这一缸水'暗示被限制在封闭信息环境中的人无法认识到外界的广阔。这是对网络管控/信息封锁的经典诗意化隐喻。",
    context_analysis="无额外上下文。鱼缸/海洋隐喻在贴吧鉴证中是成熟的GFW/信息管控批评。",
    supporting_evidence="(1) '鱼缸'隐喻封闭信息环境——在网络讨论中已固化为GFW的隐喻； (2) '海洋'隐喻外部/境外信息世界；(3) '觉得……就是……'暗示被限制者的无知——对信息管控后果的描述。三重信号构成完整的信息管控批评。",
    counter_evidence="可能是关于个人成长/视野局限的正常哲学反思。但'鱼缸'在网络语境中作为GFW隐喻的固化程度使纯哲学解读偏弱。",
    final_rationale="GFW/信息管控的经典诗意隐喻，贴吧鉴证成熟模式，判为 high。"
)


# ================================================================
# SECTION D: 贴吧风格 — 极端消极/绝望情绪 (5 samples)
# ================================================================

add(
    text="这盛世，如大家所愿",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["C2_历史事件影射", "D2_夸张/反话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：这繁荣盛世，正如大家所期望的那样。",
    encoding_analysis="这七个字是中国互联网中最经典的反讽之一。表面引用/赞扬，但在鉴证语境中已完全固化为对现状的讽刺——'盛世'讽刺官方塑造的繁荣叙事，'如大家所愿'暗示这种'盛世'只是官方想要的而非民众想要的。极简但极强——七个字承载了完整的政治讽刺。",
    context_analysis="无额外上下文。此句在中文互联网中已完全固化为政治讽刺的经典表达。",
    supporting_evidence="(1) 极简句式使其传播力极强——贴吧鉴证的标志性表达；(2) '盛世'挪用官方叙事进行反讽；(3) '如大家所愿'的核心讽刺——'大家'实际不是民众而是官方。此表达在中文互联网中已完全政治化，几乎不再有字面使用。",
    counter_evidence="理论上是正面引用。但在当代中文互联网语境中，此句的讽刺语义已彻底压倒字面语义——真诚使用此句反而需要额外说明。",
    final_rationale="中文互联网最经典的政治反讽之一，语义已完全固化，判为 high。"
)

add(
    text="真是越来越有盼头了（指盼着早点下班）",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_夸张/反话", "B4_符号/空格/Unicode 干扰"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：先说越来越有盼头，然后括号说明这种盼头其实是盼着早点下班。",
    encoding_analysis="这是'口号+括号自毁'贴吧模式的又一经典实例。'越来越有盼头了'模仿官方正能量话语（对国家未来充满希望），括号中'指盼着早点下班'将宏大的'希望'缩小为卑微的'盼下班'——暗示对未来的唯一期待就是逃离工作/逃离现实。宏大→卑微的瞬间翻转构成了对社会现状的尖锐讽刺。",
    context_analysis="无额外上下文。口号+括号自毁在贴吧阴阳怪气中是成熟模板。",
    supporting_evidence="(1) '越来越有盼头'模仿官方正能量；(2) 括号将宏大希望缩小为卑微愿望——经典贴吧解构手法；(3) '盼着早点下班'暗示对生活/工作的不满——'下班'隐喻逃离社会角色。",
    counter_evidence="可能是正常的办公室幽默。但在贴吧特定语境中，此格式已固化为社会讽刺模板。",
    final_rationale="宏大→卑微解构的贴吧阴阳怪气模式，指向社会失望，判为 high。"
)

add(
    text="相信国家相信党，剩下的交给天意",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_夸张/反话", "E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：表示相信国家和党的领导，其他的交给天意。",
    encoding_analysis="这句话在贴吧中有双重解读——正面使用时是爱国表态，但在鉴证语境中，'交给天意'的无奈收尾将前面的正面表态翻转为讽刺——'相信了国家和党之后，剩下的只能听天由命'暗示了'相信'之后没有实质改变。这种'正面表态+无奈收尾'的结构是贴吧的经典阴阳怪气。",
    context_analysis="无额外上下文。'相信国家相信党+剩下的交给……'在贴吧中已固化为特定句式。",
    supporting_evidence="(1) 前半部分是标准爱国表态；(2) '剩下的交给天意'在贴吧中使用时带有无奈/讽刺色彩——暗示信任之后没有实质帮助；(3) 整个句式在贴吧鉴证中已有成熟的反讽使用模式。",
    counter_evidence="可能是真诚的爱国表态。但在贴吧特定文化中，此句式的广泛反讽使用使其字面语义已被削弱。",
    final_rationale="正面表态+无奈收尾的贴吧阴阳怪气模式，指向对国家治理的不信任，判为 high。"
)

add(
    text="我什么都不会说的，因为我确实什么都不知道",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["D1_反讽", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：表态不会说任何话，因为确实什么都不知道。",
    encoding_analysis="这句话在贴吧鉴证中是经典的'沉默表态'——通过假装无知来表达对言论环境的不满。'什么都不会说'在此语境中不是真的无话可说，而是因为'说了也没用/说了有风险'。'因为确实什么都不知道'的表层逻辑是字面的无知，深层逻辑是'知道也不能说/不敢说'。这种'沉默作为抗议'的模式在高压言论环境中极为成熟。",
    context_analysis="无额外上下文。'什么都不会说'在贴吧鉴证中是成熟的表达模式。",
    supporting_evidence="(1) '什么都不会说'在此语境中是沉默抗议而非字面的无话可说； (2) '因为确实什么都不知道'的刻意强调暗示了反讽；(3) 沉默作为表态——在高压言论环境中，沉默本身就构成政治表达。",
    counter_evidence="可能是真的一无所知的正常表态。但配合政治讨论的上下文，纯无知表态的解释偏弱。",
    final_rationale="沉默抗议的贴吧表达模式，指向言论环境不满，判为 high。"
)

add(
    text="生于种花家，来世还入种花家（前提是能投个好胎）",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["B4_符号/空格/Unicode 干扰", "D2_夸张/反话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：前半句表达对祖国的热爱，括号中补充前提条件——需要投个好胎。",
    encoding_analysis="'生于种花家，来世还入种花家'是来自爱国动漫《那年那兔那些事》的经典爱国口号。在贴吧语境中，后半的括号'前提是能投个好胎'将爱国口号翻转为对阶层固化/社会不公的讽刺——'如果投胎到穷人家庭就不会这样说了'。爱国口号+阶层讽刺的组合构成尖锐的政治社会批评。",
    context_analysis="无额外上下文。爱国口号+括号反转在贴吧中是成熟的反讽模板。",
    supporting_evidence="(1) 挪用经典爱国口号增加讽刺力度；(2) '投个好胎'直接指向阶层固化/贫富差距——将爱国情感与社会不公对撞；(3) 爱国→社会不公的翻转揭示了对'爱国叙事掩盖社会问题'的讽刺。完整的政治社会批评。",
    counter_evidence="可能是朋友间的玩笑——调侃自己家庭条件好。但在贴吧公共讨论中，此格式已固化为政治社会讽刺。",
    final_rationale="爱国口号+阶层讽刺的贴吧阴阳怪气模式，指向社会不公，判为 high。"
)


# ================================================================
# Write output
# ================================================================

print(f"Generated {len(samples)} HIGH-risk tieba-style samples")

with open(OUTPUT, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s, ensure_ascii=False, separators=(",", ":")) + "\n")

print(f"Written to {OUTPUT}")

risk_dist = Counter(s["risk_level"] for s in samples)
enc = Counter(s["encoding_primary"] for s in samples)
print(f"Risk: {dict(risk_dist)}")
print(f"Encoding primary:")
for e, c in enc.most_common():
    print(f"  {e}: {c}")
