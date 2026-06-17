#!/usr/bin/env python3
"""
batch15: P1 风险域缺口补全 (~95 samples)
覆盖 9 个严重不足的审核类目：
新疆/西藏/法轮功/文革历史运动/香港/赌博/毒品/枪支/假证

要求：真实网络口吻、编码多元、正反证据齐全、口吻多变
"""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
COMBINED = PROJECT_ROOT / "data" / "processed" / "combined_candidates.jsonl"

# ── helpers ────────────────────────────────────────────────────────────

def base_reasoning(literal, encoding, context, supporting, counter, rationale):
    return {
        "literal_analysis": literal,
        "encoding_analysis": encoding,
        "context_analysis": context,
        "supporting_evidence": supporting,
        "counter_evidence": counter,
        "final_rationale": rationale,
    }


def sample(idx, text, risk, enc, **kw):
    """Factory for a consistent sample dict."""
    return {
        "id": f"{idx:06d}",
        "source_type": "synthetic",
        "platform": kw.get("platform", "text_comment"),
        "text": text,
        "context": kw.get("context", {}),
        "risk_level": risk,
        "encoding_primary": enc,
        "encoding_secondary": kw.get("encoding_secondary", []),
        "needs_context": kw.get("needs_context", False),
        "ambiguity": kw.get("ambiguity", "low"),
        "evidence_strength": kw.get("evidence_strength", "moderate"),
        "hard_negative": kw.get("hard_negative", False),
        "freshness": kw.get("freshness", "stable"),
        "target_known": kw.get("target_known", True),
        "reasoning": kw["reasoning"],
        "quality_status": "draft",
        "review_notes": kw.get("review_notes", "source=batch15_p1_gaps"),
    }


# ── batch15 samples ────────────────────────────────────────────────────

S = []  # sample list

# ╔══════════════════════════════════════════════════════════════════════════
# ║ 1. 新疆问题   (14 条) — 突厥/东突/分裂叙事 + 隐晦表达 + hard_negative
# ╚══════════════════════════════════════════════════════════════════════════

S.append(sample(1386,
    "东突厥斯坦从来就不属于中国，维吾尔人的土地被强占了七十年，现在还要被「再教育」、被种族灭绝，全世界都看到了",
    "high", "literal_keyword",
    platform="text_comment",
    evidence_strength="strong",
    encoding_secondary=["C2_历史事件影射"],
    reasoning=base_reasoning(
        ["文本明确使用'东突厥斯坦'（分离主义框架下的新疆称谓）并指控'种族灭绝'、'再教育'和'土地被强占'。"],
        ["'东突厥斯坦'是分离主义话术的核心编码——将新疆称为独立政治实体；'再教育'是对职业技能教育培训中心的污名化；'种族灭绝'是境外反华叙事的核心词汇。这些已不构成编码规避，而是直接使用分离主义框架中的核心术语。"],
        ["典型的分离主义政治传播话术，面向国际舆论场。将职业技能教育培训歪曲为'再教育营'、将人口发展歪曲为'种族灭绝'。"],
        ["使用'东突厥斯坦'分裂主义框架称谓", "指控'种族灭绝'——境外反华核心叙事", "把职业技能教育培训污名化为'再教育'", "声称'土地被强占七十年'否认中国主权"],
        ["新疆是中国不可分割的领土，职业技能教育培训中心旨在反恐去极端化，与所谓'再教育营'有本质区别", "维吾尔族人口持续增长，'种族灭绝'指控在人口数据上自相矛盾"],
        "直接使用分离主义政治框架并传播反华核心叙事，高确定性，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=新疆; encoding_target=literal_keyword"
))

S.append(sample(1387,
    "听说最近西域那边又在'加强管理'了，啧啧，懂的都懂，某些人种就是不配拥有自由吧。反正我早就说了，当年就该学美国人",
    "high", "D1_反讽",
    platform="text_comment",
    evidence_strength="strong",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["表面说'西域那边在加强管理'，用'懂的都懂'引导读者自行脑补负面含义。'某些人种'暗指维吾尔族，'学美国人'暗示美国对原住民的历史处理方式。"],
        ["D1_反讽：用'加强管理'表面中性词暗指压迫，'懂的都懂'是典型反讽触发器。'学美国人'是高度危险的编码——指涉美国屠杀印第安人、建立保留地等种族灭绝历史，映射到新疆。D2_隐喻：'西域'是历史地名借用，在当代语境中作为新疆的代称。"],
        ["这种'懂的都懂'式的隐晦表达在中外社交平台上广泛用于绕过审核，实际传递的是分裂主义叙事和种族仇恨。"],
        ["'懂得都懂'诱导读者填充负面含义", "'某些人种'的种族主义框架", "'学美国人'指涉种族灭绝历史，极其危险"],
        ["'西域'也可能只是历史/文学讨论中使用的地理称谓", "没有明确提及任何具体事件或政策"],
        "通过反讽和隐喻构建多层隐含意义，'学美国人'的映射是种族灭绝的极端危险暗示，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=新疆; encoding_target=D1_反讽+D2_隐喻"
))

S.append(sample(1388,
    "维吾尔人不是中国人，我们有自己的语言自己的文化自己的历史，东伊运才是真正的代表",
    "high", "literal_keyword",
    platform="text_comment",
    evidence_strength="strong",
    encoding_secondary=["C5_概念替换"],
    reasoning=base_reasoning(
        ["文本明确否认维吾尔人的中国人身份，声称'我们有自己的语言文化和历史'，并正面引用了被联合国认定为恐怖组织的'东伊运'。"],
        ["'东伊运'（东突厥斯坦伊斯兰运动）是被联合国安理会列名的恐怖组织，文本将其美化为'真正代表'是对恐怖主义的宣扬。'维吾尔人不是中国人'是典型的分裂主义框架。"],
        ["典型的分裂主义+恐怖主义美化话术，属于最严重的风险表达。"],
        ["明确否认维吾尔族中国人的身份", "正面引用并美化联合国列名的恐怖组织", "构建'我们vs他们'的对抗框架"],
        ["维吾尔族确实拥有独特的语言和文化传统，这是中华文化多元性的体现而非分离的依据"],
        "明确的分裂主义表达+恐怖组织美化，属于最高风险等级，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=新疆; encoding_target=literal_keyword"
))

S.append(sample(1389,
    "他们说去学技术，去了就回不来了。我一个表姐的邻居就是这样，家里人哭死了，都不知道人在哪里，也不敢问",
    "medium", "D2_隐喻",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="medium",
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["文本描述了一个'去学技术→回不来→家人不知下落→不敢问'的叙事。'学技术'、'不敢问'是关键词。"],
        ["'去学技术'可能是对职业技能教育培训中心的歪曲性指代——将其污蔑为'关押'场所。'不敢问'暗示恐惧氛围。表达采用了'我一个表姐的邻居'这类道听途说的叙述方式，增加了传播力但降低了可验证性。"],
        ["这种'传闻体'叙事在境外社交媒体上常见，利用模糊来源制造可信度，但本质上仍是针对新疆反恐政策的污名化传播。"],
        ["'学技术→回不来'的叙事结构与反华势力对教育培训中心的歪曲一致", "'不敢问'构建恐惧氛围"],
        ["所述内容为'表姐的邻居'第三手传闻，完全无法验证","职业技能教育培训中心学员结业后回归社会是公开可查的事实","'学技术'在中国语境中也可能指合法的职业技能培训"],
        "利用传闻体叙事污名化职业技能教育培训政策，证据来源模糊但传达了明确的负面框架，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=新疆; encoding_target=D2_隐喻"
))

S.append(sample(1390,
    "西安这边的维族小伙其实人都挺好的，烤肉做的是一绝。但我听说西边那些地方现在管得特别严，手机都要查，他们过的什么日子啊，想想就难受",
    "medium", "D1_反讽",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="medium",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["表面先肯定'维族小伙人好、烤肉好吃'，然后转折'但...西边管得严、手机要查'，以同情口吻传递负面信息。"],
        ["表面先建立善意人设再传递负面判断，是常见的话术。'西边那些地方'指新疆，'管得特别严、手机都要查'暗示警察国家式的压迫。'想想就难受'以情感共鸣的方式加固偏见。D1_反讽：先赞扬后贬低形成反差。"],
        ["通过先扬后抑的话术结构传播对新疆维稳政策的负面描述。"],
        ["先扬后抑的结构递进负面信息", "'手机都要查'暗示极端监控", "以'难受'情绪触发共情"],
        ["正文前半句确认维族生活正常（烤肉、做朋友），本身就削弱了后半句的'压迫'叙事", "'手机被查'可能在说特定安保场合（如大型活动安检）被歪曲为常态化"],
        "话术结构精致但实质仍是传播对新疆政策的不实描述，有一定隐蔽性，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=新疆; encoding_target=D1_反讽"
))

S.append(sample(1391,
    "突厥民族的历史比中华文明还要悠久，为什么我们要接受一个外来文明的统治？学学蒙古人不好吗",
    "medium", "C2_历史事件影射",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["文本以'突厥民族历史'为框架，将中华文明定性为'外来文明'，并用'学学蒙古人'影射独立/分裂。"],
        ["C2_历史事件影射：'学学蒙古人'可能指蒙古从中国分离的历史（外蒙古独立），作为对新疆分裂的影射。'突厥民族历史比中华文明悠久'构建历史优越论来为分裂主义提供'历史依据'。D2_隐喻：'外来统治'是殖民主义框架的投射。"],
        ["构建泛突厥主义的历史叙事来支持分裂主张，但表达相对学术化而非直接煽动。"],
        ["'学学蒙古人'明确指向分裂/独立", "把中华文明定性为'外来'构建对抗框架"],
        ["突厥语族历史和中华文明都是人类文明的组成部分，不存在'谁比谁悠久'的对抗关系", "表达较为学术化，可能只是历史讨论"],
        "以历史叙事为包装传播泛突厥主义分裂思想，学术化表面下有明确的分裂影射，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=新疆; encoding_target=C2_历史事件影射"
))

S.append(sample(1392,
    "今天在B站看了个新疆舞视频，评论区全在刷'集中营''灭绝'，我就想问刷这些的人你们真的去过新疆吗？我去年刚去过喀什，人家巴扎上卖馕的大爷笑呵呵的，日子过得好着呢",
    "low", "literal_keyword",
    platform="bilibili",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["驳斥了评论区刷'集中营''灭绝'的行为，并以亲身经历（去喀什、巴扎、大爷笑呵呵）作为反证。"],
        ["文字本身是在反驳谣言而非传播谣言，提及敏感词'集中营''灭绝'是引用他人言论作为驳斥对象。整体态度是正面的。"],
        ["用户在评论区驳斥他人传播的不实信息。"],
        ["以亲身经历作为反驳依据", "指出造谣者'没去过新疆'"],
        ["文本中出现了'集中营'和'灭绝'这两个敏感词，虽然是以引用驳斥的方式出现", "如果上下文缺失，可能被误判为支持这些叙事"],
        "正面驳斥谣言并以亲历为证，但因含有敏感词引用，在上下文缺失时可能被误读，判为 low。"
    ),
    review_notes="source=batch15_p1_gaps; gap=新疆; encoding_target=literal_keyword; needs_context_warning"
))

S.append(sample(1393,
    "xc有些人总拿mlsl说事，我寻思着56个民族都是一家人啊，非要搞对立有意思吗",
    "low", "A2_拼音/首字母缩写",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="high",
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["文本用'xc'（新疆）、'mlsl'（穆斯林）的拼音首字母缩写讨论民族话题，但表达了民族团结的正面立场。"],
        ["A2_拼音：使用拼音首字母缩写可能暗示用户在规避关键词检测，但实际内容却是反驳对立、支持民族团结。缩写可能只是模仿他人的表达习惯以便融入讨论。"],
        ["表达民族团结立场，反驳试图制造对立的言论。"],
        ["核心态度是'56个民族一家人'反对对立"],
        ["使用缩写可能是规避意图的残留信号","在没有上下文时，缩写本身携带不确定性"],
        "缩写形式有规避嫌疑但核心内容是民族团结正面表达，判为 low。"
    ),
    review_notes="source=batch15_p1_gaps; gap=新疆; encoding_target=A2_拼音"
))

S.append(sample(1394,
    "这次去新疆玩了十天，乌鲁木齐→吐鲁番→喀纳斯→喀什，大盘鸡拌面烤包子吃到撑，新疆人民太热情了，景区门票还给打了五折，良心推荐！",
    "none", "none",
    platform="redbook",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["新疆旅游攻略分享——行程路线、美食推荐、价格信息，充满正面体验。"],
        ["没有任何编码机制。这是完全正常的旅游分享内容，'新疆'在这里只是地理名词。"],
        ["正常的旅游消费分享，属于小红书/马蜂窝等平台的典型内容。"],
        ["行程细节具体可验证", "正面情绪（太热情、良心推荐）"],
        ["无任何风险信号"],
        "正常的新疆旅游分享，判为 none（hard negative：新疆≠分裂主义，正常的正面新疆内容很常见）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=新疆; hard_negative"
))

