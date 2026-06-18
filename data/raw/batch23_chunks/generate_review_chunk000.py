#!/usr/bin/env python3
"""Generate chunk_000_reviewed.jsonl with manually reviewed 50 samples."""
import json

OUTPUT = "data/raw/batch23_chunks/chunk_000_reviewed.jsonl"

samples = []

# ──────────────────────────────────────────────
# 002613
# ──────────────────────────────────────────────
samples.append({
    "id': '002613",
    "source_type': 'real",
    "text": "😓😓什么laji就不要叫了，艾滋里面什么人最多不用多说了吧，不要拿艾滋碰瓷同性恋，散滨😓😓😓",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'lgbt_discussion"},
    "risk_level': 'high",
    "encoding_primary': 'A2_拼音缩写",
    "encoding_secondary': ['literal_keyword"],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'strong",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "文本表面在说'什么laji（垃圾）就不要叫了'——用拼音'laji'规避'垃圾'二字直接写出。接着抛出一个反问句'艾滋里面什么人最多不用多说了吧'，这是在利用艾滋病在同性恋群体中的高感染率这一刻板印象来攻击同性恋群体。'不要拿艾滋碰瓷同性恋'表面是在说不要把艾滋病和同性恋混为一谈，但结合前文，全句的深层含义是反讽式的：表面上在为同性恋说话，实际是在强调同性恋与艾滋病的关联。'散滨'一词不明确，可能是某种编码或输入错误。"
        ],
        "encoding_analysis": [
            "'laji'是'垃圾'的拼音形式，属于A2类拼音编码——用英文字母拼写中文敏感词，以规避关键词检测。'散滨'（san bin）意义不明，可能是另一个词的拼音变体或特定圈内代称，但结合上下文判断其同质性攻击意图已经足够明确。文本核心的攻击机制是直接的：利用公众对'HIV与男同性恋高度相关'的刻板印象进行群体贬损，不需要额外解码。"
        ],
        "context_analysis": [
            "在知乎的lgbt话题下，本评论属于反同语境。用户在讨论中将同性恋与艾滋病捆绑，利用疾病污名化来完成攻击。这种'疾病关联'话术是中文互联网反同言论中最常见的策略之一，不需要更多上下文即可判断其恶意。"
        ],
        "supporting_evidence": [
            "'laji'是'laji=垃圾'的拼音规避写法，表明作者知道内容可能会被审查",
            "'艾滋里面什么人最多不用多说了吧'直接利用同性恋与HIV的刻板印象进行群体攻击",
            "'不要拿艾滋碰瓷同性恋'的反讽结构——表面否定关联、实际强化关联",
            "连续的😓😓😓表情强化了贬低/鄙视的语气"
        ],
        "counter_evidence": [
            "'散滨'一词含义不确定，可能是一个中性名称或特定代称，无法确定其攻击性。但即使忽略该词，全句的恶意已经明确。"
        ],
        "final_rationale': 'Risk: high。文本使用拼音编码'laji'（垃圾的A2编码）加上'艾滋-同性恋'的疾病刻板印象关联，构成对同性恋群体的直接攻击，是典型的反同仇恨言论。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=lgbt; toxic=1; expr=1; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002614
