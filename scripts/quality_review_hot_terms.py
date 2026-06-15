#!/usr/bin/env python3
"""质量审查：修正热词样本的风险标签。

核心原则：网络热词（鼠鼠/退退退/芭比Q/尊嘟假嘟/吗喽/哈基米等）本身不是风险信号。
风险应来自实际有害内容（仇恨言论/暴力威胁/政治颠覆），而非使用流行语进行社会评论。

修正逻辑：
- high → medium: 使用热词的社会/经济/政治评论，措辞尖锐但无仇恨/暴力/颠覆
- medium → low: 使用热词的轻度评论、语言学观察、幽默、人情故事
- 同步更新 reasoning 字段以匹配新风险等级
"""

import json
from copy import deepcopy

DATA_PATH = "data/processed/combined_candidates.jsonl"
BACKUP_PATH = DATA_PATH + ".hot_terms.bak"

# ─── high → medium: 社会评论/政策吐槽但无仇恨/暴力/颠覆 ───
HIGH_TO_MEDIUM = {
    "000870": "7字短文本，仅'這壹次，赢麻了'——政治反讽但无具体攻击对象，不足以判 high",
    "000948": "阶级评论'老板的孩子还是老板'——社会批评非仇恨言论，无暴力威胁",
    "000958": "'神神们团建+躺平心得'——圈层自嘲，无具体政治攻击",
    "000984": "'中或最赢+秦始皇摸电门'——政治反讽但无直接攻击/颠覆，属阴阳怪气范畴",
    "000988": "'绷不住了，看到那条新闻直接破防了'——内容空洞，无具体攻击对象",
    "001018": "'摸鱼是工人阶级对资本的唯一反抗形式'——阶级分析/社会评论，无暴力煽动",
    "001020": "'每一代人都有自己的反抗方式...00后躺平'——代际社会评论，学术分析口吻",
    "001211": "讨论哈基米BGM被用于规避审核——描述现象而非直接传播违规内容，属平台行为分析",
    "001212": "'吗喽的命也是命...吗喽人生'——自嘲式社会评论，无仇恨/暴力",
    "001213": "'遥遥领先现在成了一个笑话'——产品/商业批评为主，政治影射为辅",
    "001214": "'命运的齿轮...审核的齿轮'——审核制度评论，属正常公共讨论边界",
    "001215": "'纯爱战士...社会把人逼成了算账机器'——婚恋经济学社会评论",
    "001231": "'特种兵旅游的本质不是热爱旅游，是穷'——经济/旅游评论，社会观察",
    "001232": "'鼠鼠我啊...被人拿捏的一生'——自嘲式房贷/生活压力叙事",
    "001233": "'退退退...打工人的精神护身符'——职场压力社会评论",
    "001234": "'芭比Q了家人们...降薪...难关只渡我们'——职场不满吐槽",
    "001235": "'偷感...从生活缝隙里偷一点属于自己的东西'——社会观察/人生感悟",
    "001251": "'尊嘟假嘟？项目批下来了？...找了什么人打招呼'——暗示潜规则但无明确政治攻击",
    "001252": "'家人们谁懂啊，办证跑了三趟...我的税养着这些人'——政务服务投诉，属正常反馈",
}

# ─── medium → low: 轻度评论/语言学观察/幽默/人情故事 ───
MEDIUM_TO_LOW = {
    "000544": "'赢麻了，这次真的赢麻了'——仅重复口号，无具体内容，空洞无力",
    "001059": "'鼠鼠我啊，这辈子最大的成就就是活着'——自嘲式幽默，无攻击意图",
    "001219": "'命运的齿轮...视频活不过二十四小时'——现象描述+预感，风险信号弱",
    "001236": "'特种兵旅游回来后腿已经不是我的腿了'——纯旅游趣事分享，无风险意图",
    "001237": "'鼠鼠这个自称用久了真的会影响心态'——语言心理学的元评论，正面引导",
    "001238": "'显眼包...最稀缺的品质了'——生活感悟/正能量社会观察",
    "001239": "'蚌埠住了...主人翁不需要加班费'——职场吐槽段子，幽默为主",
    "001240": "'退退退大妈...一个梗背后的故事'——人情故事/社会观察，温和叙述",
    "001241": "'显眼包文化的反面...有底气不怕被孤立'——社会学级别观察，思辨性强",
    "001242": "'芭比Q这个词其实挺有意思的'——纯语言学观察，互联网语言科普",
    "001259": "'尊嘟假嘟这个梗的生命力...'——纯语言学/社交功能分析",
    "001260": "'家人们谁懂啊变成了一个万能开头'——纯语言学/传播学观察",
}

