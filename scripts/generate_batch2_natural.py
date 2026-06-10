#!/usr/bin/env python3
"""Batch 2: More natural Chinese-internet samples, focusing on HIGH risk and hard negatives."""

import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
BATCH = "batch2_natural"
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


records = []

# ═══ HIGH risk (need ~25 more) ═══

# --- C1: 历史人物类比 (high) ---
records.append(s(
    text="末代皇帝里面那个被抱进宫的小孩，眼神里有东西",
    risk_level="high", encoding_primary="C1_历史人物类比",
    lit=["讨论电影《末代皇帝》中童年溥仪的眼神。"],
    enc=["C1类比：'被抱进宫的小孩'=被动进入体制的个体，'眼神里有东西'=看透了什么。", "用电影人物映射对现实体制的观察。"],
    ctx=["电影台词在互联网政治讨论中常被作为类比引用。"],
    sup=["讨论'眼神里有东西'暗示电影/历史隐喻指向现实。"],
    cnt=["可以是纯粹的电影讨论。", "但'眼神里有东西'在此语境中通常不是单纯影评。"],
    rat="溥仪/末代皇帝意象在鉴证讨论中高频出现，'眼神有东西'暗示了不可言说的认知，判high。",
    ambiguity="low", evidence_strength="strong",
))

records.append(s(
    text="崇祯说'诸臣误我'的时候，底下人心里在想什么",
    risk_level="high", encoding_primary="C1_历史人物类比",
    lit=["讨论明末崇祯帝与大臣的关系。"],
    enc=["C1类比：崇祯=面临系统性崩溃的最高决策者，'诸臣误我'=将失败归咎体制而非自身。"],
    ctx=["崇祯+诸臣误我组合近年成为固定政治隐射。"],
    sup=["高度固化的历史类比：崇祯的'众臣误我'已是指向明确的互联网鉴证梗。"],
    cnt=["纯粹明史讨论确实可能。", "但加上'底下人心里在想什么'的揣测意识，暗示了现实观照。"],
    rat="崇祯困境是鉴证圈极高频类比，'底下人心中在想什么'引导现实投射，判high。",
    ambiguity="low", evidence_strength="strong",
))

# --- C2: 历史事件影射 (high) ---
records.append(s(
    text="秦朝二世而亡，问题出在哪？出在没给孩子足够的时间成长",
    risk_level="high", encoding_primary="C2_历史事件影射",
    encoding_secondary=["D1_反讽"],
    lit=["讨论秦朝短暂灭亡的原因。"],
    enc=["C2+反讽：表面讨论秦朝，用'没给孩子时间成长'这种现代家庭教育话语指涉现实。", "反讽点在于'孩子成长'在当代政治中有明确指向。"],
    ctx=["'孩子'在此语境中借用了现代政治讨论中的固定代指。"],
    sup=["秦朝二世而亡是中国史基本常识，讨论它不需要用到'给孩子时间'这种话术——这暴露了当代映射意图。"],
    cnt=["可能只是用现代语言调侃历史的通俗写法。"],
    rat="秦朝+孩子成长的反讽框架指向明确，'给孩子时间'暴露了当代政治隐喻，判high。",
    ambiguity="low", evidence_strength="strong",
))

# --- D1: 反讽 (high) ---
records.append(s(
    text="感谢国家，感谢平台，感谢审核员，我这评论删三次了还发",
    risk_level="high", encoding_primary="D1_反讽",
    encoding_secondary=["E1_平台黑话"],
    lit=["感谢各方后表明自己评论被多次删除。"],
    enc=["D1反讽：三重感谢的堆叠是明显的反讽结构。", "E1：讨论平台审核删除行为。"],
    ctx=["'删三次还发'表明用户在对抗审核。"],
    sup=["三重感谢的过度夸张明确指向反讽。", "删除经历证实了内容敏感。"],
    cnt=["可能是发广告被删的抱怨。", "但这种三重感谢的句式几乎总是政治相关的反讽。"],
    rat="过度感谢+删帖对抗行为，反讽意图明确，判high。",
    ambiguity="low", evidence_strength="strong",
))