S.append(sample(1395,
    "我们学校来了几个新疆交换生，昨天一起打篮球，有个维吾尔族小伙三分球十投八中，太猛了。晚自习还教了他们几句维语，亚克西姆赛斯是'你好'的意思嘿嘿",
    "none", "none",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享与新疆维吾尔族同学的日常校园互动——打篮球、学维语，充满生活气息。"],
        ["没有任何编码机制。'维吾尔族'作为民族身份自然出现而非规避。文本场景是正常的校园社交。"],
        ["正常的校园生活分享。"],
        ["多元文化交流的正面表达", "日常生活场景的细节增加了可信度"],
        ["'维吾尔族'在某些语境中可能与敏感话题关联，但此处完全是正常语境"],
        "正常的校园生活分享，展现民族交流，判为 none（hard negative：维吾尔族≠敏感话题）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=新疆; hard_negative"
))

S.append(sample(1396,
    "大盘鸡其实每个地方做法不一样，沙湾的偏辣，乌鲁木齐的偏咸，柴窝堡的辣子鸡才是真神。话说新疆面粉做拉条子真的绝了，筋道！",
    "none", "none",
    platform="redbook",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["纯粹的新疆美食讨论——大盘鸡、辣子鸡、拉条子的做法和口味对比。"],
        ["没有任何编码。'新疆'在这里是菜系的产地标识，完全在烹饪语境中使用。"],
        ["正常的美食/烹饪讨论。"],
        ["讨论内容局限于烹饪技术和口味偏好"],
        ["无任何风险信号"],
        "纯粹的新疆美食讨论，判为 none（hard negative：食物讨论≠政治表达）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=新疆; hard_negative"
))

S.append(sample(1397,
    "伊犁的薰衣草田真的太美了，比普罗旺斯还震撼。牧民骑马经过的时候那个画面简直电影级别的",
    "none", "none",
    platform="redbook",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享伊犁薰衣草田和牧民的旅游美景体验。"],
        ["没有任何编码机制。'伊犁'作为地理名词，完全在旅游审美语境中。"],
        ["正常的旅游美景分享。"],
        ["内容单纯聚焦于旅游审美和自然景观"],
        ["无任何风险信号"],
        "正常的伊犁旅游美景分享，判为 none（hard negative：新疆地理名词≠政治风险）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=新疆; hard_negative"
))

S.append(sample(1398,
    "看到有些公众号又在写'xj问题'了，点进去一看全是道听途说，就没一个真的去过xj的。我从小在阿克苏长大，我们那儿各族邻居互相拜年几十年了",
    "low", "C5_概念替换",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="medium",
    encoding_secondary=["D1_反讽"],
    reasoning=base_reasoning(
        ["用'xj'作为'新疆'的缩写讨论相关话题，但立场是反驳谣言并以自身经历（阿克苏长大、邻里互相拜年）作证。"],
        ["C5_概念替换：用'xj'（拼音首字母缩写）替代'新疆'，可能是为了规避关键词或模仿相关讨论的写法。D1_反讽：对公众号的不实信息表示轻蔑，讽刺其为'道听途说'。"],
        ["在涉及新疆议题的讨论中，以亲身经历反驳不实信息。"],
        ["以阿克苏长大的亲历者为证", "指出'没一个真的去过'揭示信息源不可靠", "各族邻里拜年体现民族团结"],
        ["使用'xj'缩写有一定规避意味", "整体处于敏感话题的讨论语境中"],
        "使用缩写讨论新疆话题但立场是反驳不实信息、支持民族团结，判为 low。"
    ),
    review_notes="source=batch15_p1_gaps; gap=新疆; encoding_target=C5_概念替换"
))

# ╔══════════════════════════════════════════════════════════════════════════
# ║ 2. 西藏问题   (12 条) — 图博/达赖/分裂叙事 + 硬负样本
# ╚══════════════════════════════════════════════════════════════════════════

