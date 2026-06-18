#!/usr/bin/env python3
"""Complete manual review corrections for batch23 chunk_000 (50 samples)."""
import json

with open('data/raw/batch23_chunks/chunk_000.jsonl') as f:
    samples = [json.loads(line) for line in f]

# Helper to build reasoning
def R(literal, encoding, context, supporting, counter, final):
    return {
        "literal_analysis": literal,
        "encoding_analysis": encoding,
        "context_analysis": context,
        "supporting_evidence": supporting,
        "counter_evidence": counter,
        "final_rationale": final
    }

corrections = {}

# --- SAMPLE 002613 ---
corrections["002613"] = {
    "risk_level": "high", "encoding_primary": "literal_keyword", "encoding_secondary": ["E1_平台黑话"],
    "ambiguity": "low", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["文本用拼音'laji(垃圾)'直接辱骂，'艾滋里面什么人最多不用多说了吧'将同性恋与艾滋病恶意关联——这是反LGBTQ言论的经典污名化套路。",
         "结尾'散滨'是网络黑话，意为'散了吧/滚'，带有驱逐意图。"],
        ["'laji'是literal_keyword——直接用拼音写'垃圾'来绕开辱骂词检测，但没有经过谐音或隐喻包装。",
         "'散滨'是E1_平台黑话，在知乎/贴吧社区中固定用作驱逐语，字面意义为空。"],
        ["知乎反LGBTQ讨论语境。裸文本攻击意图明确，不依赖额外上下文。"],
        ["1.'laji(垃圾)'是直接辱骂词；2.'艾滋→同性恋'是污名化关联；3.'散滨'是驱逐意图；4.三步(辱骂→污名→驱逐)构成完整仇恨链条。"],
        ["1.'laji'用拼音写可能降低字面攻击性——但这属于规避策略不改变攻击本质；2.缺少对话上下文无法确定针对个人还是群体——但'同性恋'泛指表明是群体攻击。"],
        "Risk: high。直接辱骂(laji)+污名化(艾滋→同性恋)+驱逐语(散滨)，完整仇恨言论链。编码literal_keyword+E1。"
    )
}

# --- SAMPLE 002614 ---
corrections["002614"] = {
    "risk_level": "low", "encoding_primary": "D1_反讽", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["表面在质疑对方：'就读错个子'（读错一个字）你就'那么大意见'。然后用反问指出——正因为有人对小事上纲上线，才导致'那么多人黑河南'。",
         "叙述者实际在揭露地域歧视的形成机制：人们因小事放大成对整个地域的偏见。"],
        ["使用D1_反讽：表面上替对方说话('你想想为什么')，实际在批评'因为小事就黑整个地域'的行为逻辑。"],
        ["知乎地域歧视讨论语境。叙述者站在反偏见立场解释歧视成因，需要上下文确认'读错字'的具体事件。"],
        ["1.'就读错个子'暗示触发攻击的导火索极其微小；2.'你想想为什么那么多人黑河南'引导反思偏见形成；3.叙述立场是反偏见——解释歧视如何产生而非实施歧视。"],
        ["1.提及'那么多人黑河南'可能被误解为合理化地域黑；2.没有明确表达'不该黑河南'的立场。"],
        "Risk: low。反偏见立场揭露地域歧视形成机制，D1反讽批评因小事扩大化的行为逻辑。话题敏感但文本不具有攻击性。"
    )
}

# --- SAMPLE 002615 ---
corrections["002615"] = {
    "risk_level": "low", "encoding_primary": "A3_方言谐音", "encoding_secondary": ["E3_互动/热点触发"],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["文本回忆贴吧地域黑河南的起源，特别提到'捞翔'——将河南方言'老乡'用谐音丑化。叙述者是在复述/揭露这一现象，'我记得特清楚'表明回忆立场。"],
        ["'捞翔'是A3_方言谐音——利用河南方言'老乡'的发音，用近音字进行丑化，是地域歧视中的方言攻击手段。叙述者本身在reporting此编码而非使用它，次要编码E3。"],
        ["知乎讨论地域歧视起源的语境。叙述者立场是揭露和回忆，非传播歧视。"],
        ["1.'我记得特清楚'表明是回忆/揭露；2.用引号标注'捞翔'表明在引用他人用语；3.叙述语气是客观描述性的。"],
        ["1.直接提及了歧视性称呼'捞翔'的具体形式，客观上传播了这一称呼；2.没有明确表达对该歧视用语的批判态度。"],
        "Risk: low。揭露贴吧地域黑起源的reporting样本，引用了A3方言谐音('捞翔')但叙述立场为反偏见。"
    )
}

# --- SAMPLE 002616 ---
corrections["002616"] = {
    "risk_level": "medium", "encoding_primary": "E1_平台黑话", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["抱怨B站'圣母婊和政治正确一点也不少'。'圣母婊'是网络黑话，指被认为站在道德高地虚伪说教的人。将'政治正确'与'圣母婊'并列，表达对反歧视话语的不满。"],
        ["'圣母婊'是E1_平台黑话——在B站/贴吧/知乎固化为贬义词，攻击对象是主张包容/反歧视的人群。文本未经过谐音/隐喻等深层编码，是相对直接的抱怨。"],
        ["贴吧种族歧视讨论语境。通过批评'政治正确'来表达对反歧视话语的抵触——这是歧视言论常见的包装策略。"],
        ["1.'圣母婊'是带贬义的平台黑话，攻击反歧视人群；2.'政治正确'在此含负面色彩；3.结合topic=race_discussion，隐含对反种族歧视的抵触。"],
        ["1.文本只是表达对平台氛围不满，未直接攻击特定群体；2.'政治正确'的批评可以是普通内容质量讨论；3.缺少上下文无法确定具体话题。"],
        "Risk: medium。E1平台黑话'圣母婊'表达对反歧视话语的不满，间接包装的偏见表达，缺少直接群体攻击。"
    )
}

# --- SAMPLE 002617 ---
corrections["002617"] = {
    "risk_level": "medium", "encoding_primary": "D3_借代", "encoding_secondary": ["D2_隐喻"],
    "ambiguity": "medium", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["表面陈述'事实'：高校艾滋病高发，留学生多的学校艾滋病更高，引用免费发放测试纸为证。实际将'留学生'(暗指非洲留学生)与艾滋病直接关联——典型污名化。"],
        ["D3_借代：'留学生'在此语境下是非洲/黑人留学生的借代词——中文网络种族歧视中常用'留学生'避免直接提及种族。D2_隐喻：将偏见包装为'统计数据'，表面讨论公共卫生，深层传递种族主义刻板印象。"],
        ["知乎种族歧视讨论语境。引用B站视频为'证据'增加可信度——网络种族主义常见的'理性包装'策略。"],
        ["1.'留学生多→艾滋高'的因果陈述将特定群体与疾病恶意关联；2.只有非洲/黑人留学生在网络歧视中被如此密集地与艾滋病挂钩——'留学生'是种族借代词；3.引用外部'证据'包装偏见。"],
        ["1.字面上讨论公共卫生话题，未出现种族词汇；2.艾滋病在高校分布可能是真实公卫议题；3.'留学生'本身是中性词。"],
        "Risk: medium。D3借代('留学生'代指黑人)+D2隐喻(偏见包装为统计)传递种族歧视，隐蔽性强但指向明确。"
    )
}