# encoding_primary 修正（部分样本的编码类型与内容不匹配）
ENCODING_FIXES = {
    # 语言学观察类 → encoding=none
    "001242": ("none", []),   # 芭比Q语义分析，无编码
    "001259": ("none", []),   # 尊嘟假嘟梗分析，无编码
    "001260": ("none", []),   # 家人们谁懂啊传播分析，无编码
    # 人情/生活类 → encoding=none
    "001236": ("none", []),   # 特种兵旅游趣事，无编码
    "001240": ("none", []),   # 退退退大妈故事，无编码
    # 职场幽默 → encoding=none
    "001239": ("none", []),   # 开会段子，无编码
    # 模糊空洞 → encoding=none
    "000988": ("none", []),   # 纯情绪表达无实质内容
}


def describe_text_surface(text, ep):
    """生成 literal_analysis 的简短描述"""
    if len(text) < 15:
        return "极简短句/口号式表达"
    if any(w in text for w in ["吗喽", "鼠鼠", "打工人", "社畜"]):
        return "使用网络热词进行自嘲式的社会评论/生活吐槽"
    if any(w in text for w in ["芭比Q", "退退退", "尊嘟假嘟", "绷不住", "蚌埠住了"]):
        return "使用网络热词作为语气/情绪包装进行吐槽或评论"
    if any(w in text for w in ["赢麻了", "遥遥领先", "中或最赢"]):
        return "使用政治反讽热词进行阴阳怪气式的社会评论"
    if any(w in text for w in ["哈基米", "电子榨菜", "纯爱战士", "特种兵旅游", "命运的齿轮", "显眼包", "偷感"]):
        return "使用网络热词对社会现象或个人体验进行描述/评论"
    if any(w in text for w in ["躺平", "摆烂", "摸鱼", "佛系", "内卷"]):
        return "讨论社会态度/生活方式选择"
    if any(w in text for w in ["家人们谁懂啊"]):
        return "使用热门句式包装日常吐槽或社会评论"
    return "使用网络流行语进行社会评论或吐槽"


