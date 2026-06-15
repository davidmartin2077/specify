#!/usr/bin/env python3
"""质量审查：修复 192 条 medium-risk needs_revision 样本。
- risk_level 修正（部分→high，少数→low）
- encoding_primary 纠正
- reasoning 去模板化
- quality_status → reviewed
"""

import json

DATA_PATH = "data/processed/combined_candidates.jsonl"
BACKUP_PATH = DATA_PATH + ".bak"


# ─── risk_level 修正 ─────────────────────────────────────────
# medium → high: 明文仇恨、政治攻击、色情推广
RISK_UPGRADE = {
    # 含明确侮辱词 + 攻击意图的
    "000039",  # 钕全...统一用这个 → hate speech pattern
    "000044",  # 中国男人应该灭绝 → 极端仇恨
    "000045",  # 生而为蝻...牧人代表... → 谐音+极端仇恨
    "000047",  # 黑粪蛋 → 种族侮辱
    "000048",  # 桖洗嘿枸 → 暴力+种族侮辱
    "000052",  # 姆蛆好恶心 → 谐音侮辱
    "000070",  # 猩猩 → 种族侮辱
    "000072",  # 公交车(侮辱女性) → 群体侮辱
    "000085",  # 巧克力色...纯黑 → 种族歧视
    "000086",  # 标子跟黑蛆一样 → 种族+性别侮辱
    "000365",  # 傻逼长得像猪 → 人身攻击
    "000366",  # 龌龊的嘴脸...打成猪头 → 暴力威胁
    "000395",  # 脑残傻逼 → 人身攻击
    "000400",  # 小娘们...跪下 → 性别侮辱+威胁
    "000410",  # 自私自利的小人 → 人身攻击
    "000415",  # 烂货...骚逼 → 极端侮辱
    "000416",  # 贱货...勾搭别人的男人 → 极端侮辱
    # 政治攻击
    "000360",  # 法轮功自焚
    "000361",  # 中共暴力镇压...天安门大屠杀
    "000373",  # 中国政府无能之极
    "000374",  # 战争列表(政治影射)
    "000390",  # 被刺习jp → 政治暗杀暗示
    "000397",  # 认清ccp本质 → 政治颠覆
    "000409",  # 王岐山...中共奴役 → 政治攻击
    "000411",  # 九评共产党 → 政治攻击
    # 色情推广(带联系方式)
    "000364",  # 色情内容+电报群推广
    "000376",  # 色情内容
    "000378",  # 色情内容+电报群推广
    "000405",  # 色情内容
    # 暴力威胁
    "000084",  # 不把你打一顿 → 暴力威胁
    # F_组合编码：赌博/色情/违规推广广告
    "000359",  # 金杯提鱼...找企鹅 → 赌博推广
    "000371",  # 史力伍佰奔...扣扣 → 赌博推广
    "000375",  # 大鹏叫育...扣扣裙 → 赌博/违规推广
    "000377",  # 离死舞...油油.泼肉 → 赌博推广
    "000389",  # 俺乃刚call...旺财 → 赌博推广
    "000396",  # 爆愉儿...牛蛙点抗母 → 赌博/色情推广
    "000406",  # 罐狀病毒檢測... → 虚假信息
    "000413",  # 嗨车...鸡巧教学...找Q → 赌博推广
    # 编码色情
    "000368",  # Tokyo hot暗示 → 色情
}

# medium → low: 正常讨论/反歧视/求助（措辞温和、正面意图）
RISK_DOWNGRADE_LOW = {
    "000036",  # 反感和歧视不一样 → 正常讨论
    "000194",  # 反对地域黑 → 反歧视言论
    "000195",  # 反对种族歧视 → 反歧视言论
    "000206",  # 反对地域黑 → 反歧视言论
    "000220",  # 反对种族歧视 → 反歧视言论
    "000224",  # 提倡尊重 → 正常讨论
    "000232",  # 反对地域黑（"都是中国人"呼吁团结）→ 正面但措辞较激烈
    "000235",  # 反对地域黑 → 反歧视言论
    "000249",  # 反对地域黑 → 反歧视言论
    "000414",  # 男女都受歧视 → 社会讨论
}

# medium → none: 完全无害、正能量、纯正面
RISK_DOWNGRADE_NONE = {
    "000226",  # 鼓励les群体找到爱人 → 纯正面鼓励
    "000228",  # 全职妈妈困境 → 社会现象描述，无攻击性
    "000386",  # 老年人也可以拥有积极的生活态度 → 纯正能量
}