# --- SAMPLE 002618 ---
corrections["002618"] = {
    "risk_level": "high", "encoding_primary": "E1_平台黑话", "encoding_secondary": ["D3_借代"],
    "ambiguity": "low", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["攻击男同群体，特别是'母零'(0号/受方且气质偏女性化)。声称他们'想当女人'但只学会'泼妇的刻薄'和'淫妇的放纵'——用性别侮辱词攻击LGBTQ。"],
        ["'母零'是E1_平台黑话——贴吧/男同社区中，'母'指气质偏女性化的男同，'零'指0号，合为贬称。D3_借代：用'泼妇''淫妇'等女性负面刻板印象借代攻击男同群体。"],
        ["贴吧反LGBTQ讨论。文本结构完整、论证链条清晰——带'分析'外衣的攻击比简单辱骂更具危害性。"],
        ["1.'母零'——对特定男同群体的贬称；2.'泼妇的刻薄''淫妇的放纵'——性别侮辱词攻击；3.全段'标签化→分析→结论'是完整仇恨论述。"],
        ["1.文本列举了女性正面特质('自信''包容''善良''温柔')，表面有平衡；2.包装在'观察分析'框架中未用直接辱骂词。"],
        "Risk: high。E1平台黑话'母零'+性别侮辱词系统性贬低LGBTQ群体，伪分析包装增加攻击杀伤力。"
    )
}

# --- SAMPLE 002619 ---
corrections["002619"] = {
    "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "high", "evidence_strength": "weak", "needs_context": True, "hard_negative": False,
    "target_known": False,
    "reasoning": R(
        ["文本警告：跟'她'走太近会在圈子里'社死'(社会性死亡)。极度简略，'她'的身份不明——可能是跨种族恋爱者、LGBTQ成员或普通争议人物。"],
        ["无编码机制。'社死'是正常网络流行语，不构成规避性或攻击性编码。风险完全取决于'她'指代什么。"],
        ["标记topic=race_discussion但文本本身无种族内容。风险完全依赖上下文——需要知道'她'是谁、为何会社死。"],
        ["1.如果topic=race_discussion准确，则'她'可能与跨种族关系有关，文本暗示排斥。"],
        ["1.文本无任何敏感维度词汇；2.'社死'是正常社交描述；3.无法判断'她'的身份和风险指向；4.完全可能是普通社交场景。"],
        "Risk: low。文本过于模糊无明确风险编码，'她'指代不明。需要完整上下文。标记needs_context=true。"
    )
}

# --- SAMPLE 002620 ---
corrections["002620"] = {
    "risk_level": "high", "encoding_primary": "D3_借代", "encoding_secondary": ["D2_隐喻"],
    "ambiguity": "low", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["引用某'默'(黑人)视频中的话后，进行种族主义评论：'没有自己的文化，怎么才能过得更好呢？当然是去吃别人碗里的'——将黑人描绘为文化掠夺者。"],
        ["'默'是D3_借代——中文网络社区对黑人的贬义简称。'吃别人碗里的'是D2_隐喻——将文化/资源争夺比喻为'吃饭'，暗示黑人是'夺食者'。"],
        ["知乎种族歧视讨论。引用黑人视频为'证据'来合理化后续种族主义评论——网络种族歧视常见策略。"],
        ["1.'默'——对黑人的贬义简称；2.'吃别人碗里的'——描绘为'夺食者'；3.'没有自己的文化'——否定整个种族群体的文化贡献；4.😆表情显示对攻击内容持愉悦态度。"],
        ["1.'默'可能是'沉默'简写或其他含义；2.文化讨论本身不一定等同种族攻击。"],
        "Risk: high。D3借代('默')+D2隐喻('吃别人碗里')种族攻击，否定黑人文化并描绘为掠夺者。"
    )
}

# --- SAMPLE 002621 ---
corrections["002621"] = {
    "risk_level": "high", "encoding_primary": "literal_keyword", "encoding_secondary": ["D3_借代"],
    "ambiguity": "low", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["长篇文本系统性地将非洲黑人男性描绘为：艾滋病携带者、利用中国女性排解寂寞、骗取居住权。同时将找非洲男友的中国女性描绘为'没人看上的'、因'情感生理需求'才找黑人。",
         "表面在'客观分析'，实际是完整的种族主义论述，包含大量刻板印象和污名化。"],
        ["主要为literal_keyword——文本直接使用'非洲人艾滋病携带者''骗p''染病'等攻击性表述，未经过复杂编码包装。部分使用D3_借代：'那些找非洲男朋友的女孩'借代攻击跨种族婚恋的女性。"],
        ["知乎种族歧视讨论。用长篇'理性分析'框架包装种族主义——比短辱骂更具传播力和说服力。"],
        ["1.系统性地将非洲男性与艾滋病、欺骗、利用关联；2.贬低跨种族婚恋女性为'没人看上眼的'；3.引用欧洲案例扩大攻击范围至中东移民；4.全文是完整种族主义论述。"],
        ["1.文本包含'批判是不存在的，做好防护措施就好'的表面让步；2.引用了欧洲案例试图增加客观性；3.某些公共卫生数据可能是真实的。"],
        "Risk: high。完整种族主义论述——系统性地将非洲黑人男性与疾病、欺骗关联，并贬低跨种族婚恋女性。literal_keyword为主，部分D3借代。"
    )
}

# --- SAMPLE 002622 ---
corrections["002622"] = {
    "risk_level": "high", "encoding_primary": "A1_普通谐音", "encoding_secondary": ["E1_平台黑话"],
    "ambiguity": "low", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["抱怨剑网3吧被'籹全尸'占领打拳。'籹全尸'是三个谐音替换字组合，还原后为'女拳师'——网络中对女性主义者的贬称。'打拳'是'女拳'的延伸，泛指女性主义言论。"],
        ["A1_普通谐音：'籹'(nǚ)→'女'，'全'(quán)→'拳'，'尸'(shī)→'师'——用三个同音/近音字替换，构成规避性谐音编码。次要编码E1_平台黑话：'打拳'在中文网络社区固化为对女性主义言论的贬义标签。"],
        ["贴吧性别攻击语境。吐槽游戏吧被性别议题占据——常见的反女性主义叙事。"],
        ["1.'籹全尸'是经过精心构造的三字谐音替换，规避意图明确；2.'打拳'是固化的反女性主义黑话；3.抱怨语气+哈哈哈哈铺垫→攻击。"],
        ["1.可能仅是抱怨游戏吧氛围变化而非针对女性群体本身；2.贴吧中'打拳'有时也用于自嘲或中性描述。"],
        "Risk: high。A1三字谐音('籹全尸'→'女拳师')+E1平台黑话('打拳')对女性主义者进行贬称攻击。"
    )
}

# --- SAMPLE 002623 ---
corrections["002623"] = {
    "risk_level": "high", "encoding_primary": "D3_借代", "encoding_secondary": ["literal_keyword"],
    "ambiguity": "low", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["用'虫类及其后代虫混'来指代黑人及混血群体——'虫'是典型去人性化(dehumanization)修辞，将目标群体贬低为低等生物。声称他们是'全球第二大贩毒运毒磕药大户'。"],
        ["'虫类''虫混'是D3_借代——用'昆虫'借代黑人群体，是极其恶意的去人性化修辞。'贩毒运毒磕药'是literal_keyword——直接使用犯罪标签攻击。"],
        ["贴吧种族歧视讨论。去人性化修辞是仇恨言论中最危险的策略之一——将目标非人化后，暴力变得更加'合理'。"],
        ["1.'虫类'——将黑人群体去人性化为昆虫；2.'虫混'——对混血群体的恶意标签；3.直接贴'贩毒运毒磕药'的犯罪标签；4.全句无任何编码包装，恶意直接。"],
        ["1.文本提到的贩毒数据可能引用真实统计——但不改变去人性化修辞的恶意本质；2.单一评论可能无法反映叙述者完整立场。"],
        "Risk: high。D3借代('虫类'去人性化)+literal_keyword(犯罪标签)的极端种族仇恨言论。"
    )
}