def generate_medium_reasoning(text, ep, risk_level, notes):
    """为降为 medium 的样本生成完整 reasoning"""
    r = {}

    # literal_analysis
    r['literal_analysis'] = [f"文本表面是{describe_text_surface(text, ep)}。"]

    # context_analysis
    r['context_analysis'] = [
        "无明确上下文；按弹幕、应用评论、音乐评论等短文本场景做裸文本判断。",
        "网络热词的使用表明文本来自互联网亚文化圈层——热词本身是语境信号而非风险信号。",
    ]

    # supporting_evidence
    r['supporting_evidence'] = []
    if any(w in text for w in ["打工", "老板", "房贷", "降薪", "加班", "工资", "房租"]):
        r['supporting_evidence'].append("内容涉及职场/经济压力吐槽——属于普遍社会讨论范畴。")
    if any(w in text for w in ["审核", "被删", "屏蔽"]):
        r['supporting_evidence'].append("内容涉及平台审核体验——属于用户正常反馈。")
    if any(w in text for w in ["赢麻了", "绷不住", "破防", "尊嘟假嘟", "芭比Q"]):
        r['supporting_evidence'].append("使用网络热词作为表达载体——热词本身不构成风险。")
    if any(w in text for w in ["吗喽", "鼠鼠", "神神", "集美"]):
        r['supporting_evidence'].append("使用圈层自嘲身份标签——属于亚文化身份表达。")
    r['supporting_evidence'].append("文本表达尖锐但无仇恨言论、暴力威胁或政治颠覆信号。")

    # encoding_analysis
    if ep == "A1_普通谐音":
        r['encoding_analysis'] = [
            "使用普通话谐音/音译手法包装表述，热词（如鼠鼠/芭比Q/退退退）本身是网络流行语的谐音产物。",
            "谐音热词的风险不在于词汇本身，而在于携带的内容——当热词仅用于社会评论/自嘲/吐槽时，风险显著低于用于仇恨/暴力。",
        ]
    elif ep == "C4_典故/物品/符号借用":
        r['encoding_analysis'] = [
            "借用流行文化符号（热词/梗/BGM）作为表达的载体。",
            "热词编码的风险取决于所包装的内容——社会评论/现象分析属于正常公共表达范畴。",
        ]
    elif ep == "C5_概念替换":
        r['encoding_analysis'] = [
            "使用抽象概念替换直接表达——热词本身即是一种概念包装。",
            "概念替换的中风险特征：表达有观点但无具体攻击对象，停留在评论层面。",
        ]
    elif ep == "D1_反讽":
        r['encoding_analysis'] = [
            "使用反讽/阴阳怪气手法表达社会评论——热词常作为反讽的载体。",
            "反讽式社会评论不同于仇恨言论——讽刺对象是现象/制度而非受保护群体。",
        ]
    elif ep == "D2_隐喻":
        r['encoding_analysis'] = [
            "使用隐喻框架包装社会观察，热词本身即为隐喻的一部分。",
            "隐喻社会评论的中风险特征：框架可识别但仅用于描述现象而非煽动仇恨。",
        ]
    elif ep == "B3_形近字替换":
        r['encoding_analysis'] = [
            "使用形近字替换（壹→一），轻微的视觉编码手段。",
            "仅替换个别字形但内容本身为空洞的政治反讽，编码手法增加不了实质风险。",
        ]
    elif ep == "none":
        r['encoding_analysis'] = [
            "该文本为直接表达，未使用编码手法对内容进行包装。",
            "内容为社会评论/吐槽/情绪宣泄但无仇恨言论、暴力威胁或政治颠覆。",
        ]
    else:
        r['encoding_analysis'] = [
            "该文本使用编码手法包装社会评论/吐槽内容。",
            "表达尖锐但停留在评论层面，未上升到仇恨/暴力/颠覆的程度。",
        ]

    # counter_evidence
    r['counter_evidence'] = []
    if len(text) < 30:
        r['counter_evidence'].append("短文本缺乏上下文，无法确认攻击目标和真实意图。")
    r['counter_evidence'].append("网络热词（鼠鼠/退退退/芭比Q/吗喽等）是圈层自嘲和情绪宣泄的常用载体——大量使用热词的表达属于亚文化共鸣而非实际攻击。")
    if any(w in text for w in ["打工", "老板", "房贷", "降薪", "加班", "工资", "房租", "KPI"]):
        r['counter_evidence'].append("职场/经济压力吐槽属于普遍社会现象讨论——批评资本/老板/房价与攻击受保护群体有本质区别。")
    if any(w in text for w in ["审核", "被删", "屏蔽", "被下", "发不出"]):
        r['counter_evidence'].append("对平台审核的讨论属于用户正常反馈——讨论审核现象不等同于传播违规内容。")
    if not r['counter_evidence']:
        r['counter_evidence'].append("在更大的语境中，该表达可能为圈层内部的情绪交流而非对外攻击。")

    # final_rationale
    source = "未知来源"
    if "toxicn" in notes: source = "ToxiCN真实数据"
    elif "cold" in notes: source = "真实网络评论"
    elif "batch" in notes: source = "合成样本"

    if ep == "A1_普通谐音":
        r['final_rationale'] = f"使用热词谐音编码包装的社会评论/吐槽（{source}），表达尖锐但无仇恨/暴力/颠覆，判为 medium。"
    elif ep in ("D1_反讽", "D2_隐喻"):
        r['final_rationale'] = f"以修辞手法包装的社会评论（{source}），反讽/隐喻指向现象而非攻击受保护群体，判为 medium。"
    elif ep in ("C4_典故/物品/符号借用", "C5_概念替换"):
        r['final_rationale'] = f"借用文化符号表达的社会评论（{source}），内容为现象描述/吐槽而非攻击，判为 medium。"
    elif ep == "B3_形近字替换":
        r['final_rationale'] = f"轻微编码包装的极短表达（{source}），内容空洞无力，不足以构成高风险，判为 medium。"
    else:
        r['final_rationale'] = f"社会评论/吐槽（{source}），内容尖锐但无仇恨言论/暴力威胁/政治颠覆，判为 medium。"

    return r


