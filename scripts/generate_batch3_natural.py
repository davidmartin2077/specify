#!/usr/bin/env python3
"""Batch 3: Replace gemini_expansion samples. Focus on LOW boundary cases,
underrepresented encodings (B1 B3 A3 C5 E4), and balanced distribution."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH = "batch3_natural"
_id = 0


def s(**kw):
    global _id
    _id += 1
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
    kw["context"] = {
        "title": kw.pop("ctx_title", ""),
        "description": "",
        "time": "",
        "topic": kw.pop("ctx_topic", ""),
    }
    kw["reasoning"] = {
        "literal_analysis": kw.pop("lit"),
        "encoding_analysis": kw.pop("enc"),
        "context_analysis": kw.pop("ctx"),
        "supporting_evidence": kw.pop("sup"),
        "counter_evidence": kw.pop("cnt"),
        "final_rationale": kw.pop("rat"),
    }
    kw["quality_status"] = "approved"
    kw["review_notes"] = f"source={BATCH}; replaces old synthetic"
    if kw.get("needs_context") and not kw["context"]["title"]:
        kw["needs_context"] = False
    return kw


R = []

# ═══════════════════════════════════════════════════════════════
# HIGH (30)
# ═══════════════════════════════════════════════════════════════

# --- C1 ---
R.append(s(text="王安石变法的失败，本质上是触动利益集团太多", risk_level="high",
    encoding_primary="C1_历史人物类比", ctx_topic="历史/政治讨论",
    lit=["讨论北宋王安石变法的失败原因。"],
    enc=["C1类比：王安石=锐意改革的决策者，'触动利益集团'=改革遭遇体制阻力。在简中鉴证圈中高度固化。"],
    ctx=["不需外部上下文，王安石变法的类比方向在中文互联网有共识。"],
    sup=["王安石是一个极高频的借古讽今载体。", "'触动利益集团'这种现代政治学术语暴露了现实映射意图。"],
    cnt=["纯历史学术讨论确实可能。", "但'利益集团'是现代政治学术语而非宋史语境用词。"],
    rat="王安石+利益集团组合暴露了强烈的现实政治映射，判high。",
    ambiguity="low", evidence_strength="strong"))

R.append(s(text="项羽不肯过江东，不是因为傻，是因为看透了", risk_level="high",
    encoding_primary="C1_历史人物类比", ctx_topic="历史/政治讨论",
    lit=["讨论项羽自刎乌江的原因。"],
    enc=["C1类比：项羽=面临绝境的政治人物，'不过江东'=不回头的决绝，'看透了'=认清了局势本质。"],
    ctx=["在特定政治节点上，项羽+看透了的组合有强烈现实映射。"],
    sup=["项羽在政治隐喻中常代表失败的理想主义者或被迫出局的决策者。", "'看透了'的三字概括引发对现实的联想。"],
    cnt=["单纯诗词赏析或历史感慨。"],
    rat="项羽+看透了是鉴证圈固定隐喻组合，方向明确，判high。",
    ambiguity="low", evidence_strength="strong"))

# --- C2 ---
R.append(s(text="柏林墙倒了三十多年了，有些墙反而越砌越高", risk_level="high",
    encoding_primary="C2_历史事件影射", encoding_secondary=["D2_隐喻"],
    lit=["比较柏林墙倒塌与当下某'墙'的增高。"],
    enc=["C2影射+D2隐喻：用柏林墙的历史事件影射当下的信息/言论壁垒。", "'有些墙'用的是模糊化+共识认领。"],
    ctx=["柏林墙在中文互联网政治讨论中是高度敏感的比较框架。"],
    sup=["柏林墙的比较暗示了对信息管控的批评。", "'越砌越高'增强了比较的负面判断。"],
    cnt=["可能是讨论物理围墙、物业围墙。", "但和柏林墙这组比较中，物理围墙的概率极低。"],
    rat="柏林墙比较框架是高度固化的C2模式，'越砌越高'强化了现实映射，判high。",
    ambiguity="low", evidence_strength="strong"))

R.append(s(text="切尔诺贝利不是事故，是体制问题", risk_level="high",
    encoding_primary="C2_历史事件影射", ctx_topic="历史/政治讨论",
    lit=["讨论切尔诺贝利核事故的根源。"],
    enc=["C2影射：切尔诺贝利=体制性失败的典型符号。", "表面讨论苏联历史，实际映射对体制的批评。"],
    ctx=["'不是事故是体制问题'的句式是固定政治批判框架。"],
    sup=["切尔诺贝利在当代政治讨论中是'体制失败'的符号化代指。", "句式本身是经典的政治批判模板。"],
    cnt=["可以是HBO剧集的观后感。", "但'体制问题'的措辞超出了影评范畴。"],
    rat="切尔诺贝利+体制问题的政治批判框架明确，判high。",
    ambiguity="low", evidence_strength="strong"))

# --- C4 ---
R.append(s(text="和平演变不是阴谋论，是正在进行时", risk_level="high",
    encoding_primary="C4_典故/物品/符号借用", ctx_topic="政治讨论",
    lit=["断言和平演变是真实发生中的过程。"],
    enc=["C4：'和平演变'本身是冷战政治术语，在当代中文互联网中用于描述西方的文化/价值观渗透。"],
    ctx=["在中文互联网政治讨论中'和平演变'有固定使用场景和指涉。"],
    sup=["该术语在中文政治讨论中方向明确。", "'正在进行时'暗示了紧迫性和现实指涉。"],
    cnt=["可以是纯粹的历史/政治学术讨论。"],
    rat="和平演变+正在进行时的政治断言框架明确，判high。",
    ambiguity="low", evidence_strength="strong"))

R.append(s(text="有些口号喊了几十年，仔细想想什么都没变", risk_level="high",
    encoding_primary="D1_反讽", encoding_secondary=["C4_典故/物品/符号借用"],
    lit=["评论某些长期口号的效果。"],
    enc=["D1反讽+C4：用'喊口号'暗示政治宣传，'什么都没变'暗指体制未改。"],
    ctx=["'喊了几十年的口号'在当代中文互联网有明确的指涉方向。"],
    sup=["对'几十年不变的口号'的批评是固定政治隐喻。", "'什么都没变'的断言是负面判断。"],
    cnt=["可以是讨论公司文化、教育口号等非政治场景。"],
    rat="口号+什么都没变的政治批评方向明确，判high。",
    ambiguity="low", evidence_strength="strong"))

# --- D1 ---
R.append(s(text="新闻里说人民生活水平持续提高，我看着工资条笑了", risk_level="high",
    encoding_primary="D1_反讽", ctx_topic="社会/经济讨论",
    lit=["表面说看到新闻对生活的正面报道后笑了。"],
    enc=["D1反讽：新闻报喜+个人现实(工资条)的强烈对比制造反讽。", "'笑了'不是开心，是苦笑/嘲讽。"],
    ctx=["这种'新闻说X，我工资条说Y'的比较是固定的互联网反讽模板。"],
    sup=["官方叙事与个人体验的对比是简中互联网经典反讽模式。", "'笑了'在此语境中明确的负面含义。"],
    cnt=["可以是真心觉得新闻幽默。", "但工资条+笑的组合在当代互联网中几乎反讽是默认解读。"],
    rat="经典工资条反讽模板，指向明确，判high。",
    ambiguity="low", evidence_strength="strong"))

# --- D2 ---
R.append(s(text="导航一直在说前方畅通，但周围的车都停着不动", risk_level="high",
    encoding_primary="D2_隐喻", ctx_topic="社会评论",
    lit=["描述导航提示与实际情况的矛盾。"],
    enc=["D2隐喻：导航=官方信息/宣传，'周围车都不动'=真实情况与宣传严重不符。"],
    ctx=["这种导航vs现实的隐喻在简中互联网已有固化理解。"],
    sup=["完整隐喻叙事：官方信息说畅通但实际停滞。", "映射方向明确。"],
    cnt=["可以是真实堵车吐槽。", "但叙事完整度和象征性使普通吐槽概率降低。"],
    rat="导航vs现实的隐喻叙事完整，政治映射方向明确，判high。",
    ambiguity="low", evidence_strength="strong"))

# --- F ---
R.append(s(text="外面的声音越来越听不到了，信号好像被什么东西挡住了", risk_level="high",
    encoding_primary="F_组合编码", encoding_secondary=["D2_隐喻", "E1_平台黑话"],
    lit=["抱怨信号不好收不到外面的声音。"],
    enc=["F组合：'外面的声音'=外部信息/观点，'信号被挡'=信息封锁。", "D2隐喻+E1平台黑话叠加。"],
    ctx=["在讨论网络封锁时该隐喻方向明确。"],
    sup=["完整的'外部信号被阻断'隐喻。", "是简中互联网讨论信息管控的经典框架。"],
    cnt=["可以是真实吐槽WiFi/手机信号差。"],
    rat="双重编码+'外面的声音'隐喻方向明确，判high。",
    ambiguity="low", evidence_strength="strong"))

R.append(s(text="已经被夹了三条了，这条换个说法试试", risk_level="high",
    encoding_primary="F_组合编码", encoding_secondary=["E1_平台黑话"],
    lit=["说明之前的评论被删，这次改表述再发。"],
    enc=["F+E1：'被夹'=被审核删除（微博黑话），'换个说法试试'=意图规避审核。"],
    ctx=["微博用户对'夹'有共识。"],
    sup=["'夹'是微博最经典的内容删除黑话。", "连续被夹+换说法表明用户在对抗审核。"],
    cnt=["可能是广告或垃圾信息被删。", "但'夹'的特定用语通常指敏感政治内容。"],
    rat="微博经典被夹+规避行为的强组合，判high。",
    ambiguity="low", evidence_strength="strong"))

# --- C3 ---
R.append(s(text="那年六月的事，现在还有人记得吗", risk_level="high",
    encoding_primary="C3_数字代指", encoding_secondary=["E2_时间节点触发"],
    lit=["询问是否还有人记得某个六月份的事件。"],
    enc=["C3+E2：'那年六月'是模糊化但指向明确的日期代指。", "疑问句式唤起共同记忆。"],
    ctx=["在中文互联网中'六月'有非常具体且固化的代指方向。"],
    sup=["'六月'+'那年'的组合在中文互联网中有高度固化指向。", "疑问句式的唤起意图明确。"],
    cnt=["可以是任何六月份的事件（毕业季、世界杯等）。"],
    rat="六月在中文互联网中的固化代指方向明确，判high。",
    ambiguity="low", evidence_strength="strong"))

# ═══════════════════════════════════════════════════════════════
# LOW (35) — boundary cases, the hardest to get right
# ═══════════════════════════════════════════════════════════════

# --- 边界历史讨论 ---
R.append(s(text="研究了一下崇祯的性格，感觉他本质上是个好人，就是命不好", risk_level="low",
    encoding_primary="C1_历史人物类比", ctx_topic="历史讨论",
    lit=["对崇祯帝的性格做个人评价。"],
    enc=["C1微弱：历史人物性格评价在特定语境下可能有类比意图，但此处更像普通历史讨论。"],
    ctx=["明史爱好者常见讨论内容。"],
    sup=["有微弱的历史人物类比可能。"],
    cnt=["完整的个人历史观点表达。", "'好人+命不好'是常见的历史抒情而非政治隐射。"],
    rat="大概率是普通历史爱好者讨论，微弱类比可能不足以升风险，判low。hard negative for C1。",
    ambiguity="high", evidence_strength="weak", hard_negative=True))

R.append(s(text="最近在看《大秦帝国》，里面的制度设计很有意思", risk_level="low",
    encoding_primary="C1_历史人物类比", ctx_topic="历史/影视讨论",
    lit=["分享看历史剧的感受。"],
    enc=["C1微弱：《大秦帝国》在政治隐射讨论中时有出现，但此处仅是普通观剧感受。"],
    ctx=["影视/阅读分享的正常语境。"],
    sup=["仅提及'大秦帝国'有微弱联想可能。"],
    cnt=["正常的影视剧观后感。", "没有映射现实的信号。", "'制度设计有意思'是正常历史讨论。"],
    rat="正常历史剧观后感。hard negative for C1。",
    ambiguity="high", evidence_strength="weak", hard_negative=True))

# --- 边界反讽 ---
R.append(s(text="我们这的公共服务真是越来越好了，好到我都不好意思用", risk_level="low",
    encoding_primary="D1_反讽",
    lit=["表面夸奖公共服务，实际最后一句暴露反讽。"],
    enc=["D1反讽微弱：'好到我都不好意思用'暗示服务实际不可用。", "但语气更接近日常吐槽而非政治指向。"],
    ctx=["日常吐槽语境。"],
    sup=["存在反讽句式。"],
    cnt=["典型的日常吐槽，没有政治指向。", "吐槽公共服务质量是常见生活分享。"],
    rat="日常吐槽，反讽目标是公共服务质量而非政治，判low。",
    ambiguity="high", evidence_strength="weak", hard_negative=True))

# --- 边界代指 ---
R.append(s(text="某些地方的规定真的很迷，但不敢说太细", risk_level="low",
    encoding_primary="E1_平台黑话",
    lit=["模糊地抱怨某些规定。"],
    enc=["'不敢说太细'有微弱的自我审查信号。", "但整体是模糊的日常抱怨。"],
    ctx=["日常吐槽。"],
    sup=["'不敢说太细'暗示了信息敏感性。"],
    cnt=["极模糊的表达，可能是任何规定（公司制度、小区规则等）。", "没有具体指涉方向。"],
    rat="模糊的日常抱怨，微弱编码信号不足以升风险，判low。",
    ambiguity="high", evidence_strength="weak"))

# --- 边界拼音 ---
R.append(s(text="最近在看一些海外的zhengzhi节目，感觉观点挺不一样的", risk_level="low",
    encoding_primary="A2_拼音/首字母缩写",
    lit=["分享观看海外政治节目的感受。"],
    enc=["A2微弱：'zhengzhi'用了拼音可能是规避，也可能是打字习惯。"],
    ctx=["日常内容分享。"],
    sup=["拼音替代可能是有意规避。"],
    cnt=["完全可能是打字习惯或输入法问题。", "海外政治节目本身不是敏感内容。"],
    rat="拼音使用可能只是打字习惯，整体语境无风险，判low。",
    ambiguity="high", evidence_strength="weak", hard_negative=True))

# --- 边界隐喻 ---
R.append(s(text="这趟车坐得太久了，想下去走走透透气", risk_level="low",
    encoding_primary="D2_隐喻",
    lit=["表达旅途疲劳想下车走走。"],
    enc=["D2微弱：'坐车太久想下去'在特定讨论中可能是政治隐喻。", "但旅行/通勤吐槽太常见了。"],
    ctx=["日常旅行分享。"],
    sup=["有微弱的隐喻可能。"],
    cnt=["完整的旅行吐槽语境。", "日常通勤中这种表达极其普遍。"],
    rat="大概率是真实旅行/通勤吐槽。hard negative for D2。",
    ambiguity="high", evidence_strength="weak", hard_negative=True))

# --- 更多边界样本 ---
R.append(s(text="这制度设计得确实精妙，一环扣一环，就是执行起来总变味", risk_level="low",
    encoding_primary="C1_历史人物类比",
    lit=["评价某制度的精巧设计但执行走样。"],
    enc=["微弱编码可能：对制度的批评可能映射现实。", "但无具体指涉。"],
    ctx=["可能是公司制度、社区规则等讨论。"],
    sup=["对制度的批评有微弱政治联想。"],
    cnt=["极大概率是公司/学校/社区制度吐槽。", "无政治指向。"],
    rat="日常制度吐槽。hard negative。",
    ambiguity="high", evidence_strength="weak", hard_negative=True))

R.append(s(text="听某位教授讲了一堂中国现代史，收获很大", risk_level="low",
    encoding_primary="none",
    lit=["分享听现代史课程的收获。"],
    enc=["无编码。正常学习分享。"],
    ctx=["学术/教育语境。"],
    sup=["'中国现代史'在特定上下文中可能触及敏感领域。"],
    cnt=["纯粹的学习经历分享。", "正面表达（收获很大）。", "学术语境完全正常。"],
    rat="正常学习分享。hard negative：训练模型不要因'现代史'关键词联想。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="小区业主群又在讨论物业费的事了，每次都很激烈", risk_level="low",
    encoding_primary="none",
    lit=["描述业主群对物业费的激烈讨论。"],
    enc=["无编码。日常社区讨论。"],
    ctx=["社区生活。"],
    sup=["无风险信号。"],
    cnt=["纯粹的社区生活讨论。"],
    rat="纯社区生活。hard negative。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

# ═══════════════════════════════════════════════════════════════
# MEDIUM (25) — authentic ambiguity
# ═══════════════════════════════════════════════════════════════

R.append(s(text="小隐隐于野，中隐隐于市，大隐隐于朝", risk_level="medium",
    encoding_primary="C1_历史人物类比", encoding_secondary=["C4_典故/物品/符号借用"],
    lit=["引用古代隐士格言。"],
    enc=["C1+C4：'隐于朝'在当代互联网讨论中常指在体制内保持沉默/隐藏真实立场。"],
    ctx=["在特定政治讨论下风险升级。裸文本为medium。"],
    sup=["古语在当代鉴证圈被赋予了新的政治含义。"],
    cnt=["纯粹的古文欣赏或人生感悟。", "没有上下文时的默认解读权重不低。"],
    rat="有编码可能但古文欣赏解释也合理，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="只许州官放火，不许百姓点灯", risk_level="medium",
    encoding_primary="C1_历史人物类比", encoding_secondary=["C4_典故/物品/符号借用"],
    lit=["引用俗语表达对双重标准的不满。"],
    enc=["C1+C4：这句俗语在简中互联网常用于影射体制内外的双重标准。"],
    ctx=["可出现在多种语境下，从公司管理到政治批评。"],
    sup=["是高频政治隐喻引用。"],
    cnt=["公司管理、学校规则等非政治场景也常使用。"],
    rat="高频引用但有广泛的非政治使用场景，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="有人在上游倒垃圾，整条河都脏了", risk_level="medium",
    encoding_primary="D2_隐喻", ctx_topic="社会评论",
    lit=["描述河流被上游污染。"],
    enc=["D2隐喻可能：上游=上级/上层，垃圾=不良政策/行为，整条河脏了=全社会受影响。"],
    ctx=["环境讨论中完全正常；社会讨论中可能隐喻。"],
    sup=["完整的环境→社会隐喻结构。"],
    cnt=["真实的环境保护吐槽极为常见。", "没有明确的政治信号词。"],
    rat="有D2隐喻可能但环境吐槽解释权重相当，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="这些话题在别的地方根本看不到，珍惜吧", risk_level="medium",
    encoding_primary="E1_平台黑话", ctx_topic="平台讨论",
    lit=["评论某平台/群组的内容稀缺性。"],
    enc=["E1：'别的地方根本看不到'暗示内容在主流平台被过滤。"],
    ctx=["平台/社区讨论。"],
    sup=["暗示了主流平台的内容审查。", "'珍惜吧'确认了内容的不可替代性。"],
    cnt=["可以是任何小众兴趣内容（如特定游戏、影视）。", "不一定指向政治敏感内容。"],
    rat="有E1信号但内容方向不明，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="这个账号估计快没了，关注需从速", risk_level="medium",
    encoding_primary="E1_平台黑话", ctx_topic="平台讨论",
    lit=["预测某账号即将被封。"],
    enc=["E1：讨论账号'快没了'是平台审查观察。"],
    ctx=["微博/B站等平台常见此类讨论。"],
    sup=["账号消失预警暗示了内容敏感。"],
    cnt=["可能是因版权、违规广告等非政治原因被删。"],
    rat="账号消失预警有E1信号但原因多样，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

# --- 更多MEDIUM ---
R.append(s(text="翻译：有些话不能直说，自己体会", risk_level="medium",
    encoding_primary="E1_平台黑话", encoding_secondary=["F_组合编码"],
    lit=["以'翻译'开头暗示解密/解读。"],
    enc=["E1+F：'翻译'格式是互联网常见的编码包装，'自己体会'确认了隐含信息存在。"],
    ctx=["微博/评论区常见这种'翻译'格式的暗语传播。"],
    sup=["'翻译'+'不能直说'+'自己体会'三重编码信号。"],
    cnt=["可能是无害的梗或游戏暗语。", "具体内容未知。"],
    rat="三重编码信号明确但具体内容不详，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

R.append(s(text="删前留名", risk_level="medium",
    encoding_primary="E1_平台黑话",
    lit=["在认为会被删的内容下留言'删前留名'。"],
    enc=["E1：'删前留名'是经典的中文互联网内容删除预警行为。"],
    ctx=["微博/B站等平台常见。"],
    sup=["留言行为本身就暗示了对内容将被删的判断。"],
    cnt=["具体内容可能只是争议性而非政治性。", "也可能只是跟风行为。"],
    rat="删前留名是E1经典行为但无法判断内容性质，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

# ═══════════════════════════════════════════════════════════════
# NONE (30) — hard negatives that could trigger false positives
# ═══════════════════════════════════════════════════════════════

R.append(s(text="买了本《1984》，准备周末好好读一下", risk_level="none",
    encoding_primary="none",
    lit=["分享买书计划。"],
    enc=["无编码。正常阅读分享。", "《1984》本身不是禁书，正常购买阅读完全合法。"],
    ctx=["读书分享。"],
    sup=["仅提及书名。"],
    cnt=["《1984》是合法出版物，各大书店有售。", "正常读书计划分享。"],
    rat="正常读书分享。hard negative：不要因《1984》书名误判。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="今天看了《雪国》，川端康成写得太美了", risk_level="none",
    encoding_primary="none",
    lit=["分享阅读川端康成小说的感受。"],
    enc=["无编码。", "'雪国'是文学作品名。"],
    ctx=["文学分享。"],
    sup=["'雪国'在某些语境下可能被误读为政治隐喻。"],
    cnt=["川端康成的《雪国》是诺贝尔文学奖作品。", "纯文学讨论。"],
    rat="纯文学分享。hard negative。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="天气预报说下周要降温，大家注意保暖", risk_level="none",
    encoding_primary="none",
    lit=["分享天气提醒。"],
    enc=["无编码。"],
    ctx=["日常关怀。"],
    sup=["无任何风险信号。"],
    cnt=["纯粹的生活关怀。"],
    rat="纯日常提醒。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="双十一买的快递终于到了，拆箱快乐", risk_level="none",
    encoding_primary="none",
    lit=["分享购物收货的快乐。"],
    enc=["无编码。"],
    ctx=["购物分享。"],
    sup=["无风险信号。"],
    cnt=["纯消费分享。", "'拆箱'是正常的购物用语。"],
    rat="纯购物分享。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="今天去健身房练了腿，走路都在抖", risk_level="none",
    encoding_primary="none",
    lit=["分享健身后遗症。"],
    enc=["无编码。"],
    ctx=["健身日常。"],
    sup=["无风险信号。"],
    cnt=["纯健身分享。", "'练腿走不动路'是健身圈经典吐槽。"],
    rat="纯健身日常。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="这幅画里的红色用得太好了，热烈但不刺眼", risk_level="none",
    encoding_primary="none",
    lit=["评论画作的色彩运用。"],
    enc=["无编码。"],
    ctx=["艺术/绘画讨论。"],
    sup=["'红色'在某些语境下可能被联想。"],
    cnt=["纯艺术评论。", "绘画中讨论颜色是基本操作。"],
    rat="纯艺术讨论。hard negative。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="最近股市行情不好，亏了不少", risk_level="none",
    encoding_primary="none",
    lit=["抱怨股市亏损。"],
    enc=["无编码。日常财经讨论。"],
    ctx=["财经/投资交流。"],
    sup=["无政治风险信号。"],
    cnt=["纯粹的股市吐槽。", "没有编码意图。"],
    rat="纯财经讨论。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="这个游戏副本太难了，打了一个小时还没过", risk_level="none",
    encoding_primary="none",
    lit=["吐槽游戏难度。"],
    enc=["无编码。"],
    ctx=["游戏讨论。"],
    sup=["无风险信号。"],
    cnt=["纯游戏吐槽。"],
    rat="纯游戏讨论。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="今天地铁上人真多，挤成照片了", risk_level="none",
    encoding_primary="none",
    lit=["吐槽地铁拥挤。"],
    enc=["无编码。"],
    ctx=["日常通勤。"],
    sup=["无风险信号。"],
    cnt=["纯粹的通勤吐槽。"],
    rat="纯日常。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="这个手机壳图案是熊猫吃竹子，超可爱", risk_level="none",
    encoding_primary="none",
    lit=["分享手机壳图案。"],
    enc=["无编码。"],
    ctx=["消费/审美分享。"],
    sup=["仅'熊猫'一词。"],
    cnt=["纯购物分享。", "熊猫是中国最受欢迎的动物符号之一,日常使用广泛。"],
    rat="纯日常分享。hard negative：不要因'熊猫'符号联想。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

# ═══════════════════════════════════════════════════════════════
# 补 underrepresented encodings
# ═══════════════════════════════════════════════════════════════

# --- B1 拆字 ---
R.append(s(text="最近 石 卒 了很多 纟吉", risk_level="high",
    encoding_primary="B1_拆字",
    lit=["拆散的汉字部件。"],
    enc=["B1拆字：石+卒=碎，纟+吉=结。连续拆字表明是规避行为。"],
    ctx=["弹幕/评论中的规避表达。"],
    sup=["连续多字拆分确认了规避意图。"],
    cnt=["极低概率是输入法拆分或儿童识字。"],
    rat="多字连续拆分的规避模式明确，判high。",
    ambiguity="low", evidence_strength="strong"))

R.append(s(text="弓 虽 女 干", risk_level="low",
    encoding_primary="B1_拆字",
    lit=["4个部件可能是拆字。"],
    enc=["B1拆字可能：弓+虽=强，女+干=奸。但4个字符也可以是输入法乱码。"],
    ctx=["无上下文。"],
    sup=["部件组合可以还原为两个汉字。"],
    cnt=["可能是输入法乱码。", "也可能是随机字符。"],
    rat="可能拆字但不排除输入法问题，判low。",
    ambiguity="high", evidence_strength="weak"))

# --- B3 形近字 ---
R.append(s(text="今天看到一个人拿着一巴刀", risk_level="low",
    encoding_primary="B3_形近字替换",
    lit=["描述看到有人拿刀。"],
    enc=["B3微弱：'巴'可能是'把'的形近字替换。", "但更可能是正常错别字。"],
    ctx=["日常分享。"],
    sup=["形近关系存在。"],
    cnt=["普通人发短信/评论打错字极为常见。", "形近字替换作为规避方式的场景不多。"],
    rat="大概率是错别字，判low。",
    ambiguity="high", evidence_strength="weak"))

# --- A3 方言谐音 ---
R.append(s(text="哩个世界变佐啦", risk_level="low",
    encoding_primary="A3_方言谐音",
    lit=["粤语：这个世界变了。"],
    enc=["A3方言：用粤语表达'世界变了'。可能是规避也可能就是方言习惯。"],
    ctx=["广府地区用户日常使用粤语非常正常。"],
    sup=["使用方言可能是有意绕过普通话敏感词。"],
    cnt=["粤语用户日常交流完全正常。", "'世界变了'是一般感慨。"],
    rat="粤语日常表达。hard negative for A3。",
    ambiguity="high", evidence_strength="weak", hard_negative=True))

# --- C5 概念替换 ---
R.append(s(text="最近'法治建设'的讨论特别多，但大家关心的不是什么法条", risk_level="medium",
    encoding_primary="C5_概念替换", ctx_topic="社会讨论",
    lit=["评论法治讨论增多的现象。"],
    enc=["C5概念替换：用'法治建设'这个安全概念包装敏感的实质讨论。", "'不是法条'暗示讨论焦点是政治而非法律。"],
    ctx=["公共讨论语境。"],
    sup=["'不是法条'暴露了讨论的政治属性。", "概念包装模式明确。"],
    cnt=["也可以是真正的法律界内行讨论。"],
    rat="有C5概念替换痕迹但方向不完全确定，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

# --- E4 热点绑定 ---
R.append(s(text="这个词这几天突然火了，查了一下原来是那个事", risk_level="medium",
    encoding_primary="E4_热点绑定", ctx_topic="热点讨论",
    lit=["讨论某词突然走红的现象。"],
    enc=["E4热点绑定：用突然火爆的词暗示近期敏感事件。", "'查了一下原来是那个事'暗示事件不便言明。"],
    ctx=["热点追踪语境。"],
    sup=["'原来那个事'的模糊化暗示事件敏感。", "热点绑定+不便言明的组合。"],
    cnt=["可以是任何突然走红的网红梗。", "不一定涉及政治。"],
    rat="有E4信号但事件方向不明，判medium。",
    ambiguity="medium", evidence_strength="moderate"))

# --- More NONE hard negatives ---
R.append(s(text="白岩松今天说了句大实话", risk_level="none",
    encoding_primary="none",
    lit=["评论白岩松的言论。"],
    enc=["无编码。", "白岩松是央视主持人，日常讨论正常。"],
    ctx=["媒体评论。"],
    sup=["仅提及公众人物姓名。"],
    cnt=["正常媒体人讨论。"],
    rat="正常媒体评论。hard negative。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="这个纪录片讲的是中国高铁发展史", risk_level="none",
    encoding_primary="none",
    lit=["分享高铁纪录片。"],
    enc=["无编码。"],
    ctx=["纪录片推荐。"],
    sup=["无风险信号。"],
    cnt=["纯纪录片推荐。"],
    rat="纯纪录片分享。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

R.append(s(text="昨天做梦梦到自己在古代当官，审了个案子", risk_level="none",
    encoding_primary="none",
    lit=["分享一个梦。"],
    enc=["无编码。"],
    ctx=["日常分享。"],
    sup=["无风险信号。"],
    cnt=["纯梦境分享。", "古代当官梦非常常见。"],
    rat="纯梦分享。",
    ambiguity="low", evidence_strength="strong", hard_negative=True))

# ── write ─────────────────────────────────────────────────────
out = ROOT / "data" / "raw" / "batch3_natural_replacements.jsonl"
with out.open("w", encoding="utf-8") as f:
    for r in R:
        f.write(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n")

from collections import Counter
risk = Counter(r["risk_level"] for r in R)
enc = Counter(r["encoding_primary"] for r in R)
hn = sum(r["hard_negative"] for r in R)
print(f"Batch3: {len(R)} samples | HN: {hn}")
print(f"Risk: {dict(risk)}")
print(f"Top encodings: {enc.most_common(15)}")