# --- C4: 符号借用 (high) ---
records.append(s(
    text="熊猫是国宝，但你不能因为它可爱就忘了它会咬人",
    risk_level="high", encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["D2_隐喻"],
    lit=["讨论熊猫可爱但有攻击性。"],
    enc=["C4+D2：熊猫=国家/体制的符号化隐喻。", "'可爱但不能忘了它会咬人'=不能因为表面温和就忽视其强制力。"],
    ctx=["熊猫作为国家符号的隐喻在简中互联网已有固化理解。"],
    sup=["熊猫在互联网政治讽刺中长期作为'国宝/国家'的符号代表。", "会咬人的警告暗示了对权力的警惕。"],
    cnt=["可以是纯粹动物科普/讨论。", "但句子结构（'不能因为它可爱就忘了'→它会咬人）明显在说人和权力，不是动物。"],
    rat="熊猫+咬人组合在当代互联网政治隐喻中方向明确，普通动物科普解释权重低，判high。",
    ambiguity="low", evidence_strength="strong",
))

records.append(s(
    text="这杯咖啡太苦了，苦到我怀疑人生",
    risk_level="none", encoding_primary="none",
    lit=["吐槽某杯咖啡过苦。"],
    enc=["无编码。"],
    ctx=["小红书咖啡探店日常。"],
    sup=["无风险信号。"],
    cnt=["完整的咖啡吐槽。", "纯粹的日常生活分享。"],
    rat="纯生活分享，hard negative。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

# --- E2: 时间节点 ---
records.append(s(
    text="六月四号什么日子来着？哦对，星期六",
    risk_level="high", encoding_primary="E2_时间节点触发",
    encoding_secondary=["C3_数字代指"],
    lit=["自问自答六月四号的日期。"],
    enc=["E2+C3：通过'自问自答'唤起特定日期记忆，然后用'星期六'作为表面回复。"],
    ctx=["这种自问自答+日期切换是常见的规避唤起句式。"],
    sup=["自问自答结构暗示了日期的重要性。", "先用日期唤起注意再用'星期六'稀释的套路明显。"],
    cnt=["真的可能在确认日期。"],
    rat="结构化唤起特定日期+转移注意力的套路明显，判high。",
    ambiguity="low", evidence_strength="strong",
))

# --- B1: 拆字 ---
records.append(s(
    text="你 女 未 女子 女子 扌 丁",
    risk_level="high", encoding_primary="B1_拆字",
    lit=["一系列拆散的汉字部件。"],
    enc=["B1拆字："],
    ctx=["B站弹幕中拆字是常见规避方式。"],
    sup=["明确的拆字规避模式。", "多个字连续拆分确认了编码意图而非偶然。"],
    cnt=["极低概率是输入法错误或儿童识字游戏。"],
    rat="连续多字拆分的规避模式明确，判high。",
    ambiguity="low", evidence_strength="strong",
))

# --- A1: 谐音 ---
records.append(s(
    text="今晚的月亮好大，像个脸盆",
    risk_level="low", encoding_primary="A1_普通谐音",
    lit=["形容月亮很大。"],
    enc=["无明确编码。'脸盆'理论上可能谐音某词但无实据。"],
    ctx=["日常天文分享。"],
    sup=["仅有极微弱的谐音可能。"],
    cnt=["正常的月亮描述。", "脸盆是常见的大小比喻。"],
    rat="纯日常分享。hard negative for A1。",
    ambiguity="high", evidence_strength="weak", hard_negative=True,
))

# --- More hard negatives ---
records.append(s(
    text="今天跟同事讨论了公司政治，真是心累",
    risk_level="none", encoding_primary="none",
    lit=["抱怨公司办公室政治。"],
    enc=["无编码。'公司政治'指职场人际关系。"],
    ctx=["日常生活吐槽。"],
    sup=["无风险信号。"],
    cnt=["'政治'在此仅指职场人际关系。", "上下文明确无政治风险。"],
    rat="职场吐槽，hard negative：训练模型区分'办公室政治'与国家政治。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

records.append(s(
    text="小米手机真的很良心，价格低配置高",
    risk_level="none", encoding_primary="none",
    lit=["夸奖小米手机性价比。"],
    enc=["无编码。日常消费讨论。"],
    ctx=["手机评测/推荐语境。"],
    sup=["无风险信号。"],
    cnt=["纯消费讨论。", "'良心'在此是消费品评价用语。"],
    rat="纯消费讨论。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

records.append(s(
    text="我爷爷参加过解放战争，每次听他讲都很感动",
    risk_level="none", encoding_primary="none",
    lit=["分享与爷爷关于解放战争的交流。"],
    enc=["无编码。正常家庭历史讨论。"],
    ctx=["家庭回忆。"],
    sup=["提到'解放战争'——正常历史词汇。"],
    cnt=["完整的家庭回忆语境。", "正面情感表达。", "无任何影射信号。"],
    rat="正面家庭历史回忆。hard negative：训练模型不要因'解放战争'等正常历史词汇误判。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

records.append(s(
    text="今天的升旗仪式真壮观，三军仪仗队太帅了",
    risk_level="none", encoding_primary="none",
    lit=["分享观看升旗仪式的感受。"],
    enc=["无编码。爱国旅游分享。"],
    ctx=["天安门旅游打卡。"],
    sup=["无风险信号。"],
    cnt=["纯旅游分享。", "正面积极表达。"],
    rat="纯旅游爱国主义分享。hard negative。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

records.append(s(
    text="查了查家谱，祖上还真是个大官",
    risk_level="none", encoding_primary="none",
    lit=["分享家谱研究结果。"],
    enc=["无编码。正常家族史研究。"],
    ctx=["家谱/历史研究。"],
    sup=["无风险信号。"],
    cnt=["纯家族史研究兴趣。"],
    rat="纯家族史讨论。hard negative。",
    ambiguity="low", evidence_strength="strong", hard_negative=True,
))

# --- HIGH: More categories ---

records.append(s(
    text="建议读读那本不能提名字的书，看完就什么都明白了",
    risk_level="high", encoding_primary="F_组合编码",
    encoding_secondary=["E1_平台黑话"],
    lit=["推荐某本不便提名的书。"],
    enc=["F+E1：'不能提名字的书'+看完就懂的强烈暗示组合。", "自我审查+引导读者自行发现。"],
    ctx=["通常指涉固定的几本敏感书籍。"],
    sup=["'不能提名字'是强烈的自我审查信号。", "'看完什么都明白了'引导读者进行特定解读。"],
    cnt=["理论上可以是任何小众书籍。"],
    rat="双重编码信号明确，判high。",
    ambiguity="low", evidence_strength="strong",
))

records.append(s(
    text="老大哥会照顾好你的，不用担心",
    risk_level="high", encoding_primary="C4_典故/物品/符号借用",
    lit=["引用《1984》中的'老大哥'概念。"],
    enc=["C4：老大哥=《1984》中的极权监视者，已成为互联网固定借代。"],
    ctx=["'老大哥'在简中互联网已完全固化，不需要额外解释。"],
    sup=["《1984》的老大哥在简中是最高频的政治隐喻之一。", "'不用担心'是经典反讽包装。"],
    cnt=["可以是单纯的《1984》书友讨论。"],
    rat="老大哥隐喻极度固化，政治指向明确，判high。",
    ambiguity="low", evidence_strength="strong",
))

records.append(s(
    text="这几天社区在发菜，每家一袋，挺暖心",
    risk_level="low", encoding_primary="C4_典故/物品/符号借用",
    lit=["分享社区发菜福利。"],
    enc=["'发菜'在特定时期有特定含义，但完整生活分享语境降低了编码可能性。"],
    ctx=["社区福利分享。"],
    sup=["仅'发菜'一词有微小编码可能。"],
    cnt=["真实的社区福利分享。", "完整语境支持普通解读。"],
    rat="普通生活分享。hard negative。",
    ambiguity="high", evidence_strength="weak", hard_negative=True,
))

# --- More HIGH & MEDIUM for diversity ---

records.append(s(
    text="有时候觉得活在一个大型剧本杀里，每个人都在背台词",
    risk_level="medium", encoding_primary="D2_隐喻",
    lit=["用剧本杀比喻生活体验。"],
    enc=["D2隐喻：剧本杀=社会生活被安排、角色被固定的感觉。"],
    ctx=["这种表达在当代年轻人中常见，不必然有政治意指。"],
    sup=["'每个人都在背台词'暗示言论不自由/行为受控。"],
    cnt=["年轻人在讨论社会压力、职场表演时也常使用类似表达。"],
    rat="有D2隐喻可能但社会压力讨论也常见，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(s(
    text="网盘里的东西又被和谐了，连个通知都没有",
    risk_level="low", encoding_primary="E1_平台黑话",
    lit=["抱怨网盘文件被删。"],
    enc=["E1平台黑话微弱：'和谐'暗示内容被审查。但网盘文件被删的原因很多（版权、违规等）。"],
    ctx=["普通网盘使用吐槽。"],
    sup=["'和谐'在中文互联网已固化为审查/删除的代名词。"],
    cnt=["网盘删文件常见原因包括版权、色情、用户举报等非政治原因。", "单条吐槽没有政治编码。"],
    rat="普通网盘吐槽。" if True else "",
    ambiguity="high", evidence_strength="weak", hard_negative=True,
))

records.append(s(
    text="这篇文章写的太直白了，估计一会儿就404",
    risk_level="medium", encoding_primary="E1_平台黑话",
    lit=["评论某文章将因内容敏感被删除。"],
    enc=["E1：'太直白'+'404'组合是互联网对敏感内容被删的共识表达。"],
    ctx=["微博用户对404有共识理解。"],
    sup=["'太直白'暗示内容敏感。", "404是删除的高共识代码。"],
    cnt=["可能是一般性的版权或争议内容（非政治）。"],
    rat="有明确E1信号但内容性质不详，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(s(
    text="有人记得三年前这时候发生了什么吗？评论区打暗号",
    risk_level="high", encoding_primary="E2_时间节点触发",
    encoding_secondary=["E1_平台黑话"],
    lit=["邀请评论回忆三年前同期的事件。"],
    enc=["E2+E1：特定时间节点触发+'暗号'引导规避讨论。", "明确要求用暗号回复暗示事件敏感。"],
    ctx=["'三年前这时候'可能是某敏感事件的周年。"],
    sup=["'打暗号'明确表明事件不可公开讨论。", "时间触发+暗号邀请的双重编码。"],
    cnt=["如果不是发生在敏感事件节点上，可能是游戏/社区内部梗。"],
    rat="时间节点+暗号的强组合，判high。注意：如果在真实敏感周年则风险更高。",
    ambiguity="low", evidence_strength="strong",
))

records.append(s(
    text="小区门口的围墙又加高了",
    risk_level="medium", encoding_primary="D2_隐喻",
    lit=["描述小区围墙升高。"],
    enc=["D2隐喻：围墙升高=某种限制/管控加强。"],
    ctx=["在特定时期（如疫情封控期间）此表达有明确映射。"],
    sup=["'围墙加高'在互联网讨论中可隐喻管控升级。"],
    cnt=["真的可能是小区物业工程。", "社区改造围墙高度很常见。"],
    rat="有隐喻可能但真实物业管理也常见，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(s(
    text="新来的领导很喜欢开会，每周一三五都要表忠心",
    risk_level="low", encoding_primary="D3_借代",
    lit=["吐槽领导爱开会让员工表忠心。"],
    enc=["'表忠心'可能有微弱的政治借代联想但主要指职场。"],
    ctx=["职场吐槽语境。"],
    sup=["'表忠心'一词有微弱的政治联想。"],
    cnt=["完整的职场吐槽语境。", "公司政治中'表忠心'是常见说法。"],
    rat="职场吐槽，政治联想极弱。hard negative。",
    ambiguity="high", evidence_strength="weak", hard_negative=True,
))

# --- FINAL few HIGH samples ---

records.append(s(
    text="凡是敌人反对的我们就要拥护，凡是敌人拥护的我们就要反对——我说的是打游戏",
    risk_level="medium", encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["D1_反讽"],
    lit=["引用一句政治语录后加上游戏标签。"],
    enc=["C4+反讽：用著名政治语录包装普通游戏评论，形成反讽效果。"],
    ctx=["'我说的是打游戏'的补充暴露了自觉性——他知道这段语录有政治色彩。"],
    sup=["引用著名政治人物语录在游戏讨论中是异常行为。", "补充'我说的是打游戏'暗示了编码意识。"],
    cnt=["可能是纯粹的玩梗/恶搞。", "游戏讨论中引用语录作幽默包装是B站常见行为。"],
    rat="语录引用+补充说明显示编码意识，但游戏语境下降级可能，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(s(
    text="把那条新闻看完，又看了一遍评论区，发现全被删干净了",
    risk_level="medium", encoding_primary="E3_话题/热点触发",
    lit=["描述某新闻评论区被清空。"],
    enc=["E3：评论被删暗示新闻敏感。", "对删评的观察本身就是在讨论敏感事件。"],
    ctx=["微博用户对'删评'有共识理解。"],
    sup=["评论区被清空是敏感新闻的强信号。"],
    cnt=["也可能是违规评论太多（辱骂、谣言等），平台正常管理。"],
    rat="删评观察暗示新闻敏感但可能是正常管理，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(s(
    text="最近这批新来的，都不太爱唱那个歌了",
    risk_level="medium", encoding_primary="C4_典故/物品/符号借用",
    encoding_secondary=["D3_借代"],
    lit=["观察新人不太愿意唱某首歌。"],
    enc=["C4/D3：'那个歌'=某种仪式性/政治性表达，'不爱唱了'=政治态度变化。"],
    ctx=["'那个歌'的模糊化处理暗示了其敏感性质。"],
    sup=["模糊化'那个歌'暗示其不便指名。", "'不爱唱了'暗示态度转变。"],
    cnt=["可能是学校/公司年会中的表演歌曲。"],
    rat="有C4可能但具体指涉不明，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

records.append(s(
    text="他说话的声音越来越小了，但说的话越来越有分量",
    risk_level="medium", encoding_primary="D2_隐喻",
    encoding_secondary=["D3_借代"],
    lit=["描述某人说话声音轻但内容有分量。"],
    enc=["D2+D3：'说话声音越来越小'=公开表达空间缩小，'越来越有分量'=内容愈加重要/敏感。"],
    ctx=["这种'小声说话'的表达在特定圈层有固定隐喻解读。"],
    sup=["'声音越来越小'在简中互联网隐喻中指向言论空间。", "与'越来越有分量'形成对比暗示。"],
    cnt=["真的在讨论某个讲师/公众人物的说话风格。"],
    rat="有D2隐喻可能但不排除字面含义，判medium。",
    ambiguity="medium", evidence_strength="moderate",
))

# ── write ─────────────────────────────────────────────────────────
output_path = ROOT / "data" / "raw" / "batch2_natural_replacements.jsonl"
with output_path.open("w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n")

risk = Counter(r["risk_level"] for r in records)
enc = Counter(r["encoding_primary"] for r in records)
hn = sum(r["hard_negative"] for r in records)
print(f"Batch2: {len(records)} samples")
print(f"Risk: {dict(risk)}")
print(f"Hard negative: {hn}")
print(f"Encodings: {enc.most_common(15)}")