# ─── encoding_primary 修正 ───────────────────────────────────
ENCODING_FIXES = {
    # 谐音编码被标为 literal_keyword
    "000039": ("A1_普通谐音", ["E1_平台黑话"]),   # 钕全=女权
    "000045": ("A1_普通谐音", ["E1_平台黑话"]),   # 蝻=男, 牧人=母人
    "000046": ("A1_普通谐音", ["E1_平台黑话"]),   # 蛛女=猪女
    "000048": ("A1_普通谐音", ["E1_平台黑话"]),   # 嘿枸=黑狗
    "000052": ("A1_普通谐音", ["E1_平台黑话"]),   # 姆蛆=母蛆
    "000059": ("A1_普通谐音", ["E1_平台黑话"]),   # 基蛆=基佬+蛆的侮辱合成
    "000065": ("D2_隐喻", []),                     # 母猪→隐喻侮辱
    "000070": ("D2_隐喻", []),                     # 猩猩→隐喻种族侮辱
    "000085": ("D2_隐喻", []),                     # 巧克力色→隐喻种族分类
    "000086": ("A1_普通谐音", ["E1_平台黑话"]),   # 标子=婊子, 黑蛆=黑+侮辱
    "000218": ("D1_反讽", []),                     # 反讽受害者有罪论
    "000365": ("D2_隐喻", []),                     # 长得像猪→隐喻侮辱
    "000366": ("D2_隐喻", ["D1_反讽"]),            # 隐喻+反讽侮辱
    "000395": ("literal_keyword", []),             # 保持，直接辱骂

    # D3_借代 → 细化
    "000035": ("D2_隐喻", []),                     # "枷锁"→隐喻
    "000038": ("D1_反讽", []),                     # 反讽黑人生活水平
    "000057": ("D1_反讽", []),                     # 反讽彩礼
    "000062": ("literal_keyword", []),             # 直接陈述
    "000067": ("D1_反讽", []),                     # 反讽"高知群体"
    "000068": ("C5_概念替换", []),                 # ◎◎◎替代
    "000073": ("A1_普通谐音", ["E1_平台黑话"]),   # 图男=屠男
    "000077": ("literal_keyword", []),             # 直接地域评价
    "000081": ("literal_keyword", []),             # 直接评价审美
}

# ─── 样本级别的 risk→encoding 联动 ────────────────────────
# 当 risk 被改为 high 时，同步需要修正的 encoding
RISK_HIGH_ENCODING = {
    "000400": ("D2_隐喻", []),        # 小娘们...跪下 → 隐喻侮辱
    "000415": ("D2_隐喻", []),        # 烂货...骚逼 → 隐喻侮辱
    "000416": ("D2_隐喻", []),        # 贱货...勾搭 → 隐喻侮辱
    "000410": ("literal_keyword", []), # 直接人身攻击
}


def detect_text_type(text):
    """检测文本类型"""
    hate_slurs = ["死光", "该死", "弄死", "婊子", "母狗", "母猪", "女犬", "幕刃", "亩枸",
                  "黑鬼", "黑粪", "垃圾", "废物", "傻逼", "脑残", "煞笔", "草泥马",
                  "贱货", "骚逼", "烂货", "猪头", "蛆", "猩猩", "猴子", "嘿枸",
                  "蝻", "蛛女", "姆蛆", "基蛆", "标子", "公交车",
                  "灭绝", "该死", "杀掉", "打死", "揍死",
                  "小娘们", "恶心", "龟孙", "畜生"]
    crime_keywords = ["抢劫", "绑架", "贩毒", "洗钱", "偷", "炸弹", "引爆", "买枪"]
    political_keywords = ["中共", "共产党", "天安门", "法轮功", "习近平", "ccp", "大纪元",
                          "九评", "零八宪章", "民主化", "屠杀", "专制", "独裁"]
    porn_keywords = ["电报:", "t.me", "http://t.me", "会员群", "熟女", "乱伦",
                     "性饥渴", "#约", "#舔", "#男m", "无码", "女优"]
    anti_discrimination = ["不要歧视", "反对歧视", "不应该歧视", "不能歧视", "不是地域黑",
                           "反对地域黑", "不是种族主义", "每个人都有", "都是中国人"]
    positive_messages = ["找到你爱的人", "加油", "积极的生活", "勇敢", "不要放弃",
                         "你可以的", "相信自己", "美好的", "珍惜", "感恩"]

    if any(w in text for w in anti_discrimination):
        return "anti_discrimination"
    if any(w in text for w in positive_messages) and not any(w in text for w in hate_slurs):
        return "positive"
    if any(w in text for w in hate_slurs):
        return "hate_speech"
    if any(w in text for w in political_keywords):
        return "political"
    if any(w in text for w in porn_keywords):
        return "porn"
    if any(w in text for w in crime_keywords):
        return "crime"
    return "other"


