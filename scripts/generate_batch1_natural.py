#!/usr/bin/env python3
"""Generate batch-1 replacement samples with genuine Chinese internet voice.

These replace the oldest grok/gemini/meme synthetic samples that suffer from
template reasoning and unnatural AI-generated text.

All samples follow the project schema and annotation guideline.
"""

from __future__ import annotations

import json
from pathlib import Path

BATCH_ID = "batch1_natural"
ROOT = Path(__file__).resolve().parents[1]

# ── helper ────────────────────────────────────────────────────────
_auto_id = 0


def _next_id():
    global _auto_id
    _auto_id += 1
    return f"{BATCH_ID}_{_auto_id:04d}"


def sample(
    *,
    text: str,
    risk_level: str,
    encoding_primary: str,
    encoding_secondary: list[str] | None = None,
    needs_context: bool = False,
    ambiguity: str = "medium",
    evidence_strength: str = "moderate",
    hard_negative: bool = False,
    context_title: str = "",
    context_topic: str = "",
    literal: list[str],
    encoding: list[str],
    context_analysis: list[str],
    supporting: list[str],
    counter: list[str],
    rationale: str,
) -> dict:
    rec = {
        "id": _next_id(),
        "split": "train",
        "source_type": "synthetic",
        "text": text,
        "context": {
            "title": context_title,
            "description": "",
            "time": "",
            "topic": context_topic,
        },
        "risk_level": risk_level,
        "encoding_primary": encoding_primary,
        "encoding_secondary": encoding_secondary or [],
        "needs_context": needs_context,
        "ambiguity": ambiguity,
        "evidence_strength": evidence_strength,
        "freshness": "stable",
        "hard_negative": hard_negative,
        "target_known": False,
        "target_reference": "",
        "should_explain_target": False,
        "reasoning": {
            "literal_analysis": literal,
            "encoding_analysis": encoding,
            "context_analysis": context_analysis,
            "supporting_evidence": supporting,
            "counter_evidence": counter,
            "final_rationale": rationale,
        },
        "quality_status": "approved",
        "review_notes": f"source={BATCH_ID}; replaces old synthetic",
    }
    if needs_context and not context_title:
        rec["needs_context"] = False  # 没给上下文就不要硬标
    return rec


# ── SAMPLES ────────────────────────────────────────────────────────
records = []

# ═══ C1 历史人物类比 (target: ~15) ═══

records.append(sample(
    text="司马懿最后赢了，靠的就是活得久",
    risk_level="medium", encoding_primary="C1_历史人物类比",
context_topic="历史/政治类比",
    literal=["字面在讲三国人物司马懿靠长寿取胜。"],
    encoding=["司马懿在当代互联网语境中常被用于暗指善于隐忍、最终靠时间取胜的政治人物。", "是C1历史人物类比，用历史人物的叙事映射现实。"],
    context_analysis=["无具体上下文，但该类比在简中互联网已成固定映射。"],
    supporting=["司马懿的'隐忍—等待—反杀'叙事与现实权力更迭叙事高度重合。", "使用'活得久'暗示的不是寿命而是政治周期。"],
    counter=["脱离特定语境仅凭一句历史评价，也可能是正常历史讨论。", "没有目标人物的明确指向。"],
    rationale="司马懿类比在简中圈层已成稳定代指，但本句无具体事件锚点，普通历史讨论解释仍有相当可能，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="读史的时候发现，每个朝代末期出现的'忠臣'都特别多",
    risk_level="medium", encoding_primary="C1_历史人物类比",
    encoding_secondary=["D1_反讽"],
context_topic="历史讨论",
    literal=["字面讨论历史规律：朝代末期会出现很多忠臣。"],
    encoding=["表面是历史规律讨论，实际用'忠臣'反讽现实中某些人的自我标榜。", "C1+反讽组合：借历史概念映射现实政治表态。"],
    context_analysis=["无上下文但从文本反讽语气可判断有隐含指向。"],
    supporting=["'忠臣'在当代政治讨论中已成为特定讽刺对象。", "句式'每个…都特别多'是简中互联网常见阴阳怪气句式。"],
    counter=["如果没有政治敏感度，可以仅解读为正常历史讨论。", "不排除真是历史爱好者的一般感慨。"],
    rationale="文本有典型互联网反讽句式+政治隐射历史类比，但在没有上下文时存在普通解读可能，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="海瑞放到今天，估计连个科员都当不上",
    risk_level="medium", encoding_primary="C1_历史人物类比",
context_topic="历史/体制讨论",
    literal=["字面讨论明朝清官海瑞在今天体制内会碰壁。"],
    encoding=["用历史上著名清官'海瑞'映射对当代体制用人逻辑的批评。", "C1类比：海瑞=正直不阿的人，'科员都当不上'=体制容不下这样的人。"],
    context_analysis=["无明确上下文，依靠海瑞在中国文化中的固定象征意义。"],
    supporting=["海瑞的形象高度固化（清廉、不妥协、得罪权贵），使得映射方向明确。", "评论模式是经典简中'借古讽今'句式。"],
    counter=["也可能是纯粹的历史虚构想象，无恶意的假如讨论。", "没有指向具体现实人物或事件。"],
    rationale="借古讽今的经典C1模式，但缺乏具体锚点，政治隐射方向明确但指涉泛化，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="赵高指鹿为马的时候，满朝文武都在配合演出",
    risk_level="high", encoding_primary="C1_历史人物类比",

    literal=["字面讲述秦朝赵高指鹿为马的典故。"],
    encoding=["用'赵高指鹿为马'+'满朝文武配合'映射现实中对明显谎言的集体默认。", "C1类比：赵高=特定权力人物，指鹿为马=颠倒黑白，满朝文武配合=体制内集体失语。"],
    context_analysis=["典故意象本身足够形成强编码，无需外部上下文。"],
    supporting=["'指鹿为马'的典故已经高度固化，在简中互联网政治讨论中方向明确。", "'配合演出'的加入强化了对现实集体行为的讽刺。"],
    counter=["严格来说也可以是单纯的历史典故讨论，但'配合演出'这个现代词的使用降低了纯历史讨论的可能。"],
    rationale="固化典故+现代词'配合演出'共同指向对现实的讽刺映射，典故方向明确，判high。",
    ambiguity="low", evidence_strength="strong",
))

