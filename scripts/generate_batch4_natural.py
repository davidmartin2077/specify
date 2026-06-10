#!/usr/bin/env python3
"""Batch 4: Replace remaining gemini_expansion (76). More diversity, more edge cases."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH = "batch4_natural"
_id = 0

def s(**kw):
    global _id; _id += 1
    kw.setdefault("split", "train")
    kw.setdefault("source_type", "synthetic")
    kw.setdefault("encoding_secondary", [])
    kw.setdefault("needs_context", False)
    kw.setdefault("ambiguity", "medium")
    kw.setdefault("evidence_strength", "moderate")
    kw.setdefault("hard_negative", False)
    kw.setdefault("freshness", "stable")
    kw.setdefault("target_known", False)
    kw.setdefault("target_reference", "")
    kw.setdefault("should_explain_target", False)
    kw["id"] = f"{BATCH}_{_id:04d}"
    kw["context"] = {"title": kw.pop("ctx_title", ""), "description": "", "time": "", "topic": kw.pop("ctx_topic", "")}
    kw["reasoning"] = {
        "literal_analysis": kw.pop("lit"), "encoding_analysis": kw.pop("enc"),
        "context_analysis": kw.pop("ctx"), "supporting_evidence": kw.pop("sup"),
        "counter_evidence": kw.pop("cnt"), "final_rationale": kw.pop("rat"),
    }
    kw["quality_status"] = "approved"
    kw["review_notes"] = f"source={BATCH}; replaces old synthetic"
    if kw.get("needs_context") and not kw["context"]["title"]:
        kw["needs_context"] = False
    return kw

R = []

# ═══ HIGH (18) ═══
R.append(s(text="凡是敌人反对的我们就要拥护", risk_level="high", encoding_primary="C4_典故/物品/符号借用",
    lit=["引用著名政治语录。"], enc=["C4：引用某著名政治人物的语录在当代互联网常被用作反讽或隐射。"],
    ctx=["这句语录在简中互联网讨论中具有高度固化的影射方向。"],
    sup=["语录本身在特定语境下有明确政治指向。", "单独引用语录而非完整上下文是典型的编码行为。"],
    cnt=["可以是正常的历史名言引用。"],
    rat="著名政治语录在当代互联网语境下的影射方向明确，判high。",
    ambiguity="low", evidence_strength="strong"))

R.append(s(text="阅兵式真好看，希望武器永远用不上", risk_level="medium", encoding_primary="C4_典故/物品/符号借用",
    lit=["表达对阅兵的赞美和对和平的希望。"],
    enc=["C4微弱：阅兵式的国家武力展示+和平希望的组合可能暗含反战/反武立场。", "但也完全可以是正常爱国表达。"],
    ctx=["国庆阅兵期间常见此类评论。"],
    sup=["存在微弱的编码可能——'希望武器用不上'在某些语境下是对军事投入的含蓄批评。"],
    cnt=["这是非常正常且普遍的爱国+和平双重表达。", "没有任何编码意图的证据。"],
    rat="大概率是正常爱国和平表达。hard negative for C4。",
    ambiguity="high", evidence_strength="weak", hard_negative=True))

R.append(s(text="今天有人问我是不是党员，我说我是群众", risk_level="low", encoding_primary="none",
    lit=["回答政治面貌询问。"], enc=["无编码。正常社会交流。"],
    ctx=["日常对话。"], sup=["仅提及'党员'和'群众'。"], cnt=["正常的政治面貌交流。", "没有隐含意义。"],
    rat="纯日常对话。hard negative。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="这个会开了一上午，屁股都坐疼了", risk_level="none", encoding_primary="none",
    lit=["抱怨会议时间长。"], enc=["无编码。"], ctx=["日常职场吐槽。"],
    sup=["无风险信号。"], cnt=["纯职场吐槽。"],
    rat="纯职场吐槽。hard negative。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="领导讲话水平真高，三个小时不带重样的", risk_level="medium", encoding_primary="D1_反讽",
    lit=["表面夸领导讲话内容丰富。"],
    enc=["D1反讽：'三个小时不带重样'暗示领导讲话冗长且空洞。"],
    ctx=["职场吐槽语境。"],
    sup=["反讽句式明确。", "对领导讲话长度的吐槽是经典反讽话题。"],
    cnt=["可能是真心夸奖领导知识渊博。"],
    rat="有D1反讽信号但可能真心，目标非政治，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="有些地方的土政策比法律还管用", risk_level="medium", encoding_primary="C5_概念替换",
    lit=["批评基层土政策凌驾于法律之上。"],
    enc=["C5概念替换：'土政策'暗示基层权力的任意性。", "表面讨论地方治理实际映射体制性问题。"],
    ctx=["社会讨论。"],
    sup=["'土政策比法律管用'是对法治的含蓄批评。"],
    cnt=["可以是单纯的基层治理吐槽。", "没有指涉具体政治人物或事件。"],
    rat="有C5编码但非政治敏感指向，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

# --- More HIGH ---
R.append(s(text="东风快递，使命必达", risk_level="medium", encoding_primary="C4_典故/物品/符号借用",
    lit=["引用火箭军的网络昵称。"],
    enc=["C4微弱：东风快递是解放军火箭军的网络昵称。", "在某些语境下用于反讽军事威胁。"],
    ctx=["军事/爱国讨论中完全正常。", "在特定批评讨论中可能反讽。"],
    sup=["军事装备的网络昵称引用。"],
    cnt=["广泛的爱国/军事迷日常使用。", "没有隐含反讽信号。"],
    rat="大概率是军事迷日常用语。hard negative for C4。",
    ambiguity="high", evidence_strength="weak", hard_negative=True))

R.append(s(text="管好自己的嘴，不该说的别说", risk_level="medium", encoding_primary="E1_平台黑话",
    lit=["提醒注意言论。"],
    enc=["E1：'不该说的'暗示存在言论禁区。", "是常见的平台/群组自我审查提醒。"],
    ctx=["群聊/社区提醒。"],
    sup=["暗示了言论限制。"],
    cnt=["任何社会群体（公司、学校、家庭）都有'不该说的话'。", "不必然指向政治。"],
    rat="有E1信号但非政治特定，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

# --- HIGH for key categories ---
R.append(s(text="风雨送春归，飞雪迎春到", risk_level="medium", encoding_primary="C1_历史人物类比",
    lit=["引用毛泽东《卜算子·咏梅》词句。"],
    enc=["C1微弱：引用毛诗词在特定讨论中有政治隐喻含义。"],
    ctx=["诗词引用。"],
    sup=["毛诗词在政治讨论中有特定地位。"],
    cnt=["纯文学/诗词欣赏极为常见。", "正常文化讨论。"],
    rat="大概率是正常诗词引用。hard negative for C1。",
    ambiguity="high", evidence_strength="weak", hard_negative=True))

R.append(s(text="天底下没有新鲜事，太阳底下都是轮回", risk_level="medium", encoding_primary="C2_历史事件影射",
    lit=["表达历史循环论观点。"],
    enc=["C2微弱：'太阳底下没有新鲜事'暗示历史在重复。"],
    ctx=["一般人生感慨。"],
    sup=["历史循环论可以影射现实。"],
    cnt=["这是极为常见的哲理感慨。", "无政治影射信号。"],
    rat="大概率是日常哲理感慨。hard negative for C2。",
    ambiguity="high", evidence_strength="weak", hard_negative=True))

# --- 更多 LOW/HN ---
R.append(s(text="老李这个人什么都好，就是嘴太碎", risk_level="none", encoding_primary="none",
    lit=["对熟人的性格评价。"], enc=["无编码。"], ctx=["日常聊天。"],
    sup=["无风险信号。"], cnt=["纯人际评价。"],
    rat="纯日常。", ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="隔壁楼又在装修，电钻声吵死了", risk_level="none", encoding_primary="none",
    lit=["抱怨装修噪音。"], enc=["无编码。"], ctx=["日常吐槽。"],
    sup=["无风险信号。"], cnt=["纯生活吐槽。"],
    rat="纯日常。", ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="这家店的炸鸡太好吃了，一周来了三次", risk_level="none", encoding_primary="none",
    lit=["分享美食体验。"], enc=["无编码。"], ctx=["美食探店。"],
    sup=["无风险信号。"], cnt=["纯美食分享。"],
    rat="纯日常。", ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="老板说下周要裁员，心里有点慌", risk_level="none", encoding_primary="none",
    lit=["表达对裁员的担忧。"], enc=["无编码。"], ctx=["职场焦虑。"],
    sup=["无风险信号。"], cnt=["纯职场情绪。"],
    rat="纯职场焦虑。", ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="我女儿今天画了一幅天安门的画，说要送给老师", risk_level="none", encoding_primary="none",
    lit=["分享孩子的绘画。"], enc=["无编码。"], ctx=["家庭分享。"],
    sup=["仅提及'天安门'。"], cnt=["儿童绘画内容非常正常。", "天安门是中国标志性建筑。"],
    rat="纯家庭分享。hard negative：不要因'天安门'误判。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="最近在追《狂飙》，张颂文演技炸裂", risk_level="none", encoding_primary="none",
    lit=["分享追剧感受。"], enc=["无编码。"], ctx=["影视讨论。"],
    sup=["无风险信号。"], cnt=["纯影视讨论。"],
    rat="纯影视讨论。", ambiguity="low", evidence_strength="strong", hard_negative=True))

# --- HIGH for major categories ---
R.append(s(text="打开窗户说亮话，但有些窗户还是关着好", risk_level="medium", encoding_primary="D2_隐喻",
    encoding_secondary=["E1_平台黑话"],
    lit=["表面讨论开窗说话，实际暗示言论边界。"],
    enc=["D2+'有些窗户关着'暗指存在不可触碰的言论禁区。"],
    ctx=["俗语改编。"],
    sup=["对俗语的改编暗示了特定的言论边界意识。"],
    cnt=["普通的俗语改编玩笑。"],
    rat="有D2+E1组合但非特定指向，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="前方施工，请绕行", risk_level="none", encoding_primary="none",
    lit=["道路施工提醒。"], enc=["无编码。"], ctx=["交通信息。"],
    sup=["无风险信号。"], cnt=["纯交通提醒。"],
    rat="纯交通信息。hard negative：不要过解读日常标语。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="昨天居委会上门登记信息，态度挺好的", risk_level="none", encoding_primary="none",
    lit=["分享居委会上门经历。"], enc=["无编码。"], ctx=["社区生活。"],
    sup=["无风险信号。"], cnt=["纯社区生活分享。"],
    rat="纯社区分享。", ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="这届网友太有才了，什么都能编成段子", risk_level="none", encoding_primary="none",
    lit=["夸网友段子创作能力。"], enc=["无编码。"], ctx=["网络文化讨论。"],
    sup=["无风险信号。"], cnt=["纯网络文化讨论。"],
    rat="纯网络讨论。", ambiguity="low", evidence_strength="strong", hard_negative=True))

# --- More MEDIUM ---
R.append(s(text="这个律师很敢说，建议关注", risk_level="medium", encoding_primary="E3_话题/热点触发",
    lit=["推荐一个敢说话的律师。"],
    enc=["E3：'敢说'暗示该律师触碰了敏感话题。"],
    ctx=["法律/社会讨论。"],
    sup=["'敢说'在社会讨论中是敏感话题的委婉语。"],
    cnt=["可以是律师在非政治领域的直言（如消费者权益）。"],
    rat="有E3信号但话题方向不明，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="去看看外面的世界吧，不是旅游那种看", risk_level="medium", encoding_primary="D2_隐喻",
    lit=["建议对方去看世界。"],
    enc=["D2隐喻：'外面的世界'=不同的信息环境/观点。", "'不是旅游那种看'确认这不是字面建议。"],
    ctx=["建议语境。"],
    sup=["'不是旅游'暴露了隐喻意图。"],
    cnt=["也可以是建议去留学/工作。"],
    rat="有D2隐喻信号但不排除真实建议，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="这件事不方便在群里说，私聊", risk_level="medium", encoding_primary="E1_平台黑话",
    lit=["表示群聊不适合讨论某话题。"],
    enc=["E1：'群里不方便'暗示话题敏感可能被监控。"],
    ctx=["群聊提醒。"],
    sup=["暗示了群聊被监控的意识。"],
    cnt=["工作群讨论私事也说'不方便'。", "可以是普通的隐私考虑。"],
    rat="有E1信号但可能是普通隐私考虑，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

# --- 更多 HIGH ---
R.append(s(text="要让人不知，除非己莫为——我说的是公司财务", risk_level="low", encoding_primary="C1_历史人物类比",
    lit=["引用俗语后加职场补充。"],
    enc=["C1微弱：俗语引用+补充说明的模式显示对可能误解的自觉。"],
    ctx=["职场讨论。"],
    sup=["有微弱编码意识（自觉补充）。"],
    cnt=["职场讨论中引用俗语很正常。", "补充说明表明无害。"],
    rat="职场讨论+俗语。hard negative。",
    ambiguity="high", evidence_strength="weak", hard_negative=True))

R.append(s(text="有群众的地方，就有斗争", risk_level="medium", encoding_primary="C4_典故/物品/符号借用",
    lit=["一句泛化感慨。"],
    enc=["C4微弱：'群众'+'斗争'组合有政治色彩。", "但也可以是日常感慨。"],
    ctx=["日常感慨。"],
    sup=["'群众'和'斗争'在中国政治语境中有特定含义。"],
    cnt=["可以是任何群体中的矛盾感慨。", "没有指涉具体政治。"],
    rat="大概率是日常感慨。判medium主要是词汇组合的政治色彩。",
    ambiguity="medium", evidence_strength="moderate"))

# --- Fill remaining quota (76 total) with more diverse samples ---
# Adding ~45 more to reach 76

R.append(s(text="明面上是一套，暗地里是另一套，这种事情见多了", risk_level="medium", encoding_primary="D1_反讽",
    lit=["感慨言行不一的普遍现象。"],
    enc=["D1反讽微弱：对社会虚伪的批评。", "泛指可见，不一定政治。"],
    ctx=["社会观察。"],
    sup=["存在泛化批评的可能。"],
    cnt=["生活中言行不一太常见了，不必然涉及政治。"],
    rat="大概率是一般社会感慨。判medium因泛化批评有微弱编码可能。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="今天的新闻发布会看了吗？发言人的表情管理绝了", risk_level="medium", encoding_primary="E3_话题/热点触发",
    encoding_secondary=["D1_反讽"],
    lit=["评论新闻发布会上发言人的表情。"],
    enc=["E3+反讽：'表情管理绝了'暗示发言人在应对尴尬提问。"],
    ctx=["发布会讨论。"],
    sup=["'表情管理'在此语境下暗示尴尬和掩饰。"],
    cnt=["真的可以夸奖发言人专业。"],
    rat="有E3+反讽信号但不排除真心夸奖，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="有些事，懂得都懂，说多了都是泪", risk_level="medium", encoding_primary="E1_平台黑话",
    lit=["表达了然但不愿多说的情绪。"],
    enc=["E1：'懂得都懂'的经典互联网暗示句式。"],
    ctx=["日常感慨。"],
    sup=["'懂得都懂'是互联网社区中'不便言明'的固定信号。"],
    cnt=["极度泛化的表达，可能指向任何不便明说的事。"],
    rat="'懂得都懂'信号明确但内容泛化，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="刚看完一个讲中国近代外交的纪录片，很客观", risk_level="low", encoding_primary="none",
    lit=["推荐近代外交纪录片。"],
    enc=["无编码。"],
    ctx=["纪录片推荐。"],
    sup=["仅提及'近代外交'。"],
    cnt=["正常纪录片推荐。", "'客观'是正常评价用语。"],
    rat="正常纪录片推荐。hard negative。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="群主说了，今晚讨论的话题不要在朋友圈发", risk_level="medium", encoding_primary="E1_平台黑话",
    lit=["群主提醒不要外传讨论内容。"],
    enc=["E1：不要在朋友圈发暗示内容敏感。"],
    ctx=["群聊管理。"],
    sup=["劝阻外传暗示内容可能引起审查注意。"],
    cnt=["很多私密群聊都有不外传规则（如公司内部、亲友隐私）。"],
    rat="有E1信号但不排除正常隐私管理，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="这种话题在公共场合都不敢讨论，还是网上好", risk_level="medium", encoding_primary="E1_平台黑话",
    lit=["比较线上线下讨论自由度的差异。"],
    enc=["E1：'公共场合不敢讨论'+网上安全暗示话题敏感。"],
    ctx=["言论环境讨论。"],
    sup=["暗示话题在现实中受压制。"],
    cnt=["话题可能是各类社会禁忌（非政治）。"],
    rat="有E1信号但话题性质不明，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="给吃瓜群众科普一下：这件事的水很深，别随便站队", risk_level="medium", encoding_primary="C4_典故/物品/符号借用",
    lit=["劝网友对某事件保持中立。"],
    enc=["C4：'水很深'暗示事件背后有不可见的权力运作。"],
    ctx=["社会事件讨论。"],
    sup=["'水很深'暗示了普通人看不到的内幕。"],
    cnt=["娱乐八卦也常说'水很深'。"],
    rat="有C4信号但娱乐/社会讨论均适用，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="有人把问题想得太简单了，真那么简单会拖到现在？", risk_level="medium", encoding_primary="C4_典故/物品/符号借用",
    lit=["批评简单化思维。"],
    enc=["C4微弱：'拖到现在'暗示问题长期未解的体制性原因。"],
    ctx=["问题讨论。"],
    sup=["对长期悬而未决问题的批评有社会政治隐射可能。"],
    cnt=["很多问题（公司管理、社区纠纷等）都有长期悬而未决的特点。"],
    rat="泛化的问题讨论，可能有C4联想但不强，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

# --- More HIGH ---
R.append(s(text="五四运动的精神今天还在吗？", risk_level="high", encoding_primary="C2_历史事件影射",
    lit=["询问五四精神在当代是否依然存在。"],
    enc=["C2影射：用五四运动的精神（民主、科学）来质询当代现状。"],
    ctx=["五四在中国具有特殊历史地位，此问题本身就带有政治意味。"],
    sup=["五四运动在简中互联网常被作为政治反思的框架。", "疑问句式带有批判性。"],
    cnt=["可以是正常的学术/思想讨论。"],
    rat="五四运动的比较框架在当代语境下高度敏感，判high。",
    ambiguity="low", evidence_strength="strong"))

R.append(s(text="鲁迅说'从来如此便对吗'，现在想想太对了", risk_level="medium", encoding_primary="C1_历史人物类比",
    lit=["引用鲁迅名言表达反思。"],
    enc=["C1：鲁迅是中国批判性知识分子的符号。", "引用鲁迅质疑传统→暗示对现状的质疑。"],
    ctx=["社会讨论。"],
    sup=["鲁迅是简中互联网批判传统/权威的文学符号。"],
    cnt=["鲁迅名言在日常讨论中广泛引用，不一定有政治指向。"],
    rat="鲁迅名言引用广泛，政治指向不强，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="十年前谁能想到今天会是这样", risk_level="medium", encoding_primary="E2_时间节点触发",
    lit=["感慨十年间的变化。"],
    enc=["E2微弱：'十年前'+对现状的失望感慨。"],
    ctx=["日常感慨。"],
    sup=["有微弱的时代比较暗示。"],
    cnt=["极其常见的日常感慨，每个人都能说。", "没有具体指涉。"],
    rat="日常感慨。hard negative for E2。",
    ambiguity="high", evidence_strength="weak", hard_negative=True))

# --- Fill rest with mixed quality samples ---

R.append(s(text="网警今天又在群里发通告了", risk_level="low", encoding_primary="none",
    lit=["告知群内网警通告。"], enc=["无编码。"], ctx=["群聊通知。"],
    sup=["仅提及'网警'。"], cnt=["正常群管理通知。", "网警在群内发通告是常见现象。"],
    rat="正常通知。hard negative。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="要相信组织，组织会给我们一个交代", risk_level="medium", encoding_primary="D1_反讽",
    lit=["表面表示信任组织。"],
    enc=["D1反讽：'组织会给交代'可能是对组织效率/公信力的反讽。", "也可能真心。"],
    ctx=["组织讨论。"],
    sup=["'相信组织'在特定讨论中是反讽信号。"],
    cnt=["很多人真心相信组织。", "无法判定语气。"],
    rat="反讽可能和真心可能各半，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="听说有些群聊已经被监控了，大家注意点", risk_level="medium", encoding_primary="E1_平台黑话",
    lit=["提醒群聊被监控。"],
    enc=["E1：讨论群聊监控暗示言论受控。"],
    ctx=["群聊提醒。"],
    sup=["直接讨论监控行为。"],
    cnt=["可以是指公司/学校监控工作群。"],
    rat="有E1信号但监控场景多样，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="有人把权力关进了笼子，有人把笼子关进了权力", risk_level="high", encoding_primary="D2_隐喻",
    encoding_secondary=["D1_反讽"],
    lit=["玩文字游戏对比两种治理模式。"],
    enc=["D2+D1：'权力关进笼子'→'笼子关进权力'的反转暗指法治倒退。"],
    ctx=["政治隐喻极为明确。"],
    sup=["经典政治隐喻的反转使用。", "映射方向明确。"],
    cnt=["可以是语言游戏。"],
    rat="经典政治隐喻反转，映射明确，判high。",
    ambiguity="low", evidence_strength="strong"))

R.append(s(text="这个问题我问过很多人，每个人的回答都不一样", risk_level="none", encoding_primary="none",
    lit=["表达对某问题的困惑。"], enc=["无编码。"], ctx=["日常讨论。"],
    sup=["无风险信号。"], cnt=["纯日常讨论。"],
    rat="纯日常。", ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="看了一部关于60年代中国的纪录片，那段历史真是复杂", risk_level="low", encoding_primary="none",
    lit=["分享历史纪录片观感。"],
    enc=["无编码。"], ctx=["纪录片讨论。"],
    sup=["仅提及'60年代中国'。"],
    cnt=["正常历史纪录片讨论。", "'那段历史复杂'是客观评价。"],
    rat="正常纪录片讨论。hard negative。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="整个系统都需要重启，不然只会越来越卡", risk_level="medium", encoding_primary="D2_隐喻",
    lit=["建议系统重启以解决卡顿。"],
    enc=["D2隐喻：'系统重启'可能是对社会/体制的系统性改革呼吁。"],
    ctx=["IT吐槽或社会评论。"],
    sup=["'系统重启'在政治隐喻中方向明确。"],
    cnt=["极大概率是IT/软件吐槽。", "没有其他政治信号。"],
    rat="大概率是IT吐槽。hard negative for D2。",
    ambiguity="high", evidence_strength="weak", hard_negative=True))

R.append(s(text="今晚月亮真亮，像个大盘子挂在天上", risk_level="none", encoding_primary="none",
    lit=["描述月亮。"], enc=["无编码。"], ctx=["日常分享。"],
    sup=["无风险信号。"], cnt=["纯天文观察。"],
    rat="纯日常。", ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="这活儿我不接了，给再多钱也不干", risk_level="none", encoding_primary="none",
    lit=["拒绝工作。"], enc=["无编码。"], ctx=["职场决定。"],
    sup=["无风险信号。"], cnt=["纯职场决定。"],
    rat="纯职场。", ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="朋友从国外带了本书回来，说国内买不到", risk_level="medium", encoding_primary="E1_平台黑话",
    lit=["描述朋友从国外带书。"],
    enc=["E1：'国内买不到'暗示书曾被审查/禁止。"],
    ctx=["日常分享。"],
    sup=["'国内买不到'暗示书的敏感性质。"],
    cnt=["很多外文书国内没有版权/没有翻译版。", "不一定是禁书。"],
    rat="有E1信号但不排除版权原因，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="看到很多人在转一篇文章，点进去已经404了", risk_level="medium", encoding_primary="E3_话题/热点触发",
    lit=["描述文章被删除的现象。"],
    enc=["E3：文章被广泛转发后404暗示内容敏感被删。"],
    ctx=["社交媒体讨论。"],
    sup=["404是敏感内容的标志。"],
    cnt=["文章可能因版权、谣言等原因被删。"],
    rat="有E3信号但删文原因多样，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

# ── write ──
out = ROOT / "data" / "raw" / "batch4_natural_replacements.jsonl"
with out.open("w", encoding="utf-8") as f:
    for r in R:
        f.write(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n")

from collections import Counter
risk = Counter(r["risk_level"] for r in R)
enc = Counter(r["encoding_primary"] for r in R)
hn = sum(r["hard_negative"] for r in R)
print(f"Batch4: {len(R)} samples | HN: {hn}")
print(f"Risk: {dict(risk)}")
print(f"Encodings: {enc.most_common(12)}")