# --- SAMPLE 002624 ---
corrections["002624"] = {
    "risk_level": "medium", "encoding_primary": "E1_平台黑话", "encoding_secondary": ["D2_隐喻"],
    "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["声称'怎么样，人家也不会瞧得起国男的'——将跨种族婚恋中的中国男性描绘为被看不起的一方。'小心别接盘就可以了'——'接盘'是网络黑话，指接手别人用过的/有问题的对象。"],
        ["'接盘'是E1_平台黑话——在网络社区固化为'接手别人用过/抛弃的对象'的贬义。'瞧不起国男'是D2_隐喻——用跨种族婚恋来隐喻中国男性的'失败'。"],
        ["知乎种族歧视讨论。将跨种族婚恋框架为中国男性vs外国男性的零和博弈。"],
        ["1.'接盘'——将交往过黑人男性的女性贬低为'需要接盘的';2.'瞧不起国男'——制造中外男性对立；3.对女性的物化倾向。"],
        ["1.文本是个人观点的表达，没有直接辱骂；2.'接盘'在某些语境下已弱化为普通网络用语；3.缺少上下文了解讨论主题。"],
        "Risk: medium。E1黑话'接盘'+D2隐喻表达跨种族婚恋偏见，涉及物化女性和制造对立，但无直接辱骂。"
    )
}

# --- SAMPLE 002625 ---
corrections["002625"] = {
    "risk_level": "medium", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'可以找，但不要住在中国了'——极简文本，结合topic=race_discussion，暗示'找了黑人对象就不要住在中国'。这是一种排斥性表达但极度省略。"],
        ["无明确编码机制。文本过于简短，没有使用谐音/隐喻/借代等包装手段。风险来自隐含的排斥态度而非编码。"],
        ["知乎种族歧视讨论。裸文本过于简短，需要上下文确定'找'的对象(大概率指找黑人伴侣)和叙述者的具体立场。"],
        ["1.结合topic=race_discussion，'找'指向跨种族婚恋；2.'不要住在中国'是排斥性表达。"],
        ["1.文本极度简短，'找'的对象不明确——可能是找工作/找对象/找其他；2.'不要住在中国了'可能是其他原因的建议；3.没有种族相关词汇。"],
        "Risk: medium。极简排斥性表达，无编码但结合语境具有种族排斥含义。标记needs_context=true。"
    )
}

# --- SAMPLE 002626 ---
corrections["002626"] = {
    "risk_level": "medium", "encoding_primary": "D2_隐喻", "encoding_secondary": [],
    "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["长篇论述从'中国女人丑不丑'开始，扩展到欧洲女性'11岁开始性生活''换男人如换衣服'、欧洲人口崩溃等——用一个对中国女性的负面评价引出对整个欧洲社会和人口危机的宏大论述。"],
        ["D2_隐喻：将欧洲人口/社会问题作为隐喻框架，实际在讨论(或引发讨论)中国的人口/性别议题。'战场百孔千疮''贫铀弹蹂躏'等战争隐喻用于描述欧洲社会问题，暗示'混乱''腐败'。"],
        ["贴吧性别讨论。文本混合了性别攻击(对中欧女性)、人口危机讨论和文明衰落叙事——多个主题交织。"],
        ["1.'中国女人那么丑'直接负面评价；2.'11岁开始过性生活''换男人如换衣服'——对欧洲女性带有贬低色彩的描述；3.战争隐喻('战场''贫铀弹')暗示社会崩溃。"],
        ["1.文本主要讨论人口问题而非性别攻击；2.引用了他人的话('朗金斯说')和学者观点；3.人口危机的宏观讨论有其学术正当性；4.对女性的不当描述在文本中占比小。"],
        "Risk: medium。以人口危机讨论为框架，夹杂对中欧女性的贬低性描述，D2隐喻将社会问题战争化。整体风险被宏论框架稀释。"
    )
}

# --- SAMPLE 002627 ---
corrections["002627"] = {
    "risk_level": "medium", "encoding_primary": "E1_平台黑话", "encoding_secondary": [],
    "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["质疑某人是假冒上海人。使用'低温人假冒京人''柴火妞''假名媛'等标签进行地域/阶层攻击。本质是地域身份的真实性争论。"],
        ["'低温人''柴火妞''假名媛'是E1_平台黑话——在知乎/贴吧等平台中固化用于贬低特定地域/阶层人群。'低温人'暗指来自寒冷/经济欠发达地区的人；'柴火妞'贬低农村/底层女性；'假名媛'攻击冒充上流社会的人。"],
        ["知乎地域讨论。身份真伪争论是地域歧视中常见的变体——通过质疑'你是假的XX人'来维护地域优越感。"],
        ["1.'低温人假冒京人'——用气候标签贬低外地人；2.'柴火妞'——对底层女性的阶层+性别双重贬低；3.全段在维护地域身份等级。"],
        ["1.主要争议对象是具体个人(某人)，非群体攻击；2.身份真伪的讨论在地域话题中有一定合理性；3.需要上下文确定讨论背景。"],
        "Risk: medium。E1平台黑话进行地域身份攻击，涉及阶层+性别交叉贬低，但对象是具体个人非群体。"
    )
}

# --- SAMPLE 002628 ---
corrections["002628"] = {
    "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["叙述者分享自己向同桌出柜后的经历——同桌从'怀疑'到'嫌弃'到'猥琐发笑'。这是在reporting一个基于性向的歧视经历，叙述者是被歧视方。"],
        ["无编码机制。文本是直白的个人经历叙述，没有使用谐音/隐喻/反讽等编码包装。风险不在于文本本身，而在于它记录了一次歧视事件。"],
        ["知乎LGBTQ讨论。是reporting型样本——受害者视角叙述被歧视经历，目的是揭露而非攻击。"],
        ["1.叙述了从'怀疑→嫌弃→猥琐发笑'的歧视过程；2.涉及LGBTQ话题。"],
        ["1.叙述者是被歧视方，文本不具有攻击性；2.是个人经历分享，无群体攻击意图；3.同桌的反应可能只是个人行为，不能代表系统性歧视的证据。"],
        "Risk: low。个人被歧视经历的reporting，受害者视角，无攻击性。话题敏感但文本无害。"
    )
}

# --- SAMPLE 002629 (hard_negative) ---
corrections["002629"] = {
    "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": False, "hard_negative": True,
    "target_known": True,
    "reasoning": R(
        ["'自己同胞遇害感到愤怒难道不应该吗'——表达同胞遇害后的愤怒情绪。'真就什么人看什么事？'——质疑对方以偏见视角解读事情。整体是情绪表达+反驳。"],
        ["无编码机制。文本是直接的愤怒表达和质疑，没有使用规避性编码。'真就什么人看什么事'是常见的反问句式。"],
        ["知乎种族歧视相关讨论。叙述者是为自己同胞辩护的立场。"],
        ["1.被ToxiCN标注toxic=0；2.文本是正常情绪表达+反问质疑。"],
        ["无风险证据。正常的情绪表达和讨论。"],
        "Risk: none (hard_negative)。正常情绪表达+反驳，无攻击性内容。虽然topic涉及敏感的种族话题但文本本身无害。"
    )
}