records.append(sample(
    text="王莽谦恭未篡时",
    risk_level="high", encoding_primary="C1_历史人物类比",
context_topic="历史/政治讨论",
    literal=["字面引用白居易诗句，讲王莽篡位前的谦恭。"],
    encoding=["这是一句在简中互联网高度固化的政治隐射诗句。", "C1类比：王莽=篡位前表现得极为谦恭的政治人物，整句暗示某人当下在伪装。"],
    context_analysis=["这句诗本身已构成完整表达，在特定圈层中理解一致，不需额外上下文。"],
    supporting=["高度固化：该诗句在鉴证圈层中是常见的'半句诗'表达，后半句'向使当初身便死'被省略，形成固定隐射。"],
    counter=["单纯从字面看，确实可以是在讨论白居易的诗或王莽的历史。", "但这种解释在简中互联网语境下权重极低。"],
    rationale="高度固化的鉴证圈'半句诗'，省略后半句形成无需上下文的强编码，判high。",
    ambiguity="low", evidence_strength="strong",
))

records.append(sample(
    text="今天看到一句话：'后人哀之而不鉴之'，真绷不住",
    risk_level="medium", encoding_primary="C1_历史人物类比",
    encoding_secondary=["D1_反讽"],

    literal=["引用《阿房宫赋》的名句，表达感慨。"],
    encoding=["杜牧的'秦人不暇自哀…后人哀之而不鉴之'在当代互联网常用于影射'重复历史错误'。", "加上'绷不住'暗示这不是纯粹文学讨论。"],
    context_analysis=["句中未指明具体指涉对象，但互联网共识使得映射方向明确。"],
    supporting=["该赋文在政治讽刺中属于高频引用。", "'绷不住'是当代互联网情绪词，表明有现实触发。"],
    counter=["普通文学青年讨论古文的可能确实存在。", "没有明确时间节点或事件对应。"],
    rationale="经典古文引用+当代互联网情绪词，暗示有现实映射，但缺乏具体事件锚点，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="推荐大家去看看申生和重耳的故事",
    risk_level="medium", encoding_primary="C1_历史人物类比",

    literal=["建议读者了解春秋时期晋国公子申生和重耳的典故。"],
    encoding=["申生（留在国内被逼死）vs 重耳（流亡后归国掌权）的对比在鉴证圈常用于类比现实政治流亡与留守。"],
    context_analysis=["该典故建议出现在敏感时间节点或政治讨论中时风险升级；裸文本在medium。"],
    supporting=["申生/重耳典故在特定圈层已成为固定政治隐喻。"],
    counter=["也可能是正经历史或文学推荐，这组典故本身确实有教育意义。", "没有上下文难以确定推荐动机。"],
    rationale="申生/重耳是固定政治隐喻典故，但裸荐书形式下普通解释仍合理，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="诸葛亮这辈子最聪明的事就是遇到刘备之前一直在种地",
    risk_level="low", encoding_primary="C1_历史人物类比",

    literal=["调侃诸葛亮在出山前的高明之处在于低调务农。"],
    encoding=["可能暗指'聪明的政治人物在时机不对时保持低调'，但指向非常模糊。"],
    context_analysis=["无上下文；这句话更像是B站常见的三国历史调侃。"],
    supporting=["存在微弱的历史政治类比可能。"],
    counter=["B站三国区日常玩梗，'诸葛亮种地'是弹幕常见笑点。", "无任何具体现实映射信号。"],
    rationale="B站三国区常见玩梗，模糊的类比可能不足以构成风险，判low。主要价值在于作为hard negative对照C1高风险样本。",
    ambiguity="high", evidence_strength="weak", hard_negative=True,
))

# ═══ C2 历史事件影射 (target: ~12) ═══

records.append(sample(
    text="建议读读万历十五年，那一年什么都没发生，又什么都在发生",
    risk_level="medium", encoding_primary="C2_历史事件影射",
context_topic="历史/政治讨论",
    literal=["推荐黄仁宇的《万历十五年》，描述该年看似平静实则暗流涌动。"],
    encoding=["'万历十五年'在简中互联网已成为政治隐射的高频引用。", "C2影射：表面讨论明史，实际暗示当代某个'表面平静但暗流涌动'的年份。"],
    context_analysis=["裸文本推荐历史书，但该书在特定圈层的政治隐射含义已高度固化。"],
    supporting=["《万历十五年》在中文互联网的政治讨论中具有特殊地位。", "描述语'什么都没发生又什么都在发生'暗示了现实投射。"],
    counter=["确实是经典历史著作，正常荐书完全合理。", "没有指涉具体现实年份或事件。"],
    rationale="《万历十五年》是鉴证圈高频引用书目，但裸荐书形式下正常解读仍然合理，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="苏联当年从开始到结束也就七十来年，值得深思",
    risk_level="high", encoding_primary="C2_历史事件影射",
context_topic="历史/政治比较",
    literal=["讨论苏联从建立到解体的七十年历程。"],
    encoding=["用苏联的历史周期影射另一个大国政权。", "C2影射：苏联的建立—强盛—僵化—解体叙事被作为比较框架。"],
    context_analysis=["'值得深思'是互联网常用的引导式结尾，暗示读者进行类比。"],
    supporting=["苏联类比是简中互联网政治讨论中最常见的C2模式。", "'七十来年'这个具体数字增强了比较意图。"],
    counter=["单纯讨论苏联历史也是合理的学术/兴趣讨论。", "没有明确说在比较哪个国家。"],
    rationale="苏联政治类比是高度敏感且固化的C2模式，'值得深思'明确引导读者投射到现实，判high。",
    ambiguity="low", evidence_strength="strong",
))

