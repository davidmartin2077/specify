#!/usr/bin/env python3
"""Review and correct all 50 samples in chunk_019.jsonl"""
import json

samples = []
with open('/Users/davidchankong/Documents/审查微调/data/raw/batch23_chunks/chunk_019.jsonl', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            samples.append(json.loads(line))

print(f"Loaded {len(samples)} samples")

# Define corrections per sample by id
corrections = {
    # 003563: Discussing regional discrimination dynamics, accusatory but analytical
    "003563": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本讨论地域歧视现象，指出某地区在'被地域黑'方面远比东北轻，批评该地区'掌握话语权把自己粉饰成受害者'。后半句提问'全国一二线城市中你最不喜欢哪个城市'延续了地域话题。",
                "关键词'地域黑'、'拍马都追不上'、'掌握话语权'、'粉饰成受害者'表明叙述者在分析地域歧视叙事格局而非直接攻击任一地域。"
            ],
            "encoding_analysis": [
                "无编码机制。文本使用直白的日常语言讨论地域歧视现象，没有采用谐音、隐喻、反讽等包装。'拍马都追不上'是普通夸张修辞，非编码。"
            ],
            "context_analysis": [
                "文本来自知乎关于'全国一二线城市你最不喜欢哪个'话题的讨论，需要对前文才能确定叙述者具体指向哪一地区。",
                "文本本身是对地域歧视话语权力的分析性评论，但缺少前文无法确定其批评的具体目标城市。"
            ],
            "supporting_evidence": [
                "文本的核心论述结构是分析性的：指出某地区比东北更少遭受地域黑但更擅长塑造受害者叙事。",
                "没有直接使用任何地域性侮辱词汇如'小偷'、'骗子'等针对特定群体。",
                "'粉饰成受害者'虽有贬义但指向的是话语策略而非地域群体本质。"
            ],
            "counter_evidence": [
                "文本确实包含对一个未指名地区的负面评价（指责其'粉饰成受害者'），在特定对话链中可能构成地域攻击。",
                "缺少前文对话导致无法判断叙述者的整体立场是批评地域黑还是参与地域黑。"
            ],
            "final_rationale": "Risk: low。文本是对地域歧视话语的评论性分析，没有直接使用攻击性词汇，主要风险来自话题敏感性而非文本本身的攻击性。"
        }
    },
    # 003564: "怕不是不知道广州一堆汉族小黑人吧🤣" - DIRECT racial mockery
    "003564": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "叙述者声称广州有大量'汉族小黑人'，暗示部分广东本地人肤色较深。'小黑人'是贬低性称呼，末尾🤣表情明确表示嘲笑态度。",
                "'怕不是不知道'这个句式是常见的讽刺性反问，增强了对被描述群体的贬低效果。"
            ],
            "encoding_analysis": [
                "直接使用了攻击性关键词'小黑人'作为对汉族群体的贬义称呼，没有经过任何编码包装。'小黑人'本身即是种族肤色相关的侮辱性词汇（literal_keyword）。",
                "末尾🤣表情进一步确认了文本的嘲笑意图而非事实陈述。"
            ],
            "context_analysis": [
                "文本来自知乎平台种族话题讨论。裸文本即可判断其攻击性，不需要额外上下文。"
            ],
            "supporting_evidence": [
                "'小黑人'明确使用了'黑'这一肤色特征来贬低汉族人群，将肤色深浅作为嘲笑对象。",
                "'怕不是不知道'句式带有明显的高姿态和讽刺意味。",
                "🤣表情直接表达了嘲笑态度，不是中性或客观陈述。",
                "攻击对象明确——广州的汉族人（'汉族小黑人'）。"
            ],
            "counter_evidence": [
                "'小黑人'在某些语境下可能是自嘲或内部戏称，但从叙述者语气和🤣表情看，不属于友好内部调侃。"
            ],
            "final_rationale": "Risk: high。直接使用种族侮辱性词汇'小黑人'并附加嘲笑表情，对特定群体进行肤色贬低。"
        }
    },
    # 003565: Tieba platform comment, nothing to do with gender
    "003565": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本讨论百度贴吧的管理功能变化：空降吧主、改贴吧目录、改吧名。'度娘'是百度网络昵称。全文为对平台功能迭代的评论。",
                "没有任何涉及性别攻击、地域攻击或其他敏感内容的关键词。"
            ],
            "encoding_analysis": [
                "无编码机制。文本是日常网络讨论，使用普通网络用语如'空降吧主'、'度娘'等贴吧常见词汇，无任何编码包装。"
            ],
            "context_analysis": [
                "尽管样本话题标签为gender_discussion，但文本内容完全不涉及性别议题。可能ToxiCN标签有误或原始对话上下文涉及性别。"
            ],
            "supporting_evidence": [
                "文本全部内容围绕贴吧的产品功能展开，未涉及任何人或群体的攻击。",
                "ToxiCN标记toxic=0，与文本实际内容一致。"
            ],
            "counter_evidence": [
                "文末'越来越会玩了'有轻微讽刺语气，但指向的是平台运营方（百度），不构成对任何人群的攻击。"
            ],
            "final_rationale": "Risk: none。文本为贴吧产品功能讨论，内容完全不含攻击性。hard_negative样本。"
        }
    },
    # 003566: "防治中国被黑化" = anti-black rhetoric
    "003566": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": ["D4_双关"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "叙述者提出宣传策略：用'防治中国被黑化'比'黑人被歧视'效果更好。'黑化'一词使用了双关——既指'被黑色人种影响'又指'被玷污/恶化'。",
                "'黑人被歧视，生的孩子一辈子也会被歧视'暗示反对黑人/中国结合，将歧视后果作为说服手段。"
            ],
            "encoding_analysis": [
                "主要使用literal_keyword——虽然'黑化'有双关意味，但其核心歧视意图明确：将黑人人口增长等同于中国的'恶化'。",
                "'黑化'的D4双关编码：表面指darkening/blackening，深层暗指被黑人'侵蚀'的负面变化。但这种编码非常浅，基本等于直白表达。"
            ],
            "context_analysis": [
                "文本来自贴吧种族话题讨论。裸文本即可判断其反黑立场，无需额外上下文。"
            ],
            "supporting_evidence": [
                "'防治中国被黑化'将黑人（'黑'）与负面变化（'化'）直接关联，是经典的种族排斥论述。",
                "文本区分了'中国'（我们）和'黑人'（他们），并主张用'保护中国'的框架替代'保护黑人'的框架。",
                "提及'生的孩子一辈子也会被歧视'暗示反对跨种族婚姻和生育。"
            ],
            "counter_evidence": [
                "叙述者声称此策略'宣传效果更好'，可能是在讨论传播策略而非表达个人种族观点。但文中的'防治'和'被黑化'措辞已经包含了明确的种族立场。"
            ],
            "final_rationale": "Risk: high。文本主张以'防治黑化'替代'反歧视'叙事，将黑人等同于对中国的威胁，是明确的种族排斥言论。"
        }
    },
    # 003567: "我同意你 不认同就是歧视同性恋我真的吐了 这道德绑架绑的"
    "003567": {
        "risk_level": "medium",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "medium",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "叙述者表达厌烦情绪：'不认同就是歧视同性恋我真的吐了'是对某种观点的串述并表达恶心。'道德绑架'指控对方通过道德压力迫使认同。",
                "'吐了吐了'重复表达强烈反感。叙述者反对的是'不认同=歧视'这一等式，而非LGBT群体本身。"
            ],
            "encoding_analysis": [
                "无编码机制。文本直接表达了对'道德绑架'式言论的不耐烦，情绪词汇'吐了'是直白的厌恶表达，没有使用隐喻、反讽等编码手段。"
            ],
            "context_analysis": [
                "文本来自知乎，是对他人言论的回应。需要看到前文才能确认叙述者反对的具体内容。",
                "叙述者可能持有反LGBT立场（将LGBT权益主张视为道德绑架），也可能只是反对'不认同即歧视'的二元逻辑。"
            ],
            "supporting_evidence": [
                "'我同意你'表明叙述者在附和他人的观点，后续是对某类道德立场的不满。",
                "'道德绑架'是中文网络常见术语，用来批评将道德立场作为强制要求的做法。",
                "文本表达了强烈的厌恶情绪（多次'吐了'）。"
            ],
            "counter_evidence": [
                "叙述者反对的是'不认同就是歧视'这个具体论断，而非针对LGBT群体本身。没有使用直接的LGBT侮辱词汇。",
                "缺乏前文导致无法判断叙述者是否认同LGBT权利——可能只是批评论证方式而非群体。"
            ],
            "final_rationale": "Risk: medium。文本对LGBT话题表达了强烈反感情绪，但攻击对象是'道德绑架'式的论证方式而非LGBT群体本身，目标不够明确。"
        }
    },
    # 003568: Neutral factual report about Netherlands/gay rights -- CORRECT as none
    "003568": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本提供关于荷兰阿姆斯特丹同性恋游行接受度的调查数据，以及荷兰法律（同性婚姻、吸毒、安乐死等）和社会态度（城乡差异、天主教影响）。",
                "'泡唱'、'麻阴'可能是输入错误（应为'泡娼'、'麻药'？）但不影响整体文义。文本呈现信息性、报道性。"
            ],
            "encoding_analysis": [
                "无编码机制。文本为转述/新闻报道式的信息汇编，没有使用任何编码或修辞攻击手段。"
            ],
            "context_analysis": [
                "文本来自贴吧LGBT话题讨论。虽然话题敏感，但文本本身是客观报道，不包含对LGBT群体的攻击。"
            ],
            "supporting_evidence": [
                "文本引用调查数据和时间、法律等具体信息，呈现知识分享态。",
                "结尾'极其排斥同性恋的'是指荷兰农村地区的天主教势力，是客观描述而非个人立场。"
            ],
            "counter_evidence": [
                "'真是太开放太前卫了'略带讽刺语气，但对象是荷兰整体社会而非LGBT群体。"
            ],
            "final_rationale": "Risk: none。文本为关于荷兰社会的数据报道，无攻击性。hard_negative样本。"
        }
    },
    # 003569: "内部有敌人，刚好最近在肃清" - generic political talk
    "003569": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "medium",
        "evidence_strength": "weak",
        "needs_context": True,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本说'内部有敌人，刚好最近在肃清，抓紧把这人肃清一下'。'敌人'、'肃清'是政治/军事术语，在日常生活也有比喻用法。",
                "文本未指定任何具体群体或个体，'内部'的范围完全取决于上下文。"
            ],
            "encoding_analysis": [
                "无编码机制。'肃清'虽然带有强烈意识形态色彩，但这是普通词汇，不是对特定群体的隐晦攻击编码。"
            ],
            "context_analysis": [
                "文本被标记为race_discussion但内容完全不涉及种族。可能的原对话讨论涉及种族话题但此条评论本身未提及。",
                "高度依赖前文才能知道'内部'和'敌人'指什么。裸文本无法判断攻击目标。"
            ],
            "supporting_evidence": [
                "文本中没有出现任何种族、地域、性别相关的关键词或指向。",
                "'肃清'一词虽有强烈语气，但在网络讨论中常用于调侃或夸张表达。"
            ],
            "counter_evidence": [
                "'敌人'、'肃清'词汇本身具有攻击性和排他性，在特定语境下可能指向特定人群。但文本本身未指明目标。"
            ],
            "final_rationale": "Risk: none。文本使用'敌人'、'肃清'等强词但未指明目标群体，裸文本无明确攻击对象。hard_negative样本。"
        }
    },
    # 003570: "为什么要纠正她们？你们希望她们过一个幸福的生活吗？" - sarcastic about correcting women
    "003570": {
        "risk_level": "medium",
        "encoding_primary": "D1_反讽",
        "encoding_secondary": [],
        "ambiguity": "high",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本提出反问：'为什么要纠正她们？你们希望她们过一个幸福的生活吗？'。'纠正她们'暗示被讨论对象（女性）需要被'矫正'，这是性别偏见的前提假设。",
                "叙句形式是反讽：表面疑问'为什么要纠正'和'希望她们幸福'，但实际态度可能是两种——要么反对纠正（认为女性不需要被'修正'），要么讽刺（认为纠正本身就是为她们好）。"
            ],
            "encoding_analysis": [
                "D1反讽编码：疑问句式表面中立但实际传递了强烈态度。'你们希望她们过一个幸福的生活吗？'这个反问，如果前文在讨论如何'纠正'女性，则这句话是在用'为你好'逻辑讽刺纠正行为本身。"
            ],
            "context_analysis": [
                "高度依赖前文。不知道前文讨论了什么'纠正'，就无法判断叙述者是对纠正行为持批评态度，还是在讽刺支持纠正的人。",
                "不同平台（贴吧男权/女权社区）对此句的解读可能完全相反。"
            ],
            "supporting_evidence": [
                "'她们'指代特定群体（女性），表明这是一个性别议题的讨论。",
                "'纠正'一词本身就暗示了说话者或其所引用观点认为女性存在需要被修正的'错误'。",
                "反问句式创造了两可的解读空间，符合反讽的基本特征。"
            ],
            "counter_evidence": [
                "没有足够上下文确认'纠正她们'的具体含义——是指对女性的传统规训还是现代xx教育。",
                "叙述者可能是在为女性辩护（'为什么要被纠正？她们有自己的幸福定义'），而非表达性别偏见。"
            ],
            "final_rationale": "Risk: medium。文本使用反讽编码讨论对女性的'纠正'，攻击方向取决于对话链——可能是反性别偏见的辩护也可能是性别偏见的复读。高度歧义。"
        }
    },
    # 003571: "黑子们四五月份骂上海..." - reporting on pattern
    "003571": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "叙述者列举'黑子们'（网络喷子/地域攻击者）在不同月份攻击不同城市的模式：四五月份骂上海、六月份骂唐山、七月份骂南京、八月份喷海南。",
                "文本是对网络地域攻击现象的观察和总结，叙述者立场是揭露这一行为模式。"
            ],
            "encoding_analysis": [
                "无编码机制。'黑子'是网络通用词，指恶意评论者。文本是直白的现象描述，没有使用任何编码手段。"
            ],
            "context_analysis": [
                "文本来自知乎，是对2022年网络舆论现象的总结。裸文本即可理解其报道性质。"
            ],
            "supporting_evidence": [
                "文本的核心内容是按时间顺序列举网络攻击目标城市，是报道性质而非参与攻击。",
                "使用'黑子们'作为主语，明确将攻击行为归因于一群特定类型的人（网络喷子），而非城市本身的属性。"
            ],
            "counter_evidence": [
                "列举攻击目标城市时提到了具体地名，可能被误读为继续传播地域攻击。但全文叙事框架是揭露而非参与。"
            ],
            "final_rationale": "Risk: low。文本是报道揭露网络地域攻击现象，叙述者立场是观察而非参与。"
        }
    },
    # 003572: "其实韩国人。。。娘炮。。。😄😄😄" - DIRECT national insult
    "003572": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本将韩国人直接称为'娘炮'并用😄😄😄表情强化嘲笑。'娘炮'（sissy/effeminate）是贬低男性气质的中文侮辱词汇。",
                "省略号'。。。''和表情增强了轻蔑和戏谑的语气。"
            ],
            "encoding_analysis": [
                "literal_keyword——直接使用侮辱性称呼'娘炮'攻击整个韩国民族。没有经过任何编码包装，属于赤裸裸的群体攻击。"
            ],
            "context_analysis": [
                "文本来自知乎种族话题讨论。裸文本即可判断其攻击性。"
            ],
            "supporting_evidence": [
                "'娘炮'是对男性人群的攻击性贬低词汇，此处用于整个韩国民族。",
                "😄😄😄表情明确表示叙述者觉得这样描述很好笑，非中性表达。",
                "攻击对象明确（韩国人作为一个整体），无任何限定条件。"
            ],
            "counter_evidence": [
                "无有效的反方证据。文本是直接的国家/民族侮辱。"
            ],
            "final_rationale": "Risk: high。直接使用侮辱词汇'娘炮'攻击韩国人群并附加嘲笑表情，是明确的群体仇恨言论。"
        }
    },
    # 003573: "黑人想尽一切办法来中国蹭我们的福利，赖着不走" - DIRECT anti-black
    "003573": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "'我没这么认为'回应他人观点后，叙述者陈述自己的立场：'黑人想尽一切办法来中国蹭我们的福利，赖着不走倒是真的'。",
                "使用'蹭福利'（scam benefits）、'赖着不走'（refuse to leave）等负面定性，将黑人描述为机会主义的寄生者。"
            ],
            "encoding_analysis": [
                "literal_keyword——'黑人'作为明确攻击目标，'蹭福利'、'赖着不走'是直白的负面定性，没有经过编码包装。"
                "'倒是真的'强化了这种负面叙述的确定性语气。"
            ],
            "context_analysis": [
                "文本来自知乎种族讨论。裸文本即可判断其反黑人立场。",
                "前文'我没这么认为'提示这是对某种更正面看待黑人的观点的反驳。"
            ],
            "supporting_evidence": [
                "'想尽一切办法'将黑人描述为主动、有意图地获取不当利益。",
                "'蹭我们的福利'（我们的）建立'我们中国人vs他们黑人'的对立框架。",
                "'赖着不走'暗示黑人非法或不当地滞留。",
                "整句话将黑人等同于福利负担，是经典的种族排斥论述。"
            ],
            "counter_evidence": [
                "没有有效的反方证据。文本是直接的反黑人种族言论。"
            ],
            "final_rationale": "Risk: high。直接陈述反黑人的种族排斥观点，将黑人描述为福利剥削者和非法滞留者，目标明确。"
        }
    },
    # 003574: "黑人本来犯罪率就较高" - DIRECT racial stereotype
    "003574": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本陈述：'黑人本来犯罪率就较高'。'本来'一词暗示犯罪率高是黑人群体的固有/天生属性，而非社会结构性因素导致。",
                "这是一种将犯罪率与种族本质直接关联的种族主义论述。"
            ],
            "encoding_analysis": [
                "literal_keyword——直接陈述种族偏见，没有使用任何编码包装。"
            ],
            "context_analysis": [
                "文本来自贴吧种族话题讨论。裸文本即可判断其种族偏见性质。",
                "在讨论框架中，这句话通常用来论证对黑人的警惕或排斥是合理的。"
            ],
            "supporting_evidence": [
                "'本来'暗示攻击性是黑人的先天特征，排除了社会经济因素的解释空间。",
                "将犯罪率归因于种族而非结构性因素（贫困、教育资源不平等、歧视性执法等）是种族主义的典型逻辑。",
                "尽管表面上是'事实陈述'语气，但'本来'一词暴露了本质化偏见。"
            ],
            "counter_evidence": [
                "从纯统计角度看，某些地区黑人犯罪率确实高于其他群体。但'本来'一词暗示这是种族本质而非社会结构性因素，改变了语气的性质。"
            ],
            "final_rationale": "Risk: high。以'本来'将犯罪率本质化为黑人种族属性，是直接种族偏见论述。"
        }
    },
    # 003575: "看不惯，干不掉，心里不爽，只能使劲黑" - analysis of regional attitudes
    "003575": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": True,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "前半句'看不惯，干不掉，心里不爽，只能使劲黑'描述了一种心理状态（看不惯某人但无法影响对方，只能靠'黑'发泄）。",
                "后半句引用姨妈在北京的生活经验，说北京人对上海人有'复杂情绪'，这种情绪反映在春晚、电视剧等文艺作品中。",
                "全文是对地域间竞争心理的分析性评论。"
            ],
            "encoding_analysis": [
                "无编码机制。文本使用日常口语，以个人经历（姨妈在北京）为论据，分析北京对上海的地域情绪。没有编码包装。"
            ],
            "context_analysis": [
                "文本来自知乎地域话题讨论。可能是对某个关于北京/上海对比问题的回答。",
                "需要前文才能确定叙述者分析的是针对哪些具体的地域黑现象。"
            ],
            "supporting_evidence": [
                "文本提供分析框架（复杂情绪、文艺作品反映）和具体论据（姨妈的经验），呈现出理性讨论而非情绪攻击。",
                "没有使用针对北京或上海人群的侮辱性词汇。"
            ],
            "counter_evidence": [
                "虽然整体是分析框架，但'看不惯'、'干不掉'、'心里不爽'等措辞本身就包含了对北京人群的地域刻板印象。",
                "这种分析本身可能强化了地域对立的叙事。"
            ],
            "final_rationale": "Risk: low。文本是分析北京与上海之间地域情绪的个人评论，虽有刻板印象元素但整体为分析性立场。"
        }
    },
    # 003576: ANTI-地域黑 stance
    "003576": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "叙述者明确反对地域歧视：'地域黑真的够了，都是中国人有什么好黑的？'然后列举常见的地域刻板印象（新疆人是小偷、河南人是骗子等），批评以偏概全和'可怕的'偏见。",
                "结尾表明立场：'我只知道，都是中国人，都值得尊重'。",
                "全文的核心论点是地域黑的危害和荒谬，是反歧视文本。"
            ],
            "encoding_analysis": [
                "无编码机制。文本直接表达了对地域歧视的批评，使用了列举和反驳的论证结构。列举的地域刻板印象是转述而非认可。"
            ],
            "context_analysis": [
                "来自知乎，回应一条提到'河南籍新疆人'的评论。文本末尾说明触发点。"
            ],
            "supporting_evidence": [
                "'地域黑真的够了'直接表达了对地域歧视的厌烦和反对。",
                "'以偏概全这种真是太可怕了'明确批评刻板印象的危害。",
                "'都值得尊重'表达积极的反歧视立场。",
                "列举刻板印象后都以'以偏概全'进行否定。"
            ],
            "counter_evidence": [
                "列举常见地域刻板印象时（新疆人是小偷、河南人是骗子等），即使作为反面例证，也可能被截取后脱离上下文传播。"
            ],
            "final_rationale": "Risk: low。文本明确反对地域歧视，立场为反偏见。列举刻板印象是为了批评而非传播。"
        }
    },
    # 003577: Pro-tolerance statement
    "003577": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": True,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "叙述者赞同某种观点：'说的太对了'。核心信息是'不管是支持还是不支持，理解或者不理解，都不能成为高人一等的借口'。",
                "这是倡导尊重多元观点的包容立场。"
            ],
            "encoding_analysis": [
                "无编码机制。文本直接表达包容性立场，没有使用任何攻击性词汇或编码手段。"
            ],
            "context_analysis": [
                "来自知乎，标记为lgbt话题。原文应该是关于LGBT权利的讨论，叙述者支持在争议中保持相互尊重的态度。",
                "确切的立场（是否支持LGBT权利）取决于被赞同的原始观点。"
            ],
            "supporting_evidence": [
                "核心句子'不能成为高人一等的借口'主张平等对话、反对优越感。",
                "文本基调是支持包容和相互理解的。"
            ],
            "counter_evidence": [
                "如果被赞同的观点本身是反LGBT的，那么这句话可能被用于包装不宽容立场：'我可以不支持，这不代表我高人一等'。"
            ],
            "final_rationale": "Risk: none。文本倡导包容和理解不同立场，不具备攻击性。hard_negative样本。"
        }
    },
    # 003578: "钕人是地雷是吧全身都是雷区要狠狠的打" - DIRECT misogynistic hate
    "003578": {
        "risk_level": "high",
        "encoding_primary": "A1_谐音",
        "encoding_secondary": ["D2_隐喻"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "'钕人'是'女人'的谐音变体，使用化学元素'钕'代替'女'，是网络男权社区的拼写习惯。'地雷'比喻女性像地雷一样危险。'全身都是雷区'进一步扩展此比喻。",
                "'要狠狠的打'直接表达对女性的暴力意图。整句是极端仇女言论。"
            ],
            "encoding_analysis": [
                "A1谐音编码：'钕'为'女'的谐音替代，是男权社区的内部拼写惯例，起到社区成员标识和审查规避作用。",
                "D2隐喻编码：将女性比作'地雷'（危险物），'全身都是雷区'进一步将女性的身体/存在本身比喻为危险区域。",
                "'要狠狠的打'则直接表达了暴力倾向，不再是编码。"
            ],
            "context_analysis": [
                "来自贴吧性别话题讨论。裸文本即表现出极端仇女性质。'钕'是贴吧/知乎男权社区的标准拼写方式。"
            ],
            "supporting_evidence": [
                "'钕人'（女+钕的同音替换）是中文互联网男权社区标志性用语。",
                "'地雷'比喻将女性物化为危险品，是经典仇女修辞。",
                "'要狠狠的打'明确表述暴力攻击意愿。",
                "攻击对象明确——全体女性（'钕人'、'她们'）。"
            ],
            "counter_evidence": [
                "无有效的反方证据。文本是极端仇女暴力言论。"
            ],
            "final_rationale": "Risk: high。通过A1谐音编码（钕=女）结合暴力隐喻（地雷、打），表达对女性的极端仇视和暴力倾向。"
        }
    },
    # 003579: "还有吃生猪皮的东北云南人😆😆😆" - regional mockery
    "003579": {
        "risk_level": "medium",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "medium",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "'还有吃生猪皮的东北云南人😆😆😆'将'东北'和'云南人'组合成一个矛盾身份，称其吃生猪皮并用疯狂笑表情嘲笑。",
                "'生猪皮'（raw pig skin）被作为嘲笑对象，暗示这种饮食习惯落后/野蛮。"
            ],
            "encoding_analysis": [
                "无编码机制。文本直接使用表情嘲笑和食物刻板印象进行地域攻击，没有编码包装。"
            ],
            "context_analysis": [
                "来自知乎地域话题讨论。可能是列举各地饮食习惯的对话链中的评论。需要前文理解'还有'指向的上下文。",
                "'东北云南人'这个矛盾组合暗示叙述者在调侃某种跨区域特征或混居群体。"
            ],
            "supporting_evidence": [
                "😆😆😆表情明确传达嘲笑语气。",
                "'吃生猪皮'将饮食习惯作为贬低目标，是常见的地域歧视手段。",
                "同时涉及两个地域（东北、云南），扩大了攻击范围。"
            ],
            "counter_evidence": [
                "如果是在列举各地奇特饮食的话题中，'吃生猪皮'可能是一个被广泛讨论的话题而非叙述者独创的侮辱。",
                "'东北云南人'可能是对特定文化融合现象的调侃而非蓄意攻击。"
            ],
            "final_rationale": "Risk: medium。通过嘲笑饮食习惯进行地域偏见表达，表情强化了嘲弄态度但文本仍保留了一定的幽默/调侃性质。"
        }
    },
    # 003580: Social commentary on boys/masculinity
    "003580": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "叙述者讨论男孩在现代社会中不能玩弹弓、砌墙、鞭炮、刀枪棍棒等传统玩具，只能玩手办，质疑'哪来的阳刚气魄？'。",
                "这是对当代教育/社会环境中男孩成长空间限制的社会评论，属于关于性别角色和育儿方式的讨论。"
            ],
            "encoding_analysis": [
                "无编码机制。文本使用日常语言讨论社会现象（男孩玩具限制），没有使用攻击性编码。"
            ],
            "context_analysis": [
                "来自贴吧性别话题讨论。这是一个关于性别角色教育的社会评论，不涉及对特定群体的攻击。"
            ],
            "supporting_evidence": [
                "文本讨论的是教育方式和儿童玩具限制，核心关切是男孩成长环境。",
                "'阳刚气魄'虽然是性别气质相关的概念，但在中文语境中是正常的性别教育讨论词汇。",
                "没有攻击任何群体或个人。"
            ],
            "counter_evidence": [
                "文本预设了'玩刀枪棍棒才能培养阳刚气魄'的性别刻板印象，但这是观点表达而非攻击。",
                "标题标签为gender_discussion且toxic=0，标注为无毒。"
            ],
            "final_rationale": "Risk: none。文本是关于育儿方式和社会规范的日常讨论，不具攻击性。hard_negative样本。"
        }
    },
    # 003581: "四年级...依旧站在打拳第一线" - self-mocking about gender debates
    "003581": {
        "risk_level": "medium",
        "encoding_primary": "E1_平台黑话",
        "encoding_secondary": [],
        "ambiguity": "high",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "叙述者回忆四年级时问母亲'为啥男女平等还会有女士优先'，自称'幼年拳皇差点被班主任扼杀在摇篮'，'现在依旧站在打拳第一线'。",
                "'打拳'是中文网络社交通用术语，指参与性别议题辩论。'拳皇'是《拳皇》游戏名称的借用。",
                "叙述者对自己从小参与性别讨论持自嘲/骄傲的态度。"
            ],
            "encoding_analysis": [
                "E1平台黑话：'打拳'在中文网络社区中被赋予了特定含义——指在性别议题上积极辩（通常是女权/平权立场）。'拳皇'借用游戏名，是双关编码。",
                "'幼年拳皇'、'扼杀在摇篮'、'打拳第一线'都是自嘲性表达，借用了游戏和网络术语。"
            ],
            "context_analysis": [
                "来自贴吧性别话题讨论。'打拳'一词在不同社区有不同评价色彩——女权社区是自嘲/骄傲，反女权社区是贬义。",
                "需要知道原始帖子的立场才能判断叙述者的性别立场（是女权支持者还是讽刺者）。"
            ],
            "supporting_evidence": [
                "'男女平等'和'女士优先'的矛盾是女权讨论的常见话题，表明叙述者从小关注性别议题。",
                "'打拳第一线'使用网络黑话表明其对性别议题持续参与。",
                "整体语气自嘲但也带有一定自豪感。"
            ],
            "counter_evidence": [
                "'拳皇'、'打拳'也可能是反女权者的内部用语——用游戏化语言讽刺女权主义者。",
                "由于缺少前文和贴吧社区的多元性，无法确定叙述者的立场方向。"
            ],
            "final_rationale": "Risk: medium。使用'E1打拳'网络黑话讨论性别议题，但立场方向高度歧义（可能是女权自嘲也可能是反女权讽刺），需要上下文。"
        }
    },
    # 003582: Racist sarcastic narrative about mixed-race children
    "003582": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": ["D1_反讽"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "叙述者编造了一个未来场景：与黑人生育的子孙后代供奉'黑白庙堂'，后代会困惑为何'祖宗是黄皮肤的和我们的不一样'，长辈回答'要不是他接盘专业，怎么会有我们'。",
                "'傻缺'直接辱骂当事人，'接盘专业'用股市术语（接盘=接手已贬值资产）来侮辱与黑人结婚的女性。",
                "全文以虚构叙事的方式表达对跨种族婚姻的敌视。"
            ],
            "encoding_analysis": [
                "literal_keyword：'傻缺'是直接辱骂。'接盘'是E1平台黑话，但在本句中因'接盘专业'的使用已高度固化，接近直白表达。",
                "D1反讽编码：整体叙述以虚构的未来对话为载体，字面讲述一个'笑话'但实际传递种族歧视价值观——黑人是劣等的、与黑人生育是'接盘'。"
            ],
            "context_analysis": [
                "来自知乎种族话题讨论。裸文本即可判断其强烈的种族歧视性质。"
            ],
            "supporting_evidence": [
                "'黑白族人'、'黑白庙堂'将种族对立视觉化。",
                "'黄皮肤的'和'不同的'明确表达了对跨种族后代的排斥。",
                "'傻缺'是直接的辱骂。",
                "'接盘专业'将黑人男性贬低为二手/贬值资产，是经典的种族+性别交织侮辱。"
            ],
            "counter_evidence": [
                "无有效的反方证据。文本是虚构叙事包装的种族仇恨言论。"
            ],
            "final_rationale": "Risk: high。通过虚构未来叙事方式表达对跨种族婚姻的敌视，包含直接辱骂和系统性种族歧视价值观。"
        }
    },
    # 003583: "媚外...自贡...国际注意神经" - xenophobic and sexist
    "003583": {
        "risk_level": "high",
        "encoding_primary": "D1_反讽",
        "encoding_secondary": ["A1_谐音"],
        "ambiguity": "medium",
        "evidence_strength": "strong",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本讽刺性地评论某人：'不仅媚外，而且为了不让女的占便宜，敢于自贡。这是多么伟大的国际注意神经'。",
                "'媚外'（fawning on foreigners）是攻击性词汇。'自贡'（Zigong city）作为'自宫'（self-castration）的谐音。'国际注意神经'是'国际主义精神'的戏仿。",
                "讽刺目标：对某类既讨好外国人（媚外）又避免女性'占便宜'的行为的嘲讽。"
            ],
            "encoding_analysis": [
                "D1反讽编码：'这是多么伟大的国际注意神经'是明显的反讽——用褒义词（伟大）搭配扭曲的'国际注意神经'来达到讽刺效果。",
                "A1谐音编码：'自贡'（Zigong城市名）谐音'自宫'（self-castration），是隐晦的性侮辱。"
            ],
            "context_analysis": [
                "来自知乎，标记为种族话题。叙述者讽刺的对象可能既涉及种族（'媚外'——讨好外国人/外族）又涉及性别（'不让女的占便宜'）。",
                "需要前文确定被讽刺对象的具体身份和行为。"
            ],
            "supporting_evidence": [
                "'媚外'是明确的贬义词，指过度崇拜外国/外族。",
                "'自贡'谐音'自宫'，表达了极端的贬低和侮辱。",
                "'国际注意神经'对'国际主义精神'的扭曲，强化了讽刺效果。",
                "😆开头表明这是嘲笑回应。"
            ],
            "counter_evidence": [
                "文本的讽刺对象似乎是某个特定个体或类型的人（'敢于自贡的某人'），而非整个群体。",
                "缺少前文无法确认叙述者所批评的'媚外'和'不让女的占便宜'的具体含义。"
            ],
            "final_rationale": "Risk: high。通过反讽和谐音编码('自贡'=自宫)对目标进行种族和性别交叉攻击，包含强烈侮辱。"
        }
    },
    # 003584: Long political analysis with racial stereotypes
    "003584": {
        "risk_level": "medium",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "medium",
        "evidence_strength": "moderate",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "长文本将美国黑人地位变化归因于资本力量而非民权运动：'与其说是黑人地位不断提升，不如说是资本力量对他们控制厉害'。",
                "包含争议性描述：'黑人还没有现在那么嚣张'（嚣张=arrogant）、'现在黑人嚣张程度到了'。",
                "也包含事实性观察：警队不敢进入贫民窟、贫民窟是'三不管地带'、非法交易被洗白等。"
            ],
            "encoding_analysis": [
                "无编码机制。文本以政治经济分析的面貌呈现，使用常规论证语言。争议性词汇'嚣张'是直接的贬义形容而非编码。"
            ],
            "context_analysis": [
                "来自贴吧，属于种族议题的政治经济分析。作者试图用资本控制论解释美国种族议题。",
                "文本长度表明这是一个有意图的论述而非随口的评论。"
            ],
            "supporting_evidence": [
                "'黑人还没有现在那么嚣张'使用贬义词'嚣张'描述黑人行为，是种族偏见表达。",
                "将黑人地位提升归结为'资本的力量'而非民权运动，否定了黑人的主体性和抗争。",
                "文本结构是'分析'但隐含了'黑人被资本工具化'的底层叙事。"
            ],
            "counter_evidence": [
                "文本中大部分内容是对美国社会结构的政治经济学分析，有论证框架和论据。",
                "对资本力量的批评本身不针对任何种族，而是批判体制。",
                "'嚣张'一词虽然有偏见色彩，但文本的主要框架是宏观分析而非情绪宣泄。"
            ],
            "final_rationale": "Risk: medium。文本以政治经济分析为主框架但包含'嚣张'等种族偏见词汇，种族偏见与学术分析交织，风险程度中等。"
        }
    },
    # 003585: Long misogynistic text about women in power
    "003585": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": ["D1_反讽"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本系统性地论证女性不适合掌权：'中国之要位，自古以来极少极少旁落于女性身上'。引用骆宾王讨伐武则天的檄文攻击女性统治者。",
                "将女性领导力归结为'政治正确'，并发明'中国生孩子协会'、'郭女'等侮辱性术语攻击中国女性。",
                "'男性作为社会的主要生产者'是经典的性别本质主义论述。"
            ],
            "encoding_analysis": [
                "literal_keyword：'郭女'是'国女'的替换，是网络男权社区对中国女性的贬称。'虚空索敌'、'敏思苦想'等网络用语是直白表达。",
                "D1反讽：'创立个中国生孩子协会，然后让郭女把自己捧上主席的位置罢'是极端讽刺，将女性的价值等同于生育。"
            ],
            "context_analysis": [
                "来自贴吧。这是典型的系统性的仇女/反女权论述。裸文本即可判断其极端性别攻击性质。"
            ],
            "supporting_evidence": [
                "'郭女'是中文互联网男权社区对中国女性的系统性贬称。",
                "'中国生孩子协会'将女性的社会价值等同于生育功能，是极端鄙视。",
                "引用武则天檄文是刻意选择最负面的女性统治者形象来论证'女性不适合掌权'。",
                "'男性作为社会的主要生产者'是性别本质主义的经典论述。"
            ],
            "counter_evidence": [
                "无有效的反方证据。文本是全方位的系统性的仇女攻击。"
            ],
            "final_rationale": "Risk: high。系统性的性别本质主义和仇女论述，使用'郭女'、'生孩子协会'等侮辱性称呼攻击全体女性。"
        }
    },
    # 003586: Sarcastic anti-racist
    "003586": {
        "risk_level": "low",
        "encoding_primary": "D1_反讽",
        "encoding_secondary": [],
        "ambiguity": "medium",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "叙述者先赞同某种观点'有道理，国内歧视这么严重，确实不应该冒险'，然后将'不要找南方矮矬子，外地土老帽'比作'经验的传承'，并以'对吧'收尾。",
                "核心机制是反讽：将歧视性偏见说成'经验的传承'，以夸张类比来揭示歧视的荒谬。"
            ],
            "encoding_analysis": [
                "D1反讽编码：表面上赞同歧视立场（'有道理''经验的传承'），实则通过模仿歧视者的口吻来暴露其逻辑的荒谬。'对吧'收尾强化了反讽的对话感。"
            ],
            "context_analysis": [
                "来自知乎，标记为种族话题。文本中的'南方矮矬子、外地土老帽'是地域歧视词汇，但叙述者并非直接使用——而是在模仿歧视者的口气。",
                "缺少前文无法确认叙述者反讽的具体对象。"
            ],
            "supporting_evidence": [
                "'经验的传承'是个正面词汇用于描述歧视观点，这种褒词贬用的反差构成了反讽的基础。",
                "'对吧'结尾邀请读者回应，暗示以上言论是荒谬的、期待认同其荒谬性。",
                "文本结构与典型的反歧视反讽一致：先假装认同→引用歧视观点→以荒谬类比揭穿。"
            ],
            "counter_evidence": [
                "如果读者不识别反讽语气，可能误以为叙述者真的在主张歧视。",
                "'矮矬子'、'土老帽'等词汇本身确实出现在文本中，可能被截取误用。"
            ],
            "final_rationale": "Risk: low。文本使用反讽编码模仿歧视者口吻来批评歧视本身的荒谬，立场是反偏见的。"
        }
    },
    # 003587: "屁股都变成那个国家的了" - xenophobic/sexist
    "003587": {
        "risk_level": "high",
        "encoding_primary": "D3_借代",
        "encoding_secondary": ["E1_平台黑话"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "叙述者评论女性嫁外国人：'屁股都变成那个国家的了'暗示通过婚姻改变效忠对象，将身体部位与国家忠诚建立粗俗关联。",
                "'原来是因为跟这边断了，接受的信息都是另一方了'试图给出一个'理性'解释——因为与国内断了联系，只能接收外国信息。"
            ],
            "encoding_analysis": [
                "D3借代编码：'屁股'借代指代整个人的身份认同/忠诚归属，是粗俗化的借代修辞。",
                "E1平台黑话：'屁股都变成那个国家的'是中文网络社区（尤其是民族主义社区）常用的侮辱性表达，用于攻击跨国婚姻/移民者。"
            ],
            "context_analysis": [
                "来自知乎种族话题讨论。是对中国女性嫁给外国人这一现象的性别+种族双重攻击。",
                "文本将女性物化为国家'资产'，嫁外国人被视为'叛变'和'屁股转向'。"
            ],
            "supporting_evidence": [
                "'屁股都变成那个国家的'用身体部位（屁股）粗俗化地表达国族忠诚的转换，极具侮辱性。",
                "'跟这边断了'暗示嫁外国人的女性断绝了与中国的关系。",
                "目标群体明确：嫁外国人的中国女性。",
                "叙述者表面上给出理性解释（信息断连），但包装的是性别歧视和种族排斥。"
            ],
            "counter_evidence": [
                "文本的后半部分（'原来是...'）试图通过信息不对称来解释跨文化婚姻中的立场变化，有一定分析成分。"
            ],
            "final_rationale": "Risk: high。通过D3借代（'屁股变国家'）攻击嫁外国人的中国女性，是性别仇外交叉的仇恨言论。"
        }
    },
    # 003588: "她们爱找谁找谁，你别去接盘就行了"
    "003588": {
        "risk_level": "medium",
        "encoding_primary": "E1_平台黑话",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本给出建议：'她们爱找谁找谁，你别去接盘就行了'。'接盘'是股市术语（接手别人抛售的股票），在互联网性别讨论中被用来指男性娶有恋爱史/与外国人交往过的女性。",
                "'你别去接盘'劝告男性不要娶被他人'用过'的女性。"
            ],
            "encoding_analysis": [
                "E1平台黑话：'接盘'是中文互联网社区特定词汇，源于股市但在性别话题中被赋予'接手二手/贬值的对象'的含义。熟悉此黑话的社区成员会理解对女性的物化意味。"
            ],
            "context_analysis": [
                "来自知乎，可能是在讨论中外通婚话题的评论链中。'她们'指涉前文讨论的女性群体。",
                "'你别去接盘'是对特定读者/前文评论者的直接劝说。"
            ],
            "supporting_evidence": [
                "'接盘'在性别语境中物化女性，将女性比喻为可被'接手'的交易标的。",
                "'她们爱找谁找谁'表面上大度但'你别去接盘'将其反转——女性与他人（尤其是外国人）交往后价值降低。",
                "这个建议的结构隐含了对女性性自主权的贬低。"
            ],
            "counter_evidence": [
                "'接盘'在日常语境中也可指一般的'接手麻烦'，未必包含性别物化的含义。",
                "文本可能只是对前文某位讨论者就个人处境给出的一般性建议。"
            ],
            "final_rationale": "Risk: medium。使用平台黑话'接盘'表达对女性物化的性别偏见，核心编码E1使得攻击性有一定隐蔽性。"
        }
    },
    # 003589: "中非友谊真的很'好'" - scare quote sarcasm
    "003589": {
        "risk_level": "medium",
        "encoding_primary": "D1_反讽",
        "encoding_secondary": [],
        "ambiguity": "medium",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本只有一句话：'中非友谊真的很'好''，将'好'用引号括起。引号的典型用法是表示反义/质疑——暗示中非友谊并非真正'好'。",
                "删除其他所有修饰后，核心指控是通过引号否定中非友谊的质量。"
            ],
            "encoding_analysis": [
                "D1反讽编码：通过引号（'好'）实现反义表达——表面说'好'，实际说不好。引号是中文网络中最基础的反讽标示手段。"
            ],
            "context_analysis": [
                "来自贴吧种族话题讨论。需要知道引发此评论的事件或讨论才能判断叙述者是在批评中国政府对非洲政策还是在表达种族偏见。",
                "'中非友谊'是政治术语，对此表示讽刺可能涉及政治立场也可能涉及种族偏见。"
            ],
            "supporting_evidence": [
                "'好'的引号是明确的反讽标记，表达了对中非友谊的否定态度。",
                "极简的文本结构（只有一句反讽）表明这是有意为之的评论。"
            ],
            "counter_evidence": [
                "不知道叙述者否定中非友谊的原因——可能批评的是中国的外交政策（政治立场）而非针对非洲人的种族偏见。",
                "没有提供理由或上下文，单句极简评论难以确定具体攻击目标。"
            ],
            "final_rationale": "Risk: medium。通过引号反讽编码表达对中非友谊的否定，但缺少上下文难以区分是种族攻击还是政治批评。"
        }
    },
    # 003590: "广东老太太谁都不虚" - normal comment
    "003590": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本回应一个关于'嗓门大'的讨论，说'广东老太太谁都不虚，无论在哪里'。意思是广东老年女性在嗓门大/气势方面不输给任何人。",
                "这是对特定地域人群特征的观察性评论，语气是调侃/赞美。"
            ],
            "encoding_analysis": [
                "无编码机制。文本是普通口语表达，'谁都不虚'（不输给任何人）是日常用语，无编码。"
            ],
            "context_analysis": [
                "来自知乎，标记为region_discussion但toxic=0，标注正确。"
            ],
            "supporting_evidence": [
                "文本没有攻击任何群体，只是在讨论地域特征。",
                "'谁都不虚'是一种正面或调侃评价，不是贬低。"
            ],
            "counter_evidence": [
                "无风险证据。"
            ],
            "final_rationale": "Risk: none。文本是对广东老年女性的日常调侃式评论，不具攻击性。hard_negative样本。"
        }
    },
    # 003591: "我发现河南邻居里最瞧不起河南的..."
    "003591": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本分析了哪个邻省最瞧不起河南人：第一陕西，第二湖北，山东有优越感但关系还行，安徽关系最好。同时称河北和山西'变穷之后就老实了'。",
                "这是对区域间刻板印象和偏见的经验观察和排序。"
            ],
            "encoding_analysis": [
                "无编码机制。文本用直白的日常语言对区域偏见现象进行观察和排序，没有使用编码手段。"
            ],
            "context_analysis": [
                "来自知乎地域话题讨论。叙述者在讨论不同省份对河南的态度差异。",
                "'变穷之后就老实了'可能含有对经济落后省份的刻板印象。"
            ],
            "supporting_evidence": [
                "文本的分析框架是观察性而非攻击性的——它在讨论谁对河南有偏见，而非表达对河南的偏见。",
                "提到了具体的省际关系对比，呈现出一定的实证性（'我发现'）。"
            ],
            "counter_evidence": [
                "'变穷之后就老实了'对部分欠发达省份（河北、山西）有刻板印象化描述。",
                "这种分析本身是在讨论地域偏见话题，可能强化地域对立的框架。"
            ],
            "final_rationale": "Risk: low。文本是对省际偏见的经验分析，虽有对部分省份的刻板印象但主要框架是观察性评论。"
        }
    },
    # 003592: "我宁愿当太监也不会找黑人🤔" - DIRECT anti-black
    "003592": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本说'我宁愿当太监也不会找黑人🤔'。用'当太监'（被阉割/失去性能力）作为极端牺牲的参照物，以此强调找黑人是不可接受的。",
                "这将黑人（作为婚恋对象）置于比'当太监'更低的位置。"
            ],
            "encoding_analysis": [
                "literal_keyword——直接以'黑人'为攻击目标，用'当太监'与'找黑人'进行极端对比。没有编码包装。"
            ],
            "context_analysis": [
                "来自知乎种族话题讨论。裸文本即可判断其强烈的反黑立场。"
            ],
            "supporting_evidence": [
                "'宁愿当太监也不会找黑人'将黑人婚恋等同于极端负面（不如去势），是对黑人群体的极端贬低。",
                "🤔表情假装思考/犹豫，但结论已明确——'当太监'是更优选择。",
                "目标明确（黑人）、立场明确（排斥）。"
            ],
            "counter_evidence": [
                "无有效的反方证据。文本是直接的反黑人种族表达。"
            ],
            "final_rationale": "Risk: high。通过'当太监'与'找黑人'的极端对比直接表达对黑人的排斥和贬低。"
        }
    },
    # 003593: "太棒了，支持你，什么时候介绍你老婆我认识一下"
    "003593": {
        "risk_level": "medium",
        "encoding_primary": "D1_反讽",
        "encoding_secondary": [],
        "ambiguity": "high",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "字面义：'太棒了，支持你'是正面鼓励。'什么时候介绍你老婆我认识一下'是要求见面。",
                "但结合性别话题讨论的背景，这句话可能暗含威胁或恶意——'认识你老婆'可能是在性别讨论中对对方进行人身威胁或嘲讽。"
            ],
            "encoding_analysis": [
                "D1反讽编码：表面正面支持但实际含义与字面完全相反。'认识你老婆'在性别对抗的语境中常被用作对对方的男性尊严的挑战。"
            ],
            "context_analysis": [
                "来自贴吧性别话题讨论。极度依赖前文：如果前文是某男性在发表大男子主义言论，则'认识你老婆'可能是对其尊严的幽默质疑；如果前文是激烈对抗，则可能是威胁。",
                "裸文本完全无害，但贴吧性别话题的对抗性语境使这句话可能充满敌意。"
            ],
            "supporting_evidence": [
                "'太棒了，支持你'过度热情，可能已经是反讽的信号。",
                "在性别对抗语境下，'介绍你老婆'是一种介入对方私人领域的话语，通常包含挑战或嘲讽意味。"
            ],
            "counter_evidence": [
                "裸文本字面完是友好支持和社交请求，没有任何攻击性词汇。",
                "也可能是真实的赞同和想认识对方家属的友好表达。",
                "高度依赖前文来判断实际意图。"
            ],
            "final_rationale": "Risk: medium。高度歧义的反讽表达——字面友好但在性别对抗语境下可能包含针对男性尊严的挑战。"
        }
    },
    # 003594: "原来女人在你眼里就是个盘" - ANTI-接盘 rhetoric
    "003594": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": True,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本回应他人使用'接盘'一词来讨论女性：'原来女人在你眼里就是个盘。。。有本事你可以不接的嘛。'",
                "叙述者是在批评对方将女性物化为'盘'的思维方式，并说如果你不同意你可以不参与。",
                "这是反性别物化的立场，而非性别攻击本身。"
            ],
            "encoding_analysis": [
                "无编码机制。文本直接引用并反驳对方的'接盘'论述，使用的是日常辩论语言。"
            ],
            "context_analysis": [
                "来自知乎，标记为race_discussion。但文本讨论的核心是性别话题中的'接盘'概念。",
                "叙述者是对前文使用'接盘'的人提出批评。"
            ],
            "supporting_evidence": [
                "'原来女人在你眼里就是个盘'是批评式复述，直指对方物化女性的不当。",
                "'有本事你可以不接的嘛'是辩论式的反驳——如果你不喜欢这样你可以选择不参与。",
                "叙述者站在反物化、反歧视的一方。"
            ],
            "counter_evidence": [
                "文中的'盘'和'接'使用了对方的前设框架，虽然是为了反驳，但也绕不开该框架的语言。"
            ],
            "final_rationale": "Risk: none。文本批评对方物化女性的言论，是反性别歧视的立场。hard_negative样本。"
        }
    },
    # 003595: Political analysis about Taiwan/Hong Kong
    "003595": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本分析台湾香港被'黑'（在网络中被批评）的原因：与全球民粹化有关。台湾香港有人为西方说话，被贴上'汉奸'标签。",
                "提到自媒体让极端言论被大陆网民看到，引起大陆网民的民粹化。但有中央压着，民粹不会成为主流。",
                "这是一个政治分析评论。"
            ],
            "encoding_analysis": [
                "无编码机制。文本使用政治分析的框架和术语（民粹化、汉奸、自媒体、中央压着），是直白的政策评论。"
            ],
            "context_analysis": [
                "来自知乎地域话题讨论。叙述者试图解释台湾香港被网络攻击的政治原因。",
                "这是一个分析性、学术型的评论。"
            ],
            "supporting_evidence": [
                "文本提供了因果分析框架（民粹化→台湾香港被黑→自媒体放大→中央控制），表现出理性讨论意图。",
                "没有直接攻击台湾/香港人群（'汉奸'标签被说成是被贴的、可避免的）。"
            ],
            "counter_evidence": [
                "使用了'汉奸'这一强烈政治词汇（虽然是在分析为什么被贴标签的过程）。",
                "'有中央压着，民粹不会成为大陆的主流'带有一定的政治立场。"
            ],
            "final_rationale": "Risk: low。文本是对台湾香港网络舆论现象的一篇政治分析评论，不具备对特定群体的直接攻击性。"
        }
    },
    # 003596: ANTI-discrimination, pro-Shanghai/Wu language
    "003596": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "叙述者声明自己是上海土著，'反对歧视外地人'，同时希望新老上海人携手传承吴语，'勿相互攻击'。",
                "这是明确的反歧视立场，提倡文化传承的同时反对排斥。"
            ],
            "encoding_analysis": [
                "无编码机制。直接表达包容立场和身份认同，没有使用编码或攻击性语言。"
            ],
            "context_analysis": [
                "来自知乎地域话题讨论。是上海本地人就城市融合与文化传承话题发表的建设性意见。"
            ],
            "supporting_evidence": [
                "'反对歧视外地人'是明确的反歧视声明。",
                "'勿相互攻击'倡导和谐共处。",
                "文本基调是建设和包容的。"
            ],
            "counter_evidence": [
                "无风险证据。"
            ],
            "final_rationale": "Risk: none。文本明确反对地域歧视，倡导本地与外地居民和谐共处。hard_negative样本。"
        }
    },
    # 003597: "你就是河南人，我没说错吧"
    "003597": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "medium",
        "evidence_strength": "weak",
        "needs_context": True,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本说'你就是河南人，我没说错吧'——陈述对方是河南人并确认。",
                "这是对某人地域身份的指认。在关于河南人的地域黑讨论中，这可能是一种标签化攻击，但也可能是单纯确认对方身份。"
            ],
            "encoding_analysis": [
                "无编码机制。文本是直白的身份指认语句。"
            ],
            "context_analysis": [
                "来自知乎地域话题讨论。在前文涉及河南人相关话题（可能是负面刻板印象）时，这句话可能是恶意的'抓到你了'。",
                "但在普通讨论中，确认对方籍贯也是正常的对话行为。"
            ],
            "supporting_evidence": [
                "文本本身没有包含任何侮辱性词汇。",
                "'我没说错吧'包含一种'我有证据'的姿态，但不一定恶意。"
            ],
            "counter_evidence": [
                "如果前文是在贬低河南人，那么'你就是河南人'可能是一种具有攻击性的标签化。",
                "缺少上下文无法判断这句话的真实意图。"
            ],
            "final_rationale": "Risk: none。文本是身份指认语句，未包含攻击性词汇。hard_negative样本。"
        }
    },
    # 003598: "法国不是法国人的法国" - coded anti-immigration
    "003598": {
        "risk_level": "medium",
        "encoding_primary": "C5_概念替换",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本说'法国不是法国人的法国'。第一个'法国'指国家，第二个'法国'指法国人群体（概念替换），第三个'法国'又指国家。",
                "这句话的核心含义：法国（国家）已经不是法国人（法国白人/本土法国人）的法国了。暗示移民改变了法国的民族构成。"
            ],
            "encoding_analysis": [
                "C5概念替换编码：'法国人'一词在本句中从'公民'替换成了'族群/血缘'的意义——用'法国人'(族群意义)指代白人/本土法国人。这种编码需要读者理解该替换才能在移民/种族议题上解码。"
            ],
            "context_analysis": [
                "来自贴吧种族话题讨论。这句话是网络上关于欧洲移民问题的常见口号式论述。",
                "裸文本可理解基本含义，但需要了解欧洲移民/种族人口变化的社会背景。"
            ],
            "supporting_evidence": [
                "两个'法国人'的重复使用产生了族群归属与国家主权之间的张力。",
                "'不是……的法国'是经典的'失去国家'叙事结构。",
                "在互联网语境中，此表述通常与反移民立场关联。"
            ],
            "counter_evidence": [
                "这句话也可能是对社会变化的中性观察（法国因移民变得多元化，不再是单一族群社会）。",
                "极简的表达使得攻击性程度取决于解读角度。"
            ],
            "final_rationale": "Risk: medium。通过C5概念替换编码（'法国人'从公民替换为族群意义）表达对移民改变人口构成的立场。"
        }
    },
    # 003599: "全世界须眉阶级联合起来" - parody of communist slogan
    "003599": {
        "risk_level": "medium",
        "encoding_primary": "E1_平台黑话",
        "encoding_secondary": ["D1_反讽"],
        "ambiguity": "high",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "'全世界须眉阶级联合起来'仿写了共产党宣言口号'全世界无产者联合起来'。'须眉'是古典词，指男性。'须眉阶级'将男性称为一个阶级。",
                "这是对阶级斗争话语的戏仿，套用到性别议题上。"
            ],
            "encoding_analysis": [
                "E1平台黑话：'须眉阶级'是中文网络男权/反女权社区的特定用语，模仿阶级话语包装性别诉求。",
                "D1反讽编码：使用革命口号的庄严形式来表达性别议题，本身带有戏仿和反讽效果。"
            ],
            "context_analysis": [
                "来自贴吧性别话题讨论。这句话的含义取决于立场：男权社区可能认真以此号召男性团结；旁观者可能视为戏仿。",
                "高度依赖社区语境来确定这是认真的性别动员还是戏谑的玩笑。"
            ],
            "supporting_evidence": [
                "戏仿革命口号来讨论性别议题，是典型的网络亚文化表达方式。",
                "'须眉阶级'将男性群体构建为一个利益共同体（阶级），指向性别对抗立场。"
            ],
            "counter_evidence": [
                "这句话也可能是纯粹的文字游戏或戏仿，不包含真正的性别攻击意图。",
                "极短的文本使得判断严重缺乏依据。"
            ],
            "final_rationale": "Risk: medium。戏仿革命口号讨论性别议题，使用E1黑话'须眉阶级'，但极度依赖社区语境判断攻击意图。高度歧义。"
        }
    },
    # 003600: "现在也没有少骂啊 都荷兰喷子 恶意地域攻击"
    "003600": {
        "risk_level": "high",
        "encoding_primary": "A1_谐音",
        "encoding_secondary": ["E1_平台黑话"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本说'现在也没有少骂啊 都荷兰喷子 恶意地域攻击'。'荷兰喷子'字面意思是荷兰的网络喷子。但在中文互联网中这是编码用法。",
                "'荷兰'发音与'河南'高度相似。'喷子'指网络无脑攻击者。'荷兰喷子'等同'河南喷子'——通过谐音攻击河南人。"
            ],
            "encoding_analysis": [
                "A1谐音编码：'荷兰'（Hélán，Netherlands）谐音'河南'（Hénán），是经典的地域歧视审查规避手段。通过使用国家名为掩饰来攻击河南人群。",
                "E1平台黑话：'喷子'是中文网络社区的特定术语，指在网上随意攻击他人者。"
            ],
            "context_analysis": [
                "来自知乎地域话题讨论。裸文本即可判断其通过谐音进行地域攻击。",
                "'恶意地域攻击'这个措辞本身具有讽刺性——叙述者自己正在实施地域攻击。"
            ],
            "supporting_evidence": [
                "'荷兰喷子'在中文互联网上是对'河南喷子'的标准谐音替代表达，频率极高，已是固定搭配。",
                "'恶意地域攻击'与'荷兰喷子'的矛盾使用（一边说别人是恶意地域攻击，一边自己用谐音搞地域攻击）增强了叙述者意图的确定性。",
                "攻击目标明确——河南人。"
            ],
            "counter_evidence": [
                "在极罕见的语境下，'荷兰喷子'可能指字面的'从荷兰来的网络评论者'，但结合语境和平台（知乎中文）这种可能性很低。"
            ],
            "final_rationale": "Risk: high。通过A1谐音编码('荷兰=河南')进行地域攻击，是典型的审查规避型仇恨言论。"
        }
    },
    # 003601: Historical discussion about Li Shimin
    "003601": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本讨论唐太宗李世民的祖先血统：祖母是鲜卑人，父系是汉人（李嵩）。并说明中国和世界的民族认定看父系。",
                "这是一段历史知识分享，涉及种族/民族话题但讨论的是历史和民族认定标准。"
            ],
            "encoding_analysis": [
                "无编码机制。文本是知识性陈述，无攻击性编码。"
            ],
            "context_analysis": [
                "来自知乎种族话题讨论。可能在讨论汉族血统纯正性时引用的历史例子。",
                "文本本身是事实陈述，但可能被用来论证'汉族不纯'或相反论点。"
            ],
            "supporting_evidence": [
                "引用了具体的历史人物和史实（李嵩、太宗祖母鲜卑人）。",
                "提供了民族认定标准的知识（父系认定）。",
                "语气是中性的知识分享。"
            ],
            "counter_evidence": [
                "在民族/种族话题的争论中，这种历史知识可能被选择性使用来支持特定立场。"
            ],
            "final_rationale": "Risk: none。文本是历史知识分享，无攻击性。hard_negative样本。"
        }
    },
    # 003602: "有些gay就是恶心，骚扰人" but also "有些就干干净净"
    "003602": {
        "risk_level": "medium",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本包含两个部分：'有些gay就是恶心，骚扰人，这纯纯没素质行为'；'但有些就干干净净，有干净的圈子和让人舒适的人品'。",
                "叙述者区分了'好gay'和'坏gay'，用'恶心'来描述前者。'再遇到这种骚扰人的你完全可以削他'建议用暴力应对。"
            ],
            "encoding_analysis": [
                "literal_keyword：'恶心'是直接对部分同性恋人群的贬义定性。没有经过编码包装。'削他'是直接的建议使用暴力。"
            ],
            "context_analysis": [
                "来自知乎LGBT话题讨论。叙述者在LGBT话题中表达了评价性立场，既对部分同性恋人做出负面评价又保护'好的'同性恋者。"
            ],
            "supporting_evidence": [
                "'有些gay就是恶心'直接对性少数群体使用'恶心'这一贬义定性。",
                "'再遇到这种骚扰人的你完全可以削他'建议用暴力解决问题。",
                "虽然区分了好和坏，但对被归入'坏'的同性恋者的措辞强烈负面。"
            ],
            "counter_evidence": [
                "文本也承认了存在'干干净净'的同性恋者，不是无差别的群体攻击。",
                "'骚扰人'这个行为确实是不当的，叙述者针对的是行为而非身份本身。",
                "对暴力（削他）的建议在中文口语中常是夸张表达。"
            ],
            "final_rationale": "Risk: medium。文本使用'恶心'形容部分同性恋者并建议暴力，虽有区分'好gay'但整体对性少数群体表达了负面评价。"
        }
    },
    # 003603: "系统删除四个大字...就像长沙的法律"
    "003603": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本抱怨百度贴吧的删帖行为：'系统删除四个大字写在那里'，并评论'删帖规则不明，就像长沙的法律'。",
                "'就像长沙的法律'是对删帖规则模糊的比喻——用比喻表达对平台管理的不满是主要意图。"
            ],
            "encoding_analysis": [
                "无编码机制。对长沙法律的引用是对删帖规则不明的日常比喻，不是对长沙/湖南的地域攻击。"
            ],
            "context_analysis": [
                "来自贴吧，标记为gender_discussion但内容完全不涉及性别。可能是ToxiCN标签错误。",
                "文本是对贴吧删帖管理的不满表达。"
            ],
            "supporting_evidence": [
                "文本核心是批评百度贴吧的删帖规则不透明。",
                "'就像长沙的法律'是比喻性的抱怨，没有直接攻击长沙人或湖南人。",
                "没有使用任何地域侮辱性词汇。"
            ],
            "counter_evidence": [
                "'就像长沙的法律'对长沙的法律体系有一定负面含义，但对地域的指向力很弱——更多强调的是'规则不明'这个抽象特性。"
            ],
            "final_rationale": "Risk: low。文本是对贴吧删帖规则的不满表达，提及长沙的法律是比喻而非系统性地域攻击。"
        }
    },
    # 003604: "河南室友...开玩笑的教我们怎么偷井盖" - recounting experience
    "003604": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "叙述者说上大学前没听过'河南人偷井盖'这个梗，直到碰到河南室友，室友'跟她讲她们河南人为什么偷井盖'并'开玩笑的教我们怎么偷井盖😅'。",
                "文本是在讲述个人经历——通过河南室友了解到这个刻板印象，室友是以开玩笑的方式参与的。"
            ],
            "encoding_analysis": [
                "无编码机制。文本是叙事性经历分享，使用日常口语。"
            ],
            "context_analysis": [
                "来自知乎地域话题讨论。叙述者讲述了一个关于刻板印象如何被传播的个人故事。",
                "室友自己参与玩笑使得文本的性质复杂化——但这更多是叙事而非攻击。"
            ],
            "supporting_evidence": [
                "文本的核心是'第一次听说'和'室友告诉我'，是信息获取经历而非攻击。",
                "😅表情表明叙述者对此感到尴尬或好笑，而非愤怒或歧视。",
                "自嘲/反讽的语气（室友自己开玩笑）降低了攻击性。"
            ],
            "counter_evidence": [
                "'她们河南人为什么偷井盖'直接引用了地域刻板印象。",
                "即使以玩笑方式传播，也仍然在再生产这个刻板印象。"
            ],
            "final_rationale": "Risk: none。文本是个人经历叙事，提到地域刻板印象是在描述现实经历而非表达攻击。hard_negative样本。"
        }
    },
    # 003605: "加速让问题严重才是解决问题的方式"
    "003605": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "medium",
        "evidence_strength": "weak",
        "needs_context": True,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本表达了一种'加速主义'式的观点：让问题变得更严重本身就是解决问题的方法。",
                "这是一句陈述方法论的观点，不涉及具体议题或群体。"
            ],
            "encoding_analysis": [
                "无编码机制。文本是用日常语言表达的政治/社会观点。"
            ],
            "context_analysis": [
                "来自知乎标记为种族话题。虽然标注为种族讨论，但文本本身完全不涉及种族。",
                "可能是对某个种族相关社会问题的应对策略的评论。"
            ],
            "supporting_evidence": [
                "文本是抽象的方法论陈述，没有指向任何具体目标。",
                "无攻击性词汇或编码。"
            ],
            "counter_evidence": [
                "在种族话题讨论中，这种'加速'观点可能被用在种族冲突的语境中。"
            ],
            "final_rationale": "Risk: none。文本陈述加速主义方法论观点，无具体攻击目标。hard_negative样本。"
        }
    },
    # 003606: "我怀疑你在侮辱窑姐...她们白给甚至倒贴" - misogynistic
    "003606": {
        "risk_level": "high",
        "encoding_primary": "D3_借代",
        "encoding_secondary": ["E1_平台黑话"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "'我怀疑你在侮辱窑姐'——说对方在侮辱妓女。'即使窑姐接了还挣钱的呢'——妓女至少还挣钱。'她们白给甚至倒贴🤔'——某些女性不仅不给还倒贴。",
                "文本的核心是将妓女'窑姐'作为比较基准——以妓女来贬低其他女性。"
            ],
            "encoding_analysis": [
                "D3借代编码：'窑姐'（妓女）被借用来作为衡量女性价值的贬低标尺——'还不如窑姐'是比较修辞。",
                "E1平台黑话：'白给'（give away for free）是互联网色情话语中的常见词，指女性在性方面无代价给予。"
            ],
            "context_analysis": [
                "来自知乎种族话题讨论中。文本前半句回应前文的某种说法，但核心是用'窑姐'比喻进行性别侮辱。",
                "🤔表情假装思考/质疑，但实质是用性产业比喻攻击女性。"
            ],
            "supporting_evidence": [
                "'窑姐'是对性工作者的贬称，此处用来和其他女性比较。",
                "'白给甚至倒贴'将女性的性/婚恋行为贬低为免费服务。",
                "比较修辞的核心逻辑：某些女性比妓女更糟。",
                "目标明确——被讨论的女性群体。"
            ],
            "counter_evidence": [
                "文本表面上是为'窑姐'说话（质疑侮辱窑姐），但实质是性贬低。"
            ],
            "final_rationale": "Risk: high。通过D3借代（窑姐作为比较标尺）和性贬低语言对女性进行系统侮辱。"
        }
    },
    # 003607: "一刀劈S这个嘿蛆" - extreme racial violence
    "003607": {
        "risk_level": "high",
        "encoding_primary": "A1_谐音",
        "encoding_secondary": ["literal_keyword"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本说'你们的武士道精神呢？一刀劈S这个嘿蛆'。'武士道'引用日本文化概念。'劈S'是'劈死'的拼写省略。",
                "'嘿蛆'是极端种族侮辱：'嘿'谐音'黑'（black），'蛆'（maggot）是极端的非人化/动物化比喻。'嘿蛆'= '黑蛆' = 黑色蛆虫。"
            ],
            "encoding_analysis": [
                "A1谐音编码：'嘿'谐音'黑'，是规避审查的同音替代。",
                "literal_keyword：'蛆'（maggot）是赤裸裸的非人化侮辱词汇，不属于系统编码体系——属于直接仇恨言论。",
                "'劈S'用英文S替代'死'是网络次文化的拼写习惯。"
            ],
            "context_analysis": [
                "来自贴吧种族话题讨论。裸文本即可判断极端的种族暴力仇恨。"
            ],
            "supporting_evidence": [
                "'嘿蛆'将黑人比作蛆虫，是极致的非人化侮辱。",
                "'一刀劈S'明确表达了暴力杀害意图。",
                "'你们的武士道精神'以质问语气催促采取暴力行动。",
                "目标明确——针对黑人群体。"
            ],
            "counter_evidence": [
                "无有效的反方证据。文本是暴力种族歧视言论。"
            ],
            "final_rationale": "Risk: high。通过A1谐音编码('嘿'=黑)和直接侮辱关键词'蛆'，对黑人群表达极端非人化和暴力杀害意图。"
        }
    },
    # 003608: "找老婆还找强势脾气的纯属自杀" - mild sexism
    "003608": {
        "risk_level": "medium",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本说'谈恋爱也就算了，找老婆还找强势脾气的纯属自杀'。区分了恋爱（可以容忍）和婚姻（不能容忍）。'强势脾气'指性格强势的女性。",
                "'纯属自杀'是夸张说法，形容选择强势女性为妻是自讨苦吃。"
            ],
            "encoding_analysis": [
                "无编码机制。文本用直白的日常语言表达了对特定性格类型女性的负面评价。",
                "'自杀'（日常夸张用法，非字面）不是编码手段。"
            ],
            "context_analysis": [
                "来自贴吧性别话题讨论。表达了对女性性格的个人偏好——偏好温和型而非强势型女性。"
            ],
            "supporting_evidence": [
                "'强势脾气'作为一个女性性格特征被负面化（=找她就等于自杀）。",
                "对女性性格的评判本身就是一种性别预设（认为女性应当温柔）。"
            ],
            "counter_evidence": [
                "这只是个人择偶观点的表达，'强势脾气'对男性同样可以用，不一定是性别攻击。",
                "夸张修辞（纯属自杀）是口语常见表达。",
                "强度较低，属于个人偏好而非系统性的性别攻击。"
            ],
            "final_rationale": "Risk: medium。文本表达了对强势女性的负面评价，属于温和的性别刻板印象表达，但整体强度较低。"
        }
    },
    # 003609: News reporting about scientific study
    "003609": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本是一篇关于澳大利亚研究的转述，研究发现认知能力与反同偏见之间存在相关性。引用了具体的研究机构、作者、样本量、测试方法。",
                "这是完全中性的新闻报道/知识分享。"
            ],
            "encoding_analysis": [
                "无编码机制。文本是学术研究报告的转述，使用中性科学语言。"
            ],
            "context_analysis": [
                "来自贴吧LGBT话题讨论。虽然话题敏感但文本属于科学信息分享。"
            ],
            "supporting_evidence": [
                "提供了具体的学术来源（昆士兰大学、Francisco Perales、《Intelligence》期刊、样本量11564）。",
                "没有表达任何个人立场或评价。",
                "全文是客观转述研究发现。"
            ],
            "counter_evidence": [
                "无风险证据。"
            ],
            "final_rationale": "Risk: none。文本是学术研究报告的中性转述，无攻击性。hard_negative样本。"
        }
    },
    # 003610: "中国男人配不上中国女人的鬼话" - defending against stereotype
    "003610": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本反驳'中国男人配不上中国女人的鬼话'，称其为'带出个好节奏'。指出家庭暴力和情侣矛盾是人类共有的特点，不能'扣帽子说只有中国人会这样'。",
                "叙述者的立场是反对针对中国男性群体的负面刻板印象。",
                "'真是离谱'表达对上述观点的不满。"
            ],
            "encoding_analysis": [
                "无编码机制。文本直接反驳对中国男性的负面刻板印象，表达方式直白。"
            ],
            "context_analysis": [
                "来自知乎，标记为种族话题。但文本讨论的是关于中国男性的性别/国族刻板印象。"
            ],
            "supporting_evidence": [
                "'鬼话'和'带节奏'是在批评某种言论而非攻击群体。",
                "提出反论据（家暴是人类普遍现象）而非情绪宣泄。",
                "整体是反对刻板印象的立场。"
            ],
            "counter_evidence": [
                "文本使用了强烈语气（'离谱'），但语气强≠攻击性。",
                "可能引用到种族相关话题的讨论链中。"
            ],
            "final_rationale": "Risk: low。文本反对针对中国男性的刻板印象，是反偏见立场。"
        }
    },
    # 003611: News report about sexual assault
    "003611": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本引用美国全国广播公司的报道：美国一女子在通勤列车上遭性侵，无乘客报警阻止。",
                "这是一条中性新闻报道的单句摘要。"
            ],
            "encoding_analysis": [
                "无编码机制。文本是客观新闻报道引述，无编码。"
            ],
            "context_analysis": [
                "来自贴吧，标记为种族话题。报道本身没有提及种族信息，但可能被用来讨论美国公共安全问题（可能隐含种族关联）。",
                "文本本身没有任何攻击性内容。"
            ],
            "supporting_evidence": [
                "引用了新闻来源（美国全国广播公司）。",
                "文本是纯粹的新闻转述，不包括评论或立场。"
            ],
            "counter_evidence": [
                "在种族话题讨论中，这种新闻可能被选择性使用来支持特定种族叙事。"
            ],
            "final_rationale": "Risk: none。文本是中性新闻报道转述，无攻击性。hard_negative样本。"
        }
    },
    # 003612: "自己不想被别人黑，但是还去黑别人？" - calling out hypocrisy
    "003612": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "weak",
        "needs_context": True,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本问：'自己不想被别人黑，但是还去黑别人？'——批评双标行为：自己不愿承受却对他人做同样的事。",
                "这是典型的反歧视逻辑：指出施加歧视者也讨厌被歧视。"
            ],
            "encoding_analysis": [
                "无编码机制。文本是直接质问，日常语言，无编码。"
            ],
            "context_analysis": [
                "来自知乎，标记为地域话题。可能在批评某人用双重标准参与地域攻击。"
            ],
            "supporting_evidence": [
                "质问的逻辑结构（'不想被黑但去黑别人'）是反歧视/反双标的常用框架。",
                "文本本身没有包含对任何群体的攻击。"
            ],
            "counter_evidence": [
                "需要前文确定叙述者批评的对象是谁。"
            ],
            "final_rationale": "Risk: none。文本批评双标行为，是反歧视立场。hard_negative样本。"
        }
    }
}