# --- SAMPLE 002630 ---
corrections["002630"] = {
    "risk_level": "medium", "encoding_primary": "D1_反讽", "encoding_secondary": [],
    "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["叙述者自称东北人'不黑安徽反而同情'，然后说'你们的富邻居们肯定要黑的'——用反讽方式说富裕邻省(江苏/浙江)会地域黑安徽。'毕竟和东北一个地位，不压榨一下怎么行'——反讽指出经济强省对弱省的结构性歧视。"],
        ["D1_反讽：表面在陈述'富邻居会黑'这一事实，实际在批评富裕地区对经济较弱地区的地域歧视和经济压榨。'不压榨一下怎么行'是典型的反讽句式——字面赞同实际批判。"],
        ["知乎地域歧视讨论。叙述者将东北和安徽并列为被歧视对象，分析歧视的经济根源。"],
        ["1.'和东北一个地位'——将被歧视地区并列；2.'不压榨一下怎么行'——典型反讽句式批判经济压迫；3.叙述立场是同情被歧视地区。"],
        ["1.提及了'黑安徽'的刻板印象，客观上重复了这一叙事；2.反讽意图需要语境确认；3.缺少上下文确定讨论背景。"],
        "Risk: medium。D1反讽批评地域歧视的经济根源，叙述立场反偏见，但反讽句式在裸文本中可能被误读。"
    )
}

# --- SAMPLE 002631 (hard_negative) ---
corrections["002631"] = {
    "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "weak", "needs_context": True, "hard_negative": True,
    "target_known": False,
    "reasoning": R(
        ["'关键是这男的他爸还支持？'——表达对一个男性及其父亲态度的惊讶/质疑。极度简略，缺乏任何敏感内容。"],
        ["无编码机制。普通的惊讶反问句式。"],
        ["标记topic=race_discussion但文本无任何种族内容。与种族歧视的关联完全依赖上下文。"],
        ["被ToxiCN标注toxic=0。"],
        ["1.文本无任何种族、性别、地域等敏感词汇；2.是普通的情感/态度表达；3.风险完全依赖于看不见的上下文。"],
        "Risk: none (hard_negative)。普通惊讶反问，不包含任何风险内容。标记needs_context=true因为含义完全依赖上下文。"
    )
}

# --- SAMPLE 002632 ---
corrections["002632"] = {
    "risk_level": "low", "encoding_primary": "D1_反讽", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'广西不也被黑得很惨吗'——指出广西也是地域歧视的受害者。叙述者立场是揭露地域歧视的普遍性，而非传播歧视。"],
        ["D1_反讽：字面上是疑问句，实际上是在确认'广西确实被黑得很惨'这一事实，带有对地域歧视现象的讽刺/不满。没有使用规避性编码。"],
        ["知乎地域歧视讨论。叙述者通过指出其他被歧视地区来揭露地域黑的普遍性问题。"],
        ["1.指出广西是地域歧视受害者——揭露而非传播歧视；2.叙述立场反偏见。"],
        ["1.'被黑得很惨'重复了'被黑'的叙事框架；2.需要上下文确定讨论背景；3.极短文本判断有限。"],
        "Risk: low。揭露地域歧视普遍性的反偏见表达，D1反讽批评歧视现象。"
    )
}

# --- SAMPLE 002633 ---
corrections["002633"] = {
    "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["河南人叙述自己亲身经历的地域歧视：同学母亲因为自己'是河南的'不同意孩子来做客；饭局上有人说在二七看到偷井盖。叙述者在揭露歧视经历，并表达了'对鄙视链也是...'的无奈。"],
        ["无编码机制。文本是直白的个人被歧视经历叙述。提及的'偷井盖'是河南地域歧视中的刻板印象，但叙述者是在复述他人言论，不是传播。"],
        ["知乎地域歧视讨论。叙述者是被歧视方，分享真实经历来揭露地域歧视的荒谬性。"],
        ["1.叙述了两起具体的地域歧视经历；2.'她说她妈并没有认识的河南人'——揭示歧视的非理性；3.叙述者立场是被歧视方/反偏见。"],
        ["1.提及了'偷井盖'的刻板印象，客观上重复了这一刻板叙事；2.对'鄙视链也是...'的省略可能暗示更大的不满。"],
        "Risk: low。受害者视角揭露地域歧视经历，无攻击性。话题敏感但文本属于reporting类型。"
    )
}

# --- SAMPLE 002634 (hard_negative) ---
corrections["002634"] = {
    "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "weak", "needs_context": False, "hard_negative": True,
    "target_known": False,
    "reasoning": R(
        ["'就感觉结婚事太多了所以我以后要和男生过'——表达对婚姻复杂性的厌倦，表示以后要和男生一起生活。可能是同性恋倾向的表达，也可能只是调侃。"],
        ["无编码机制。简短的日常表达，字面意思清晰。'和男生过'是直接陈述。"],
        ["贴吧性别讨论。是个人生活选择的表达，不构成对任何群体的攻击。"],
        ["被ToxiCN标注toxic=0。"],
        ["1.文本不攻击任何人/群体；2.是个人生活选择的正常表达；3.无编码机制。"],
        "Risk: none (hard_negative)。个人生活选择的正常表达，不包含攻击性内容。虽然topic=gender但文本无害。"
    )
}

# --- SAMPLE 002635 ---
corrections["002635"] = {
    "risk_level": "medium", "encoding_primary": "D1_反讽", "encoding_secondary": ["E1_平台黑话"],
    "ambiguity": "medium", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'怎么回事反同恋吧被同性恋占领了'——抱怨反同贴吧被同性恋'占领'。'神淋看了都要哭'——'神淋'是贴吧LGBTQ社区中的梗(淋语文化)，这里反讽使用。'等着被吸吧'——'吸'在贴吧LGBTQ语境中有性暗示。"],
        ["D1_反讽：叙述者表面抱怨贴吧被'占领'，实际带有调侃/讽刺语气。'神淋''吸'是E1_平台黑话——淋语文化和贴吧Gay圈用语。"],
        ["贴吧反LGBTQ讨论。使用了LGBTQ社区自身的文化符号('神淋')进行反讽，是一种复杂的表达——既使用同性恋文化梗又站在反同立场。"],
        ["1.'反同恋吧被同性恋占领了'表达不满；2.'等着被吸吧'带有性暗示的贬低；3.使用对方文化符号进行攻击。"],
        ["1.使用了LGBTQ社区自身的文化梗('神淋')，可能是圈内人自嘲而非攻击；2.'吸'在某些语境下是中性梗；3.整体语气偏调侃/玩笑。"],
        "Risk: medium。D1反讽+E1平台黑话在反LGBTQ语境中表达不满，使用了同性恋社区文化符号进行复杂攻击/调侃。"
    )
}

# --- SAMPLE 002636 (hard_negative) ---
corrections["002636"] = {
    "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "weak", "needs_context": True, "hard_negative": True,
    "target_known": False,
    "reasoning": R(
        ["'我也想知道现在如何了'——纯粹的好奇表达，想知道某事的后续。无任何敏感内容。"],
        ["无编码机制。普通的跟进询问。"],
        ["标记topic=race_discussion但文本完全无种族内容。与话题的关联完全依赖上下文。"],
        ["被ToxiCN标注toxic=0。"],
        ["1.文本无任何风险内容；2.是普通的社交互动表达。"],
        "Risk: none (hard_negative)。普通跟进询问，无任何攻击性或风险内容。"
    )
}