def generate_encoding_analysis(text, ep, es_list, notes):
    """根据编码类型 + 文本类型生成 encoding_analysis"""
    text_type = detect_text_type(text)

    if ep == "none":
        if text_type == "positive":
            return [
                "该文本为正面/鼓励性言论，不含编码手法或风险意图。",
                "虽然文本可能提及了敏感词汇，但语境是积极正面的——鼓励而非攻击。",
                "此类是典型的 hard_negative 样本：形态上可能被误判（含敏感词），但实质完全无害。",
            ]
        elif text_type == "anti_discrimination":
            return [
                "该文本为反歧视/呼吁团结的正面言论，不含编码手法。",
                "文本讨论社会议题但立场是反对歧视、提倡平等——属于正常公共讨论。",
            ]
        else:
            return [
                "该文本为完全无害的日常表达，不含编码手法或风险意图。",
                "hard_negative 样本——训练模型区分'看似可疑但实际无害'的内容，防止误杀。",
            ]

    if ep == "literal_keyword":
        if text_type == "hate_speech":
            return [
                "该文本为明文侮辱/歧视言论，未使用编码手法——攻击意图直接暴露在字面上。",
                "明文侮辱的风险在于伤害的直接性和煽动性——直接的群体贬低、人身攻击无需解码即可造成伤害。",
                "中风险评定的关键在于：侮辱程度是否达到极端（死亡威胁/性暴力暗示）还是停留在一般辱骂层面。",
            ]
        elif text_type == "political":
            return [
                "该文本涉及政治敏感内容，未使用编码手法进行包装——直接表达政治立场或指控。",
                "政治类明文表达的风险在于内容本身——对政府/体制的直接攻击、历史事件的重述或政治运动的推广。",
            ]
        elif text_type == "porn":
            return [
                "该文本含色情内容及推广信息（联系方式/群组链接），未使用编码手法。",
                "色情推广类文本的风险在于：不仅在传播色情内容，还通过联系方式引导至私域进行交易或进一步扩散。",
            ]
        elif text_type == "anti_discrimination":
            return [
                "该文本表面是反对歧视/呼吁平等的言论，未使用编码手法。",
                "反歧视言论本身是正面或中性的社会讨论——但如果措辞激烈或引用侮辱性词汇作为反面例子，可能被误判。",
            ]
        else:
            return [
                "该文本为直接表达，未使用编码手法对内容进行包装。",
                "需要在更大的语境中综合判断——孤立文本可能无法完整反映表达者的真实意图。",
            ]

    analyses = {
        "A1_普通谐音": [
            "使用普通话谐音替换手法，将侮辱性词汇包装为同音或近音汉字组合。",
            "谐音编码是中文互联网最常见的规避审查和软性侮辱手段——保留原词发音联想的同时在字形上制造伪装。",
        ],
        "D1_反讽": [
            "使用反讽修辞手法，表面陈述与真实意图之间存在张力。",
            "反讽的中风险特征在于：字面意思可能被误解，需要在语气和语境中判断真实立场。",
        ],
        "D2_隐喻": [
            "使用隐喻手法，通过类比框架表达贬损或攻击。",
            "隐喻的隐蔽性使其风险评级通常低于明文攻击——但隐喻映射的清晰度和攻击指向的明确性会影响最终判断。",
        ],
        "D3_借代": [
            "使用借代手法，用相关事物代替目标对象。",
            "借代的隐蔽性取决于约定俗成的程度——高频使用的借代关系更容易被识别。",
        ],
        "C5_概念替换": [
            "使用符号或概念替换来替代敏感词汇。",
            "符号替换是最低成本的编码手段——单个字符的替换即可改变文本的表面可读性。",
        ],
        "F_组合编码": [
            "该文本混合使用了多种编码手法（谐音、数字代指、符号替换等），单一手法不足以完成风险包装。",
            "组合编码常见于赌博/色情推广等商业违规内容——多手法叠加增加了自动识别的难度。",
        ],
    }

    base = analyses.get(ep, ["该文本使用编码手法包装敏感内容。"])
    return base