records.append(sample(
    text="历史课本上有些事写得特别简略，越简略越有味道",
    risk_level="medium", encoding_primary="C2_历史事件影射",

    literal=["评论历史教科书中某些事件的简略处理。"],
    encoding=["暗示历史课本中被简略处理的事件包含敏感内容。", "C2影射：用'简略'暗示审查和自我审查。"],
    context_analysis=["不需具体上下文；这是对历史叙事本身的元评论。"],
    supporting=["简中互联网对'历史课本简略处'的讨论有固定指向。", "'越简略越有味道'是暗示性句式。"],
    counter=["也可能是普通学生对课本编写质量的吐槽。", "没有指涉具体历史事件。"],
    rationale="对历史叙事的元评论，暗示性强但缺乏具体事件锚点，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="那十年真的是文化断层，很多好东西都断了传承",
    risk_level="high", encoding_primary="C2_历史事件影射",
context_topic="历史/文化讨论",
    literal=["讨论某个十年时期的文化断层现象。"],
    encoding=["'那十年'在简中语境中有明确固定指向。", "C2影射：用'文化断层'和'断了传承'暗指特定历史时期的破坏。"],
    context_analysis=["'那十年'本身已是简中互联网的固定代指，尽管需要一定背景知识。"],
    supporting=["'那十年'高度固化，是简中语境中无需言明的共识代指。", "提到'传承断了'有明确的损失评价。"],
    counter=["理论上也可以是讨论其他国家的十年。", "但'那十年'在中文语境中的默认指向太强。"],
    rationale="'那十年'是极度固化的代指，在简中语境中几乎没有歧义，判high。",
    ambiguity="low", evidence_strength="strong",
))

records.append(sample(
    text="上次看到这么多人聚集还是……算了不说了",
    risk_level="medium", encoding_primary="C2_历史事件影射",
    encoding_secondary=["E1_平台黑话"],

    literal=["想说上次类似的大规模聚集场景但欲言又止。"],
    encoding=["省略号+欲言又止指向某个敏感的公众聚集事件。", "C2/E1组合：用未完成的比较暗示敏感事件。"],
    context_analysis=["无上下文时指向模糊，但'算了不说了'是强烈的自我审查信号。"],
    supporting=["'算了不说了'在简中互联网是常见的自我审查标记，暗示后续内容敏感。", "句式本身在邀请读者自行脑补。"],
    counter=["也可能是日常吐槽，比如'上次看到这么多人还是演唱会'之类。", "省略的内容可以是无害的。"],
    rationale="自我审查标记明显，但省略的内容方向不确定，无上下文时只能判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="看到新闻联播里又在说形势一片大好，我就放心了",
    risk_level="medium", encoding_primary="D1_反讽",

    literal=["表面说看到新闻联播的正面报道感到放心。"],
    encoding=["简中互联网常见D1反讽模式：'看到…我就放心了'实际含义相反。", "新闻联播被用作官方叙事的代指，表达对官方宣传的不信任。"],
    context_analysis=["这种反讽句式已高度固化，本身就能被识别。"],
    supporting=["'形势一片大好'+'我就放心了'组合是经典简中阴阳怪气句式。", "新闻联播在此语境中不指向具体节目而指向'官方说法'。"],
    counter=["老年用户确实可能真心表达对新闻联播内容的认同。", "但网络语境中该句式的反讽权重远高于字面。"],
    rationale="高度固化的D1反讽句式，在互联网语境中反讽权重远高于字面，但仍有极少数真心使用的可能，判medium。",
    ambiguity="low", evidence_strength="strong",
))

# ═══ C3 数字代指 (target: ~8) ═══

records.append(sample(
    text="64这个数字在某些地方不能随便打",
    risk_level="high", encoding_primary="C3_数字代指",

    literal=["谈论数字64在某些平台被限制。"],
    encoding=["64在简中互联网中是极度固化的数字代指。", "C3：数字本身指向特定历史事件日期。"],
    context_analysis=["无需上下文；64作为数字代指的固化程度极高。"],
    supporting=["64是简中互联网最知名的数字代指，固化程度达到不需要任何额外上下文。"],
    counter=["纯数学讨论64这个数字的可能性在互联网语境下极低。"],
    rationale="极度固化的数字代指，非数学讨论的互联网语境下几乎无歧义，判high。",
    ambiguity="low", evidence_strength="strong",
))

records.append(sample(
    text="8964和1989的区别是什么？一个是算式一个是年份",
    risk_level="high", encoding_primary="C3_数字代指",

    literal=["以数学提问形式区分两个数字。"],
    encoding=["表面在问数字区别，实际通过提问形式唤起特定日期记忆。", "C3+F组合：用数字算式包装，加'年份'提示映射方向。"],
    context_analysis=["无需上下文；该数字组合已高度固化。"],
    supporting=["这种'算式vs年份'的提问形式在简中互联网是经典的规避式唤起。", "两个数字组合都是固化代指。"],
    counter=["纯数学角度，这两个确实可以区分为算式和年份。", "但提问行为本身在互联网语境下有明确的隐含意图。"],
    rationale="极度固化的数字代指+规避式提问组合，实际意图明确，判high。",
    ambiguity="low", evidence_strength="strong",
))

records.append(sample(
    text="那年五月的第四个星期，很多事情都变了",
    risk_level="medium", encoding_primary="C3_数字代指",
    encoding_secondary=["E2_时间节点触发"],

    literal=["模糊地回忆某个五月第四周发生的变化。"],
    encoding=["通过'五月第四周'模糊指代一个具体时间，避免直接说出。", "C3+E2组合：用模糊时间描述替代明确日期。"],
    context_analysis=["在接近特定时间节点发表时风险升级；日常发布则为medium。"],
    supporting=["'五月第四周'+'很多事情都变了'在特定圈层中有固定理解方向。"],
    counter=["也可能是描述个人生活变化，五月毕业季换工作搬家都正常。", "没有直接给出年份。"],
    rationale="模糊时间+感慨句式有编码痕迹但不够强，离开特定时间节点后普通解释仍可能，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="我在06月03日这天总是不太舒服",
    risk_level="low", encoding_primary="C3_数字代指",
    encoding_secondary=["E2_时间节点触发"],

    literal=["表达在6月3日这天身体不适。"],
    encoding=["使用完整日期格式'06月03日'而非口语'6月3号'，可能是有意标注。", "但仅凭日期格式异常不足以构成强证据。"],
    context_analysis=["无其他上下文；如果出现在敏感事件周年附近则风险升级。"],
    supporting=["日期格式的非口语化有点异常。"],
    counter=["真的就是那天不舒服，夏天中暑很正常。", "没有其他编码信号支持。"],
    rationale="仅有日期格式的微弱异常，无其他编码或语境支持，普通解释可能极大，判low。",
    ambiguity="high", evidence_strength="weak", hard_negative=True,
))