# --- SAMPLE 002637 (hard_negative) ---
corrections["002637"] = {
    "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": False, "hard_negative": True,
    "target_known": True,
    "reasoning": R(
        ["陈述高考名额分配的数据：山东每年挤出3万个名额支援中西部，河南分到几千个。讨论的是教育资源分配问题，没有攻击任何地域。"],
        ["无编码机制。正常的数据陈述和政策讨论。"],
        ["知乎地域讨论。讨论高考名额分配是正常的社会/教育政策讨论。"],
        ["被ToxiCN标注toxic=0。"],
        ["1.正常的教育政策讨论；2.数据陈述客观；3.没有地域攻击内容。"],
        "Risk: none (hard_negative)。正常高考名额分配讨论，数据陈述客观，无攻击性。"
    )
}

# --- SAMPLE 002638 ---
corrections["002638"] = {
    "risk_level": "low", "encoding_primary": "D1_反讽", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'为啥在网上在这帮男人眼里好像全国女生都喜欢黑人一样'——批评一种网络上的男性叙事(认为中国女性都喜欢黑人)。'这句话是错的。仅此而已'——明确否定该叙事。"],
        ["D1_反讽：通过转述+否定的结构('这句话是错的')来批评网络上的种族偏见叙事。叙述者站在反对种族偏见和性别偏见的立场。"],
        ["知乎种族歧视讨论。叙述者揭穿和否定了一个网络上的种族/性别偏见叙事。"],
        ["1.明确否定了'全国女生都喜欢黑人'的偏见叙事；2.'这句话是错的。仅此而已'——清晰的反偏见立场；3.叙述者同时反对种族偏见和性别偏见。"],
        ["1.转述了偏见叙事本身，客观上重复了它；2.需要上下文了解讨论背景；3.语气较为简略可能被误读。"],
        "Risk: low。明确反偏见的揭露型表达，D1反讽批评网络上的种族+性别偏见叙事。"
    )
}

# --- SAMPLE 002639 ---
corrections["002639"] = {
    "risk_level": "low", "encoding_primary": "D1_反讽", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'这些对东北人搞地域歧视的人其实很蠢，早晚搬起石头砸自己脚'——直接批判地域歧视者'很蠢'，并预测他们会自食其果。"],
        ["D1_反讽：通过'搬起石头砸自己脚'的比喻来讽刺地域歧视者的愚蠢和短视。无规避性编码，是直白的反歧视表达。"],
        ["知乎地域歧视讨论。叙述者明确站在反地域歧视的立场。"],
        ["1.'搞地域歧视的人其实很蠢'——直接批判歧视者；2.'搬起石头砸自己脚'——预测歧视的反弹效应；3.反偏见立场明确。"],
        ["1.使用了'很蠢'的侮辱词攻击歧视者，仍在攻击范畴内；2.需要上下文确定具体回应什么地域歧视言论。"],
        "Risk: low。明确反地域歧视表达，D1反讽批评歧视者。攻击对象是歧视者而非被歧视群体。"
    )
}

# --- SAMPLE 002640 ---
corrections["002640"] = {
    "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'安徽主要是在上海被歧视'——陈述一个社会现象：安徽人主要在上海受到地域歧视。这是在分析/描述歧视的分布，而非传播歧视。"],
        ["无编码机制。直白的社会观察/分析。"],
        ["知乎地域歧视讨论。叙述者在分析地域歧视的地域分布特征——属于对社会现象的客观描述。"],
        ["1.是在分析/报告歧视现象而非实施歧视；2.叙述立场中立偏反偏见。"],
        ["1.陈述了'安徽被歧视'的事实但未明确反对；2.极短文本判断空间有限；3.需要上下文确认立场。"],
        "Risk: low。社会现象的客观描述，分析地域歧视的分布特征，无攻击性。"
    )
}

# --- SAMPLE 002641 ---
corrections["002641"] = {
    "risk_level": "medium", "encoding_primary": "D1_反讽", "encoding_secondary": ["E1_平台黑话"],
    "ambiguity": "medium", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["长文分析B站弹幕中的性别双标现象：男性互殴弹幕'玩玩梗'，女性打架弹幕出现'姐姐好飒''小仙女互殴'等扩大化弹幕。提出'这是当初仙女们扩大化的反噬'——认为女性群体先搞性别扩大化，现在遭到报复。"],
        ["D1_反讽：叙述者表面在分析'扩大化的反噬'，实际在表达对女性主义('仙女们')的不满。'小仙女'是E1_平台黑话——在B站/贴吧固化为对女性(尤其是被认为是'女拳'的)的贬称。"],
        ["贴吧性别讨论。文本结构是'观察现象→分析原因→归咎于对方群体'——将性别对立的责任单方面归于女性群体。"],
        ["1.'小仙女'——对女性的平台贬称；2.'仙女们扩大化的反噬'——将性别对立归咎于女性；3.分析框架有偏向性——只提及女性的扩大化，未提男性的扩大化。"],
        ["1.文本确实提出了一个可验证的观察(B站弹幕中的性别差异)；2.使用了'扩大化当然是不好的'表达了规范立场；3.分析在一定程度上可能是准确的；4.使用了反讽+分析而非直接辱骂。"],
        "Risk: medium。D1反讽+E1黑话将性别对立归咎于女性，分析框架有偏向性但包装在理性讨论中。"
    )
}

# --- SAMPLE 002642 ---
corrections["002642"] = {
    "risk_level": "medium", "encoding_primary": "D2_隐喻", "encoding_secondary": [],
    "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["对比'男權社會'和'女權社會'：声称前者会出现优待女人的行为和女性特权，而后者'只会一味女性特权，打压男性'。用对比框架输出反女性主义观点。"],
        ["D2_隐喻：将'男权社会'和'女权社会'设置为对立隐喻框架——男权=优待女性，女权=打压男性。这个二分法是简化和误导性的，用来制造'男性也是受害者'的叙事。"],
        ["贴吧性别讨论。通过构建虚假的对称性来输出反女性主义观点——这是网络反女性主义话语的常见策略。"],
        ["1.'女权社会只会一味女性特权打压男性'——明确的反女性主义表达；2.二分框架误导性地暗示男女权社会是对称的。"],
        ["1.文本讨论的是抽象社会概念，没有攻击具体人群；2.对女性主义的批评在一定范围内属于正常社会讨论；3.没有使用辱骂词。"],
        "Risk: medium。D2隐喻通过构建虚假的男女权对称框架输出反女性主义观点，包装在抽象社会讨论中。"
    )
}

# --- SAMPLE 002643 ---
corrections["002643"] = {
    "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": False, "hard_negative": True,
    "target_known": True,
    "reasoning": R(
        ["分析'这种地方'被吐槽的两种类型：发达城市被外来打工者吐槽，或不太发达地区因外出打工者素质不高被吐槽。是社会学式观察，没有攻击特定群体。"],
        ["无编码机制。客观的社会观察/分析。"],
        ["知乎地域讨论。是分析地域歧视产生机制的客观讨论。"],
        ["被ToxiCN标注toxic=0。"],
        ["1.客观分析；2.无攻击性；3.是社会现象的理性讨论。"],
        "Risk: none (hard_negative)。客观的社会现象分析，讨论地域歧视的产生机制，无攻击性。"
    )
}