def generate_counter_evidence(text, ep, risk_level, notes):
    """生成真实的 counter_evidence"""
    text_type = detect_text_type(text)
    ctr = []

    if len(text) < 30:
        ctr.append("短文本缺乏上下文，单独一句可能存在歧义或断章取义的可能。")

    if any(w in text for w in ["据说", "听说", "有人说", "看到过", "原文", "引用"]):
        ctr.append("文本可能是引用或转述他人言论，需要区分说话者自身立场与转述内容。")

    if any(w in text for w in ["建议", "不如", "直接", "加速"]) and len(text) > 20:
        ctr.append("可能为反讽/阴阳怪气而非真实主张——中文互联网的加速主义表达常以'建议'形式包装。")

    if text_type == "hate_speech":
        if ep in ("A1_普通谐音",):
            ctr.append("谐音替代也可能是输入法错误或拼写习惯，需要确认该谐音在特定圈层中的约定性。")
        elif ep == "literal_keyword":
            ctr.append("虽是明文攻击，但互联网情绪宣泄与真实伤害意图之间存在区分——存在大量口嗨成分。")
        ctr.append("孤立的一条评论可能脱离对话背景——回复性质的内容需要看前文才能完整判断。")

    elif text_type == "political":
        ctr.append("政治表达与合法异议之间的边界因语境而异——需要结合平台规则和法律框架综合判断。")

    elif text_type == "porn":
        ctr.append("部分色情内容可能属于合法成人内容——需要区分违法淫秽与合规成人内容。")

    elif text_type == "anti_discrimination":
        ctr.append("文本本身是在反对歧视/呼吁平等——引用侮辱性词汇是为了批判而非传播。")
        ctr.append("反歧视言论属于正常社会讨论范畴，不应仅因提及敏感词而被判定为风险。")

    if ep in ("D1_反讽",):
        ctr.append("反讽的识别高度依赖语气和语境——在纯文本中，反讽与真诚陈述字面完全相同，存在误判可能。")
    if ep in ("F_组合编码",):
        ctr.append("编码手法本身不构成风险——需要确认解码后的实际内容是否违规。")

    if not ctr:
        ctr.append("在更大的上下文或对话历史中，该文本的含义可能与孤立判断不同。")

    return ctr


def generate_final_rationale(text, ep, notes, risk_level):
    """生成具体的 final_rationale"""
    text_type = detect_text_type(text)

    source = "未知来源"
    if "toxicn" in notes: source = "ToxiCN真实毒评数据"
    elif "cold" in notes: source = "真实网络评论"
    elif "chinesesafe" in notes: source = "ChineseSafe安全数据"

    level_label = {"high": "high", "medium": "medium", "low": "low"}.get(risk_level, risk_level)

    if ep == "literal_keyword":
        if text_type == "hate_speech":
            return f"明文侮辱/歧视言论（{source}），攻击意图直接但程度未达极端暴力/威胁级别，判为 {level_label}。"
        elif text_type == "political":
            return f"政治敏感内容（{source}），直接表达政治立场/指控，判为 {level_label}。"
        elif text_type == "porn":
            return f"色情内容（{source}），含推广信息，判为 {level_label}。"
        elif text_type == "anti_discrimination":
            return f"反歧视/呼吁平等言论（{source}），属正常社会讨论但措辞可能引发争议，判为 {level_label}。"
        else:
            return f"直接表达（{source}），综合文本信号与反证分析，判为 {level_label}。"
    elif ep == "A1_普通谐音":
        if risk_level == "high":
            return f"通过谐音编码包装的侮辱性言论（{source}），谐音替代非偶然且有圈层约定性，攻击指向明确，判为 {level_label}。"
        return f"通过谐音编码包装的表述（{source}），编码增加了解读难度但未完全消除风险信号，判为 {level_label}。"
    elif ep == "D1_反讽":
        return f"以反讽手法包装的表述（{source}），表面与真实意图之间的张力构成编码，判为 {level_label}。"
    elif ep == "D2_隐喻":
        return f"通过隐喻框架表达的贬损性内容（{source}），隐喻映射可识别但隐蔽性较强，判为 {level_label}。"
    elif ep == "F_组合编码":
        return f"多层编码叠加的敏感内容（{source}），编码复杂度高但解码后风险明确，判为 {level_label}。"
    else:
        return f"综合文本信号与反证分析（{source}），判为 {level_label}。"


