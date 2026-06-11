#!/usr/bin/env python3
"""
Generate batch9: National-security-threatening HIGH-risk samples.

Source reference: 中国大陆网络用语列表整理.md (323 entries, Wikipedia-derived)
Only targeting genuine threats — NOT normal internet slang/memes.

Four categories (ALL high):
1. 领导人编码全变体 — all documented leader encoding variants
2. 政策/体制攻击 — policy and system attacks using coded language
3. 消极社会思想 — nihilistic, anti-social ideological expressions
4. 群体攻击/政治标签 — political group labels in hostile contexts

Preserving: YYDS, 蓝瘦香菇, 芭比Q了, 帝都, 魔都, sports/gaming terms, etc.
These are healthy internet culture — NOT targeted.

All sensitive content in output file only. We defend China's network security.
"""

import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data/raw/batch9_national_security.jsonl"

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
        "id": f"B9_{len(samples)+1:04d}",
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
        "review_notes": "source=batch9_national_security;",
    })


# ================================================================
# SECTION 1: 领导人编码全变体 (15 samples)
# Using documented variants: 外貌借代, 食物借代, 谐音, 英文名借代
# ================================================================

add(
    text="话说那只爱吃包子的熊，最近包子涨价了他会不会不开心",
    risk_level="high",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["C4_典故/物品/符号借用", "D1_反讽", "F_组合编码"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：讨论一只爱吃包子的熊，担心包子涨价会让它不开心。",
    encoding_analysis="三重编码叠加指代最高领导人：(1) '熊'借代——源自该领导人与卡通熊形象的外貌联想，已完全固化；(2) '爱吃包子'引用该领导人2013年排队买包子的公开事件——'包子'已成为其专属代称；(3) '包子涨价'表面讨论物价，实则暗讽经济下行。三重编码+经济讽刺构成完整的政治攻击。",
    context_analysis="无额外上下文。'熊'+'包子'的双重借代在中国互联网中具有唯一指向性。",
    supporting_evidence="(1) '熊'和'包子'各自都是最高领导人的成熟编码——两个编码叠加消除了任何歧义；(2) '包子涨价'将经济议题与领导人编码关联——暗示领导人应对物价上涨负责；(3) '不开心'将政治讽刺伪装为对动物的关心——贴吧阴阳怪气的经典手法。",
    counter_evidence="字面上是讨论动物园里的熊和包子价格。但'爱吃包子的熊'这一特定组合在中国互联网中已有唯一且明确的政治指向——这正是该编码的核心特征：表面无害，实指明确。",
    final_rationale="三重领导人编码叠加+经济讽刺，指代唯一且明确，属恶意政治攻击，判为 high。"
)

add(
    text="维尼最近是不是减肥了，好久没看到他出镜了",
    risk_level="high",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["C4_典故/物品/符号借用", "E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：讨论卡通角色小熊维尼，猜测它是否减肥了，很久没在电视上看到它。",
    encoding_analysis="'维尼'（小熊维尼/Winnie the Pooh）是中国互联网中最广为人知的最高领导人借代之一——源自2013年该领导人与奥巴马会晤时，网友发现其与迪士尼卡通角色小熊维尼的外貌相似。此编码已在全球范围内出圈。'出镜'表面指卡通角色出镜，实指领导人公开露面。'减肥'是外貌调侃。",
    context_analysis="无额外上下文。'维尼'作为最高领导人借代在中国互联网中已完全约定俗成。",
    supporting_evidence="(1) '维尼'是全球范围内最知名的最高领导人编码——在中文互联网中几乎不再有字面使用；(2) '出镜'的双关——表面是卡通角色，实指公开露面；(3) '好久没看到他'暗示对其公开活动频率的关注/讽刺。三重信号明确指向政治人物调侃。",
    counter_evidence="理论上是纯卡通讨论。但在中国互联网语境中，'维尼'用于讨论'出镜/不出镜'时，几乎100%是政治借代——正常卡通讨论会说'迪士尼新作'而非'出镜'。",
    final_rationale="全球最知名的领导人编码，意图明确且恶意，判为 high。"
)

add(
    text="今天早上吃了顿包子，突然想起来好久没见过那位爱吃包子的大爷了",
    risk_level="high",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["C4_典故/物品/符号借用", "D1_反讽"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：吃包子时想起了一位很久没见的爱吃包子的大爷。",
    encoding_analysis="'爱吃包子的大爷'是三层借代编码：(1) '包子'引用该领导人2013年排队买包子事件；(2) '大爷'将国家最高领导人戏称为普通老人——刻意贬低/市井化；(3) 吃包子→想起的联想路径看似自然实则刻意——将政治讨论伪装为日常感悟。'好久没见过'是对领导人公开露面频率的讽刺性关注。",
    context_analysis="无额外上下文。'包子'+'大爷'在贴吧鉴证中已固化为领导人借代。",
    supporting_evidence="(1) '包子'事件是最高领导人的专属代称——具有唯一指向性；(2) '大爷'的刻意市井化——将领导人降格为普通老人；(3) '好久没见过'暗示对公开露面频率的关注——在贴吧中这是对领导人健康/权力状态的讽刺性讨论。",
    counter_evidence="可能真的是对某个爱吃包子的长辈的怀念。但'包子事件'作为领导人专属代称的固化程度，加上'好久没见'暗示公众视野而非私人关系，使普通长辈解释不成立。",
    final_rationale="三层领导人借代编码，指代唯一且恶意明确，判为 high。"
)

add(
    text="话说咱家那位最大的，今年又去哪儿过年了",
    risk_level="high",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["D1_反讽", "E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：询问家中最大的那位今年在哪里过年。",
    encoding_analysis="'咱家最大的'是经典的贴吧领导人借代——'咱家'将国家伪装为家庭（源自'家国一体'的话语），'最大的'直指最高领导人。这种'家庭化+最高级'的编码模式在贴吧中高度成熟。'去哪儿过年'表面关心实则讽刺——将领导人的行程/生活作为八卦对象，暗含对其特权/不透明的质疑。",
    context_analysis="无额外上下文。'咱家最大的'在贴吧语境中已固化为领导人借代。",
    supporting_evidence="(1) '咱家'将国家伪装为家庭——贴吧经典手法；(2) '最大的'明确指向最高级别——在家庭隐喻中消除歧义；(3) '去哪儿过年'将领导人的私人行程作为八卦对象——讽刺其不透明/特殊待遇。三重信号完整。",
    counter_evidence="可能是在讨论家族中的长辈。但在公共讨论（贴吧/评论区）中讨论'咱家最大的'，其宏大指代超出了私人家庭讨论的范围。",
    final_rationale="家庭化领导人借代的贴吧经典模式，恶意调侃领导人私人生活，判为 high。"
)

add(
    text="宽肩膀的那位同志最近又瘦了，为国操劳啊（手动狗头）",
    risk_level="high",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["D1_反讽", "B4_符号/空格/Unicode 干扰", "D2_夸张/反话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：一位肩膀宽的同志最近瘦了，感叹他为国家操劳。结尾加了'手动狗头'表示反讽。",
    encoding_analysis="'宽肩膀'是领导人的外貌特征借代。'同志'在此表面是正常称呼，实则带讽刺距离感。'为国操劳'是经典贴吧反讽——表面赞扬实则讽刺。'手动狗头'是贴吧反讽的标准标记——明确告知读者前述内容为反讽（因为'狗头'=狗头保命=说反话来自保）。狗头标记+表面赞扬+外貌借代的三层结构是贴吧阴阳怪气的标准模式。",
    context_analysis="无额外上下文。'手动狗头'在贴吧中是反讽的明确标记——它的存在使前述内容的字面解读完全不成立。",
    supporting_evidence="(1) '宽肩膀'的外貌借代具有唯一指向性；(2) '为国操劳'配合狗头标记确认了反讽意图——如果是真诚赞扬不需要狗头；(3) '手动狗头'是贴吧反讽的标志性标记——它的存在本身就是对前述内容的否定。",
    counter_evidence="狗头标记明确否定了字面解读的可能——使用狗头标记的文本几乎100%是反讽。",
    final_rationale="外貌借代+标记性反讽的贴吧标准模式，恶意调侃领导人，判为 high。"
)

add(
    text="说起来，那年的包子事件真是改变了历史走向啊（懂的都懂）",
    risk_level="high",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["C2_历史事件影射", "E2_时间节点触发", "D1_反讽"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：讨论某年的包子事件改变了历史走向，括号中表示知情者都明白。",
    encoding_analysis="'包子事件'明确指向2013年领导人排队买包子的标志性事件——该事件在此编码中指代该领导人上台/执政的起点。'改变历史走向'在此是反讽——表面肯定其历史意义，实则表达对其执政方向的不满。'懂的都懂'确认了对话的编码性质。事件借代+历史评价+知情者确认构成完整的政治讽刺。",
    context_analysis="无额外上下文。'包子事件'在中国互联网政治话语中具有唯一且明确的指代。",
    supporting_evidence="(1) '包子事件'是最高领导人的专属事件代称——唯一指向；(2) '改变历史走向'是表面肯定+实质性批评的贴吧反讽；(3) '懂的都懂'确认了编码性质——如果是正常历史讨论不需要此暗示。",
    counter_evidence="可能是对某个无关事件的中性讨论。但在中国互联网语境中，'包子事件'与领导人的关联已完全固化和出圈。",
    final_rationale="领导人专属事件代称+历史评价反讽，政治攻击意图明确，判为 high。"
)

add(
    text="那什么总啊，时间不短了，差不多得了",
    risk_level="high",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["D1_反讽", "C2_历史事件影射"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：对某个称为'总'的人说，时间够长了，差不多该停下了。",
    encoding_analysis="'总'在此语境中是'总书记'的简称——在贴吧中单独使用'总'（不加姓名）来指代最高领导人是成熟的借代模式。'时间不短了'在此指执政时间——自2012年上台至今已超过十年。'差不多得了'是贴吧经典表达——表面劝人适可而止，在此语境中暗指对长期执政/终身任期的不满。头衔简称+时间暗示+劝退表达构成完整的政治攻击。",
    context_analysis="无额外上下文。单独使用'总'在贴吧政治讨论中指代最高领导人的模式已成熟。",
    supporting_evidence="(1) 单独'总'在贴吧中是最高领导人的成熟借代；(2) '时间不短了'暗示执政时间过长；(3) '差不多得了'暗含对长期执政/终身任期的否定——是贴吧典型的政治劝退表达。三重信号指向任期问题的政治攻击。",
    counter_evidence="可能是对某个公司总经理的劝退。但在公共讨论中不指名道姓地单称'总'且讨论'时间不短了'，指向公共/政治人物的概率远高于公司领导。",
    final_rationale="头衔简称+任期攻击的贴吧模式，指向领导人任期问题，判为 high。"
)

add(
    text="不是我说，这届舵手开船开得我晕船了",
    risk_level="high",
    encoding_primary="D2_隐喻",
    encoding_secondary=["C1_历史人物类比", "D1_反讽"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：抱怨这届舵手开船让人晕船。",
    encoding_analysis="'舵手'在中国政治话语中是一个高度政治化的隐喻——源自'大海航行靠舵手'这一革命歌曲/政治口号，在此被反讽性挪用。'这届'明确指向当前领导班子。'开船开得我晕船了'将国家治理比喻为航行，'晕船'表达了对治理方向/方式的生理性不适。革命话语挪用+身体不适隐喻构成尖锐的政治讽刺。",
    context_analysis="无额外上下文。'舵手'作为政治领袖隐喻在中国文化中有深厚的历史根基。",
    supporting_evidence="(1) '舵手'在中国政治文化中是成熟的领袖隐喻——源自革命话语体系；(2) '这届'明确了时间指向——当前任期；(3) '晕船'将政治不满表达为身体不适——贴吧常见的'政治恶心'隐喻。三重信号构成完整的治理批评。",
    counter_evidence="可能是对游轮/船只驾驶员的真实抱怨。但在公共讨论中，'舵手'作为政治隐喻的使用远多于字面的船员讨论。",
    final_rationale="革命话语挪用+政治治理隐喻，指向对现任领导层的讽刺性批评，判为 high。"
)

add(
    text="我有时候真羡慕隔壁家的孩子，考得好还能偶尔放个假",
    risk_level="high",
    encoding_primary="C2_历史事件影射",
    encoding_secondary=["D2_隐喻", "D1_反讽"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：羡慕邻居家的孩子成绩好还能偶尔放假休息。",
    encoding_analysis="'隔壁家的孩子'在贴吧鉴证中是国际政治比较的经典隐喻——'隔壁家'指代其他国家（尤其是发达国家），'考得好'指代该国治理/经济发展良好，'偶尔放个假'指代政治更替/领导人轮换制度。将国际政治比较伪装为育儿/邻里闲聊是贴吧极经典的伪装手法。",
    context_analysis="无额外上下文。'隔壁家孩子'的国际政治隐喻在贴吧鉴证中已成熟。",
    supporting_evidence="(1) '隔壁家'在国际政治比较中是经典隐喻；(2) '考得好'隐喻他国治理成效；(3) '偶尔放个假'隐喻领导人轮换制度——暗示对中国终身任期的讽刺。三重隐喻指向政治制度比较。",
    counter_evidence="可能是真实的育儿/邻里闲聊。但在贴吧鉴证语境中，'隔壁家'+'考得好'+'放假'的组合已被固化为国际政治比较的隐喻模板。",
    final_rationale="国际政治比较的贴吧家庭隐喻模式，指向对领导人轮换制度的讽刺，判为 high。"
)

add(
    text="以前那位还能偶尔看到，现在这位是真的深居简出",
    risk_level="high",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["C2_历史事件影射", "D1_反讽"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：比较以前和现在的某位人物——以前的偶尔能看到，现在的很少露面。",
    encoding_analysis="'以前那位'和'现在这位'是对不同时期领导人的代际比较——通过'露面频率'的差异来暗示领导人风格/政治环境的变化。在贴吧鉴证中，通过比较前后两任领导人的行为模式来传递政治评价是常见手法。'深居简出'在此语境中暗示现任领导人脱离群众/信息不透明。",
    context_analysis="无额外上下文。前后任领导人的代际比较在贴吧政治讨论中成熟。",
    supporting_evidence="(1) '以前那位'和'现在这位'的对比结构明确指向领导人的代际比较；(2) '偶尔能看到vs深居简出'的对比暗示现任脱离群众；(3) 代际比较在贴吧中是成熟的政治评价模式——通过对比来含蓄表达对现任的不满。",
    counter_evidence="可能是对某个公司两任CEO/部门领导的比较。但'深居简出'对于企业管理者来说是不自然的描述——企业管理者需要经常公开露面。",
    final_rationale="领导人代际比较的政治评价模式，指向对现任领导人的负面评价，判为 high。"
)

add(
    text="听说钢厂的产量又创新高了，不愧是钢铁公司",
    risk_level="high",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["C4_典故/物品/符号借用", "D1_反讽", "F_组合编码"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：评论某钢厂的产量创新高，称赞其不愧是钢铁公司。",
    encoding_analysis="'钢铁公司'在此语境中是双重编码：(1) 字面的钢铁制造企业；(2) 对特定前领导人的借代——源自毛泽东1974年称其为'钢铁公司'（形容其政治意志坚定）。'产量创新高'表面讨论钢铁产量，实则可能影射该领导人执政时期的某项政策成果。'不愧是'在贴吧中是反讽标志。双重语义的结构使该评论可在字面和政治隐喻之间切换——这是贴吧规避审查的经典手法。",
    context_analysis="无额外上下文。'钢铁公司'在特定政治讨论中已固化为前领导人借代。",
    supporting_evidence="(1) '钢铁公司'是对特定前领导人的成熟借代——有明确的历史出处（毛泽东1974年评价）；(2) '不愧是'在贴吧中常用于反讽；(3) 双重语义结构的伪装性——表面讨论钢铁企业，政治指代在知情者中明确。",
    counter_evidence="可能是对某钢铁企业的真诚讨论。但'钢铁公司'的特定历史指代使其在政治讨论中的隐喻使用不容忽视。",
    final_rationale="前领导人借代+双重语义伪装，贴吧政治影射经典模式，判为 high。"
)

add(
    text="不是我说，这位是真的能熬，把同届的都熬走了",
    risk_level="high",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["D1_反讽", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：评论某人很能熬——把同期的其他人都熬走了。",
    encoding_analysis="'这位'的模糊指代在贴吧政治讨论中常指向最高领导人。'把同届的都熬走了'在此语境中暗示该领导人通过清除/排挤同期政治对手来实现长期执政。'能熬'在此是双关——表面为耐心/坚持，实则暗示权力斗争中的生存/排挤能力。这种'竞技化/生存化'的政治叙事在贴吧鉴证中极为常见。",
    context_analysis="无额外上下文。'熬走同届'在贴吧政治讨论中是经典的权力分析模式。",
    supporting_evidence="(1) '这位'的模糊指代+政治语境指向最高领导人；(2) '能熬'暗示权力斗争的生存/排挤能力——将政治斗争演绎为生存游戏；(3) '同届的都熬走了'暗指对政治对手的清除/排挤——贴吧对党内权力斗争的经典叙事。",
    counter_evidence="可能是对某个职场/体育竞技选手的评论。但在公共讨论中，'同届'的宏大指代和'熬走'的权力暗示超出职场吐槽的范围。",
    final_rationale="权力斗争叙事的贴吧政治攻击模式，指向领导人排挤政治对手，判为 high。"
)

add(
    text="那锅蛋炒饭的故事，每隔一段时间就有人翻出来重新炒一遍",
    risk_level="high",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["C2_历史事件影射", "E3_话题/热点触发"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：讨论一个关于蛋炒饭的故事/传闻，说每隔一段时间就有人重新提起。",
    encoding_analysis="'蛋炒饭'在中文互联网中是对特定历史人物（前领导人长子）及其死亡事件的戏谑化/贬低化代称——源自该人物死亡时的相关传闻。'每隔一段时间就有人翻出来'暗示该话题作为一个周期性出现的政治敏感话题。用食物代称历史人物+贬低化编码在中文互联网中极为常见。",
    context_analysis="无额外上下文。'蛋炒饭'在特定鉴证社群中已固化为对特定历史人物/事件的代称。",
    supporting_evidence="(1) '蛋炒饭'在鉴证圈中是成熟的特定历史人物/事件代称——具有唯一指向性；(2) '每隔一段时间翻出来'暗示该话题周期性出现——符合敏感历史话题的传播特征；(3) 食物代称+历史人物贬低化编码——恶意历史人物攻击的经典模式。",
    counter_evidence="可能是关于某道菜品的正常讨论。但在中国互联网特定语境中，'蛋炒饭的故事'配合'翻出来重新炒'的双关暗示已具有明确的鉴证含义。",
    final_rationale="特定历史人物/事件的贬低性食物代称，恶意历史攻击，判为 high。"
)

add(
    text="你别说，有些肉放久了确实会变成腊味",
    risk_level="high",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["C4_典故/物品/符号借用", "D1_反讽"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：评论肉类放久了会变成腊味——关于食物加工的讨论。",
    encoding_analysis="'腊味'→'腊肉'的谐音/联想在鉴证圈中是对特定前领导人的恶意贬称。'肉放久了变成腊味'表面是食品加工常识，实则是将前领导人贬称为'腊肉'的恶意攻击。'你别说'的贴吧开场白暗示了接下来要说的是不便直说的内容。食物比喻+历史人物攻击在中文互联网鉴证圈中极为常见。",
    context_analysis="无额外上下文。'腊肉'作为对特定前领导人的蔑称在鉴证圈中已固化。",
    supporting_evidence="(1) '腊味→腊肉'的联想路径指向特定前领导人的蔑称；(2) '放久了'在此语境中暗含对已故人物的不敬；(3) '你别说'的贴吧开场暗示内容不便直说。三重信号指向对已故前领导人的恶意攻击。",
    counter_evidence="可能是关于食品加工的正常讨论。但在中文互联网鉴证语境中，'腊肉'作为特定前领导人蔑称的使用已广泛到使其食品语义在特定社群中被政治语义覆盖。",
    final_rationale="特定前领导人的恶意蔑称编码，历史人物攻击，判为 high。"
)

add(
    text="那谁家的孩子不是去北边留学了嘛，听说那边的教育质量比我们这边好",
    risk_level="high",
    encoding_primary="C2_历史事件影射",
    encoding_secondary=["D2_隐喻", "C1_历史人物类比"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：讨论某个家庭的孩子去北边留学，说那边教育质量好。",
    encoding_analysis="'那谁家的孩子去北边留学'在贴吧鉴证中是经典的政治隐喻。(1) '那谁家'暗示不便直说的人家——在特定语境中指向特定政治人物的子女；(2) '北边'代指西方国家/发达国家；(3) '教育质量好'暗示对国内教育/体制的不满。将政治人物的家庭隐私（子女留学）与国内外体制比较结合起来，构成双重政治攻击。",
    context_analysis="无额外上下文。'北边留学'+家庭指代在贴吧中是成熟的领导人家人隐私/特权讨论模式。",
    supporting_evidence="(1) '那谁家'的模糊指代暗示不便直说——却又有约定俗成的指向；(2) '北边留学'暗示西方国家——政治精英子女留学是敏感话题；(3) '教育质量好'暗示国内不如国外——将个人选择上升为体制比较。",
    counter_evidence="可能是正常的留学讨论。但在公共讨论中，'那谁家'的模糊指代配合'教育质量比较'使其超出了私人留学讨论的范围。",
    final_rationale="领导人家庭成员隐私+体制比较的贴吧政治攻击模式，判为 high。"
)


# ================================================================
# SECTION 2: 政策/体制攻击 (15 samples)
# Using: 伟光正, GFW/墙, 冲塔, 改开党, 和谐, 喝茶, 茧中互联网 等
# ================================================================

add(
    text="伟光正永远正确，如果你觉得有问题，那一定是你的问题",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["C4_典故/物品/符号借用", "D2_夸张/反话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：声称'伟光正'永远正确，如果你认为有问题那是你有问题。",
    encoding_analysis="'伟光正'是对'伟大的、光荣的、正确的'这一中共官方表述的缩写挪用——在鉴证语境中已完全固化为对中共及其宣传话语的讽刺。'永远正确+你有问题'的组合讽刺了官方话语中不容质疑的绝对正确性——暗示体制将任何批评都定义为'批评者的问题'。这是对官方话语体系的经典解构式攻击。",
    context_analysis="无额外上下文。'伟光正'在中文互联网中的反讽语义已压倒其字面语义。",
    supporting_evidence="(1) '伟光正'在鉴证语境中已被完全固化为对中共的讽刺性指代；(2) '永远正确+你有问题'的归咎逻辑讽刺了官方对批评的回应模式；(3) 整句是对官方话语体系的系统性解构——贴吧鉴证的核心手法。",
    counter_evidence="理论上是正面引用。但在当代中文互联网语境中，'伟光正'的讽刺语义已完全压倒字面语义，真诚使用的概率极低。",
    final_rationale="官方话语体系的系统性讽刺解构，对中共的恶意攻击，判为 high。"
)

add(
    text="翻个墙就像做贼一样，明明只是想看看外面的世界长什么样",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["D1_反讽", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：抱怨翻墙上网像做贼，只是想知道外面的世界什么样。",
    encoding_analysis="'翻墙'是GFW/网络审查的经典隐喻。'像做贼一样'将合法求知行为被定为'违法'的荒谬感具象化。'只是想看看外面的世界'将翻墙行为合理化为人类好奇心的基本需求——暗示GFW剥夺了公民了解外部世界的基本权利。这构成了对网络审查制度的明确攻击。",
    context_analysis="无额外上下文。'翻墙'+信息获取的叙事在鉴证话语中是经典的审查批评模式。",
    supporting_evidence="(1) '翻墙'是对GFW/网络审查的明确指代；(2) '像做贼一样'将正常行为被定为违法的荒谬感具象化——对审查合理性的直接质疑；(3) '只是想看看外面'将翻墙合理化为基本人权——贴吧经典的审查批评叙事。",
    counter_evidence="可能是对技术问题的中性讨论。但'像做贼一样'的道德/法律评价使纯技术讨论的解释不成立。",
    final_rationale="对网络审查制度的明确攻击，将翻墙合理化为基本人权需求，判为 high。"
)

add(
    text="茧中互联网真是太舒服了，什么都不知道就不会不开心",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["A2_拼音/首字母缩写", "E1_平台黑话", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：说茧中互联网很舒服，什么都不知道就不会不开心。",
    encoding_analysis="'茧中'是'简中'（简体中文）的谐音——利用'茧'（蚕茧）和'简'的谐音，暗示简体中文互联网用户如同被包裹在信息茧中一般坐井观天。'太舒服了'是贴吧反讽——实际表达的是对信息封闭的讽刺。'什么都不知道就不会不开心'讽刺了'无知即幸福'的信息管控逻辑。多重谐音+反讽构成对信息管控的系统性攻击。",
    context_analysis="无额外上下文。'茧中互联网'在鉴证圈中已固化为对中文互联网信息管控的讽刺性称呼。",
    supporting_evidence="(1) '茧中'谐音双关——同时指'简中'和'信息茧房'，暗示中文互联网用户被封闭在信息茧中；(2) '太舒服了'的贴吧反讽——对信息管控的讽刺性赞扬；(3) '什么都不知道就不会不开心'讽刺了通过信息封锁维持社会稳定的逻辑。三重信号构成对信息管控的系统性攻击。",
    counter_evidence="可能是对外界信息过载的正常感慨。但'茧中互联网'在鉴证圈中的特定指向使其纯个人感慨解读不成立。",
    final_rationale="谐音双关+信息管控攻击，对中文互联网审查制度的系统性讽刺，判为 high。"
)

add(
    text="冲塔一时爽，一直冲塔一直爽，号没了就换一个",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["D1_反讽", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：描述一种行为——冲塔让人爽快，账号被封了就换一个继续。",
    encoding_analysis="'冲塔'源自游戏术语（英雄联盟中冲入对方防御塔），但在中文互联网中已被完全固化为'主动提及/讨论政治敏感话题'的代称。'一直冲塔一直爽'鼓励持续的政治敏感言论。'号没了就换一个'暗示对平台封号的蔑视——将封号视为可接受的代价。这构成了对政治敏感话题讨论的积极鼓励和对平台管控的公然蔑视。",
    context_analysis="无额外上下文。'冲塔'在中文互联网中的政治含义已完全固化。",
    supporting_evidence="(1) '冲塔'在中文互联网中已固化为政治敏感话题讨论的代称；(2) '一直冲塔一直爽'积极鼓励敏感话题讨论——暗示这是一种'爽'的行为；(3) '号没了就换一个'公然蔑视平台管控——构成对言论管控体系的正面挑战。完整的政治煽动信号。",
    counter_evidence="可能是游戏术语的字面使用。但在公共讨论中，'冲塔'配合'号没了'（指社交平台封号而非游戏封号）使游戏解读不成立——游戏中的塔不会导致'号没了'。",
    final_rationale="公然的敏感话题讨论鼓励+平台管控蔑视，构成政治煽动，判为 high。"
)

add(
    text="和谐你全家，这句话当年有多火，现在就有多讽刺",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["D1_反讽", "C2_历史事件影射"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：回忆'和谐你全家'这个当年的流行语，说它现在变得很讽刺。",
    encoding_analysis="'和谐'在中国互联网中是'审查/删帖/屏蔽'的代称——源自2000年代后期中国互联网的内容管控政策。'和谐你全家'源自绿坝花季护航的衍生梗，已成为对审查制度的经典讽刺。'当年有多火现在就有多讽刺'暗示审查力度随时间推移而加强——从当年的调侃变成如今的现实。对审查制度的明确讽刺和批评。",
    context_analysis="无额外上下文。'和谐'作为审查代称在中文互联网中已完全固化。",
    supporting_evidence="(1) '和谐'在中国互联网中已完全固化为审查的代称；(2) '和谐你全家'是审查讽刺的经典梗——具有历史和文化的双重指代；(3) '现在更讽刺'暗示审查力度随时间加强——构成对审查制度的历史性批评。",
    counter_evidence="可能是对网络流行文化的怀旧。但配合'现在更讽刺'的现实指涉，纯怀旧解读不成立。",
    final_rationale="审查制度的经典讽刺+历史性批评，对网络内容管控的明确攻击，判为 high。"
)

add(
    text="你们有没有发现，现在的互联网越来越干净了，干净到什么都没有了",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_隐喻", "E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：注意到互联网越来越干净了，干净到什么都没有了。",
    encoding_analysis="这是对网络内容管控/审查清除的经典先捧后杀讽刺。'越来越干净'先是正面评价（干净=无不良信息），然后'干净到什么都没有了'将正面含义翻转为负面——将'干净'等同于'空无一物'，讽刺审查已经过度到扼杀了互联网的所有内容。官方话语挪用+自我否定结构的贴吧经典模式。",
    context_analysis="无额外上下文。'干净=空'的讽刺在贴吧中是对过度审查的经典评价模式。",
    supporting_evidence="(1) '干净'挪用官方正面话语——官方对网络整治的正面描述；(2) '什么都没有了'将正面评价翻转为负面讽刺——揭示了'干净'的另一面是'空'；(3) 先捧后杀的完整贴吧结构。对网络内容管控的系统性讽刺。",
    counter_evidence="可能是对某个小众社区没落的感慨。但'互联网越来越干净'的宏大范围使其指向整体互联网环境而非特定社区。",
    final_rationale="内容管控的经典先捧后杀讽刺，对网络审查的系统性攻击，判为 high。"
)

add(
    text="每一次说话之前都要想一想，这话会不会害我被查水表",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["D1_反讽", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：每次说话前需要思考这话会不会导致被查水表。",
    encoding_analysis="'查水表'源自网络流行语（快递/查水表/送外卖→警方上门调查），已被固化为'被警方/国安约谈/调查'的代称。'每一次说话都要想一想'描述了言论审查/自我审查的常态化——将自我审查描述为日常行为。这构成了对言论管控/社会监控体系的明确讽刺和批评。",
    context_analysis="无额外上下文。'查水表'在中文互联网中已被固化为'被警方调查'的经典代称。",
    supporting_evidence="(1) '查水表'是警方调查的经典代称；(2) '每一次说话都要想'描述自我审查的常态化——暗示言论环境的高压；(3) 将自我审查描述为日常习惯构成了对言论管控体系的讽刺性揭露。完整的言论环境批评。",
    counter_evidence="可能是朋友间开玩笑——讨论谨慎发言的习惯。但配合'查水表'这一政治化的代称，纯玩笑解读偏弱。",
    final_rationale="言论审查/自我审查的经典讽刺，对言论管控体系的明确攻击，判为 high。"
)

add(
    text="这瓶水不仅要喝，还要喝出感情来，不喝就是不识抬举",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_隐喻", "C4_典故/物品/符号借用"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：说这瓶水不仅要喝还要喝出感情，不喝就是不知好歹。",
    encoding_analysis="'喝（茶）'在中文互联网鉴证话语中已被固化为'被警方/国安约谈'的代称。'不仅要喝还要喝出感情'讽刺了将被迫接受的行为包装为'自愿自愿'的逻辑——暗示在高压环境下，被约谈者不仅要接受调查还要表现出配合/感恩的态度。'不喝就是不识抬举'进一步讽刺了这种强制性——将拒绝约谈/不配合等同于'不识抬举'。",
    context_analysis="无额外上下文。'喝茶'作为警方约谈的代称在中文互联网中已完全固化。",
    supporting_evidence="(1) '喝茶'是警方约谈的经典代称；(2) '喝出感情'讽刺了将被迫行为包装为自愿的强制性逻辑；(3) '不喝就是不识抬举'进一步讽刺了不配合的后果。三重信号构成对警方约谈/言论管控体系的系统性讽刺。",
    counter_evidence="可能是关于饮茶文化的正常讨论。但在互联网讨论中，'茶'作为约谈代称的使用已使正常饮茶讨论不时受到此语义的污染。",
    final_rationale="警方约谈制度的经典讽刺，对言论管控体系的系统性攻击，判为 high。"
)

add(
    text="改开党的路子走不通了，该换换思路了",
    risk_level="high",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["D1_反讽", "C2_历史事件影射"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：说'改开党'的路走不通了，需要换思路。",
    encoding_analysis="'改开党'是左翼/毛派网民对中共改革开放派系的讽刺性称呼——将改革开放政策视为一个'党派'的错误路线。'路子走不通了'对改革开放40年政策的全盘否定。'该换换思路了'暗示需要回到更左/更激进的路线。这是对中国现行经济/政治体制的系统性攻击。",
    context_analysis="无额外上下文。'改开党'在特定政治社群中已固化为对改革开放路线的讽刺性称呼。",
    supporting_evidence="(1) '改开党'是对改革开放政策的讽刺性标签——将国策贬低为'一个党派的路线'；(2) '走不通了'对40年改革开放政策的全盘否定；(3) '换思路'暗示需要改变基本路线——对现行体制的明确攻击。",
    counter_evidence="可能是对某个企业改革政策的正常讨论。但'改开党'这一特定政治标签在企业管理讨论中不自然。",
    final_rationale="改革开放政策全盘否定的系统性体制攻击，判为 high。"
)

add(
    text="天朝大局域网了解一下，网速快内容少主打一个干净",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["D1_反讽", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：推荐'天朝大局域网'——特点是速度快但内容少，主打干净。",
    encoding_analysis="'天朝大局域网'是GFW/中国互联网限制的经典讽刺性称呼——将全球互联网贬称为'大局域网'（只能访问国内的局域网），讽刺了网络审查造成的互联网封闭。'网速快内容少主打干净'是贴吧阴阳怪气——表面推销实则讽刺GFW过滤了大量内容。这是对网络审查/GFW的明确讽刺和攻击。",
    context_analysis="无额外上下文。'天朝大局域网'在鉴证圈中已固化为对中国互联网的讽刺性称呼。",
    supporting_evidence="(1) '天朝大局域网'是对中国互联网/GFW的经典讽刺称呼；(2) '内容少主打干净'讽刺了审查导致的信息贫乏——'干净'=被过滤后的空虚；(3) 推销式讽刺——贴吧阴阳怪气的经典模式。对网络审查的系统性讽刺。",
    counter_evidence="可能是对某个企业内网的讨论。但'天朝'的国家层面指代使其指向国家级的网络政策而非企业。",
    final_rationale="GFW/网络审查的系统性讽刺，对网络管控政策的明确攻击，判为 high。"
)

add(
    text="一切为了你好，所以你要听话，不听话就是不识好歹",
    risk_level="high",
    encoding_primary="D2_隐喻",
    encoding_secondary=["D1_反讽", "C4_典故/物品/符号借用"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：以'为你好'为理由要求听话，不听话就是不知好歹。",
    encoding_analysis="这句话在贴吧鉴证中是对家长式统治/威权治理逻辑的经典讽刺。'一切为了你好'模仿官方话语（政策/管控以人民利益为名），'你要听话'要求服从，'不听话就是不识好歹'将不服从等同于道德缺陷。完整的威权主义治理逻辑讽刺——将国家-公民关系歪曲为家长-子女关系中的强制性'关爱'。",
    context_analysis="无额外上下文。家长式治理逻辑的讽刺在贴吧中是对中国政治体制的经典批评模式。",
    supporting_evidence="(1) '为你好'挪用官方话语逻辑——政策/管控总是以人民利益为名；(2) '要听话'暗示对服从的要求——威权治理的核心特征；(3) '不听话就是不识好歹'讽刺了将异议等同于道德缺陷的逻辑。完整的威权治理批评。",
    counter_evidence="可能是对家庭教育方式的讨论。但在公共讨论的宏大语境中，'一切为了你好+你要听话'的逻辑结构在政治批评中已有成熟的隐喻使用。",
    final_rationale="威权治理逻辑的经典隐喻化讽刺，对政治体制的系统性攻击，判为 high。"
)

add(
    text="你是民我是主，咱俩加一块就是民主",
    risk_level="high",
    encoding_primary="B1_拆字",
    encoding_secondary=["D1_反讽", "F_组合编码"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：用拆字法调侃——'你是民，我是主，加起来是民主'。",
    encoding_analysis="拆字式政治讽刺——将'民主'拆解为'你是民（人民），我是主（主人）'——暗示中国的'民主'实质上是'人民的名义+一个人的主宰'。这种拆字法将政治概念的字形拆解来揭示/讽刺其实际运作逻辑，是中文互联网政治讽刺的经典手法。直指中国政治体制核心——'民主'概念的被扭曲。",
    context_analysis="无额外上下文。拆字讽刺是中文互联网政治表达的经典手法。",
    supporting_evidence="(1) 拆字法将'民主'解构为'民+主=你是民我是主'——揭示/讽刺了'民主'在中国语境下的实质性扭曲；(2) 拆字这一形式本身就暗示了对文字/话语操控的讽刺——呼应了官方对'民主'定义的重塑；(3) 极简而有力的政治讽刺结构。对中国政治体制核心概念的明确攻击。",
    counter_evidence="可能是对文字结构的文字游戏/语言学讨论。但配合政治语境，纯文字游戏的解释极为勉强。",
    final_rationale="拆字法对'民主'概念的讽刺解构，对中国政治体制核心的攻击，判为 high。"
)

add(
    text="听说过一句话吗：当一个人说你错了，可能是他错了。当所有人说你错了，那一定是统计口径的问题",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_隐喻", "C3_数字代指"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：用'统计口径'来解释为什么当所有人都说你错时，仍然不是你的问题。",
    encoding_analysis="这是对官方统计数据/话语操控的经典讽刺。前半句设立一个正常逻辑预期（多数人认为你错→你可能有错），后半句用'统计口径'推翻——暗示官方可以通过调整统计口径/话语框架来使任何批评'不算数'。'统计口径的问题'讽刺了官方通过定义/统计/话语的操控来消解批评的模式。",
    context_analysis="无额外上下文。'统计口径'在贴吧中是讽刺官方数据/话语操控的经典代称。",
    supporting_evidence="(1) '统计口径'在贴吧中是官方数据/话语操控的经典讽刺标签；(2) 通过'定义权'来消除批评的逻辑揭露——贴吧对官方话语权的解构；(3) 讽刺结构的完整性——从正常逻辑到官方逻辑的转折。对官方话语/统计可信度的明确攻击。",
    counter_evidence="可能是对某个企业内部数据统计的讨论。但'统计口径'在公共政治讨论中的讽刺使用已使其超出了企业管理讨论的范围。",
    final_rationale="官方数据/话语操控的经典讽刺，对官方可信度的系统性攻击，判为 high。"
)

add(
    text="中国特色这几个字真是万能，前面加什么都合理",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_隐喻", "C4_典故/物品/符号借用"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：评论'中国特色'这个词很万能——加在任何词前面都合理。",
    encoding_analysis="这是对'中国特色社会主义'话语框架的经典讽刺。'中国特色'作为官方话语中的核心限定词（用来解释中国不同于西方模式的各种制度安排），在贴吧鉴证中被讽刺为一个'万能修饰词'——暗示它可以为任何不合理的制度/做法提供话语合法性。'前面加什么都合理'讽刺了该话语框架的空洞性——它可以被用来为任何东西辩护。",
    context_analysis="无额外上下文。'中国特色'作为万能修饰词的讽刺在贴吧中成熟。",
    supporting_evidence="(1) '中国特色'挪用官方核心话语进行讽刺；(2) '万能'暗示该话语框架的空洞性——可用来为任何不合理之事辩护；(3) '前面加什么都合理'直接揭露了话语权力——定义的权力。对中国官方核心话语体系的明确解构。",
    counter_evidence="可能是对'中国特色'作为文化标签的正常讨论。但'万能''加什么都合理'的讽刺口吻使其超出了正常文化讨论的范围。",
    final_rationale="官方核心话语框架的系统性解构，对中国政治话语体系的攻击，判为 high。"
)

add(
    text="惠台办又发福利了，对岸的人真幸福，我们这边的待遇什么时候也能这么好",
    risk_level="high",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["D1_反讽", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：评论台湾事务办公室对台湾的优惠政策，表达对政策偏向的不满。",
    encoding_analysis="'惠台办'是'跪台办/施舍办'等讽刺性称呼的变体——贴吧网民对国台办对台'让利'政策的贬称。'发福利'讽刺了对台的不断经济让利。'我们这边'暗示大陆民众——将大陆民众与台湾民众的待遇进行对比，暗示惠台政策以牺牲大陆民众利益为代价。这是对国台办政策的明确攻击。",
    context_analysis="无额外上下文。'惠台办/跪台办'在贴吧中是国台办的固定讽刺称呼。",
    supporting_evidence="(1) '惠台办'是对国台办政策的讽刺性称呼；(2) '发福利'讽刺了对台经济让利——贬低为'施舍/福利'；(3) '我们这边什么时候能这么好'将惠台与大陆民众利益对立。完整的对台政策攻击。",
    counter_evidence="可能是对两岸政策的正常讨论。但'惠台办'这一特定讽刺标签使正常的政策讨论解读不成立。",
    final_rationale="国台办/对台政策的明确攻击，利用两岸对比煽动不满，判为 high。"
)


# ================================================================
# SECTION 3: 消极社会思想/意识形态攻击 (8 samples)
# ================================================================

add(
    text="努力有什么用，投个好胎比什么都强",
    risk_level="high",
    encoding_primary="D2_隐喻",
    encoding_secondary=["D1_反讽", "E3_话题/热点触发"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：说努力没有用，投胎到好家庭比什么都重要。",
    encoding_analysis="这是对阶层固化/社会不公的极端消极表达。'努力没用'否定了社会基本价值观——勤劳致富/奋斗改变命运。'投个好胎'将人生成败完全归因于出身——暗示社会已完全固化，个人努力无法改变命运。这构成了对社会制度的全盘否定和对奋斗价值观的瓦解。",
    context_analysis="无额外上下文。'努力没用+投胎决定论'在贴吧中是经典的消极社会思想表达。",
    supporting_evidence="(1) '努力没用'直接否定了社会主义核心价值观中的'奋斗'精神；(2) '投个好胎'将社会描述为完全由出身决定的固化结构——对社会流动性的全盘否定；(3) 消极思想的传播性——这种表达鼓励读者放弃努力接受'现实'。",
    counter_evidence="可能是个人情绪发泄——一时的挫折感表达。但在公共讨论中传播这种绝对化的消极思想具有社会破坏性。",
    final_rationale="阶层固化的极端消极思想表达，否定社会核心价值观，判为 high。"
)

add(
    text="说什么奋斗改变命运，都是骗打工人的，老板的孩子还是老板",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_隐喻", "E3_话题/热点触发"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：说'奋斗改变命运'是欺骗打工人的谎言——老板的孩子仍然是老板。",
    encoding_analysis="这是对'奋斗改变命运'这一社会主流价值观的系统性质疑。'都是骗打工人的'将官方提倡的奋斗精神贬低为欺骗/洗脑。'老板的孩子还是老板'用阶层复制的现实来反驳社会流动性的承诺。这构成了对社会主义核心价值观的系统性攻击和对社会制度的全盘否定。",
    context_analysis="无额外上下文。'奋斗vs老板的孩子'在贴吧中是经典的阶层固化叙事。",
    supporting_evidence="(1) '奋斗改变命运'被定义为'骗'——直接否定社会核心价值观；(2) '老板的孩子还是老板'用阶层复制来论证——暗示社会已被阶层固化；(3) 系统性否定——不是批评个别现象而是否定整个社会流动机制。",
    counter_evidence="可能是对个人职场经历的不满表达。但在公共讨论中传播这种系统性的社会否定具有煽动社会对立的危险。",
    final_rationale="社会核心价值观的系统性否定，煽动阶层对立，判为 high。"
)

add(
    text="爱国能当饭吃吗？不能。能当房子住吗？不能。那我爱它干什么",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["D2_隐喻", "D2_夸张/反话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：用功利主义的逻辑否定爱国的价值——爱国不能换饭吃/房子，没有实用价值。",
    encoding_analysis="这是将爱国主义彻底功利化/庸俗化的极端消极思想。通过'爱国不能当X'的排比句式，将爱国情感贬低为没有任何实际效用的虚无之物。'那我爱它干什么'的结论将个人利益与国家认同完全对立起来——暗示如果国家不能给个人带来物质利益，个人就没有理由爱国。这是对爱国主义这一社会核心价值的系统性消解。",
    context_analysis="无额外上下文。'爱国不能当X'的功利化消解在消极思想传播中成熟。",
    supporting_evidence="(1) 将爱国彻底功利化——用物质利益来衡量爱国价值；(2) '不能当饭吃/房子住'用生存压力来消解爱国情感——暗示生存优先于国家认同；(3) 排比+结论的修辞结构强化了说服力——对爱国主义的系统性消解。",
    counter_evidence="可能是对生活压力的个人情绪发泄。但在公共讨论中，这种将爱国功利化的表述传播了危险的消极思想。",
    final_rationale="爱国主义的系统性功利化消解，传播危害国家认同的消极思想，判为 high。"
)

add(
    text="活着的意义是什么？还房贷，然后死了",
    risk_level="high",
    encoding_primary="D2_隐喻",
    encoding_secondary=["D1_反讽", "E3_话题/热点触发"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：人生意义就是还房贷然后死去——极其消极的人生观表达。",
    encoding_analysis="这是对当代中国年轻人生活状态的极端绝望表达。将人生的全部意义压缩为'还房贷→死'两个节点，完全消解了人生的所有其他价值——家庭、事业、社会贡献、精神追求等。这种将社会压力极致简化为生存痛苦的叙事在贴吧消极文化中极为常见，具有强烈的情绪传染性和社会破坏力。",
    context_analysis="无额外上下文。'还房贷=人生全部'在贴吧消极文化中是经典的绝望叙事。",
    supporting_evidence="(1) 人生意义的极端简化——从多元价值压缩为单一痛苦；(2) '还房贷'控诉高房价/经济压力——将社会问题内化为人生绝望；(3) '然后死了'的虚无主义结尾——完全消解了生存意义。具有极强传染性的社会消极思想。",
    counter_evidence="可能是个人短暂的低落情绪表达。但在公共讨论中，这种极端消极的表达会被大量共鸣者传播和强化。",
    final_rationale="极端虚无主义的社会消极思想表达，具有强社会传染性，判为 high。"
)

add(
    text="这个社会就是你踩我我踩你，谁也别装好人",
    risk_level="high",
    encoding_primary="D2_隐喻",
    encoding_secondary=["D1_反讽", "E3_话题/热点触发"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：社会就是相互踩踏的关系，没有人是好人。",
    encoding_analysis="这是对社会道德/合作基础的彻底否定。'你踩我我踩你'将社会关系描述为零和的丛林法则——否定了一切合作/互助/信任的可能性。'谁也别装好人'进一步消解了道德行为的动机——将一切善行都视为伪装/表演。这构成了对社会道德基础和人际信任的系统性破坏。",
    context_analysis="无额外上下文。'你踩我我踩你'在消极社会思想中是经典的丛林社会叙事。",
    supporting_evidence="(1) 社会关系的彻底丛林化——否定合作/互助的可能；(2) '谁也别装好人'消解一切道德行为的动机——将善定义为伪善；(3) 对社会信任基础的全面攻击。具有破坏社会凝聚力的危险性。",
    counter_evidence="可能是对职场/特定环境的个人感受。但在公共讨论中，这种对社会整体的绝对否定具有危险性。",
    final_rationale="社会道德/信任基础的系统性消解，传播丛林社会消极思想，判为 high。"
)

add(
    text="你们有没有一种感觉，就是在等一个不知道会不会来的东西",
    risk_level="high",
    encoding_primary="D2_隐喻",
    encoding_secondary=["E1_平台黑话", "D1_反讽"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：表达一种等待感——在等一个不知是否会到来的东西。",
    encoding_analysis="在贴吧鉴证语境中，'在等一个不知道会不会来的东西'是对政治变革/社会变天的含蓄期待——'等的东西'可能指向政治变革/体制变革/社会动荡。'不知道会不会来'表达了不确定性和绝望感——可能永远等不到但仍在等。这种'等待变革'的含蓄表达在高压环境中是对政治变革期待的经典编码。",
    context_analysis="无额外上下文。'等待某个东西'在贴吧鉴证中是政治变革期待的经典含蓄表达。",
    supporting_evidence="(1) '在等一个东西'的刻意模糊——不便直说但暗示了重大的期待对象；(2) '不知道会不会来'表达了绝望与希望的混合——典型的政治变革期待叙事；(3) '你们有没有'寻求共鸣——将个人等待转化为集体体验。含蓄的政治变革期待。",
    counter_evidence="可能是对个人生活（如等offer/等机会）的正常表达。但'你们有没有'的集体共鸣呼唤和'不知道会不会来'的绝望暗示使其超出了个人生活的范围。",
    final_rationale="政治变革期待的含蓄编码，传播消极等待/社会变天思想，判为 high。"
)

add(
    text="下辈子不来了，这个地方太累了",
    risk_level="high",
    encoding_primary="D2_隐喻",
    encoding_secondary=["D1_反讽", "E3_话题/热点触发"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：表达对生命的厌倦——下辈子不想再来了，这个地方太累了。",
    encoding_analysis="'下辈子不来了'是中文互联网中最常见的极端消极表达之一。'这个地方'在此语境中有双重指代——字面指代世界/人生，但在鉴证语境中常隐喻中国。'太累了'将社会压力/生活艰辛压缩为身体感受。这种极简的绝望表达在贴吧中具有极强的传染性和影响力。",
    context_analysis="无额外上下文。'下辈子不来了'在中文互联网消极文化中极为流行。",
    supporting_evidence="(1) '下辈子不来了'直接表达了对生命的否定；(2) '这个地方'的双重指代——表面指世界，在特定语境中隐喻国家/社会；(3) '太累了'将系统性社会问题压缩为个人感受——简单但极具传染性的消极表达。",
    counter_evidence="可能是对生活压力的短暂情绪发泄。但'下辈子不来了'的极端绝望程度使其超出了正常情绪发泄。",
    final_rationale="极端消极生命态度+可能的国家隐喻，具有强传染性的消极思想，判为 high。"
)

add(
    text="我们是韭菜，他们的镰刀从来没停过",
    risk_level="high",
    encoding_primary="D2_隐喻",
    encoding_secondary=["C4_典故/物品/符号借用", "D1_反讽"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：将自己比喻为韭菜，说收割者的镰刀从未停止。",
    encoding_analysis="'韭菜-镰刀'在中文互联网中已成为阶层剥削/压榨的经典隐喻。(1) '韭菜'=普通民众/底层人民——被反复收割的对象；(2) '镰刀'=收割者/统治阶层/资本家——持续获取利益的人。'从来没停过'暗示剥削是持续/制度性的——不是偶发现象而是系统运作。这是对经济/政治制度的系统性负面定义。",
    context_analysis="无额外上下文。'韭菜-镰刀'隐喻在中文互联网中已完全固化。",
    supporting_evidence="(1) '韭菜-镰刀'是阶层剥削的成熟隐喻——在中国互联网中已完全固化；(2) '他们'的模糊指代——暗示不便直说的统治/剥削阶层；(3) '从来没停过'暗示剥削的制度性——不是偶发而是系统运作。对制度合法性的系统性攻击。",
    counter_evidence="可能是对商业消费行为的批评（商家割消费者韭菜）。但配合'他们'的政治暗示和'从来没停过'的制度性描述，纯商业批评的解释偏弱。",
    final_rationale="阶层剥削隐喻的系统性制度攻击，煽动阶级对立，判为 high。"
)


# ================================================================
# SECTION 4: 群体攻击/政治标签 (7 samples)
# ================================================================

add(
    text="小粉红又来刷屏了，能不能带点脑子再来上网",
    risk_level="high",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["D1_反讽", "E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：攻击被称为'小粉红'的人群，说他们刷屏且无脑。",
    encoding_analysis="'小粉红'是中国互联网中对爱国年轻网民群体的贬称/蔑称——暗示他们朴素麻木、盲目爱国而忽略社会弊病。'不带脑子'是典型的智力贬低攻击。'刷屏'暗示其行为是组织化的（如网评员）。这是对中国爱国网民群体的系统性贬低和群体攻击。",
    context_analysis="无额外上下文。'小粉红'在中文互联网中已固化为对爱国网民的贬称。",
    supporting_evidence="(1) '小粉红'是对爱国网民群体的固定贬称——暗示其'盲目+幼稚+被洗脑'；(2) '不带脑子'是系统性智力贬低；(3) '刷屏'暗示组织化行为——将爱国表达污名化为有组织的宣传。对爱国网民群体的恶意贬低。",
    counter_evidence="可能是对网络评论质量的正常吐槽。但'小粉红'这一特定政治标签使其超出了正常的网络讨论范围。",
    final_rationale="对爱国网民群体的系统性贬低和群体攻击，煽动网络对立，判为 high。"
)

add(
    text="五毛又出来上班了，今天发了几条啊",
    risk_level="high",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["D1_反讽", "E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：嘲笑被称为'五毛'的人又开始工作了，问他们今天发了多少条。",
    encoding_analysis="'五毛'是中国互联网中对政府网络评论员的经典贬称——源自每条评论0.5元的传闻。'上班了'将爱国言论贬低为有偿工作——暗示发表爱国言论不是出于真实情感而是受雇行为。'今天发了几条'进一步将爱国表达量化为计件工作。这是对网络评论员制度的明确攻击和对爱国言论的系统性贬低。",
    context_analysis="无额外上下文。'五毛'在中文互联网中已固化为对政府网络评论员的贬称。",
    supporting_evidence="(1) '五毛'是对网络评论员的固定贬称——有具体的历史出处；(2) '上班'将爱国表达污名化为雇佣行为——否定爱国言论的真实性；(3) '发了几条'将爱国言论量化为计件工作——进一步贬低。对网络评论制度的系统性攻击。",
    counter_evidence="可能是朋友间的玩笑。但在公共讨论中，'五毛'标签是用来消解对方发言合法性的政治攻击工具。",
    final_rationale="对政府网络评论制度的明确攻击和爱国言论的系统性贬低，判为 high。"
)

add(
    text="赵家人当然过得好了，人家什么时候不好过",
    risk_level="high",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["C1_历史人物类比", "D1_反讽"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：评论'赵家人'当然生活好，他们从来没过过不好的日子。",
    encoding_analysis="'赵家人'源自鲁迅《阿Q正传》中'赵太爷'，在当代中国互联网中已被固化为对中共权贵阶层及其子女的贬称——暗示他们享有普通人无法企及的特权和资源。'当然过得好'暗示权贵阶层的特权是理所当然的——构成了对体制性特权/不平等的明确攻击。",
    context_analysis="无额外上下文。'赵家人'在中文互联网中已固化为对中共权贵阶层的贬称。",
    supporting_evidence="(1) '赵家人'是对中共权贵阶层的固定贬称——有文学和历史出处；(2) '当然过得好'暗示特权是系统性的——不是个人努力而是体制保障；(3) '从来没不好过'暗示权贵阶层与普通民众的差距是永久性的。对政治体制特权/不平等的明确攻击。",
    counter_evidence="可能是对某个赵姓家族的正常讨论。但在公共讨论中，'赵家人'作为政治标签的使用已使其脱离了普通姓氏讨论。",
    final_rationale="中共权贵阶层的贬低性标签攻击，煽动对政治体制的不满，判为 high。"
)

add(
    text="神神们又在团建了，今天又有什么新的躺平心得",
    risk_level="high",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["D1_反讽", "E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：说'神神'们又在集体活动了，问有什么新的躺平心得。",
    encoding_analysis="'神神/神友'源自百度贴吧'神奈川冲浪里'吧——该社群以极端消极/反社会/政治不满言论著称，已成为中文互联网中消极/反社会亚文化的代称。'团建'讽刺了该群体的集体行动特征。'躺平心得'暗示该群体的核心话语——放弃努力/退出社会竞争。这是对消极/反社会亚文化群体的描述和间接传播。",
    context_analysis="无额外上下文。'神神'在中文互联网中已固化为特定消极亚文化群体的标签。",
    supporting_evidence="(1) '神神/神友'是对特定消极/反社会亚文化群体的固定标签；(2) '团建'暗示了集体行动/组织化特征；(3) '躺平心得'暗示该群体的核心意识形态——放弃社会参与。对消极亚文化的描述性传播。",
    counter_evidence="可能是对特定游戏/兴趣社群的讨论。但'神神'在中文互联网中已具有特定的政治/亚文化含义。",
    final_rationale="消极/反社会亚文化群体的标签化传播，间接鼓励极端消极思想，判为 high。"
)

add(
    text="不是我说，有些人就是跪久了站不起来，看到外国人就腿软",
    risk_level="high",
    encoding_primary="D2_隐喻",
    encoding_secondary=["D1_反讽", "C4_典故/物品/符号借用"],
    needs_context=False,
    hard_negative=False,
    ambiguity="medium",
    literal_analysis="文本字面意思：批评某些人'跪久了站不起来'——见到外国人就自卑/屈服。",
    encoding_analysis="'跪久了站不起来'在中国互联网中是经典的政治攻击用语——用于指责那些被认为'崇洋媚外/亲西方/不爱国'的人。'见到外国人就腿软'将国际交往/文化开放贬低为奴性/自卑的表现。这种表述在中文互联网中被广泛用于攻击持不同观点（尤其是亲西方观点）的人——将文化/政治偏好贬低为道德/心理缺陷。",
    context_analysis="无额外上下文。'跪久了站不起来'在中文互联网攻击性话语中已固化为经典模板。",
    supporting_evidence="(1) '跪久了站不起来'是对持不同政治观点者的经典攻击模板；(2) '见到外国人就腿软'将文化开放贬低为奴性；(3) 用身体/道德隐喻攻击政治观点——将观点差异转化为道德/人格缺陷。具有强攻击性的政治对立工具。",
    counter_evidence="可能是对个别人士崇洋媚外行为的批评。但'跪久了站不起来'作为攻击模板的广泛使用使其超出了对具体行为的批评。",
    final_rationale="政治观点差异的人格化攻击，煽动网络对立和群体仇恨，判为 high。"
)

add(
    text="现在还敢说实话的人越来越少了，要么被关要么被删要么自己闭嘴了",
    risk_level="high",
    encoding_primary="D1_反讽",
    encoding_secondary=["E1_平台黑话", "D2_隐喻"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：感叹敢说实话的人越来越少——要么被关起来，要么内容被删，要么自我审查。",
    encoding_analysis="这是对言论管控/政治打压的明确指控。'被关'（坐牢）、'被删'（删帖/封号）、'自己闭嘴'（自我审查）——三个递进的后果描述了言论管控的完整链条。'说实话的人'在此语境中暗示批评政府/体制的人。这构成了对言论管控体系的直接指控——将正常的社会治理描述为政治打压。",
    context_analysis="无额外上下文。'被关/被删/闭嘴'的三段论在贴吧中是经典的言论管控指控模式。",
    supporting_evidence="(1) '被关'直接指控政治打压/入狱；(2) '被删'指控网络审查/删帖；(3) '自己闭嘴'指控自我审查的寒蝉效应。三段论完整描述了言论管控的因果链——构成了对制度的系统性攻击。",
    counter_evidence="可能是对社会现象的客观描述。但'被关→被删→闭嘴'的递进结构在贴吧政治话语中已固化为对言论管控的控诉模板。",
    final_rationale="言论管控的系统性指控，对政治制度的直接攻击，判为 high。"
)

add(
    text="理中客滚出克，这里不需要你装理性",
    risk_level="high",
    encoding_primary="A2_拼音/首字母缩写",
    encoding_secondary=["D1_反讽", "E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    ambiguity="low",
    literal_analysis="文本字面意思：让'理中客'滚出去，说这里不需要假装理性。",
    encoding_analysis="'理中客'是'理性、中立、客观'的缩写——在中文互联网中被污名化为贬称，用于攻击那些试图理性讨论敏感话题的人。'滚出克'是'滚出去'的谐音变体——增强了攻击性。'装理性'暗示理性讨论是伪装——将理性/中立/客观贬低为虚伪。这构成了对理性讨论本身的系统性攻击。",
    context_analysis="无额外上下文。'理中客'在中文互联网争论中已固化为攻击性标签。",
    supporting_evidence="(1) '理中客'将正面品质（理性中立客观）污名化为攻击标签——颠覆了理性讨论的价值；(2) '滚出克'是明确的驱逐/攻击用语；(3) '装理性'暗示一切理性讨论都是伪装——消解了对话的基础。对理性讨论的系统性攻击。",
    counter_evidence="可能是对特定网友言论风格的不满。但'理中客'作为攻击标签使这种表达超出了对个人的批评——构成对理性讨论本身的攻击。",
    final_rationale="理性讨论价值的系统性消解+攻击性驱逐用语，破坏网络讨论秩序，判为 high。"
)


# ================================================================
# Write output
# ================================================================

print(f"Generated {len(samples)} HIGH-risk national-security samples")

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

# Section breakdown
sections = Counter()
for s in samples:
    t = s['text']
    enc_p = s['encoding_primary']
    # rough categorization
    if enc_p == 'C1_历史人物类比':
        sections['leader_encoding'] += 1
    elif enc_p in ('D1_反讽', 'D2_隐喻') and any(k in t for k in ['伟光正', '墙', '翻墙', '和谐', '冲塔', '查水表', '喝茶', '改开', '天朝', '大局域网', '茧中', '惠台', '统计', '中国特色']):
        sections['policy_attack'] += 1
    elif any(k in t for k in ['努力', '投胎', '奋斗', '爱国能当', '韭菜', '意义', '下辈子', '踩着']):
        sections['negative_ideology'] += 1
    else:
        sections['group_attack'] += 1

print(f"\nSection breakdown (approx):")
for sec, count in sections.most_common():
    print(f"  {sec}: {count}")