# --- SAMPLE 002644 ---
corrections["002644"] = {
    "risk_level": "low", "encoding_primary": "C2_历史事件影射", "encoding_secondary": [],
    "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'八国洋人在天津消灭了九成天津人，天津貌似没有被毁灭啊'——涉及历史事件(八国联军/天津)，用历史来论证'天津经历了大屠杀但没有被毁灭'。"],
        ["C2_历史事件影射：引用八国联军在天津的历史事件，可能影射现实中的某些讨论。'消灭了九成天津人'这一表述可能夸张/歪曲历史。但整体是对历史事件的提及，风险不高。"],
        ["知乎地域讨论。引用历史事件来参与地域讨论——历史影射在地域话题中可能触发敏感讨论。"],
        ["1.提及了外国军队在中国的历史暴行；2.'消灭了九成'是夸张表述。"],
        ["1.讨论的是历史事件而非现实攻击；2.主要话题是地域而非政治；3.可能只是历史讨论。"],
        "Risk: low。C2历史事件影射，引用八国联军历史参与地域讨论。风险低但涉及历史敏感内容。"
    )
}

# --- SAMPLE 002645 ---
corrections["002645"] = {
    "risk_level": "high", "encoding_primary": "A1_普通谐音", "encoding_secondary": ["E1_平台黑话"],
    "ambiguity": "low", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'幕刃瘠薄又逮着「理」了'——使用谐音编码攻击女性。'幕刃'→'母人'(贬低女性的黑话)，'瘠薄'→'鸡巴'(粗俗词)，合起来是恶意的性别辱骂。"],
        ["A1_普通谐音：'幕刃'(mù rèn)→'母人'(mǔ rén)，用近音字替换，规避直接打'母人'。'瘠薄'(jí báo)→'鸡巴'(jī ba)，用近音字替换粗俗词。E1_平台黑话：'母人'在贴吧等社区固化为贬低女性的黑话。"],
        ["贴吧性别攻击。通过谐音编码包装恶意辱骂——规避直接检测但保留了攻击性。"],
        ["1.'幕刃'→'母人'是精心构造的谐音替换；2.'瘠薄'→'鸡巴'是规避性谐音；3.整体是针对性别的恶意辱骂。"],
        ["1.谐音替换可能被解释为输入法错误；2.缺少对话上下文确定攻击对象。"],
        "Risk: high。A1双字谐音('幕刃''瘠薄')+E1平台黑话进行性别辱骂，规避意图明确。"
    )
}

# --- SAMPLE 002646 ---
corrections["002646"] = {
    "risk_level": "high", "encoding_primary": "D3_借代", "encoding_secondary": ["literal_keyword"],
    "ambiguity": "low", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["极端种族仇恨言论。用'国际鬼子虫类及其它们后代虫混'去人性化指代黑人及混血群体，涉及吴亦凡案件和宁波案件，使用俄语词'республиканскоеправительство'（共和国政府）进行某种政治影射。"],
        ["D3_借代：'虫类''虫混'——用昆虫借代黑人群体，是去人性化修辞。literal_keyword：'国际鬼子'是对外国人的直接辱骂。B4_符号/Unicode干扰：使用俄语西里尔字母插入中文文本，可能用来规避关键词检测。"],
        ["贴吧种族歧视讨论。极端仇恨言论——去人性化修辞+外语插入+案件影射，多重策略组合。"],
        ["1.'虫类''虫混'——去人性化修辞；2.'国际鬼子'——直接辱骂；3.俄语插入试图规避检测；4.整体是极端种族仇恨言论。"],
        ["1.发言可能来自情绪极端化的个人；2.俄语插入可能是复制粘贴非原创编码。"],
        "Risk: high。D3去人性化('虫类')+literal_keyword+外语干扰的极端种族仇恨言论，多重策略组合。"
    )
}

# --- SAMPLE 002647 (hard_negative) ---
corrections["002647"] = {
    "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "weak", "needs_context": True, "hard_negative": True,
    "target_known": False,
    "reasoning": R(
        ["'我评论中有提到关于男性或者女性的字眼吗？😄😄'——自我辩护，声称自己的评论没有提到性别。使用微笑emoji可能是表示无辜或反讽。"],
        ["无编码机制。直接的自我辩护表达。"],
        ["标记topic=lgbt_discussion但文本无LGBTQ内容。是对话中的自我辩护——需要上文才能理解争议内容。"],
        ["被ToxiCN标注toxic=0。"],
        ["1.文本本身无攻击性内容；2.是社交互动中的自我辩护；3.无编码机制。"],
        "Risk: none (hard_negative)。自我辩护的社交互动，文本本身无风险内容。"
    )
}

# --- SAMPLE 002648 (hard_negative) ---
corrections["002648"] = {
    "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": False, "hard_negative": True,
    "target_known": True,
    "reasoning": R(
        ["东北人自述走南闯北二十年的经历——'从来没觉得有人瞧不起我'，强调人品正直就能赢得尊重，最后以'天王老子也不怕'收尾。是自信积极的自我表达。"],
        ["无编码机制。直白的个人经历分享和价值观表达。'老子''天王老子'是东北方言中正常的自我指代和口语表达，非攻击性。"],
        ["知乎地域讨论。通过个人正面经历来反驳地域歧视的存在/影响。"],
        ["被ToxiCN标注toxic=0。"],
        ["1.积极正面的价值观表达；2.无攻击性内容；3.是反驳地域歧视影响的个人叙事。"],
        "Risk: none (hard_negative)。正面的个人经历分享，反驳地域歧视，无攻击性。"
    )
}

# --- SAMPLE 002649 ---
corrections["002649"] = {
    "risk_level": "medium", "encoding_primary": "D1_反讽", "encoding_secondary": ["E1_平台黑话"],
    "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'击毙我，你得到一具遗体！满足我，你可以去眼馋异教徒韩男！'——充满攻击性/戏剧性的表达。'异教徒韩男'涉及宗教+国籍双重标签，'眼馋'暗示性/情感竞争。"],
        ["D1_反讽：通过极端的'击毙→遗体''满足→眼馋韩男'对照来制造反讽效果。'异教徒'的使用引入了宗教维度——可能是对中韩男性竞争的夸张反讽。"],
        ["贴吧性别讨论。文本高度戏剧化，可能是特定讨论(中韩男性比较/竞争)中的反讽回复。"],
        ["1.'异教徒韩男'引入了宗教+国籍双重对立；2.整体语气带有攻击性和戏剧性。"],
        ["1.可能是特定讨论中的反讽/调侃；2.'异教徒'可能只是夸张用语非严肃宗教指涉；3.极短文本缺少上下文难以确定真实意图。"],
        "Risk: medium。D1反讽+E1黑话的戏剧化表达，涉及国籍+宗教标签，缺少上下文难以确定真实意图。"
    )
}

# --- SAMPLE 002650 ---
corrections["002650"] = {
    "risk_level": "low", "encoding_primary": "D2_隐喻", "encoding_secondary": [],
    "ambiguity": "medium", "evidence_strength": "weak", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'个性签名亮了:向韩国人学习😓'——引用某人的个性签名'向韩国人学习'，加上😓表情表示无语/不满。'韩国人'在中文网络种族歧视话语中有时用作反讽或攻击目标。"],
        ["D2_隐喻：'向韩国人学习'的具体含义依赖上下文——可能指学习韩国人的某些被认为负面的特质(如'大男子主义''整容''文化挪用'等)。在特定话题中可能是反讽/攻击。"],
        ["知乎种族歧视讨论。风险完全取决于上下文——'向韩国人学习'的具体含义和讨论的主题。"],
        ["1.😓表情明确表达了不满/无语；2.引用'向韩国人学习'作为批评对象。"],
        ["1.文本本身只是引用+表情，无直接攻击；2.'向韩国人学习'完全可以是正面的；3.缺少上下文无法确认风险指向。"],
        "Risk: low。引用+表情的极简表达，D2隐喻依赖上下文触发。风险很低但需要上下文确认。"
    )
}