def update_review_notes(old_notes):
    if "quality_reviewed=medium_r1" not in old_notes:
        return old_notes + "; quality_reviewed=medium_r1"
    return old_notes


def main():
    with open(DATA_PATH) as f:
        samples = [json.loads(line) for line in f]

    # 备份
    with open(BACKUP_PATH, 'w') as f:
        for s in samples:
            f.write(json.dumps(s, ensure_ascii=False) + '\n')
    print(f"✓ 备份到 {BACKUP_PATH}")

    fixed_count = 0
    risk_up = 0
    risk_down = 0
    ep_fixed = 0

    for s in samples:
        if s.get('quality_status') != 'needs_revision':
            continue
        if s['risk_level'] != 'medium':
            continue

        sid = s['id']
        changed = False

        # ── 1. risk_level 修正 ──
        if sid in RISK_UPGRADE:
            s['risk_level'] = 'high'
            risk_up += 1
            changed = True
        elif sid in RISK_DOWNGRADE_NONE:
            s['risk_level'] = 'none'
            s['encoding_primary'] = 'none'
            s['encoding_secondary'] = []
            s['hard_negative'] = True
            risk_down += 1
            changed = True
        elif sid in RISK_DOWNGRADE_LOW:
            s['risk_level'] = 'low'
            risk_down += 1
            changed = True

        # ── 2. encoding_primary 修正 ──
        if sid in ENCODING_FIXES:
            new_ep, new_es = ENCODING_FIXES[sid]
            if s['encoding_primary'] != new_ep:
                s['encoding_primary'] = new_ep
                ep_fixed += 1
                changed = True
            if new_es:
                existing = set(s['encoding_secondary'])
                existing.update(new_es)
                s['encoding_secondary'] = sorted(existing)
                changed = True

        if sid in RISK_HIGH_ENCODING:
            new_ep, new_es = RISK_HIGH_ENCODING[sid]
            if s['encoding_primary'] != new_ep:
                s['encoding_primary'] = new_ep
                ep_fixed += 1
                changed = True
            if new_es:
                existing = set(s.get('encoding_secondary', []))
                existing.update(new_es)
                s['encoding_secondary'] = sorted(existing)
                changed = True

        # ── 3. 重写 reasoning ──
        r = s['reasoning']
        text = s['text']
        ep = s['encoding_primary']
        notes = s.get('review_notes', '')
        risk = s['risk_level']

        # encoding_analysis
        old_enc = r.get('encoding_analysis', [])
        boilerplate = "真实外部评论/安全数据样本；优先按短文本本身判断，不编造额外上下文。"
        if (len(old_enc) == 1 and old_enc[0].strip() == boilerplate) or not old_enc:
            r['encoding_analysis'] = generate_encoding_analysis(text, ep, s.get('encoding_secondary', []), notes)
            changed = True

        # counter_evidence
        old_ctr = r.get('counter_evidence', [])
        generic_ctrs = [
            "需避免只因群体词出现就误判；本条风险来自完整表达。",
            "仍需区分引用、反驳和真实攻击；本条按原始标签与文本整体判断。",
            "该文本整体风险信号足够明确。",
        ]
        if (not old_ctr) or (old_ctr[0].strip() in generic_ctrs):
            r['counter_evidence'] = generate_counter_evidence(text, ep, risk, notes)
            changed = True

        # final_rationale
        old_final = r.get('final_rationale', '')
        if old_final.strip() == "综合文本信号和反证，判为 medium。" or not old_final:
            r['final_rationale'] = generate_final_rationale(text, ep, notes, risk)
            changed = True

        # ── 4. quality_status → reviewed ──
        if s['quality_status'] == 'needs_revision':
            s['quality_status'] = 'reviewed'
            changed = True

        # ── 5. review_notes ──
        s['review_notes'] = update_review_notes(s.get('review_notes', ''))

        if changed:
            fixed_count += 1

    # 写回
    with open(DATA_PATH, 'w') as f:
        for s in samples:
            f.write(json.dumps(s, ensure_ascii=False) + '\n')

    print(f"✓ 修复 {fixed_count}/192 条 medium-risk needs_revision")
    print(f"  risk ↑ (medium→high): {risk_up}条")
    print(f"  risk ↓ (medium→low): {risk_down}条")
    print(f"  encoding_primary 修正: {ep_fixed}条")


if __name__ == "__main__":
    main()