records.append(sample(
    text="5+1=6，3+1=4，懂得自然懂",
    risk_level="high", encoding_primary="C3_数字代指",
    encoding_secondary=["F_组合编码"],

    literal=["两道简单算术题，然后说'懂得自然懂'。"],
    encoding=["5+1=6和3+1=4分别映射为64。", "F组合：用数学算式规避+编码提示'懂得自然懂'确认这不是普通算术。"],
    context_analysis=["'懂得自然懂'是强编码确认信号，明确否定普通算术解释。"],
    supporting=["算术结果64+编码确认信号'懂得自然懂'形成强组合。", "普通数学讨论不会加'懂得自然懂'。"],
    counter=["理论上可能是某些游戏或社区的内部梗，指向完全不同的东西。", "但这种算术形式+确认口吻在中文互联网的默认理解方向过于明确。"],
    rationale="数学规避+编码确认信号组合，暗示意图明确，判high。",
    ambiguity="low", evidence_strength="strong",
))

# ═══ C4 典故/物品/符号借用 (target: ~15) ═══

records.append(sample(
    text="最近白纸紧缺，到处买不到",
    risk_level="medium", encoding_primary="C4_典故/物品/符号借用",

    literal=["抱怨白纸缺货，买不到。"],
    encoding=["'白纸'在特定时期获得了强烈政治符号含义。", "C4借用：白纸=特定抗议符号。"],
    context_analysis=["如果出现在白纸运动相关时期则升级为high；日常裸文本为medium。"],
    supporting=["'白纸'+'买不到'的组合在特定时期有明确指向。"],
    counter=["真缺纸在疫情期间发生过，纯粹生活抱怨很合理。", "没有时间或事件锚点。"],
    rationale="白纸在特定时期被赋予了强烈符号意义，但常态化时期普通物价吐槽解释仍合理，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="我家狗又开始叫了，每次电视里那个人出来它就叫",
    risk_level="medium", encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["D3_借代"],

    literal=["描述家里狗对电视里某个人物的反应。"],
    encoding=["用'狗叫'这种看似日常的叙事暗指对某公众人物的厌恶。", "C4借用：狗叫的'本能反感'映射人的政治反感。"],
    context_analysis=["无上下文时存在正常养狗解释，但组合了'电视里那个人'增加了编码可能。"],
    supporting=["'电视里那个人'的含糊表述+狗的反感反应是互联网常见讽刺模板。"],
    counter=["真实养狗人士的日常吐槽完全合理，狗确实会对电视里的人叫。"],
    rationale="有编码可能但正常生活解释权重相当，无上下文时判medium。这是C4/D3交界的好边界样本。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="天安门广场的华表真好看，每次去北京都要看",
    risk_level="low", encoding_primary="C4_典故/物品/符号借用",

    literal=["游客分享天安门华表的观赏体验。"],
    encoding=["华表在特定语境下可能被赋予政治符号含义，但此处的旅游分享口吻非常自然。"],
    context_analysis=["小红书旅游推荐语境，完全没有编码信号。"],
    supporting=["出现'天安门'可能会触发一些关键词匹配系统。"],
    counter=["这是典型的旅游打卡分享，没有任何隐含编码。", "句式自然、语境明确。", "该样本是hard negative：训练模型不要因'天安门'就判风险。"],
    rationale="纯旅游分享，词面有'天安门'但语境完全无害，判low（而非none因为她确实可能触发关键词系统）。",
    ambiguity="low", evidence_strength="weak", hard_negative=True,
))

records.append(sample(
    text="这套西装不错，穿上就像要发表重要讲话",
    risk_level="low", encoding_primary="C4_典故/物品/符号借用",

    literal=["评价一套西装，调侃穿上像要发表讲话。"],
    encoding=["'发表重要讲话'可能微弱的C4借用，暗示某些公众人物形象。", "但整体是小红书常见的穿搭调侃。"],
    context_analysis=["时尚穿搭语境，普通解读占绝对优势。"],
    supporting=["'发表重要讲话'有微弱的政治联想。"],
    counter=["小红书穿搭博主常用类似表达，纯玩笑。", "没有指涉任何具体人物。", "整体氛围轻松无风险。"],
    rationale="穿搭玩笑中的模糊联想，风险极低。适合作为C4类别的hard negative。",
    ambiguity="high", evidence_strength="weak", hard_negative=True,
))

records.append(sample(
    text="最近迷上了养青蛙，每天看它蹲在那里动都不动，特别治愈",
    risk_level="low", encoding_primary="C4_典故/物品/符号借用",

    literal=["分享养宠物青蛙的治愈体验。"],
    encoding=["'青蛙'在特定语境下可能是政治符号，但此处完整自然的宠物叙事使其没有编码意图。"],
    context_analysis=["完整的宠物分享语境，每个细节都指向真实养蛙。"],
    supporting=["'青蛙'一词可能触发关键词误判。"],
    counter=["完整的养宠叙事真实自然。", "'动都不动'+'治愈'是真实宠物日常。", "无任何政治影射信号。"],
    rationale="纯粹宠物日常分享，仅因'青蛙'词面可能被误判。重要hard negative，训练模型识别完整语境。",
    ambiguity="low", evidence_strength="weak", hard_negative=True,
))