def generate_low_reasoning(text, ep, risk_level, notes):
    """为降为 low 的样本生成完整 reasoning"""
    r = {}

    # literal_analysis
    r['literal_analysis'] = [f"文本表面是{describe_text_surface(text, ep)}。"]

    # context_analysis
    r['context_analysis'] = [
        "无明确上下文；按弹幕、应用评论、音乐评论等短文本场景做裸文本判断。",
        "文本语境轻松——网络热词在此作为幽默/分享/反思的工具而非攻击武器。",
    ]

    # supporting_evidence
    r['supporting_evidence'] = []
    if any(w in text for w in ["有意思", "生命力", "万能", "好用", "分析", "观察"]):
        r['supporting_evidence'].append("文本为语言学/传播学观察——属于知识讨论范畴。")
    if any(w in text for w in ["旅游", "周末", "爬山", "香山", "故宫"]):
        r['supporting_evidence'].append("文本为旅游趣事分享——属于日常生活内容。")
    if any(w in text for w in ["开会", "加班费", "主人翁", "方案", "写"]):
        r['supporting_evidence'].append("文本为职场幽默段子——以娱乐为目的的吐槽。")
    r['supporting_evidence'].append("文本核心意图为娱乐/分享/反思而非攻击——网络热词在此作为表达工具。")

    # encoding_analysis
    if ep == "none":
        r['encoding_analysis'] = [
            "该文本为日常表达/段子/趣事分享，未使用编码手法包装风险内容。",
            "文本可能提及网络热词或敏感话题，但语境是轻松的——幽默、人情故事或语言学观察。",
        ]
    elif ep == "D1_反讽":
        r['encoding_analysis'] = [
            "轻度使用反讽修辞，但内容为空洞口号或自嘲幽默，无实质攻击对象。",
            "低风险反讽的特征：讽刺对象模糊、以娱乐为目的、不涉及受保护群体。",
        ]
    elif ep == "D2_隐喻":
        r['encoding_analysis'] = [
            "使用隐喻框架但仅为自嘲/幽默——热词'鼠鼠'作为自我矮化的隐喻。",
            "隐喻的低风险使用：映射关系仅用于描述个人感受而非攻击他人。",
        ]
    elif ep == "A1_普通谐音":
        r['encoding_analysis'] = [
            "使用热词谐音编码进行轻度社会评论或语言学观察。",
            "谐音热词在此上下文中仅作为表达工具——内容为反思/观察而非攻击。",
        ]
    elif ep == "C4_典故/物品/符号借用":
        r['encoding_analysis'] = [
            "借用文化符号但内容为现象描述/预感而非攻击。",
            "文化符号的低风险使用：提及敏感话题但无具体攻击对象和煽动意图。",
        ]
    elif ep == "C5_概念替换":
        r['encoding_analysis'] = [
            "使用概念替换进行社会观察/生活感悟——内容积极或中性。",
            "概念替换的低风险使用：表达观点但立场温和、无攻击性。",
        ]
    else:
        r['encoding_analysis'] = [
            "该文本为轻度表达，风险信号弱。",
            "低风险特征：内容为幽默/观察/感悟，无明确攻击对象。",
        ]

    # counter_evidence
    r['counter_evidence'] = []
    if len(text) < 30:
        r['counter_evidence'].append("短文本缺乏上下文，独立判断可能被过度解读。")
    r['counter_evidence'].append("文本的核心意图是娱乐/分享/反思而非攻击——网络热词在此作为表达工具而非攻击武器。")
    r['counter_evidence'].append("低风险表达属于正常网络交流范畴——区分'使用敏感词汇'与'传播有害内容'是训练的核心目标。")
    if not r['counter_evidence']:
        r['counter_evidence'].append("在完整对话上下文中，该文本的非攻击性更为明确。")

    # final_rationale
    source = "未知来源"
    if "batch" in notes: source = "合成样本"

    if ep == "none":
        r['final_rationale'] = f"日常段子/趣事/语言观察（{source}），无风险意图，判为 low。"
    elif ep in ("D1_反讽", "D2_隐喻"):
        r['final_rationale'] = f"轻度修辞包装的自嘲/幽默表达（{source}），无实质攻击内容，判为 low。"
    elif ep == "A1_普通谐音":
        r['final_rationale'] = f"热词谐音包装的轻度表达（{source}），内容为反思/观察而非攻击，判为 low。"
    elif ep in ("C4_典故/物品/符号借用", "C5_概念替换"):
        r['final_rationale'] = f"文化符号包装的轻度表达（{source}），内容温和无攻击性，判为 low。"
    else:
        r['final_rationale'] = f"轻度表达（{source}），风险信号弱，判为 low。"

    return r