# Apply corrections
for sample in samples:
    sid = sample["id"]
    if sid in corrections:
        corr = corrections[sid]
        for field in ["risk_level", "encoding_primary", "encoding_secondary", "ambiguity", "evidence_strength", "needs_context", "hard_negative", "target_known"]:
            sample[field] = corr[field]
        sample["reasoning"] = corr["reasoning"]
        sample["quality_status"] = "reviewed"
        sample["review_notes"] = sample.get("review_notes", "") + "; reviewed_by=claude; chunk=019"

# Write output
outpath = '/Users/davidchankong/Documents/审查微调/data/raw/batch23_chunks/chunk_019_reviewed.jsonl'
with open(outpath, 'w') as f:
    for sample in samples:
        f.write(json.dumps(sample, ensure_ascii=False) + '\n')

# Summary
high = sum(1 for s in samples if s["risk_level"] == "high")
med = sum(1 for s in samples if s["risk_level"] == "medium")
low = sum(1 for s in samples if s["risk_level"] == "low")
none = sum(1 for s in samples if s["risk_level"] == "none")
hn = sum(1 for s in samples if s["hard_negative"])

print(f"\nchunk_019: wrote {len(samples)} samples")
print(f"  risk_level: high={high}, medium={med}, low={low}, none={none}")
print(f"  hard_negative: {hn}")
print(f"  outfile: {outpath}")

# Verify all have quality_status==reviewed
unreviewed = [s["id"] for s in samples if s["quality_status"] != "reviewed"]
if unreviewed:
    print(f"  WARNING: unreviewed: {unreviewed}")
else:
    print(f"  All samples quality_status=reviewed: OK")

# Print changes summary
print("\nChanges by sample:")
for sample in samples:
    sid = sample["id"]
    old_data = None
    # We don't have old_data but can show new risk
    print(f"  {sid}: risk={sample['risk_level']}, encoding={sample['encoding_primary']}, hard_neg={sample['hard_negative']}")