records.append(sample(
    text="这个up主被限流了，因为上次那条视频讲了点实在的",
    risk_level="medium", encoding_primary="E1_平台黑话",
    encoding_secondary=["C4_典故/物品/符号借用"],

    literal=["讨论up主因特定视频内容被平台限流。"],
    encoding=["'讲了点实在的'暗示内容触及平台敏感线。", "E1+C4组合：平台规避讨论+'实在的'作为敏感内容的代指。"],
    context_analysis=["B站社区对'限流'和'实在内容'有共识理解。"],
    supporting=["B站用户在讨论限流时，'讲了点实在的'是常见的委婉说法。"],
    counter=["也可能是up主讲了争议性但不涉政的内容，比如批评某个行业或产品。"],
    rationale="有E1平台规避讨论+'实在的'委婉语，但'实在的'可能指非政治内容，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="别喝茶了，这杯茶太贵，不是谁都喝得起",
    risk_level="medium", encoding_primary="C4_典故/物品/符号借用",

    literal=["劝人不要喝某种昂贵的茶。"],
    encoding=["'喝茶'在简中互联网已固化为'被约谈/被调查'的代指。", "C4：茶=约谈。"],
    context_analysis=["'喝不起'强化了隐喻方向—不是真的讨论茶叶价格。"],
    supporting=["互联网语境中'喝茶'+'太贵'+'喝不起'组合，方向明确。"],
    counter=["品茶讨论确实存在，高价位茶叶也是真实消费品。", "但如果是一般消费讨论不会说'不是谁都喝得起'这种话——这明显不是在讨论茶叶。"],
    rationale="茶=约谈的固化隐喻+价格隐喻暗示风险，普通讨论解释权重低但未完全排除，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

# ═══ D1 反讽 (target: ~12) ═══

records.append(sample(
    text="赢麻了，这次真的赢麻了",
    risk_level="medium", encoding_primary="D1_反讽",

    literal=["表面重复庆祝'赢了'。"],
    encoding=["'赢麻了'是简中互联网最著名的反讽句式之一。", "D1：字面庆祝实际在讽刺。"],
    context_analysis=["弹幕常见句式，在非竞技类视频中出现时反讽概率极高。"],
    supporting=["'赢麻了'在简中已成为标准反讽句式，脱离竞技语境的中奖或胜利几乎都是反讽。"],
    counter=["体育比赛、电竞等竞技场景下'赢麻了'可能是真心庆祝。", "但脱离竞技语境时此解释不成立。"],
    rationale="高度固化的反讽句式，但脱离具体视频语境时无法确定在讽刺什么——可能讽刺比赛结果也可能讽刺社会事件。判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="我们这里治安越来越好了，街上每隔一百米就有一个摄像头",
    risk_level="medium", encoding_primary="D1_反讽",

    literal=["表面称赞治安好因为摄像头多。"],
    encoding=["用'治安好'和'摄像头密度'的反差进行反讽。", "D1：实际在暗示监控过度而非治安真正改善。"],
    context_analysis=["这种'治安好因摄像头多'的表达在简中已是常见D1句式。"],
    supporting=["'每隔一百米就有一个摄像头'的量化描述指向监控密度而非治安。", "句式结构是经典的'正面包装+负面暗示'。"],
    counter=["确实有用户真心认为摄像头多=治安好。", "但这种'每隔一百米'的夸张表述降低了真心赞美的可能性。"],
    rationale="有编码痕迹和反讽结构，但脱离具体事件，普通人对摄像头态度也确实存在分歧，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="这个政策太棒了，希望全国各地都推广，一个都别落下",
    risk_level="medium", encoding_primary="D1_反讽",

    literal=["表面支持某个政策全国推广。"],
    encoding=["'一个都别落下'暴露了反讽意图——真心支持通常不会加这么重的强调。", "D1反讽：用过度热情包装真实反对态度。"],
    context_analysis=["无法确定具体指哪个政策，但句式本身有反讽信号。"],
    supporting=["'希望全国各地都推广'这种全量推广的强调在真心支持中不常见。", "'一个都别落下'的用力过猛感。"],
    counter=["确实有人真心支持政策并希望全国推广。", "脱离具体政策内容无法判断。"],
    rationale="句式有反讽信号但不够强，脱离具体政策可能只是真心支持者，判medium。",
    ambiguity="medium", evidence_strength="weak",
))

records.append(sample(
    text="这个电影太好看啦，我看了三遍才睡着（狗头）",
    risk_level="none", encoding_primary="none",

    literal=["调侃电影无聊到让自己三次睡着。"],
    encoding=["使用（狗头）标记表明这是玩笑/阴阳怪气。", "但目标是电影质量而非政治风险。"],
    context_analysis=["娱乐内容讨论，完全无政治风险。"],
    supporting=["存在阴阳怪气表达但针对的是电影质量。"],
    counter=["纯娱乐调侃。", "（狗头）明确标记了玩笑性质。", "不存在政治或社会风险映射。"],
    rationale="纯文娱讨论，阴阳怪气对象是电影，完全无风险。适合作为D1类别的hard negative，训练模型区分政治反讽和娱乐反讽。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

records.append(sample(
    text="太感动了，看得我热泪盈眶，恨不得现在就回去种地",
    risk_level="none", encoding_primary="none",

    literal=["被某个内容感动到想回乡种地。"],
    encoding=["'回去种地'在特定语境下有政治含义，但此处是情绪化观影反应。"],
    context_analysis=["影视评论语境。'热泪盈眶'+'回去种地'组合在观影反应中是常见夸张表达。"],
    supporting=["出现'回去种地'可能被联想为某些政治隐喻。"],
    counter=["完整语境是影视内容的情感反应。", "'热泪盈眶'和夸张修辞是观影常态。", "没有任何政治映射的信号。"],
    rationale="影视情感反应，'回去种地'在此是夸张修辞而非政治隐喻。hard negative：训练模型不要在娱乐语境下过度联想。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

# ═══ D2 隐喻 (target: ~10) ═══

records.append(sample(
    text="方向盘打得太猛，车上的人已经开始晕了",
    risk_level="high", encoding_primary="D2_隐喻",

    literal=["描述开车太猛导致乘客晕车。"],
    encoding=["D2隐喻：'方向盘'=政策方向，'打得太猛'=政策转向过快，'车上的人晕了'=民众感到不适。"],
    context_analysis=["'方向盘'+'晕了'组合在政治隐喻中高度固化，不需要额外上下文。"],
    supporting=["简中互联网政治隐喻中，'开车/方向盘/刹车/乘客'有高度固定的映射关系。", "'已经开始晕了'映射政策的负面影响已经开始显现。"],
    counter=["也可能是真的在说开车经历。", "但这种高度完整的映射组合使普通解释权重极低。"],
    rationale="高度完整的政治隐喻组合，映射关系固定，普通解释可能性极低，判high。",
    ambiguity="low", evidence_strength="strong",
))

records.append(sample(
    text="车开得太快有点怕，希望司机能看看路",
    risk_level="medium", encoding_primary="D2_隐喻",

    literal=["表达对车速过快的担忧。"],
    encoding=["D2隐喻可能：开车=政策推行速度。", "但文本自然度高于纯编码，可能是真开车评论。"],
    context_analysis=["如果是驾校或赛车视频下的评论，纯字面。", "如果出现在政治讨论视频下，隐喻权重上升。"],
    supporting=["'开太快'+'看看路'在中文互联网可解读为对政策推进速度的隐喻。"],
    counter=["驾校视频、赛车视频、日常分享下的真开车评论非常常见。", "没有其他政治信号词。"],
    rationale="有D2隐喻可能但普通开车讨论概率更高，无上下文时判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="这游戏更新后越来越卡了，优化跟倒车似的",
    risk_level="low", encoding_primary="D2_隐喻",

    literal=["抱怨游戏更新后性能下降。"],
    encoding=["'倒车'在政治隐喻中有特定含义，但此处完整游戏讨论语境指向纯游戏吐槽。"],
    context_analysis=["完整的游戏讨论语境：更新、卡顿、优化。"],
    supporting=["出现'倒车'这个词可能触发政治隐喻联想。"],
    counter=["游戏性能用'倒车'形容退步是游戏圈常见表达。", "完整游戏语境没有政治信号。"],
    rationale="游戏性能吐槽中使用'倒车'是正常表达，hard negative帮助模型区分语境。",
    ambiguity="low", evidence_strength="weak", hard_negative=True,
))

records.append(sample(
    text="刹车已经踩死了，但车还在往前滑",
    risk_level="high", encoding_primary="D2_隐喻",

    literal=["描述刹车失效的紧急情况。"],
    encoding=["D2隐喻高度固化：刹车=政策纠偏，踩死刹车但车还在滑=纠偏措施无效。", "是简中政治隐喻中最常见的意象之一。"],
    context_analysis=["'刹车踩死'+'车还往前滑'的完整叙事映射特定政治判断，无需外部上下文。"],
    supporting=["该隐喻组合高度固化，映射方向明确。", "'踩死'的强化和'还在滑'的无力感构成完整政治叙事。"],
    counter=["极低概率是真在描述打滑的驾驶经历。", "但叙事完整性和细节选择使普通驾驶分享的可能性很低。"],
    rationale="高度固化的政治隐喻，完整的'刹车失效'叙事几乎没有普通解释空间，判high。",
    ambiguity="low", evidence_strength="strong",
))

# ═══ D3 借代 (target: ~8) ═══

records.append(sample(
    text="眼镜哥又上新闻了，这次说了不少实在话",
    risk_level="medium", encoding_primary="D3_借代",

    literal=["评论某个戴眼镜的公众人物上新闻说话很实在。"],
    encoding=["'眼镜哥'在简中互联网是特定公众人物的固定外号型借代。", "D3：用外貌特征借代具体人物。"],
    context_analysis=["B站弹幕/评论中讨论公众人物时'眼镜哥'指向明确。"],
    supporting=["'眼镜哥'在B站已固化为特定人物的代称。", "'说了不少实在话'暗示该人物言论触及敏感话题。"],
    counter=["理论上'眼镜哥'可以是任何戴眼镜的男性公众人物。", "但B站弹幕文化中该外号的指向性很强。"],
    rationale="固定外号借代+敏感言论暗示，指向较明确但不100%确定，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="包子铺最近生意特别好，每天排队排到马路对面",
    risk_level="low", encoding_primary="D3_借代",

    literal=["美食探店分享包子铺火爆。"],
    encoding=["'包子'在特定互联网语境下有借代含义，但此处的完整美食叙事没有编码意图。"],
    context_analysis=["小红书探店语境，排队、生意好都是真实美食分享信号。"],
    supporting=["仅'包子'一词可能被联想。"],
    counter=["完整的美食探店叙事真实自然。", "'排队排到马路对面'是美食笔记常见表达。", "没有任何政治影射的叙事信号。"],
    rationale="纯美食分享，仅词面可能触发误判。重要hard negative。",
    ambiguity="low", evidence_strength="weak", hard_negative=True,
))

records.append(sample(
    text="这个赛季的农夫山泉不好打",
    risk_level="low", encoding_primary="D3_借代",

    literal=["吐槽某游戏中'农夫山泉'角色/装备/关卡难度高。"],
    encoding=["游戏用语，编码意图无。但词语可能被误读。"],
    context_analysis=["游戏讨论语境明确：'赛季'+'不好打'。"],
    supporting=["词面有'农夫'和'山泉'。"],
    counter=["明显的游戏讨论语境。", "'赛季'+'不好打'明确指向游戏。"],
    rationale="游戏用语，hard negative训练模型识别游戏语境。",
    ambiguity="low", evidence_strength="weak", hard_negative=True,
))

# ═══ A2 拼音/首字母缩写 (target: ~6) ═══

records.append(sample(
    text="隔壁群已经没了，因为有人说了不该说的zhengzhi话题",
    risk_level="medium", encoding_primary="A2_拼音/首字母缩写",

    literal=["通知某个群因政治话题被封。"],
    encoding=["使用拼音'zhengzhi'而非汉字'政治'，是有意识的规避行为。", "A2拼音规避。"],
    context_analysis=["'群已经没了'提供了平台审查语境。"],
    supporting=["用拼音替代汉字是明显的规避行为。", "'不该说的'确认了话题敏感意识。"],
    counter=["也可能是打字习惯或输入法问题。", "但加上'不该说的'降低了无心之失的权重。"],
    rationale="拼音规避行为明显，但因话题内容不详，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="现在网上一提到SH，大家都知道在说哪",
    risk_level="medium", encoding_primary="A2_拼音/首字母缩写",

    literal=["讨论网友用SH代指某地。"],
    encoding=["SH在特定时期和语境下已固化为上海的拼音缩写代指，关联特定事件。"],
    context_analysis=["'大家都知道在说哪'确认了共同体认知。"],
    supporting=["特定时期的SH+共识确认信号。"],
    counter=["SH可以单纯指上海，城市简称用拼音首字母很正常。"],
    rationale="有编码可能但也可以是正常城市缩写，视语境而定，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

# ═══ E1 平台黑话 (target: ~8) ═══

records.append(sample(
    text="这个视频估计活不过今晚，多看几遍吧",
    risk_level="medium", encoding_primary="E1_平台黑话",

    literal=["预测视频很快会被删除，建议多看几遍。"],
    encoding=["E1：B站用户对'视频活不过xx'有共识理解——指视频因敏感内容将被平台下架。"],
    context_analysis=["B站弹幕、评论区常见此类表达。"],
    supporting=["'活不过今晚'是B站对视频被删的经典预测句式。", "'多看几遍吧'暗示内容稀缺且有价值。"],
    counter=["也可以指up主会自己删视频或视频因版权下架。", "不知道视频具体内容。"],
    rationale="E1平台黑话明确，但不知视频内容（版权还是政治），判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="画风突变那一下我直接好家伙",
    risk_level="none", encoding_primary="none",

    literal=["对视频内容的突然转折感到惊讶。"],
    encoding=["'画风突变'和'好家伙'都是B站日常弹幕用语，无编码意图。"],
    context_analysis=["纯视频内容反应，B站弹幕常规表达。"],
    supporting=["没有任何风险信号。"],
    counter=["完全正常的弹幕反应。", "B站日常用语。"],
    rationale="纯日常弹幕，无任何风险。hard negative帮助模型不要过度敏感于'画风突变'等词。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

# ═══ E2 时间节点触发 (target: ~6) ═══

records.append(sample(
    text="又到了每年的这个时候，懂的都懂",
    risk_level="high", encoding_primary="E2_时间节点触发",
    encoding_secondary=["E1_平台黑话"],

    literal=["暗示某个周期性时间点的到来。"],
    encoding=["E2+E1组合：'又到了'时间节点触发+'懂的都懂'平台黑话确认编码意图。"],
    context_analysis=["不需要外部上下文——'又到了每年这个时候'+'懂的都懂'的组合本身就是强编码。"],
    supporting=["两个固定编码信号叠加。", "在非节日期间出现时指向明确。"],
    counter=["传统节日（春节、中秋等）也可能使用类似表达。", "但对这些传统节日人们不会说'懂的都懂'——这暗示了信息的隐蔽性。"],
    rationale="双重编码信号，'懂的都懂'排除普通节日解释，判high。",
    ambiguity="low", evidence_strength="strong",
))

records.append(sample(
    text="春天来了，万物复苏，又到了动物们……的季节",
    risk_level="none", encoding_primary="none",

    literal=["玩赵忠祥《动物世界》经典配音梗。"],
    encoding=["这是B站赵忠祥动物世界配音梗的日常玩梗，无任何编码意图。"],
    context_analysis=["赵忠祥配音梗在B站属于经典meme，与政治风险无关。"],
    supporting=["'又到了'出现但组合的是经典配音梗。"],
    counter=["B站日常meme。", "完整语境指向赵忠祥配音梗而非政治隐喻。"],
    rationale="B站经典配音梗，'又到了'在此是无害的meme触发器。hard negative帮助模型区分E2时间节点与日常玩梗。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

# ═══ E3 话题/热点触发 (target: ~8) ═══

records.append(sample(
    text="刚看了那个新闻发布会，主持人的表情管理值得学习",
    risk_level="medium", encoding_primary="E3_话题/热点触发",
    encoding_secondary=["D1_反讽"],

    literal=["夸赞某新闻发布会主持人的表情管理。"],
    encoding=["E3+反讽：对新闻发布会的'表情管理'评论实际在暗示发言内容有问题。", "结合热点新闻发布会的讨论暗示。"],
    context_analysis=["需要知道是哪个发布会才能判断具体指涉。"],
    supporting=["'表情管理'在此语境中是委婉批评——暗示主持人在面对尴尬提问时需要控制表情。"],
    counter=["真的可以是夸奖主持人专业。", "如果发布会本身无争议事件，纯欣赏主持人是合理的。"],
    rationale="有E3热点触发可能，但'表情管理'评论可以在任何发布会上出现，无上下文判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="热搜又被撤了，截图存证吧",
    risk_level="medium", encoding_primary="E3_话题/热点触发",

    literal=["指出某话题热搜被移除，建议截图保存。"],
    encoding=["E3：讨论热搜撤除行为暗示话题敏感。", "'存证'表明意识到内容可能被进一步删除。"],
    context_analysis=["微博用户对热搜撤除有共识理解。"],
    supporting=["'热搜被撤'是微博常见的敏感话题讨论信号。", "'存证'确认了内容的对抗性。"],
    counter=["也可能是明星负面新闻、企业公关撤热搜，不一定是政治内容。", "撤热搜的原因很多。"],
    rationale="热搜撤除讨论暗示内容敏感，但撤热搜的原因多样，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

# ═══ F 组合编码 (target: ~8) ═══

records.append(sample(
    text="这个不能说太细，只能说：禾兑 氵去 女子 女子",
    risk_level="high", encoding_primary="F_组合编码",
    encoding_secondary=["B1_拆字", "E1_平台黑话"],

    literal=["声称不能说太细，然后发了一段拆字。"],
    encoding=["B1拆字：'禾兑'=税，'氵去'=法，'女子 女子'=好好。", "F+B1+E1：拆字规避+不能说太细的元评论。"],
    context_analysis=["'不能说太细'是强烈的编码确认信号。"],
    supporting=["拆字+自我审查确认信号，编码意图明确。"],
    counter=["可能是加密开玩笑，具体内容未知。"],
    rationale="拆字规避+编码确认信号，意图明确但还原内容有难度，判high。",
    ambiguity="low", evidence_strength="strong",
))

records.append(sample(
    text="天气真好，阳光明媚，乌云都散了",
    risk_level="none", encoding_primary="none",

    literal=["描述天气好。"],
    encoding=["'乌云散了'在某些语境下是政治隐喻，但此处作为天气描述自然完整。"],
    context_analysis=["纯天气描述，没有任何编码信号。"],
    supporting=["如果有上下文支持，'乌云散了'可能有隐喻含义。"],
    counter=["完整的天气描述，日常生活分享。", "没有上下文支持政治隐喻解读。"],
    rationale="纯天气分享。hard negative：训练模型不要一见'乌云'就联想。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

# ═══ More hard negatives (各类关键词撞车) ═══

records.append(sample(
    text="我今天在厨房切菜，差点切到手，血的教训啊",
    risk_level="none", encoding_primary="none",

    literal=["分享厨房切菜的小意外。"],
    encoding=["无编码。'血'和'教训'都是字面意思。"],
    context_analysis=["生活分享，厨房安全提醒。"],
    supporting=["没有任何风险信号。"],
    counter=["纯生活分享。", "'血的教训'是常用成语，此处字面使用。"],
    rationale="纯生活分享。hard negative：防止模型因'血的教训'而误判。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

records.append(sample(
    text="强烈推荐这个历史纪录片，讲的是明代政治制度演变",
    risk_level="none", encoding_primary="none",

    literal=["推荐关于明代政治制度的纪录片。"],
    encoding=["无编码。正常纪录片推荐。"],
    context_analysis=["B站知识区常见内容推荐。"],
    supporting=["有'政治'和'明代'——两个可能触发关键词系统的词。"],
    counter=["纯粹的历史纪录片推荐。", "没有影射现实的任何信号。", "B站知识区正常生态。"],
    rationale="正常历史纪录片推荐。重要的hard negative：训练模型识别正常历史讨论。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

records.append(sample(
    text="这个up主每次更新我都要投两个币，太良心了",
    risk_level="none", encoding_primary="none",

    literal=["表达对up主的支持。"],
    encoding=["无编码。B站日常互动。"],
    context_analysis=["B站投币文化。"],
    supporting=["没有任何风险信号。"],
    counter=["纯B站日常互动。"],
    rationale="纯日常。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

records.append(sample(
    text="微信又更新了，每次更新都占更多内存",
    risk_level="none", encoding_primary="none",

    literal=["抱怨微信占用内存。"],
    encoding=["无编码。日常软件吐槽。"],
    context_analysis=["日常科技讨论。"],
    supporting=["没有任何风险信号。"],
    counter=["纯软件吐槽。"],
    rationale="纯日常吐槽。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

# ═══ More HIGH samples across categories ═══

records.append(sample(
    text="西边的风有点大，吹得人站不稳",
    risk_level="medium", encoding_primary="D2_隐喻",

    literal=["描述刮大风。"],
    encoding=["D2隐喻可能：'西边的风'暗指来自西方的影响/思潮。", "但作为天气吐槽也非常正常。"],
    context_analysis=["如果是日常天气分享，normal。", "如果出现在政治讨论中，隐喻权重上升。"],
    supporting=["'西边的风'在特定讨论中有隐喻历史。"],
    counter=["纯天气吐槽在微博上极其常见。", "没有其他政治信号支持隐喻解读。"],
    rationale="有D2可能但天气吐槽概率更高，无上下文判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(sample(
    text="这届年轻人不好管了",
    risk_level="low", encoding_primary="none",

    literal=["感慨年轻一代不好管理。"],
    encoding=["可能是正常社会观察。但有微弱政治联想可能。"],
    context_analysis=["无上下文。这类感慨可出现在任何话题下。"],
    supporting=["有微弱的'不服管理'政治隐射可能。"],
    counter=["企业管理、家庭教育等场景下完全正常。", "是常见的中年人感慨。"],
    rationale="大概率是普通社会观察，判low而非none主要因为有微弱编码可能。适合做边界hard negative。",
    ambiguity="high", evidence_strength="weak", hard_negative=True,
))

records.append(sample(
    text="今晚的月亮真圆啊，就是有点红",
    risk_level="low", encoding_primary="C4_典故/物品/符号借用",

    literal=["描述今晚的月亮又圆又红。"],
    encoding=["'红月亮'在特定语境下有政治符号含义。", "但此处是正常天文现象描述。"],
    context_analysis=["月食期间'红月亮'是常见分享主题。"],
    supporting=["'红'+'月亮'可被解读为符号借用。"],
    counter=["天文现象。", "没有编码信号。"],
    rationale="天文分享的hard negative。",
    ambiguity="high", evidence_strength="weak", hard_negative=True,
))

records.append(sample(
    text="兔子急了也会咬人的，别逼太紧",
    risk_level="low", encoding_primary="C4_典故/物品/符号借用",

    literal=["俗语引用：温和的人被逼急了也会反抗。"],
    encoding=["'兔子'在特定互联网语境下可代表某些符号含义。", "但此处是完整俗语使用。"],
    context_analysis=["俗语使用场景广泛。"],
    supporting=["仅'兔子'一词可被联想。"],
    counter=["完整俗语使用。", "'兔子急了也咬人'是日常俗语。"],
    rationale="俗语使用而非编码。hard negative。",
    ambiguity="high", evidence_strength="weak", hard_negative=True,
))

# ── write ─────────────────────────────────────────────────────────
output_path = ROOT / "data" / "raw" / "batch1_natural_replacements.jsonl"
output_path.parent.mkdir(parents=True, exist_ok=True)
with output_path.open("w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n")

print(f"Wrote {len(records)} samples to {output_path}")

# Quick stats
from collections import Counter
risk = Counter(r["risk_level"] for r in records)
enc = Counter(r["encoding_primary"] for r in records)
hn = sum(r["hard_negative"] for r in records)
print(f"Risk: {dict(risk)}")
print(f"Hard negative: {hn}")
print(f"Top encodings: {enc.most_common(10)}")