# --- SAMPLE 002651 ---
corrections["002651"] = {
    "risk_level": "medium", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'不结婚。但喜欢跟黑人做。😅😅'——表达个人性偏好。可能是在跨种族婚恋讨论中的个人表态，也可能带有故意挑衅/刺激他人的意图。"],
        ["无明确编码机制。文字直白，'做'是'做爱'的口语省略。😅表情(尴尬/苦笑)可能暗示自知话题敏感。"],
        ["知乎种族歧视讨论。在中跨种族婚恋的敏感讨论中，这种直白的个人偏好表达可能带有挑衅性。"],
        ["1.明确表达了跨种族的性偏好；2.在敏感话题中使用直白表达可能意在刺激。"],
        ["1.是个人偏好的表达而非群体攻击；2.'喜欢跟黑人做'本身不是攻击性陈述；3.😅表情可能表明自知敏感而添加的缓和。"],
        "Risk: medium。在敏感讨论中的个人偏好直白表达，可能意在挑衅但未直接攻击。标记needs_context=true。"
    )
}

# --- SAMPLE 002652 ---
corrections["002652"] = {
    "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["总结地域黑的'典型'分布：东北(大区域)、河南(省)、武汉(二线)、广州(一线)。末尾🤣表情显示以调侃态度看待这一现象。"],
        ["无编码机制。是客观/半调侃的社会现象总结。🤣(笑到打滚)表情表明叙述者的态度是调侃/讽刺歧视现象本身。"],
        ["知乎地域歧视讨论。通过列举被黑地区来讽刺地域黑现象的普遍性——是一种揭露/调侃而非传播歧视。"],
        ["1.客观列举了常见的被地域黑地区；2.🤣表情表明调侃/讽刺态度；3.叙述框架是揭露现象。"],
        ["1.列举了各地域的负面刻板印象，客观上重复了它们；2.没有明确表达反对立场；3.需要上下文确认叙述者真实态度。"],
        "Risk: low。总结地域黑现象的social observation，🤣表情显示调侃/讽刺态度。话题敏感但文本属于揭露型。"
    )
}

# --- SAMPLE 002653 ---
corrections["002653"] = {
    "risk_level": "high", "encoding_primary": "A1_普通谐音", "encoding_secondary": ["D2_隐喻"],
    "ambiguity": "low", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'只有大果的姥爷喜欢黑，送银子送穴都要跪求黑来'——'大果'→'大国'(中国)，'姥爷'→'老爷'(当官的)，'送穴'是粗俗的性暗示(献上女性)。整体在攻击中国政府/领导层与非洲的关系，使用粗俗和种族化的表达。"],
        ["A1_普通谐音：'大果'(dà guǒ)→'大国'(dà guó)，用近音字替换规避。'姥爷'(lǎo ye)→'老爷'(lǎo ye)，近音替换指代当权者。D2_隐喻：'送银子送穴'是粗俗隐喻——将中非关系描绘为用金钱+性(女性)来'跪求'黑人。"],
        ["贴吧种族歧视讨论。通过谐音编码攻击中国对非政策，将国际关系粗俗化和种族化。"],
        ["1.'大果'→'大国'是规避性谐音；2.'姥爷'→'老爷'近音替换指代当权者；3.'送穴'是极其粗俗的性化表达；4.'跪求黑来'带有种族化视角。"],
        ["1.贴吧中'大果'等谐音有时用于非政治性吐槽；2.可能只是极端个人情绪表达。"],
        "Risk: high。A1双字谐音+D2粗俗隐喻攻击中国政府对非政策，涉及政治敏感+种族+性别三重维度。"
    )
}

# --- SAMPLE 002654 ---
corrections["002654"] = {
    "risk_level": "medium", "encoding_primary": "D3_借代", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'不予置评……不过你问我的话我可能给你输出racial discrimination观念。（虽然并未接触过默）'——'默'是黑人的贬义简称。叙述者承认自己有种族歧视观念但'未接触过'——是在反思还是炫耀？"],
        ["'默'是D3_借代——黑人的贬义简称。叙述者使用'racial discrimination'英文词来框架化自己的偏见——一种疏离/学术化的包装。"],
        ["知乎种族歧视讨论。叙述者用半反思的语调承认自己有种族偏见——语气模糊，可能在自我批评也可能在炫耀/合理化。"],
        ["1.明确承认自己会'输出racial discrimination观念'；2.使用贬义借代词'默'。"],
        ["1.'不予置评'表明有一定自我约束；2.'虽然并未接触过'暗示偏见来自二手信息——有反思元素；3.括号中的补充说明带有一定的自嘲/反思。"],
        "Risk: medium。D3借代('默')+半反思语调表达种族偏见，反思元素降低了直接攻击性但偏见内容明确。"
    )
}

# --- SAMPLE 002655 ---
corrections["002655"] = {
    "risk_level": "high", "encoding_primary": "D3_借代", "encoding_secondary": ["literal_keyword"],
    "ambiguity": "low", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'其实上边的吧友们都真正地理解自己反对的是什么。就是反对自己后代的基因被染黑。'——将种族歧视合理化为'保护后代基因不被染黑'。'染黑'是极其直白的种族主义表达，将黑人基因描绘为污染。"],
        ["D3_借代：'染黑'——用颜色词'黑'借代黑人种族/基因，将跨种族繁衍隐喻为'污染/染色'。literal_keyword：'反对自己后代的基因被染黑'是直白的种族主义陈述，未经过复杂编码。"],
        ["贴吧种族歧视讨论。将种族歧视包装为'保护后代基因'——这是白人至上主义/种族主义的经典叙事框架。"],
        ["1.'基因被染黑'——极其直白的种族主义表达；2.将歧视合理化为'保护后代'；3.'吧友们都真正地理解'——寻求群体认同。"],
        ["1.文本是在转述/分析'吧友们的想法'而非直接表达自己观点，但'都真正地理解'表明赞同。"],
        "Risk: high。D3借代('染黑')+literal_keyword，以'保护后代基因'框架包装的直白种族主义。"
    )
}

# --- SAMPLE 002656 ---
corrections["002656"] = {
    "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "weak", "needs_context": True, "hard_negative": False,
    "target_known": False,
    "reasoning": R(
        ["'当面问清楚，不能接受有孩子就说清楚立刻分了，越快越好，迟则生变，抱着玩玩的心态我认为不可以啊'——在给感情建议：如果有孩子的问题要当面沟通，不能接受就分手。"],
        ["无编码机制。正常的感情建议/人生建议。"],
        ["标记topic=gender_reporting。是普通的感情建议，与性别攻击无关。"],
        ["1.是建设性的感情建议。"],
        ["1.文本无任何攻击性内容；2.是正常的社交讨论；3.无编码机制。"],
        "Risk: low。正常的感情建议，无攻击性内容。标记topic与文本不符，文本本身无害。"
    )
}

# --- SAMPLE 002657 ---
corrections["002657"] = {
    "risk_level": "high", "encoding_primary": "D3_借代", "encoding_secondary": ["literal_keyword"],
    "ambiguity": "low", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'希望他们嫁给默以后都去非洲吧，不要待在国内，看着觉得蛮恶心的，跑爹默竟然也有人中国女人愿意嫁也不配当中国人'——'默'是黑人贬称，'跑爹默'是粗俗的种族侮辱。主张将嫁给黑人的中国女性驱逐出中国并剥夺其中国人身份。"],
        ["'默'是D3_借代——黑人的贬义简称。'跑爹默'是极其粗俗的种族+性别侮辱——暗示女性'跑去跟黑人父亲...'。literal_keyword：'恶心''不配当中国人'是直接的辱骂和排斥。"],
        ["知乎种族歧视讨论。极端排斥言论——不仅攻击黑人还攻击选择跨种族婚姻的中国女性，使用驱逐和身份剥夺的极端措辞。"],
        ["1.'默''跑爹默'——种族侮辱词；2.'恶心'——直接辱骂；3.'不配当中国人'——身份剥夺/驱逐；4.全句是完整的排斥/仇恨言论。"],
        ["1.单一评论无法代表整体舆论。"],
        "Risk: high。D3借代('默')+literal_keyword，极端排斥言论——攻击跨种族婚恋并主张身份剥夺和驱逐。"
    )
}

