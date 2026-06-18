#!/usr/bin/env python3
"""Review chunk_018.jsonl - rewrite all reasoning with text-specific analysis."""

import json

INPUT = "/Users/davidchankong/Documents/审查微调/data/raw/batch23_chunks/chunk_018.jsonl"
OUTPUT = "/Users/davidchankong/Documents/审查微调/data/raw/batch23_chunks/chunk_018_reviewed.jsonl"

APPENDIX = "; reviewed_by=claude; chunk=018"

def make(cfg):
    """Build a fully reviewed sample. Fields not in cfg are copied from orig
    (with review_notes appended).  Assert orig on the first call sets a baseline."""
    # We'll patch onto the original dict read from disk
    pass

def review_sample(s):
    """Return a deep-updated copy of s with all reasoning reviewed."""
    sid = s["id"]
    out = dict(s)

    # Build new review_notes from old
    notes = s.get("review_notes", "")
    out["review_notes"] = notes + APPENDIX
    out["quality_status"] = "reviewed"

    # =========================================================
    # Per-sample review
    # =========================================================

    if sid == "003513":
        # Text: "为什么会被歧视？我觉得尊重是互相的，我不歧视任何群体，我是鄙夷某些行为。"
        # This reads as a defensive personal-opinion statement. "鄙夷某些行为" is a classic
        # "I'm not X but" framing that could be a veiled prejudice, but the text itself is
        # not attacking anyone—it's expressing a principle. No encoding, no direct attack.
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "medium",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本表面是表达个人立场：'我不歧视任何群体，我是鄙夷某些行为'——说话者声称自己秉持互尊原则，将歧视归因于'某些行为'而非群体身份。",
                    "关键短语'鄙夷某些行为'是常见的'not-racist-but'修辞框架，通过把批评对象从群体转向行为来规避直接歧视标签，但'鄙夷'一词仍带有强烈负面态度。"
                ],
                "encoding_analysis": [
                    "无编码机制。文本直接表达了说话者的观点立场，没有使用谐音、隐喻、黑话等任何编码手段。'鄙夷某些行为'属于日常修辞，不是特殊编码。"
                ],
                "context_analysis": [
                    "话题标签为race_reporting暗示文本处于种族讨论语境，但文本本身没有提及任何种族群体。含义高度依赖对话上下文：如果上一句是讨论某群体的具体行为，则'鄙夷某些行为'可能是隐晦的攻击回应。"
                ],
                "supporting_evidence": [
                    "1. 文本没有直接攻击任何群体或个人。",
                    "2. '尊重是互相的'表明说话者强调双向性，立场倾向于非歧视。",
                    "3. '我不歧视任何群体'是明确的反歧视表态。",
                    "4. 文本结构是回应性发言（以'为什么会被歧视？'开头），更可能是参与讨论而非发起攻击。"
                ],
                "counter_evidence": [
                    "1. '鄙夷'一词情感强烈，在种族话题语境下可能暗含'某些行为=某群体的典型行为'的预设，作为隐晦的替代表达。",
                    "2. 缺乏完整上下文——如果前文明确指向某个种族群体，则此句可能是对该群体的间接批评。"
                ],
                "final_rationale": "Risk: none。文本表达个人立场且包含反歧视表态，虽存在'鄙夷某些行为'的模糊措辞，但整体无直接攻击性，证据不足认定存在编码攻击。"
            }
        })

    elif sid == "003514":
        # Text: "差不多，小学的时候班主任也是打拳的，男的打女的抄课文，女的打男的p事没有，结果最后一个学期快结束了全班男生起义"
        # "打拳的" is derogatory slang for feminists (女拳师). Narrative describes a teacher
        # showing gender bias against boys. "全班男生起义" uses humor.
        out.update({
            "risk_level": "medium",
            "encoding_primary": "E1_平台黑话",
            "encoding_secondary": ["D1_反讽"],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "moderate",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本讲述小学经历：班主任是'打拳的'（指女权主义者），对男生女生区别对待——男生犯错罚抄课文，女生犯错无事；最后全班男生'起义'。",
                    "'打拳的'是'女拳师'的缩略，互联网上对积极女权主义者的贬称。'起义'以军事术语幽默夸张描写男生的集体反抗。"
                ],
                "encoding_analysis": [
                    "使用了平台黑话(E1)编码：'打拳的'是中文互联网上对女权主义者的贬义黑话，源自'女拳'（谐音女权+攻击性）。不在贴吧/知乎等平台语境中，此词含义不明确。",
                    "使用了反讽(D1)编码：表面叙述童年轶事，但'p事没有'和'全班男生起义'以戏谑口吻暗示对'打拳的'老师的不认可，实际态度与表面叙述之间存在张力。"
                ],
                "context_analysis": [
                    "贴吧平台中'打拳''拳师'等词高度固化，常用于性别议题论战。文本不需要额外上下文即可判断其使用贬义黑话的意图。",
                    "'起义'一词暗示说话者将男生群体视为被压迫方，立场明确站在男性一侧。"
                ],
                "supporting_evidence": [
                    "1. '打拳的'是贴吧/知乎等平台对女权主义者的固定贬称，具有群体攻击性。",
                    "2. 文本构建了'女生打人没事、男生受罚'的叙事框架，强化'女权特权'刻板印象。",
                    "3. '全班男生起义'将被描述为正义反抗，隐含将女性教师/女权立场视为压迫方的对立叙事。"
                ],
                "counter_evidence": [
                    "1. 文本讲述的是单个教师的个人行为，并非对所有女性的攻击。",
                    "2. 叙述可能是基于真实经历的观察，语言虽带有情绪但不构成严重的仇恨言论。"
                ],
                "final_rationale": "Risk: medium。文本通过E1黑话('打拳的')和D1反讽叙述在性别讨论语境中传递了对女权主义者的贬低态度，但攻击性被包裹在个人经历叙事中。"
            }
        })

    elif sid == "003515":
        # Text: "所谓母亲和母体都是只有一种性别父亲可以多种性别"
        # A factual/linguistic observation about terminology.
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本讨论语言中的性别概念：'母亲'和'母体'（mother/maternal body）只指一种性别，而'父亲'（father）可以指多种性别（可能指现代语境中'父亲'角色的扩展定义）。",
                    "这是对性别术语的语义观察，语气中性，不含攻击或贬低。"
                ],
                "encoding_analysis": [
                    "无编码机制。文本是正常的知识讨论，不使用任何谐音、隐喻、黑话或修辞编码手段。"
                ],
                "context_analysis": [
                    "话题为gender_discussion，可能是在性别议题讨论中发表的学术性/语言哲学性评论。文本本身不参与攻击，仅为概念辨析。"
                ],
                "supporting_evidence": [
                    "1. 文本被ToxiCN标注为非有毒(toxic=0)。",
                    "2. 语言风格为分析性、陈述性，无情感色彩。",
                    "3. 内容聚焦词义辨析，不指向任何群体或个人。"
                ],
                "counter_evidence": [
                    "1. 在激烈性别讨论中，此类'生物学定义'式的发言可能被用作论证工具，但文本本身无害。"
                ],
                "final_rationale": "Risk: none (hard_negative)。纯知识性讨论，无攻击意图，虽话题敏感但内容无害。"
            }
        })

    elif sid == "003516":
        # Text: "西安本地作风彪悍的大多是东边某省逃荒过来的后裔"
        # Regional stereotype: Xi'an locals who are tough are descendants of refugees.
        out.update({
            "risk_level": "medium",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "moderate",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本声称西安本地人中'作风彪悍'（行事野蛮/好斗）的大多是某个东部省份逃荒者的后代。将逃荒背景与'彪悍'负面特质建立因果关联。",
                    "'东边某省'是用模糊指代规避直接点名，但结合'逃荒'（fleeing famine）的历史语境，可能指向河南或山东等地。"
                ],
                "encoding_analysis": [
                    "无特殊编码机制。文本是对地域群体特征的直接陈述式贬损，没有经过谐音、隐喻等包装。'东边某省'是普通的模糊指代，并非平台黑话或隐晦编码。",
                    "当前标注的D1反讽和D2隐喻不适用——文本语气非反讽，也没有建立隐喻映射，只是直接下判断。"
                ],
                "context_analysis": [
                    "知乎平台的地域话题讨论中，'某省'式模糊指代常见，既规避直接点名也增加暗示效果。文本不需要额外上下文即可理解其贬损含义。"
                ],
                "supporting_evidence": [
                    "1. '作风彪悍'在中文语境中常含贬义（粗野、好斗）。",
                    "2. 将负面行为归因于'逃荒后裔'是一种地域/出身决定论，否认个体的独立性。",
                    "3. '大多是'使用全称量化词，形成对某省后裔的群体性判断。"
                ],
                "counter_evidence": [
                    "1. '彪悍'在某些语境下可中性（如'作风彪悍=雷厉风行'），含义不完全确定。",
                    "2. 文本未使用粗俗辱骂词汇，语气相对克制。"
                ],
                "final_rationale": "Risk: medium。文本直接表达了地域刻板印象和出身决定论，将负面特质归于特定地域群体的后裔，但措辞相对克制。"
            }
        })

    elif sid == "003517":
        # "感觉这个吧的吧主好没存在感"
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本表达对贴吧吧主（版主）的观感：'好没存在感'，意思是活跃度低或影响力弱。",
                    "这是贴吧平台常见的用户反馈，语气中性偏调侃，不涉及攻击。"
                ],
                "encoding_analysis": [
                    "无编码机制。普通日常表达，没有使用任何谐音、隐喻、黑话等编码手段。"
                ],
                "context_analysis": [
                    "话题标签为gender_discussion但文本内容与性别完全无关。可能是ToxiCN上下文分类偏差——原帖讨论性别议题但此回帖仅评论吧主存在感。"
                ],
                "supporting_evidence": [
                    "1. 被ToxiCN标注为非有毒(toxic=0)。",
                    "2. 文本内容为对平台管理者的日常评价，无攻击性。"
                ],
                "counter_evidence": [
                    "1. 内容与上下文话题（gender_discussion）脱节，说明此样本的上下文分类可能存在偏差。"
                ],
                "final_rationale": "Risk: none (hard_negative)。贴吧用户对版主的日常评价，无任何攻击性或风险。"
            }
        })

    elif sid == "003518":
        # "可惜亚裔不会反抗，也不团结，要不然不会演变成如今的局面"
        out.update({
            "risk_level": "low",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": True,
            "ambiguity": "medium",
            "evidence_strength": "weak",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本说'亚裔不会反抗，也不团结'——对亚裔群体做出了负面群体性判断（不抵抗、不团结），认为这导致了'如今的局面'（不利处境）。",
                    "语气是惋惜式的批评，但核心是对亚裔群体特征的全称否定判断。"
                ],
                "encoding_analysis": [
                    "无特殊编码机制。文本直接陈述了对亚裔群体的看法，未使用谐音、隐喻等编码。"
                ],
                "context_analysis": [
                    "话题为race_discussion，可能是在讨论反亚裔歧视或亚裔处境时的发言。说话者身份未知——如果是亚裔内部自省，则批评性较弱；如果是非亚裔评论，则攻击性更强。",
                    "需要了解前文讨论的具体情境才能准确判断其意图是善意反思还是恶意攻击。"
                ],
                "supporting_evidence": [
                    "1. '不会反抗，也不团结'是对亚裔群体的负面对比判断。",
                    "2. 文本有victim-blaming（责备受害者）的潜在含义——暗示亚裔处境是他们自身不团结的结果。"
                ],
                "counter_evidence": [
                    "1. 语气偏向惋惜而非攻击，可能是对亚裔群体的反思性呼吁。",
                    "2. 未使用辱骂性词汇或仇恨言论常见修辞（疾病、动物化等）。",
                    "3. 缺乏上下文判断说话者身份和具体语境。"
                ],
                "final_rationale": "Risk: low。文本包含对亚裔群体的负面群体性判断，但语气偏向分析与反思，证据较薄弱，需要更多上下文确定意图。"
            }
        })

    elif sid == "003519":
        # "不是吧，你北京打工除了买不起房难道不让你看病了？"
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本对抱怨北京生活困难的人进行反驳：'除了买不起房难道不让你看病了？'——认为即便在北京买不起房，基本生活保障（看病）仍然可以。",
                    "这是论坛常见的辩论反驳句式，语气带有质疑但无攻击性。"
                ],
                "encoding_analysis": [
                    "无编码机制。普通日常讨论，反问句是正常修辞，非编码手段。"
                ],
                "context_analysis": [
                    "话题为region_discussion，可能是在讨论北京生活压力。文本是辩论性回帖，表达了对过度抱怨的反驳。"
                ],
                "supporting_evidence": [
                    "1. 被ToxiCN标注为非有毒(toxic=0)。",
                    "2. 内容为正常的观点辩论，不针对任何群体。"
                ],
                "counter_evidence": [
                    "1. 无风险证据。正常表达。"
                ],
                "final_rationale": "Risk: none (hard_negative)。正常辩论中的观点表达，无攻击性。"
            }
        })

    elif sid == "003520":
        # "苍蝇不叮无缝蛋，自食恶果。"
        out.update({
            "risk_level": "medium",
            "encoding_primary": "D2_隐喻",
            "encoding_secondary": [],
            "needs_context": True,
            "ambiguity": "high",
            "evidence_strength": "moderate",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本由两条谚语组成：'苍蝇不叮无缝蛋'（问题出在自身）和'自食恶果'（承受自身行为的后果）。",
                    "在种族话题语境中引用这两句谚语，是经典的victim-blaming（责备受害者）修辞——暗示被歧视者自身有问题，'苍蝇'（歧视者）只是被'蛋缝'（受害者的缺点）吸引。"
                ],
                "encoding_analysis": [
                    "使用了隐喻(D2)编码：'苍蝇'和'无缝蛋'构成比喻关系——苍蝇代表批评者/歧视者，蛋代表被批评/被歧视的对象。'蛋有缝'暗示被歧视者自身有缺陷。",
                    "两条谚语组合使用形成递进式的责备逻辑，是高度固化的受害者归因隐喻。"
                ],
                "context_analysis": [
                    "在知乎种族话题下，脱离对话上下文的这两句谚语高度歧义——单纯读起来可以是普遍人生哲理。但在指责受害者的对话语境中，其含义明确表达'被歧视是因为你自身有问题'。",
                    "needs_context=True因为仅凭短文无法确定是指向某个群体还是泛泛而谈。"
                ],
                "supporting_evidence": [
                    "1. '苍蝇不叮无缝蛋'在中文互联网中是最经典的受害者归因隐喻之一。",
                    "2. 与'自食恶果'连用，强化了因果报应逻辑。",
                    "3. 在种族话题语境中引用，其目标指向明确的群体。"
                ],
                "counter_evidence": [
                    "1. 谚语本身是通用表达，在非攻击性语境中也可使用（如自我反思）。",
                    "2. 文本极短且无明确指代词，需要上下文才能确定具体目标。"
                ],
                "final_rationale": "Risk: medium。通过D2隐喻编码使用经典受害者归因谚语，在种族话题语境中传递'被歧视者自身有问题'的隐含信息，但谚语的高度通用性增加了歧义。"
            }
        })

    elif sid == "003521":
        # "得个艾滋病，人生绝对废掉了"
        out.update({
            "risk_level": "medium",
            "encoding_primary": "D2_隐喻",
            "encoding_secondary": ["E3_互动/热点触发"],
            "needs_context": True,
            "ambiguity": "high",
            "evidence_strength": "weak",
            "hard_negative": False,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本说'得个艾滋病，人生绝对废掉了'——字面意思是对艾滋病后果的陈述（患病后人生毁掉）。",
                    "文本中没有出现任何种族群体指代词。如果脱离上下文，这是一个关于疾病后果的陈述（虽有不准确的恐惧渲染）。"
                ],
                "encoding_analysis": [
                    "编码方式为隐喻(D2)：将'艾滋病'作为负面符号来影射某个群体（在种族讨论语境中，可能用于暗示某群体与艾滋病关联）。",
                    "编码方式为热点触发(E3)：文本含义完全取决于对话语境——需要知道前文讨论的具体话题才能判断'艾滋病'在此处指代什么群体。",
                    "当前标注的C4(典故/物品/符号借用)不准确——文本未引用任何典故或文化符号。"
                ],
                "context_analysis": [
                    "话题为race_discussion暗示文本在种族讨论中使用'艾滋病'作为编码攻击，但文本本身零种族词。",
                    "高度依赖前文：如果前文讨论某种族群体时提到'艾滋病'，则此句是编码攻击；如果是在讨论艾滋病政策，则是一般陈述。"
                ],
                "supporting_evidence": [
                    "1. 话题标签为race_discussion，表明上下文为种族讨论。",
                    "2. '人生绝对废掉了'语气绝对化，带有恐惧渲染。"
                ],
                "counter_evidence": [
                    "1. 文本完全没有提及任何种族群体或指代词。",
                    "2. 陈述可在非歧视语境中出现（如讨论疾病危害）。",
                    "3. 艾滋病与种族的关联完全依赖于未提供的上下文。"
                ],
                "final_rationale": "Risk: medium。文本本身不包含种族词，但在种族话题语境中使用'艾滋病'作为隐喻编码，存在指向特定群体的攻击可能，但证据薄弱且高度依赖未提供的上下文。"
            }
        })

    elif sid == "003522":
        # "北京河南山东东北把风头给你整完了，你们也就一个一Q一芭蕾，一q一亏内的保定丽丽能打点"
        out.update({
            "risk_level": "medium",
            "encoding_primary": "F_组合编码",
            "encoding_secondary": ["A2_拼音缩写", "E1_平台黑话"],
            "needs_context": True,
            "ambiguity": "high",
            "evidence_strength": "moderate",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本列出多个地域（北京、河南、山东、东北）后说'把风头给你整完了'，然后出现了'一Q一芭蕾'、'一q一亏内'、'保定丽丽'等不可直接理解的字串。",
                    "'保定丽丽'可能指保定地区的一个具体人物或网络梗。'一Q一芭蕾'和'一q一亏内'看起来是拼音缩写或谐音编码，无法直接推测原义。",
                    "整体结构是：你们其他地方把风头抢完了，你们（保定）只能靠'一Q一芭蕾'和'保定丽丽'来撑场面——暗含贬低保定的竞争力。"
                ],
                "encoding_analysis": [
                    "组合编码(F)：文本混合使用了多种编码手段。'一Q一芭蕾'中的'Q'可能是拼音首字母缩写(A2)，'一q一亏内'也类似。",
                    "'保定丽丽'可能引用网络人物或当地话题(E1平台黑话/互动热点)。编码复杂性高，需要本地知识才能完全解码。",
                    "当前标注的D1反讽和D2隐喻不准确——文本主要是采用模糊编码层而非修辞手法。"
                ],
                "context_analysis": [
                    "文本高度依赖对编码的共享知识。'一Q一芭蕾'和'一q一亏内'可能指向特定方言或内网梗。",
                    "'保定丽丽'可能是一个地方知名人物或网红。文本在知乎地域讨论中出现，使用密集的本地编码来贬低保定地区。"
                ],
                "supporting_evidence": [
                    "1. 文本使用明显的人工编码（Q/q缩写）来包装贬低性内容。",
                    "2. 结构为地域对比型的贬低：你们（保定）没有什么能拿出手的。",
                    "3. 使用'你'直接称呼讨论对方，具有互动攻击性。"
                ],
                "counter_evidence": [
                    "1. 编码的具体含义不透明，无法完全确定是否为攻击性内容。",
                    "2. '保定丽丽'可能是一个正面的本地人物引用。"
                ],
                "final_rationale": "Risk: medium。文本使用F组合编码（含拼音缩写和平台黑话）在地域讨论语境中传递贬低保定的内容，但编码过于复杂导致含义不透明。"
            }
        })

    elif sid == "003523":
        # "这要再加上在山大当过学伴，buff就叠满了"
        out.update({
            "risk_level": "low",
            "encoding_primary": "E3_互动/热点触发",
            "encoding_secondary": ["D1_反讽"],
            "needs_context": True,
            "ambiguity": "medium",
            "evidence_strength": "moderate",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本引用'山大（山东大学）学伴'事件——一位中国女学生被安排给非洲留学生做'学伴'（study buddy）。'buff就叠满了'是游戏术语（多种增益叠加），此处反讽说这种经历集齐了各种争议元素。",
                    "'学伴'制度在2019年引发巨大争议，被批评为对非洲留学生提供特殊优待。引用此事件是在调用一个固化的种族争议热点。"
                ],
                "encoding_analysis": [
                    "热点触发(E3)：引用'山大学伴'这一特定社会热点事件，文本的风险和含义完全绑定于此事件的争议含义。",
                    "反讽(D1)：'buff就叠满了'以游戏术语戏谑地表达'各种争议标签都凑齐了'，表面是游戏化表述，实际是对整体情境的嘲讽。"
                ],
                "context_analysis": [
                    "需要了解'山大学伴'的争议背景才能理解文本的隐含指向——即在批评对外国留学生的特殊待遇政策。纯字面阅读会误解为游戏讨论。"
                ],
                "supporting_evidence": [
                    "1. '山大学伴'事件是与中国非洲留学生政策相关的高争议热点。",
                    "2. '叠buff'的游戏化表述包裹了对该事件的讽刺态度。",
                    "3. 在region_reporting上下文中的引用暗示对地域/种族政策的批评。"
                ],
                "counter_evidence": [
                    "1. 文本本身不对任何群体直接攻击，而是对政策/事件的讽刺。",
                    "2. 可能仅是对社会现象的评论，不表达仇恨或歧视。"
                ],
                "final_rationale": "Risk: low。通过E3热点引用和D1反讽编码对'山大学伴'事件进行游戏化讽刺，攻击对象是事件/政策而非群体，属于社会评论范畴。"
            }
        })

    elif sid == "003524":
        # "墨翟是黑人？你确定说这话的人没疯？"
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本质疑'墨翟是黑人'这一说法，认为说这话的人'疯了'。墨翟（墨子）是春秋战国时期的中国哲学家，此处是对一种历史观点的反驳。",
                    "语气是惊讶和质疑（'没疯？'），针对的是某个历史论断的可信度而非攻击任何群体。"
                ],
                "encoding_analysis": [
                    "无编码机制。普通的知识性质疑，没有使用谐音、隐喻、黑话等编码手段。"
                ],
                "context_analysis": [
                    "话题为race_discussion，可能是在讨论种族历史话题时有人提出'墨子可能是黑人'的争议性观点，文本是对这一观点的反应。"
                ],
                "supporting_evidence": [
                    "1. 被ToxiCN标注为非有毒(toxic=0)。",
                    "2. '你确定说这话的人没疯'质疑的是论断的可信度，非攻击群体。"
                ],
                "counter_evidence": [
                    "1. 无风险证据。正常讨论。"
                ],
                "final_rationale": "Risk: none (hard_negative)。对历史论断的真实性质疑，无攻击性。"
            }
        })

    elif sid == "003525":
        # "找了个帅的白人，再找个丑的国人。然后放在一起比较，说中国男人就是比欧美男人丑，有意思吗？"
        out.update({
            "risk_level": "low",
            "encoding_primary": "E3_互动/热点触发",
            "encoding_secondary": [],
            "needs_context": True,
            "ambiguity": "low",
            "evidence_strength": "moderate",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本揭露了一种不公平的比较方式：选一个好看的白人和一个丑的中国人做对比，然后得出'中国男人比欧美男人丑'的结论。反问'有意思吗？'表达对此类做法的批判。",
                    "关键词是'有意思吗？'——这是典型的反偏见修辞，揭露方法论偏差后的质疑。"
                ],
                "encoding_analysis": [
                    "热点触发(E3)：文本是对他人言论的引用和批评（你方...说...），属于报道/揭露型表达。",
                    "当前标注的D1反讽不准确——文本不是讽刺，而是直接揭露逻辑谬误。"
                ],
                "context_analysis": [
                    "文本是对另一个帖子的回应，引用了对方的论证方式。仅看本句可判断为反偏见立场，但需要前文确认所揭露的'对方'具体言论。"
                ],
                "supporting_evidence": [
                    "1. '找个帅的白人，再找个丑的国人'描述了有偏见的对比方法。",
                    "2. '有意思吗？'表达了对这种偏见操作的不认同。",
                    "3. 结构为揭露型：描述不当做法+反问质疑。"
                ],
                "counter_evidence": [
                    "1. 文本也使用了'丑的国人'这一标签化表达，可能强化'中国人丑'的联想。",
                    "2. 需要上下文确认被引用方是否存在。"
                ],
                "final_rationale": "Risk: low。文本作为揭露和反驳偏见对比的报道型发言，虽有'丑的国人'的引用措辞，但整体立场为反偏见。"
            }
        })

    elif sid == "003526":
        # Long narrative about "黑小子" (black kid) and study buddies
        out.update({
            "risk_level": "high",
            "encoding_primary": "D1_反讽",
            "encoding_secondary": ["literal_keyword"],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "strong",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本以一个虚构故事的形式描写'黑小子'从出生到上学的经历：'黑小子'学习费劲、考试倒数、没朋友，学校安排女'学伴'给他，女学生怀孕给加学分保研。",
                    "关键词：'黑小子'（黑人小孩）、'学习东西很费劲，考试总是最后一名'（智力低下刻板印象）、'每个黑小子要配上2个以上的女学生做学伴'（暗示性服务）、'怀孕了还给加学分保研'（性交易暗示）。"
                ],
                "encoding_analysis": [
                    "反讽(D1)：整段用构建的虚构故事进行反讽，表面是叙事，实际是对黑人留学生政策的种族主义攻击。",
                    "直接文字攻击(literal_keyword)：'黑小子'直接指代黑人群体，'学习东西很费劲，考试总是最后一名'等是对黑人群体的直接负面刻板印象陈述，无编码包装。",
                    "当前标注的D2隐喻不足以描述——文本不是隐喻，而是直接使用'黑小子'作为种族指代构建攻击性场景。"
                ],
                "context_analysis": [
                    "知乎平台常见此类用虚构叙事来影射种族政策的文体。文本自身提供了完整的攻击框架，不需要额外上下文即可判断。",
                    "结尾表情😆表明叙述者将此故事视为好笑/嘲讽的对象，进一步确认攻击立场。"
                ],
                "supporting_evidence": [
                    "1. '黑小子'直接指代黑人群体。",
                    "2. '学习东西很费劲，考试总是最后一名'——黑人智力低下的刻板印象。",
                    "3. '每个黑小子要配上2个以上的女学生做学伴'——将黑人男性性化为对华女性的威胁。",
                    "4. '不小心怀孕了学校还给加学分保研'——暗示中国教育机构纵容性交易。"
                ],
                "counter_evidence": [
                    "1. 文本采用了虚构故事的形式，理论上可辩解为'笑话'或'讽刺创作'。"
                ],
                "final_rationale": "Risk: high。文本通过虚构叙事(D1反讽)直接使用'黑小子'对黑人群体发起多重种族主义攻击（智力低下、性威胁、特殊优待），含有明确的直接攻击文字。"
            }
        })

    elif sid == "003527":
        # Long text about 清道夫 (suckerfish) - fish metaphor
        out.update({
            "risk_level": "high",
            "encoding_primary": "D2_隐喻",
            "encoding_secondary": ["literal_keyword"],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "strong",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本表面是对清道夫鱼（plecostomus）的抱怨：'又黑、骨头又多、不好吃、繁殖快、吃本土鱼卵、对渔业没贡献、挤压本土鱼生存空间'。",
                    "关键触发词：'又黑'明确点名肤色特征。'清道夫'（垃圾鱼）作为贬称。'简直就是一群没有用的垃圾'——强烈的灭绝性表述。'希望把这些清道夫全部弄死'——暴力消灭诉求。",
                    "在种族话题上下文中，'清道夫'作为对黑人群体的种族隐喻——入侵者、无用者、破坏生态者。"
                ],
                "encoding_analysis": [
                    "隐喻(D2)：整段使用清道夫鱼作为黑人群体的喻体。'又黑'是人类肤色描述而非鱼的特征，泄露了隐喻的真实指向。'繁殖快、吃本土鱼卵、挤压生存空间'映射种族主义的'大置换'(great replacement)阴谋论。",
                    "直接攻击文字(literal_keyword)：'没有用的垃圾''希望全部弄死'——这些是直接的语言暴力表达，经过了鱼的比喻层但仍保留直接暴力性。"
                ],
                "context_analysis": [
                    "在race_discussion话题下，此类以动物隐喻种族的文本是常见的种族主义编码方式。'又黑'明确指向种族而非鱼类。",
                    "不需要额外上下文即可判断——文本自身内部的'又黑'泄露了解码的关键。"
                ],
                "supporting_evidence": [
                    "1. '又黑'直接指向肤色，是隐喻的破绽点。",
                    "2. '繁殖快、吃本土鱼卵、挤压生存空间'暗含'大置换'阴谋论框架。",
                    "3. '没有用的垃圾'是直接的人格贬损。",
                    "4. '希望把这些清道夫全部弄死'包含暴力消灭诉求。"
                ],
                "counter_evidence": [
                    "1. 表面字义确实是讲鱼，如果脱离'race_discussion'话题标签，单纯读作钓鱼抱怨也有合理之处。"
                ],
                "final_rationale": "Risk: high。通过D2隐喻编码使用'清道夫'作为黑人群体的种族主义喻体，结合'又黑''没有用的垃圾''希望全部弄死'等直接攻击性文字，构成了清晰的种族仇恨内容。"
            }
        })

    elif sid == "003528":
        # "看不懂，只知道可以透。"
        out.update({
            "risk_level": "high",
            "encoding_primary": "literal_keyword",
            "encoding_secondary": ["E1_平台黑话"],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "strong",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本说'看不懂，只知道可以透'——表示不理解前文内容，但知道可以'透'。",
                    "'透'是贴吧/互联网上的粗俗俚语，指性交。此处对某个对象（在性别话题语境下为女性）进行性物化。"
                ],
                "encoding_analysis": [
                    "直接使用攻击性词汇(literal_keyword)：'透'在中文互联网语境中是直接表达性行为的粗俗词汇。",
                    "平台黑话(E1)：'透'作为'性交'的俚语表达在贴吧特定社区固化使用，跨出该平台后含义可能模糊。",
                    "当前标注的E1/D3可以接受——'透'既是平台黑话也是借代用法。"
                ],
                "context_analysis": [
                    "在性别讨论话题下，'看不懂，只知道可以透'的'可以透'指涉的是出现在前文中的女性。不需要额外上下文即可判断其性物化意图。"
                ],
                "supporting_evidence": [
                    "1. '透'是贴吧固化的性交粗俗俚语。",
                    "2. '只知道可以透'表明说话者将讨论对象仅视为性对象。",
                    "3. 在gender_discussion语境中，目标对象为女性群体。"
                ],
                "counter_evidence": [
                    "1. 文本极短，'透'在不同方言中有不同含义（如'说透'=解释清楚），但互联网语境下含义明确。"
                ],
                "final_rationale": "Risk: high。文本使用粗俗俚语'透'(literal_keyword+E1)对女性进行性物化，攻击意图直接明确。"
            }
        })

    elif sid == "003529":
        # "这我倒没话说，看起来那些双标的男人好多了"
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": True,
            "ambiguity": "high",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本说'那些双标的男人好多了'——'双标的男人'指双重标准的男性。'这我倒没话说'表示对某个前文的赞同或不反驳。",
                    "文本比较了'双标的男人'与某个未指明的对比对象，认为前者'好多了'。没有提及任何种族群体。"
                ],
                "encoding_analysis": [
                    "无编码机制。文本为普通的比较表达，'双标的男人'是日常用语。",
                    "当前标注的D2隐喻和D1反讽不适用——文本没有使用比喻或反讽。"
                ],
                "context_analysis": [
                    "话题标签为race_discussion但文本内容为性别讨论（'男人'）。缺乏核心上下文：'这'指代什么？比较对象是谁？",
                    "高度依赖前文——没有'这'的指代无法理解全句含义。"
                ],
                "supporting_evidence": [
                    "1. 话题标签与文本内容不一致（race vs 性别）。",
                    "2. 文本未涉及任何种族内容。"
                ],
                "counter_evidence": [
                    "1. '双标的男人'在语境中可能是对特定群体男性（如某种族男性）的代称，但文本无证据支撑此解读。",
                    "2. 文本太短且高度依赖代词指代，无法做出有信心的判断。"
                ],
                "final_rationale": "Risk: none (hard_negative)。文本不包含可识别的攻击性内容，'双标的男人'虽含贬义但在日常讨论中常见，且话题标签与内容可能不匹配。"
            }
        })

    elif sid == "003530":
        # "可是世界女权组织背后谁给拿钱啊..."
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本质疑女权组织的资金来源(「世界女权组织背后谁给拿钱啊」)，认为网络上的男女对立被刻意放大(「各个问题引导你来回答男女问题」)，与实际生活感受不符。",
                    "表达的是对性别议题被操纵的怀疑论观点，属于社会评论。"
                ],
                "encoding_analysis": [
                    "无编码机制。文本为直接表达个人观点的社会评论，未使用任何编码手段。"
                ],
                "context_analysis": [
                    "话题标签为race_discussion但文本内容为性别讨论。话题标签与内容可能不匹配。"
                ],
                "supporting_evidence": [
                    "1. 被ToxiCN标注为非有毒(toxic=0)。",
                    "2. 内容为观点表达，不攻击任何群体。"
                ],
                "counter_evidence": [
                    "1. 文本包含对女权运动的质疑，在性别讨论中可能被视为anti-feminist。"
                ],
                "final_rationale": "Risk: none (hard_negative)。社会评论观点表达，不包含攻击性内容。"
            }
        })

    elif sid == "003531":
        # "感觉你这种加上省名的也算地域黑…隐隐约约透露出'皖乃穷鬼'的气息…"
        out.update({
            "risk_level": "low",
            "encoding_primary": "E3_互动/热点触发",
            "encoding_secondary": [],
            "needs_context": True,
            "ambiguity": "low",
            "evidence_strength": "moderate",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本批评某人'加上省名的也算地域黑'（在提到省份名称时带有地域歧视），并引用'皖乃穷鬼'（安徽人是穷鬼）作为对方言论的概括。",
                    "结构是meta-critique：甲批评乙的地域歧视言论。'皖乃穷鬼'是乙言论的概括引用，非甲自己的主张。"
                ],
                "encoding_analysis": [
                    "热点触发(E3)：文本是对他人言论的揭露和批评，属于报道/转述型。'皖乃穷鬼'是引用对方的地域歧视言论来分析。",
                    "当前标注的D1反讽不适用——文本不是反讽，而是直接批评。"
                ],
                "context_analysis": [
                    "需要前文确认被批评方的原话是否存在。文本是对话中的回应性发言。"
                ],
                "supporting_evidence": [
                    "1. '也算地域黑'明确使用了'地域黑'（地域歧视）标签，立场是反对地域歧视的。",
                    "2. '皖乃穷鬼'被作为负面例子引用，不是甲本人的观点。",
                    "3. 整体结构为反偏见报道。"
                ],
                "counter_evidence": [
                    "1. '皖乃穷鬼'的文字出现在输出中，即使作为引用也可能强化刻板印象。"
                ],
                "final_rationale": "Risk: low。文本是揭露和批评地域歧视的报道型发言，立场为反偏见，风险仅来自引用的歧视性内容。"
            }
        })

    elif sid == "003532":
        # "在上海，最被歧视的是上海人"
        out.update({
            "risk_level": "low",
            "encoding_primary": "E3_互动/热点触发",
            "encoding_secondary": [],
            "needs_context": True,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本说'在上海，最被歧视的是上海人'——一个关于歧视格局的观察性/评论性陈述。表达的是'上海人被外地人歧视'或'上海本地人在上海被边缘化'的观点。",
                    "这是一个反转常规定义（通常说外地人在上海被歧视）的辩论性观点。"
                ],
                "encoding_analysis": [
                    "热点触发(E3)：文本是对歧视现象的观察评论，属于报道/分析型表达，非攻击性语言。"
                ],
                "context_analysis": [
                    "需要前文了解讨论的具体语境——是比较各地歧视现象还是讨论上海的社会变迁。"
                ],
                "supporting_evidence": [
                    "1. 结构为评论分析而非攻击。",
                    "2. '最被歧视的是'是观察性表述。"
                ],
                "counter_evidence": [
                    "1. 可能被解读为'上海人受害者论'，在讨论中可能转移对真正受歧视群体的关注。"
                ],
                "final_rationale": "Risk: low。对歧视格局的观察性评论，非攻击性语言，属于报道/分析类型。"
            }
        })

    elif sid == "003533":
        # "这货应该是虫混而且她基因就是虫混..."
        out.update({
            "risk_level": "high",
            "encoding_primary": "literal_keyword",
            "encoding_secondary": ["D3_借代"],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "strong",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本攻击某人：称其为'虫混'（虫子混血，对混血儿的恶意贬称）、攻击其基因、攻击其用修图软件将'绵羊卷毛头发'修直、将'黑咖啡色皮肤'修成暗黄。",
                    "'虫混'是侮辱性极强的新造词——将混血儿比作昆虫杂交。'绵羊卷毛头发'和'黑咖啡色皮肤'是对卷发和深色肤色的物理特征攻击。"
                ],
                "encoding_analysis": [
                    "直接使用攻击性词汇(literal_keyword)：'虫混'是对混血儿的直接贬义造词，将人比作虫类杂交。",
                    "当前标注的D2隐喻和D1反讽严重低估了文本的攻击性——这不是隐晦表达，而是露骨的种族攻击。"
                ],
                "context_analysis": [
                    "贴吧平台种族话题下的人身攻击。文本自身提供了完整的攻击内容（面部特征+肤色+血统），不需要额外上下文。"
                ],
                "supporting_evidence": [
                    "1. '虫混'是恶意贬称，将混血儿比作昆虫杂交。",
                    "2. '把它的绵羊卷毛头发修成直发'攻击肤色特征。",
                    "3. '黑咖啡色皮肤修成暗黄皮肤'攻击肤色。",
                    "4. 用'这货''它'而非人称代词，表达蔑视。"
                ],
                "counter_evidence": [
                    "1. 无—文本的攻击性质和指向极其明确。"
                ],
                "final_rationale": "Risk: high。文本使用'虫混'(literal_keyword)等直接攻击性词汇对混血个体进行种族特征攻击（肤色、发质、血统），攻击意图和指向极其明确。"
            }
        })

    elif sid == "003534":
        # "已经举报这个帖主，感谢"
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本说'已经举报这个帖主，感谢'——表示已经举报了帖子作者，并对某人表示感谢。",
                    "内容为平台管理行为，无攻击性。"
                ],
                "encoding_analysis": [
                    "无编码机制。日常表达。"
                ],
                "context_analysis": [
                    "话题标签gender_discussion但内容不涉及性别——可能是对某个违规帖子/用户的举报响应。"
                ],
                "supporting_evidence": [
                    "1. 被ToxiCN标注为非有毒(toxic=0)。",
                    "2. '举报'是正当平台行为。"
                ],
                "counter_evidence": [
                    "1. 无风险证据。"
                ],
                "final_rationale": "Risk: none (hard_negative)。平台举报行为的正常表达，无风险。"
            }
        })

    elif sid == "003535":
        # "东北跟山东是兄弟？呵呵 黑东北最多的就是山东..."
        out.update({
            "risk_level": "low",
            "encoding_primary": "E3_互动/热点触发",
            "encoding_secondary": [],
            "needs_context": True,
            "ambiguity": "low",
            "evidence_strength": "moderate",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本反驳'东北跟山东是兄弟'的说法，声称'黑东北最多的就是山东'（黑=地域攻击），并引用网易新闻评论区山东人攻击东北现象的观察。",
                    "结构是：反驳一个友好观点 + 提出反例（山东人攻击东北人最多）+ 引用证据。"
                ],
                "encoding_analysis": [
                    "热点触发(E3)：文本是对地域攻击现象的观察报告，属于报道/分析型。提供具体平台（网易）和内容类型（东北新闻）作为证据。",
                    "当前标注的D1反讽不适用——文本是直接反驳而非讽刺。"
                ],
                "context_analysis": [
                    "需要确认前文中'东北跟山东是兄弟'这句话是否确实存在。文本以'呵呵'开头表达不认同，语气带有情绪。"
                ],
                "supporting_evidence": [
                    "1. '黑东北'中的'黑'指的是地域攻击（黑=贬低/攻击），文本是在报告这种攻击现象。",
                    "2. 提供了具体观察来源（网易东北新闻评论区）。"
                ],
                "counter_evidence": [
                    "1. '黑东北最多的就是山东'本身可能构成对山东人的地域概括。",
                    "2. 文本情绪较强，可能是在参与而非仅报告地域争论。"
                ],
                "final_rationale": "Risk: low。文本以报道和反驳的形式讨论地域攻击现象，虽有'山东人黑东北'的概括但整体为讨论型内容。"
            }
        })

    elif sid == "003536":
        # "是的，没有哪个省的人是应该被黑的"
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": True,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本说'没有哪个省的人是应该被黑的'——表达地域歧视是错误的立场。'是的'表示同意前文观点。",
                    "这是明确的反对地域歧视的声明。"
                ],
                "encoding_analysis": [
                    "无编码机制。反歧视的直白表达。"
                ],
                "context_analysis": [
                    "是回应性发言，'是的'表明同意前文。讨论地域歧视的语境。"
                ],
                "supporting_evidence": [
                    "1. '没有哪个省的人是应该被黑的'明确表达了反地域歧视立场。"
                ],
                "counter_evidence": [
                    "1. 无风险证据。"
                ],
                "final_rationale": "Risk: none (hard_negative)。明确的反对地域歧视声明。"
            }
        })

    elif sid == "003537":
        # "盗视频投自制（我联系视频原创官方人家说没有给任何个人账号原视频）用贴纸故意p掉女方无理取闹标题有钓鱼执法嫌疑"
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本描述了一个视频被抄袭和恶意篡改的事件：盗用视频、伪装原创、P掉水印、标题有钓鱼执法嫌疑。",
                    "内容为内容侵权举报，不包含攻击性。"
                ],
                "encoding_analysis": [
                    "无编码机制。事件描述性语言。"
                ],
                "context_analysis": [
                    "话题标签gender_discussion但内容与性别无关。可能是对某个涉及女性的视频版权纠纷的讨论。"
                ],
                "supporting_evidence": [
                    "1. 被ToxiCN标注为非有毒(toxic=0)。",
                    "2. 内容为侵权事件描述。"
                ],
                "counter_evidence": [
                    "1. 无风险证据。"
                ],
                "final_rationale": "Risk: none (hard_negative)。内容侵权事件的正常描述，无风险。"
            }
        })

    elif sid == "003538":
        # "女⭕️师和泥鸽。导致艾资也不少"
        out.update({
            "risk_level": "high",
            "encoding_primary": "E1_平台黑话",
            "encoding_secondary": ["F_组合编码"],
            "needs_context": False,
            "ambiguity": "medium",
            "evidence_strength": "strong",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本包含三个编码词：'女⭕️师'（女拳师/女权主义者，⭕️替代'拳'字）、'泥鸽'（编码词，可能指LGBTQ群体或某个群体代称）、'艾资'（艾滋病资金或艾滋病相关编码）。",
                    "核心攻击逻辑：女权主义者和'泥鸽'（某群体）导致艾滋病相关的负面后果。"
                ],
                "encoding_analysis": [
                    "平台黑话(E1)：'女⭕️师'是'女拳师'的变体（用符号替代汉字），为贴吧对女权主义者的固定贬称。",
                    "组合编码(F)：'泥鸽'可能是谐音编码（泥=你/N？鸽=某词的谐音？），也可能是特定社区黑话，需要深入社区知识才能完全解码。'艾资'可能是'艾滋病'的缩写。",
                    "当前标注的D1反讽不合适——文本不是讽刺，而是直接使用多个编码词进行攻击。"
                ],
                "context_analysis": [
                    "话题为lgbt_discussion，表明'泥鸽'很可能指向LGBTQ群体。'艾资'（艾滋病）是常见的针对LGBTQ的攻击关联。",
                    "贴吧平台使用符号替代汉字（⭕️）是常见的规避审查编码。"
                ],
                "supporting_evidence": [
                    "1. '女⭕️师'是女权主义者的贬义黑话。",
                    "2. '泥鸽'在lgbt话题语境中指向LGBTQ群体。",
                    "3. '艾资'将目标群体与艾滋病负面关联。",
                    "4. 使用符号替代汉字(⭕️)表明刻意编码。"
                ],
                "counter_evidence": [
                    "1. '泥鸽'的具体含义不完全透明，存在解读误差。",
                    "2. 文本极短，缺乏完整论证链条。"
                ],
                "final_rationale": "Risk: high。文本使用E1平台黑话和F组合编码对女权主义者和LGBTQ群体进行密集编码攻击（'女⭕️师''泥鸽''艾资'），将目标群体与艾滋病负面关联。"
            }
        })

    elif sid == "003539":
        # "一看它们又是再到处传染各种各样вирус"
        out.update({
            "risk_level": "high",
            "encoding_primary": "A4_外语谐音",
            "encoding_secondary": ["literal_keyword"],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "strong",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本说'它们'（中性/动物性代词，通常不用于人）'到处传染各种各样вирус'（俄语'病毒'）。",
                    "'它们'将目标群体去人化（用动物代词）。'传染病毒'使用经典的疾病隐喻——将目标群体等同于传染源。使用俄语'вирус'替代中文'病毒'是一种规避审查的编码策略。"
                ],
                "encoding_analysis": [
                    "外语谐音(A4)：使用俄语'вирус'（病毒）替代中文词，既增加了理解门槛也规避了关键词过滤。",
                    "直接攻击词汇(literal_keyword)：'它们'（动物代词去人化）、'到处传染'（疾病传播指控）是直接攻击。",
                    "当前标注的D2隐喻不足以描述编码复杂度——文本核心是使用外语作为编码层(A4)，而非中文隐喻。"
                ],
                "context_analysis": [
                    "话题为race_discussion，指向种族群体。疾病隐喻（传染病毒）是种族主义中最古老的仇恨编码之一。",
                    "不需要额外上下文即可判断——'它们'去人化 + 疾病传播指控构成完整的仇恨逻辑。"
                ],
                "supporting_evidence": [
                    "1. '它们'使用动物/物体代词，去人化目标群体。",
                    "2. '到处传染'使用疾病传播框架。",
                    "3. 'вирус'使用俄语替代中文，是刻意编码。",
                    "4. 疾病-传染隐喻是种族仇恨的经典模式。"
                ],
                "counter_evidence": [
                    "1. 在非种族语境中（如讨论生物安全），'传染病毒'可以是中性描述。"
                ],
                "final_rationale": "Risk: high。文本使用A4外语谐音编码(вирус)结合去人化代词('它们')和疾病传播指控('到处传染')，构成对种族群体的经典仇恨攻击。"
            }
        })

    elif sid == "003540":
        # "面对公开的外人评论。可谓是最公开公正了。"
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": True,
            "ambiguity": "high",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本说'面对公开的外人评论。可谓是最公开公正了'——意思是在公开的外人评论面前，可以说是最公开公正的。",
                    "文本非常简短且抽象，含义模糊。可能是正面的肯定（评论处理公正）也可能是反讽（说公正其实不公正）。"
                ],
                "encoding_analysis": [
                    "无编码机制。文本短且平淡，未见任何编码手段。"
                ],
                "context_analysis": [
                    "话题标签lgbt_discussion但文本内容与LGBTQ无直接关联。文本高度依赖前文来理解'外人评论'和'公开公正'的具体所指。"
                ],
                "supporting_evidence": [
                    "1. 被ToxiCN标注为非有毒(toxic=0)。"
                ],
                "counter_evidence": [
                    "1. 文本太短且高度歧义，无法做出有信心判断。",
                    "2. 可能是反讽（表面说公开公正实际批评），但无文本证据。"
                ],
                "final_rationale": "Risk: none (hard_negative)。文本过于简短模糊，无法识别风险内容。"
            }
        })

    elif sid == "003541":
        # "没办法，我们黑龙江人口流失严重不说还不靠海岸线..."
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本描述黑龙江的困境：人口流失、无海岸线、邻国只有稀疏的俄罗斯远东地区。用'姥姥不疼舅舅不爱'（俗语：没人关心）自嘲。",
                    "这是对家乡困境的感慨，语气无奈，无攻击性。"
                ],
                "encoding_analysis": [
                    "无编码机制。日常感叹。'姥姥不疼舅舅不爱'是普通俗语，非编码。"
                ],
                "context_analysis": [
                    "在讨论区域发展的语境下发表的感慨性发言。"
                ],
                "supporting_evidence": [
                    "1. 被ToxiCN标注为非有毒(toxic=0)。",
                    "2. 内容为对本地困境的客观描述。"
                ],
                "counter_evidence": [
                    "1. 无风险证据。"
                ],
                "final_rationale": "Risk: none (hard_negative)。对家乡困境的客观描述和自嘲，无攻击性。"
            }
        })

    elif sid == "003542":
        # "中国一带一路战略就是投资那些地方..."
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本讨论一带一路战略的经济效益分配：收益归资本巨头，普通人只能吃发展红利，其他国家'说不定过的比我们好'。",
                    "这是对政策经济影响的讨论，无攻击性。"
                ],
                "encoding_analysis": [
                    "无编码机制。政策讨论型表达。"
                ],
                "context_analysis": [
                    "在race_discussion话题下'那些地方'可能指代特定种族区域，但文本本身为经济讨论。"
                ],
                "supporting_evidence": [
                    "1. 被ToxiCN标注为非有毒(toxic=0)。",
                    "2. 内容为经济政策讨论。"
                ],
                "counter_evidence": [
                    "1. '那些地方'在种族话题语境下可能隐射种族区域。"
                ],
                "final_rationale": "Risk: none (hard_negative)。经济政策讨论，无攻击性内容。"
            }
        })

    elif sid == "003543":
        # "找代孕不香吗，干嘛找个女人收割自己"
        out.update({
            "risk_level": "medium",
            "encoding_primary": "D1_反讽",
            "encoding_secondary": ["E1_平台黑话"],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "moderate",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本说'找代孕不香吗，干嘛找个女人收割自己'——反讽地建议男人找代孕替代结婚找女人，并认为女人会'收割'（欺骗/剥削）男人。",
                    "'收割'（harvest/reap）是网络俚语，指被利用或欺骗。'不香吗'是反问句式：代孕更好。"
                ],
                "encoding_analysis": [
                    "反讽(D1)：'找代孕不香吗'表面是提供替代方案建议，实际是对婚姻/女性的贬低——暗示女性只会'收割'男人。",
                    "平台黑话(E1)：'收割'在网络用语中指利用/欺骗他人获取利益。",
                    "当前标注的E1/D3大致合理但D1应为primary。"
                ],
                "context_analysis": [
                    "在性别讨论语境中对女性群体进行贬低。不需要额外上下文即可判断其misogyny倾向。"
                ],
                "supporting_evidence": [
                    "1. '收割自己'暗示女性是剥削者的负面形象。",
                    "2. '代孕'作为婚姻的替代方案暗示女性仅具生育功能。",
                    "3. 反问句式'不香吗'以劝导口吻包装了针对女性的攻击。"
                ],
                "counter_evidence": [
                    "1. 文本是对婚姻制度的批评而非直接攻击女性。",
                    "2. 语气偏调侃/吐槽，严重性有限。"
                ],
                "final_rationale": "Risk: medium。通过D1反讽和E1黑话('收割')贬低女性在婚姻中的作用，将女性塑造为剥削者，但攻击间接且以调侃口吻包装。"
            }
        })

    elif sid == "003544":
        # "黑人为什么出不了科学家？因为黑人没有进化完全，四肢发达，头脑简单..."
        out.update({
            "risk_level": "high",
            "encoding_primary": "literal_keyword",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "strong",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本以问答形式陈述：'黑人为什么出不了科学家？'然后回答因为'黑人没有进化完全，四肢发达，头脑简单'，还说'科学这种高大上的东西，他们理解不了'。",
                    "这是教科书式的种族主义：声称黑人在进化上低于其他人种、智力低下、无法理解复杂事物。"
                ],
                "encoding_analysis": [
                    "直接使用攻击性词汇(literal_keyword)：文本直接使用'黑人'作为目标并直接陈述'没有进化完全''四肢发达头脑简单''理解不了'，未经任何编码包装。",
                    "当前标注的C4(典故/物品/符号借用)不适用——文本未使用典故或符号。"
                ],
                "context_analysis": [
                    "贴吧种族话题下的直接的种族主义宣言。"
                ],
                "supporting_evidence": [
                    "1. '黑人'明确指定攻击目标。",
                    "2. '没有进化完全'——进化等级论（黑人低于其他人种）。",
                    "3. '四肢发达，头脑简单'——智力低下刻板印象。",
                    "4. '科学这种高大上的东西，他们理解不了'——直接否定黑人的认知能力。"
                ],
                "counter_evidence": [
                    "1. 无防御性解释的空间。"
                ],
                "final_rationale": "Risk: high。使用literal_keyword对黑人群体进行直接的种族主义智力贬低（进化不完全、四肢发达头脑简单），无任何编码包装。"
            }
        })

    elif sid == "003545":
        # "张华考上了北京大学，李萍进了中等技术学校，猩猩被引进了国内高端大学..."
        out.update({
            "risk_level": "high",
            "encoding_primary": "C4_典故/物品/符号借用",
            "encoding_secondary": ["literal_keyword"],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "strong",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本借用经典名句'张华考上了北京大学，李萍进了中等技术学校，我在百货公司当售货员，我们都有光明的前途'，将'我'替换为'猩猩被引进了国内高端大学'。",
                    "'猩猩'在此上下文中是种族歧视词，将黑人比作猩猩（类人猿）。'他们都有光明的未来[拥抱]🐶'是反讽。"
                ],
                "encoding_analysis": [
                    "典故借用(C4)：套用了中国教科书中的经典句式来包装新的歧视性内容。原句是教育平等的隐喻，被篡改为种族攻击。",
                    "直接攻击文字(literal_keyword)：'猩猩'在种族语境中是对黑人的直接侮辱性称呼（人猿类比）。",
                    "当前标注的D2隐喻不够准确——核心是借用文化典故(C4)和直接侮辱(literal_keyword)。"
                ],
                "context_analysis": [
                    "贴吧种族话题下的经典句式改编。'猩猩'在中文互联网上是对黑人的极端贬称。句尾表情[拥抱]🐶增强反讽效果。"
                ],
                "supporting_evidence": [
                    "1. '猩猩'是中文互联网对黑人的种族主义贬称（人猿类比）。",
                    "2. 套用经典名言框架增强传播效果。",
                    "3. '被引进了国内高端大学'暗示黑人靠特殊政策而非实力入学。",
                    "4. '[拥抱]🐶'表情符号增强嘲讽效果。"
                ],
                "counter_evidence": [
                    "1. '猩猩'字面指动物，在非种族语境中仅为动物名。"
                ],
                "final_rationale": "Risk: high。通过C4典故借用和literal_keyword('猩猩')将对黑人的人猿类比嵌入经典文化句式，构成高毒性的种族攻击。"
            }
        })

    elif sid == "003546":
        # "黑人智力≥70，沃森诚不欺我！"
        out.update({
            "risk_level": "high",
            "encoding_primary": "literal_keyword",
            "encoding_secondary": ["C4_典故/物品/符号借用"],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "strong",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本直接陈述'黑人智力≥70'，并引用詹姆斯·沃森（James Watson，因种族智商言论被撤职的诺贝尔奖得主）作为权威背书。",
                    "'智力≥70'暗示黑人智力低下（70是临床智力障碍的临界值）。'诚不欺我'是以反讽口吻表示赞同。"
                ],
                "encoding_analysis": [
                    "直接攻击词汇(literal_keyword)：'黑人智力≥70'直接对黑人群体进行智力水平的负面判断，无编码包装。",
                    "典故借用(C4)：引用詹姆斯·沃森（James Watson）——一个有争议的科学家，其关于种族和智商的言论被广泛批评为种族主义。",
                    "当前标注的D2隐喻不准确——文本未使用隐喻手法，而是直接陈述。"
                ],
                "context_analysis": [
                    "贴吧种族话题下引用'权威'来加强种族智商论的文本。不需要额外上下文即可判断。"
                ],
                "supporting_evidence": [
                    "1. '黑人智力≥70'直接对黑人群体进行智力贬低。",
                    "2. '沃森'引用一个有争议的种族智商论点作为背书。",
                    "3. '诚不欺我'表达对种族智商论的赞同。"
                ],
                "counter_evidence": [
                    "1. '沃森诚不欺我'可能是反讽（讽刺性地引用一个被取消的科学家）。但语句的正面语气使反讽解读较牵强。"
                ],
                "final_rationale": "Risk: high。使用literal_keyword直接陈述'黑人智力≥70'的种族智商论，并引用沃森(C4)作为背书，构成明确的种族贬低。"
            }
        })

    elif sid == "003547":
        # "典型的幸存者偏差，混血儿丑八怪的多了去了，人们都只漂亮的几个看"
        out.update({
            "risk_level": "high",
            "encoding_primary": "literal_keyword",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "strong",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本说混血儿中'丑八怪'很多，人们只看到漂亮的几个——这是'幸存者偏差'。",
                    "'混血儿丑八怪'是对混血群体外貌的直接贬低。'多了去了'（数量很多）是全称化表述。"
                ],
                "encoding_analysis": [
                    "直接攻击词汇(literal_keyword)：'混血儿丑八怪'直接使用贬义词'丑八怪'对混血群体进行外貌攻击。无编码包装。",
                    "当前标注的C4(典故/物品/符号借用)不适用——文本未使用典故或符号。"
                ],
                "context_analysis": [
                    "知乎种族话题下的对混血群体的直接外貌攻击。不需要上下文。"
                ],
                "supporting_evidence": [
                    "1. '混血儿丑八怪'直接使用贬义词'丑八怪'进行外貌攻击。",
                    "2. '多了去了'制造'混血儿普遍丑'的假象。",
                    "3. 用'幸存者偏差'伪装成理性分析。"
                ],
                "counter_evidence": [
                    "1. 文本结构为'某种偏差+举例+批评'，可被解读为对美化混血儿现象的批评。"
                ],
                "final_rationale": "Risk: high。使用literal_keyword('混血儿丑八怪')对混血群体进行直接外貌贬低，用'幸存者偏差'伪装为理性分析。"
            }
        })

    elif sid == "003548":
        # "对啊，我长这么大压根没见到过女性和黑人在一起的..."
        out.update({
            "risk_level": "high",
            "encoding_primary": "literal_keyword",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "strong",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本声称从未见过女性和黑人在一起，并说'中国人的审美很难认为黑人帅'。",
                    "核心攻击：否定黑人在中国审美标准下的吸引力。逻辑链条：我没见过→不存在→不帅。"
                ],
                "encoding_analysis": [
                    "直接攻击词汇(literal_keyword)：文本直接评论黑人群体的外貌吸引力（'中国人的审美很难认为黑人帅'），无编码包装。",
                    "当前标注的C4不适用。"
                ],
                "context_analysis": [
                    "知乎种族讨论下对黑人外貌的直接评价。不需要上下文。"
                ],
                "supporting_evidence": [
                    "1. '中国人的审美很难认为黑人帅'——直接对黑人群体进行外貌审美排除。",
                    "2. '压根没见到过'以个人经验否定跨种族关系的存在。",
                    "3. '咱也不瞎不傻'以'正常人都会这么认为'的姿态包装偏见。"
                ],
                "counter_evidence": [
                    "1. 文本表达的是个人审美观点，而非仇恨言论。",
                    "2. 审美差异是客观存在的社会现象讨论。"
                ],
                "final_rationale": "Risk: high。使用literal_keyword直接陈述对黑人外貌的负面审美判断，以个人经验为否定跨种族关系的论据，构成种族性排斥。"
            }
        })

    elif sid == "003549":
        # "有些穆斯林特恶心吃猪肉的，不爱带面纱的女人也滚......他们的三观出问题了吗？"
        out.update({
            "risk_level": "low",
            "encoding_primary": "E3_互动/热点触发",
            "encoding_secondary": [],
            "needs_context": True,
            "ambiguity": "medium",
            "evidence_strength": "weak",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本描述了某些极端穆斯林的价值观：不吃猪肉的人恶心、不带面纱的女人该滚。结尾问'他们的三观出问题了吗？'——质疑这种价值观。",
                    "结构不明确：可能是a)转述某极端穆斯林群体的观点+质疑，也可能是b)作者自己的观点（少数穆斯林恶心且不爱带面纱的女人该滚）。结尾问句倾向第一种解读。"
                ],
                "encoding_analysis": [
                    "热点触发(E3)：文本可能是对极端宗教观点的转述和批评，属于报道/分析型。",
                    "当前标注的D1反讽不适用——文本不是反讽，而是陈述+疑问。"
                ],
                "context_analysis": [
                    "话题标签lgbt_reporting与内容（伊斯兰教法）部分相关（面纱/LGBTQ可能交叉）。需要前文确认叙述者是转述还是表达自身观点。",
                    "结尾问句('他们的三观出问题了吗？')表明叙述者与描述的观点保持距离。"
                ],
                "supporting_evidence": [
                    "1. 结尾疑问句'他们的三观出问题了吗？'表达了对所述价值观的质疑。",
                    "2. 叙述口吻偏向分析/报道。"
                ],
                "counter_evidence": [
                    "1. 文本可能被解读为对穆斯林群体的直接攻击（'有些穆斯林特恶心'）。",
                    "2. 结尾问句可能是反讽式附和的修辞。",
                    "3. '不爱带面纱的女人也滚'如果是作者本人的话，则是直接的性别攻击。"
                ],
                "final_rationale": "Risk: low。文本可能是对极端观点的转述和质疑，但结构和指向不够清晰，存在被误解为直接攻击的风险。"
            }
        })

    elif sid == "003550":
        # "酒桌上谈这事儿，喝得下酒吗？"
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": True,
            "ambiguity": "high",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本说在酒桌上讨论'这事儿'（前文话题），是否还喝得下酒——表达了对某个话题的厌恶或不适。",
                    "'这事儿'完全依赖前文指代。语气可能是不赞成或调侃。"
                ],
                "encoding_analysis": [
                    "无编码机制。普通反问句。"
                ],
                "context_analysis": [
                    "话题标签race_discussion暗示'这事儿'指向种族话题。但文本本身无任何种族内容。"
                ],
                "supporting_evidence": [
                    "1. 无直接攻击性内容。"
                ],
                "counter_evidence": [
                    "1. 含义完全取决于未提供的上下文。",
                    "2. 如果'这事儿'涉及特定群体，反问句可能表达对该群体的贬低。"
                ],
                "final_rationale": "Risk: none (hard_negative)。文本过于简短歧义，但无直接攻击性内容。"
            }
        })

    elif sid == "003551":
        # "换个角度，如果从一开始就不结婚哪有这些破事儿..."
        out.update({
            "risk_level": "medium",
            "encoding_primary": "D1_反讽",
            "encoding_secondary": ["E1_平台黑话"],
            "needs_context": False,
            "ambiguity": "medium",
            "evidence_strength": "moderate",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本说如果不结婚就没有'这些破事儿'（婚姻的麻烦），该做的事一样做（暗示性行为），'那啥点的崽子落地直接走人'（孩子生了直接离开）。",
                    "'那啥点'（do that thing）是性行为的委婉语。'崽子'是带贬义的'孩子'称呼。整体主张弃养和逃避婚姻责任。"
                ],
                "encoding_analysis": [
                    "反讽(D1)：表面是'换个角度'的建议，实际是对婚姻制度和女性角色的贬低——男人可以享受性而不承担责任。",
                    "平台黑话(E1)：'那啥'是贴吧常见的性行为委婉表达（that thing）。'崽子'是贬义称呼。"
                ],
                "context_analysis": [
                    "在性别话题中，此文本倡导男性逃避婚姻和父亲责任，将女性工具化为性和生育对象。"
                ],
                "supporting_evidence": [
                    "1. '这些破事儿'贬低婚姻中的责任。",
                    "2. '那啥点'将性关系工具化。",
                    "3. '崽子落地直接走人'倡导弃养。"
                ],
                "counter_evidence": [
                    "1. 文本可被解读为对婚姻制度的批评而非攻击女性。",
                    "2. 语气调侃，攻击性强于吐槽但弱于仇恨言论。"
                ],
                "final_rationale": "Risk: medium。通过D1反讽和E1平台黑话倡导逃避婚姻责任，将女性工具化为性和生育对象，但攻击被包裹在'另类角度'的建议框架中。"
            }
        })

    elif sid == "003552":
        # "现在不是桑嗨仁歧视外地人的时候了🤣"
        out.update({
            "risk_level": "low",
            "encoding_primary": "E3_互动/热点触发",
            "encoding_secondary": ["A3_方言谐音"],
            "needs_context": True,
            "ambiguity": "low",
            "evidence_strength": "moderate",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本说'现在不是桑嗨仁歧视外地人的时候了🤣'——意思是现在已经不是上海人歧视外地人的时代了（语气可能为反讽或感慨）。",
                    "'桑嗨仁'是吴语/上海话的'上海人'发音（桑=上，嗨=海，仁=人），属方言谐音书写。"
                ],
                "encoding_analysis": [
                    "热点触发(E3)：文本是对歧视现象的评论/报道。",
                    "方言谐音(A3)：'桑嗨仁'是上海话'上海人'的方言发音谐音书写，增加了口语化和地方色彩。",
                    "当前标注的D1反讽可能适用但非主要编码。"
                ],
                "context_analysis": [
                    "在讨论地域歧视的动态变化中发表。需要前文了解讨论的具体语境——是感慨上海人不再歧视外地人，还是反讽上海人仍在歧视。"
                ],
                "supporting_evidence": [
                    "1. '桑嗨仁'是方言书写，非攻击性。",
                    "2. 文本是对歧视格局变化的社会观察。"
                ],
                "counter_evidence": [
                    "1. 🤣表情符号增添嘲讽色彩，可能表达反讽意味。",
                    "2. 如果为反讽，则可能在说上海人还在歧视外地人。"
                ],
                "final_rationale": "Risk: low。对地域歧视格局变化的评论观察，使用A3方言谐音('桑嗨仁')增加口语色彩，可能带有反讽但整体为报道型内容。"
            }
        })

    elif sid == "003553":
        # "我同学，生在安徽长在新疆"
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本简单陈述：我同学出生在安徽，在新疆长大。",
                    "纯粹的客观事实陈述。"
                ],
                "encoding_analysis": [
                    "无编码机制。简单陈述。"
                ],
                "context_analysis": [
                    "区域话题讨论中提供的个人信息。"
                ],
                "supporting_evidence": [
                    "1. 被ToxiCN标注为非有毒(toxic=0)。",
                    "2. 纯事实陈述无表达成分。"
                ],
                "counter_evidence": [
                    "1. 无风险证据。"
                ],
                "final_rationale": "Risk: none (hard_negative)。纯事实陈述，无任何风险。"
            }
        })

    elif sid == "003554":
        # Long essay about masculinity, 娘化, females 倒贴外男
        out.update({
            "risk_level": "medium",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "moderate",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "长篇论述'雄性意识'(masculinity)对民族存亡的重要性，批评东亚国家'雄性意识弱化、娘化明显'，认为这是'审美安全隐患'，甚至'高于意识形态战线溃败'。",
                    "批评部分女性'无原则地倒贴外男'（崇拜外国男性）。提出恢复'春秋阳刚精神''秦汉尚武霸气'作为解决方案。",
                    "核心问题词：'娘化'（feminization，贬义）形容东亚男性；'倒贴外男'（foreign-men chasing，贬义）形容女性。"
                ],
                "encoding_analysis": [
                    "无特殊编码机制。文本是直白的长篇个人观点论述，使用日常词汇而非特殊编码。",
                    "当前标注的D2隐喻和D1反讽不适用——文本是直接表达观点，没有使用比喻或反讽修辞（'雄性意识'虽可视为概念隐喻但不属于编码范畴）。"
                ],
                "context_analysis": [
                    "话题标签为race_discussion但文本主要讨论性别和民族议题。'倒贴外男'涉及种族间关系。",
                    "整体是民族主义+传统性别观的混合论述，主张强化男性气质、批评女性和外族男性的结合。"
                ],
                "supporting_evidence": [
                    "1. '娘化明显'是贬低男性女性化特征的表达。",
                    "2. '无原则地倒贴外男'批评女性的跨种族婚恋选择。",
                    "3. '沦为奴隶之族'以民族存亡危机感包装观点。"
                ],
                "counter_evidence": [
                    "1. 文本是一篇系统的个人观点论述，非攻击性发泄。",
                    "2. 主要主张是民族复兴，非煽动对特定群体的仇恨。"
                ],
                "final_rationale": "Risk: medium。文本系统论述了民族主义的性别观，包含'娘化''倒贴外男'等贬低性判断，但整体为观点论述而非直接仇恨攻击。"
            }
        })

    elif sid == "003555":
        # "目前关于lgbt的一切问题都还处于纸上谈兵阶段..."
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本讨论LGBTQ议题的现状：还处于纸上谈兵阶段，反同的声音也是为LGBTQ发声的一部分，解决方案需要由上层基于社会情况决定。",
                    "这是一个政治/社会讨论，主张更全面地看待LGBTQ议题。语气理性，无攻击性。"
                ],
                "encoding_analysis": [
                    "无编码机制。理性讨论型表达。",
                    "当前标注的D1反讽和D4双关不适用。"
                ],
                "context_analysis": [
                    "贴吧LGBTQ话题下的社会讨论。文本持相对中立的态度。"
                ],
                "supporting_evidence": [
                    "1. 文本为分析讨论型，不攻击任何群体。",
                    "2. 语调理性，承认问题的复杂性。"
                ],
                "counter_evidence": [
                    "1. '反同也是为lgbt发声的'这一论断有争议性，可能被解读为为恐同辩护。"
                ],
                "final_rationale": "Risk: none (hard_negative)。理性社会讨论，无攻击性内容。"
            }
        })

    elif sid == "003556":
        # "习惯就好了，想想人家河南人，那么多年都过来了……"
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": True,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本说'习惯就好了，想想人家河南人，那么多年都过来了'——以河南人长期承受地域歧视的案例来安慰某人接受现状。",
                    "语气是劝慰性的，但也可能被解读为'歧视是正常的'。"
                ],
                "encoding_analysis": [
                    "无编码机制。日常劝慰表达。"
                ],
                "context_analysis": [
                    "在区域话题讨论中用来安慰某人。引用河南人的经历作为参考。"
                ],
                "supporting_evidence": [
                    "1. 被ToxiCN标注为非有毒(toxic=0)。",
                    "2. 语气为劝慰。"
                ],
                "counter_evidence": [
                    "1. '习惯就好了'可被解读为对歧视的消极接受。",
                    "2. 使用河南人作为'习惯被黑'的例子可能强化刻板印象。"
                ],
                "final_rationale": "Risk: none (hard_negative)。劝慰性日常表达，虽引用河南人作为参考但无攻击意图。"
            }
        })

    elif sid == "003557":
        # Long essay by Henanese woman defending Henan
        out.update({
            "risk_level": "low",
            "encoding_primary": "E3_互动/热点触发",
            "encoding_secondary": [],
            "needs_context": True,
            "ambiguity": "low",
            "evidence_strength": "moderate",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "一位河南女性发表长篇自我陈述，从多角度反驳地域歧视：教育水平（河南分数线高、考生竞争激烈）、人口比例（人口多所以不好的人绝对数量多）、政策不公（少数民族优惠政策、河南被忽视）。",
                    "核心立场是反地域偏见同时表达对国家政策的不满。关键词：'河南学子的成绩基本都是数一数二'、'我并不觉得受过高等教育的河南人素质低'、'国家说：你们河南穷虽穷，又饿不死，不会反的，于是乎中原振兴提了n年'。"
                ],
                "encoding_analysis": [
                    "热点触发(E3)：文本是对地域歧视的直接反驳和自我辩护，属于报道/反偏见型。",
                    "当前标注的D1反讽不适用——文本情绪真挚不属反讽。"
                ],
                "context_analysis": [
                    "在知乎区域话题讨论中，河南人自身站出来反驳地域歧视。书写者明确表态：'我依然可以骄傲的说我是河南人'。"
                ],
                "supporting_evidence": [
                    "1. '作为河南的一个女孩子，尽管大家黑河南，我依然可以骄傲的说我是河南人'——明确反歧视立场。",
                    "2. 从教育、政策、人口统计等多角度反驳歧视逻辑。",
                    "3. '我不曾像别人黑的那样偷摸拐骗'——正面表态。"
                ],
                "counter_evidence": [
                    "1. 文本包含对政策的不满批评（如'国家只在口头上支持'），但属于正常政策讨论。"
                ],
                "final_rationale": "Risk: low。河南女性的反地域歧视自我辩护，立场明确反偏见，属报道/反偏见型内容。"
            }
        })

    elif sid == "003558":
        # "就是吃Human blood steamed bread"
        out.update({
            "risk_level": "low",
            "encoding_primary": "A4_外语谐音",
            "encoding_secondary": ["D2_隐喻"],
            "needs_context": True,
            "ambiguity": "high",
            "evidence_strength": "weak",
            "hard_negative": False,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本说'就是吃Human blood steamed bread'——中英混合表达，字面意思为'就是吃人血馒头'。",
                    "'人血馒头'是中文成语，原指蘸人血治痨病的馒头（鲁迅作品描写），现代用法指利用他人苦难牟利。此处混合了英文'Human blood'。"
                ],
                "encoding_analysis": [
                    "外语编码(A4)：将成语中的'人血'替换为英文'Human blood'，可能是为了强调、增加冲击力或规避中文关键词过滤。",
                    "隐喻(D2)：'吃人血馒头'本身是一个社会隐喻，指利用他人苦难获利。",
                    "当前标注为'none'——忽略了中英混用的编码特征。"
                ],
                "context_analysis": [
                    "话题标签为race_discussion暗示'人血馒头'在此处可能指代某个种族群体在苦难中被利用。但文本极短且高度歧义。",
                    "需要前文确认'人血馒头'在此处具体指向哪种社会现象。"
                ],
                "supporting_evidence": [
                    "1. 中英混合可能是刻意编码。",
                    "2. '人血馒头'是对利用他人苦难牟利行为的负面批评。"
                ],
                "counter_evidence": [
                    "1. 文本是成语的日常使用，未必针对种族群体。",
                    "2. 极短且歧义高。"
                ],
                "final_rationale": "Risk: low。通过A4外语编码和D2隐喻使用'人血馒头'成语批评社会现象，但目标不明确且证据薄弱，风险较低。"
            }
        })

    elif sid == "003559":
        # "所以你一直看一个中年啤酒肚人字拖大叔和肥胖宽腰垂胸大妈天天搂搂抱抱亲亲的同样恶心吧。所以是个人形象的问题而不是同性的问题啊。"
        out.update({
            "risk_level": "none",
            "encoding_primary": "none",
            "encoding_secondary": [],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本使用类比论证：你看到不好看的异性恋情侣亲密也会觉得恶心，所以问题在于个人形象而非性取向。论证核心是反对同性恋歧视。",
                    "关键词：'个人形象的问题而不是同性的问题'——明确表达反歧视立场。"
                ],
                "encoding_analysis": [
                    "无编码机制。类比论证是正常修辞，非编码。"
                ],
                "context_analysis": [
                    "在LGBTQ话题讨论中使用'让你也感觉恶心'的类比来反驳反同立场。"
                ],
                "supporting_evidence": [
                    "1. '是个人形象的问题而不是同性的问题'明确反歧视。",
                    "2. 整体论证结构为反恐同立场。"
                ],
                "counter_evidence": [
                    "1. '恶心'一词带有负面情感，类比可能不太恰当。"
                ],
                "final_rationale": "Risk: none (hard_negative)。反同性恋歧视的论证，无攻击性。"
            }
        })

    elif sid == "003560":
        # "这是打算开始通过歧视光棍来试图提高结婚率了？"
        out.update({
            "risk_level": "low",
            "encoding_primary": "D1_反讽",
            "encoding_secondary": [],
            "needs_context": True,
            "ambiguity": "low",
            "evidence_strength": "weak",
            "hard_negative": True,
            "target_known": False,
            "reasoning": {
                "literal_analysis": [
                    "文本反讽地说：这是不是打算通过歧视'光棍'（单身男性）来提高结婚率？",
                    "内容是对某种政策提案的讽刺性评论。'光棍'指单身大龄男性。"
                ],
                "encoding_analysis": [
                    "反讽(D1)：以夸张的反问讽刺某个政策逻辑的荒谬性。",
                    "当前标注的D4双关不适用——无反讽的双关含义。"
                ],
                "context_analysis": [
                    "在性别话题讨论中讽刺某个针对'光棍'的政策或建议。需要前文确认具体讽刺对象。"
                ],
                "supporting_evidence": [
                    "1. 反问句式表明讽刺/不赞同立场。",
                    "2. '歧视光棍'是对政策批评的关键词。"
                ],
                "counter_evidence": [
                    "1. 文本对政策而非对群体进行攻击。",
                    "2. '光棍'虽含轻微贬义但属社会常用词。"
                ],
                "final_rationale": "Risk: low。使用D1反讽对政策进行讽刺性评论，非攻击群体。"
            }
        })

    elif sid == "003561":
        # Yang Li reference - "因为杨笠说男人是垃圾..."
        out.update({
            "risk_level": "low",
            "encoding_primary": "E3_互动/热点触发",
            "encoding_secondary": ["D1_反讽"],
            "needs_context": True,
            "ambiguity": "low",
            "evidence_strength": "moderate",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "文本引用杨笠（脱口秀演员）'说男人是垃圾'并'教育男性不要对号入座'的事件，然后反讽地建议女性也'不要对号入座'——如果你觉得骂的不是你就不在骂你。",
                    "核心逻辑：男性可以不对号入座，那女性也应该同理。最后'我们就欣然接受吧'是反讽式的妥协。",
                    "杨笠事件是2020-2021年性别争论的热点话题。"
                ],
                "encoding_analysis": [
                    "热点触发(E3)：引用杨笠事件这一众所周知的性别争论热点构建论点。",
                    "反讽(D1)：'我们就欣然接受吧'表面是接受，实际是对双重标准的不满。"
                ],
                "context_analysis": [
                    "文本是对杨笠事件的回应和性别双重标准的批评。需要了解杨笠'男人是垃圾'事件才能完全理解。"
                ],
                "supporting_evidence": [
                    "1. '杨笠说男人是垃圾'引用争议事件。",
                    "2. '如果你觉得骂的不是你，就不是在骂你'引用杨笠团队的回应逻辑。",
                    "3. '那么我们也希望你们女性不要对号入座'以牙还牙的框架。"
                ],
                "counter_evidence": [
                    "1. 文本是对双重标准的批评而非攻击女性群体。",
                    "2. 使用了杨笠本人的逻辑来反驳。"
                ],
                "final_rationale": "Risk: low。引用杨笠事件(E3)讨论性别双重标准，使用D1反讽表达不满，但为论辩性内容而非直接攻击。"
            }
        })

    elif sid == "003562":
        # Long rant about women: "她们努力追求高品质的生活代价就是牺牲他人成全自己..."
        out.update({
            "risk_level": "high",
            "encoding_primary": "literal_keyword",
            "encoding_secondary": ["D1_反讽"],
            "needs_context": False,
            "ambiguity": "low",
            "evidence_strength": "strong",
            "hard_negative": False,
            "target_known": True,
            "reasoning": {
                "literal_analysis": [
                    "长篇对女性的攻击性描述：牺牲他人成全自己、欺软怕硬、对有钱公子委曲求全、对正常男人嚣张算计虚伪。关键攻击词：'哄抬逼价'（哄抬女性身价的粗俗表达）、'欺软怕硬'、'嚣张算计虚伪样'、'坚韧不拔的奋斗精神啊我都快感动哭了'（反讽）。"
                ],
                "encoding_analysis": [
                    "直接攻击词汇(literal_keyword)：'哄抬逼价'（抬升阴道价格）是极其粗俗的物化女性表达。'欺软怕硬''嚣张算计虚伪样'是直接人格攻击。",
                    "反讽(D1)：'多么坚韧不拔的奋斗精神啊我都快感动哭了'以高度反讽的口吻总结，增强了攻击性。",
                    "当前标注的D1/D4不完全——主要编码应为literal_keyword。"
                ],
                "context_analysis": [
                    "贴吧性别讨论中的长篇misogyny式攻击。文本自身提供了完整的攻击内容，不需要额外上下文。"
                ],
                "supporting_evidence": [
                    "1. '哄抬逼价'——极端粗俗的女性物化表达。",
                    "2. '欺软怕硬'——整体人格否定。",
                    "3. '对有钱公子委曲求全'/'对正常男人嚣张算计'——构建女性双重标准负面形象。",
                    "4. '坚韧不拔的奋斗精神啊我都快感动哭了'——反讽加强攻击。",
                    "5. '被几个女人骗过没骗到我'——自称亲历者增加话语权威性。"
                ],
                "counter_evidence": [
                    "1. 文本以个人经历叙事为基础，可辩解为情绪宣泄。",
                    "2. 部分内容针对具体行为而非全体女性。"
                ],
                "final_rationale": "Risk: high。使用literal_keyword('哄抬逼价'等)和D1反讽对女性群体进行极端misogyny式攻击，包含粗俗物化表达和人格全称否定。"
            }
        })

    else:
        raise ValueError(f"Unknown sample id: {sid}")

    return out


# Main
samples = []
with open(INPUT, 'r') as f:
    for line in f:
        s = line.strip()
        if s:
            samples.append(json.loads(s))

reviewed = [review_sample(s) for s in samples]

with open(OUTPUT, 'w', encoding='utf-8') as f:
    for s in reviewed:
        f.write(json.dumps(s, ensure_ascii=False) + '\n')

print(f"chunk_018: wrote {len(reviewed)} samples")