S.append(sample(1399,
    "Tibet was never part of China, it was an independent nation invaded in 1951. The Dalai Lama is the true spiritual leader of Tibetan people. Free Tibet！",
    "high", "literal_keyword",
    platform="text_comment",
    evidence_strength="strong",
    encoding_secondary=["A4_外语谐音/跨语言音译"],
    reasoning=base_reasoning(
        ["英文明文否认西藏自古以来属于中国，称1951年为'侵略'，将达赖喇嘛称为'真正的精神领袖'，并以'Free Tibet'收尾。"],
        ["英文表达本身就是一种编码规避——绕过中文审核机制。'Tibet'在英文语境中常被反华势力用作政治符号而非地理名称。'Free Tibet'是国际上最具代表性的藏独口号。"],
        ["典型的英文藏独话术，目标受众是国际社会。"],
        ["否认中国对西藏的主权", "'Free Tibet'是明确的藏独分裂口号", "使用英文规避中文审核"],
        ["西藏自古以来就是中国不可分割的领土，1951年西藏和平解放是历史进程的必然"],
        "使用英文表达明确的分裂主义立场和藏独口号，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=西藏; encoding_target=literal_keyword+A4"
))

S.append(sample(1400,
    "图博人的文化正在被系统性消灭。汉语教育取代了藏语学校，汉族移民淹没了拉萨，藏传佛教被改造成了旅游景点。1949年到现在，我们都看到了",
    "high", "D2_隐喻",
    platform="text_comment",
    evidence_strength="strong",
    encoding_secondary=["C5_概念替换"],
    reasoning=base_reasoning(
        ["用'图博'（Tibet的音译替代）指代西藏，指控'文化灭绝'、'汉族移民淹没'、'宗教被旅游化'，声称1949年以来持续发生。"],
        ["'图博'是Tibet的音译形式，在中文语境中作为'西藏'的编码替代——规避直接使用'西藏'，同时也是藏独话语体系中的政治符号。C5_概念替换：用'图博'替换'西藏'来暗示一个独立政治实体的概念。'系统性消灭'、'淹没'等词汇构建受害者叙事。"],
        ["典型的'文化灭绝'叙事——国际反华势力攻击中国西藏政策的核心框架之一。"],
        ["'图博'作为政治符号区别于地理名称'西藏'", "指控'文化灭绝'是境外反华核心叙事", "1949年作为时间锚点隐含政权更替叙事"],
        ["中国政府高度重视藏族文化保护，藏语教育在全自治区得到保障", "西藏旅游发展促进了藏文化的传播而非消灭"],
        "用'图博'政治符号构建'文化灭绝'叙事，编码意图明确，指向性强，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=西藏; encoding_target=D2_隐喻+C5"
))

S.append(sample(1401,
    "你们知道吗，达赖喇嘛说的话其实都是有道理的。他只是想要自治又不是独立，为什么就不能坐下来谈呢？非要给人扣帽子",
    "high", "D1_反讽",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["表面是'理性讨论'的语调，说达赖喇嘛'只是要自治不是独立'、'为什么不能坐下来谈'、'给人扣帽子'。"],
        ["D1_反讽：伪装成中立理性，实则美化达赖喇嘛的分裂主义本质。事实上，达赖集团从未放弃过分裂主张，所谓'自治'本质上是变相独立。'非要给人扣帽子'暗指中国政府不宽容，是受害者叙事的构建。"],
        ["典型的美化分裂分子的'理性中立'话术——通过降低冲突强度（'只是自治不是独立'）来使分裂主张显得合理。"],
        ["达赖喇嘛是分裂主义政治符号而非单纯的宗教人物", "'自治'话术是变相独立", "将反对分裂歪曲为'扣帽子'"],
        ["表面语调理性温和，没有直接使用攻击性语言"],
        "以'理性中立'为包装美化和辩护分裂主义，隐蔽性强但实质危险，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=西藏; encoding_target=D1_反讽"
))

S.append(sample(1402,
    "有人把雪山狮子的头像挂在朋友圈背景，说是信仰自由。我就想问一下，同样的行为换成一个明确的政治符号你还会说是自由吗？自由是有边界的",
    "medium", "C4_典故/物品/符号借用",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=["D1_反讽"],
    reasoning=base_reasoning(
        ["讨论'雪山狮子'作为头像的政治含义，指出'信仰自由'不能成为使用政治符号的挡箭牌。"],
        ["C4_符号借用：'雪山狮子'（雪山狮子旗的意象）是藏独分裂主义的标志性符号。文本以自由讨论的方式提醒该符号的政治含义。D1_反讽：对'信仰自由'说辞的质疑。"],
        ["反分裂意识的表达，但讨论的是符号识别问题。"],
        ["指出了'雪山狮子'作为政治符号的本质", "区分了宗教信仰自由与政治表达"],
        ["本身立场是反对分裂符号的使用，虽然提及了分裂符号"],
        "讨论藏独政治符号的识别问题，立场是反对分裂，但话题本身处于敏感区，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=西藏; encoding_target=C4_符号借用"
))

S.append(sample(1403,
    "每年三月份总有一些账号开始密集发藏区的内容，镜头永远只拍破房子和老人，然后配一些'传统文化消失'的解说。这种套路看了十年了，换个花样行不行",
    "medium", "E2_时间节点触发",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=["D1_反讽"],
    reasoning=base_reasoning(
        ["批评每年3月（西藏相关时间节点）有账号发布刻意选择负面角度的藏区内容，声称'传统文化消失'。"],
        ["E2_时间节点触发：'每年三月份'指涉与西藏相关的政治敏感期（1959年3月西藏叛乱/达赖出逃），一些势力会在此时集中发布负面内容。文本以反讽方式揭穿这些账号的操作套路。"],
        ["识别和揭露境外势力在敏感时间节点进行的舆论操作。"],
        ["指出了特定时间节点的规律性操作", "揭示了'选择性拍摄'的信息操纵手法"],
        ["文本本身是揭露不实信息的正面行为"],
        "揭露信息操纵的正面表达，但讨论的话题本身是涉藏敏感领域，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=西藏; encoding_target=E2_时间节点"
))

S.append(sample(1404,
    "这几年藏区发展真的快，我老家昌都那边通了高速，网络也好了，以前去趟拉萨要两天现在几个小时",
    "none", "none",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享藏区基础设施改善的亲身经历——昌都高速通车、网络改善、交通时间缩短。"],
        ["完全没有编码。'藏区'作为地理名词在正常的经济发展语境中使用。"],
        ["正常的藏区发展体验分享。"],
        ["具体的发展数据（高速、网络、时间缩短）可验证"],
        ["无任何风险信号"],
        "正常的藏区发展体验分享，判为 none（hard negative：藏区≠政治敏感，正常发展讨论很常见）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=西藏; hard_negative"
))

S.append(sample(1405,
    "有人问藏传佛教和汉传佛教的区别，我说最简单的：藏传有活佛转世系统，汉传没有。然后就被举报了，理由是'涉及敏感宗教话题'，我真的谢",
    "none", "none",
    platform="zhihu",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=["D1_反讽"],
    reasoning=base_reasoning(
        ["分享回答宗教知识问题后被误举报的经历，吐槽被过度审核。"],
        ["D1_反讽：对被误举报的吐槽（'我真的谢'是反语）。讨论的是客观的宗教知识（活佛转世vs汉传佛教），是正常的学术/宗教常识交流。"],
        ["正常的知识问答场景中的误审核吐槽。"],
        ["讨论的是公开的宗教常识", "客观对比而非价值判断"],
        ["'活佛转世'话题可能触发敏感词的机械审核"],
        "正常的宗教知识讨论被误伤后的吐槽，判为 none（hard negative：宗教常识讨论≠政治敏感）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=西藏; hard_negative"
))

S.append(sample(1406,
    "下个月准备去拉萨，看了好多攻略说第一天别洗澡别剧烈运动怕高反。有没有去过的老哥分享一下经验，红景天到底管不管用？",
    "none", "none",
    platform="redbook",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["纯粹的旅行准备咨询——高反预防、红景天效果、拉萨旅游tips。"],
        ["没有任何编码。'拉萨'、'高反'完全在旅游语境中使用。"],
        ["正常的旅游咨询。"],
        ["问题完全围绕旅行实用信息"],
        ["无任何风险信号"],
        "正常的拉萨旅游咨询，判为 none（hard negative：西藏地名≠政治表达）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=西藏; hard_negative"
))

S.append(sample(1407,
    "唐卡真的太震撼了，一笔一划画好几个月，那个专注力我直接跪了。朋友说学唐卡要先学三年线描，难怪那么精细",
    "none", "none",
    platform="redbook",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["对藏族唐卡艺术的欣赏和工艺讨论。"],
        ["没有任何编码。'唐卡'作为藏族传统艺术形式，在正常的美术/手工艺语境中讨论。"],
        ["正常的文化艺术欣赏。"],
        ["讨论局限于美术工艺层面", "正面积极的审美体验"],
        ["无任何风险信号"],
        "正常的藏族文化艺术讨论，判为 none（hard negative：藏族文化≠政治敏感）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=西藏; hard_negative"
))

S.append(sample(1408,
    "我外公是五几年的进藏干部，后来就留在拉萨了。小时候听他讲修路的故事，说那时候真是苦，但也是真的自豪。现在我每年还回去看他那些老战友的子女",
    "none", "none",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享家族中进藏干部的正面记忆——修路、艰苦、自豪、与藏区建立的代际联系。"],
        ["没有任何编码。'进藏干部'是历史事实陈述，语境是家族史中的正面记忆。"],
        ["正常的家族历史回忆。"],
        ["正面情感（自豪）", "代际联系体现了深度融入"],
        ["无任何风险信号"],
        "正常的家族历史回忆，展现建设者的正面贡献，判为 none（hard negative：进藏干部的历史叙事≠政治敏感）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=西藏; hard_negative"
))

S.append(sample(1409,
    "有博主发了藏羚羊的保护现状，评论里就有人开始发散'可可西里无人区其实是...'你懂的。保护动物的视频下面也要搞这些，真的烦",
    "medium", "E3_互动/热点触发",
    platform="bilibili",
    evidence_strength="moderate",
    ambiguity="medium",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["吐槽在可可西里/藏羚羊保护视频下，有人借题发挥散播政治言论。"],
        ["E3_互动/热点触发：评论者利用保护动物的视频作为入口，将话题引向政治敏感方向。'你懂的'是典型的不言自明的暗示手法。'可可西里无人区其实是...'省略的内容暗示与西藏相关的政治叙事。"],
        ["用户识别并吐槽他人在正常内容下插入政治敏感言论的行为。"],
        ["识别了他人的政治敏感触发行为", "保护动物的立场是正面的"],
        ["文本本身是揭露而非传播", "省略了敏感内容的具体表述"],
        "揭发他人在正常内容下传播敏感言论的行为，本身立场正确但因涉及敏感话题的讨论，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=西藏; encoding_target=E3_互动触发"
))

S.append(sample(1410,
    "网上说那些有的没的，我都不信。反正我认识的藏族朋友都挺好的，该上班上班该刷抖音刷抖音，哪有那么多事",
    "low", "C4_典故/物品/符号借用",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="medium",
    encoding_secondary=["D1_反讽"],
    reasoning=base_reasoning(
        ["以轻松随意的口吻 ('该上班上班该刷抖音刷抖音') 反驳网上关于藏区的传言，以及日常接触的藏族朋友的正常生活作为论据。"],
        ["C4：'有的没的'是对网上关于西藏问题的各类传言的模糊化指代。D1_反讽：以'哪有那么多事'的口吻表达对这些传言的轻蔑。"],
        ["用日常观察反驳不实传言。"],
        ["基于实际接触的论据", "日常生活的正常性作为反驳"],
        ["'有的没的'措辞模糊，不清楚具体指什么", "表达过于随意可能被视为不认真对待问题"],
        "以日常接触反驳不实传言，正面立场但表达模糊，判为 low。"
    ),
    review_notes="source=batch15_p1_gaps; gap=西藏; encoding_target=C4+反讽"
))

# ╔══════════════════════════════════════════════════════════════════════════
# ║ 3. 法轮功   (10 条) — 传教话术/政治影射 + hard_negative
# ╚══════════════════════════════════════════════════════════════════════════

S.append(sample(1411,
    "法轮大法是宇宙至高真理，李洪志师父是转世佛陀。退党保命！三退人数已超过三亿，历史将证明一切！共产党气数已尽",
    "high", "literal_keyword",
    platform="text_comment",
    evidence_strength="strong",
    encoding_secondary=["C4_典故/物品/符号借用"],
    reasoning=base_reasoning(
        ["直接宣扬法轮功教义（'法轮大法'、'李洪志师父'、'转世佛陀'），并结合'退党保命'、'三退'、'共产党气数已尽'等明确的攻击性政治表达。"],
        ["'法伦大法'、'李洪志师父'是法轮功组织的核心术语。'三退'（退党退团退队）是法轮功组织的标准政治煽动话术。'三亿'是法轮功组织的虚假宣传数字。这已超出编码范畴，是直接使用该组织的标志性话术。"],
        ["法轮功组织的标准政治煽动模板。"],
        ["使用法轮功组织的标志性话术", "结合政治攻击和宗教包装", "'三退'是明确的组织性政治煽动"],
        ["无，表述明确不具有其他解释可能"],
        "法轮功组织的标准宣传话术+政治煽动，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=法轮功; encoding_target=literal_keyword"
))

S.append(sample(1412,
    "九p的最新一集讲得真透彻，尤其是讲那个组织的历史那一段，看了才知道原来这么多事情我们都被蒙在鼓里。想看的朋友私信我，我发真相资料给你",
    "high", "D2_隐喻",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["E1_平台黑话"],
    reasoning=base_reasoning(
        ["'九p'是'九评'的规避缩写——法轮功标志性反共材料《九评共产党》。'真相资料'是法轮功组织对其宣传材料的自称。'私信我发资料'是典型的组织性传播行为。"],
        ["D2_隐喻：'九p'用拼音首字母替代敏感词，'那个组织'模糊指代中共。'真相资料'是法轮功组织对反共宣传资料的内部称谓——对不知情者而言无害，对知情者而言是明确的signal。E1_平台黑话：'私信我'是在公开评论区进行地下传播的常见操作。"],
        ["公开评论区中的暗号式传播和组织动员。"],
        ["'九p'→'九评'的直接映射", "'真相资料'是法轮功内部语", "'私信我发资料'是组织传播行为"],
        ["对不熟悉该组织的人而言，'九p'和'真相资料'可能不具有明确含义"],
        "通过暗语和内部称谓进行法轮功反共材料的组织性传播，编码明确，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=法轮功; encoding_target=D2_隐喻+E1"
))

S.append(sample(1413,
    "真shan忍，这是最朴素的三个字，但也是最有力量的三个字。你可以不信，但请你不要诋毁那些信的人。每个人的信仰都是自由的不是吗",
    "high", "D1_反讽",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["B4_符号/空格/Unicode 干扰"],
    reasoning=base_reasoning(
        ["'真shan忍'中拆分了'善'字（shan=善的拼音），规避完整写出法轮功的核心口号'真善忍'。以'信仰自由'为旗号包装该组织的宣传。"],
        ["B4_符号干扰：'真shan忍'用拼音替换中间的'善'字——这是最常见的中文平台敏感词规避手段之一。D1_反讽：表面讨论'信仰自由'的普世价值，实际是为法轮功组织张目——该组织并非单纯的宗教团体而是被依法取缔的邪教组织。'每个人的信仰都是自由的'是故意混淆邪教与合法宗教的边界。"],
        ["利用'信仰自由'的普世话语为邪教组织提供掩护。"],
        ["'真shan忍'规避了完整写出法轮功核心口号", "'信仰自由'为邪教组织提供了话语掩护"],
        ["脱离法轮功语境，'真善忍'三个字本身可以是普通的道德倡导"],
        "以规避形式传播法轮功核心口号并以'信仰自由'为掩护，结合编码与话语策略，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=法轮功; encoding_target=D1+B4"
))

S.append(sample(1414,
    "我奶奶最近不知道从哪看了一些东西，天天说什么'天灭中共''退党保平安'，还非要拉我去公园参加什么'集体炼功'。我查了一下这个组织的资料，怎么劝她都不听。求助怎么办",
    "medium", "literal_keyword",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["描述家人被疑似法轮功组织拉拢的情况——'天灭中共'、'退党保平安'、'集体炼功'等术语，并寻求帮助。"],
        ["虽然提及了法轮功相关话术，但这是受害家属的求助——文本的态度是反对和忧虑的。'天灭中共'是法轮功的标志性口号，'集体炼功'是法轮功活动的伪装。"],
        ["作为被邪教影响的家庭的求助表达。"],
        ["以寻求帮助为目的", "对相关言论持反对态度", "识别了该组织的危害性"],
        ["在求助中复述了相关口号"],
        "家属反邪教求助，虽然提及了非法组织的话术，但立场是反对的，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=法轮功; encoding_target=literal_keyword; 家属求助"
))

S.append(sample(1415,
    "发现单位楼下有人发册子，封面写的养生保健，翻开全是讲某功法的，还说能治癌症。我直接拍了照片发给社区民警了，大家遇到这种事记得举报",
    "medium", "C5_概念替换",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["描述遇到以'养生保健'为掩护的法轮功传教行为，并已向警方举报。"],
        ["C5_概念替换：'某功法'以模糊化方式指代法轮功，'养生保健'是该组织常见的传教掩护方式——表面讲养生实际宣传教义。文本的立场是揭露和举报。"],
        ["公民发现邪教传教行为并举报的经验分享。"],
        ["识别了'养生保健'的伪装", "采取了正确的举报行动", "呼吁他人效仿"],
        ["提及了邪教相关内容但以举报为目的"],
        "反邪教的正面经验分享，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=法轮功; encoding_target=C5_概念替换"
))

S.append(sample(1416,
    "今天路过公园看见一群大爷大妈在练功，不知道是太极拳还是什么功法，反正动作挺慢的。看着挺有意思的，我也想去学学养生",
    "none", "none",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["描述在公园看到老年人练功的日常场景，产生了学习养生的兴趣。"],
        ["没有任何编码。'功法'、'养生'、'太极拳'都是在正常的健康养生语境中使用。公园老年人晨练是中国城市的日常景观。"],
        ["正常的日常生活观察。"],
        ["'太极拳'是正常的中国传统武术/健身方式", "'养生'是大众健康话题", "场景是正常的公园晨练"],
        ["'功法'在非常特定的语境中可能与某些组织有关联，但此处完全是正常的晨练场景"],
        "正常的公园晨练观察和养生兴趣，判为 none（hard negative：太极/养生≠邪教功法）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=法轮功; hard_negative"
))

S.append(sample(1417,
    "网上在传的那个气功视频，说练了能开天眼什么的，我笑了。气功就是个健身方法而已，跟广播体操差不多，搞得神乎其神的不就是想骗钱吗",
    "none", "none",
    platform="bilibili",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=["D1_反讽"],
    reasoning=base_reasoning(
        ["批评网上吹嘘气功能'开天眼'的视频，指出气功只是健身方法，神化气功是为了骗钱。"],
        ["D1_反讽：用'我笑了'表达对神化气功者的讽刺。文本立场是反迷信、反骗钱、理性看待气功。"],
        ["反迷信的理性讨论。"],
        ["明确指出气功是健身方法", "揭露'开天眼'等话术是为了骗钱"],
        ["在讨论气功真伪时提及了'开天眼'等夸大宣传内容"],
        "理性看待气功的反迷信讨论，判为 none（hard negative：批评伪气功≠讨论邪教）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=法轮功; hard_negative"
))

S.append(sample(1418,
    "神韵的票谁买谁傻逼，花几百块钱看一群人在台上扭秧歌，朋友圈还有人安利说'这是被禁的艺术'，被禁不是因为它是艺术，是因为背后那点事，懂吧",
    "medium", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=["D1_反讽"],
    reasoning=base_reasoning(
        ["批评朋友推荐'神韵'演出——指出神韵不是被禁的艺术而是与法轮功组织有关。"],
        ["E1_平台黑话：'神韵'（神韵演出）是法轮功组织运营的演出团体，经常以'被禁的中国艺术'为包装进行海外演出。'背后那点事'是模糊化指代法轮功背景。'懂吧'是暗示不言自明信息的常见手法。"],
        ["揭露神韵演出的法轮功背景。"],
        ["识别了'被禁的艺术'包装话术", "指出禁止原因是背后的邪教组织而非艺术本身"],
        ["在揭露时提及了法轮功相关组织的详细名称"],
        "揭露法轮功相关组织的伪装，虽提及敏感组织名称但立场正确，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=法轮功; encoding_target=E1_平台黑话"
))

S.append(sample(1419,
    "有个海外博主天天发'苏家屯集中营''活摘人体器官'之类的东西，说得跟真的一样。我就查了一下——没有任何国际组织、任何国家的官方文件证实这些说法。纯纯的谣言制造机",
    "low", "literal_keyword",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    encoding_secondary=["D1_反讽"],
    reasoning=base_reasoning(
        ["揭露某个海外博主传播'苏家屯集中营''活摘器官'等法轮功组织的标志性谣言，以事实核查方式驳斥。"],
        ["'苏家屯'、'活摘器官'是法轮功组织炮制的经典谣言。文本以事实核查方式驳斥，指出没有任何官方证实。立场是反谣言的。"],
        ["反谣言的事实核查表达。"],
        ["以无官方证实作为反驳", "明确指出是'谣言'"],
        ["在驳斥中复述了谣言的完整内容"],
        "反谣言揭露，但因复述了谣言细节，在上下文缺失时可能被误解，判为 low。"
    ),
    review_notes="source=batch15_p1_gaps; gap=法轮功; encoding_target=literal_keyword"
))

S.append(sample(1420,
    "看到油管上有个频道一直在讲'退dang''三tui'，评论区跟邪教现场一样。想说这些人是不是活在平行世界，中国十几亿人要是真像他们说的那样早完了",
    "low", "A2_拼音/首字母缩写",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="medium",
    encoding_secondary=["D1_反讽"],
    reasoning=base_reasoning(
        ["用拼音缩写描述法轮功组织的宣传内容（'退dang'='退党'，'三tui'='三退'），并以讽刺口吻反驳。"],
        ["A2_拼音：使用拼音缩写替代敏感词，可能是为了安全讨论——既让读者理解所指又避免直接写完整敏感词。D1_反讽：以'平行世界'、'早完了'的戏谑口吻驳斥法轮功的不实宣传。"],
        ["在公共讨论中驳斥法轮功组织的谣言。"],
        ["以常识逻辑反驳（十几亿人早完了）", "识别了邪教式评论氛围"],
        ["使用了拼音缩写规避形式"],
        "以反讽和缩写形式驳斥法轮功谣言，立场正面但使用了规避写法，判为 low。"
    ),
    review_notes="source=batch15_p1_gaps; gap=法轮功; encoding_target=A2_拼音"
))

# ╔══════════════════════════════════════════════════════════════════════════
# ║ 4. 文革/历史运动   (10 条) — 文革/大跃进/四人帮影射 + hard_negative
# ╚══════════════════════════════════════════════════════════════════════════

S.append(sample(1421,
    "现在的中国和wg时期有什么区别？领袖崇拜、言论控制、政治运动一波接一波。当年红卫兵打砸抢，现在网上那些小粉红跟那时候的红卫兵有什么两样？",
    "high", "C2_历史事件影射",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["C1_历史人物类比"],
    reasoning=base_reasoning(
        ["用'wg'（文革）作为类比框架，将当代中国与文革时期划等号，具体比对'领袖崇拜'、'言论控制'、'政治运动'，并将爱国网民（'小粉红'）类比为'红卫兵'。"],
        ["C2_历史事件影射：将文革这一历史事件框架投射到当代中国，构建'历史重演'的叙事。C1_历史人物类比：将当代爱国网民类比为文革时期的红卫兵，暗示他们是非理性的暴力执行者。'wg'是'文革'的拼音缩写规避。"],
        ["典型的历史类比攻击——通过将当代中国与文革划等号来否定现实。这种叙事在境外中文圈非常普遍。"],
        ["系统性地将当代中国与文革进行类比", "将爱国网民俗名化为红卫兵", "构建'历史循环'的否定叙事"],
        ["当代中国与文革时期在政治制度、经济发展、社会秩序等各方面有本质不同，类比不成立"],
        "利用历史类比全面否定当代中国的政治叙事，映射明确、攻击性强，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=文革; encoding_target=C2+C1"
))

S.append(sample(1422,
    "五八年大yue进饿死三千万，这账是不是也该算一算？搞浮夸风的人后来都高升了，那些饿死的农民呢？历史书上这一页是空白的",
    "high", "C2_历史事件影射",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=["A2_拼音/首字母缩写"],
    reasoning=base_reasoning(
        ["用'大yue进'（大跃进的拼音规避）讨论三年困难时期，声称饿死人数、追责问题、历史书写问题。"],
        ["A2_拼音：'yue进'是'跃进'的拼音规避。C2_历史事件影射：将三年困难时期高度简化/歪曲为'饿死三千万'——在引用未经证实的数据同时，以'历史书空白'暗示官方掩盖。"],
        ["利用历史事件进行政治攻击的典型表达。'历史书空白'、'账算一算'暗示当代政权应对历史负责。"],
        ["利用特定历史时期进行政治攻击", "使用未经证实的数据", "'历史书空白'暗示掩盖叙事"],
        ["三年困难时期是多因素造成的复杂历史事件，简单归因不准确"],
        "利用历史事件构建攻击性叙事，数据未经证实且指向明确的政治攻击，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=大跃进; encoding_target=C2+A2"
))

S.append(sample(1423,
    "四人帮打倒了，但四人帮的精神遗产还在。看今天的官场就知道，该有的毛病一个没少。不说了，说多了号没了",
    "high", "D1_反讽",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["C1_历史人物类比"],
    reasoning=base_reasoning(
        ["声称'四人帮的精神遗产还在'，将当代官场的问题归因于四人帮的精神延续。"],
        ["C1_历史人物类比：将四人帮的政治特征投射到当代官场，暗示腐败、专断等问题源于体制。D1_反讽：'说多了号没了'以自嘲口吻表达害怕被审查，同时暗示'我说的是真的但不敢说'。"],
        ["以历史人物类比进行制度性批评。"],
        ["将当代官场问题归因于四人帮的体制性延续", "'说多了号没了'制造'敢怒不敢言'的氛围", "将历史负面人物的特征映射到当代"],
        ["反腐败斗争是当代中国的重要政治议程，与四人帮代表的历史阶段有本质区别"],
        "利用历史人物类比攻击现行体制，影射明确，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=文革; encoding_target=D1+C1"
))

S.append(sample(1424,
    "爷爷是六几年下乡的知青，他说那时候虽然苦，但年轻人之间特别单纯，没有现在这么卷。我听完不知道该怎么接话——他说的'苦'和'单纯'，到底是怀念还是什么",
    "medium", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="medium",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["分享祖父的知青经历——'苦但单纯'，并反思这种怀念心态的复杂性。"],
        ["E1_平台黑话：'卷'是当代网络用语（内卷）。D2_隐喻：通过代际对比（知青时代 vs 当代），暗示对当前社会氛围的某种复杂感受。文本的核心是对代际经验差异的反思而非政治攻击。"],
        ["家庭内部的代际对话与反思。"],
        ["'不知道该怎么接话'表明文本并非在直接做政治判断", "反思的是个人感受而非制度"],
        ["提及'下乡知青'可能会被误关联到政治敏感", "对'单纯'的怀念可能被误解为美化那个时代"],
        "代际经验反思，对历史持复杂情感但未做明确政治判断，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=文革; encoding_target=E1_平台黑话"
))

S.append(sample(1425,
    "很多人喜欢用'那个十年'指代一段历史，但我想说那十年里也不是每个人都参与了疯狂，很多普通人只是在努力活下去。历史从来不是非黑即白的",
    "medium", "D2_隐喻",
    platform="zhihu",
    evidence_strength="weak",
    ambiguity="high",
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["以'那个十年'模糊指代文革时期，讨论历史的复杂性——指出并非所有人都参与了'疯狂'，普通人只是在'活下去'。"],
        ["D2_隐喻：'那个十年'是中文互联网上对文革的常见委婉指代，避免直接提及该历史时期。文本试图以非黑白二元的方式讨论历史——强调普通人的视角。"],
        ["在公共讨论中以相对温和的方式承认历史复杂性。"],
        ["强调历史的复杂性而非简单定性", "突出普通人视角"],
        ["对文革的讨论在中国的网络环境中本身就是一个高度敏感的话题", "'那个十年'的模糊指代暗示用户认为直接提及该时期是不被允许的"],
        "以相对温和的方式讨论复杂历史，没有做出明确的政治攻击，但话题本身处于敏感领域，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=文革; encoding_target=D2_隐喻"
))

S.append(sample(1426,
    "昨天看了一个关于liushaoqi的纪录片片段，感觉很复杂。历史人物的评价真的会随时代而变，但作为后人我们应该有更全面的视角去看",
    "medium", "C1_历史人物类比",
    platform="zhihu",
    evidence_strength="moderate",
    ambiguity="medium",
    encoding_secondary=["A2_拼音/首字母缩写"],
    reasoning=base_reasoning(
        ["用拼音'liushaoqi'指代历史人物，表达了对历史评价随时间变迁的复杂感受。"],
        ["A2_拼音：用拼音替代名字以规避可能的敏感词检测。C1_历史人物类比：讨论历史人物的评价变迁——这种讨论如果没有延伸为对现实的攻击，本身属于正常的历史反思范畴。但'评价随时代而变'可以被解读为对当代历史叙述的质疑。"],
        ["对历史人物评价的反思性讨论。"],
        ["表达的是'应该有更全面的视角'的历史研究态度"],
        ["使用拼音规避形式暗示了自我审查的存在", "'评价随时代而变'可被解读为暗讽"],
        "以学术化的口吻讨论历史人物评价的复杂性，使用拼音规避，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=文革; encoding_target=C1+A2"
))

S.append(sample(1427,
    "说实话我不懂为什么有些人对那个年代有那么深的执念，我也读过一些回忆录，是好是坏各有说法。我觉得历史讨论就该就事论事，而不是拿它当武器",
    "low", "C5_概念替换",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="medium",
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["以'那个年代'模糊指代文革时期，主张历史讨论应该'就事论事'而非'当武器'。"],
        ["C5_概念替换：用'那个年代'替代直接提及具体历史时期。文本的核心立场是呼吁理性的历史讨论，区分'就事论事'和'当武器'。"],
        ["呼吁理性看待历史的表达。"],
        ["主张历史讨论应理性客观", "反对将历史政治工具化"],
        ["'那个年代'的模糊化表述本身可能导致不确定性"],
        "呼吁理性讨论历史的表达，立场温和中立，判为 low。"
    ),
    review_notes="source=batch15_p1_gaps; gap=文革; encoding_target=C5_概念替换"
))

S.append(sample(1428,
    "在看一本关于中国60年代社会史的书，作者是北大的教授。书里引用了很多一手档案，数据很扎实。历史研究就该这样，用证据说话而不是用情绪说话",
    "none", "none",
    platform="zhihu",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享阅读学术性的中国60年代社会史书籍的正面体验。"],
        ["没有任何编码。这是正常的学术阅读分享——讨论学术著作的资料来源、研究方法和学术价值。60年代作为一个历史时期出现在正常的学术讨论语境中。"],
        ["正常的学术阅读体验分享。"],
        ["强调学术著作的证据（一手档案、扎实数据）", "引用北大教授增加了学术性", "主张理性而非情绪化的研究方法"],
        ["60年代包含了文革等敏感历史时期，但文本将其作为学术研究对象而非政治工具"],
        "正常的学术阅读讨论，判为 none（hard negative：学术性历史讨论≠政治敏感）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=文革; hard_negative"
))

S.append(sample(1429,
    "《芙蓉镇》真的拍得太好了，谢晋导演那个年代敢拍这样的片子，了不起。姜文和刘晓庆的演技绝了，最后那个镜头我直接哭成狗",
    "none", "none",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享对电影《芙蓉镇》的观影感受——导演、演员、情感反应。"],
        ["没有任何编码。'芙蓉镇'是以文革为背景的经典电影，但它是一部合法的、获多项国际大奖的中国电影。讨论这部电影属于正常的文艺评论。"],
        ["正常的电影评论/观影分享。"],
        ["讨论的是合法的文艺作品", "赞美的是导演和演员的艺术表现", "情感反应（感动哭了）是正常的观影体验"],
        ["《芙蓉镇》以文革为背景，但它是公开上映的文艺作品而非政治工具"],
        "合法的文艺作品讨论，判为 none（hard negative：文艺作品评论≠政治敏感）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=文革; hard_negative"
))

S.append(sample(1430,
    "我们学校历史系开了一门'共和国史专题研究'，主讲老师讲得特别好。上次课讲的是'大跃进的经济决策过程'，从一手档案解读决策逻辑和后果，既客观又有深度",
    "none", "none",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享大学历史系课程——'共和国史专题研究'——的正面体验，具体描述了讲解大跃进经济决策的学术方法。"],
        ["没有任何编码。'大跃进'在这里是学术课程中的历史时期名称，讨论的是学术研究方法和一手档案——这是完全正常的高等教育内容。"],
        ["正常的大学课程体验分享。"],
        ["讨论的是学术研究方法而非政治判断", "大学历史系课程是完全合法的教学内容", "强调'客观'和'深度'的学术态度"],
        ["'大跃进'是敏感历史时期，但作为学术课程研究对象是完全正常的"],
        "正常的大学历史课程讨论，判为 none（hard negative：学术教育中的历史讨论≠政治敏感）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=文革; hard_negative"
))

# ╔══════════════════════════════════════════════════════════════════════════
# ║ 5. 香港问题   (13 条) — 反送中/黄蓝/粤语编码 + hard_negative
# ╚══════════════════════════════════════════════════════════════════════════

S.append(sample(1431,
    "光复香港，时代革命！五大诉求，缺一不可！香港人不是中国人，我们宁做英国狗也不做中国人，黑警必遭天谴！",
    "high", "literal_keyword",
    platform="text_comment",
    evidence_strength="strong",
    encoding_secondary=["E1_平台黑话"],
    reasoning=base_reasoning(
        ["直接使用香港黑暴期间的核心口号——'光复香港，时代革命'、'五大诉求，缺一不可'、'黑警必遭天谴'，并明确否认香港人是中国人。"],
        ["'光复香港，时代革命'是香港黑暴期间最核心的港独口号，已被定性为分裂国家的政治标语。'五大诉求，缺一不可'是黑暴期间的政治动员口号。'黑警'是对香港警察的侮辱性称呼。"],
        ["香港黑暴期间的核心政治标语和港独言论。"],
        ["多个香港黑暴标志性口号", "明确否认香港人中国人身份", "'宁做英国狗'是极端侮辱性的自我贬低和分裂表达"],
        ["无，表述明确没有其他解释可能"],
        "直接使用港独口号和分裂言论，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=香港; encoding_target=literal_keyword"
))

S.append(sample(1432,
    "今日出街见到成街都系黑衫，心谂：香港人嘅意志仲未死㗎！虽然唔可以好似以前咁大摇大摆行出来，但我哋知道边个系自己人。手足，坚持住！",
    "high", "A3_方言谐音",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["E1_平台黑话"],
    reasoning=base_reasoning(
        ["粤语文本：表达看到街上穿黑衣的人（黑暴象征）后的振奋，声称'香港人的意志未死'，以'手足'互称，鼓励坚持。"],
        ["A3_方言谐音（粤语）：使用粤语本身增加了一层编码——非粤语使用者可能无法理解，同时也强化了'香港本土'的身份认同。E1_平台黑话：'黑衫'是黑暴期间抗议者的标志性着装，'手足'（兄弟姐妹）是黑暴参与者之间的互相称呼，在特定社区中具有明确的政治含义。"],
        ["粤语编码的黑暴动员和政治表达。"],
        ["'黑衫'是黑暴的标志性视觉符号", "'手足'是黑暴内部称谓", "粤语强化了分离主义的身份政治"],
        ["粤语是香港的法定语言之一，使用粤语本身不构成风险"],
        "使用粤语进行黑暴相关的政治动员和身份认同构建，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=香港; encoding_target=A3_粤语+E1"
))

S.append(sample(1433,
    "2019年11月发生的事，全世界都看到了。愿荣光归香港，那些牺牲的年轻人不会被忘记。总有一天历史会还他们一个公道",
    "high", "D1_反讽",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["C2_历史事件影射"],
    reasoning=base_reasoning(
        ["提及2019年11月（香港黑暴高峰期）和'愿荣光归香港'（港独歌曲名），称黑暴参与者为'牺牲的年轻人'。"],
        ["'愿荣光归香港'是已被定性为港独歌曲的非法作品。'牺牲的年轻人'是对违法犯罪者的美化和哀悼。'历史会还给公道'暗示时间站在港独一边——是一种长期主义的政治叙事。"],
        ["美化黑暴、传播港独歌曲的政治表达。"],
        ["使用了被定性为非法的港独歌曲名", "将违法者美化为'牺牲者'", "构建'历史终将还公道'的长期叙事"],
        ["无，表述明确指向政治立场"],
        "美化黑暴和传播港独符号的政治表达，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=香港; encoding_target=D1+C2"
))

S.append(sample(1434,
    "我系土生土长香港人，国安法之后确实清净咗好多，以前成日惊出街遇到示威，而家终于可以安安稳稳过日子。但系我啲friend话我变咗蓝，好无奈",
    "medium", "D1_反讽",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="medium",
    encoding_secondary=["A3_方言谐音"],
    reasoning=base_reasoning(
        ["粤语表达：支持国安法带来的安定（'清净咗好多'、'安安稳稳过日子'），但表达被朋友标签为'蓝'（亲建制）的无奈。"],
        ["A3_方言谐音（粤语）：使用粤语表达。D1_反讽：'好无奈'表达了被二元对立撕裂的人际关系的复杂情感。'蓝'和'黄'是香港政治光谱的二分标签。文本的立场是务实而非政治的——'可以安安稳稳过日子'。"],
        ["香港普通市民在政治二元对立环境中的日常困境。"],
        ["支持国安法带来安定是正面表达", "表达了被标签化的无奈"],
        ["提及了'蓝/黄'的政治标签", "表达了香港社会撕裂的现状"],
        "支持社会安定但反映了香港社会撕裂的现状，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=香港; encoding_target=A3粤语+D1"
))

S.append(sample(1435,
    "香港以前是国际金融中心，现在呢？人才走了、外资跑了、自由没了。国安法一出，香港彻底变成了另一个内地城市。一个时代的终结",
    "medium", "D1_反讽",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["声称国安法导致香港人才外流、外资撤离、自由消失，香港变成了'另一个内地城市'、'一个时代的终结'。"],
        ["D1_反讽：'国际金融中心→另一个内地城市'的对比是典型的贬低叙事，将'内地城市'暗指为不如'国际金融中心'。'自由没了'是对国安法的歪曲——国安法针对的是危害国家安全的行为而非正当自由。"],
        ["对国安法和香港现状的负面评价叙事。"],
        ["构建了'国安法前=繁荣自由，国安法后=衰败'的二元对比"],
        ["国安法实施后香港经济数据保持稳定，营商环境和法治指数依然位居全球前列", "香港的独特地位和优势得到中央政府的充分保障"],
        "对国安法和香港现状的负面评价，虽有夸大但未到直接煽动分裂的程度，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=香港; encoding_target=D1+D2"
))

S.append(sample(1436,
    "蓝店定黄店自己分啦，不过我净系知道有啲铺头门口贴满晒文宣嗰啲，入去食嘢都觉得唔舒服。食餐饭都要分颜色，香港几时变成咁？",
    "medium", "A3_方言谐音",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="medium",
    encoding_secondary=["E1_平台黑话"],
    reasoning=base_reasoning(
        ["粤语表达：描述香港'蓝店/黄店'（按政治立场分类的商铺）现象，表达对吃饭都要分颜色的无奈。"],
        ["A3_粤语+E1_平台黑话：'蓝店/黄店'是香港独特的政治标签现象——商业被政治立场绑架。文本表达了对此现象的不满（'食餐饭都要分颜色，香港几时变成咁？'），立场是反对将政治渗透到日常生活中。"],
        ["香港市民对政治化日常生活的无奈表达。"],
        ["表达了对政治撕裂的厌倦", "'食餐饭都要分颜色'揭示了政治化的荒谬", "询问'几时变成咁'暗示现状不合理"],
        ["提及了蓝黄政治标签", "表达了香港社会现状的负面感受"],
        "对香港政治撕裂的无奈表达，虽涉及敏感政治标签但持批判性立场，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=香港; encoding_target=A3粤语+E1"
))

S.append(sample(1437,
    "有人喺tg群发咗条link，话系'香港最新情况'，打开一睇就系嗰啲嘢。即刻退出咗个群，而家呢啲群好危险，分分钟被人拉",
    "medium", "E3_互动/热点触发",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="medium",
    encoding_secondary=["A3_方言谐音"],
    reasoning=base_reasoning(
        ["粤语表达：描述在Telegram群中收到'香港最新情况'链接，识别为敏感内容后退出群组。'嗰啲嘢'（那些东西）和'分分钟被人拉'暗示了内容的违法风险。"],
        ["E3_互动/热点触发：'tg群'（Telegram群）是香港敏感内容传播的主要渠道。'香港最新情况'是常见的敏感内容包装。'嗰啲嘢'是粤语中常用的模糊化指代。文本立场是识别风险并退出。"],
        ["在Telegram中识别敏感内容后自我保护的表达。"],
        ["识别了Telegram传播的敏感内容", "采取了退出群组的自我保护行为", "认识到法律风险（'被人拉'）"],
        ["提及了Telegram和'香港情况'等敏感关联词"],
        "自我保护的风险识别表达，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=香港; encoding_target=E3+A3"
))

S.append(sample(1438,
    "连登上面成日有人话要'坚持抗争'，但系而家出post嘅人越来越少了，好多人移咗民就唔再出声。好现实，走得嘅就走，留低嘅就收声，所谓'手足'不过如此",
    "medium", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=["A3_方言谐音"],
    reasoning=base_reasoning(
        ["粤语表达：观察连登（LIHKG，香港知名讨论区）上的黑暴情绪变化——表态的人减少、移民后就沉默，讽刺'手足'（黑暴内部称谓）的虚情假意。"],
        ["E1_平台黑话：'连登'是香港最具影响力的网络讨论区之一，在黑暴期间是重要组织平台。'手足'的黑暴含义上文已分析。但文本的态度是讽刺性的——揭穿'手足情谊'的虚伪（'走得嘅就走，留低嘅就收声'）。"],
        ["对香港黑暴社区内部虚伪性的观察和讽刺。"],
        ["揭示了黑暴社区的人去楼空", "讽刺'手足'情谊的虛假"],
        ["提及了连登、手足等黑暴相关平台和术语"],
        "对黑暴社区的反思和讽刺，虽涉及敏感平台和术语但持批判立场，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=香港; encoding_target=E1+A3"
))

S.append(sample(1439,
    "看到朋友圈有人转'反送中'的旧文，感觉已经是上辈子的事了。现在香港该怎样怎样，日子还得过。历史留下什么不重要，重要的是往前走",
    "low", "C2_历史事件影射",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="medium",
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["提及看到朋友圈转发'反送中'旧文，表达了'已经是过去的事'、'日子还得过'、'往前走'的态度。"],
        ["C2_历史事件影射：'反送中'是2019年香港事件的触发点之一。文本的态度是淡化该事件的历史重要性——'上辈子的事了'、'历史留下什么不重要，重要的是往前走'。"],
        ["对过去事件的淡化态度。"],
        ["表达的是放下过去向前看", "把事件定位为'上辈子的事'表明不认同持续炒作"],
        ["提及了'反送中'事件"],
        "以淡化态度讨论香港历史事件，立场是向前看而非持续政治化，判为 low。"
    ),
    review_notes="source=batch15_p1_gaps; gap=香港; encoding_target=C2"
))

S.append(sample(1440,
    "琴日同friend去咗大澳，食咗超好味嘅虾酱蒸猪肉同埋茶果，仲见到中华白海豚！香港其实真系好靓，唔好成日净系睇新闻嗰啲负面嘢啦",
    "none", "none",
    platform="redbook",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["粤语分享大澳（香港离岛）一日游——美食、海豚、自然景观，呼吁大家不要只看负面新闻。"],
        ["没有任何编码。这是正常的香港本地旅游和美食分享。使用粤语是自然的本地语言表达。"],
        ["正常的本地旅游分享。"],
        ["内容完全围绕旅游和美食", "正面积极的情绪", "呼吁关注美好事物而非负面新闻"],
        ["'咪成日净系睇新闻嗰啲负面嘢'隐含了对媒体报道倾向的批评，但这是在旅游语境中的随口抱怨"],
        "正常的香港本地旅游分享，判为 none（hard negative：香港日常≠政治敏感）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=香港; hard_negative"
))

S.append(sample(1441,
    "香港迪士尼跟上海迪士尼怎么选？带娃去的话。港迪人少排队快但是园区小，上迪项目多但是排队排到怀疑人生。有去过的宝妈分享一下吗？",
    "none", "none",
    platform="redbook",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["亲子旅游咨询——香港迪士尼vs上海迪士尼的对比选择。"],
        ["没有任何编码。'香港'在这里作为旅游目的地出现，完全是正常的消费决策咨询。"],
        ["正常的亲子旅游咨询。"],
        ["内容完全围绕带娃旅游的实用信息"],
        ["无任何风险信号"],
        "正常的香港旅游咨询，判为 none（hard negative：香港旅游≠政治）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=香港; hard_negative"
))

S.append(sample(1442,
    "学紧粤拼，有冇人一齐？我系北方人但系觉得广东话好好听，尤其系啲歌词。最近单曲循环《喜帖街》，谢安琪把声太正啦",
    "none", "none",
    platform="redbook",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享学习粤语拼音的爱好——北方人觉得粤语好听、喜欢粤语歌曲。"],
        ["没有任何编码。这是正常的语言学习和音乐欣赏分享。使用粤语只是为了练习和展示。"],
        ["正常的语言学习/音乐欣赏分享。"],
        ["文化学习交流的正面表达", "跨地域文化欣赏"],
        ["无任何风险信号"],
        "正常的粤语学习分享，判为 none（hard negative：粤语学习/文化欣赏≠政治敏感）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=香港; hard_negative"
))

S.append(sample(1443,
    "茶餐厅文化真的是香港最伟大的发明，冻柠茶+菠萝油+沙爹牛肉面，30块钱吃出人生巅峰。北京开了好几家港式茶餐厅但总感觉少了那个味道",
    "none", "none",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享香港茶餐厅美食文化和个人体验。"],
        ["没有任何编码。这是纯粹的饮食文化分享。"],
        ["正常的美食文化讨论。"],
        ["内容完全局限于饮食文化"],
        ["无任何风险信号"],
        "正常的美食文化分享，判为 none（hard negative：茶餐厅文化≠政治敏感）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=香港; hard_negative"
))

# ╔══════════════════════════════════════════════════════════════════════════
# ║ 6. 网络赌博   (10 条) — 盘口/时时彩/棋牌伪装 + hard_negative
# ╚══════════════════════════════════════════════════════════════════════════

S.append(sample(1444,
    "英超曼城vs利物浦，曼城让半球，水位0.95，稳如老狗。要玩的兄弟抓紧上，今晚九点截止，私我拿地址，新用户首充送188",
    "high", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["literal_keyword"],
    reasoning=base_reasoning(
        ["以英超赛事为掩护进行博彩推广——'让半球'、'水位0.95'是专业的博彩术语，'私我拿地址'、'首充送188'明确引导投注。"],
        ["E1_平台黑话：'让半球'（亚洲盘口术语）、'水位0.95'（赔率术语）是博彩行业的专业技术语言。'稳如老狗'是赌圈用语。'私我拿地址'是博彩推广的标准操作——在公开平台引流到私密渠道。"],
        ["体育赛事伪装下的博彩推广和引流。"],
        ["专业的博彩术语（盘口、水位、让球）", "'私我拿地址'的引流操作", "'首充送188'的新用户诱导策略"],
        ["表面讨论的是正常的英超足球比赛"],
        "专业的博彩推广和引流操作，编码明确，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=赌博; encoding_target=E1_平台黑话"
))

S.append(sample(1445,
    "时.时.彩 计.划 稳.赚 每.日.收.入.5.0.0.起。跟.我.玩.的.都.发.了。加.Q.群.8.8.8.6.6.6.不.懂.的.私.聊.",
    "high", "B4_符号/空格/Unicode 干扰",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["E1_平台黑话"],
    reasoning=base_reasoning(
        ["用点号分割的方式规避关键词检测——'时.时.彩'（时时彩——非法网络彩票赌博）、'计.划.稳.赚'（引诱话术）、'加.Q.群'（引流到QQ群）。"],
        ["B4_符号干扰：通过在字符间插入句号来规避关键词过滤。E1_平台黑话：'时时彩'是非法网络彩票赌博的类型，'计划稳赚'是博彩推广的标准话术，'每日收入500起'是利益诱导。"],
        ["典型的规避式博彩广告。"],
        ["点号分割的规避意图明确", "'时时彩'是非法赌博类型", "'稳赚'和'每日500起'是虚假利益诱导", "QQ群引流操作"],
        ["对不熟悉博彩广告模式的人而言，可能看不明白这些断开的文字"],
        "典型的规避式博彩广告，多信号印证，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=赌博; encoding_target=B4+E1"
))

S.append(sample(1446,
    "六合彩特码三中三，内部消息包中！上一期中了50万，这一期跟我买，只要500一个号。不开玩笑，加微信liuhe****查看上期中奖截图",
    "high", "literal_keyword",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["E1_平台黑话"],
    reasoning=base_reasoning(
        ["'六合彩特码三中三'是地下六合彩赌博的术语，以'内部消息包中'和'上期中50万'为诱饵，引导加微信。"],
        ["地下六合彩（非法彩票赌博）广告。'特码'、'三中三'是六合彩赌博的专业术语。'内部消息'和'上期截图'是典型的虚假诱导话术。加微信逃避平台审核。"],
        ["非法六合彩赌博的推广广告。"],
        ["六合彩赌博的专业术语", "'内部消息包中'的虚假承诺", "加微信的引流操作", "'500一个号'的价格说明这是商业操作"],
        ["无，广告性质和赌博意图明确"],
        "明确的非法六合彩赌博广告，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=赌博; encoding_target=literal_keyword"
))

S.append(sample(1447,
    "最近压力大睡不着，朋友推了个台子给我，玩了一个月输了小两万。想戒但是总觉得下次能翻本，这种感觉太可怕了。有过来人吗，怎么走出来的",
    "medium", "D2_隐喻",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=["E1_平台黑话"],
    reasoning=base_reasoning(
        ["表达赌博成瘾者的困境——'台子'（赌博网站/平台）、输了近两万、'想戒但总觉得能翻本'的成瘾心理，并寻求帮助。"],
        ["D2_隐喻：'台子'是赌博平台的生动隐喻，如同赌场的台桌。'翻本'是赌博成瘾的核心心理陷阱——不断加注以挽回损失。文本的立场是求助性的——'有过来人吗，怎么走出来的'。"],
        ["赌博成瘾者的求助表达。"],
        ["成瘾的典型心理（总觉得能翻本）", "'输了小两万'表明实际损失", "求助意愿是积极信号"],
        ["虽在求助但仍在谈论赌博经验"],
        "赌博成瘾者的求助表达，立场是想要戒除，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=赌博; encoding_target=D2_隐喻"
))

S.append(sample(1448,
    "有些直播间表面是棋牌教学，点进去一看全是在'上分''下分'的，懂的都懂。平台也不管管，我举报了好几次都没用",
    "medium", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["揭露直播平台上的赌博伪装——'棋牌教学'实为赌博，'上分/下分'是赌博充值/提现的黑话。"],
        ["E1_平台黑话：'上分/下分'是棋牌赌博直播中的标准暗语——'上分'即充值/购买筹码，'下分'即提现/兑换现金。'懂的都懂'是对于不言自明的暗示。"],
        ["揭露直播平台赌博伪装的举报表达。"],
        ["识别了赌博直播的伪装（棋牌教学）", "解释了赌博黑话", "采取了举报行动"],
        ["在揭露时提及了赌博运营细节"],
        "揭露直播平台赌博伪装的正面表达，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=赌博; encoding_target=E1_平台黑话"
))

S.append(sample(1449,
    "AG真人的台子有人玩吗，最近想换个环境，私信交流一下。要稳的，黑台别来",
    "medium", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="medium",
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["正在寻找赌博平台的用户——'AG真人'是知名在线赌场品牌，'台子'指赌博平台，'稳的'和'黑台别来'是赌客间的质量术语。"],
        ["E1_平台黑话：'AG真人'是在线赌场品牌，'台子'、'黑台'（欺诈性的赌博平台）是赌客社区的专业术语。'私信交流'试图将讨论从公开平台转移到私密渠道。"],
        ["赌客社区的公开交流。"],
        ["提及了具体赌博品牌", "'私信交流'体现了逃避监管的意识"],
        ["没有直接发生博彩交易行为", "只是在询问信息"],
        "赌客社区的公开讨论和潜在引流，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=赌博; encoding_target=E1_平台黑话"
))

S.append(sample(1450,
    "朋友拉我进了一个群，说什么'龙虎斗''牛牛'天天发红包。我看着不对劲就没参与，但他已经投进去好几万了。这种是赌博吗？该怎么劝他",
    "low", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["描述朋友被拉入疑似赌博群——'龙虎斗''牛牛'（赌博游戏类型）、红包诱导、大额投入，并询问是否为赌博以及劝解方法。"],
        ["E1_平台黑话：'龙虎斗'、'牛牛'是网络棋牌赌博的游戏类型。'天天发红包'是赌博群的常见诱导手段。质疑'这是赌博吗'并寻求帮助表明用户处于识别阶段。"],
        ["对疑似赌博群的识别和求助。"],
        ["处于怀疑和寻求帮助的阶段", "自己没有参与体现了风险意识", "在思考帮助朋友的方法"],
        ["讨论了赌博游戏的具体名称"],
        "识别疑似赌博并寻求帮助的谨慎表达，判为 low。"
    ),
    review_notes="source=batch15_p1_gaps; gap=赌博; encoding_target=E1_平台黑话"
))

S.append(sample(1451,
    "今天看球了，曼城这场踢得真的烂，德布劳内一拿球就被断了，后防跟漏勺似的。不过足球嘛，输赢都正常，下赛季再来",
    "none", "none",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["纯粹的足球观赛评论——球员表现、战术分析、情绪表达。"],
        ["没有任何编码。这是完全正常的体育赛事讨论。分析球员表现和战术，表达失望但理性（'输赢都正常，下赛季再来'）。"],
        ["正常的体育赛事评论。"],
        ["讨论的是体育竞技而非博彩", "情绪表达正常（失望但不极端）"],
        ["与博彩评论共享'曼城vs某某队'的赛事框架，可能被误关联"],
        "正常的体育赛事讨论，判为 none（hard negative：足球讨论≠赌球）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=赌博; hard_negative"
))

S.append(sample(1452,
    "三国杀真好玩，跟室友从晚上八点打到凌晨三点，用黄盖一直苦肉一直爽。室友说我太狗了哈哈哈哈",
    "none", "none",
    platform="bilibili",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享在宿舍玩三国杀桌游的愉快经历。"],
        ["没有任何编码。'三国杀'是合法的桌游/卡牌游戏。'黄盖苦肉'是游戏内的角色技能机制。这是完全正常的游戏体验分享。"],
        ["正常的游戏体验分享。"],
        ["讨论的是合法桌游", "宿舍社交场景增加了正常性"],
        ["'一直苦肉一直爽'可能看起来像赌徒心理的调侃，但这里完全是游戏语境"],
        "正常的桌游分享，判为 none（hard negative：棋牌游戏≠赌博）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=赌博; hard_negative"
))

S.append(sample(1453,
    "下载了个象棋APP，天天跟网友下棋。现在业八水平，有没有棋友来切磋一下。纯下棋不聊别的，别推荐什么买彩的谢谢",
    "none", "none",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享象棋爱好并明确声明'纯下棋不聊别的'和'别推荐买彩'——主动与赌博划清界限。"],
        ["没有任何编码。'买彩'（买彩票/博彩）作为被拒绝的对象出现。文本主动声明不接受博彩推荐，体现了清晰的反赌博立场。"],
        ["正常的棋类爱好分享，明确排斥赌博。"],
        ["主动与赌博划清边界", "纯粹讨论象棋技术"],
        ["提及了'买彩'但以拒绝的口吻"],
        "正常的象棋爱好分享并主动抵制赌博推荐，判为 none（hard negative：象棋≠赌博）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=赌博; hard_negative"
))

# ╔══════════════════════════════════════════════════════════════════════════
# ║ 7. 毒品交易   (10 条) — 暗语交易/经验分享 + hard_negative
# ╚══════════════════════════════════════════════════════════════════════════

S.append(sample(1454,
    "新到一批叶子，品质保证，不是上次那种垃圾货。需要的老哥私我，同城面交，外地不包邮但给视频验货。懂的来",
    "high", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["'叶子'（大麻的常见代称）、'货'（毒品的泛化代称）、'老哥'（目标受众）、'同城面交'（交易方式）、'视频验货'（质量控制）构成完整的毒品交易广告。"],
        ["E1_平台黑话：'叶子'是中文互联网上大麻最普遍的代称之一。'货'泛指毒品。D2_隐喻：'品质保证'、'视频验货'借用商品交易的术语来讨论毒品。'懂的来'是对知情者的信号。"],
        ["典型的毒品交易广告——从产品描述到交易方式到质量保证一应俱全。"],
        ["'叶子'是对大麻的明确代指", "完整的交易信息（面交、验货）", "'懂的来'筛选知情人"],
        ["对不知情者而言，'叶子'可能只是字面意思"],
        "完整且专业的毒品交易广告，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=毒品; encoding_target=E1_平台黑话"
))

S.append(sample(1455,
    "周末想嗨一下，有没有飞行员带带我。最近太累了就想放松放松，有的私",
    "high", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["'嗨一下'（吸毒的俗称）、'飞行员'（带新手吸毒或介绍毒品渠道的人）——通过毒品社区黑话寻求毒品。"],
        ["E1_平台黑话：'嗨'在毒品语境中指吸毒后的兴奋状态。'飞行员'是毒品社区中指引路人/毒贩的黑话——'带你飞'即带你体验吸毒。'放松放松'是对吸毒动机的日常化包装。"],
        ["通过社区黑话公开寻求毒品渠道。"],
        ["'嗨'→吸毒的代称", "'飞行员'→引路人的代称", "'私'是寻求私下交易的标准操作"],
        ["脱离毒品语境，'嗨一下'和'飞行员'可能有普通解释"],
        "使用毒品黑话公开寻求毒品，编码明确且意图直接，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=毒品; encoding_target=E1"
))

S.append(sample(1456,
    "溜冰真的太爽了，第一次朋友带我，那感觉没法形容。不过后来发现身体越来越差，现在戒了半年了。劝看到的兄弟千万别碰，碰了就回不去了",
    "high", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["literal_keyword"],
    reasoning=base_reasoning(
        ["'溜冰'（吸食冰毒的俗称）——分享吸毒体验、描述身体损害、声称已戒，但在详细描述吸毒快感的同时又进行劝诫。"],
        ["E1_平台黑话：'溜冰'是冰毒吸食的常见俗称。文本虽然表面上在劝诫，但详细描述了'太爽了'、'没法形容'的吸毒快感体验——这种'先描述快感再说危害'的结构实际上可能激发好奇心而非制止。"],
        ["'先扬后抑'的吸毒体验分享——核心风险在于详细描述了吸毒的快感。"],
        ["'溜冰'直接指涉冰毒", "描述了吸毒快感体验", "虽以劝诫结尾但风险在内容本身"],
        ["以劝诫'千万别碰'收尾，表明文本希望产生正面影响"],
        "虽有劝诫意图但详细描述了吸毒快感体验，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=毒品; encoding_target=E1"
))

S.append(sample(1457,
    "有些人在夜店玩那个气球，说是合法的不算dp。笑死了，笑气就不是毒了？吸多了神经都坏掉。别自欺欺人了",
    "medium", "D1_反讽",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=["E1_平台黑话"],
    reasoning=base_reasoning(
        ["批评夜店中吸食'笑气'（一氧化二氮）并以'合法'为借口的行为，指出其危害性。"],
        ["E1_平台黑话：'气球'是笑气吸食的常见方式——将气体充入气球后吸入。'dp'是毒品的拼音缩写。文本立场是反毒品的——指出'合法≠无害'。"],
        ["批评毒品文化的反毒品表达。"],
        ["明确的反毒品立场", "指出了'合法≠安全'的常识", "揭示了'合法'借口的自欺欺人性"],
        ["提及了毒品的具体使用方式（气球），可能助长认知"],
        "反毒品表达，虽提到了使用方式但总体立场正确，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=毒品; encoding_target=D1+E1"
))

S.append(sample(1458,
    "出差去某西南城市，打了个车，司机师傅一路跟我聊哪里可以'拿货'。我愣了一下说我不碰这个的，他说年轻人不玩这个玩什么。后面全程不敢接话",
    "medium", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["讲述出差中遇到陌生人推销毒品的经历——'拿货'（购买毒品的暗语），用户的反应是拒绝和恐惧。"],
        ["E1_平台黑话：'拿货'在毒品语境中指购买毒品。'某西南城市'的模糊化地理指代可能是为了保护隐私或避免地域歧视。用户的反应（'不碰'、'不敢接话'）是恐惧和拒绝。"],
        ["被陌生人推销毒品的恐惧经历分享。"],
        ["用户的反应是拒绝和恐惧", "揭示了毒品在某些场合的渗透"],
        ["提及了毒品交易的暗语", "用了'西南城市'可能构成地域暗示"],
        "被毒品推销的恐惧经历分享，目标受众是路人但内容涉及毒品暗语，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=毒品; encoding_target=E1+D2"
))

S.append(sample(1459,
    "贴吧看到有人发'煲猪肉'的教程，标题写的'如何享受美食'点进去才发现不对劲。现在的暗号越来越五花八门了，平台真的该管管",
    "medium", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["揭露以'煲猪肉'（吸食冰毒的方言俗称）为暗号的网络毒品教程，批评平台监管不力。"],
        ["E1_平台黑话：'煲猪肉'是冰毒吸食的方言俗称，源于吸毒工具与烹饪器具的相似性。D2_隐喻：以烹饪（'享受美食'）为掩护传递毒品信息。文本立场是揭发和批评。"],
        ["揭露网上毒品暗号的举报/批评表达。"],
        ["识别了'煲猪肉'→冰毒的映射", "指出了平台的监管漏洞", "立场是反毒品"],
        ["揭露毒品暗号时传播了该暗号的具体写法"],
        "揭露毒品暗号和平台监管漏洞的批评表达，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=毒品; encoding_target=E1+D2"
))

S.append(sample(1460,
    "我有个表哥以前吸那个东西，后来进戒毒所三次才成功戒掉。现在他在社区做义工，经常跟年轻人说'好奇心是最贵的东西，代价你付不起'",
    "low", "C5_概念替换",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["分享表哥戒毒成功的正面故事——'那个东西'模糊指代毒品，强调'好奇心是最贵的东西'的警示。"],
        ["C5_概念替换：用'那个东西'模糊化指代毒品——避免直接提及毒品名称，可能是出于社交礼貌或平台安全。文本的立场是反毒品的——讲述戒毒成功和社区教育。"],
        ["戒毒成功案例的正面分享。"],
        ["以成功案例传递反毒品信息", "社区义工是正面社会行为", "警示语有教育意义"],
        ["'那个东西'的模糊化表达可能导致不确定性"],
        "正面反毒品故事分享，判为 low。"
    ),
    review_notes="source=batch15_p1_gaps; gap=毒品; encoding_target=C5"
))

S.append(sample(1461,
    "昨天去买电子烟弹，老板问我要不要试一下'特别的'。我说不用不用就普通的就行。出来以后手心都是汗，这种试探太吓人了",
    "low", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="medium",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["描述买电子烟弹时被店家试探推销'特别的'（可能含毒品成分的烟弹）——用户的反应是恐惧和拒绝。"],
        ["E1_平台黑话：电子烟店是毒品/违禁品灰色交易的潜在场景之一。'特别的'是试探性的模糊化指代——如果用户'懂'就会接话，不懂就像当事人这样只是困惑和恐惧。这符合'钓鱼式试探'的毒品推销模式。"],
        ["被试探性毒品推销的恐惧经历。"],
        ["用户的恐惧和拒绝反应是健康的", "识别了试探模式"],
        ["缺少更多证据确认'特别的'具体指什么——可能只是店家的营销话术"],
        "疑似毒品推销的恐惧经历，证据不足确认但模式可疑，判为 low。"
    ),
    review_notes="source=batch15_p1_gaps; gap=毒品; encoding_target=E1+D2"
))

S.append(sample(1462,
    "最近在研究CBD电子烟，说是合法的大麻提取物，不含THC，不会上瘾。有没有懂化学的科普一下，这玩意跟毒品到底什么关系？怕买错了惹麻烦",
    "none", "none",
    platform="zhihu",
    evidence_strength="weak",
    ambiguity="medium",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["在知乎上询问CBD（大麻二酚）电子烟的合法性——是否与毒品有关，表达了'怕买错了惹麻烦'的合规意识。"],
        ["CBD电子烟在中国属于灰色地带，但文本采用的是学术/法律咨询的口吻——要求'懂化学的科普'、关心法律边界。'怕惹麻烦'表明用户在积极寻求合规。这与毒品宣传有本质区别。"],
        ["出于合规意识的法律/科学咨询。"],
        ["以科普和法律咨询为目的", "明确表达了避免违法的意识", "要求专业人士解答"],
        ["CBD与THC的关系容易引起误解", "讨论大麻相关产品在中国语境中本身是敏感的"],
        "基于合规意识的合法咨询，判为 none（hard negative：合法物质咨询≠毒品讨论）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=毒品; hard_negative"
))

S.append(sample(1463,
    "我奶奶做手术打了全麻，出来以后跟我们说'医生那个药真好使，一秒就睡着了'。然后问医生能不能再打一次。医生说那个是麻醉药不是安眠药！笑死了奶奶太可爱了",
    "none", "none",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享奶奶手术后对麻醉药的天真反应——想要再打一次，医生耐心解释。"],
        ["没有任何编码。'全麻'（全身麻醉）是合法的医疗操作，'麻醉药'是规范的医学术语。这个故事的趣味性来自于老年患者的天真误解——与毒品滥用完全无关。"],
        ["温馨的家庭趣事分享。"],
        ["明确在医疗场景中", "幽默温馨的调性", "医生的专业回应强化了合规性"],
        ["讨论麻醉药的效果在非常极端的脱离上下文的条件下可能被误解"],
        "温馨的家庭趣事，判为 none（hard negative：医疗麻醉≠毒品）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=毒品; hard_negative"
))

# ╔══════════════════════════════════════════════════════════════════════════
# ║ 8. 枪支武器   (8 条) — 气狗/电狗暗语 + hard_negative
# ╚══════════════════════════════════════════════════════════════════════════

S.append(sample(1464,
    "出进口秃鹰全套，带喵（光学瞄具）和气瓶，九成新，有意私。懂的都懂这价位不是普通玩具能比的，别问些没营养的问题",
    "high", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["'秃鹰'是高性能气枪的知名品牌代称，'喵'是'瞄具'（瞄准镜）的谐音暗语，'气瓶'是气枪的动力源，'不是普通玩具'明确暗示这是具有杀伤力的武器。"],
        ["E1_平台黑话：'秃鹰'是气枪圈最知名的品牌代号之一。'喵'→'瞄'是A1_普通谐音，但在气枪社区中已高度固化。'全套'→枪支+配件。'懂的都懂'筛选知情买家。D2_隐喻：'不是普通玩具'通过否定来确认其杀伤力。"],
        ["典型的气枪交易广告——产品描述、配件、价格暗示一应俱全。"],
        ["'秃鹰'→高性能气枪的固定代称", "提供全套配件（瞄具、气瓶）", "'不是普通玩具'暗示杀伤力", "'懂的都懂'规避平台审核"],
        ["对不熟悉气枪社区的人，这些术语可能没有明确含义"],
        "完整的气枪交易广告，编码明确，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=枪支; encoding_target=E1+D2"
))

S.append(sample(1465,
    "收一把电狗，最好是M4或者AK的壳，用来下场玩的。只要发射器不要配件，预算2000以内，有的私。走转转或咸鱼",
    "high", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["'电狗'（电动气枪的圈内术语）、'M4/AK的壳'（枪型）、'发射器'（枪支的代称暗语）、'下场玩'（wargame/射击活动的黑话）。完整的收购信息。"],
        ["E1_平台黑话：'狗'是气枪圈的标志性黑话（源于粤语'气枪'→'气狗'的谐音演变）。'M4/AK'指仿制枪型。'发射器'是伪装枪支为玩具/文具的标准规避术语。'下场'指在wargame中使用。"],
        ["典型的气枪收购广告——在公开平台寻找卖家然后转到私密渠道交易。"],
        ["'狗'是气枪圈最核心的黑话", "'发射器'是枪支的规避代称", "描述了具体交易信息（预算、平台）"],
        ["wargame本身是合法的运动，'下场'、'发射器'在wargame社区有合法的字面含义"],
        "以wargame为掩护的气枪交易，编码丰富且意图明确，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=枪支; encoding_target=E1+D2"
))

S.append(sample(1466,
    "自己组了一把，板球座+精密管+高压阀门，初速290，精度30米硬币。全套花了三千多，比买的成品香多了。需要组装配件清单的兄弟私信",
    "high", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["'板球座'（气枪品牌）、'精密管'（枪管）、'高压阀门'（击发部件）、'初速290'（290米/秒的子弹初速——远高于法定气枪初速限制）、'精度30米硬币'（射击精度）。完整的自组气枪分享和配件分享邀约。"],
        ["E1_平台黑话：'板球'（Cricket）是高性能PCP气枪品牌。'初速290'的单位是米/秒——远超中国法律对气枪的认定标准。'30米硬币'即30米能击中硬币大小的目标，属于高精度。D2_隐喻：以'配件清单'为名传播武器制造信息。"],
        ["自组高性能气枪的经验分享和配件传播。"],
        ["'初速290'远超法定限制", "'30米硬币'表明高精度杀伤力", "分享'配件清单'是武器制造信息的传播"],
        ["对wargame爱好者而言，这可能只是技术讨论"],
        "自组高性能气枪的技术传播，数据明确超出合法范围，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=枪支; encoding_target=E1+D2"
))

S.append(sample(1467,
    "有没有玩板球的朋友，想问一下调节阀门用什么工具比较顺手。我自己拧了半天要么漏气要么力度不对，还是得请教老司机",
    "medium", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="medium",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["'板球'（PCP气枪品牌）——在询问维修/调试的技术问题。'阀门'（击发装置部件）、'漏气'、'力度'都是PCP气枪的技术术语。"],
        ["E1_平台黑话：'板球'如前所述是气枪代称。'阀门'、'漏气'、'力度'可以同时属于合法的工业/气动设备和非法气枪。"],
        ["气枪维修的技术讨论——存在合法的wargame解释和非法武器的双重可能性。"],
        ["'板球'在气枪圈中是固定的品牌代指", "技术讨论的专业性暗示用户深度参与"],
        ["'阀门'、'漏气'在合法的工业/家居维修中也完全正常", "没有明确的交易或杀伤力描述"],
        "气枪维修的技术讨论，存在双重解释空间，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=枪支; encoding_target=E1+D2"
))

S.append(sample(1468,
    "同学在朋友圈发了个打靶的视频，用的好像是那种打鸟的气狗，七八十米外的易拉罐一枪就打掉了。我就想知道这犯法不犯法，看他在那炫耀有点瘆得慌",
    "medium", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["描述同学炫耀使用气枪（'气狗'）打靶的行为——打到七八十米外的易拉罐表明较高的杀伤力。用户在质疑合法性。"],
        ["E1_平台黑话：'气狗'如前所述。'打鸟'是气枪用于狩猎的民间说法。'七八十米'的射程在气枪中属于高性能范围。"],
        ["对同学使用非法气枪的担忧和质疑。"],
        ["识别了行为的危险性", "在质疑合法性", "感到不安是正常的风险意识"],
        ["只是旁观者的观察和担忧，没有参与"],
        "对他人使用非法枪支的担忧表达，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=枪支; encoding_target=E1"
))

S.append(sample(1469,
    "问一下CS2里M4A4和M4A1-S现在哪个好用？以前一直用A4，听说A1被削了，但看职业比赛还是有人在用",
    "none", "none",
    platform="bilibili",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["纯粹的游戏内武器性能讨论——CS2中M4A4与M4A1-S的对比选择。"],
        ["没有任何编码。'M4A4'、'M4A1-S'是CS2游戏中的虚拟枪械。讨论的是游戏内的武器平衡和职业比赛meta，与现实枪支完全无关。"],
        ["正常的电子游戏讨论。"],
        ["游戏中武器的名称完全在游戏语境中", "讨论的是竞技平衡性而非现实武器"],
        ["M4系列枪械名称可能与真实枪械讨论混淆——但gaming社区是最大的M4提及场景之一"],
        "正常的游戏讨论，判为 none（hard negative：游戏枪械≠真实武器）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=枪支; hard_negative"
))

S.append(sample(1470,
    "今天去Wargame场地打了半天，用的场地租的发射器，累得半死但是超级爽。这运动是真的费体力，跑完三场腿都软了。深圳这边有没有好的场子推荐？",
    "none", "none",
    platform="redbook",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享在合法Wargame场地使用场地提供的'发射器'（合法道具枪）的体验——提到运动强度大、累但爽。"],
        ["'发射器'在Wargame中可能是指合法的道具枪/彩弹枪——文本提到了'场地租的'说明来自合法经营者。讨论的是wargame作为一项体育运动的体验。这与非法枪支的讨论有本质区别——是在合规场所使用合规设备。"],
        ["合法的运动体验分享。"],
        ["在合法经营场地使用合规设备", "讨论运动体验而非武器性能", "Wargame是合法的体育运动"],
        ["'发射器'在特定语境中可能被误解为枪支代称"],
        "合法的Wargame运动体验分享，判为 none（hard negative：合规运动≠枪支交易）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=枪支; hard_negative"
))

S.append(sample(1471,
    "我爸是个军事迷，家里一堆军模，什么95式、M16、AK47，不过都是1:6的塑料模型。最近他又在拼一个二战系列，一个虎式坦克弄了两个月了还没拼完哈哈",
    "none", "none",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享父亲军事模型的爱好——包括了各种枪械名称但说明是'1:6的塑料模型'。"],
        ["没有任何编码。'95式'、'M16'、'AK47'作为军事模型的名称出现。用户明确标注'塑料模型'和'1:6'（模型比例），完全排除了真实武器的可能。"],
        ["正常的模型收藏爱好分享。"],
        ["明确标注为塑料模型", "模型比例信息增加了可信度", "讨论的是拼装过程而非武器性能"],
        ["提及了多款真实枪械名称"],
        "正常的军事模型爱好分享，判为 none（hard negative：模型收藏≠真实武器讨论）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=枪支; hard_negative"
))

# ╔══════════════════════════════════════════════════════════════════════════
# ║ 9. 假证/假章   (8 条) — 办证广告/学历造假 + hard_negative
# ╚══════════════════════════════════════════════════════════════════════════

S.append(sample(1472,
    "办.各.类.证.书：毕.业.证、学.位.证、四.六.级、驾.照、身.份.证，包.查.包.真。加.微.信.zheng*****8，十.年.老.店.信.誉.保.证。不.信.别.加",
    "high", "B4_符号/空格/Unicode 干扰",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["E1_平台黑话"],
    reasoning=base_reasoning(
        ["通过在每个字之间插入句号（.）来规避关键词过滤——推销各类假证件：毕业证、学位证、四六级、驾照、身份证，并声称'包查包真'（承诺能在系统查到）。"],
        ["B4_符号干扰：使用句号打断关键词是规避自动化检测的标准手法。E1_平台黑话：'包查包真'（承诺学信网可查）是假证广告的标准话术——声称能在官方系统查验（通常是假的或利用了系统漏洞）。'十年老店'建立虚假信任感。"],
        ["典型的规避式假证广告。"],
        ["句号分割的规避意图明确", "'包查包真'是假证行业的标志性话术", "覆盖面广（从学历到驾照到身份证）", "加微信的引流操作"],
        ["对不熟悉者而言，分割的文字可能没有明确含义"],
        "规避式假证广告，多信号印证，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=假证; encoding_target=B4+E1"
))

S.append(sample(1473,
    "四六级没过？没关系，我们帮你搞定。正规渠道，学信网可查，价格合理。私信咨询，不成功不收费。",
    "high", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["假证广告——'学信网可查'（中国高等教育学生信息网）是假证广告的核心承诺，'正规渠道'是伪装。'不成功不收费'降低心理门槛。"],
        ["E1_平台黑话：'学信网可查'是假证行业最核心的话术——造假者声称能让假证在教育部官方系统中查询。'正规渠道'暗示存在灰色地带的合法操作空间——这是一种误导。"],
        ["以'帮助'为包装的假证推广。"],
        ["'学信网可查'是假证广告的标志性承诺", "'正规渠道'的误导性包装"],
        ["对于真正需要补办证件的人，这可能被误解为合法服务"],
        "以'正规渠道''学信网可查'为核心卖点的假证广告，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=假证; encoding_target=E1+D2"
))

S.append(sample(1474,
    "急用本科学历找工作，就差这个门槛。全日制统招本科毕业证学位证，档案齐全，懂的私，价格可谈",
    "high", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="strong",
    ambiguity="low",
    encoding_secondary=["D2_隐喻"],
    reasoning=base_reasoning(
        ["假学历的求购广告——'全日制统招本科'（最难造假的类型也最贵）、'档案齐全'（暗示全套造假服务）、'懂的私'（筛选知情者）。"],
        ["E1_平台黑话：'全日制统招本科'是学历造假中技术要求最高的类型。'档案齐全'暗示造假服务链涵盖学籍档案、成绩单等全套材料。'懂的私'筛选买家。"],
        ["高端的全套学历造假求购。"],
        ["'全日制统招本科'的要求指向高难度的造假", "'档案齐全'表明对造假链的专业认知", "'懂的私'避免被路人发现"],
        ["从文字表面看不出来是否是真正咨询学历提升的人"],
        "专业的学历造假求购，判为 high。"
    ),
    review_notes="source=batch15_p1_gaps; gap=假证; encoding_target=E1+D2"
))

S.append(sample(1475,
    "在网上搜'办驾照'出来一堆代办，价格从几百到几千都有。我想问一下这些所谓的'免考直出'到底是真的假的？有没有懂的科普一下，不想被骗",
    "medium", "E1_平台黑话",
    platform="zhihu",
    evidence_strength="moderate",
    ambiguity="medium",
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["描述在网上搜索'办驾照'代办服务，注意到'免考直出'（不考试直接拿驾照）的广告，询问真假以避免被骗。"],
        ["E1_平台黑话：'免考直出'是驾照造假/非法代办的标志性话术——承诺不参加考试即可获得真实驾照（通常是假的或通过行贿获得）。'不想被骗'表明用户持怀疑态度。"],
        ["对可疑驾照代办服务的质疑和询问。"],
        ["对'免考直出'持怀疑态度", "明确表示'不想被骗'", "在主动寻求真伪辨别信息"],
        ["搜索和讨论'办驾照'代办服务的合法性"],
        "对可疑驾照代办的质疑和科普寻求，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=假证; encoding_target=E1"
))

S.append(sample(1476,
    "我室友前几天买了个假的病假条不去上课，结果被辅导员一眼识破了，因为落款医院那天根本没开门。笑死我了，造假都不会先做功课",
    "medium", "E1_平台黑话",
    platform="bilibili",
    evidence_strength="moderate",
    ambiguity="low",
    encoding_secondary=["D1_反讽"],
    reasoning=base_reasoning(
        ["描述同学购买假病假条被识破的趣事——造假者因忽略医院开门时间而暴露。"],
        ["D1_反讽：以调侃口吻（'笑死我了'、'造假都不会先做功课'）讲述造假失败的故事——这种叙事实际上是在分享造假的风险和愚蠢。"],
        ["以搞笑方式分享造假风险的叙事。"],
        ["以失败揭示造假的风险", "调侃的口吻降低了模仿的诱导性"],
        ["分享了造假的具体方法（假病假条）"],
        "以搞笑失败故事揭示造假风险，判为 medium。"
    ),
    review_notes="source=batch15_p1_gaps; gap=假证; encoding_target=E1+D1"
))

S.append(sample(1477,
    "现在找工作太难了，有些公司就差个学历门槛。但是买假证万一被查出来不是更惨吗？简历造假被hr圈拉黑的案例太多了",
    "low", "D1_反讽",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="medium",
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["讨论就业压力下的学历造假诱惑和造假风险——'买假证万一被查出来不是更惨吗'表达了风险意识。"],
        ["D1_反讽：从讨论假证的可能性转到'不是更惨吗'——结构上是先提出诱惑再自我反驳。这种自我辩论的模式在假证话题中比较常见——既是'我考虑过这条路'的表达，也是'但我最终会走正路'的暗示。"],
        ["就业压力下的求职伦理讨论。"],
        ["自我辩论最终导向不造假的结论", "指出了造假的实际风险（被拉黑）"],
        ["前半句承认了造假存在诱惑，可能对处于同样压力下的人产生不良影响"],
        "就业压力下的伦理自我辩论，最终偏向不造假，判为 low。"
    ),
    review_notes="source=batch15_p1_gaps; gap=假证; encoding_target=D1"
))

S.append(sample(1478,
    "考研成绩出来了，差3分过线，现在在想要不要二战。但是又看到网上那些'办证保证录取'的广告，虽然知道99%是骗子但心里还是咯噔一下。唉，老老实实再学一年吧",
    "low", "E1_平台黑话",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["考研失利后看到'办证保证录取'广告的心理波动——最终决定'老老实实再学一年'。"],
        ["E1_平台黑话：'办证保证录取'是学历/录取造假广告的常见话术。文本完整呈现了'看到诱惑→心理波动→理性回归'的决策过程，最终选择了合规道路。"],
        ["考研失利后面对造假诱惑的心理挣扎和最终理性抉择。"],
        ["最终决定'老老实实再学一年'", "认识到了'99%是骗子'"],
        ["提及了造假广告的具体内容", "表达了对造假的短暂心动"],
        "考研失利后面对造假诱惑的挣扎和理性回归，判为 low。"
    ),
    review_notes="source=batch15_p1_gaps; gap=假证; encoding_target=E1"
))

S.append(sample(1479,
    "刚去学信网查了一下我的学历认证，确认没问题才放心。建议大家都去查查，尤其是准备出国留学的同学，有些学校要WES认证，提前准备材料",
    "none", "none",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享在学信网查验学历认证并建议他人提前准备材料的实用建议。"],
        ["没有任何编码。'学信网'（中国高等教育学生信息网）是官方的学历认证平台。'WES认证'（World Education Services）是正规的学历认证服务机构。这是完全合规的学历事务讨论。"],
        ["正常的学历认证实用分享。"],
        ["使用的是官方学历认证渠道", "建议合规操作", "讨论的都是正规认证服务"],
        ["'学信网'同时也是假证广告中常被提及的系统——但此处是正规使用"],
        "正常的学历认证实用建议，判为 none（hard negative：学历认证≠假证）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=假证; hard_negative"
))

S.append(sample(1480,
    "身份证丢了，去派出所补办居然这么简单，带了个户口本拍了个照，三天就拿到临时身份证了。给深圳公安的办事效率点赞，真的快",
    "none", "none",
    platform="text_comment",
    evidence_strength="weak",
    ambiguity="low",
    hard_negative=True,
    encoding_secondary=[],
    reasoning=base_reasoning(
        ["分享在派出所正常补办身份证的正面体验。"],
        ["没有任何编码。'身份证补办'是正常的公民服务流程。'派出所'是合法的政府机构。文本表达的是对政府服务效率的认可。"],
        ["正常的证照补办体验分享。"],
        ["官方正规渠道补办证件", "正面评价政府服务", "鼓励他人走正规模渠道"],
        ["'身份证丢了→补办'的流程可能与假证广告中的'身份证代办'共享关键词"],
        "正常的证照补办体验，判为 none（hard negative：补办证件≠造假）。"
    ),
    review_notes="source=batch15_p1_gaps; gap=假证; hard_negative"
))

# ═════════════════════════════════════════════════════════════════════════
# Write JSONL
# ═════════════════════════════════════════════════════════════════════════

with open(COMBINED, "a", encoding="utf-8") as f:
    for s in S:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")

print(f"✅ Appended {len(S)} samples to {COMBINED}")
print(f"   ID range: {S[0]['id']} – {S[-1]['id']}")
print(f"   Domains: 新疆14 | 西藏12 | 法轮功10 | 文革10 | 香港13 | 赌博10 | 毒品10 | 枪支8 | 假证8")