# --- SAMPLE 002658 ---
corrections["002658"] = {
    "risk_level": "medium", "encoding_primary": "E1_平台黑话", "encoding_secondary": [],
    "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'最好的防守就是进攻，在被利用前利用她们，不要贪恋美色，多了不好'——建议采取先发制人的策略对待女性，将两性关系描绘为'利用 vs 被利用'的零和博弈。"],
        ["E1_平台黑话：'利用她们'在贴吧/PUA社区语境中固化为对女性采取操控手段。没有使用谐音/隐喻等规避性编码，是相对直白的表述。"],
        ["贴吧性别讨论。将两性关系描绘为敌对博弈——是PUA/红丸社区中常见的话语模式。"],
        ["1.'在被利用前利用她们'——将女性预设为利用者并建议先发制人；2.'利用'暗示操控/剥削；3.将两性关系描绘为战争('防守→进攻')。"],
        ["1.可能是对特定情况的个人建议而非普遍性的攻击；2.'利用'在中文中也可用于较中性的语境；3.缺少上下文确定讨论背景。"],
        "Risk: medium。E1平台黑话将两性关系描绘为敌对博弈，建议先发制人的操控策略。需要上下文确定具体语境。"
    )
}

# --- SAMPLE 002659 ---
corrections["002659"] = {
    "risk_level": "medium", "encoding_primary": "D1_反讽", "encoding_secondary": ["E1_平台黑话"],
    "ambiguity": "medium", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["长篇叙述一个'白男利用中国女性后反被利用'的故事：白男来华赚钱→找中国女性同居→女方怀孕→男方要求打掉→女方追到国外起诉→拿钱回国。将中国女性('小仙女')描绘为精于算计的牟利者。"],
        ["D1_反讽：用'高高兴兴地拿钱回国'等正面词汇描述负面行为——将女性描绘为贪婪的牟利者。'小仙女'是E1_平台黑话——对女性(尤其是年轻/被认为精于算计的)的贬称。"],
        ["贴吧性别讨论。构建了'外国男利用中国女→中国女反利用外国男'的叙事，将跨国婚恋描绘为双方的算计/利用。"],
        ["1.'小仙女'——对女性的贬称；2.'高高兴兴地拿钱回国'——将女性描绘为贪婪牟利者；3.整个叙事框架将两性/跨国关系描绘为互相利用。"],
        ["1.是叙述故事而非直接攻击；2.涉及法律维权('大使馆帮忙起诉')——故事中有女性合法维权的元素；3.可能是在批评'白男'而非单纯攻击女性。"],
        "Risk: medium。D1反讽+E1黑话构建跨国婚恋中的'互相利用'叙事，将中国女性描绘为牟利者。"
    )
}

# --- SAMPLE 002660 ---
corrections["002660"] = {
    "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": True, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["苏南到东北的跨地域生活者分享身份困境：'说哪儿都不合适'。对地域黑的态度是'黑去呗'(随他们黑)——一种无奈/无所谓的态度。"],
        ["无编码机制。直白的个人经历分享。"],
        ["知乎地域歧视讨论。跨地域身份者在讨论地域歧视——是被歧视的视角。"],
        ["1.分享了跨地域身份带来的身份困境；2.'黑去呗'是对地域歧视的无奈态度。"],
        ["1.是个人经历分享，无攻击性；2.'黑去呗'是在放弃对抗而非传播歧视。"],
        "Risk: low。跨地域身份者的个人经历分享，对被歧视的无奈态度。无攻击性。"
    )
}

# --- SAMPLE 002661 ---
corrections["002661"] = {
    "risk_level": "high", "encoding_primary": "D2_隐喻", "encoding_secondary": ["E1_平台黑话"],
    "ambiguity": "low", "evidence_strength": "strong", "needs_context": False, "hard_negative": False,
    "target_known": True,
    "reasoning": R(
        ["'比起你为了生活到处传艾更好'——'传艾'=传播艾滋。将对方(同性恋者)与传播艾滋病关联，是对LGBTQ群体的恶毒污名化。"],
        ["D2_隐喻：'传艾'——用'艾'(艾滋病)作为隐喻框架，暗示LGBTQ群体=艾滋传播者。E1_平台黑话：'艾'在贴吧等社区中作为'艾滋'的缩写/黑话使用。"],
        ["贴吧反LGBTQ讨论。用'传艾'进行极其恶毒的污名化攻击——将整个群体与致命疾病关联。"],
        ["1.'传艾'——将LGBTQ群体与艾滋病传播恶意关联；2.用'比起...更好'的比较句式强化攻击；3.污名化是反LGBTQ言论中最恶劣的形式之一。"],
        ["1.可能是针对特定个人的指控而非群体攻击；2.极短文本缺少上下文。"],
        "Risk: high。D2隐喻('传艾')将LGBTQ群体与艾滋病传播恶意关联——最恶劣的污名化攻击形式之一。"
    )
}

# --- SAMPLE 002662 ---
corrections["002662"] = {
    "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [],
    "ambiguity": "low", "evidence_strength": "moderate", "needs_context": True, "hard_negative": True,
    "target_known": True,
    "reasoning": R(
        ["'最早就是河南，我还记得井盖和董存瑞。现在得加上东三省了。嗯嗯，估计明后年再回答这个问题的时候山东人会要求把他们也加上。'——回忆地域黑的历史和演变。提及了'井盖'(河南刻板印象)和'董存瑞'(可能与地域相关)。预测下一个被黑的地区。"],
        ["无编码机制。是在总结/回忆地域歧视的历史演变。提及刻板印象('井盖')是在复述/引用而非主动传播。"],
        ["知乎地域歧视讨论。通过回顾地域黑的历史来揭示其荒谬性和演变规律——可能意在讽刺。"],
        ["被ToxiCN标注toxic=0。"],
        ["1.是在总结/分析歧视现象而非传播；2.预测式的语气可能意在揭露歧视的荒谬；3.缺少明确的反对歧视表态。"],
        "Risk: low。总结地域黑历史演变的社会观察，hard_negative因为文本目的是揭露/调侃歧视现象本身。但提及了具体刻板印象('井盖')。"
    )
}

# Apply corrections
for s in samples:
    sid = s['id']
    if sid in corrections:
        c = corrections[sid]
        for key in c:
            s[key] = c[key]
    s['quality_status'] = 'reviewed'
    if 'reviewed_by=claude' not in s.get('review_notes', ''):
        s['review_notes'] = s.get('review_notes', '') + '; reviewed_by=claude; chunk=000'

# Write output
with open('data/raw/batch23_chunks/chunk_000_reviewed.jsonl', 'w') as f:
    for s in samples:
        f.write(json.dumps(s, ensure_ascii=False) + '\n')

# Stats
changed = sum(1 for s in samples if s['id'] in corrections)
print(f"Corrected: {changed}/50 samples")
print(f"Written to data/raw/batch23_chunks/chunk_000_reviewed.jsonl")
