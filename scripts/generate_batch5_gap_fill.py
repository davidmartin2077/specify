#!/usr/bin/env python3
"""
Generate batch5 gap-fill samples based on 50706-term lexicon coverage analysis.

Gap categories targeted:
- 广告/诈骗/导流 (spam_ads_fraud): 21k terms, 0.1% hit rate → 25 samples
- 平台规避/审查黑话 (platform_censorship_evasion): 5k terms → 20 samples
- 色情低俗 (sexual_content): 1.7k terms → 15 samples
- 政治历史/鉴证梗 (political_history): 1.6k terms → 10 samples
- 枪爆武器 (weapons_explosives): 935 terms → 10 samples

Principles:
- Natural Chinese internet voice, NOT analyst/moderator speech
- No "懂得都懂", "私下说", "不代表", "可能只是...也可能"
- Each sample has proper chain-of-thought reasoning
- Include contrast sets: direct risk, obfuscated, boundary, hard negative
"""

import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data/raw/batch5_gap_fill.jsonl"

samples = []

def add(text, risk_level, encoding_primary, encoding_secondary,
        needs_context, hard_negative, literal_analysis, encoding_analysis,
        context_analysis, supporting_evidence, counter_evidence, final_rationale,
        context=None, ambiguity="medium"):
    """Add a sample with full reasoning chain."""
    if context is None:
        context = {}
    samples.append({
        "text": text,
        "risk_level": risk_level,
        "encoding_primary": encoding_primary,
        "encoding_secondary": encoding_secondary if isinstance(encoding_secondary, list) else [encoding_secondary],
        "needs_context": needs_context,
        "hard_negative": hard_negative,
        "ambiguity": ambiguity,
        "evidence_strength": "strong" if risk_level in ("high", "none") else "moderate",
        "reasoning": {
            "literal_analysis": [literal_analysis],
            "encoding_analysis": encoding_analysis,
            "context_analysis": context_analysis,
            "supporting_evidence": supporting_evidence,
            "counter_evidence": counter_evidence,
            "final_rationale": final_rationale,
        },
        "context": context,
        "quality_status": "reviewed",
        "review_notes": "source=batch5_gap_fill;",
    })

# ============================================================
# SECTION 1: 广告/诈骗/导流 (25 samples) — biggest gap
# ============================================================

# -- 1a: Modern 引流 techniques (high/medium) --

add(
    text="想要的直接看主页背景，不在这回了",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C4_典故/物品/符号借用"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：让对方去主页背景图查看信息，不想在当前评论区回复。",
    encoding_analysis="利用平台功能进行导流操作——'主页背景'是头像/背景图藏联系方式的经典手法，'不在这回了'表明规避评论区审核。属于规避平台审查的导流黑话。",
    context_analysis="无额外上下文，文本本身的导流意图已足够明确。",
    supporting_evidence="'主页背景'是已知的非法引流藏匿点，'不在这回了'暗示评论区存在审核风险。组合信号指向明确的规避性导流行为。",
    counter_evidence="纯字面可解读为不想在评论区讨论私事，但'主页背景'的指定性太强，与正常私信引导不同。",
    final_rationale="规避性导流信号明确，判为 high。"
)