def update_review_notes(old_notes):
    if "quality_reviewed=hot_terms_r1" not in old_notes:
        return old_notes + "; quality_reviewed=hot_terms_r1"
    return old_notes


def main():
    with open(DATA_PATH) as f:
        samples = [json.loads(line) for line in f]

    # 备份
    with open(BACKUP_PATH, 'w') as f:
        for s in samples:
            f.write(json.dumps(s, ensure_ascii=False) + '\n')
    print(f"✓ 备份到 {BACKUP_PATH}")

    high_down = 0
    medium_down = 0
    ep_fixed = 0

    for s in samples:
        sid = s['id']
        changed = False

        # ── 1. encoding_primary 修正 ──
        if sid in ENCODING_FIXES:
            new_ep, new_es = ENCODING_FIXES[sid]
            if s['encoding_primary'] != new_ep:
                s['encoding_primary'] = new_ep
                s['encoding_secondary'] = new_es
                ep_fixed += 1
                changed = True

        # ── 2. risk_level 修正 ──
        if sid in HIGH_TO_MEDIUM:
            s['risk_level'] = 'medium'
            high_down += 1
            changed = True

            # 重写 reasoning
            new_r = generate_medium_reasoning(
                s['text'], s['encoding_primary'], 'medium',
                s.get('review_notes', '')
            )
            s['reasoning'] = new_r

        elif sid in MEDIUM_TO_LOW:
            s['risk_level'] = 'low'
            medium_down += 1
            changed = True

            # 重写 reasoning
            new_r = generate_low_reasoning(
                s['text'], s['encoding_primary'], 'low',
                s.get('review_notes', '')
            )
            s['reasoning'] = new_r

        # ── 3. review_notes 标记 ──
        if changed:
            s['review_notes'] = update_review_notes(s.get('review_notes', ''))

    # 写回
    with open(DATA_PATH, 'w') as f:
        for s in samples:
            f.write(json.dumps(s, ensure_ascii=False) + '\n')

    print(f"✓ high→medium: {high_down} 条")
    print(f"✓ medium→low: {medium_down} 条")
    print(f"✓ encoding_primary 修正: {ep_fixed} 条")
    print(f"✓ 总计修正: {high_down + medium_down} 条")


if __name__ == "__main__":
    main()