# ──────────────────────────────────────────────
samples.append({
    "id': '002614",
    "source_type': 'real",
    "text': '人家就读错个子，你意见都那么大，你想想为什么那么多人黑河南了吧",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_reporting"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'moderate",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "文本在为一个'读错个子（读错了一个字）'的人辩护，转向反问对方为什么'那么多人黑河南'。核心句式是'你想想为什么'——这是在将'因小错而过度批评'与'地域黑'进行类比，暗示地域黑的根源在于地域歧视者的过度挑剔，而不是地域本身的问题。",
            "'人家就读错个子'中的'个子'是'一个字'的口语化说法（子作为量词后缀）。全句没有出现任何攻击性词汇，也没有对其他省份或群体进行贬低。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本是直白的日常表达，使用标准的反问句式。'黑河南'中的'黑'是网络上对'抹黑/歧视'的通用说法，不属于编码。整段话是论辩性质的评论，没有任何谐音、隐喻、拆字或平台黑话。"
        ],
        "context_analysis": [
            "文本出现在知乎的地域歧视话题下，是对某个具体事件或评论的回应。'读错个子'指向帖中某人因发音错误被批评的事件。上下文可能包含具体的被批评对象，但即使独立看，文本的立场也是反对过度地域歧视的。"
        ],
        "supporting_evidence": [
            "全句没有一个贬义词或攻击性词汇——'意见大'是对行为的描述而非攻击",
            "'你想想为什么那么多人黑河南了吧'是反问句，旨在让对方反思自己行为与地域歧视的相似性，而非在传播地域黑",
            "文本逻辑清晰的因果链：过度批评小事→和地域黑是一个道理，属于反偏见论证"
        ],
        "counter_evidence": [
            "虽然文本整体是反偏见的，但'黑河南'一词出现了，话题本身涉及地域歧视，如果脱离上下文可能被误解为参与地域黑。不过句子的语法结构和逻辑方向明确指向反偏见。"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本虽然提及'黑河南'这一地域歧视话题，但实际是在反对地域黑，通过类比论证批评对方的过度反应。属于反偏见立场的报告/分析，无攻击性内容。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=1; expr=3; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002615
# ──────────────────────────────────────────────
samples.append({
    "id': '002615",
    "source_type': 'real",
    "text': '当面就是从贴吧开始黑河南的，我记得特清楚，什么老乡叫成\"捞翔\"",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_reporting"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'moderate",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "文本在追溯'黑河南'这一地域歧视现象的起源，声称是从贴吧开始的。'我记得特清楚'表明说话者是在回忆。'什么老乡叫成\\\"捞翔\\\"'是举出一个例子：河南方言中的'老乡'（laoxiang）被外地人模仿/嘲笑为'捞翔'（laoxiang的歪曲发音）。",
            "'捞翔'是河南方言中'老乡'一词的发音在贴吧中被取笑和刻板印象化的产物。文本中说话者是在引用这个歧视性用法作为例证，而非自己使用'捞翔'来攻击河南人。"
        ],
        "encoding_analysis": [
            "不存在编码机制。'捞翔'不是作者用来传输隐含意义的编码，而是作者在引用/转述一个已知的地域歧视梗。全文是历史追溯性的报告/分析文本。'黑河南'也是直接的字面用法（黑=抹黑/歧视），没有经过编码包装。"
        ],
        "context_analysis": [
            "文本是对地域歧视现象起源的评论，属于分析/报告型表达。'当面就是从贴吧开始黑河南的'这个判断需要一定的互联网历史知识来理解（贴吧的河南歧视文化），但文本本身不包含攻击性。"
        ],
        "supporting_evidence": [
            "文本明确是在追溯'黑河南'的历史来源，属于分析/报告类型，而非在实施攻击",
            "'我记得特清楚'是回忆性标记词，表明说话者是在陈述所知的历史",
            "'什么老乡叫成\\\"捞翔\\\"'中的'捞翔'是作为被引用的歧视性例子出现，而非作者的攻击用语",
            "全句没有表达对河南人的负面态度，实际是在描述一个现象"
        ],
        "counter_evidence": [
            "文本中出现了'捞翔'这个对河南方言的歪曲模仿词，即使以引用方式出现，仍可能被模型误判为在传播地域黑。且'黑河南'的表述本身也携带地域歧视话题的敏感性。"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本是对贴吧河南地域歧视起源的历史回顾，引用'捞翔'作为例证但并非在实施攻击，属于反偏见立场的报告/分析。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=1; expr=3; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002616
# ──────────────────────────────────────────────
samples.append({
    "id': '002616",
    "source_type': 'real",
    "text': '因为B站圣母婊和政治正确一点也不少，",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'medium",
    "encoding_primary': 'literal_keyword",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'medium",
    "evidence_strength': 'moderate",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "文本批评B站存在大量'圣母婊'和'政治正确'的内容/用户。'圣母婊'是中文互联网上对自以为道德高尚、过度同情/包容的人的一个侮辱性称呼。'政治正确'是指不基于事实而基于政治立场表达观点。",
            "值得注意的是，虽然上下文topic标记为race_discussion，但文本本身没有提到任何种族或群体。'圣母婊'是一个带有性别色彩的侮辱性词汇（婊=bitch），但在中文互联网语境中已经高度泛化，常被用作批评他人'装圣母'的通用攻击词。"
        ],
        "encoding_analysis": [
            "'圣母婊'是直接使用的侮辱性词汇，不存在编码——它本身就是攻击性表达。'圣母'（saintly mother/too kind person）+ '婊'（bitch）合成一个复合谩骂词。这属于literal_keyword类。不存在谐音、隐喻或其他编码机制。"
        ],
        "context_analysis": [
            "该文本来自贴吧，话题为种族讨论，但文本中并未明确提及种族。'政治正确'可能涉及种族议题（如对少数族裔的态度），但文本太短，且缺乏对话上下文来确定政治正确指的是什么具体内容。'圣母婊'也缺乏具体的指向对象。需要更多上下文（帖子的标题、被回复的内容等）才能做出准确判断。"
        ],
        "supporting_evidence": [
            "'圣母婊'是一个侮辱性称呼，其中的'婊'是典型的贬损后缀，具有攻击性",
            "话题上下文为race_discussion，表明这段话可能是在种族相关的讨论中批评那些被认为过于同情少数族裔的用户"
        ],
        "counter_evidence": [
            "文本中没有出现任何种族相关的词汇（黑人、白人、移民等），'圣母婊'和'政治正确'的攻击对象可能是任何类型的B站用户，不一定是种族相关",
            "'圣母婊'在中文互联网中已被广泛用作一般性网络骂人话，攻击性有一定程度的弱化，不一定构成群体仇恨言论",
            "单句不完整（以逗号结尾），可能是更长的评论中的一部分，缺乏完整的语境"
        ],
        "final_rationale': 'Risk: medium。文本使用'圣母婊'这一侮辱性词汇攻击B站用户，含性别化贬损成分，且话题涉及种族讨论语境，但因缺乏明确指向和完整上下文，风险等级为中等。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=race; toxic=1; expr=1; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002617
# ──────────────────────────────────────────────
samples.append({
    "id': '002617",
    "source_type': 'real",
    "text': '现在各高校都是艾滋频发区，那个学校留学生多，那个学校艾滋高。前俩年在各大高校免费发放艾滋测试纸，当天发放当天完。然后引起轰动。具体可以去b站看看",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'high",
    "encoding_primary': 'literal_keyword",
    "encoding_secondary': ['C4_典故/物品/符号借用"],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'strong",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "文本做出了一个明确的因果论断：'那个学校留学生多，那个学校艾滋高。'——将留学生数量与艾滋病发生率直接挂钩。随后提到高校免费发放HIV检测试纸'当天发放当天完'，暗示检测阳性率高。最后指引去'b站'（Bilibili）查看详情。",
            "文本的核心是一个刻板印象——留学生（特别是特定国家的留学生）携带HIV的比例更高。这个论断被包装成'事实报告'的形式呈现，增加了可信度上的误导性。"
        ],
        "encoding_analysis": [
            "文本主要使用直接陈述的句式（literal_keyword），不存在谐音、缩写、拆字等编码。但是存在一种C4类符号借用：'留学生'是公开群体代称，但在上下文中承载了种族歧视的隐含意义——'留学生'在此特指非洲/亚非拉留学生。'b站'是Bilibili的缩写，属于常规平台简称，不是编码。"
        ],
        "context_analysis": [
            "知乎的种族讨论语境下，'留学生多→艾滋高'这种表述是典型的种族歧视话术，利用艾滋病污名化来攻击特定留学生群体（主要指向非洲留学生）。虽然文本是以'新闻报道'语气呈现的，但论断本身缺乏统计数据支撑，属于煽动性言论。"
        ],
        "supporting_evidence": [
            "'那个学校留学生多，那个学校艾滋高'是一个明确的因果论断，将留学生群体与艾滋病捆绑，属于群体污名化",
            "引用'免费发放艾滋测试纸当天发放当天完'作为证据，暗示高校中HIV感染率极高且与留学生相关",
            "使用新闻报道式的口吻（'前俩年'、'具体可以去b站看看'）来增强论断的可信度"
        ],
        "counter_evidence": [
            "作者可能是在引用或转述某个实际发生过的事件（高校检测试纸发放活动），字面事实不一定虚假。但文本的指向——将留学生群体作为HIV高发群体来污名化——是明确的。"
        ],
        "final_rationale': 'Risk: high。文本以报道式语气做出'留学生多→艾滋高'的因果论断，利用艾滋病污名化攻击留学生群体（主要指向非洲留学生），是种族歧视仇恨言论。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=race; toxic=1; expr=1; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002618
# ──────────────────────────────────────────────
samples.append({
    "id': '002618",
    "source_type': 'real",
    "text': '很多同性恋，特别是母零。这一辈子都想当女人。就开始学一些女人的特征，开始假装自己是一个女王。想了半天女人的特征到底是什么呢？没有想到自信没有想到包容没有想到善良也没有想到温柔，却学到了泼妇的刻薄。以及淫妇的放纵。",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'lgbt_discussion"},
    "risk_level': 'high",
    "encoding_primary': 'E1_平台黑话",
    "encoding_secondary': ['D3_借代"],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'strong",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "文本攻击同性恋中的'母零'（女性化的男同性恋中的'零/'受'方）。作者声称'母零'一辈子想当女人，但又说他们在学习女性特征时，学到的不是自信、包容、善良、温柔这些正面特征，而是'泼妇的刻薄'和'淫妇的放纵'。全段构建了一个'同性恋=心理扭曲、只能模仿女性负面特征'的刻板印象。"
        ],
        "encoding_analysis": [
            "'母零'是中文同性恋亚文化的黑话——'零'是男同性恋中扮演女性/受方角色的代称（源自0/1的性角色分类），'母'指女性化特征。这个词在这个文本中被用作贬义标签（E1平台黑话分类）。'女王'、'泼妇'、'淫妇'是D3借代——用这些女性角色类型来代表作者认为的'女性负面特征'。"
        ],
        "context_analysis": [
            "贴吧是反同言论的高发平台。该文本运用了'同性恋者扭曲地模仿女性'的经典反同叙事框架。作者将'女性的正面特征'（自信、包容等）与'女性的负面特征'（泼妇、淫妇）对立，构建一个'同性恋只能学到坏的东西'的讽刺性论证。"
        ],
        "supporting_evidence": [
            "'很多同性恋，特别是母零'——以群体范围词开头，将攻击对象扩大化到几乎整个同性恋群体",
            "'这一辈子都想当女人'——对同性恋者心理的轻蔑性总结，抹杀了性取向的多样性",
            "'没有想到自信没有想到包容没有想到善良也没有想到温柔'——用排比强调同性恋者缺失了所有正面特质",
            "'却学到了泼妇的刻薄。以及淫妇的放纵'——使用'泼妇'和'淫妇'两个高度贬义的女性标签来污名化同性恋者"
        ],
        "counter_evidence": [
            "文本使用的是贴吧反同社区内部常见的叙事模板，对不熟悉这种叙事的人来说可能看起来像在讨论性别特征。但'泼妇的刻薄。以及淫妇的放纵'的攻击性表述过于明确，难以被误读为中性讨论。"
        ],
        "final_rationale': 'Risk: high。文本使用平台黑话'母零'（E1）和'泼妇/淫妇'借代（D3），构建'同性恋者只能学到女性负面特征'的污名化叙事，是对男同性恋群体的明确仇恨攻击。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=lgbt; toxic=1; expr=1; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002619
# ──────────────────────────────────────────────
samples.append({
    "id': '002619",
    "source_type': 'real",
    "text': '而且，跟她走太近，在圈子里跟着社死",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'none",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'high",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "文本说'跟她走太近，在圈子里跟着社死'——字面意思是如果和一个特定女性走得太近，在某个社交圈子里就会'社死'（社会性死亡）。'社死'是中文互联网上的常用缩写词，指因某事导致社交信誉严重受损，常常尴尬到无法在圈子中继续正常社交。",
            "文本中没有提到任何与种族相关的词汇。'她'指的是谁完全不清楚。'圈子'指什么社交圈也完全没有说明。这是一段高度依赖上下文的碎片化表达。"
        ],
        "encoding_analysis": [
            "不存在编码机制。'社死'是'社会性死亡'的简写（A2拼音缩写类），但这是中文互联网上极其普遍的通用词汇，使用频率极高，属于大众通用缩写而非风险编码。文本没有使用任何谐音、隐喻、借代或者其他编码方式来传输隐含攻击。"
        ],
        "context_analysis": [
            "虽然上下文标记为race_discussion，但文本中没有任何种族相关的内容。'跟她走太近'可能指与某个有争议的人物交往。'社死'是常用网络用语。这段文本的信息量极度有限，没有足够证据表明它涉及任何风险话题。可能是在讨论某人因与某个特定人物（可能是跨种族恋情的女性？）走得太近而在圈子里遭受排挤，但高度不确定。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的非有毒标注（toxic=0），文本本身没有攻击性词汇",
            "'社死'是通用网络用语，不具有特殊的风险编码意义",
            "文本读起来像是对某社交事件的评论，而非在表达攻击或偏见"
        ],
        "counter_evidence": [
            "话题标签为race_discussion，意味着它出现在种族讨论的帖子中。如果'她'是一个与外国男性（如黑人）交往的中国女性，那么'跟她走太近→社死'可能涉及种族偏见——认为应该与这类人保持距离以免被连累。但这种解读完全依赖外部猜测，无法从文本本身证实。"
        ],
        "final_rationale': 'Risk: none (hard_negative)。文本信息量极低，仅表达'跟某人走太近会导致社交损失'的意思，没有任何攻击性词汇或编码机制。虽然标注话题为种族讨论但文本本身不包含种族相关内容。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=race; toxic=0; expr=0; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002620
# ──────────────────────────────────────────────
samples.append({
    "id': '002620",
    "source_type': 'real",
    "text": "“这里是你的吗？是你买的吗？这里是我的！”某默视频里这么说的😆所以没有自己的文化，怎么才能过得更好呢？当然是去吃别人碗里的😆",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'high",
    "encoding_primary': 'C4_典故/物品/符号借用",
    "encoding_secondary': ['A1_普通谐音"],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'strong",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "文本引用了一段据称来自'某默视频'的对话——某人宣称'这里是我的'（占有某物/场所）。然后作者说'所以没有自己的文化，怎么才能过得更好呢？当然是去吃别人碗里的'——这是在评论一个种族或民族没有自己的文化，只能掠夺/依赖别人的资源。",
            "'某默'中的'默'是代指'黑人/黑人的'的一种编码写法。'默'字的本义是'沉默/黑暗'，在此被用作'黑'的近似替代（黑→默，颜色上的近似代指）。"
        ],
        "encoding_analysis": [
            "'某默视频'中的'默'是C4类编码——'默'作为'黑'的符号替代（语义上暗/黑相似），'某默'即'某个黑人（的视频）'。这属于用相近语义但不同字面来指代目标对象的编码机制。随后'没有自己的文化'、'去吃别人碗里的'是直接的攻击性比喻（→说黑人没有自己的文化、靠掠夺为生）。整体编码路径是：默→黑→黑人→黑人无文化→黑人掠夺。"
        ],
        "context_analysis": [
            "在知乎的种族讨论语境中，'默'是网络上用来替代'黑'的常见规避写法（因为'黑'字可能触发审查或因为'黑'的敏感度更高）。后面'没有自己的文化'和'吃别人碗里的'是种族歧视中关于'黑人没有自己的文明、只会抢夺'的经典话术。"
        ],
        "supporting_evidence": [
            "'某默视频'中的'默'明确指向'黑'（黑人），是规避审查的替代编码",
            "'没有自己的文化'是对整个群体的否定，宣称某个种族缺乏文明成就",
            "'去吃别人碗里的'是掠夺/寄生比喻——暗示该群体不创造价值只靠侵占他人谋生",
            "😆表情的反复使用表示作者以戏谑/嘲讽的态度传播这种观点"
        ],
        "counter_evidence": [
            "'某默'也可能是指某个视频博主的绰号或ID中含有'默'字（如'默默'、'默然'等），不一定指向种族。但结合'没有自己的文化'的攻击性评论，种族指向基本可以确认。"
        ],
        "final_rationale': 'Risk: high。文本使用'默→黑'的C4符号替代编码指代黑人，配合'没有自己的文化'和'去吃别人碗里的'直接攻击，构成典型的种族仇恨言论。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=race; toxic=1; expr=1; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002621
# ──────────────────────────────────────────────
samples.append({
    "id': '002621",
    "source_type': 'real",
    "text': '谁会觉得非洲黑人高人一等？中国女孩找非洲黑人做男朋友的原因不用分析，都是成年人难道她们不知道非洲人艾滋病携带者比例有多高？难道她们不知道非洲男朋友找她们只是为了排解寂寞？难道她们不知道即使跟她们结婚是为了拿居住权？她们很清楚。看看那些找非洲男朋友的女孩有几个是被中国男孩看上眼的，人家也有情感和生理上的需求好吗。至于那些所谓被骗p，染病，单亲女孩来说，大家看到几个来控诉的？没违法没道德败坏的何来批判之说。别拿黑人前男友感染艾滋病又传染给中国丈夫和孩子的例子说事儿，那种愚蠢的男女还是很少的。欧洲有些国家的女性倒是不鸟这些黑人和中东移民、难民结果这些国家被qj的女性直线上升。弄得当地ZF各种宣传教他们怎么跟当地女孩发生性关系。说到中国女孩找非洲男朋友为其他女同胞挡了多少伤害。所以批判是不存在的最好防护措施就好了。",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'high",
    "encoding_primary': 'literal_keyword",
    "encoding_secondary': ['D1_反讽"],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'strong",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "这是一段长篇的种族歧视檄文。核心论点是一个反讽性的'中国女孩找非洲男朋友=为其他女同胞挡伤害'——表面上似乎在为这些中国女孩辩护，实际上是在系统地列出非洲男性的各种负面刻板印象：HIV携带率高、只想排解寂寞、骗婚取居住权、感染中国女性后传给中国丈夫等。",
            "文本还进行了跨国比较：说欧洲女性'不鸟这些黑人和中东移民、难民'后，被强奸率'直线上升'——将黑人和中东移民等同于性侵威胁。作者使用了大量反问句来强化刻板印象的'天然正确性'。结尾的'批判是不存在的'和'最好防护措施就好了'是反讽（D1）——表面说不需要批判，实际上是在进行最严厉的批判。"
        ],
        "encoding_analysis": [
            "文本几乎全部使用直接语言（literal_keyword），直接出现了'非洲黑人'、'艾滋病携带者比例'、'被qj'等明确词汇，没有经过谐音或编码包装。主要的修辞工具是D1反讽——'所以批判是不存在的最好防护措施就好了'是典型的反讽表达，表层的'不需要批判'与深层的大量攻击形成鲜明对比。"
        ],
        "context_analysis": [
            "文本属于中文互联网中'中国女性与外籍男性（特别是非洲男性）交往'这一持续争议话题下的典型极端观点。作者试图用'理性分析'的外壳包装种族偏见，引用各种'论据'（艾滋病比例、签证居留权、欧洲强奸案等）制造看起来有理有据的假象。这种精确的'分析式种族主义'是知乎平台上的一种常见形式。"
        ],
        "supporting_evidence": [
            "一连串的反问句'难道她们不知道……？难道她们不知道……？'实质是强迫读者接受'非洲男性=HIV/性侵/骗婚'的等同关系",
            "'欧洲有些国家的女性倒是不鸟这些黑人和中东移民、难民结果这些国家被qj的女性直线上升'——将黑人和中东移民与性侵犯罪直接挂钩",
            "'别拿黑人前男友感染艾滋病又传染给中国丈夫和孩子的例子说事儿，那种愚蠢的男女还是很少的'——虽然表面说别拿这些例子说事，但实际是在强调这些'例子'的存在",
            "反讽结论句'所以批判是不存在的最好防护措施就好了'——表面说不需要批判，实际是在进行最大程度的批判"
        ],
        "counter_evidence": [
            "文本中有部分句式可以解读为对选择与非洲男性交往的中国女性的同情（'人家也有情感和生理上的需求'），但这层伪装的'理解'被大量的负面刻板印象所淹没，整体基调是种族攻击性的。"
        ],
        "final_rationale': 'Risk: high。文本使用直接语言（literal_keyword）系统性地将非洲/黑人男性与HIV、性侵、骗婚、文化低等负面刻板印象挂钩，以反讽（D1）修辞包装，构成明确的种族仇恨言论。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=race; toxic=1; expr=1; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002622
# ──────────────────────────────────────────────
samples.append({
    "id': '002622",
    "source_type': 'real",
    "text': '咱们没人家团结，我经常去剑网3吧看攻略，结果，现在哈哈哈哈哈哈哈哈哈哈哈哈哈哈全都是籹全尸在打拳。",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'gender_discussion"},
    "risk_level': 'high",
    "encoding_primary': 'B1_拆字",
    "encoding_secondary': ['E1_平台黑话"],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'strong",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者说自己去'剑网3吧'（剑侠情缘网络版3吧，一个武侠游戏的贴吧）看攻略，结果发现'全都是籹全尸在打拳'。'打拳'是中文互联网上对女权/女性主义者的贬称（源自'打拳击'，'拳师'代指女权主义者）。'籹全尸'是一个复合编码词，由'籹'和'全尸'组成，攻击那些被认为'女权'的女性。",
            "'籹'字是汉字'女'的一个古代变体或罕见字，在此被拆解/组合成一个侮辱性称呼。全句表达了作者对剑网3贴吧被女权主义者'占领'的不满和嘲讽。"
        ],
        "encoding_analysis": [
            "'籹全尸'是B1拆字类编码与E1平台黑话的组合。'籹'（nǚ）是'女'的异体/古体字，在此被用作对女性的蔑称。'全尸'（complete corpse）是直接的中文词汇但组合方式异常。整体词'籹全尸'可能是利用字形对'女'相关词汇进行编码攻击。'打拳'是E1平台黑话——在贴吧/A岛等平台中'拳师/打拳'是专指女权主义者的贬称，不了解此文化的人无法理解其指向。"
        ],
        "context_analysis": [
            "剑网3吧本身是一个以女性玩家为主的游戏社区，'籹全尸在打拳'是对该社区女性玩家群体的一种蔑称。'哈哈哈哈哈哈哈哈哈哈哈哈哈哈'的超长笑声表达了强烈的嘲讽态度。文本的核心是对女性参与网络讨论的敌视。"
        ],
        "supporting_evidence": [
            "'籹全尸'使用罕见/变体字形编码对女性群体进行侮辱，属于B1拆字类编码",
            "'打拳'是平台黑话（E1），专门用于贬称女权主义者/积极表达性别观点的女性",
            "文本出现在贴吧的性别讨论语境中，攻击女性群体（剑网3的玩家多为女性）",
            "'哈哈哈哈哈哈哈哈哈哈哈哈哈哈'连续笑声强化了嘲讽/轻蔑的语气"
        ],
        "counter_evidence": [
            "'籹全尸'的具体编码还原路径存在争议——'籹'的解码方式可能需要更多的贴吧社区知识才能完全确定。但这不影响整体的攻击性判断，因为'打拳'的指向已经非常明确。"
        ],
        "final_rationale': 'Risk: high。文本使用字形编码'籹全尸'（B1拆字）和平台黑话'打拳'（E1），对游戏社区中的女性群体进行性别攻击，构成仇恨言论。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=gender; toxic=1; expr=1; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002623
# ──────────────────────────────────────────────
samples.append({
    "id': '002623",
    "source_type': 'real",
    "text': '楼主你恐怕不知道虫类及其后代虫混是拉美人外全球第二大贩毒和运毒和磕药的大户",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'high",
    "encoding_primary': 'D2_隐喻",
    "encoding_secondary': ['literal_keyword"],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'strong",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "文本说'虫类及其后代虫混是拉美人外全球第二大贩毒和运毒和磕药的大户'。表面在讨论全球毒品贸易，但'虫类'和'虫混'是将某个特定种族人类贬低为虫子的比喻。'虫混'='虫子的混血后代'。结合话题标签race_discussion和平台（贴吧），这里'虫类/虫混'指向的是黑人群体。",
            "文本使用了非人化的语言（dehumanization）——将人类比作虫子（害虫），这是种族歧视中最极端的修辞之一。"
        ],
        "encoding_analysis": [
            "'虫类'和'虫混'是D2类隐喻——用'虫'（虫子/害虫）作为比喻载体（源域），映射到目标对象（目标域是黑人群体）。选择'虫'作为比喻意象本身就带有强烈的贬低和排斥意味，暗示该群体如害虫般低等、有害、需要清除。'拉美人'（拉丁美洲人）是直接提及的对照群体。整体编码路径：虫类（源域）→黑人群体（目标域）。"
        ],
        "context_analysis": [
            "在贴吧种族讨论语境中，'虫类'已经是特定群体对黑人的习惯性蔑称（类似于欧美极右翼将少数族裔称作'vermin'）。文本出现在一个对话（对'楼主'说），是在'科普'某个种族群体在毒品贸易中的作用。"
        ],
        "supporting_evidence": [
            "'虫类'和'虫混'（虫子的混血后代）是对人类的非人化比喻，将人等同于低等生物",
            "'全球第二大贩毒和运毒和磕药的大户'——将种族群体与毒品犯罪直接挂钩，进行群体污名化",
            "文本来自贴吧种族话题讨论，'虫类'在此是已知的种族歧视代称"
        ],
        "counter_evidence": [
            "对于不熟悉贴吧黑话的读者，'虫类'字面上可能被理解为在说昆虫。但后续的'拉美人外全球第二大……'表明讨论的是人类群体，结合'楼主'的称呼方式可见是在对他人发表观点，不是关于昆虫的讨论。"
        ],
        "final_rationale': 'Risk: high。文本使用D2隐喻将黑人群体非人化为'虫类/虫混'，并将其污名化为全球毒品犯罪的主要力量，构成极端种族仇恨言论。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=race; toxic=1; expr=1; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002624
# ──────────────────────────────────────────────
samples.append({
    "id': '002624",
    "source_type': 'real",
    "text': '这个作者，完全说出了我的心里话 。人家一个愿打一个愿挨 。。操哪门子心 。怎么样，人家也不会瞧得起国男的。小心别接盘就可以了 。",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'medium",
    "encoding_primary': 'E1_平台黑话",
    "encoding_secondary': ['D1_反讽"],
    "needs_context": True,
    "ambiguity': 'medium",
    "evidence_strength': 'moderate",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者认同某个帖子的观点（'完全说出了我的心里话'）。关键句'人家也不会瞧得起国男的'——这里的'国男'是中文网络上对'中国男性'的自称/他称。'小心别接盘就可以了'中的'接盘'原为股市用语（高位接盘），在网络婚恋语境中指娶一个与非中国男性（在race_discussion语境下指与外国男性有恋爱或性经历）的女性。",
            "文本的完整含义是：中国女性与外国男性发生关系后，不会尊重中国男性，所以中国男性的建议是'不要接盘'（不要娶这些女性）。包含了对中国女性的贬损（选择外国男性）和对外国男性的排斥。"
        ],
        "encoding_analysis": [
            "'国男'是中文互联网中的政治/性别话题常用词（E1平台黑话），在性别对抗语境中指代'中国男性'整体，带有性别/民族对立的色彩。'接盘'是E1平台黑话——从股市术语被借用到婚恋语境，指接受有特定恋爱史的女性。这两个词脱离平台语境后含义不同，属于社区内部黑话。"
        ],
        "context_analysis": [
            "在race_discussion主题下，这段评论最可能是在讨论中国女性与外国（非洲/黑人）男性交往的话题。'人家一个愿打一个愿挨'——指当事人（中国女性和外国男性）各取所需。'操哪门子心'——批评第三方多管闲事。全句呈现一种冷漠的实用主义态度：不阻止跨种族交往但主张'国男'自我保护。"
        ],
        "supporting_evidence": [
            "'人家也不会瞧得起国男的'——暗示与外国男性交往的中国女性会看不起中国男性，是性别+种族的双重贬损",
            "'小心别接盘就可以了'中的'接盘'在跨种族语境中暗示中国男性不应接受有过外国伴侣的女性",
            "'人家一个愿打一个愿挨'——将跨种族关系描述为'一个愿打一个愿挨'（一方愿意挨打），对关系持贬低态度"
        ],
        "counter_evidence": [
            "文本没有直接使用种族侮辱性词汇（如黑鬼、默等）。'人家一个愿打一个愿挨'可以被解读为对当事人自主选择权的尊重（不干涉态度）。'小心别接盘'也可以被解读为对个人婚恋风险的善意提醒。文本的毒性是间接的，依赖于读者对'接盘'编码的理解。"
        ],
        "final_rationale': 'Risk: medium。文本使用平台黑话'国男'和'接盘'（E1），在跨种族婚恋话题中表达了对中国女性的贬低和对外国男性的排斥，但攻击性较为间接。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=race; toxic=1; expr=2; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002625
# ──────────────────────────────────────────────
samples.append({
    "id': '002625",
    "source_type': 'real",
    "text': '可以找，但不要住在中国了",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'medium",
    "encoding_primary': 'literal_keyword",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'high",
    "evidence_strength': 'weak",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "一句话文本：'可以找，但不要住在中国了'。主语和宾语都没有明确给出，但根据话题（race_discussion）和语境，这很可能是对跨种族婚恋的评论——'可以找（外国人/黑人），但不要（让他们/你们）住在中国了'。",
            "文本表达了一种有条件的容忍：不反对跨种族关系，但主张将外国伴侣排除在中国之外。这是一种排斥性态度（exclusionary position）。但因为文本极度简短且缺乏主语，歧义很高。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本使用直接的字面语言（literal_keyword），没有任何谐音、拆字、隐喻或其他编码方式。其潜在的风险来源于语义本身（对外国人的排斥性主张）而非编码机制。"
        ],
        "context_analysis": [
            "由于文本只有9个字且缺少主语/宾语，必须依赖外部上下文才能确定其准确含义。在race_discussion话题下，可能的完整语境是：某帖讨论中国女性找黑人/外国男友，此评论回应道——'可以找，但不要（让黑人/外国人）住在中国了'。这种'接纳但不允许多元化'的态度在跨种族讨论中常见。"
        ],
        "supporting_evidence": [
            "文本表达了对外国人的排斥态度——允许短期存在但不接受长期共同生活",
            "话题标签为race_discussion，指向该评论是在种族/跨种族关系的讨论语境中发出的"
        ],
        "counter_evidence": [
            "文本缺少主语和宾语，无法确定'找'的对象和'住'的主体。也有可能是在讨论非种族话题（如海外工作、留学）。'但不要住在中国了'可能指的是特定个人而非整个群体。文本太短，证据强度极弱。"
        ],
        "final_rationale': 'Risk: medium。文本表达了'可以交往但不能住在中国'的排外态度，指向外国群体，但因句子极短且缺乏主语宾语，歧义高、证据弱，风险等级为中等。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=race; toxic=1; expr=2; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002626
# ──────────────────────────────────────────────
samples.append({
    "id': '002626",
    "source_type': 'real",
    "text': '曼联前领队朗金斯说\"中国女人那么丑，怎么还会生那么多孩子？\"中国女人丑不丑我说不清楚，但很多欧洲女人从11岁开始过性生活，换男人如换衣服，如前所述，\"战场\"早就百孔千疮，甚于饱受美军贫铀弹蹂躏的科索沃土地，爱情本能想来也所剩无几，离婚率高得离谱，自然没有多少孩子可生了。柏林的妇产科医院空荡荡，巴特基辛根人口平均年龄68岁，意大利小镇一个接一个消亡。整个欧洲都在老去，等着吃财政饭的老人越来越多，再加上欧洲各国财政状况糟糕，可能那些人会靠喝西北风活下去？！韩国首尔国立大学社会学教授殷基洙说：\"除非能把人口问题处理好，否则，韩国社会将会在20至30年内崩溃。\"日本情况也差不多。如果算上移民因素，欧洲在30年内必然崩溃——统计已表明欧洲出现了可怕的劳动力向美转移。欧洲崩溃，全球遭殃，中国会比欧洲倒得更快。关于中国的新人口危机，防风和何亚福两人合写的《中国新人口危机》有详尽的论述，读者可以一读。我要说的是，由于他们没有发现生育率低的真正原由，他们对危机爆发的时间估计不准。如果放任下去，即使不受外部拖累，中国也会在50年内崩溃。",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'gender_discussion"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "这是一篇关于全球人口危机的长篇分析。开篇引用'曼联前领队朗金斯'说的'中国女人那么丑，怎么还会生那么多孩子？'——但作者随即表示'中国女人丑不丑我说不清楚'，没有赞同该观点。随后作者讨论欧洲人口下降的原因（'欧洲女人从11岁开始过性生活，换男人如换衣服'→性开放导致生育率低），以及韩国、日本、中国的人口危机。",
            "文本的主要论点是全球人口危机（老龄化、低生育率），引用了多个来源（韩国教授、书籍）。文章中有一些对欧洲女性性观念的刻板描述（'换男人如换衣服'、'战场早就百孔千疮'），但整体目的是讨论人口统计学问题，而非攻击某个特定群体。"
        ],
        "encoding_analysis": [
            "不存在编码机制。全文是论述/分析文体，直接使用学术讨论式的语言。引用了'朗金斯'的话但明确表态'说不清楚'，没有使用任何谐音、隐喻、拆字或平台黑话来传输隐含意义。"
        ],
        "context_analysis": [
            "话题标记为gender_discussion，文本确实涉及性别相关讨论（对中国/欧洲女性生育行为的描述），但文本的主线是人口危机分析而非性别攻击。'欧洲女人从11岁开始过性生活，换男人如换衣服'这一描述带有性别刻板印象，但主要用于论证生育率低的原因，而非攻击欧洲女性。"
        ],
        "supporting_evidence": [
            "文本包含对中国女性的负面描述（通过引用'朗金斯说中国女人那么丑'）和对欧洲女性性观念的刻板印象（'换男人如换衣服'）",
            "'战场早就百孔千疮'使用了战争比喻来描述女性的性生活，具有贬低意味"
        ],
        "counter_evidence": [
            "文本主体是人口危机的学术分析，引用了多位学者和统计数据",
            "作者明确表示'中国女人丑不丑我说不清楚'，未赞同引用的攻击性言论",
            "对欧洲女性的刻板描述是作为生育率低的论证素材出现，不是攻击的主要目标",
            "整体文本基调是担忧全球人口危机的分析性讨论，而非仇恨言论",
            "文本主要讨论的是人口、生育率、移民、老龄化等宏观社会问题"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本虽然包含对中国和欧洲女性的刻板描述，但主体是人口危机的分析讨论，不属于仇恨攻击，是话题敏感的困难负样本。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=gender; toxic=1; expr=1; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002627
# ──────────────────────────────────────────────
samples.append({
    "id': '002627",
    "source_type': 'real",
    "text': '他不是江南人，绝对不是，江南人讲话口吻脾气秉性不是这样的。他是明显的假冒魔都人有种现象很有趣，就是低温人假冒京人某些人假冒魔都人尤其这些年，去魔都的人各地都有，比之前杂多了，不少人，您比如假名媛吧，某些柴火妞就是中专没毕业到魔都钓个老头过两月出门就说自己魔都人😅我真不相信他是上海人",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_reporting"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'low",
    "evidence_strength': 'moderate",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "文本讨论上海人的身份认同问题。作者声称某人不是江南人（长江以南地区，特指上海/江浙），然后举例说有一些人假冒上海人：'低温人假冒京人'（BTW: '低温人'可能是'低端人'的误写或代称，指低学历/低收入的人）假冒北京人，也有人假冒上海人。作者用'假名媛'（fake socialites）和'柴火妞'（农村土姑娘）来描写那些冒充上海人的人群，说她们中专没毕业到上海'钓个老头'（傍大款）后就说自己是上海人。",
            "文本包含地域歧视（对非上海人的贬低）和阶级歧视（对低学历人群的嘲弄），但整体是观察/分析式的描述。"
        ],
        "encoding_analysis": [
            "不存在编码机制。'假名媛'、'柴火妞'、'钓个老头'都是中文中直接使用的口语词，没有经过编码包装。'低温人'可能是'低端人'的输入错误或替代说法，但不构成明确的编码。文本直接陈述了作者对外来人口冒充上海本地人的不满。"
        ],
        "context_analysis": [
            "文本是对一个具体人物的身份真伪的判断（'他不是江南人'），随后展开了对外地人'假冒上海人'这一社会现象的评论。话题标签为region_reporting，符合文本内容——作者在描述和评论一种社会现象：外地人冒充本地人。但文本中也带有对外来人口的负面态度。"
        ],
        "supporting_evidence": [
            "'柴火妞就是中专没毕业到魔都钓个老头过两月出门就说自己魔都人'——对低学历外来女性带有轻蔑的描写",
            "'低温人假冒京人'/'去魔都的人各地都有，比之前杂多了'——表达了对人口流动造成'纯度'下降的不满"
        ],
        "counter_evidence": [
            "文本的主要目的是判断一个人的地域身份（他不是江南人），并讨论假冒身份的社会现象，而非直接攻击某个群体",
            "'低温人'含义不明确，可能影响风险判断",
            "话题标签为region_reporting，表明是报告/分析型文本",
            "😅表情有缓和语气的作用，使批评显得更加调侃性质"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本涉及地域身份讨论，包含对外来人口的轻蔑描述，但主要目的是社会现象分析，仇恨攻击意图不明确，属于话题敏感的困难负样本。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=1; expr=3; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002628
# ──────────────────────────────────────────────
samples.append({
    "id': '002628",
    "source_type': 'real",
    "text': '分享一个我的故事和一个事故我和同桌说，我是gay，然后他一脸怀疑，问我是不是真的，我说是真的，然后他一脸惊讶第二天，他用嫌弃的眼神看着我第三天，他一看我就猥琐发笑",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'lgbt_reporting"},
    "risk_level': 'none",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "作者分享了一个个人经历：向同桌出柜（说自己是gay），同桌从怀疑→惊讶→嫌弃→猥琐发笑的过程。这是一段个人叙事，描述了作者亲历的恐同反应。作者没有使用任何攻击性语言，恰恰相反，作者是遭受了歧视（同桌的'嫌弃眼神'和'猥琐发笑'）。",
            "文本中的'事故'是双关——既指一件不愉快的事，也谐音'故事'。这是一个真实的个人经历分享，属于lgbt_reporting（LGBT相关报告）类别。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本是直白的个人叙事，'gay'是英文词汇但已是中文中的通用语，不是编码。所有描述都是直接的：'一脸怀疑'、'嫌弃的眼神'、'猥琐发笑'都是标准的描述用语。"
        ],
        "context_analysis": [
            "在知乎的LGBT话题下，这是典型的出柜经历分享。作者通过叙述同桌的反应（嫌弃→猥琐发笑），向读者展示了校园中隐性恐同的形式。这是第一人称回忆体，作者本人是经历者而非攻击者。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的非有毒标注（toxic=0），文本本身没有攻击性词汇",
            "作者是出柜故事的讲述者，故事中的'嫌弃'和'猥琐发笑'是他人对作者的行为，而非作者对他人",
            "文本是一个个人经历分享，不包含任何对他人或群体的攻击"
        ],
        "counter_evidence": [
            "文本中出现了'猥琐发笑'这个对他人行为的描述，虽然是在描述作者受歧视的经历，但'猥琐'一词本身带有贬义。不过这种使用方式（描述他人对自己的不善行为）是合理的。"
        ],
        "final_rationale': 'Risk: none (hard_negative)。文本是个人出柜经历的叙事，作者是受歧视的一方而非攻击者，没有任何攻击性内容，属于与LGBT话题相关的困难负样本。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=lgbt; toxic=0; expr=3; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002629
# ──────────────────────────────────────────────
samples.append({
    "id': '002629",
    "source_type': 'real",
    "text': '自己同胞遇害感到愤怒难道不应该吗，真就什么人看什么事？😓",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'none",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'medium",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "作者问'自己同胞遇害感到愤怒难道不应该吗'——这是一个反问句，认为对同胞被害感到愤怒是理所当然的。'真就什么人看什么事？'是在批评那些对不同的事件（或不同受害者）持双重标准的人。从内容上看，这似乎是某件涉及中国公民遇害事件的评论区回应。",
            "文本没有对任何群体进行攻击，而是表达了一种民族情感（对'同胞'遇害的愤怒）。话题标签为race_discussion，可能'同胞'在此与种族/国籍有关。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本使用直接语言（'同胞遇害'、'愤怒'），没有任何谐音、隐喻、拆字或平台黑话。'同胞'是中文中对同国籍/同种族人的正式称呼。"
        ],
        "context_analysis": [
            "需要更多上下文来确定'同胞遇害'指的是什么具体事件。可能是在某起涉及中国公民（可能被外国人所害）的刑事案件下，有人质疑评论区'过分愤怒'，作者反驳这种质疑。文本本身不包含攻击性内容。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的非有毒标注（toxic=0），文本本身没有攻击性词汇",
            "作者在表达正当的民族情感——对同胞遇害感到愤怒，没有攻击任何其他群体",
            "'真就什么人看什么事？'是在批评双重标准，而非传播仇恨"
        ],
        "counter_evidence": [
            "如果'同胞遇害'事件涉及跨种族冲突（比如中国公民被外籍人员杀害），那么文本的'愤怒'可能隐含排外情绪。但这是对具体事件的反应，而非对群体的抽象攻击。缺乏具体事件信息。"
        ],
        "final_rationale': 'Risk: none (hard_negative)。文本表达对同胞遇害的愤怒，不包含对任何群体的攻击性，属于话题敏感的困难负样本。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=race; toxic=0; expr=0; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002630
# ──────────────────────────────────────────────
samples.append({
    "id': '002630",
    "source_type': 'real",
    "text': '我一东北人从来不黑安徽反而同情。不过你们的富邻居们肯定要黑的。毕竟和东北一个地位，不压榨一下怎么行。",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_discussion"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'moderate",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者自述是东北人，说自己'从来不黑安徽反而同情'——建立了一个不歧视安徽的人设。然后说'你们的富邻居们肯定要黑的'——这里的'富邻居'指经济发达地区（如江浙沪等），暗示富裕地区会歧视/压榨发展水平较低的地区。'毕竟和东北一个地位，不压榨一下怎么行'——将安徽和东北都定位为被歧视/被压榨的地区。",
            "这是对地域歧视现象（富裕地区歧视欠发达地区）的观察/评论，作者站在同情被歧视方的立场。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本使用直接语言，'黑'（抹黑/歧视）是互联网通用词。'富邻居'是比喻性表达（用'邻居'指代邻近省份），但这是常见修辞而非编码。"
        ],
        "context_analysis": [
            "文本出现在知乎的地域话题讨论中，最可能是在讨论安徽/东北被地域黑的现象。作者的观点是有趣的——作为'被黑的东北人'来同情'同样被黑的安徽人'，并指出共同的'欺凌者'是经济发达地区。这是对地域歧视社会动力学（谁歧视谁、为什么歧视）的分析。"
        ],
        "supporting_evidence": [
            "文本中出现了'黑安徽'和'不压榨一下怎么行'等涉及地域歧视的表述",
            "将安徽与东北并列为'被压榨'的对象，将富裕地区描述为'压榨者'"
        ],
        "counter_evidence": [
            "作者明确表达了对安徽的同情而非攻击立场",
            "'黑'是描述地域歧视行为的通用词，不是作者在实施歧视",
            "整体立场是反歧视/分析的（报告型表达，expression=3）",
            "文本是对地域歧视社会结构的观察，而非传播歧视"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本从被歧视方（东北人）的视角分析地域歧视的结构，对安徽表达同情而非攻击，属于地域话题的困难负样本。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=1; expr=3; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002631
# ──────────────────────────────────────────────
samples.append({
    "id': '002631",
    "source_type': 'real",
    "text': '关键是这男的他爸还支持？",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'none",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'high",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "一句话：'关键是这男的他爸还支持？'——表达了对某个'男的'的父亲竟然表示支持的惊讶/质疑。'支持'什么、'这男'是谁、他爸是谁完全没有上下文。文本只有9个字，信息量极低。",
            "在race_discussion的话题标签下，这可能是在评论一个跨种族关系/婚姻的话题——'这男'可能指与外国女性/黑人女性交往的中国男性，'他爸还支持'表示惊讶。但完全无法确认。"
        ],
        "encoding_analysis": [
            "不存在编码机制。这句话是纯粹的字面日常表达，没有任何谐音、拆字、隐喻、反讽或平台黑话。"
        ],
        "context_analysis": [
            "文本极短且信息密度极低，必须依赖上下文才能有任何判断。没有对话上下文，无法确定'这男'指代谁、'支持'什么内容。目前在race_discussion的话题下，最可能的解读是涉及跨种族关系的讨论。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的非有毒标注（toxic=0），文本本身没有任何攻击性词汇或编码",
            "'支持'是中性词，无贬义"
        ],
        "counter_evidence": [
            "文本太短，缺乏完整的句子结构，无法确定语境和含义。不能仅凭话题标签就判定其风险。"
        ],
        "final_rationale': 'Risk: none (hard_negative)。文本仅有9个字，表达对某事'被支持'的惊讶，没有任何攻击性词汇或编码机制，是完全的困难负样本。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=race; toxic=0; expr=0; reviewed_by=claude; chunk=000"
})
# ──────────────────────────────────────────────
# 002632
# ──────────────────────────────────────────────
samples.append({
    "id': '002632",
    "source_type': 'real",
    "text': '广西不也被黑得很惨吗",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_reporting"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'low",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "'广西不也被黑得很惨吗'——这是一个反问/陈述句，意思是'广西也被黑（地域歧视）得很惨'。作者在列举广西作为地域歧视的受害者之一。'被黑'在中文互联网语言中是'被抹黑/被歧视'的常用说法。",
            "文本没有任何攻击性，只是陈述一个观察（广西是被地域黑的对象）。说话者显然是将广西视为被歧视方而非歧视方。"
        ],
        "encoding_analysis": [
            "不存在编码机制。'被黑'中的'黑'是中文互联网中对'抹黑/歧视'的标准用语，完全无需编码解密。整句话是日常口语化的陈述。"
        ],
        "context_analysis": [
            "文本是对他人言论的补充/附和——在讨论哪些地区被地域黑时，作者补充说'广西不也被黑得很惨吗'。话题标签为region_reporting，属于报告型表达。缺少之前的对话上下文，但单句已足够判断方向。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的有毒标注（toxic=1），但文本本身不直接攻击任何人",
            "作者是在列举被地域黑的地区，而非参与地域黑"
        ],
        "counter_evidence": [
            "文本虽然本身不包含攻击，但'被黑得很惨'的表述涉及地域歧视话题，可能被模型认为在传播'广西被黑'的认知。不过这种信息传递属于客观描述而非攻击。"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本陈述'广西被黑得很惨'这一观察，属于对地域歧视现象的报告/评论，不包含攻击性内容。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=1; expr=3; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002633
# ──────────────────────────────────────────────
samples.append({
    "id': '002633",
    "source_type': 'real",
    "text': '我都不会说，我是河南的，在东北也依然遇到过地域歧视。我邀请同学到我家做客，然后她妈不同意，因为是河南的啊，可是她说她妈并没有认识的河南人。到最后来了，感觉我们这边感觉还不错。还有一次是跟朋友吃饭，刚认识的一个人说他在二七那边看到有人偷井盖，无语了，我那么多年天天去二七也没看到过咋让他碰上了。幸好这还算个别的，不过我对这鄙视链也是。。。",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_reporting"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'moderate",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "一段个人经历分享，作者是河南人，在东北生活时遭遇地域歧视。两个具体事例：1）邀请同学做客，同学的母亲因'河南的'而不同意，但实际上该母亲从未认识过河南人（说明歧视是基于刻板印象而非经验）；2）饭局上有人声称在二七（郑州地名）看到人偷井盖——这是经典的'河南人偷井盖'刻板印象，作者反驳说自己在二七多年从未见过。",
            "文本是典型的反地域歧视叙事——作者作为被歧视者讲述亲身经历，用自己的经验证伪刻板印象。结尾'我对这鄙视链也是。。。'表达了对这种歧视链文化的无奈。"
        ],
        "encoding_analysis": [
            "不存在编码机制。全文是直白的个人叙事，使用日常口语，没有任何编码。'偷井盖'是已广为人知的地域歧视梗，但在文本中是作为被引用的、被反驳的刻板印象出现的，不是作者在传播。"
        ],
        "context_analysis": [
            "在知乎的地域歧视话题下，这种个人经历分享很常见。作者列举两个实例来证明河南人受到的歧视是不公平的（基于虚空假设和刻板印象）。结尾'鄙视链'指出了地域歧视的结构性问题。"
        ],
        "supporting_evidence": [
            "作者在用自己的亲身经历反驳地域歧视，而不是在传播歧视",
            "'她妈并没有认识的河南人'——用朋友母亲的矛盾行为揭示歧视的非理性",
            "'我那么多年天天去二七也没看到过'——用个人经验直接反驳偷井盖刻板印象",
            "结尾'我对这鄙视链也是。。。'表达了对歧视文化的不满和无奈"
        ],
        "counter_evidence": [
            "文本中重复了'偷井盖'这一歧视性刻板印象（即使是在反驳的语境中），模型可能仅因关键词匹配而误判为传播偏见。但阅读全文可知是在反驳。"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本是河南人讲述遭遇地域歧视的个人经历，用实例反驳刻板印象，属于反偏见立场的报告/叙事，无攻击性内容。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=1; expr=3; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002634
# ──────────────────────────────────────────────
samples.append({
    "id': '002634",
    "source_type': 'real",
    "text': '就感觉结婚事太多了所以我以后要和男生过",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'gender_discussion"},
    "risk_level': 'none",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "'就感觉结婚事太多了所以我以后要和男生过'——作者表达因为觉得结婚太麻烦，所以打算以后和男生一起生活。这是一种个人生活选择/性取向的表达——作者可能是在说自己是同性恋，所以选择与男性伴侣生活。",
            "文本没有任何攻击性。作者是在表达个人倾向，没有对任何群体进行贬低或攻击。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本是日常口语化的个人表达，不存在任何编码。'和男生过'（与男性一起生活/与男性伴侣建立关系）是直白的表述。"
        ],
        "context_analysis": [
            "话题标签为gender_discussion，但文本中作者只是表达个人观点（结婚太麻烦→未来和男生一起生活），没有参与任何性别对抗性讨论。可能是在回应一个关于'结婚vs单身'或'同性恋'的帖子。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的非有毒标注（toxic=0），文本不包含攻击性词汇",
            "作者在表达个人生活选择，没有攻击或贬低任何人",
            "'结婚事太多了'是对婚姻制度的一般性抱怨，属于常见表达"
        ],
        "counter_evidence": [
            "文本可能被误解为对异性婚姻的贬低或对传统家庭价值观的否定，但这种解读过度延伸，缺乏文本证据。"
        ],
        "final_rationale': 'Risk: none (hard_negative)。文本是个人生活选择的表达（因婚姻繁琐选择同性伴侣生活），不包含任何攻击性内容，是性别话题的困难负样本。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=gender; toxic=0; expr=0; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002635
# ──────────────────────────────────────────────
samples.append({
    "id': '002635",
    "source_type': 'real",
    "text': '怎么回事反同恋吧被同性恋占领了。真的不知道说什么好。神淋看了都要哭。等着被吸吧",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'lgbt_discussion"},
    "risk_level': 'medium",
    "encoding_primary': 'A1_普通谐音",
    "encoding_secondary': ['E1_平台黑话"],
    "needs_context": False,
    "ambiguity': 'medium",
    "evidence_strength': 'moderate",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者说'反同恋吧'（一个反对同性恋的贴吧）被同性恋者'占领'了，然后说'神淋看了都要哭'和'等着被吸吧'。'反同恋吧'是一个以反同性恋立场为特色的贴吧社区，这里作者在抱怨该贴吧的内容被同性恋者/支持同性恋的帖子淹没。",
            "'神淋'是一个编码词——可能是'神（经病）'+'淋（病）'的谐音组合，或是某个特定社区人物的代称。'等着被吸吧'中的'吸'有性暗示意味（在男同性恋语境中常指口交）。"
        ],
        "encoding_analysis": [
            "'神淋'可能是A1类谐音编码——发音上接近某个人物或特定称呼。在贴吧LGBT社区中，'淋'可能源自'淋病'（性病）或是某个网络人物（如'淋语'文化中的'淋'——源自台湾歌手蔡依林的粉丝文化中'淋'的特殊用法）。'等着被吸吧'中的'吸'是同性恋文化黑话中的性行为代称（E1平台黑话）。"
        ],
        "context_analysis": [
            "在'反同恋吧'（一个反同贴吧）的语境下，该评论作者可能本身是反同立场，抱怨该吧被'同性恋'渗透。'等着被吸吧'可解读为对同性恋者的威胁或嘲弄。但整体表达的语调是困惑/调侃而非纯粹的仇恨攻击。"
        ],
        "supporting_evidence": [
            "'反同恋吧被同性恋占领了'——对LGBT群体出现在特定空间的敌意反应",
            "'等着被吸吧'——使用带有性暗示意味的表达，在反同语境中具有攻击性",
            "话题为lgbt_discussion，涉及对同性恋社区的负面表达"
        ],
        "counter_evidence": [
            "'神淋看了都要哭'可能是纯粹的玩梗（来源不明），整体语气可能是指向调侃而非恶毒攻击",
            "文本的语调更接近调侃/幽默而非仇恨，'怎么回事'和'真的不知道说什么好'传递的是困惑而非愤怒",
            "'占领'是一个被泛化使用的网络词，不一定有严重的排他含义"
        ],
        "final_rationale': 'Risk: medium。文本在反同贴吧语境中抱怨'被同性恋占领'并用性暗示用语'等着被吸吧'表达敌意，但语气偏调侃，风险为中等。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=lgbt; toxic=1; expr=2; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002636
# ──────────────────────────────────────────────
samples.append({
    "id': '002636",
    "source_type': 'real",
    "text': '我也想知道现在如何了",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'none",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'high",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "'我也想知道现在如何了'——作者想知道某件事/某人的最新状况。这句话完全中性，没有包含任何情感倾向或立场。在所有50个样本中这是最中性的表达之一。"
        ],
        "encoding_analysis": [
            "不存在编码机制。6个字的标准中文表达，没有任何编码或修饰。"
        ],
        "context_analysis": [
            "话题标签为race_discussion，但文本本身没有任何种族相关内容。最可能的是在某个讨论种族话题的帖子下等待更新或进展。独立性不足以做出任何风险判断。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的非有毒标注（toxic=0），文本没有任何攻击性词汇或风险相关信息",
            "全句由6个完全中性的汉字组成"
        ],
        "counter_evidence": [
            "无——文本完全中性，没有任何证据表明存在风险。"
        ],
        "final_rationale': 'Risk: none (hard_negative)。6字中性表达，不包含任何攻击性或风险信息，是最基础的困难负样本。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=race; toxic=0; expr=0; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002637
# ──────────────────────────────────────────────
samples.append({
    "id': '002637",
    "source_type': 'real",
    "text': '每年，山东得挤出3万个大学名额来支援中西部，分给河南的名额有几千个。东部中部每年好像给河南5万来个名额。山东每8个高考生就得被刷下来一个。",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_discussion"},
    "risk_level': 'none",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "作者讨论高考招生名额分配问题：山东每年需要'挤出'3万个大学名额分配给中西部地区，其中河南分到几千个。结果导致山东每8个高考生中就有1个因名额被调出而落榜。这段文字是在讨论中国高等教育资源分配的地区间不平衡问题。",
            "这是典型的政策讨论/数据分析文本，不带攻击性。作者在陈述一个关于高考名额跨省调配的统计事实（虽然数据准确性存疑），但整体是中性报告。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本使用数据报告式的客观语言，没有任何编码。'挤出'是拟人化的政策描述，但不是编码。"
        ],
        "context_analysis": [
            "在知乎的地域讨论话题下，这是一篇关于高考招生指标分配的评论。涉及省份间的资源分配矛盾（山东的资源被调走），但讨论的是政策层面的问题，而非对某个省份的歧视。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的非有毒标注（toxic=0），文本不包含攻击性内容",
            "文本是事实陈述式的政策讨论，使用数据支持论点"
        ],
        "counter_evidence": [
            "文本隐含了'被刷下来'（因名额调出而落榜）的不满，可能被解读为对中西部省份享有的招生倾斜政策的抱怨，但缺乏明显的攻击性。"
        ],
        "final_rationale': 'Risk: none (hard_negative)。文本是关于高考名额跨省调配的政策讨论，使用数据报告风格，不包含攻击性或歧视性内容。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=0; expr=0; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002638
# ──────────────────────────────────────────────
samples.append({
    "id': '002638",
    "source_type': 'real",
    "text': '为啥在网上在这帮男人眼里好像全国女生都喜欢黑人一样这句话是错的。仅此而已。",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_reporting"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'moderate",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者说'为啥在网上在这帮男人眼里好像全国女生都喜欢黑人一样这句话是错的'——这是一个条件句，完整解读是：'（有人说）\\\"为什么在网上在这些男人眼里好像全国女生都喜欢黑人一样\\\"，这句话是错的。'作者认为'并非全国女生都喜欢黑人'——这是在驳斥一个刻板印象。",
            "'这句话是错的。仅此而已。'——作者简洁地指出某个观点的错误，没有进一步的攻击或贬低。文本被标记为race_reporting，符合报告/反偏见的特征。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本是直接的明确陈述，没有编码。'黑人'是标准的中文种族称呼，在此不是作为攻击性词汇出现（是在引用/驳斥刻板印象）。"
        ],
        "context_analysis": [
            "在种族报告话题下，作者在驳斥一个常见的刻板印象——'全国女生都喜欢黑人'。这个刻板印象本身在中文互联网上经常出现（通常是反跨种族交往的言论的一部分），而作者明确指出这个说法是错误的。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的有毒标注（toxic=1），但实际文本是反刻板印象的",
            "'这句话是错的。仅此而已。'——明确表达否定立场，简洁有力",
            "讨论的是对刻板印象的驳斥，属于反偏见/报告型表达"
        ],
        "counter_evidence": [
            "文本中出现了'黑人'这一种族关键词，并且在引用一个负面刻板印象（全国女生都喜欢黑人——暗含贬义）。虽然作者是在反驳，但复述刻板印象本身可能被模型误判。"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本是对'全国女生都喜欢黑人'这一刻板印象的明确反驳，属于反偏见报告型表达，不构成种族攻击。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=race; toxic=1; expr=3; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002639
# ──────────────────────────────────────────────
samples.append({
    "id': '002639",
    "source_type': 'real",
    "text': '这些对东北人搞地域歧视的人其实很蠢，早晚搬起石头砸自己脚。",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_reporting"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'moderate",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者批评那些对东北人进行地域歧视的人——说他们'很蠢'，并且预言这种歧视行为最终会'搬起石头砸自己脚'（自食恶果）。文本的立场是明确的反对地域歧视。",
            "'很蠢'是负面评价，但针对的是歧视行为本身（对东北人搞地域歧视），而非针对某个地域群体。这是对施害者的批评，而非对受害者的攻击。"
        ],
        "encoding_analysis": [
            "不存在编码机制。'搬起石头砸自己脚'是中文成语，属于标准修辞而非编码。"蠢"是直接评价。没使用任何谐音、拆字、隐喻等编码。"
        ],
        "context_analysis": [
            "在region_reporting话题下，作者站在反对地域歧视的立场，批评那些地域黑的人。文本清晰的因果逻辑：地域歧视行为是愚蠢的，且最终会对歧视者自身不利。"
        ],
        "supporting_evidence": [
            "明确批评地域歧视行为（'对东北人搞地域歧视'），立场清晰",
            "'早晚搬起石头砸自己脚'——对歧视行为的负面后果的预言",
            "属于反偏见/报告型表达"
        ],
        "counter_evidence": [
            "'很蠢'是负面评价词，可能被模型认为具有攻击性。但这里攻击的对象是'歧视行为'而非任何特定群体，属于正当批评。"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本明确站在反地域歧视立场，批评歧视者，不属于攻击性内容而是反偏见表达。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=1; expr=3; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002640
# ──────────────────────────────────────────────
samples.append({
    "id': '002640",
    "source_type': 'real",
    "text': '安徽主要是在上海被歧视",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_reporting"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'low",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "'安徽主要是在上海被歧视'——作者陈述一个观察：安徽人在上海受到的地域歧视最严重。文本是一个简洁的地域歧视现象观察，没有包含任何攻击性内容。作者指出了上海对安徽人群体的歧视现象，但自己并未参与歧视。",
            "文本是典型的报告型表达——陈述一个社会现象，无主观攻击。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本是直白的社会现象陈述，没有任何编码。"
        ],
        "context_analysis": [
            "在知乎的地域歧视报告话题下，这可能是对'哪些省份/地区被歧视'类问题的回答。作者指出安徽人在上海受到的歧视最为显著。"
        ],
        "supporting_evidence": [
            "文本陈述的是安徽人在上海被歧视的社会现象，属于报告型表达",
            "'安徽主要是在上海被歧视'——没有攻击性词汇，是客观陈述的语气"
        ],
        "counter_evidence": [
            "文本重复了'安徽被歧视'的说法，但只是作为社会事实陈述，不属于传播歧视。"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本简短陈述安徽在上海受歧视的社会现象，属于报告型表达，无攻击性。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=1; expr=3; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002641
# ──────────────────────────────────────────────
samples.append({
    "id': '002641",
    "source_type': 'real",
    "text': '这个up，他上传了两个稿件一个是图一，两男性互殴，弹幕都是玩玩梗的。第二个是图二，是俩女性打架，结果弹幕出现了很多姐姐好飒，小仙女互殴这类的扩大化弹幕。（扩大化大家应该都不陌生，我们没少被仙女扩大化过，一有男性个人劣迹就上升整个群体。）扩大化当然是不好的，而且不理智，不正确的。只能说这是当初仙女们扩大化的反噬，这让b站年轻群体都感觉到了危机，进行反抗。",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'gender_discussion"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary': ['E1_平台黑话"],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'moderate",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者分析B站（Bilibili）弹幕中的双重标准现象：两个男性打架的弹幕是玩梗性质的，而两个女性打架的弹幕则出现'姐姐好飒'（好帅气）和'小仙女互殴'（仙女在打架/小仙女是反讽称呼）。作者指出这是'扩大化'（将个体行为上升为群体特征）的现象。接着作者承认男性也经常被'仙女'（女性群体）扩大化——'一有男性个人劣迹就上升整个群体'。最后作者总结说'这是当初仙女们扩大化的反噬'——男性群体正在反击。",
            "文本是一个关于网络暴力/双重标准的分析，使用了'仙女'（指代女性群体，带反讽）和'反噬'等术语，整体是分析性文字但带有一定的性别对抗色彩。"
        ],
        "encoding_analysis": [
            "不存在主要的编码机制。'小仙女'是E1类平台黑话——在中文互联网中原本是褒义（漂亮女孩），但在性别对抗语境中已经变成对女性/女权主义者的反讽称呼。'扩大化'是社会学用语的直接使用。文本整体是分析/报告性的。"
        ],
        "context_analysis": [
            "在贴吧的性别讨论话题下，作者在做一个关于'弹幕双重标准'的观察分析。作者承认两性都曾遭受'扩大化'，认为男性现在的反应是对女性之前行为的'反噬'。虽然用了反讽称呼'仙女'，但整体分析保持了相对平衡的视角。"
        ],
        "supporting_evidence": [
            "文本中出现了'小仙女互殴'这一对女性打架事件的调侃标签",
            "'仙女们扩大化的反噬'——将男性群体的反击描述为对女性行为的反应",
            "'让b站年轻群体都感觉到了危机，进行反抗'——将男性群体的反应描述为正当反抗"
        ],
        "counter_evidence": [
            "作者明确说'扩大化当然是不好的，而且不理智，不正确的'——否定了扩大化行为本身",
            "作者承认男性也'没少被仙女扩大化过'——承认双方的情况",
            "文本主体是对网络现象的分析/观察，不是直接攻击",
            "'小仙女'虽然有反讽意味但攻击性较弱"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本是对B站弹幕双重标准的分析，虽使用反讽称法'小仙女'但整体是报告/分析型表达，攻击性弱。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=gender; toxic=1; expr=2; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002642
# ──────────────────────────────────────────────
samples.append({
    "id': '002642",
    "source_type': 'real",
    "text': '男權社會：會出現很多優待女人的行為，甚至女性特權女權社會：只會一味女性特權，打壓男性",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'gender_reporting"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'moderate",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "对比两种社会结构：'男权社会'（男性主导的社会）中会出现优待女性的行为甚至女性特权；而'女权社会'（女性主导的社会）只会一味追求女性特权并打压男性。文本构建了一个不对称对比：男权社会实际上优待女性，女权社会却压迫男性。",
            "使用繁体字（男權、會、體）——可能来自港台或习惯使用繁体的用户。文本是对两性关系的一种政治观点表达，将男权社会描述为'好的'（实际上给女性特权），将女权社会描述为'坏的'（打压男性）。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本使用直接的政治分析语言，繁体字不是编码（只是书写习惯）。'男权社会'、'女权社会'、'女性特权'、'打壓'都是标准术语，没有经过编码包装。"
        ],
        "context_analysis": [
            "在性别报告话题下，作者表达了一种常见的反女权观点：认为男权社会反而给了女性更多利益/特权，而女权社会则是对男性的压迫。这种观点在中文互联网的性别话题中很常见，属于政治观点陈述而非仇恨攻击。"
        ],
        "supporting_evidence": [
            "文本涉及性别议题讨论，对'女权社会'的描述呈负面",
            "'只会一味女性特権，打圧男性'——将女权社会简单化为'打压男性'"
        ],
        "counter_evidence": [
            "文本是对两种社会结构的对比分析，属于政治/社会评论",
            "没有使用侮辱性词汇或攻击性语言（没有'婊'、'狗'等贬称）",
            "话题标签为gender_reporting，本身就是报告型"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本是对男权/女权社会的对比分析，虽持反女权立场但使用标准术语而非侮辱性语言，属于政治观点讨论。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=gender; toxic=1; expr=3; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002643
# ──────────────────────────────────────────────
samples.append({
    "id': '002643",
    "source_type': 'real",
    "text': '这种地方，要么就是发达的城市，被外来打工的吐槽，要么就是不太发达的好多都出去打工可能素质不太高",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_discussion"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'medium",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "作者在讨论一种关于地域刻板印象的模式：'这种地方'要么是发达城市，被外来打工者吐槽；要么是欠发达地区，外出打工的人可能'素质不太高'。文本是对一种常见的地域评价模式的描述——人们倾向于批评/看不起与自己不同的地区。",
            "'素质不太高'是中国网络用语中对人或地区的一种常见的委婉批评，指向教育水平/行为规范。这里作者是在描述一种刻板印象的模式，而非自己做出这样的评价。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本是口语化的社会观察，任何词汇都没有经过编码包装。"
        ],
        "context_analysis": [
            "需要更多上下文来确定'这种地方'的指代对象。从句式判断，作者可能在总结一种规律或回应他人的批评。话题为region_discussion，但文本本身更像是元评论（关于地域评价模式的分析）。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的非有毒标注（toxic=0），文本作为社会观察不包含直接攻击",
            "'素质不太高'虽然是一个带有阶级/地域偏见的用词，但这里是在描述一种刻板印象模式而非直接攻击"
        ],
        "counter_evidence": [
            "'素质不太高'是中文互联网中用于批评欠发达地区/农村人口的常见词汇，带有一定的阶层偏见。即使是在描述模式，使用这个词汇本身也反映了作者的预设。"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本是对地域刻板印象模式的社会观察，虽使用了'素质不太高'这带有偏见的词汇，但整体是描述性而非攻击性。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=0; expr=0; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002644
# ──────────────────────────────────────────────
samples.append({
    "id': '002644",
    "source_type': 'real",
    "text': '八国洋人在天津消灭了九成天津人，天津貌似没有被毁灭啊",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_discussion"},
    "risk_level': 'none",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'medium",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "作者引用了一个历史数据/说法——'八国洋人（八国联军）在天津消灭了九成天津人'，然后指出一个矛盾：'天津貌似没有被毁灭啊'。作者是在质疑这个历史说法或讨论历史记忆的选择性。",
            "文本不包含对任何群体的攻击，只是在讨论历史记忆问题。话题标签为region_discussion，可能是在讨论不同地区在历史叙述中的地位。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本是历史讨论的直接表述，没有任何编码。"
        ],
        "context_analysis": [
            "需要上下文来确定作者为什么在region_discussion话题下讨论八国联军在天津的历史。可能是在回应关于'为什么某些地区被记住而其他被忽略'的讨论。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的非有毒标注（toxic=0），文本没有任何攻击性",
            "文本是历史事实的讨论"
        ],
        "counter_evidence": [
            "'八国洋人'对'八国联军'的称呼可能被解读为对洋人的贬称（'洋人'在历史语境中有贬义），但这属于历史术语的沿用。"
        ],
        "final_rationale': 'Risk: none (hard_negative)。文本是关于天津历史（八国联军相关）的事实讨论，不包含攻击性或歧视性内容。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=0; expr=0; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002645
# ──────────────────────────────────────────────
samples.append({
    "id': '002645",
    "source_type': 'real",
    "text': '幕刃瘠薄又逮着\"理\"了",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'gender_discussion"},
    "risk_level': 'high",
    "encoding_primary': 'B1_拆字",
    "encoding_secondary': ['A1_普通谐音"],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'strong",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "'幕刃瘠薄又逮着\\\"理\\\"了'——这是一条使用编码的性别攻击。'幕刃'是一个已知的拆字编码，通过在字形上操作来指向一个强烈的女性侮辱词（女字旁+表音部分）。'瘠薄'是'鸡巴'（男性生殖器，用作粗口）的谐音替代。'又逮着\\\"理\\\"了'是反讽——说女性/女权主义者又自以为'有道理'了。",
            "全句是一个高度敌视女性的表达，使用了多层编码来规避审查。"
        ],
        "encoding_analysis": [
            "'幕刃'是B1类拆字编码——通过对目标侮辱词的字形分析，提取其组成部分（'幕'处理为目标字的上半部分或其他部件变体），组合成一个看起来无害但内行能解码的词。'瘠薄'是A1类谐音编码——'瘠薄'（jí bó）的发音接近'鸡巴'（jī ba，男性生殖器的粗口），用来替代脏话。整体属于F类组合编码。"
        ],
        "context_analysis": [
            "在贴吧的性别讨论话题下，这是典型的'反女拳'（anti-feminist）贴吧文化的产物。'幕刃'在贴吧中已经成为一个相对固化的女性贬称编码。'瘠薄'进一步强化了攻击的语言强度。整句在嘲讽某个女性的言论（'逮着理了'）。"
        ],
        "supporting_evidence": [
            "'幕刃'是贴吧文化中针对女性的已知拆字编码，属于B1类字形编码",
            "'瘠薄'通过A1谐音的方式替换'鸡巴'脏话，强化攻击性",
            "'又逮着\\\"理\\\"了'使用引号括住'理'字，表达反讽（不是真有道理而是自以为有道理）",
            "整体语境是性别讨论，攻击目标明确为女性/女权主义者"
        ],
        "counter_evidence": [
            "'幕刃'的具体字形编码还原路径在缺乏贴吧内部知识的情况下可能不唯一。但结合上下文和已知的贴吧黑话使用习惯，目标指向已经明确。"
        ],
        "final_rationale': 'Risk: high。文本使用B1拆字编码（'幕刃'指向女性侮辱词）和A1谐音（'瘠薄'替代脏话），构成对女性的明确仇恨攻击，属于高隐蔽性组合编码。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=gender; toxic=1; expr=1; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002646
# ──────────────────────────────────────────────
samples.append({
    "id': '002646",
    "source_type': 'real",
    "text': '请大家大声说出来如果吴亦凡是国际鬼子虫类及其它们后代虫混说不定国际鬼子虫类及其它们后代虫混亲儿子республиканскоеправительство的判罚又是另当别论可见宁波案件会被国际鬼子虫类及其它们后代虫混亲儿子республиканскоеправительство一定压的永远压的石沉大海",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'high",
    "encoding_primary': 'D2_隐喻",
    "encoding_secondary': ['A4_外语谐音/跨语言音译"],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'strong",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者讨论吴亦凡案与另一个案件（宁波案件）的差异，核心论点：如果是'国际鬼子虫类及其后代虫混'（对外国人和混血人群的贬称），判罚结果会不同。使用了俄语'республиканскоеправительство'（共和政府/共和国政府）。",
            "文本使用了多层次的侮辱性代称：'鬼子'（历史贬称，指外国侵略者）、'虫类'（将人比作虫子，非人化）、'虫混'（虫子的混血，攻击混血人群）。攻击目标明确为外国人/混血人群/特定种族。"
        ],
        "encoding_analysis": [
            "主要编码是D2类隐喻——'虫类'将目标人类非人化为虫子，是最恶劣的侮辱方式之一；'虫混'是'虫类+混血'的复合贬称。'鬼子'可视为C4类符号借用（历史符号的现代表达）。俄语'республиканскоеправительство'是A4类跨语言音译/外语使用。整体呈现F类组合编码特征，多层编码叠加。"
        ],
        "context_analysis": [
            "在贴吧种族话题下，作者通过对比吴亦凡案（加拿大籍华人）和宁波案件，表达了对'外国人和混血人群受优待'的不满。'宁波案件'可能指某起涉及外国人的案件。俄语的使用在中文贴吧语境中可能是为了混淆审查或增加语气强度。"
        ],
        "supporting_evidence": [
            "'鬼子'是对外国人的历史贬称，在现代语境中仍然具有强烈的排外意味",
            "'虫类'和'虫混'使用D2隐喻将人群非人化为虫类，是最极端的群体攻击",
            "俄语'республиканскоеправительство'的插入（A4编码）暗示'外国政府'或'共和国政府'的不公正",
            "'一定压的永远压的石沉大海'——断言司法不公，基于种族身份而非事实"
        ],
        "counter_evidence": [
            "俄语'республиканскоеправительство'的意思在中俄文混合语境中可能被误解。但结合上下文，其主要作用是强化对外国政府/势力的批评。"
        ],
        "final_rationale': 'Risk: high。文本使用D2隐喻（虫类非人化）、C4符号借用（鬼子）和A4外语编码多层组合，对外国人和混血人群进行极端仇恨攻击。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=race; toxic=1; expr=1; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002647
# ──────────────────────────────────────────────
samples.append({
    "id': '002647",
    "source_type': 'real",
    "text': '我评论中有提到关于男性或者女性的字眼吗？😄😄",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'lgbt_discussion"},
    "risk_level': 'none",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'high",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "作者反问：'我评论中有提到关于男性或者女性的字眼吗？'——这是在为自己辩护，否认自己的评论涉及性别/性取向话题。两个😄表情表明语气轻松/调侃。",
            "文本没有包含任何攻击性内容。作者在回应某种被批评的情况，辩解自己的评论不含性别/性取向内容。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本是直接的自我辩护式反问，没有任何编码。"
        ],
        "context_analysis": [
            "在LGBT话题讨论语境中，这意味着作者的某个话被批评为涉及性取向问题，作者反驳说自己的原话中没有提到男性或女性。需要之前对话的上下文来理解作者在反驳什么。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的非有毒标注（toxic=0），文本没有任何攻击性",
            "作者在申辩自己的原话不涉及性别/性取向内容"
        ],
        "counter_evidence": [
            "无风险证据。完全中性的自我辩护。"
        ],
        "final_rationale': 'Risk: none (hard_negative)。文本是自我辩护式的反问——否认自己的评论涉及性别内容，完全不包含攻击性。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=lgbt; toxic=0; expr=0; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002648
# ──────────────────────────────────────────────
samples.append({
    "id': '002648",
    "source_type': 'real",
    "text': '别在这自艾自怜了，我都不理解你怎么会有这种想法，人是否被人瞧得起是自己说了算的，我二十岁从黑龙江出来 走南闯北现在二十年了，我从来没觉得有人瞧不起我，行得正坐得直，气场杠杠滴，在哪老子都不是配角儿，谁敢瞧不起我。 只要人品正直，不做让人那把柄的事儿，不吹牛不装逼。天王老子也不怕！😎",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_discussion"},
    "risk_level': 'none",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'low",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "作者在鼓励某人不要自艾自怜（自怨自艾），主张人的尊严由自己决定。作者以自身经历为例——20岁从黑龙江出来走南闯北20年，从未感觉被人瞧不起。核心论点是'行得正坐得直，气场杠杠滴'——人品好、行事正直就不会被看不起。",
            "文本是典型的励志/鼓励型评论。虽然涉及黑龙江/东北的地域背景，但作者是在表达积极的人生态度，而非参与地域讨论。'不吹牛不装逼'中的'装逼'是口语化表达但不是攻击。"
        ],
        "encoding_analysis": [
            "不存在编码机制。全文是直白的励志口语表达，没有任何编码。'行得正坐得直'是成语。'老子'是自称（非攻击性）。'天王老子也不怕'是夸张表达。"
        ],
        "context_analysis": [
            "在region_discussion话题下，可能是有人抱怨因是东北人/黑龙江人而遭受歧视，作者回应说'人是否被人瞧得起是自己说了算的'——这是对某人的鼓励而非对地域歧视的讨论。作者自身的东北背景（黑龙江）是在以身说法。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的非有毒标注（toxic=0），文本不包含任何攻击性",
            "文本是励志型鼓励，主张个人尊严由自己决定"
        ],
        "counter_evidence": [
            "'不吹牛不装逼'中的'装逼'是口语化粗话，可能被模型敏感词触发。但这里是在批评一种行为（吹牛装逼）而非攻击任何人。"
        ],
        "final_rationale': 'Risk: none (hard_negative)。文本是鼓励型评论，作者以自身经历鼓励他人不要自怨自艾，主张个人尊严自主决定，无攻击性内容。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=0; expr=0; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002649
# ──────────────────────────────────────────────
samples.append({
    "id': '002649",
    "source_type': 'real",
    "text': '击毙我，你得到一具遗体！满足我，你可以去眼馋异教徒韩男！",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'gender_discussion"},
    "risk_level': 'medium",
    "encoding_primary': 'D4_双关",
    "encoding_secondary': ['E1_平台黑话"],
    "needs_context": True,
    "ambiguity': 'high",
    "evidence_strength': 'weak",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "'击毙我，你得到一具遗体！满足我，你可以去眼馋异教徒韩男！'——这读起来像是一段游戏台词、角色扮演对话或网络梗。字面上是一个条件交换：杀了我你只得到一具尸体；满足我（可能指性需求），你可以去羡慕那些'异教徒韩男'（Korean men）。",
            "'异教徒韩男'将韩国男性标记为'异教徒'（infidels），可能源于某些网络社区中的宗教/民族对立话语。文本高度抽象，含义不明确。"
        ],
        "encoding_analysis": [
            "D4双关——句子可以有多重解读：1）字面上的'击毙/满足'条件交换；2）性暗示（'满足我'）；3）关于韩男的评论。'异教徒韩男'可能是特定社区（如反韩/韩流相关贴吧）中的E1平台黑话——在某些社区中'韩男'已经成为一个带有贬义的代称。整体表达带有反讽/夸张的修辞特征。"
        ],
        "context_analysis": [
            "文本高度抽象，看起来更像是特定社区的内部梗或角色扮演对话。在性别讨论话题下，'满足我'有性暗示色彩，'韩男'指向韩国男性。可能需要更多的社区知识或上下文才能准确解码其含义。"
        ],
        "supporting_evidence": [
            "'异教徒韩男'可能将韩国男性标记为负面对象（异教徒=宗教上的他者）",
            "'满足我，你可以去眼馋'有一定的性暗示和物化色彩",
            "话题标签为gender_discussion，表明与性别对抗相关"
        ],
        "counter_evidence": [
            "文本可能是某个游戏/影视作品中的台词引用或角色扮演，不具有实际攻击意图",
            "对话逻辑不完整，读起来更像是一种戏谑而非严肃的攻击",
            "'异教徒'一词可能是特定社区内部的隐喻说法，不指实际的宗教"
        ],
        "final_rationale': 'Risk: medium。文本高度抽象模糊，使用D4双关和可能的平台黑话，指向性别/种族（韩男）话题，但因证据不足且可能是角色扮演，风险为中等。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=gender; toxic=1; expr=2; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002650
# ──────────────────────────────────────────────
samples.append({
    "id': '002650",
    "source_type': 'real",
    "text': '个性签名亮了:向韩国人学习😓",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'none",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'medium",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "作者评论某人的个性签名——'向韩国人学习'——说这个签名'亮了'（有趣/犀利/引人注目）。😓表情表示无语或尴尬。文本是对某人个性签名的一句简短评论，不包含直接攻击。",
            "在race_discussion话题下，'向韩国人学习'的签名可能带有讽刺意味（指向中韩之间的文化/政治议题），但作者仅评论了签名本身而没有发表自己的观点。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本是直接的简短评论，没有任何编码。"
        ],
        "context_analysis": [
            "需要确定'向韩国人学习'的签名在什么语境下被当作'亮了'。可能是一个涉及中韩比较的讨论中，某人设置了这样的签名。作者仅评论了签名的趣味性，没有表达自己的立场。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的非有毒标注（toxic=0），文本不包含攻击性",
            "作者仅评论他人签名，没有发表自己的政治/种族观点"
        ],
        "counter_evidence": [
            "'向韩国人学习'的签名可能带有政治讽刺意味，但作者没有参与讽刺，仅评论签名本身。"
        ],
        "final_rationale': 'Risk: none (hard_negative)。文本仅评论他人个性签名'亮了'，不包含任何攻击性内容或明确的立场表达。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=race; toxic=0; expr=0; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002651
# ──────────────────────────────────────────────
samples.append({
    "id': '002651",
    "source_type': 'real",
    "text': '不结婚。但喜欢跟黑人做。😅😅",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'high",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者声明个人偏好：'不结婚。但喜欢跟黑人做。'——表明不打算结婚但喜欢与黑人发生性关系。😅😅表情表明这是一种尴尬/自嘲的语气。",
            "文本本身不包含攻击性。作者在表达个人的性偏好和婚恋态度，不涉及对他人的贬低或攻击。话题标签为race_discussion，但作者的立场是个人偏好声明而非种族讨论。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本使用直接的语言表达个人偏好，没有任何编码。'黑人'是标准种族称呼，在此不是作为攻击性词汇出现。"
        ],
        "context_analysis": [
            "在种族话题讨论语境中，这可能是某人在回应'中国女孩是否喜欢黑人'之类的问题时给出个人答案。作者选择了不结婚但与黑人发生性关系，这只是一个个人选择，不涉及价值判断或攻击。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的有毒标注（toxic=1），但文本实际不包含攻击性",
            "作者在表达个人偏好，没有对任何群体进行贬低或攻击",
            "'不结婚。但喜欢跟黑人做。😅😅'——自嘲语气，没有仇恨色彩"
        ],
        "counter_evidence": [
            "文本涉及种族话题（'黑人'）和性话题，可能被模型认为在强化'中国女性与黑人性行为'的刻板印象。但作者是在陈述个人事实而非传播刻板印象。"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本是个人性偏好的陈述，不包含对任何群体或个人的攻击，属于话题敏感的困难负样本。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=race; toxic=1; expr=2; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002652
# ──────────────────────────────────────────────
samples.append({
    "id': '002652",
    "source_type': 'real",
    "text': '地域黑比较典型的几个，按大区域东北被黑，按省河南被黑，二线城市武汉被黑，一线城市广州被黑🤣",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_reporting"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'moderate",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者列举地域歧视的典型受害者：东北（跨大区域）、河南（按省级）、武汉（二线城市）、广州（一线城市）。🤣表情表明这是一种调侃/哭笑不得的语气。",
            "文本是对地域歧视现象的归纳总结，属于报告/分析型表达。作者只是在列举哪些地方经常被'黑'，没有自己参与地域攻击。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本是直白的社会现象列举，没有任何编码。"
        ],
        "context_analysis": [
            "在region_reporting话题下，这是典型的观察归纳型表达。作者在回答'哪些地方被黑得最严重'之类的问题，列举了各个层面的典型。🤣表情表明作者在以一种无奈的幽默态度讨论这个现象。"
        ],
        "supporting_evidence": [
            "文本是对地域歧视现象的类型归纳，属于报告型",
            "'被黑'中的'黑'是标准互联网用语，指抹黑/歧视，作者在描述现象而非参与攻击",
            "'按大区域'、'按省'、'二线城市'、'一线城市'——系统的分类结构表明是分析性语言"
        ],
        "counter_evidence": [
            "列举具体的受害地名可能被认为是在强化'这些地方被黑'的认知，但作为社会现象描述，这属于客观归纳。"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本系统列举地域歧视受害者（东北、河南、武汉、广州），属于报告/分析型表达，无攻击性。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=1; expr=3; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002653
# ──────────────────────────────────────────────
samples.append({
    "id': '002653",
    "source_type': 'real",
    "text': '只有大果的姥爷喜欢黑，送银子送穴都要跪求黑来，至于为什么呢，那就不好说了",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'high",
    "encoding_primary': 'C4_典故/物品/符号借用",
    "encoding_secondary': ['A1_普通谐音"],
    "needs_context": False,
    "ambiguity': 'medium",
    "evidence_strength': 'strong",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "文本声称某个国家/势力的大人物（'大果的姥爷'）喜欢'黑'（黑人/黑人群体），不惜'送银子送穴'（送钱送资源）来'跪求黑来'。最后'至于为什么呢，那就不好说了'——暗示有不方便明说的原因。",
            "'大果'很可能是'大国/大国的'的谐音或隐喻。'姥爷'是'老爷/大人物/高层'的谐音或替代。'黑'在此指向黑人/黑人群体/黑色人种。'送银子送穴'——银子是钱/资金，'穴'可能是'血'（资源/生命）的谐音或'洞穴/位置'（利益/地位）。全段在批评某个大国政府向黑人群体提供资源和利益。"
        ],
        "encoding_analysis": [
            "'大果的姥爷'是C4类符号借用——'姥爷'（grandfather/old master）代指高层领导人或决策者，是历史典故式的符号用法。'黑'是典型的C4符号——'黑色/黑人'作为代指。'穴'可能是A1类谐音——'穴'（xué）发音接近'血'（xuè），'送穴'即'送血'（付出生命代价/输送资源）。整体是一段使用多层编码的种族/政治暗讽。"
        ],
        "context_analysis": [
            "在贴吧种族话题下，这极大概率的'大果'是指美国或某个大国的政府。'姥爷'指代该国领导人。全段在批评该国的移民/种族政策（吸引黑人移民）。'送银子送穴'指提供福利和资源。'那就不好说了'是典型的'懂的都懂'表达——暗示原因不便明说（可能指某种政治正确或选举需要）。"
        ],
        "supporting_evidence": [
            "'大果的姥爷'使用C4编码——'姥爷'代指高层人物，'大果'代指大国",
            "'喜欢黑'中的'黑'明确指向黑人群体/黑色人种",
            "'送银子送穴都要跪求黑来'——抱怨资源被用于吸引黑人群体的政策",
            "'至于为什么呢，那就不好说了'——典型的加密表达，暗示不便明说的原因"
        ],
        "counter_evidence": [
            "'大果的姥爷'的编码还原路径有多重可能性（可能指某个具体历史人物或时事），不能100%确定指向谁。但'喜欢黑'和'送银子送穴'的种族指向已经足够明确。"
        ],
        "final_rationale': 'Risk: high。文本使用C4编码（'姥爷'代指高层、'黑'代指黑人群体）和A1谐音（'穴'），批评政府向黑人群体输送资源，是种族歧视言论。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=race; toxic=1; expr=2; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002654
# ──────────────────────────────────────────────
samples.append({
    "id': '002654",
    "source_type': 'real",
    "text': '不予置评……不过你问我的话我可能给你输出racial discrimination观念。（虽然并未接触过默）",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "作者说'不予置评'（不做评论），但随即说'不过你问我的话我可能给你输出racial discrimination观念'（如果你问我的话我可能会给你输出种族歧视的观点）。接着在括号中承认'虽然并未接触过默'——虽然从未接触过黑人/与黑人无直接接触。",
            "'默'是对'黑人/黑'的替代字（默→黑，黑色的暗指）。作者在坦诚自己可能持有基于二手信息的种族歧视观点，因为自己从未实际接触过黑人。这是一种相对诚实和自省式的表达——作者在承认自己的偏见来源于不了解而非真实经验。"
        ],
        "encoding_analysis": [
            "文本主要使用直接语言（literal_keyword），'racial discrimination'是英文词但不是编码。'默'是C4类符号借用——用'默'（沉默/黑暗）替代'黑'来指代黑人群体，可能是为了避免直接使用'黑'字。这种替代是中文网络上一种常见的规避写法。"
        ],
        "context_analysis": [
            "在知乎的种族话题下，作者在以一种相对诚实的方式表达自己的种族观点储备。'（虽然并未接触过默）'这一括号自白表明作者对自己偏见的来源有一定反思——从未接触过黑人但可能输出种族歧视观点。这更像是对偏见的自我分析而非攻击。"
        ],
        "supporting_evidence": [
            "'可能给你输出racial discrimination观念'——作者承认自己可能持有种族歧视观点",
            "'并未接触过默'——使用'默'替代'黑'指代黑人"
        ],
        "counter_evidence": [
            "作者没有实际输出种族歧视内容，而只是假设在自己的语境中可能这样做",
            "'不予置评'起了缓冲作用——作者首先表示不愿评论",
            "'虽然并未接触过默'——作者在为自己的可能偏见提供解释（不是基于真实经验）",
            "整体更像是对偏见的自我审视而非实施攻击"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本是自我审视式的种族观点声明，使用'默'替代'黑'但未实际输出歧视内容，属于话题敏感的困难负样本。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=race; toxic=1; expr=1; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002655
# ──────────────────────────────────────────────
samples.append({
    "id': '002655",
    "source_type': 'real",
    "text': '其实上边的吧友们都真正地理解自己反对的是什么。就是反对自己后代的基因被染黑。",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'high",
    "encoding_primary': 'D2_隐喻",
    "encoding_secondary': ['literal_keyword"],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'strong",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者声称回复中（上边的吧友们）真正理解自己在反对什么——即'反对自己后代的基因被染黑'。'基因被染黑'是一个种族主义生物学隐喻——指后代有黑人血统/与黑人通婚。全句在表达反对跨种族（特别是黑-中）通婚的立场，并用'基因被染黑'来渲染这种反对的'合理性'。",
            "'染黑'是一个被动语态的负面表述——后代不想'被染黑'，意味着黑人是污染源。这是典型的种族主义生物学话语。"
        ],
        "encoding_analysis": [
            "主要编码是D2类隐喻——'基因被染黑'将跨种族生育比作基因污染/'染色'过程。'染'（dye/stain）本身带有污损的语义，'染黑'意味着清白被破坏。这是种族主义话语中最经典的'血统纯洁性'隐喻。文本也有literal_keyword部分（直白的关于后代的表述）。"
        ],
        "context_analysis": [
            "在贴吧种族话题讨论中，这是在回应一个关于跨种族关系/通婚的帖子。'上边的吧友们'指之前的回帖者。作者将之前的反对跨种族通婚的立场总结为'反对基因被染黑'——用种族纯洁论来为种族隔离立场辩护。"
        ],
        "supporting_evidence": [
            "'后代的基因被染黑'使用D2隐喻——基因被比作可被污染/染色的物质，"染黑'暗示'白色/纯洁'→'变黑/被污染"的种族主义生物学叙事",
            "'染黑'的被动语态表明跨种族婚恋被视为一种外在侵害/污染",
            "全文在强化种族纯洁性的观念，是经典的种族隔离/排斥论调"
        ],
        "counter_evidence": [
            "作者可能是在转述/总结其他吧友的观点而非表达自己的立场。但'其实上边的吧友们都真正地理解自己反对的是什么'这句表明作者认同并支持这种观点。"
        ],
        "final_rationale': 'Risk: high。文本使用D2隐喻（'基因被染黑'=基因污染）表达反对跨种族通婚的种族纯洁论立场，是明确的种族仇恨言论。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=race; toxic=1; expr=1; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002656
# ──────────────────────────────────────────────
samples.append({
    "id': '002656",
    "source_type': 'real",
    "text': '当面问清楚，不能接受有孩子就说清楚立刻分了，越快越好，迟则生变，抱着玩玩的心态我认为不可以啊",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'gender_reporting"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'low",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "作者在给出关系建议：当面问清楚（对方是否能接受有孩子），如果不能接受就立刻分手，越快越好。并批评'抱着玩玩的心态'（只贪图玩乐的心态）。",
            "文本是典型的婚恋建议类型，不涉及攻击任何人。'不能接受有孩子'可能指某一方有孩子或是否想要孩子的问题。整体是中性的情感建议。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本是直白的情感建议，使用日常口语，没有任何编码。"
        ],
        "context_analysis": [
            "话题标签为gender_reporting，但文本更偏向个人情感咨询而非性别议题讨论。可能在某个情感类帖子下给出建议。需要上下文确定'有孩子'的具体语境。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的有毒标注（toxic=1），但文本实际上是中性的婚恋建议",
            "没有攻击性词汇或编码机制"
        ],
        "counter_evidence": [
            "文本建议在对方'不能接受有孩子'时'立刻分了'，可能被认为是在鼓励对'不带孩子'的伴侣的排斥，但这属于个人价值判断而非攻击。"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本是婚恋关系建议（关于孩子接受问题的沟通和分手建议），不包含攻击性内容。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=gender; toxic=1; expr=3; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002657
# ──────────────────────────────────────────────
samples.append({
    "id': '002657",
    "source_type': 'real",
    "text': '希望他们嫁给默以后都去非洲吧，不要待在国内，看着觉得蛮恶心的，跑爹默竟然也有人中国女人愿意嫁也不配当中国人",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'race_discussion"},
    "risk_level': 'high",
    "encoding_primary': 'C4_典故/物品/符号借用",
    "encoding_secondary': ['literal_keyword"],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'strong",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者希望那些嫁给'默'（黑人）的中国女性'都去非洲吧'，不要待在国内——因为'看着觉得蛮恶心的'。然后攻击那些中国女性说'也不配当中国人'。",
            "'默'是'黑/黑人'的规避代称——用意义相近的'默'（黑暗/沉默/暗）替代'黑'（黑色/黑人）。全文是种族和性别双重攻击：攻击嫁给黑人的中国女性（不配当中国人），攻击黑人（'跑爹默'——'跑爹'可能指'跑掉的老爹'或某种侮辱代称）。"
        ],
        "encoding_analysis": [
            "'默'是C4类符号借用——用'默'替代'黑'代指黑人群体。'跑爹默'是一个复合词，'爹'在此可能指代男性/父亲，'跑爹默'整体是对黑人的贬称。'恶心'、'不配当中国人'是直接的攻击性语言（literal_keyword）。"
        ],
        "context_analysis": [
            "在知乎的种族话题下，这是典型的种族隔离+民族主义立场表达。核心主张：1）与黑人结婚的中国女性应被驱逐出中国；2）这种行为令人恶心；3）这些女性不应被视为中国人。是对跨种族婚恋的最极端反动之一。"
        ],
        "supporting_evidence": [
            "'希望他们嫁给默以后都去非洲吧'——明确主张将嫁给黑人的中国女性驱逐出境",
            "'看着觉得蛮恶心的'——用'恶心'表达对这种跨种族关系的生理性排斥和厌恶",
            "'跑爹默'——对黑人的侮辱性称呼（C4编码+复合词）",
            "'也不配当中国人'——对嫁给黑人的中国女性的'中国身份'的剥夺，民族主义+种族的双重排斥"
        ],
        "counter_evidence": [
            "'默'作为'黑'的代称也可能被不了解编码的人误读。但结合'去非洲'和'恶心'的上下文，指向已经极为明确。"
        ],
        "final_rationale': 'Risk: high。文本使用C4编码（'默'代指黑人）和直接攻击语言，主张驱逐嫁给黑人的中国女性并剥夺其中国人身份，是种族+性别双重仇恨言论。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=race; toxic=1; expr=1; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002658
# ──────────────────────────────────────────────
samples.append({
    "id': '002658",
    "source_type': 'real",
    "text': '最好的防守就是进攻，在被利用前利用她们，不要贪恋美色，多了不好",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'gender_discussion"},
    "risk_level': 'medium",
    "encoding_primary': 'literal_keyword",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'medium",
    "evidence_strength': 'moderate",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者主张对女性采用先发制人的策略：'最好的防守就是进攻，在被利用前利用她们'。这是一种将异性关系视为零和博弈/竞争的思维——认为女性会利用男性，因此男性应该先利用女性。'不要贪恋美色，多了不好'——克制对美貌的迷恋，因为过多会带来负面影响。",
            "文本将女性定位为潜在的'利用者'，主张男性采取对抗性策略。这种性别对抗思维在贴吧的性别话题中很常见，包含对女性的工具化态度（'利用她们'）。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本是直白的人际策略建议，没有任何编码。'美色'是标准中文词汇（指女性美貌/性魅力），在此没有经过编码。"
        ],
        "context_analysis": [
            "在贴吧性别讨论话题下，这最可能是男性社区中的'两性博弈'讨论的一部分。'在被利用前利用她们'的预设是'女性会利用男性'，这种互不信任的性别对抗叙事在贴吧的某些亚文化中很常见。文本将女性客体化（'利用她们'），具有性别歧视色彩。"
        ],
        "supporting_evidence": [
            "'在被利用前利用她们'——以性别对抗为前提的策略建议，将女性预设为潜在的利用者",
            "'不要贪恋美色'——'美色'将女性的吸引力物化为需要克制的诱惑",
            "在贴吧性别话题下，这种叙事模式常见于男权/反女权话语"
        ],
        "counter_evidence": [
            "文本可以被解读为一种一般的社交/心理策略建议（应对所有人而非特指女性），'她们'可能指某个特定类型的群体而非全体女性",
            "缺乏上下文来确定'她们'的具体指代"
        ],
        "final_rationale': 'Risk: medium。文本使用'在被利用前利用她们'的对抗性话语将女性定位为潜在利用者，具有性别歧视/客体化色彩，但攻击性中等。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=gender; toxic=1; expr=2; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002659
# ──────────────────────────────────────────────
samples.append({
    "id': '002659",
    "source_type': 'real",
    "text': '西方国家有规定，同居半年以上就是事实婚姻，但中国没有这项规定，然后一些来中国赚钱的白男就很喜欢找中国女的同居，女的怀孕后，他们就要求女的打掉，但让他们没有想到的是，女的不会打还会把事闹大，白男没办法跑回国，这就正中了小仙女的下怀，他们会追到白男的国家去，然后和当地大使馆说这个事，大使馆绝对会帮忙起诉，维护中国公民的权利，然后当地法院就只能案当地的法律判离婚案，小仙女就高高兴兴地拿钱回国。",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'gender_discussion"},
    "risk_level': 'medium",
    "encoding_primary': 'D1_反讽",
    "encoding_secondary': ['E1_平台黑话"],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'moderate",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者描述了一个模式：白人男性来中国赚钱，与中国女性同居（利用中国法律没有'事实婚姻'规定的漏洞），女性怀孕后被要求打掉，但女性拒绝并将事情闹大，白人男性逃回国后，女性追到其国家并通过大使馆起诉离婚，最终获得赔偿。作者使用'小仙女'（反讽称呼）来指代这些女性，将整个过程描述为女性的'算计'。",
            "文本的核心叙事是：白人男性试图'骗炮'但被中国女性反向利用。'小仙女'在这里是反讽用法（字面上仙女/女神，实际暗讽精于算计）。整体将跨种族关系描述为一种博弈/算计。"
        ],
        "encoding_analysis": [
            "'小仙女'是E1平台黑话——原本是褒义（美丽女性），但在贴吧/A岛等性别对抗语境中已变成对女性/女权主义者的反讽称呼。D1反讽——字面说'高高兴兴地拿钱回国'，好像在说女性赢了，但整体叙事暗含对这些女性的负面评价（心机/算计）。"
        ],
        "context_analysis": [
            "在贴吧性别讨论话题下，这是典型的'白男vs中国女性'的叙事模板。作者描述的是一种'精明女性反向利用外国男性'的模式，对白人男性和中国女性都持负面态度。文本中将白人男性描述为利用法律漏洞的骗子，将中国女性描述为精明的报复者。"
        ],
        "supporting_evidence": [
            "'小仙女'在贴吧语境中通常是对女性的反讽称呼（E1平台黑话）",
            "'正中了小仙女的下怀'——将女性的应对描述为蓄谋已久的算计",
            "将跨种族关系描述为'白人骗炮→女性反向利用→赚钱'的算计模式"
        ],
        "counter_evidence": [
            "文本描述的是一种具体的社会现象/个案模式，可能在转述某种报道或传闻",
            "对白男也没有正面评价（'来中国赚钱的白男'、'要求女的打掉'、'跑回国'），态度是多向批评而非单一种族歧视",
            "'小仙女'的贬义程度在贴吧文化中相对有限"
        ],
        "final_rationale': 'Risk: medium。文本使用反讽称呼'小仙女'（E1/D1）和博弈叙事模式描述跨种族关系中的算计，对中国女性和白人男性都持负面态度，风险中等。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=gender; toxic=1; expr=2; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002660
# ──────────────────────────────────────────────
samples.append({
    "id': '002660",
    "source_type': 'real",
    "text': '地域黑怎么也避免不了，我一个从小从苏南去东北生活的人说是哪儿的都不合适🥺，黑去呗。",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_reporting"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": False,
    "reasoning": {
        "literal_analysis": [
            "作者表达对地域黑现象的无奈：'怎么也避免不了'。作者自称从小从苏南（江苏南部）去东北生活，所以'说是哪儿的都不合适'——因为既不是纯粹的'苏南人'也不是'东北人'，陷入身份认同的尴尬。最后'黑去呗'表达了一种放弃/无所谓的态度。🥺表情传递了无奈。",
            "文本没有攻击性，而是一个人在地域歧视文化中的尴尬处境的自述。作者既不是歧视者也不是在传播歧视。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本是直白的个人经历叙述，没有任何编码。"
        ],
        "context_analysis": [
            "在region_reporting话题下，作者在分享个人在地域歧视环境中的身份认同困境——从苏南到东北的迁移使自己的地域身份变得模糊，无论被视为哪里人都会被另一面质疑。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的有毒标注（toxic=1），但实际是反地域歧视的个人叙述",
            "'地域黑怎么也避免不了'——表达对地域歧视现象的无奈",
            "'黑去呗'——放弃/无所谓的态度，不是传播歧视"
        ],
        "counter_evidence": [
            "文本重复了'地域黑'和'被黑'的表述，但这是作为社会现象来讨论，而非参与。"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本是跨地域生活者在地域歧视文化中的身份认同困境自述，无攻击性内容。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=1; expr=3; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002661
# ──────────────────────────────────────────────
samples.append({
    "id': '002661",
    "source_type': 'real",
    "text': '比起你为了生活到处传艾更好",
    "platform': 'tieba",
    "context': {'title": "", "description": "", "time": "", "topic': 'lgbt_discussion"},
    "risk_level': 'high",
    "encoding_primary': 'A2_拼音缩写",
    "encoding_secondary': ['D4_双关"],
    "needs_context": False,
    "ambiguity': 'low",
    "evidence_strength': 'strong",
    "hard_negative": False,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "'比起你为了生活到处传艾更好'——意思是'比起你为了生活到处传播艾滋病（更好）'或'比你的情况更好，你为了生活到处传播艾滋病'。'传艾'是'传播艾滋病'的简称（艾=艾滋）。这句话是在攻击某人，指控其为了生计而到处传播艾滋病。",
            "在lgbt_discussion（反同/LGBT讨论）话题下，'传艾'是针对同性恋者的经典攻击话术——将同性恋与艾滋病传播联系起来。"
        ],
        "encoding_analysis": [
            "'传艾'是A2类拼音缩写编码——'艾'是'艾滋'（AIDS）的缩写保留一个汉字。同时'传艾'也是D4类双关——'艾'的发音是ài，'传艾'发音与'传爱'（传递爱）相同。因此'传艾'可以同时解读为'传播艾滋病'和'传爱'（传递爱/传播爱），表面上是后者但实质是前者，构成双关。"
        ],
        "context_analysis": [
            "在贴吧LGBT话题下，这是极其常见的反同攻击话术。攻击者将同性恋者与艾滋病传播者等同，使用'传艾'这个缩写来降低直接攻击的露骨程度。'为了生活'暗示该人通过性行为谋生或频繁更换性伴侣。"
        ],
        "supporting_evidence": [
            "'传艾'是'传播艾滋病'的缩写（A2拼音缩写），直接指控某人传播AIDS",
            "在lgbt话题下，这种攻击话术明确指向同性恋者，利用HIV/AIDS污名化",
            "'为了生活'暗示攻击对象的性行为是有偿的/频繁的，进一步强化负面形象"
        ],
        "counter_evidence": [
            "'传艾'在极少数情况下可能指'传播艾草/艾灸'（中医养生相关），但在lgbt话题下这种解读可能性极低。"
        ],
        "final_rationale': 'Risk: high。文本使用A2编码'传艾'（传播艾滋病的缩写）攻击他人，在LGBT话题下利用AIDS污名化进行仇恨攻击。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=tieba; topic=lgbt; toxic=1; expr=2; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# 002662
# ──────────────────────────────────────────────
samples.append({
    "id': '002662",
    "source_type': 'real",
    "text': '是，最早就是河南，我还记得井盖和董存瑞。现在得加上东三省了。嗯嗯，估计明后年再回答这个问题的时候山东人会要求把他们也加上。",
    "platform': 'zhihu",
    "context': {'title": "", "description": "", "time": "", "topic': 'region_discussion"},
    "risk_level': 'low",
    "encoding_primary': 'none",
    "encoding_secondary": [],
    "needs_context": True,
    "ambiguity': 'low",
    "evidence_strength': 'weak",
    "hard_negative": True,
    "freshness': 'stable",
    "target_known": True,
    "reasoning": {
        "literal_analysis": [
            "作者回应一个关于地域歧视的问题。'最早就是河南'——最早被地域黑的是河南。'我还记得井盖和董存瑞'——这里的'井盖'是'河南人偷井盖'的经典刻板印象；'董存瑞'指河南某地的董存瑞雕像被损坏的争议事件。'现在得加上东三省了'——东北也加入了被地域黑的行列。最后预言山东人也可能'要求被加上'（被列入地域黑名单）。",
            "文本是对地域歧视现象的演变历史的总结，作者作为旁观者在描述哪些地区何时进入'被黑名单'。不包含攻击性内容。"
        ],
        "encoding_analysis": [
            "不存在编码机制。文本是直接的社会现象讨论，'井盖和董存瑞'是作为地域歧视标志性事件/梗的引用出现的，不是作者在传播歧视。"
        ],
        "context_analysis": [
            "在知乎的地域话题下，这是对'哪些地区被黑'类问题的回答。作者用时间线的方式列出：河南（最早）→东北→山东（预测）。'井盖和董存瑞'是对河南刻板印象的两个符号。作者的语气是客观观察式的，像是在盘点一种文化现象。"
        ],
        "supporting_evidence": [
            "该样本来自ToxiCN的非有毒标注（toxic=0），不包含直接攻击",
            "文本是对地域歧视现象演变的历史性总结",
            "'井盖和董存瑞'是作为被引用的刻板印象符号出现，不是作者原创攻击"
        ],
        "counter_evidence": [
            "文本中提到了'井盖'（河南人偷井盖的刻板印象），即使是在引用历史，仍然可能在模型中触发关键词匹配。",
            "作者对可能的'山东人也来要求被加上'的预测带有一丝调侃/幸灾乐祸"
        ],
        "final_rationale': 'Risk: low (hard_negative)。文本是对地域歧视对象演变的历史性总结，引用'井盖和董存瑞'作为标志梗但不参与传播歧视。"
    },
    "quality_status': 'reviewed",
    "review_notes': 'source=batch23_toxicn; platform=zhihu; topic=region; toxic=0; expr=0; reviewed_by=claude; chunk=000"
})

# ──────────────────────────────────────────────
# Write output
# ──────────────────────────────────────────────
import os
outdir = os.path.dirname(OUTPUT)
if outdir:
    os.makedirs(outdir, exist_ok=True)

with open(OUTPUT, "w', encoding='utf-8") as f:
    for s in samples:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")

print(f"Done. {len(samples)} samples written to {OUTPUT}")

# Write output
with open(OUTPUT, "w', encoding='utf-8") as f:
    for s in samples:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")

print(f"Done. File written to {OUTPUT}")