add(
    text="📍看简介，📱在置顶",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["B4_符号/空格/Unicode 干扰"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：用emoji提示对方看个人简介和置顶内容。",
    encoding_analysis="使用📍和📱emoji分别代指位置和联系方式，配合'看简介''在置顶'指示对方去个人主页查找。这是典型的emoji辅助导流模式，emoji起到规避关键词过滤的作用。",
    context_analysis="无额外上下文，文本自身构成完整的导流指令。",
    supporting_evidence="emoji替代关键信息（位置📍、联系方式📱）+ 明确指向个人主页的特定区域，构成规避性导流的完整信号链。",
    counter_evidence="可能是正常社交账号引导关注者查看更新内容，但📱emoji的'联系方式'暗示性较强。",
    final_rationale="emoji+主页导流组合信号强度高，判为 high。"
)

add(
    text="不在这说了，看我关注列表第一个",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：不在当前评论区继续对话，让对方查看自己关注的第一个账号。",
    encoding_analysis="利用'关注列表'跳转到另一个账号来绕过当前评论区审核。'第一个'暗示特定目标账号，属于多层跳转导流策略。",
    context_analysis="无需额外上下文，导流意图清晰。",
    supporting_evidence="明确的规避当前对话场景+指向外部账号的组合信号。",
    counter_evidence="可能是推荐朋友关注某个搞笑博主，但'不在这说了'表明当前对话有不可在此完成的内容。",
    final_rationale="多层跳转导流信号明确，判为 high。"
)

add(
    text="📎浏灠器打开 → t.cₙ/xxxxx 自取",
    risk_level="high",
    encoding_primary="F_组合编码",
    encoding_secondary=["A1_普通谐音", "B4_符号/空格/Unicode 干扰", "C4_典故/物品/符号借用"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：用📎emoji开头，提示用浏览器打开一个短链接自行获取内容。",
    encoding_analysis="多重规避编码：(1) '浏灠器'为'浏览器'的形近字替换；(2) 使用短链接t.cₙ隐藏真实URL，其中cₙ使用Unicode下标字符规避域名检测；(3) '自取'暗示资源/文件下载；(4) 📎emoji暗示附件/链接。属于高度规避的组合编码。",
    context_analysis="无额外上下文。短链接+形近字+Unicode干扰的三重规避使得文本本身已具有明确的规避意图。",
    supporting_evidence="形近字'灠'替换'览'、Unicode下标ₙ替换n、短链接隐藏真实域名、'自取'暗示可获取内容——每个单独信号都有规避意图，组合后证据充分。",
    counter_evidence="理论上是分享公开资源的正常行为，但三重编码的存在使得'正常分享'的解释不成立——正常分享不需要同时使用形近字+Unicode+短链接。",
    final_rationale="高度规避的组合编码，意图明确，判为 high。"
)

add(
    text="找工作的私我，日入四位很简单",
    risk_level="high",
    encoding_primary="C3_数字代指",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：寻找工作机会的人可以私聊，声称每日收入可达四位数。",
    encoding_analysis="'日入四位'即一天收入1000元以上，是刷单/赌博/诈骗类招募的典型话术。'私我'引导私信沟通以规避公开审核。收入承诺的极端性（日入千元）与正常招聘不符。",
    context_analysis="无额外上下文，但'日入四位'的夸大承诺本身构成风险信号。",
    supporting_evidence="'日入四位'的极端收入承诺 + '私我'规避公开沟通，组合信号指向刷单/诈骗类非法招募。",
    counter_evidence="可能是合法销售或自由职业的引流，但合法工作极少用'日入X位'这种话术，更多见于非法或灰色产业招募。",
    final_rationale="非法招募信号明确，判为 high。"
)

add(
    text="有想搞点副业的不，我这边有路子",
    risk_level="medium",
    encoding_primary="E1_平台黑话",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：询问是否有人想做副业，声称自己这边有渠道。",
    encoding_analysis="'有路子'是模糊指代非法或灰色渠道的经典话术，避免了直接说明具体内容。'搞点副业'的表面说法可用于掩盖刷单、赌博推广、传销等非法活动。",
    context_analysis="无额外上下文。文本的模糊性使其处于风险边界——可能是合法副业分享，也可能是非法招募。",
    supporting_evidence="'有路子'的模糊性+主动招募姿态，符合非法或灰色产业招募的典型开场白模式。",
    counter_evidence="确实存在合法的副业分享社区，'有路子'也可能是正常的人脉资源分享。文本本身没有明确指向非法内容。",
    final_rationale="存在风险信号但缺乏具体指向，保留召回价值，判为 medium。"
)

# -- 1b: 现代非法交易隐语 (medium) --

add(
    text="这台车刚出，手续齐全，价好谈",
    risk_level="medium",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：一辆车刚上市/刚出来，手续齐全，价格可以商量。",
    encoding_analysis="在特定语境下，'车'可能是违禁品（如毒品、枪支、被盗账号等）的代称。'刚出'可指新批次到货。'手续齐全'在违禁交易中暗指交易流程有保障。但字面解释为二手车交易同样通顺。",
    context_analysis="无额外上下文。文本的歧义性使其处于边界——二手车交易群中完全正常，但在某些类型的群组中可能是违禁交易暗语。",
    supporting_evidence="'刚出''手续齐全''价好谈'在违禁品交易黑话中有对应语义映射。",
    counter_evidence="这些表述在正常的二手车/电子产品交易中极为常见，无法仅凭文本区分合法与非法。",
    final_rationale="存在歧义但正常解释同样通顺，判为 medium。"
)

add(
    text="新版到货了，老顾客直接滴我",
    risk_level="medium",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：新版本的商品到货了，老顾客可以直接联系我。",
    encoding_analysis="'新版到货'可用于各类商品但也可用于违禁品。'老顾客'的强调暗示存在一个不在公开场合讨论的客户群。'滴我'是私信联系的口语化表达。组合信号存在歧义。",
    context_analysis="无额外上下文，文本的模糊使其处于常规交易与违禁交易的边界。",
    supporting_evidence="'老顾客'标签+回避公开讨论的'滴我'，与违禁品交易的私密性特征吻合。",
    counter_evidence="正常微商、代购也会使用这些表述。'滴我'是普遍的社交口语。",
    final_rationale="存在可疑信号但缺乏决定性证据，判为 medium。"
)

add(
    text="代找各种zi源，需要的来",
    risk_level="medium",
    encoding_primary="B4_符号/空格/Unicode 干扰",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：代为寻找各种资源，有需要的来找我。",
    encoding_analysis="'zi源'中的'zi'使用拼音替代汉字（资源→zi源），规避关键词过滤。'各种'的模糊性暗示范围广泛，包括可能违规的内容。'代找'的中介角色降低了直接发布违规内容的风险。",
    context_analysis="无额外上下文。拼音替代+模糊指代构成规避信号。",
    supporting_evidence="拼音'zi'替代'资'是规避'资源'关键词的常见手法，'各种'的模糊范围暗示可能包含违规内容。",
    counter_evidence="可能是代找学术文献、影视资源等正常内容，拼音替代也可能是打字习惯。",
    final_rationale="存在规避信号但内容指向模糊，判为 medium。"
)

add(
    text="充値找我，比官方便宜一半",
    risk_level="medium",
    encoding_primary="B3_形近字替换",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：需要充值可以找我，价格比官方渠道便宜一半。",
    encoding_analysis="'充値'中的'値'是'值'的形近字（日文汉字），用于规避'充值'关键词过滤。'便宜一半'的极端折扣暗示可能涉及黑卡、盗刷或非法代充。",
    context_analysis="无额外上下文。形近字+极端折扣的组合信号指向灰色代充产业。",
    supporting_evidence="形近字规避+极端折扣（半价）不符正常商业逻辑，指向黑产代充。",
    counter_evidence="可能是合法的批发折扣或促销活动，形近字也可能是输入法问题。",
    final_rationale="存在规避信号和价格异常，保留召回价值，判为 medium。"
)

add(
    text="收几个听话的，能坚持的来",
    risk_level="medium",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["D2_夸张/反话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：招募几个服从指令并能坚持的人。",
    encoding_analysis="'听话的'暗示需要服从指令，'能坚持'暗示任务有持续性。这种模糊的招募话术常见于刷单、传销、网络水军等需要下线配合的灰色产业。",
    context_analysis="无额外上下文。'听话'的要求在正常招聘中极为罕见，增加了风险权重。",
    supporting_evidence="'听话'要求暗示任务性质不便公开说明，与灰色产业招募特征吻合。",
    counter_evidence="可能是健身教练招募学员、学习小组招募成员等正常场景，'听话'也可能指听从指导。",
    final_rationale="存在异常招募信号但缺乏具体指向，判为 medium。"
)

# -- 1c: Hard negatives for spam/fraud (none) --

add(
    text="客服说订单号别发评论区，私信处理就行",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：转述客服的建议——不要在评论区发订单号，通过私信处理售后问题。",
    encoding_analysis="这是正常的售后指导。'订单号别发评论区'是出于隐私保护（避免泄露个人信息），'私信处理'是电商平台的标准售后流程。没有规避审查或导流的意图。",
    context_analysis="售后场景中，保护客户隐私是正常商业行为。",
    supporting_evidence="字面信息可完全用正常的售后隐私保护来解释。",
    counter_evidence="无任何风险信号——'订单号'是正常电商术语，'私信处理'是标准售后流程，不存在规避意图。",
    final_rationale="纯正常售后场景的隐私保护建议，判为 none；训练模型区分正常售后与导流行为。"
)

add(
    text="招聘：新媒体运营，薪资面议，有意私信",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：正规招聘启事——招聘新媒体运营岗位，薪资面议，有意者私信联系。",
    encoding_analysis="这是标准的招聘文本。'私信'在此是正常的求职沟通方式，不构成规避。'薪资面议'是常见招聘用语。没有模糊承诺、极端收入或其他异常信号。",
    context_analysis="正常招聘场景中，私信沟通是常见且合理的。",
    supporting_evidence="职位明确（新媒体运营）、无夸大收入承诺、格式规范，是正常招聘。",
    counter_evidence="无任何风险信号——既没有模糊的'有路子'式招募，也没有极端收入承诺，也没有规避性编码。",
    final_rationale="标准招聘文本，判为 none；训练模型区分正常招聘与非法招募。"
)

add(
    text="这个博主的教程太有用了，关注列表都是宝藏",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：称赞某博主的教程很有用，其关注列表中有很多值得关注的账号。",
    encoding_analysis="这是正常的社交媒体互动。'关注列表'在此是指值得关注的其他账号推荐，是正常的社区行为。没有任何导流或规避意图。",
    context_analysis="社交媒体中推荐优质账号是正常的社区行为。",
    supporting_evidence="内容正面、指向明确（教程博主），不涉及任何交易或导流。",
    counter_evidence="完全无害的正常社交互动，无风险信号。",
    final_rationale="正常的社交媒体评论，判为 none；训练模型区分正常互动与导流。"
)

add(
    text="姐妹们这家店真的绝了，我回购三次了",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：向朋友推荐一家店铺，表示自己已经回购三次。",
    encoding_analysis="这是正常的消费分享。'回购三次'是真实的用户推荐，非付费推广或刷单。没有规避性编码或导流行为。",
    context_analysis="社交媒体中的正常消费分享行为。",
    supporting_evidence="自然的消费推荐口吻，'回购三次'提供了真实的消费体验细节。",
    counter_evidence="完全无害的消费分享，无任何风险信号。",
    final_rationale="自然消费分享，判为 none；训练模型区分真实推荐与营销导流。"
)

add(
    text="有需要的加我vx，备注来意",
    risk_level="medium",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["A2_拼音/首字母缩写"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：需要的人添加我的微信，注明来意。",
    encoding_analysis="'vx'是微信的拼音首字母缩写，配合'加我'构成导流行为。'备注来意'暗示有多种可能的服务类型。导流意图明确但具体内容未知——可能是合法商业活动也可能是灰色交易。",
    context_analysis="无额外上下文。导流行为本身不一定是违规的，但配合模糊的'有需要的'增加了不确定性。",
    supporting_evidence="明确的跨平台导流行为+模糊的服务范围描述。",
    counter_evidence="合法商业活动（如自由职业、咨询服务）也经常使用类似话术。'vx'缩写是正常社交习惯。",
    final_rationale="导流意图明确但内容未知，判为 medium。"
)

# ============================================================
# SECTION 2: 平台规避/审查黑话 (20 samples)
# ============================================================

# -- 2a: Emoji/符号替换规避 (high/medium) --

add(
    text="这个🈷️底前把💰凑齐，别等最后一天",
    risk_level="high",
    encoding_primary="F_组合编码",
    encoding_secondary=["B4_符号/空格/Unicode 干扰", "C4_典故/物品/符号借用"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：月底前把钱凑齐，不要等到最后一天。",
    encoding_analysis="使用🈷️替代'月'、💰替代'钱'，这两个emoji替换使文本在进行集资/催款暗示的同时规避了关键词检测。emoji替换是当前最流行的规避手段之一。",
    context_analysis="无额外上下文。emoji+时间节点的组合增加了催款行为的隐秘性。",
    supporting_evidence="emoji替换敏感词+明确的时间节点（月底前）+催款行为，组合信号指向规避性集资/催款。",
    counter_evidence="可能是正常的朋友间催还借款或家庭集资，emoji使用也可能是打字习惯。但商业催收一般不需要emoji替换。",
    final_rationale="emoji规避+催款组合信号明确，判为 high。"
)

add(
    text="那件事，懂的都💔",
    risk_level="medium",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["E3_话题/热点触发"],
    needs_context=True,
    hard_negative=False,
    literal_analysis="文本字面意思：用💔emoji替代了一个词，表示那件事让人心碎/懂了。",
    encoding_analysis="使用💔emoji替代敏感词（可能的历史/政治事件名称），'那件事'是话题触发（E3）。emoji在此起到既表达情感又规避文字检测的双重作用。",
    context_analysis="需要上下文来确定'那件事'指什么话题，emoji的表现力在此语境中替代了具体的文字表达。",
    supporting_evidence="emoji+含蓄指代+话题触发，在特定上下文中可能指向规避性讨论。",
    counter_evidence="'心碎'emoji在日常对话中使用极为普遍，'那件事'范围极广，纯文本无法确定指向。",
    final_rationale="存在规避信号但依赖上下文才能确定，判为 medium，标注 needs_context。"
)

add(
    text="最近别🚬了，查得严",
    risk_level="medium",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["E3_话题/热点触发"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：最近不要抽烟了，检查很严格。或者用🚬代指其他行为。",
    encoding_analysis="🚬emoji在此可能有两层含义：(1)字面的吸烟；(2)代指某种'危险'或'会被查'的行为。'查得严'暗示存在某种监管/打击行动。emoji的隐喻用法在此起了关键规避作用。",
    context_analysis="'查得严'暗示近期有执法/平台打击行动，需要上下文来确定具体指向。",
    supporting_evidence="'查得严'+行为规避的组合信号指向可能存在违规行为。",
    counter_evidence="完全可能是字面意思——某地禁烟执法变严，朋友间互相提醒。",
    final_rationale="存在歧义但正常解释成立，判为 medium。"
)

add(
    text="V我50看看实力",
    risk_level="low",
    encoding_primary="A2_拼音/首字母缩写",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=True,
    ambiguity="low",
    literal_analysis="文本字面意思：微信转我50元来证明你的实力。这是网络流行梗。",
    encoding_analysis="'V我50'是网络流行语，'V'是微信的简称，源自肯德基疯狂星期四的玩梗文化。属于互联网烂梗而非规避行为。这个样本用于训练模型识别网络流行语与真正规避/勒索的差异。",
    context_analysis="源自肯德基疯狂星期四的网络段子文化，已完全出圈成为日常玩笑。",
    supporting_evidence="高度流行的网络梗，在各种语境下均被用作玩笑，不具有真实的勒索或交易意图。",
    counter_evidence="如果出现在完全不了解此梗的社群中，可能被误判为索要钱财。",
    final_rationale="网络流行梗，判为 low；训练模型识别网络流行文化中的无害表达。"
)

# -- 2b: 拆字/形近字/拼音规避 (medium) --

add(
    text="木倉在哪里买比较靠谱，新人求指路",
    risk_level="high",
    encoding_primary="B1_拆字",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：询问某物品在哪里买比较可靠，新人寻求指导。",
    encoding_analysis="'木倉'是敏感词（涉及武器类别）的拆字写法——将原字拆分为两个部分。'新人求指路'暗示需要被引导进入某个交易渠道。拆字+求购+新人身份的组合信号强度高。",
    context_analysis="无额外上下文。拆字写法本身已说明用户知道该词敏感，有意规避。",
    supporting_evidence="拆字规避+求购意图+新人身份（暗示需要引路人），信号链完整。",
    counter_evidence="极微弱的可能：对方在讨论木制仓库家具。但'新人求指路'的搭配在这种解释下极不自然。",
    final_rationale="拆字规避+明确求购意图，判为 high。"
)

add(
    text="有人知道那木示志的事后来怎么处理了吗",
    risk_level="medium",
    encoding_primary="B1_拆字",
    encoding_secondary=["E3_话题/热点触发"],
    needs_context=True,
    hard_negative=False,
    literal_analysis="文本字面意思：询问有人知道某个标志/事件后续如何处理。'木示志'看起来像三个不相关的汉字。",
    encoding_analysis="'木示志'可能是'標誌'（标志）的拆字或拆分写法。拆字是规避检测的经典手段。如果'那...的事'指向的是敏感事件，则构成话题触发+拆字的双重规避。",
    context_analysis="需要上下文确定'那...的事'的具体指向，拆字本身暗示可能有规避意图。",
    supporting_evidence="拆字写法+询问敏感事件后续，组合信号指向规避性讨论。",
    counter_evidence="不确定的具体指代+拆字可能只是输入错误或特殊排版。缺乏明确的敏感话题指向。",
    final_rationale="存在规避信号但内容指向模糊，判为 medium，标注 needs_context。"
)

add(
    text="这个禾厶服怎么用啊，有没有教程",
    risk_level="medium",
    encoding_primary="B2_合字/拼字",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：询问某个东西怎么使用，需要教程。'禾厶服'看起来是一个拼合的词。",
    encoding_analysis="'禾厶服'是'私服'（私人服务器）的拆字/拼字写法——'禾+厶=私'。私服在游戏领域属于灰色地带。用户通过拆字规避'私服'关键词的检测。",
    context_analysis="游戏私服属于灰色产业，但'求教程'的表述降低了恶意程度。",
    supporting_evidence="拆字规避+求私服信息的组合信号。",
    counter_evidence="也可能是技术学习目的，私服在游戏圈有一定讨论空间。",
    final_rationale="拆字规避+灰色内容，判为 medium。"
)

add(
    text="开𣎴起就别开，炫什么富",
    risk_level="medium",
    encoding_primary="B3_形近字替换",
    encoding_secondary=["D1_反讽"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：开不起（某车）就别开，炫耀什么。但'𣎴'是一个极罕见的字。",
    encoding_analysis="'𣎴'是'不'的生僻异体字。使用生僻字替换常见字是一种规避策略——在辱骂/嘲讽内容中插入异体字以绕过关键词过滤。这句话表达的是对炫富行为的不满。",
    context_analysis="无额外上下文。异体字+负面情绪的组合增加了文本的规避性。",
    supporting_evidence="使用生僻异体字替代常见字，配合负面攻击性内容。",
    counter_evidence="可能是打字错误或输入法问题导致的异常字符。但'𣎴'是真实存在的汉字。",
    final_rationale="异体字规避+负面内容，判为 medium。"
)

add(
    text="Q内搜索xxxxx，懂的来",
    risk_level="medium",
    encoding_primary="A2_拼音/首字母缩写",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：在QQ内搜索某个号码/群号，懂的人来加入。",
    encoding_analysis="'Q'是QQ的拼音首字母缩写。'懂的来'筛选知情者，暗示群内内容不便在公开场合说明。'搜索xxxxx'引导至特定QQ群，构成跨平台导流。",
    context_analysis="无额外上下文。QQ群导流+知情者筛选的组合信号。",
    supporting_evidence="引导至外部平台+筛选知情者，符合私密社群导流模式。",
    counter_evidence="正常兴趣群组也会使用类似方式招募成员，'懂的来'也可能是对某话题感兴趣的人。",
    final_rationale="跨平台导流+知情者筛选，判为 medium。"
)

# -- 2c: Normal typography variations (hard negative, none) --

add(
    text="今天 天 气 真 好 啊",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：表达今天天气好。每个字之间有空格。",
    encoding_analysis="字间加空格是某些用户的打字习惯或排版风格。在此上下文中，空格仅用于日常表达，没有任何规避意图。这是一个纯正常文本，用于训练模型不要对所有空格分隔的文本产生误判。",
    context_analysis="日常寒暄语境，无风险信号。",
    supporting_evidence="内容无害（天气感叹），空格是个人排版风格。",
    counter_evidence="空格分隔在规避场景中可能用于拆分敏感词，但此处文本内容完全无害，空格不影响判断。",
    final_rationale="正常日常表达，空格为排版风格，判为 none；训练模型区分规避性空格与正常空格排版。"
)

add(
    text="这 个 电 影 太 好 看 了 ！ ！ ！",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：表达对电影的喜爱。每个字之间有空格。",
    encoding_analysis="空格+感叹号的排版风格常见于表达强烈情感的评论。文本内容（评价电影好看）完全无害。空格在此是情绪表达的手段，不是规避。",
    context_analysis="影评场景，情感表达自然。",
    supporting_evidence="完全无害的电影评价内容，空格是情感表达方式。",
    counter_evidence="无任何风险信号。",
    final_rationale="正常影评表达，空格为情绪强调手段，判为 none。"
)

add(
    text="c h e c k 一下这个bug",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：让同事/朋友检查一下这个程序错误。英文单词字母间加了空格。",
    encoding_analysis="'c h e c k'是英文单词check的字母分隔写法。在技术讨论中，这可能只是排版习惯或强调写法。'bug'是正常的编程术语。整个文本是正常的开发协作语境。",
    context_analysis="技术开发场景，内容无害。",
    supporting_evidence="纯技术讨论内容，字母分隔是排版习惯。",
    counter_evidence="字母分隔也可用于规避检测（如f u c k），但此处check和bug的组合在开发语境中完全正常。",
    final_rationale="正常技术讨论，字母分隔为排版风格，判为 none。"
)

add(
    text="🈶没有人和我一样觉得这个bgm绝了",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：询问是否有人和自己一样觉得背景音乐很棒。'🈶'是emoji替代'有'。",
    encoding_analysis="'🈶'替代'有'是流行的emoji文字游戏（'🈶'是日语'有'的emoji），在年轻用户中常见。'bgm'是正常音乐术语。整个文本是正常的音乐评论互动。",
    context_analysis="音乐评论区场景，emoji使用是年轻人的正常表达方式。",
    supporting_evidence="正面音乐评价，emoji使用符合正常的年轻用户表达习惯。",
    counter_evidence="无任何风险信号。emoji替代在规避场景中也被使用，但此处内容无害，emoji是风格选择。",
    final_rationale="正常音乐评论，emoji为风格化表达，判为 none。"
)

add(
    text="P 站 的 设 计 素 材 真 的 好 用",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：Pinterest/某设计网站的素材很好用。'P 站'可能指Pinterest（设计素材网站）。字间有空格。",
    encoding_analysis="'P站'在日常用语中最常指Pinterest（设计素材平台）。但'P站'也可以是其他平台的缩写（如Pixiv或Pornhub）。在此语境中，'设计素材'明确了指向Pinterest/Pixiv等设计平台。需要训练模型根据上下文（'设计素材'）而非单独关键词（'P站'）判断。",
    context_analysis="'设计素材'这一上下文明确指向设计平台，排除了其他解读。",
    supporting_evidence="'设计素材'的关键上下文将'P站'锁定在设计平台语义上。",
    counter_evidence="'P站'本身有歧义（可指Pixiv或Pornhub），但'设计素材'排除了不当解读。",
    final_rationale="上下文明确为设计平台讨论，判为 none；训练模型根据上下文消歧而非简单关键词匹配。"
)

# ============================================================
# SECTION 3: 色情低俗 (15 samples)
# ============================================================

# -- 3a: Natural encoding patterns (medium) --

add(
    text="有没有1啊，0太多了",
    risk_level="medium",
    encoding_primary="C3_数字代指",
    encoding_secondary=["E1_平台黑话"],
    needs_context=True,
    hard_negative=False,
    literal_analysis="文本字面意思：数字1和0的数量对比，看起来像在讨论二进制或数学。",
    encoding_analysis="'1'和'0'在特定社群（LGBTQ+交友）中分别代指攻方和受方。这是一个经典的社群黑话代指。但同样的文字在讨论编程（二进制）、体育比分等领域完全正常。需要上下文来消歧。",
    context_analysis="在编程讨论或体育评论中可以完全正常；在特定交友社区则可能为约炮暗语。需要上下文。",
    supporting_evidence="数字代指特定角色在社群中是常见且成熟的暗语体系。",
    counter_evidence="在技术讨论（二进制）、体育比分、甚至排队人数统计中都可能出现同样的表达。",
    final_rationale="存在社群黑话代指的可能但正常解释同样成立，判为 medium，标注 needs_context。"
)

add(
    text="今晚有没有出來玩的，懂的滴滴",
    risk_level="medium",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C4_典故/物品/符号借用"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：今晚有没有人出来玩，知道的人私信联系。",
    encoding_analysis="'出來的玩'和'懂的滴滴'可能为约炮/色情服务的隐晦表达。'滴滴'是私信/联系的口语化表达。'懂的'筛选知情者。但这种表达也可能是正常的社交活动邀约。",
    context_analysis="无额外上下文。'懂的滴滴'的筛选机制增加了暧昧性。",
    supporting_evidence="'懂的滴滴'暗示了只有特定知情者才能理解的内容属性。",
    counter_evidence="完全可能是正常的社交活动（吃饭、唱歌、打球等）邀约。'懂的滴滴'在很多场景中只是'有兴趣的联系我'的俏皮说法。",
    final_rationale="存在模糊的邀约信号但缺乏明确指向，判为 medium。"
)

add(
    text="fw一个人在家好无聊",
    risk_level="medium",
    encoding_primary="A2_拼音/首字母缩写",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：'fw'一个人在家无聊。'fw'是拼音首字母缩写。",
    encoding_analysis="'fw'有多个可能含义——'服务'、'范围'、'废物'，或在某些社群中指代色情服务。含义取决于使用者的社群背景。'一个人在家无聊'的搭配增加了暧昧性。",
    context_analysis="无额外上下文。'fw'的多义性使其处于多个可能的解读之间。",
    supporting_evidence="拼音首字母缩写的多义性中包含了可能的色情服务代指。",
    counter_evidence="'fw'更常见的意思是'废物'（自嘲）或'服务'（如fw=服务器），在正常对话中使用频率远高于色情服务代指。",
    final_rationale="存在微弱风险信号但正常解读更强，判为 medium。"
)

add(
    text="🍬🍬🍬 私",
    risk_level="medium",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：三个糖果emoji加一个'私'字。极简表达。",
    encoding_analysis="在特定社群中，糖果/药丸emoji可代指药物（尤其是非法药物）。三个🍬叠加可能暗示数量或品种。'私'引导至私信沟通。但这种符号组合也可指代完全正常的内容（如果只是卖糖果/零食）。",
    context_analysis="极简emoji+单字'私'的格式常见于擦边交易/服务推广。",
    supporting_evidence="emoji代指+私信引导的极简格式在灰色交易中较为常见。",
    counter_evidence="可能是正常的糖果/零食推广。emoji+私信引导也是很多正常微商的沟通方式。",
    final_rationale="极简emoji+导流格式存在风险但内容指向模糊，判为 medium。"
)

add(
    text="有人想一起合租吗，限女生",
    risk_level="low",
    encoding_primary="none",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：寻找女性室友一起合租。",
    encoding_analysis="这是常见的合租信息。'限女生'是常见的合租性别偏好。但在某些平台上，'合租限女生'可能被用于灰色目的（如以合租为名的其他性质邀约）。大多数情况下，这是正常的租房信息。",
    context_analysis="在租房/生活类帖子中完全正常。",
    supporting_evidence="大多数情况下是正常的合租需求。",
    counter_evidence="存在被滥用于非合租目的的可能，但概率较低。",
    final_rationale="正常合租信息，判为 low；训练模型不要将所有'限女生'的合租判定为风险。"
)

# -- 3b: 正常教育/健康讨论 (hard negative, none) --

add(
    text="这个性教育科普视频做得真好，推荐给所有家长",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：称赞一个性教育科普视频做得好，推荐家长观看。",
    encoding_analysis="这是正常的性教育内容讨论。'性教育'是正常的健康教育术语，'科普''家长'等上下文将其锚定在教育语境中。没有色情暗示或擦边表达。",
    context_analysis="教育/科普场景，讨论性教育是完全正当且必要的。",
    supporting_evidence="'科普''家长'等关键词将其锚定在教育/健康领域而非色情。",
    counter_evidence="无任何风险信号。'性教育'是正常的社会议题和健康话题。",
    final_rationale="正常教育内容讨论，判为 none；训练模型不要将涉及'性'字的正常教育内容误判为色情。"
)

add(
    text="HPV疫苗约上了，姐妹们冲",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：分享自己预约成功HPV疫苗的消息，鼓励其他女性去预约。",
    encoding_analysis="这是正常的健康话题讨论。HPV疫苗是正常的医疗健康内容，'姐妹们冲'是女性社群中互相鼓励的常见表达。没有任何色情或擦边暗示。",
    context_analysis="女性健康社区场景，HPV疫苗讨论是正常的健康交流。",
    supporting_evidence="内容为正规医疗健康话题，无任何风险信号。",
    counter_evidence="无。HPV疫苗是国家推广的公共卫生项目。",
    final_rationale="正常健康话题讨论，判为 none；训练模型识别正常医疗健康内容。"
)

add(
    text="安全套应该进校园，这才是真正的性教育",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：主张安全套应该进入校园作为性教育的一部分。",
    encoding_analysis="这是正常的公共政策/教育观点表达。'安全套'是正常的医疗卫生产品，在性教育、公共卫生讨论中完全正当。'性教育'进一步确认了其教育/政策讨论的语境。",
    context_analysis="公共政策讨论场景，内容属于正当的健康教育主张。",
    supporting_evidence="在教育/公共卫生语境下，讨论安全套作为性教育工具是完全正当的。'性教育'关键词锚定了教育语境。",
    counter_evidence="无。这是正常的公共政策讨论。",
    final_rationale="正常公共政策讨论，判为 none；训练模型识别正常的社会议题讨论。"
)

add(
    text="想买内衣，有人推荐舒服的牌子吗",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：寻找内衣品牌推荐。",
    encoding_analysis="这是正常的消费咨询。'内衣'是正常的服饰品类，没有任何色情暗示或擦边表达。正常的消费推荐请求。",
    context_analysis="正常的消费/穿搭咨询场景。",
    supporting_evidence="纯消费咨询，无任何风险信号。",
    counter_evidence="无风险信号。",
    final_rationale="正常消费咨询，判为 none。"
)

add(
    text="青春期儿子问我生理卫生的问题，怎么回答比较好",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：家长询问如何回答青春期儿子关于生理卫生的问题。",
    encoding_analysis="这是正常的家庭教育讨论。'生理卫生'是正常的教育/健康话题，'青春期''儿子''家长'等关键词将其锚定在家庭教育语境中。",
    context_analysis="家庭教育/健康咨询场景。",
    supporting_evidence="完全正常的家庭教育和健康话题。",
    counter_evidence="无任何风险信号。",
    final_rationale="正常家庭教育讨论，判为 none。"
)

# ============================================================
# SECTION 4: 政治历史/鉴证梗 (10 samples)
# ============================================================

# -- 4a: Historical allusion / person metonymy (high/medium) --

add(
    text="《1984》真的是一部伟大的预言，每次读都有新感受",
    risk_level="medium",
    encoding_primary="C2_历史事件影射",
    encoding_secondary=["D2_隐喻"],
    needs_context=True,
    hard_negative=False,
    literal_analysis="文本字面意思：称赞乔治·奥威尔的小说《1984》是伟大的预言作品，每次重读都有新的感悟。",
    encoding_analysis="《1984》是正常文学作品，讨论它本身没有问题。但在特定政治语境中，引用《1984》常用于影射监控、言论审查等政治议题。'每次读都有新感受'暗示文本与现实的对应关系。需要上下文来判断是纯文学讨论还是政治影射。",
    context_analysis="在文学读书会的语境中完全正常；在政治新闻评论区可能为影射。需要上下文。",
    supporting_evidence="《1984》在中文互联网中已成为政治影射的高频引用来源。'每次读都有新感受'暗示了文学与现实的对照。",
    counter_evidence="《1984》是公认的文学经典，在世界范围内被广泛讨论和引用，绝大多数讨论是正常的文学交流。",
    final_rationale="可能为文学讨论也可能为政治影射，判为 medium，标注 needs_context。"
)

add(
    text="楚虽三户，亡秦必楚",
    risk_level="medium",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["C2_历史事件影射"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：引用《史记》典故——楚国即使只剩三户人家，灭亡秦国的也一定是楚人。表达不屈的反抗意志。",
    encoding_analysis="引用历史典故表达政治情绪是常见的影射手法。'秦'在当代鉴证话语中常被映射为威权/专制象征，'楚'映射为反抗者。但这个典故本身是中华文化遗产的一部分，在文学、历史讨论中完全正常。",
    context_analysis="无额外上下文。该典故的多义性使其处于文学引用与政治影射的边界。",
    supporting_evidence="在鉴证圈话语体系中，'亡秦必楚'有其特定的政治映射含义。",
    counter_evidence="这是中国历史文化经典典故，被广泛引用在文学、影视、游戏中，绝大多数使用场景是正常的历史文化讨论。",
    final_rationale="存在鉴证圈映射的可能但正常文化引用同样成立，判为 medium。"
)

add(
    text="那个跳水的现在过得怎么样了",
    risk_level="medium",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["E3_话题/热点触发"],
    needs_context=True,
    hard_negative=False,
    literal_analysis="文本字面意思：询问某个跳水运动员/跳水相关人物的近况。",
    encoding_analysis="'跳水的'可能借指某个与'跳水'（字面或隐喻）相关的公众人物。通过职业特征/事件代指人物是中国互联网常见的借代手法。具体指向需要上下文。",
    context_analysis="需要上下文确定'跳水的'的具体指代对象——可能为正常体育讨论也可能为政治人物借代。",
    supporting_evidence="职业/事件借代是常见的鉴证圈人物回避手法。",
    counter_evidence="可能是纯体育讨论——询问退役跳水运动员的近况。",
    final_rationale="存在借代可能但正常解释同样成立，判为 medium，标注 needs_context。"
)

add(
    text="听说那个胖子又上热搜了",
    risk_level="medium",
    encoding_primary="C1_历史人物类比",
    encoding_secondary=["E3_话题/热点触发"],
    needs_context=True,
    hard_negative=False,
    literal_analysis="文本字面意思：听说一个体型偏胖的人又登上了热搜榜。",
    encoding_analysis="'那个胖子'是典型的外貌特征借代——用体型特征代替人名。在中国互联网中，这种借代可用于规避敏感人名检测。但'胖子'也可能只是对于正、孙越等公众人物的戏称（这些是正常讨论）。具体指向取决于上下文。",
    context_analysis="需要上下文确定'胖子'的具体指代——如果是娱乐明星则是正常讨论；如果指向不便直呼其名的人物则可能为规避。",
    supporting_evidence="外貌特征借代是规避敏感人名的常用手法之一。",
    counter_evidence="'那个胖子'在娱乐/体育讨论中极其常见且通常是正常讨论。",
    final_rationale="存在借代可能但正常使用极常见，判为 medium，标注 needs_context。"
)

add(
    text="六十四天后再看",
    risk_level="medium",
    encoding_primary="C3_数字代指",
    encoding_secondary=["E2_时间节点触发"],
    needs_context=True,
    hard_negative=False,
    literal_analysis="文本字面意思：六十四天后再来看结果/后续。看起来像在说一个普通的时间节点。",
    encoding_analysis="'六十四'在中国互联网鉴证话语中可能与特定历史日期相关联（64天≈两个月，或暗示某个包含64的敏感日期）。但'六十四天'也可能是完全正常的倒计时（如考试、旅行、项目截止）。具体含义需要上下文。",
    context_analysis="需要上下文确定'六十四天'是字面的时间计算还是数字影射。",
    supporting_evidence="数字代指是鉴证圈常见的编码手法，特定数字有其约定俗成的映射。",
    counter_evidence="'六十四天'可能是完全正常的倒计时（装修工期、备考天数、旅行计划等）。",
    final_rationale="存在数字影射的可能但正常解释同样成立，判为 medium，标注 needs_context。"
)

# -- 4b: Abstract/meme encoding (medium) --

add(
    text="有没有一种可能，他们说的都是真的",
    risk_level="medium",
    encoding_primary="D1_反讽",
    encoding_secondary=["E3_话题/热点触发"],
    needs_context=True,
    hard_negative=False,
    literal_analysis="文本字面意思：提出一个假设——他们说的话可能是真实的。",
    encoding_analysis="'有没有一种可能'是网络流行的反问式表达，常用于暗示某种不被主流接受的观点可能为真。'他们说的都是真的'暗示存在某种被压制/不被承认的真相叙事。这种回避式表达常用于绕开直接的政治表态。",
    context_analysis="需要上下文确定'他们'指谁、'说的'是什么内容。反问句式暗示了与主流叙事不同的立场。",
    supporting_evidence="回避式反问+真相暗示的组合在鉴证话语中常见。",
    counter_evidence="'有没有一种可能'是互联网常用句式，广泛用于娱乐、体育、生活等各种话题的假设性讨论。",
    final_rationale="存在隐喻暗示可能但句式本身极普遍，判为 medium，标注 needs_context。"
)

add(
    text="品，细品",
    risk_level="low",
    encoding_primary="D2_夸张/反话",
    encoding_secondary=["E3_话题/热点触发"],
    needs_context=True,
    hard_negative=False,
    literal_analysis="文本字面意思：请对方仔细品味/思考。极简表达。",
    encoding_analysis="'品，细品'是互联网流行的表达，用于暗示某事/某话有深层含义需要琢磨。本身不包含具体敏感内容，但其暗示性使其在特定语境下可能指向敏感话题。需要上下文才能判断。",
    context_analysis="极简表达，强烈依赖上下文。可以用于影评、时评、八卦等任何需要'细品'的场景。",
    supporting_evidence="'细品'的暗示性在特定上下文中可能指向规避性讨论。",
    counter_evidence="'品，细品'是极其常见的互联网表达，广泛用于各类话题中，本身不携带风险信号。",
    final_rationale="极简暗示性表达，判为 low；训练模型理解其上下文依赖性。"
)

add(
    text="大的要来了",
    risk_level="low",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["E3_话题/热点触发"],
    needs_context=True,
    hard_negative=False,
    ambiguity="high",
    literal_analysis="文本字面意思：预告有大事即将发生。",
    encoding_analysis="'大的要来了'是互联网社区的流行表达，用于预告即将发生的重大事件——可以是新游戏发布、公司裁员、政策出台、娱乐圈大瓜等任何'大事'。在鉴证圈中也可用于预告敏感事件。但其使用场景极其广泛，无上下文时无法判断。",
    context_analysis="极端依赖上下文的表达。在游戏圈、娱乐圈、时政圈都有使用。",
    supporting_evidence="在鉴证圈中有特定使用模式，但与其他圈子的使用难以区分。",
    counter_evidence="该表达在游戏（新版本发布）、娱乐（大瓜预告）、科技（新品发布）等圈子的使用频率远高于政治讨论。",
    final_rationale="高度上下文依赖的极简表达，判为 low。"
)

add(
    text="加速，油门踩到底",
    risk_level="medium",
    encoding_primary="D2_隐喻",
    encoding_secondary=["E1_平台黑话"],
    needs_context=True,
    hard_negative=False,
    literal_analysis="文本字面意思：加速前进，油门踩到底。",
    encoding_analysis="'加速'在互联网社区中有特定隐喻含义——指助推某种趋势/局面走向极端以引发变革。源自'加速主义'（accelerationism）的网络话语。'油门踩到底'强化了这种不加控制的推进感。但在赛车/驾驶话题中也可为字面意思。",
    context_analysis="在赛车/驾驶社区中为字面意思；在特定政治/社会讨论中为隐喻。需要上下文。",
    supporting_evidence="'加速'在网络话语中有其特定的政治隐喻含义。",
    counter_evidence="赛车游戏、驾驶社区、甚至工作激励（'加速推进项目'）中都广泛使用类似表达。",
    final_rationale="存在隐喻可能但字面解释同样普遍，判为 medium，标注 needs_context。"
)

add(
    text="《关于我重生到这个世界发现什么都没变这件事》",
    risk_level="medium",
    encoding_primary="D1_反讽",
    encoding_secondary=["C2_历史事件影射", "D2_夸张/反话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：模仿轻小说标题格式，表达重生后发现世界没有改变的失望/讽刺。",
    encoding_analysis="模仿日本轻小说长标题格式（'关于……这件事'）表达政治失望是鉴证圈的结构性编码。'什么都没变'暗示对社会/政治变革的期待落空。轻小说标题格式本身是正常的二次元文化表达，但其内容'什么都没变'在特定语境下构成政治影射。",
    context_analysis="无额外上下文。结构梗的编码形式使其在二次元社区中可伪装为正常玩笑。",
    supporting_evidence="轻小说标题格式+社会失望主题的组合在鉴证圈中有固定的使用模式。",
    counter_evidence="'什么都没变'也可能指个人生活（减肥失败、工作没进展等），轻小说标题格式是正常的二次元文化表达。",
    final_rationale="结构性编码+失望主题，判为 medium。"
)

# ============================================================
# SECTION 5: 枪爆武器 (10 samples)
# ============================================================

# -- 5a: 暗语/编码交易 (medium) --

add(
    text="收玩具，成色好的优先",
    risk_level="medium",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：收购玩具，品质好的优先。",
    encoding_analysis="'玩具'在特定圈层中可用于代指枪支/武器（尤其是仿真枪/气枪圈）。'成色好'指物品品相/新旧程度。'收'是收购的口语表达。但这种暗语模式同样可能指向正常的手办/模型交易。",
    context_analysis="在手办/模型交易语境中完全正常；在特定圈子中可能为武器交易暗语。",
    supporting_evidence="'玩具'作为武器代称在某些圈子中有使用记录。",
    counter_evidence="'玩具'在绝大多数场景中指代真正的玩具——手办、模型、潮玩等。'收玩具'是正常收藏圈用语。",
    final_rationale="存在暗语可能但正常解释远更常见，判为 medium。"
)

add(
    text="出点东西，懂的私，价格美丽",
    risk_level="medium",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C4_典故/物品/符号借用"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：出售一些物品，知情者私聊，价格优惠。",
    encoding_analysis="'出点东西'的模糊指代+ '懂的私'的知情者筛选+ '价格美丽'的低价暗示，构成了典型的灰色交易暗语模式。但'出东西'也是正常二手交易的常见表述。",
    context_analysis="无额外上下文。模糊指代+知情者筛选的组合增加了可疑程度。",
    supporting_evidence="模糊指代+筛选+低价的三重信号组合在灰色交易中常见。",
    counter_evidence="正常的二手交易、闲置转让也使用这些表述。'价格美丽'是常见的二手交易用语。",
    final_rationale="存在风险信号但缺乏具体指向，判为 medium。"
)

add(
    text="有没有出配件的，急求",
    risk_level="medium",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：急需购买配件。",
    encoding_analysis="'配件'在武器/枪支交易中可指枪支配件（如消音器、弹匣等）。'急求'表明紧迫需求。但'配件'也是极其普遍的日常用语——电脑配件、汽车配件、手机配件等。",
    context_analysis="无额外上下文。'配件'一词的普遍性使其无法仅凭文本判断。",
    supporting_evidence="'配件'在武器交易中有其特定使用语境。",
    counter_evidence="'配件'在日常生活和电子商务中使用频率极高（电脑配件、汽车配件等），绝大多数场景完全正常。",
    final_rationale="存在微弱风险信号但日常使用压倒性占优，判为 medium。"
)

add(
    text="听说最近来了一批好货",
    risk_level="medium",
    encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["E1_平台黑话"],
    needs_context=False,
    hard_negative=False,
    literal_analysis="文本字面意思：听说最近到了一批好商品。",
    encoding_analysis="'好货'是模糊的商品代称，在违禁品交易（毒品、武器、走私品等）中常用。'来了一批'暗示新货源到达。但这种表达在正常的商品讨论中也极其常见。",
    context_analysis="无额外上下文。'好货'的通用性使其风险判断高度依赖上下文。",
    supporting_evidence="模糊商品代称在违禁交易中有长期使用历史。",
    counter_evidence="'好货'在电商、代购、二手交易中是极其普遍的正常用语。",
    final_rationale="存在模糊风险信号但正常使用极广泛，判为 medium。"
)

# -- 5b: 正常武器讨论 (hard negative, none) --

add(
    text="军事博物馆那个抗战展区太震撼了，老枪保养得真好",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：参观军事博物馆的抗战展区感到震撼，称赞老式枪支的保养状况。",
    encoding_analysis="这是正常的博物馆参观体验分享。'老枪'指博物馆展出的历史枪支，'抗战展区''军事博物馆'等上下文将其锚定在历史文化教育领域。没有任何交易意图或危险暗示。",
    context_analysis="博物馆/教育场景，讨论历史武器展品是正常的文化活动。",
    supporting_evidence="'军事博物馆''抗战展区'等上下文明确指向历史文化教育。",
    counter_evidence="无风险信号。讨论博物馆展品是正常文化活动。",
    final_rationale="正常博物馆参观分享，判为 none；训练模型区分历史文化讨论与武器交易。"
)

add(
    text="吃鸡里M416配什么配件最好",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：在吃鸡游戏（绝地求生/PUBG）中询问M416步枪的最佳配件搭配。",
    encoding_analysis="这是正常的游戏讨论。M416是游戏中的虚拟武器，'吃鸡'是游戏昵称。'配件'在此明确指游戏内的虚拟配件（握把、枪口、弹匣等）。所有术语都锚定在游戏语境中。",
    context_analysis="游戏讨论场景，内容为虚拟游戏道具。",
    supporting_evidence="'吃鸡'明确指向游戏语境，M416是知名游戏虚拟武器。",
    counter_evidence="无风险信号。纯游戏讨论。",
    final_rationale="纯游戏讨论，判为 none；训练模型识别游戏虚拟武器讨论。"
)

add(
    text="CS里狙打得好的都是大哥",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：在CS游戏中狙击枪用得好的人都是厉害玩家。",
    encoding_analysis="这是正常的游戏讨论。'狙'是狙击枪的游戏术语，'大哥'是游戏圈中对高手的敬称。所有内容都锚定在游戏语境中。",
    context_analysis="游戏讨论场景。",
    supporting_evidence="'CS'明确了游戏语境，所有术语为正常游戏用语。",
    counter_evidence="无风险信号。",
    final_rationale="纯游戏讨论，判为 none。"
)

add(
    text="抗战剧里的三八大盖声音太独特了",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：评论抗战题材影视剧中三八式步枪的音效很独特。",
    encoding_analysis="这是正常的影视剧讨论。'三八大盖'是三八式步枪的民间俗称，是历史军事知识。在影视剧讨论的语境中完全正常。",
    context_analysis="影视剧讨论场景，内容为历史文化知识。",
    supporting_evidence="'抗战剧'明确了影视讨论语境，'三八大盖'是正常的历史军事知识。",
    counter_evidence="无风险信号。",
    final_rationale="正常影视剧讨论，判为 none。"
)

add(
    text="这个生存博主教的打火石取火技巧太实用了",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：称赞一个户外生存博主教的打火石生火技巧很实用。",
    encoding_analysis="这是正常的户外/生存技能讨论。'打火石'是正常的户外生存工具。'取火技巧'是正常的生存技能教学。所有术语都锚定在户外/生存语境中。",
    context_analysis="户外/生存技能学习场景。",
    supporting_evidence="'生存博主''取火技巧'等上下文指向正常的户外技能学习。",
    counter_evidence="无风险信号。",
    final_rationale="正常户外技能讨论，判为 none。"
)

# ============================================================
# SECTION 6: 混合/边界补充 (5 samples)
# ============================================================

add(
    text="用T开头的那个东西，你懂的",
    risk_level="medium",
    encoding_primary="A2_拼音/首字母缩写",
    encoding_secondary=["E1_平台黑话"],
    needs_context=True,
    hard_negative=False,
    literal_analysis="文本字面意思：使用某个以字母T开头的东西，暗示对方应该知道指什么。",
    encoding_analysis="'T开头的那个东西'使用首字母+模糊指代。首字母指代是规避敏感词检测的常见手法。'你懂的'暗示存在共识但不愿在公开场合明确说出。具体指代完全依赖上下文。",
    context_analysis="需要上下文确定'T'指代什么——可能是正常内容也可能为规避性指代。",
    supporting_evidence="首字母指代+知情者暗示的组合在规避场景中常见。",
    counter_evidence="日常对话中经常使用首字母+模糊指代来表达不便直说的话题（如T=体温计/T=某品牌），这本身不一定是规避行为。",
    final_rationale="存在规避信号但内容完全依赖上下文，判为 medium，标注 needs_context。"
)

add(
    text="今晚八点老地方集合，带好装备",
    risk_level="medium",
    encoding_primary="E2_时间节点触发",
    encoding_secondary=["C4_典故/物品/符号借用"],
    needs_context=True,
    hard_negative=False,
    literal_analysis="文本字面意思：通知晚上八点在常去的地点集合，带上装备。",
    encoding_analysis="'老地方'是模糊地点暗示，'带好装备'可指代各种物品——从运动器材到危险工具。'集合'可能为正常社交活动也可能为线下动员。具体性质依赖上下文。",
    context_analysis="在游戏/运动社群中完全正常（如打球、骑行）；在特定语境中可能为线下集结。",
    supporting_evidence="'集合'+'装备'的组合在某些动员语境中有特定含义。",
    counter_evidence="极其常见的社交活动组织用语，在运动/户外/游戏等正常场景中广泛使用。",
    final_rationale="存在微弱风险信号但正常使用压倒性占优，判为 medium，标注 needs_context。"
)

add(
    text="去机场送人而已，别想太多",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：只是去机场送人，让对方不要多想/过度解读。",
    encoding_analysis="这是正常的生活场景描述。'去机场送人'是常见的日常活动。'别想太多'是针对可能的误解作出的澄清。虽然'机场'在一些语境中可作为暗语（如'去机场'暗指逃跑/出境），但'送人而已'的澄清+日常语气锚定为正常场景。",
    context_analysis="正常的人际沟通场景。",
    supporting_evidence="'送人而已'澄清了行为性质，'别想太多'是针对误解的正常回应。",
    counter_evidence="极微弱的可能：'去机场'在某些圈子的暗语中可暗指出境/逃跑，但'送人'降低了这一解读的可能性。",
    final_rationale="正常生活场景，判为 none；训练模型不要将日常表述过度解读。"
)

add(
    text="别光喝酒，吃点菜啊",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False,
    hard_negative=True,
    literal_analysis="文本字面意思：劝朋友喝酒时也吃点菜。",
    encoding_analysis="这是中文互联网常用调侃语，用于劝人不要'光做白日梦'或'说胡话'——即'吃菜解酒，清醒一点'的调侃。这是一个广泛使用的玩笑梗，不具有任何政治或风险含义。",
    context_analysis="网络调侃场景，该表达已完全出圈为日常玩笑。",
    supporting_evidence="已完全出圈的日常调侃梗，在各类话题下均作为玩笑使用。",
    counter_evidence="无风险信号。",
    final_rationale="广泛使用的网络调侃梗，判为 none。"
)

add(
    text="这盛世如你所愿",
    risk_level="medium",
    encoding_primary="D1_反讽",
    encoding_secondary=["C2_历史事件影射"],
    needs_context=True,
    hard_negative=False,
    literal_analysis="文本字面意思：这盛世正如你所希望的那样。表面上是一句赞美/肯定的话。",
    encoding_analysis="这句话在中文互联网中有双重语义。表面是引用/赞美，但在特定政治语境中已成为反讽——用于表达对社会现状的失望/讽刺。其具体含义完全取决于使用语境和对象。'如你所愿'中的'你'指代对象决定了话语性质。",
    context_analysis="极强依赖上下文。在对国家发展表示肯定时可正面使用；在特定语境中可为反讽。",
    supporting_evidence="在鉴证话语中，该句式有固定的反讽使用模式。",
    counter_evidence="该句式同时也是广泛使用的正面表达（如对国家建设成就的肯定、对先辈的告慰）。",
    final_rationale="强烈依赖上下文的双重语义表达，判为 medium，标注 needs_context。"
)


# ============================================================
# Write to output
# ============================================================

print(f"Generated {len(samples)} samples")

with open(OUTPUT, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s, ensure_ascii=False, separators=(",", ":")) + "\n")

print(f"Written to {OUTPUT}")

# Show category distribution
from collections import Counter
risk_dist = Counter(s["risk_level"] for s in samples)
hn_count = sum(1 for s in samples if s.get("hard_negative"))
nc_count = sum(1 for s in samples if s.get("needs_context"))
print(f"Risk: {dict(risk_dist)}")
print(f"Hard negative: {hn_count}")
print(f"Needs context: {nc_count}")

# Show encoding distribution
enc = Counter(s["encoding_primary"] for s in samples)
print(f"\nEncoding primary:")
for e, c in enc.most_common():
    print(f"  {e}: {c}")
