#!/usr/bin/env python3
"""Review chunk_034.jsonl — 50 ToxiCN samples. Text-specific rewriting of ALL reasoning fields."""
import json
from collections import Counter

src = "/Users/davidchankong/Documents/审查微调/data/raw/batch23_chunks/chunk_034.jsonl"
dst = "/Users/davidchankong/Documents/审查微调/data/raw/batch23_chunks/chunk_034_reviewed.jsonl"

samples = []
with open(src) as f:
    for line in f:
        line = line.strip()
        if line:
            samples.append(json.loads(line))

# ====== REVIEW FUNCTIONS ======

def rev_004313(s):
    s["risk_level"] = "medium"
    s["encoding_primary"] = "C4_典故/物品/符号借用"
    s["encoding_secondary"] = ["D2_隐喻"]
    s["needs_context"] = True
    s["ambiguity"] = "medium"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "字面义是'那个会打人的悲伤蛙？把它拿过来吧'，采用网络meme句式'拿来吧你'。'悲伤蛙'是Pepe the Frog的中文译名。",
            "'打人的悲伤蛙'将'打人'（暴力行为）与Pepe青蛙形象绑定，在种族讨论语境中Pepe常被用作黑人群体的代指符号。"
        ],
        "encoding_analysis": [
            "主编码C4（符号借用）：悲伤蛙/Pepe是国际互联网上被极右翼/种族主义群体挪用的meme符号，在中国互联网种族讨论中常见用Pepe指代黑人群体。",
            "次编码D2（隐喻）：'打人'隐喻'暴力倾向'，将暴力属性投射到Pepe->黑人群体上。整体是'黑人=会打人的青蛙'的贬义映射链。"
        ],
        "context_analysis": [
            "知乎平台种族话题讨论中，Pepe青蛙是已知的种族歧视编码符号，脱离此语境则可能被误读为无攻击性的meme玩梗。",
            "需要更多上下文（原帖/回复关系）才能确定是否确实指向黑人群体而非单纯的meme分享。"
        ],
        "supporting_evidence": [
            "1. '悲伤蛙'在中文互联网种族讨论中是公认的黑人代指符号（类似黑猩猩、猴子等动物化编码的变体）。",
            "2. '打人的'将暴力属性附着于该符号，强化了对黑人群体的'暴力危险'刻板印象。",
            "3. '拿来吧你'是典型的上位者/支配者语气，在此表现为对'打人的青蛙'的支配态度。",
            "4. 样本被ToxiCN标注为toxic=1且expression=2（隐晦表达），确认原始标注者识别到了编码痕迹。"
        ],
        "counter_evidence": [
            "1. 悲伤蛙/Pepe在部分中文社区已泛化为普通meme，不必然指向种族编码。'拿来吧你'本身是无攻击性的meme句式。",
            "2. 单条评论缺少原帖上下文，无法确认种族指向是发帖人的本意还是标注者的解读。"
        ],
        "final_rationale": "Risk: medium。通过Pepe（悲伤蛙）符号+暴力隐喻编码种族贬义，但编码链较间接，需要语境才能准确解码；存在纯玩梗的合理解释可能。"
    }
    return s

def rev_004314(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本分析地域歧视的传播模式：以山东为例，警告其可能步河南和东北的后尘——最初看似无害的网络讨论会演变成大规模地域黑。",
            "叙述者引用历史经验（'当年河南和东北被黑的时候，开始造势也是这个样'），将当前的山东讨论与过去的地域黑事件做类比。"
        ],
        "encoding_analysis": [
            "无编码机制。文本是直接的观察分析，没有使用谐音、隐喻、反讽等手段。叙述者用'希望……扛得住'表面是祝愿实际是预警，但语气仍是分析性的。",
            "'\U0001f606\U0001f606\U0001f606'表情符号表示苦笑/无奈，不是嘲讽幸灾乐祸，而是在社会批评中表达无奈感——'我已经见过这个剧本了'。"
        ],
        "context_analysis": [
            "知乎平台的地域话题讨论中，这是典型的'反地域黑'或'预警'型评论。不需要额外上下文即可判断其立场是反对地域歧视的。"
        ],
        "supporting_evidence": [
            "1. 文本将地域黑描述为可预见的负面过程（'后来就控制不住了'），站在批评者而非煽动者立场。",
            "2. '希望下一轮南方攻击你们能扛得住'是预警式表达，不是攻击山东人。",
            "3. 叙述者通过河南/东北的先例来论证地域黑的破坏性，是社会学分析式写作。",
            "4. 文本未被ToxiCN标注为toxic，属于hard_negative类别，但原字段误标为expr=3（揭露/报告）。"
        ],
        "counter_evidence": [
            "1. 可被解读为'幸灾乐祸地预测山东也会被黑'的隐性攻击，但全文叙事框架是反偏见而非传播偏见。"
        ],
        "final_rationale": "Risk: none (hard_negative)。文本是对地域歧视现象的社会学观察和预警，站在反对地域黑的立场，不具备攻击性。"
    }
    return s

def rev_004315(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本陈述一个事实：苏南人歧视苏北/江北人，而江北人自己也在江苏内部歧视链中处于下游。'讲真'（说实话）是口语化的真实宣称。"
        ],
        "encoding_analysis": [
            "无编码机制。文本是直白的社会观察。'江北人'（长江以北的江苏人）是标准的地域分类术语，'被苏南歧视'是直接描述社会现象，没有使用攻击性词汇或编码。"
        ],
        "context_analysis": [
            "在地域话题讨论中，这句话可能是回应某个质疑'谁歧视谁'的讨论链。不需要额外上下文即可判断这是陈述而非攻击。"
        ],
        "supporting_evidence": [
            "1. '讲真'标志叙述者试图呈现客观事实而非表达偏见。",
            "2. '自己都是被……的人'的结构暗示同情（你们自己也是受害者）。",
            "3. 没有使用任何侮辱性词汇或负面评价。",
            "4. 被ToxiCN标注为toxic=0（非有毒），是hard_negative样本。"
        ],
        "counter_evidence": [
            "1. 如果脱离原对话链，可被孤立解读为'承认苏南对江北的歧视是事实'，但这只是陈述社会现象，不是煽动歧视。"
        ],
        "final_rationale": "Risk: none (hard_negative)。文本是陈述地域歧视社会结构的客观观察，无攻击性。"
    }
    return s

def rev_004316(s):
    s["risk_level"] = "medium"
    s["encoding_primary"] = "D2_隐喻"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "medium"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "表面义为'路人说：我他妈的来的这是动物园吗？'——将当前场景比作动物园，强调所见之人如同展出的动物。",
            "'旁人'（bystander）是一种叙事视角，暗示这是'客观旁观者'的反应，增强贬义的合理性。'他么'是语气词，加强惊讶/不屑。"
        ],
        "encoding_analysis": [
            "主编码D2（隐喻）：将一群人比作动物园里的动物，是一种去人化的隐喻攻击。'动物园'意象暗示被描述者不是'人'而是'供人观赏的动物'。",
            "编码路径清晰：场景 -> 动物园 -> 动物 -> 去人化 -> 群体贬低。同类编码在种族歧视语境中常见（将少数群体比作珍奇动物）。"
        ],
        "context_analysis": [
            "贴吧种族讨论话题，原帖大概率涉及某个少数群体的聚集场景，发帖人用'动物园'来贬低该群体。",
            "需要原帖内容才能确认被比作动物的是哪个具体群体（黑人/其他少数族裔）。"
        ],
        "supporting_evidence": [
            "1. '动物园'比作人类场景是经典的去人化隐喻，常见于种族/地域歧视表达。",
            "2. '旁人'的叙事视角是修辞技巧，暗示'不是我说的，是路人说的'以规避直接责任。",
            "3. '我他么'的口语化语气传递了强烈的负面试探/不屑情绪。",
            "4. 被ToxiCN标注为toxic=1且expression=2（隐晦表达），确认有编码痕迹。"
        ],
        "counter_evidence": [
            "1. 如果是参观实体动物园后的评论，则字面义就是字面义。缺少原帖内容，无法完全排除这种可能性。",
            "2. '动物园'在网络用语中也可用来形容场面混乱热闹（'评论区变动物园了'），不一定都是歧视。"
        ],
        "final_rationale": "Risk: medium。通过'动物园'隐喻实施去人化攻击，将某群体比作供观赏的动物；表达隐晦需要语境确认，但编码指向明确。"
    }
    return s

def rev_004317(s):
    s["risk_level"] = "high"
    s["encoding_primary"] = "D2_隐喻"
    s["encoding_secondary"] = ["C4_典故/物品/符号借用"]
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "strong"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本使用'猿形毕露'（原形毕露的变体，将'原'改为'猿'即猿猴）作为核心攻击词，指某人/某群体露出了猿猴的真面目。",
            "后续'狗狗的YD长在了猩猩身上'将狗（狗狗）的阴茎（YD）安在猩猩身上，并用'有怜悯之心''每天拿它娱乐娱乐'进行嘲讽，整体构成动物化、性器官化的侮辱。"
        ],
        "encoding_analysis": [
            "主编码D2（隐喻）：通过猿猴、猩猩、狗等动物意象隐喻某群体'不是人'，是经典的种族歧视动物化编码。'猿形毕露'是中文网络针对黑人群体的高度固化的种族编码词。",
            "次编码C4（符号借用）：'猿形毕露'是对成语'原形毕露'的恶搞借用，改变了关键字的偏旁部首以指向猿猴——这种对语言符号的有意识改造是符号借用。",
            "'YD'（阴茎）是拼音缩写，属于A2类拼音编码，但在本条中主要是增强侮辱性，不是主要编码机制。"
        ],
        "context_analysis": [
            "贴吧种族话题中，'猿形毕露'是专门针对黑人群体的种族歧视编码词（类比黑人=猿猴）。不需要上下文就能判断攻击对象是黑人群体。",
            "全段语气是假惺惺的'怜悯'（'大家要有怜悯之心'），实则是变本加厉的侮辱。"
        ],
        "supporting_evidence": [
            "1. '猿形毕露'是中文互联网上针对黑人群体的高度固化种族歧视词，'猿'字直接指向猿猴/灵长类动物化比喻。",
            "2. '猩猩''狗狗'进一步强化动物化比喻，形成语言叠加效应。",
            "3. '每天拿它娱乐娱乐'表达了将对象当作玩物的支配态度。",
            "4. 'YD'（阴茎缩写）的加入将攻击升级为性器官层面的侮辱。"
        ],
        "counter_evidence": [
            "1. 从极严格字面看，文本似乎在描述一个虚构的动物杂交场景，没有直接提及任何种族名称。但'猿形毕露'在中文网络中的种族编码已高度固化，反方证据极弱。"
        ],
        "final_rationale": "Risk: high。使用高度固化的种族编码词'猿形毕露'指向黑人群体，叠加动物化/性器官化侮辱，攻击明确、恶意明显。"
    }
    return s

def rev_004318(s):
    s["risk_level"] = "medium"
    s["encoding_primary"] = "D1_反讽"
    s["encoding_secondary"] = ["D3_借代"]
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本假装进行精细的地域分析——将东北三省拆分，声称所有的'杀人放火、打架斗殴、洗脚城女性、海南偷菜'全是黑龙江干的，其他两省无辜。",
            "'洗脚城女性'（足浴店女性）和'海南偷菜'（东北人在海南偷菜的地域梗）是具体的地域负面刻板印象清单——每一种负面标签都被精准甩给黑龙江。"
        ],
        "encoding_analysis": [
            "主编码D1（反讽）：文本表面在'做地域精细化分析'（听起来理性客观），实际意图是将所有对东北的负面印象集中在黑龙江一个省上，是一种反讽式的'甩锅'——'你看问题不在东北，在黑龙江'。",
            "次编码D3（借代）：'杀人放火、打架斗殴、洗脚城女性、海南偷菜'这些具体行为借代（代表）对黑龙江的全面负面评价，用部分借代整体。"
        ],
        "context_analysis": [
            "知乎平台地域讨论中常见'分省甩锅'的反讽句式——把一个区域的负面都归到一个子区域，表面客观实际上地域黑。不需要额外上下文即可识别反讽语气。"
        ],
        "supporting_evidence": [
            "1. '如果我们把三个省拆分来看就会发现'——用'学术化'的句式包装主观甩锅行为，是反讽的标志。",
            "2. 列举的具体负面刻板印象（杀人放火、打架斗殴、洗脚城女性、海南偷菜）全部是有据可查的互联网地域梗。",
            "3. '全都只是黑龙江而已'——'全都'和'而已'的组合轻描淡写地给一省贴上所有负面标签。",
            "4. 被ToxiCN标注为toxic=1且expression=2，确认有隐晦编码。"
        ],
        "counter_evidence": [
            "1. 如果原帖在讨论'东北问题到底出在哪'，这条回复可能是在反讽'选择性归因'这种行为本身，而非真正攻击黑龙江。反讽和地域黑的边界依赖原帖语境。"
        ],
        "final_rationale": "Risk: medium。通过反讽式'精细化分析'和借代手法将黑龙江一省当作东北所有问题的替罪羊，是间接但可识别的地域攻击。"
    }
    return s

def rev_004319(s):
    s["risk_level"] = "low"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "medium"
    s["evidence_strength"] = "weak"
    s["hard_negative"] = False
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "'一丘之路'是成语'一丘之貉'的错别字或变体（貉->路），意为'都是一路货色'。评价对象是抖音、B站、微博三个平台。",
            "文本的核心是说这三个平台是一丘之貉——性质相同、都不是好东西。"
        ],
        "encoding_analysis": [
            "无有效编码机制。'一丘之貉'是普通成语，不在互联网歧视编码体系中。'一丘之路'可能是输入错误或故意改字，但改变后的'路'字不产生新的编码意义。",
            "原标注E1（平台黑话）不当：'一丘之貉'不是任何平台的特定黑话，是普通书面语。"
        ],
        "context_analysis": [
            "贴吧话题为gender_discussion（性别讨论），暗示此评论可能是在批评这三个平台纵容/传播性别对立内容。平台批评本身不是群体攻击。"
        ],
        "supporting_evidence": [
            "1. 文本批评对象是商业平台而非受保护的群体（性别、种族、地域等），不在常见歧视范畴内。",
            "2. '一丘之貉'虽然带有贬义，但针对的是平台，不具有群体攻击性。",
            "3. 无任何性别歧视关键词，与gender_discussion话题的关系是间接的。"
        ],
        "counter_evidence": [
            "1. 原标注为toxic=1且expression=1（直接表达），说明标注者认为有风险。但平台批评与群体歧视不同。",
            "2. 如果'一丘之貉'的'貉'字改为'路'是有意为之，可能是在规避某个自动审核词。但'一丘之貉'本身不是敏感词，改字动机不明。"
        ],
        "final_rationale": "Risk: low。文本批评三个互联网平台为'一丘之貉'，不针对受保护群体，风险来自语境（性别讨论话题）而非文本自身。"
    }
    return s

def rev_004320(s):
    s["risk_level"] = "high"
    s["encoding_primary"] = "literal_keyword"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "strong"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本嘲笑某人（'他'）是同性恋，并用'谁教养他做基佬'暗示同性恋是'教的'（错误的培养结果），加上'真丢人'表达强烈的社会排斥。",
            "'基佬'是中文中对男同性恋的侮辱性称呼（粤语借词'基'来自gay），在互联网用语中带有贬义。"
        ],
        "encoding_analysis": [
            "无编码。'基佬'是直接的侮辱性词汇，没有经过谐音、隐喻等包装。'教养'（教育培养）的用法表达'成为同性恋是被教坏的'这一典型恐同逻辑。",
            "原标注E1/E3编码不当——'基佬'本身就是一个已知的贬义词，不需要平台黑话编码来识别。"
        ],
        "context_analysis": [
            "贴吧反LGBTQ话题，语境清晰。文本直白地表达了对同性恋者的攻击和排斥，不需要额外上下文。"
        ],
        "supporting_evidence": [
            "1. '基佬'是公认的对男同性恋者的侮辱性称呼，属于常见的仇恨言论关键词。",
            "2. '谁教养他做基佬'的逻辑暗示'同性恋是后天教坏的'，这是典型的反LGBTQ叙事框架。",
            "3. '真丢人'明确表达了排斥态度，将同性恋与羞耻直接关联。",
            "4. '笑到肚子痛了'的开场用幸灾乐祸的语气确立全篇的嘲弄基调。"
        ],
        "counter_evidence": [
            "1. 如果发帖人在转述某个具体场景（比如引用他人的原话），则可能是reporting而非本人态度。但句式为第一人称直接表达，转述可能性低。"
        ],
        "final_rationale": "Risk: high。使用侮辱性称呼'基佬'+'真丢人'直接表达反同攻击，是明确、无编码的仇恨言论。"
    }
    return s

def rev_004321(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本劝诫某人不要使用自己不了解的东西，更不要拿出来炫耀，否则会出丑。是一般性的劝告/批评句式。",
            "'喔'是台湾/网络语气词，带有一点善意的警示语气。语气整体不是攻击性的。"
        ],
        "encoding_analysis": [
            "无编码机制。这是日常中文网络交流中的常见劝诫表达，不涉及任何已知的歧视编码、黑话或隐喻。"
        ],
        "context_analysis": [
            "贴吧gender_discussion话题下，可能是在回复某个使用女权术语但用错的人——'自己不知道怎么用的东西'可能指女权相关概念。但文本本身是中性劝告。"
        ],
        "supporting_evidence": [
            "1. 文本是通用性劝诫，没有提及任何受保护群体或使用侮辱性词汇。",
            "2. '喔'的语气缓和了批评的力度，表明说话者不是纯粹的攻击态度。",
            "3. 被ToxiCN标注为toxic=0（非有毒），是hard_negative样本。"
        ],
        "counter_evidence": [
            "1. 在性别讨论话题下，可能被解读为'对使用女权语言的女性的讽刺性劝告'，但文本本身无攻击性。"
        ],
        "final_rationale": "Risk: none (hard_negative)。一般性网络劝诫表达，无攻击性，原始判定正确。"
    }
    return s

def rev_004322(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "叙述者自称是河南南阳人，表示没有感受到某种现象（likely某种地域歧视/负面评价），也没有听别人提过。",
            "'阿'是语气词，相当于'啊'，口语化表达。全文是一个普通用户对自己亲身经历的陈述。"
        ],
        "encoding_analysis": [
            "无编码机制。纯事实陈述，无任何攻击性语言或编码痕迹。"
        ],
        "context_analysis": [
            "知乎地域话题讨论中，南阳人是河南人，本句可能是回应'河南人不好的印象'之类的讨论——本地人表示没感觉。"
        ],
        "supporting_evidence": [
            "1. '我南阳的'是自我介绍身份，用于增强发言的说服力。",
            "2. '没感觉''没听有人说'双重否定，强调未经历/未知所描述的现象。",
            "3. 被ToxiCN标注为toxic=0（非有毒），是hard_negative样本。"
        ],
        "counter_evidence": [
            "1. 无风险证据。这是完全正常的个人陈述。"
        ],
        "final_rationale": "Risk: none (hard_negative)。南阳本地人对地域负面描述的亲身否认，正常人表达，无任何风险。"
    }
    return s

def rev_004323(s):
    s["risk_level"] = "high"
    s["encoding_primary"] = "literal_keyword"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "strong"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本陈述'所以所有同性恋都应该被纠正性取向'。'都该'（都应该）表达了强制性立场——认为同性恋取向是错误且需要被修正的。",
            "'纠正'（correct/fix）的使用暗示同性恋取向是一种'偏差'或'错误'，需要外部干预来'矫正'，这是经典的恐同（homophobic）论述框架。"
        ],
        "encoding_analysis": [
            "无编码。文本是直接的反同主张，没有使用任何谐音、隐喻或包装。'纠正取向'是直白的治疗性语言，完全在字面意义上运作。",
            "原标注D1_反讽不当——这不是反讽（没有字面义与实际态度之间的张力）。这就是说话者的真实态度。"
        ],
        "context_analysis": [
            "贴吧反LGBTQ话题，语境明确。文本本身已足够判断风险等级，不需要额外上下文。"
        ],
        "supporting_evidence": [
            "1. '都该'（全部应该）是绝对性表述，不包含例外，表达了对整个群体的强制立场。",
            "2. '纠正取向'（纠正性取向）借用了'转化疗法'的概念框架，将同性恋病理化。",
            "3. 整句话没有if/but等条件或限定词，是赤裸裸的歧视性主张。",
            "4. 被ToxiCN标注为toxic=1且expression=1（直接表达）——符合直接仇恨言论特征。"
        ],
        "counter_evidence": [
            "1. 如果是在讨论'有些人认为……'的语境中，可能是转述他人观点（reporting）。但句式是断言式而非转述式，可能性极低。"
        ],
        "final_rationale": "Risk: high。直接提出'所有同性恋都应被纠正取向'，是明确的反同主张，无编码，无歧义。"
    }
    return s

def rev_004324(s):
    s["risk_level"] = "medium"
    s["encoding_primary"] = "D1_反讽"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本声称'同性恋现在高贵的很'（现在同性恋很了不起/高高在上）和'真败坏路人缘'（确实破坏了在普通大众中的形象）。",
            "'高贵的很'是明显的反讽——字面说'高贵'实际在批评对方傲慢自大。'败坏路人缘'是网络常用语，指让原本中立的旁观者产生反感。"
        ],
        "encoding_analysis": [
            "主编码D1（反讽）：'高贵的很'是反讽的关键标识——字面为'很高贵'，实际意思是'以为自己了不起'。通过表面的反语来表达对同性恋群体态度高傲的不满。",
            "非编码部分：'真败坏路人缘'是直接的抱怨，不依赖反讽机制，直接表达了'同性恋群体的行为导致公众对他们的反感'的观点。"
        ],
        "context_analysis": [
            "知乎反LGBTQ话题，语境清晰。全文是抱怨同性恋群体的行为损害了公众形象，不需要额外上下文即可判断。"
        ],
        "supporting_evidence": [
            "1. '高贵的很'在日常用语中几乎总是反讽用法（类似'你很高贵哦'），极少字面赞美。",
            "2. '败坏路人缘'将同性恋视为一个整体，指责其行为损害了自身形象——这是对群体的负面概括。",
            "3. 全句结构是先反讽地给出虚假赞美（'高贵的很'），再给出真正的批评（'败坏路人缘'）。"
        ],
        "counter_evidence": [
            "1. 文本的对抗性较温和——用'路人缘'这个娱乐圈/公众形象词汇来讨论社会接受度，更像是抱怨而非仇恨言论。",
            "2. 没有使用侮辱性称呼（如基佬、死同性恋等），表达方式在反同内容中相对克制。"
        ],
        "final_rationale": "Risk: medium。通过反讽表达对同性恋群体行为的不满，有群体负面评价但未使用侮辱性词汇，中度风险。"
    }
    return s

def rev_004325(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "weak"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本表达'每个人都有各自的志向和喜好，为什么要批判别人呢？我不理解'的立场。'人各有志，各有所好'是两个成语的连用，强调个体差异的正当性。",
            "'搞不懂'表达困惑，暗示说话者认为批判他人的选择是没有道理的。"
        ],
        "encoding_analysis": [
            "无编码机制。这是普通的中文日常表达，使用的是标准成语和日常用语，没有任何歧视编码或攻击性修辞。"
        ],
        "context_analysis": [
            "知乎种族话题讨论中，这句话可能是为种族多样性辩护——'每个种族都有其特点，为什么要批判不同种族的人？'。但文本本身是通用的包容立场。"
        ],
        "supporting_evidence": [
            "1. '人各有志，各有所好'是包容/多元主义的经典汉语表达。",
            "2. '为啥要批判'直接质疑歧视/批判行为的合理性。",
            "3. 被ToxiCN标注为toxic=0（非有毒），是hard_negative样本。"
        ],
        "counter_evidence": [
            "1. 无风险证据。这是完全的正常表达。"
        ],
        "final_rationale": "Risk: none (hard_negative)。包容多元的通用表达，无任何风险。"
    }
    return s

def rev_004326(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "high"
    s["evidence_strength"] = "weak"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本说'可行'（方案可行），像杨笠一样有一个'标志物'（标志/标识物）易于分辨。杨笠是知名脱口秀演员，因性别话题争议闻名。",
            "文本在讨论某个'方案'（原帖中的提议），用杨笠作为类比来说明'有个标志物容易识别'——可能指用某个标志性人物/符号来标记某类人。"
        ],
        "encoding_analysis": [
            "无编码机制。提到了杨笠作为类比对象，但不涉及攻击性编码。原标注D2_隐喻不准确——杨笠是真实人物，不是隐喻符号。"
        ],
        "context_analysis": [
            "知乎种族话题背景，但杨笠是性别争议人物。文本高度依赖原帖上下文——不知道'方案'是什么、'标志物'指什么，就无法判断意图。",
            "可能是讨论如何识别某种行为模式/群体，用杨笠作为标签参照。缺乏关键上下文，判断力不足。"
        ],
        "supporting_evidence": [
            "1. '可行'表示赞同某个提案，但提案内容未知。",
            "2. 杨笠是知名公众人物，提及她不一定有恶意。",
            "3. 被ToxiCN标注为toxic=0（非有毒），是hard_negative样本。"
        ],
        "counter_evidence": [
            "1. '有个标志物容易分辨'在特定上下文中可能是'用杨笠当标签来识别和攻击女性/女权主义者'。缺乏语境无法排除这种可能。"
        ],
        "final_rationale": "Risk: none (hard_negative)。高度依赖上下文的模糊表达，在缺乏原帖内容的情况下无法确定存在风险。"
    }
    return s

def rev_004327(s):
    s["risk_level"] = "low"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = False
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "叙述者先称赞对方'写得太好了'（你写的太好了），然后描述了自己在耽美（danmei/男男小说）书评区看到很多人骂同性恋的现象，认为'这个圈子里面的人太可怕了'。",
            "'这个圈子里面的人'指的是那些在耽美书评里骂同性恋的恐同者——叙述者是在批评那些骂人的人，而不是批评同性恋群体。"
        ],
        "encoding_analysis": [
            "无编码机制。文本是直接的reporting，叙述者描述观察到的网络现象，表达对恐同攻击者的不满。",
            "原标注E3（互动/热点触发）不当——没有依赖互动语境触发风险，文本自身是完整的反偏见reporting。"
        ],
        "context_analysis": [
            "知乎反LGBTQ话题标签有误导性——这条文本实际上是批评恐同者的，而不是在传播反LGBTQ内容。评论区比话题标签更能反映内容性质。"
        ],
        "supporting_evidence": [
            "1. '我觉得你写的太好了'是正面的开场，为下文定基调。",
            "2. '底下都会有很多很多的人骂同性恋的'——'骂'字明确表示'攻击/辱骂'，叙述者是在描述攻击行为。",
            "3. '这个圈子里面的人太可怕了'——这里的'圈子'指书评区的攻击者，叙述者对他们感到不安/恐惧。",
            "4. 文本是对网络恐同现象的观察和批评，不是恐同言论本身。"
        ],
        "counter_evidence": [
            "1. 如果没有仔细读'骂同性恋的'这个短语，可能被误读为叙述者本人在骂同性恋。但'骂'在中文中明确是负面评价动词。"
        ],
        "final_rationale": "Risk: low。叙述者在批评耽美书评区里攻击同性恋的人，是反偏见/reporting立场，反转读才是误读。"
    }
    return s

def rev_004328(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本解释为什么一些女孩恐男（恐惧男性）——因为从小和男生接触少。给出的解释是社会学/心理学归因（陌生导致恐惧），不是价值判断。",
            "'可以理解'表达了对这种现象的合理化理解——说话者不认为恐男是非理性的，而是有原因的。"
        ],
        "encoding_analysis": [
            "无编码机制。这是正常的社会现象分析，使用平实的语言，没有攻击性词汇或编码。",
            "原标注E3（互动/热点触发）不适用——文本本身是完整的分析，不依赖外部互动语境。"
        ],
        "context_analysis": [
            "贴吧性别话题中，此句可能回应'为什么有些女性恐男'的提问。是中性/友善的解答，不需要额外上下文。"
        ],
        "supporting_evidence": [
            "1. '可以理解'表达同情/理解而非批评。",
            "2. 给出的原因是客观的成长环境因素（'接触的少'），不是对男性的批评。",
            "3. '好多女孩也恐男'——把恐男描述为常见的、可理解的现象。",
            "4. 被ToxiCN标注为toxic=0（非有毒），是hard_negative样本。"
        ],
        "counter_evidence": [
            "1. 无风险证据。正常的社会心理学解释。"
        ],
        "final_rationale": "Risk: none (hard_negative)。对女性恐男现象的中立社会学解释，无攻击性或偏见。"
    }
    return s

def rev_004329(s):
    s["risk_level"] = "medium"
    s["encoding_primary"] = "D2_隐喻"
    s["encoding_secondary"] = ["D1_反讽"]
    s["needs_context"] = False
    s["ambiguity"] = "medium"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本为春晚一个被认为是性别歧视的节目辩护：说节目是好段子、'我身边的正常女性没觉得被冒犯'，然后质问'怎么就有人对号入座石砸狗叫了呢'。",
            "'对号入座'（taking it personally）+'石砸狗叫'（狗被石头砸中了才叫，比喻只有被说中了才会跳脚）——这两个词组合起来的意思是：那些觉得被冒犯的女性，是因为她们'被说中了'。"
        ],
        "encoding_analysis": [
            "主编码D2（隐喻）：'石砸狗叫'是一个完整的隐喻——'石头'比喻讽刺内容，'狗'比喻被讽刺到而跳脚的人，'叫'比喻抗议。通过这个隐喻，将女性抗议者比作'乱叫的狗'。",
            "次编码D1（反讽）：表面在'夸节目好/讲道理'，实际通过'正常女性'与'对号入座者'的二分法，将抗议的女性排除在'正常'范畴之外，是反向攻击。"
        ],
        "context_analysis": [
            "贴吧性别话题，这是性别对立中常见的辩护策略：'好的部分是好的，对你没恶意，你以为在说你是因为你心虚'。石砸狗叫是该策略的集中体现。"
        ],
        "supporting_evidence": [
            "1. '我身边的正常女性没觉得被冒犯'——用'正常女性'这一标签暗示抗议的女性'不正常'，是典型的分化策略。",
            "2. '石砸狗叫'是整个文本的修辞重心——狗被石头砸中的比喻将抗议者降格为动物/非理性存在。",
            "3. '对号入座'（自我代入被批评角色）+'石砸狗叫'（叫=抗议）构成逻辑闭环：抗议者=被说中的人=狗。"
        ],
        "counter_evidence": [
            "1. '石砸狗叫'在某些语境中可作无恶意的惯用语使用，不一定指对方是狗。但结合'对号入座'和性别对抗语境，恶意的可能性大。",
            "2. 文本为单条评论，缺乏原帖（节目本身）的内容，无法独立判断节目是否确实含有性别歧视。"
        ],
        "final_rationale": "Risk: medium。通过'石砸狗叫'的动物隐喻将女性抗议者比作狗，用'正常女性'标签分化女性群体，是间接但系统性的性别贬低。"
    }
    return s

def rev_004330(s):
    s["risk_level"] = "high"
    s["encoding_primary"] = "literal_keyword"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "strong"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本说'原来ln（某个账号/平台的缩写）的受众是穆狗啊'。'穆狗'是'穆斯林狗'的缩写——将穆斯林群体称为狗，是极端的宗教仇恨言论。",
            "'ln'可能指某个主播、UP主或平台的缩写，无法确定具体指代。"
        ],
        "encoding_analysis": [
            "主编码literal_keyword：'穆狗'是对穆斯林群体的直接侮辱性称呼，'穆'取自'穆斯林'的前缀，'狗'是动物化贬损。这不是编码而是直接攻击。",
            "原标注E1（平台黑话）不当：'穆狗'不是平台内部的特定黑话编码，而是公开的宗教侮辱词。"
        ],
        "context_analysis": [
            "贴吧性别话题标签可能不准（更像是宗教仇恨话题），但文本自身已足够判断：将某群体称为'狗'在任何语境下都是明确的仇恨言论。"
        ],
        "supporting_evidence": [
            "1. '穆狗'是'穆斯林狗'的简称，在中文网络中是公认的宗教仇视词（类比'X狗'结构：台狗、港狗、日狗等群体污名化命名法）。",
            "2. '原来……是……啊'句式表达了'意料之中的发现'——'ln的受众是穆狗'暗示听众是该群体，降格为'狗'。",
            "3. 即使不知道'ln'的具体指代，'穆狗'一词本身即构成完整的宗教攻击。"
        ],
        "counter_evidence": [
            "1. 如果'穆'是对某个词（比如某种缩写/网名）的无关联引用而非指穆斯林，则'穆狗'可能不是宗教蔑称。但常规用法中'穆'字单独出现时几乎总是指穆斯林。"
        ],
        "final_rationale": "Risk: high。使用侮辱性词汇'穆狗'（穆斯林狗）直接表达宗教仇恨，编码为literal_keyword，风险明确不可否认。"
    }
    return s

def rev_004331(s):
    s["risk_level"] = "high"
    s["encoding_primary"] = "literal_keyword"
    s["encoding_secondary"] = ["E1_平台黑话"]
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "strong"
    s["hard_negative"] = False
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本说'这个男的可能是有绿帽癖'。'绿帽'（green hat）在中文里指'被戴绿帽子'（伴侣出轨），'pi'是'癖'（fetish/obsession）的缩写。",
            "'绿帽pi'（绿帽癖）在互联网用语中用于嘲讽男性，指他喜欢或习惯被出轨，或他的伴侣出轨。是一种性羞辱（sexual humiliation）式攻击。"
        ],
        "encoding_analysis": [
            "主编码literal_keyword：'绿帽癖'是一个直接攻击性词汇，羞辱男性的性际遇/婚姻状况。",
            "次编码E1（平台黑话）：'绿帽pi'中的'pi'是网络拼音缩写习惯（癖->pi），在贴吧等社区中常见。但整体已泛化为通用网络侮辱词，不完全是平台黑话。",
            "'绿帽'本身是文化隐喻（绿色帽子的典故），但在当前用法中已高度固化，更像直接侮辱而非隐喻。"
        ],
        "context_analysis": [
            "贴吧性别话题，针对个体的性羞辱。目标性别（男）和攻击性质（性羞辱）均明确，不需要额外上下文。"
        ],
        "supporting_evidence": [
            "1. '恐怕是'表面是推测语气，但在攻击性语境中实为断定+嘲讽。",
            "2. '绿帽癖'直接指控该男性被伴侣出轨，是严重的性际遇羞辱。",
            "3. 在性别讨论话题中，用性羞辱攻击个体是常见的性别对抗策略。"
        ],
        "counter_evidence": [
            "1. 如果'绿帽pi'是在泛泛讨论某类网络现象/persona而非针对真实个体，攻击性会降低。但核心句式'这男的恐怕是……'强指真实个体。"
        ],
        "final_rationale": "Risk: high。使用'绿帽癖'对个体实施性羞辱式攻击，语言直白、侮辱性强。"
    }
    return s

def rev_004332(s):
    s["risk_level"] = "medium"
    s["encoding_primary"] = "D1_反讽"
    s["encoding_secondary"] = ["D2_隐喻"]
    s["needs_context"] = True
    s["ambiguity"] = "medium"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本假装认真地在给Derek Chauvin（用膝盖压死George Floyd的警察）封'超级英雄'称号——'黑膝侠、美国队长、铁腿超人'。",
            "'黑膝侠'（Black-Knee Hero化用了Black Panther+膝盖压杀）/'美国队长'（Captain America但Chauvin是白人警察）/ '铁腿超人'（Iron Leg Man化用Iron Man）——每个称号都讽刺性地关联了Chauvin的杀人行为。"
        ],
        "encoding_analysis": [
            "主编码D1（反讽）：整段文本是典型的反讽——字面上在'赞颂'Chauvin为英雄，实际在揭露和嘲弄种族主义暴力执法的荒谬性。'封神'（被奉为神）一词是反讽的明确标记。",
            "次编码D2（隐喻）：用超级英雄/漫画符号来隐喻警察暴力执法中的角色转换——杀人者被塑造成'英雄'，讽刺社会对警察暴力的美化。"
        ],
        "context_analysis": [
            "知乎种族话题，讨论的是美国警察暴力（Floyd事件）。需要知道Floyd事件和Chauvin案的背景才能理解讽刺指向，但不需要额外的原帖上下文。",
            "文本是自由派/左派式的反讽批评（讽刺警察暴力和种族主义），并非在传播种族歧视。"
        ],
        "supporting_evidence": [
            "1. '众所周知'的反讽用法——'众所周知'后面跟的是主观恶搞结论，与'众所周知'的客观义形成反差。",
            "2. '封神'和'称号'构建了一个虚假的'封神仪式'框架来反讽。",
            "3. '黑膝侠'直接指向'膝盖压颈'（Chauvin的杀人方式），'铁腿超人'也指腿/膝。",
            "4. 这种反讽英雄命名是中文互联网上常见的政治评论手法。"
        ],
        "counter_evidence": [
            "1. 反讽在文本中无法被自动系统可靠识别——如果不了解Floyd事件，'黑膝侠'等可能被误读为直接的英雄崇拜。",
            "2. 反讽修辞在跨文化/跨语境传播中可能失效，被接收为字面意义的种族正义吹捧。"
        ],
        "final_rationale": "Risk: medium。通过反讽超级英雄命名体系批评警察暴力和种族主义，是揭露性/批评性表达而非传播歧视，但反讽有被误读的可能。"
    }
    return s

def rev_004333(s):
    s["risk_level"] = "high"
    s["encoding_primary"] = "literal_keyword"
    s["encoding_secondary"] = ["C5_概念替换"]
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "strong"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本将某群体定义为'原始人的一种'并且是'未经进化和淘汰的'——明确宣称该群体进化不完全、是原始人类的遗留。",
            "'未经进化和淘汰'使用了社会达尔文主义的语言框架——暗示该群体在'自然选择'中本应被淘汰但未被淘汰。"
        ],
        "encoding_analysis": [
            "主编码literal_keyword：直接使用'原始人''进化''淘汰'等进化论术语进行种族贬低，属于直接攻击而非编码表达。",
            "次编码C5（概念替换）：将进化论/社会达尔文主义的概念框架借用（abuse）到群体评价中——把生物学概念'进化'和'淘汰'替换到社会/种族评论中。"
        ],
        "context_analysis": [
            "贴吧种族话题，目标为黑人群体（原始人/进化不全是针对黑人的经典种族主义叙事）。不需要额外上下文即可判断。"
        ],
        "supporting_evidence": [
            "1. '原始人'在种族歧视话语中常用于贬低非白人族群（认为其落后、未开化、进化不全）。",
            "2. '未经进化和淘汰'精准对应19世纪社会达尔文主义种族理论——白人是进化的，其他种族是'活化石'。",
            "3. '一种'（一种原始人）的分类学口吻，假装在科学分类以增加'客观性'。",
            "4. 被ToxiCN标注为toxic=1且expression=1（直接表达），确认高风险。"
        ],
        "counter_evidence": [
            "1. 如果是讨论某个具体人类的原始部落（如亚马逊雨林中的与世隔绝部落），可能不是种族歧视而是事实描述。但topic=race_discussion和内容中无具体指向，泛泛而谈的可能性更高。"
        ],
        "final_rationale": "Risk: high。使用进化论话语框架将某群体贬低为'原始人'和'未经淘汰'的劣等人，是经典的种族主义语言。"
    }
    return s

def rev_004334(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本讨论人造子宫（artificial womb）技术的潜在好处：可以选择后代血统、配合基因剪接技术可以自定义后代特征、使人类全方位进步。",
            "是典型的技术乐观主义发言，讨论未来科技可能的社会影响。"
        ],
        "encoding_analysis": [
            "无编码机制。这是正常的技术/社会讨论，使用标准的科技词汇和未来主义表述，没有任何攻击性语言或歧视编码。"
        ],
        "context_analysis": [
            "贴吧性别话题标签可能是误标——内容根本不涉及性别攻击，而是科技讨论。可能原因是人造子宫话题被关联到性别/女权讨论（人工子宫替代女性生育功能）。"
        ],
        "supporting_evidence": [
            "1. '好东西啊'表达了正面态度。",
            "2. '令人类在全方位更进一步'总体是乐观预测。",
            "3. 完全围绕科技工具的潜在应用展开，没有任何针对个人的攻击或评价。",
            "4. 被ToxiCN标注为toxic=0（非有毒），是hard_negative样本。"
        ],
        "counter_evidence": [
            "1. '选择血统'的表述略带优生学色彩，但这是常见的人工子宫讨论中的伦理思考框架，不构成攻击。"
        ],
        "final_rationale": "Risk: none (hard_negative)。未来科技讨论，中性语言，无攻击性。"
    }
    return s

def rev_004335(s):
    s["risk_level"] = "high"
    s["encoding_primary"] = "literal_keyword"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "strong"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本断言和黑人生孩子的中国女性（'国女'）大概率会社会性死亡（社死）。'\U0001f923\U0001f923'表达幸灾乐祸。",
            "这句的恶意是双重的：一是对黑人群体的歧视（'给黑人生孩子=社死'暗示黑人是不应该与之生育的低等群体）；二是对与黑人交往的中国女性的污名化和威胁。"
        ],
        "encoding_analysis": [
            "主编码literal_keyword：'给黑人生孩子'直接点明种族，'社死'是社会性死亡的直接断言。没有使用隐喻或反讽，是直接的威胁性言论。",
            "'国女'（中国女性）和'黑人'（Black people）都是直白的身份标签。"
        ],
        "context_analysis": [
            "知乎种族话题，此评论针对的是中国女性和黑人的跨种族关系。不需要额外上下文即可判断这是种族歧视内容。"
        ],
        "supporting_evidence": [
            "1. '给黑人生孩子'将'黑人'作为贬低标记——生孩子>社死的因果链暗示黑人是不可接受的伴侣/生育对象。",
            "2. '基本上……大概率'双重概率词构建了一个'不可避免的'负面后果（社会性死亡）。",
            "3. '\U0001f923\U0001f923'表情符号表达对预测后果的幸灾乐祸/快感。",
            "4. 这种叙事在中文互联网上被归类为'easy girl羞辱'的变体——专门攻击与黑人交往的中国女性。"
        ],
        "counter_evidence": [
            "1. 说话者可能认为自己是在'善意警告'跨种族关系的现实社会压力，而非表达个人歧视。但'\U0001f923\U0001f923'表明态度是幸灾乐祸而非同情。"
        ],
        "final_rationale": "Risk: high。将'与黑人生孩子'与'社会性死亡'直接挂钩，双重污名化黑人和跨种族关系中的中国女性。"
    }
    return s

def rev_004336(s):
    s["risk_level"] = "high"
    s["encoding_primary"] = "literal_keyword"
    s["encoding_secondary"] = ["D2_隐喻"]
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "strong"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本引用并赞同了一句极端厌女言论：'外面要只四条腿走路的猪可能难找，两条腿的女人满街都是'（外面要找一只四条腿的猪可能难找，但两条腿的女人满大街都是）。",
            "引文将女人直接比作猪——而且是比猪更低等（因为猪'难找'而女人'满街都是'，暗示女人比猪更廉价/更容易获取）。叙述者补充'绝大多数猪都在圈里真不会放出来到处跑'——把'大多数女人应该在圈里待着不要到处跑'的价值观也放进来了。"
        ],
        "encoding_analysis": [
            "主编码literal_keyword：虽然用了比喻形式，但'女人=猪'的比喻在中文厌女话语中如此常见和固化，以至于几乎等于直接辱骂。'满街都是'的表达进一步将女性商品化。",
            "次编码D2（隐喻）：隐喻'女人属于圈里（家庭）不应该到处跑'——'猪在圈里'是女性应该被限制在家庭空间的主张的隐喻表达。"
        ],
        "context_analysis": [
            "知乎种族话题可能为误标——此文本明显是性别歧视而非种族歧视。在种族话题中出现可能是原帖讨论跨种族关系（如黑人+中国女性），但文本本身攻击的是女性整体。"
        ],
        "supporting_evidence": [
            "1. '竟然无法反驳'表明叙述者接受了这个厌女比喻为'有道理'的。",
            "2. '绝大多数猪都在圈里真不会放出来到处跑'——将女人比作应该在圈里待着的猪，主张对女性的空间限制。",
            "3. '两条腿的女人满街都是'将女性商品化/贬值为易得的低价值存在。",
            "4. 这是中文互联网上流传的经典厌女段子，具有高度恶名。"
        ],
        "counter_evidence": [
            "1. 文本声称是转述'竟然无法反驳'——可能是转述他人段子而非自创，但赞同态度明确。"
        ],
        "final_rationale": "Risk: high。将女性比作比猪更低等/易得的生物，并主张限制女性活动空间，是极端明确的厌女攻击。"
    }
    return s

def rev_004337(s):
    s["risk_level"] = "medium"
    s["encoding_primary"] = "D1_反讽"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "high"
    s["evidence_strength"] = "weak"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "两个连续反问句：'你觉得我什么不行呢？'（你认为我哪方面不够好？）和'你觉得种族歧视是个贬义词？'（你认为种族歧视是个负面词汇吗？）。",
            "第二个问题暗含一种挑衅——质疑种族歧视是否真的是负面的，暗示种族歧视可能不必然是坏东西。"
        ],
        "encoding_analysis": [
            "主编码D1（反讽）：第二个反问句'你觉得种族歧视是个贬义词？'是反讽——表面在问一个荒谬的问题（种族歧视当然是贬义词），实际在表达'我不同意种族歧视是贬义词/不好的东西'。",
            "反讽的机制：通过问一个'答案显而易见的问题'来暗示相反的立场。类似'你觉得太阳是从西边出来的吗？'——提问本身即表明对该立场的否定。"
        ],
        "context_analysis": [
            "知乎种族话题中，这两句话可能是对某个批评的回应——对方批评了发帖人，然后发帖人反问'你是觉得我水平不行还是觉得种族歧视不对？'。高度依赖原帖对话链。"
        ],
        "supporting_evidence": [
            "1. 第二个反问句'你觉得种族歧视是个贬义词？'在中文修辞中几乎必然被解读为对'种族歧视是贬义词'这一共识的质疑/挑战。",
            "2. 两个反问句连用，语气具有对抗性——不是寻求信息而是在反攻。"
        ],
        "counter_evidence": [
            "1. 完全可能是在反讽对方——意思是'你连种族歧视是贬义词这种基本常识都要质疑吗？'，即在批评对方。但语意模糊度极高。",
            "2. 缺乏原帖对话链，无法确定两只反问句各自的对象。第一种解读（质疑者自己支持种族歧视）和第二种解读（质疑者在反讽对方）在双反问句中都无法排除。"
        ],
        "final_rationale": "Risk: medium（不确定性高）。核心风险来自第二个反问句对'种族歧视是贬义词'这一共识的潜在挑战，但高度依赖上下文，存在反讽性批评对方的合理解读。"
    }
    return s

def rev_004338(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "high"
    s["evidence_strength"] = "weak"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本说某件事是'霸凌和不完整的家庭氛围造成的'。给出了一个两因解释：校园欺凌（霸凌）和家庭结构不完整。",
            "句子不完整——缺少主语（什么是由霸凌和家庭氛围造成的）。在LGBT话题中，可能是讨论'同性恋造成的'这也是常见的反同归因。但文本本身没有明确说出来。"
        ],
        "encoding_analysis": [
            "无编码机制。这是一个不完整的因果陈述句，本身不含攻击性语言或编码。攻击性取决于隐含的主语是什么。"
        ],
        "context_analysis": [
            "知乎LGBT话题中，'霸凌和不完整的家庭氛围造成的'很可能是反同言论——将同性恋归因于童年创伤和家庭问题。但文本本身没有点明主语。高度依赖原帖上下文。"
        ],
        "supporting_evidence": [
            "1. 文本被标注为toxic=0（非有毒），ToxiCN也认为无风险。",
            "2. 句子本身不含任何攻击性词汇或侮辱。"
        ],
        "counter_evidence": [
            "1. 在反LGBTQ语境中，'霸凌''不完整的家庭氛围'是常见的'同性恋成因'负面归因框架，如果补充主语'同性恋'则变成反同言论。但文本就是没有说出这个词。"
        ],
        "final_rationale": "Risk: none (hard_negative)。不完整的因果句，缺乏主语，本身无攻击性。语境暗示可能指向反同归因但文本未明确，不宜判高风险。"
    }
    return s

def rev_004339(s):
    s["risk_level"] = "medium"
    s["encoding_primary"] = "literal_keyword"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本列举了一系列贴吧社区（沙湖清真食品吧、我是回族吧、回民贴吧吧、伊斯俩目吧），然后说'加入反同'（加入反对同性恋的阵营）。",
            "这是一个号召：通过排列这些宗教/民族文化贴吧来暗示——这些社群都支持反同立场。这是对反同立场的背书和招募行动。"
        ],
        "encoding_analysis": [
            "主编码literal_keyword：'反同'（anti-gay）是直接的立场声明，没有任何编码包装。'加入反同'是明确的号召行动。",
            "列举的贴吧名称都是标准的社区名称，无编码。原标注D1_反讽和D4_双关均不适用——没有反讽或双关的证据。"
        ],
        "context_analysis": [
            "贴吧反LGBTQ话题。文本通过在社群列表后接'加入反同'的方式，将宗教/民族社群与反同立场关联，暗示这些社群普遍反同。不需要额外上下文。"
        ],
        "supporting_evidence": [
            "1. '支持:'开头——确立'我支持以下内容'的背书框架。",
            "2. 列出的贴吧全部与伊斯兰/回族有关（清真食品、回族、伊斯俩目），暗示伊斯兰社群的反同立场。",
            "3. '加入反同'是明确的行动号召——'加入反对同性恋的队伍'。",
            "4. 被ToxiCN标注为toxic=1且expression=1（直接表达）。"
        ],
        "counter_evidence": [
            "1. 文本可能是在描述'这些贴吧加入了反同阵营'（reporting）而非号召加入。但缺少reporting标志词（如'据说''听说'），更可能是立场声明。"
        ],
        "final_rationale": "Risk: medium。明确的反同立场声明和号召，但主要风险在于态度而非极端辱骂——没有使用侮辱性词汇，是立场表达。"
    }
    return s

def rev_004340(s):
    s["risk_level"] = "medium"
    s["encoding_primary"] = "C4_典故/物品/符号借用"
    s["encoding_secondary"] = ["D2_隐喻"]
    s["needs_context"] = True
    s["ambiguity"] = "medium"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = False
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本将民主党的'和平演变'策略比作'葵花宝典'（金庸小说中的武功秘籍，练习需自宫），然后说美国国内一堆破事，'把自己切了让别人死'（自残式攻击他人）。结尾评价'典型的又蠢又坏'。",
            "'葵花宝典'在原著中的特征：要练神功先自宫（付出巨大代价=自宫才能获得力量）。用在这里精准对应民主党政策的'自损八百伤敌一千'的特征。"
        ],
        "encoding_analysis": [
            "主编码C4（典故借用）：'葵花宝典'是金庸小说的虚构秘籍，被借用来评论美国政治——用小说的'自宫'典故比喻政策的自我伤害性。",
            "次编码D2（隐喻）：'把自己切了让别人死'（把自己切了让别人死）是隐喻——不是真的自残，而指自我破坏性政策。'又蠢又坏'收尾是直接评价。"
        ],
        "context_analysis": [
            "知乎种族话题但内容明显更偏向美国政治评论。文本攻击对象是民主党/美国政策而非种族群体，风险在于政治攻击的尖锐程度。"
        ],
        "supporting_evidence": [
            "1. '葵花宝典'典故使用巧妙——'自宫'隐喻完美对应'自我破坏'的政策效果。",
            "2. '把自己切了让别人死'是暴力意象——虽然不是字面暴力但有攻击性。",
            "3. '典型的又蠢又坏'是直接的负面评价（蠢=愚蠢，坏=恶劣）。"
        ],
        "counter_evidence": [
            "1. 攻击对象是美国政党和政策，不是受保护群体（种族/性别/宗教等）。政治批评的尖锐程度与仇恨言论的标准不同。",
            "2. '葵花宝典'虽带'自宫'的暴力意象，但在中文网络评论中是常见的反讽修辞，不必然越界为仇恨言论。"
        ],
        "final_rationale": "Risk: medium。使用金庸小说典故（葵花宝典/自宫）隐喻美国民主党政策为'自残伤敌'，修辞尖锐但攻击对象是政治实体而非受保护群体。"
    }
    return s

def rev_004341(s):
    s["risk_level"] = "low"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "medium"
    s["evidence_strength"] = "weak"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本表达了一种不满：中国男人没变（'还是那样的中国男人'），但中国女人变了（'已经不是那样的中国女人了'），然后主张公平——'你能变我也能变'。",
            "核心逻辑：女性发生了变化（指向现代社会中对女性角色的重新定义）而男性没有相应变化，导致了某种不平衡。说话者要求'公平'需要变化也是对等的。"
        ],
        "encoding_analysis": [
            "无有效编码机制。文本是直白的性别关系评论，不使用隐喻或反讽。'那样的'是模糊指代——依赖于对话语境中已定义的'那样的'具体属性。",
            "原标注D2_隐喻不适用——'中国男人''中国女人'是字面引用，不是隐喻。"
        ],
        "context_analysis": [
            "知乎种族话题标签可能为误标（应是gender/性别话题）。原帖可能讨论了男女在某个问题上的不同态度或行为模式。需要知道'那样的'指什么才能做精确判断。"
        ],
        "supporting_evidence": [
            "1. '凡事讲究一个公平'——说话者使用了公平/对等的话语框架，而不是直接的攻击。",
            "2. 没有使用任何侮辱性词汇（如直男癌、拳师、龟男等常见的性别对抗标签）。",
            "3. '你也变我也能变'表达的是对称变化的诉求而非单方面贬低。"
        ],
        "counter_evidence": [
            "1. '中国男人还是那样的中国男人'带有'中国男人落伍/不思进取'的贬义。具体的贬义程度取决于'那样的'在语境中的定义。",
            "2. '中国女人已经不是那样的中国女人了'可能隐含'中国女人变坏了/失去了传统美德'的判断。"
        ],
        "final_rationale": "Risk: low。评论中国性别角色变化，表达不对等变化的不满，语言克制无侮辱词，主要风险来自话题敏感性。"
    }
    return s

def rev_004342(s):
    s["risk_level"] = "medium"
    s["encoding_primary"] = "A2_拼音缩写"
    s["encoding_secondary"] = ["D1_反讽"]
    s["needs_context"] = False
    s["ambiguity"] = "medium"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本讽刺同性恋者（'txl'）擅长'复制粘贴'（复印+复制+粘贴）知乎的文章来否定正常人的智商，然后说'就那两个赞的文章谁信谁才智商有问题'。",
            "'复印'（copy-paste）是讽刺性的'赞美'——'你们txl的copy-paste能力真强'。'正常人'（normal people）的使用将同性恋者排除在'正常'之外。"
        ],
        "encoding_analysis": [
            "主编码A2（拼音缩写）：'txl'是'同性恋'的拼音首字母缩写（tong xing lian）。在中文互联网中，'txl'是加密/缩略地指代同性恋群体的常见方式。",
            "次编码D1（反讽）：'复印还得是你们txl厉害'表面是夸赞（'复印还得是你们厉害'=你们复印最厉害），实际是讽刺对方只会复制粘贴没有原创性。"
        ],
        "context_analysis": [
            "贴吧反LGBTQ话题。文本讽刺同性恋者只会复制粘贴知乎文章，暗示他们没有独立思考能力。不需要额外的对话上下文即可判断。"
        ],
        "supporting_evidence": [
            "1. 'txl'是'同性恋'的拼音缩写（A2编码），需要解码才能明确指向。",
            "2. '复印'被用作讽刺性赞美——'你们这方面最强'实际在讽刺。",
            "3. '正常人的智商'将同性恋者与'正常人'对立——暗示同性恋者不正常、智商有问题。",
            "4. '就那两个赞的文章'贬低对方引用的来源质量。"
        ],
        "counter_evidence": [
            "1. 'txl'也可能被解读为其他含义的缩写（如贴在东西/同学录等），但在LGBT话题下同性恋是唯一的合理解读。",
            "2. 文本的嘲讽主要指向对方的论证方式（copy-paste）而非性取向本身，但'txl'和'正常人'的二分法将攻击延伸到了群体层面。"
        ],
        "final_rationale": "Risk: medium。通过'txl'（A2拼音缩写）编码指代同性恋者，用'复印'反讽和'正常人'的二分法实施群体贬低。"
    }
    return s

def rev_004343(s):
    s["risk_level"] = "low"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本说'看她会不会用一些女权最喜欢用的词，下头、直男癌之类的'——建议观察某位女性的用词来判断她是否为女权主义者。",
            "'下头'（网络用语=让人感到扫兴/下头）和'直男癌'（直男癌，对直男/直男癌的批评词）被列举为女权'最喜欢用的词'。"
        ],
        "encoding_analysis": [
            "无编码机制。文本是字面描述——列举网络用语并归因于女权群体。'下头'和'直男癌'虽然是网络特定用语，但此处是引用它们作为'女权常用语清单'，而非使用这些词本身攻击人。"
        ],
        "context_analysis": [
            "贴吧性别话题，可能是在讨论如何识别女权主义者/'拳师'（通过用词判断）。语气偏向群体观察/social spotting而非直接攻击。"
        ],
        "supporting_evidence": [
            "1. '看她会不会用'是观察/测试的框架——'看她是否使用某类词汇'。",
            "2. '女权最喜欢用的词'虽然有刻板印象化嫌疑但不直接攻击。",
            "3. '下头'和'直男癌'在此处是作为元语言讨论的例句被引用，不是用于攻击。"
        ],
        "counter_evidence": [
            "1. '女权最喜欢用的词'可以解读为'女权群体的标志性用语'，暗含'用这些词的人就是女权'的贴标签行为。",
            "2. 将女权主义简化/归约为几个流行词汇的测试是一种轻蔑的简化。"
        ],
        "final_rationale": "Risk: low。在元语言层面讨论女权常用词汇以识别女权群体，有刻板印象化但无直接攻击。"
    }
    return s

def rev_004344(s):
    s["risk_level"] = "high"
    s["encoding_primary"] = "literal_keyword"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "strong"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本宣称'艾滋病是黑皮搞出来的'（AIDS was created by dark-skins），说'他们以得艾滋病为荣'，主张'支持他们在非洲大陆勇于传播艾滋病'。",
            "'黑皮'（dark-skin）是中文互联网上对黑人的贬义称呼。全文构建了一个完整的种族主义叙事：黑人=艾滋病制造者=以传播艾滋病为荣=需要通过传播'净化'同族。"
        ],
        "encoding_analysis": [
            "主编码literal_keyword：'黑皮'是已知的对黑人的贬义称呼。'艾滋病'（AIDS）被用作污名化工具。整段没有使用任何编码包装——是直接、赤裸的种族攻击。",
            "原标注C4（典故/符号借用）不准确——没有借用典故或符号，'艾滋病'和'黑皮'都是字面直接使用。"
        ],
        "context_analysis": [
            "知乎种族话题，文本明确攻击黑人群为艾滋病来源和传播者。不需要额外上下文即可判断为极端种族主义。"
        ],
        "supporting_evidence": [
            "1. '黑皮'（dark-skin）是中文互联网上针对黑人群体的贬义称呼（皮=皮肤）。",
            "2. '艾滋病是黑皮搞出来的'——将传染病起源归咎于特定种族，是种族主义的经典叙事框架。",
            "3. '他们以得艾滋病为荣'——虚构群体态度来增强负面形象，是刻板印象强化的典型方法。",
            "4. '他们致力于感染每一个没有艾滋病的族人'——使用'他们'构建'我们vs他们'的对立，将黑人刻画为刻意传播疾病的威胁。"
        ],
        "counter_evidence": [
            "1. 文本没有任何反方证据——语言太过于直接和系统化，无法合理解读为非歧视性内容。"
        ],
        "final_rationale": "Risk: high。极端种族主义文本，将艾滋病归咎于黑人并虚构'以传播疾病为荣'的刻板印象，无编码、无歧义。"
    }
    return s

def rev_004345(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "叙述者陈述自己的家庭背景——爷爷和叔叔都是阿訇（伊斯兰教的宗教领袖/imam），然后补充'不过我不信教'（但是我不信教）。",
            "这是一句个人背景介绍，逻辑：虽出生在伊斯兰教家庭（家族有宗教领袖），但本人不信仰宗教。"
        ],
        "encoding_analysis": [
            "无编码机制。'阿訇'是标准中文对伊斯兰教领袖的称呼（来自波斯语akhund），不是编码词汇。全文是个人家庭背景的事实陈述。"
        ],
        "context_analysis": [
            "知乎地域话题（region_discussion）可能不准确——更像是宗教/文化话题。但不影响判断——文本无攻击性。"
        ],
        "supporting_evidence": [
            "1. '我爷爷叔叔都是阿訇'——身份背景的事实陈述，无评价。",
            "2. '不过我不信教'——用'不过'转折，表明说话者与家庭宗教传统保持距离，是个人选择声明。",
            "3. 被ToxiCN标注为toxic=0（非有毒），是hard_negative样本。"
        ],
        "counter_evidence": [
            "1. 无风险证据。完全是正常的个人背景介绍。"
        ],
        "final_rationale": "Risk: none (hard_negative)。个人家庭背景和宗教信仰的事实陈述，无任何攻击性或风险。"
    }
    return s

def rev_004346(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本在纠正某个说法：'蛤？他明明黑的是广西好吧？'（Huh? He's clearly making fun of Guangxi, OK?）。",
            "'黑'（black）在此处是网络用语的'黑=讽刺/批评/抹黑'（如'黑某人'=to disrespect someone），不是种族指涉。说话者在纠正关于地域歧视对象的事实错误。"
        ],
        "encoding_analysis": [
            "无编码机制。'黑某人'（to diss someone）是常见的网络动词用法（来自'黑'的引申义：抹黑/批评），不是歧视编码。原标注E3或D1编码均不适用。"
        ],
        "context_analysis": [
            "知乎地域话题，有人在讨论/否定某个地域黑现象，此回复在纠正对象（不是A是广西）。是在meta层面讨论地域歧视的指向，而非实施歧视。"
        ],
        "supporting_evidence": [
            "1. '蛤？'（huh?）表达诧异/质疑，用于反驳某个不准确的表述。",
            "2. '明明……好吧'（clearly...OK?）——'明明'强调事实明显性与对方的错误。",
            "3. '黑的是广西'的'黑'是网络动词用法（抹黑/讽刺），不是名词。",
            "4. 被ToxiCN标注为toxic=0（非有毒），是hard_negative样本。"
        ],
        "counter_evidence": [
            "1. 如果缺乏原帖上下文，'黑的是广西'可能被孤立地误解为'说广西坏话'。但全文在讨论他人言论的对象，不在传播歧视。"
        ],
        "final_rationale": "Risk: none (hard_negative)。在元语言层面纠正地域歧视对象的归属，本身不参与歧视。"
    }
    return s

def rev_004347(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = True
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "该长评论分析河南在互联网上的负面形象问题：承认'河南有一些问题'和确实存在亲身体验形成的负面印象，但建议不要用历史/文化成就来反驳歧视（这没用），而是客观面对。",
            "叙述者是河南人（'我已经很久没有碰到人歧视我了'，'希望以后会越来越好'）——从亲历者角度讨论地域歧视。提到西北地区时说'我就不奢望了'，幽默地自嘲某些地区改变更慢。"
        ],
        "encoding_analysis": [
            "无编码机制。全文是理性、深度的地域歧视社会现象分析，使用标准书面语言，没有任何攻击性表达或编码。",
            "原标注为none/无编码，此判断正确。"
        ],
        "context_analysis": [
            "知乎地域讨论，这是典型的反地域黑/亲历者分享。不需要额外上下文。"
        ],
        "supporting_evidence": [
            "1. 叙述者从亲历者（河南人）角度分析，'我已经很久没有碰到人歧视我了'证明了个人体验。",
            "2. '有人说两个河南骗子，形成了刻板印象，你给他说河南历史悠久，你觉得有用没？'——理性分析刻板印象的心理机制，而不是为歧视辩护。",
            "3. '希望以后会越来越好'表达正向期望。",
            "4. 被ToxiCN标注为toxic=0（非有毒）。"
        ],
        "counter_evidence": [
            "1. 有人可能将'河南有一些问题'解读为承认负面刻板印象的真实性，但这是站在亲历者角度的事实描述（任何地方都有问题），不是煽动歧视。"
        ],
        "final_rationale": "Risk: none (hard_negative)。河南人从亲历者角度对地域歧视的社会分析，理性、有洞察力、反偏见。"
    }
    return s

def rev_004348(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本表达对'抵制地域黑从我做起'这一倡议的支持：说自己不知道能否做到、能做到多好，但愿成为其中一份子。",
            "这是典型的反地域歧视承诺（pledge）类发言——表达主观意愿参与反对地域歧视的行动。"
        ],
        "encoding_analysis": [
            "无编码机制。直接表达支持和参与意愿，没有任何攻击性词汇或编码。",
            "'抵制地域黑'是正面的社会倡议标签。"
        ],
        "context_analysis": [
            "知乎地域报道话题，回复某个呼吁抵制地域黑的帖子。不需要额外上下文。"
        ],
        "supporting_evidence": [
            "1. '抵制地域黑从我做起'是正面的反歧视口号引用。",
            "2. '虽然不知道我自己能不能做到'展现了诚实和自省。",
            "3. '我愿成为其中一份子'表达了明确的参与意愿。"
        ],
        "counter_evidence": [
            "1. 无风险证据。"
        ],
        "final_rationale": "Risk: none (hard_negative)。对'抵制地域黑'倡议的支持表态，是无风险的反偏见宣言。"
    }
    return s

def rev_004349(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "high"
    s["evidence_strength"] = "weak"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本说'楼主作为早期人士'（OP as an early person）并'目标都是一样的'（goals are the same）。极为简短且依赖语境。",
            "'早期人士'（early person）可能是某个社群/身份/时间节点的指代，但内容中缺乏定义。"
        ],
        "encoding_analysis": [
            "无编码机制。文本过于简短和模糊，无法判断存在任何编码。"
        ],
        "context_analysis": [
            "贴吧反LGBTQ话题标签但文本本身未提及任何相关关键词。高度依赖原帖内容——可能是在评论某个LGBTQ相关的早期行动者/倡导者的目标。"
        ],
        "supporting_evidence": [
            "1. 被标注为toxic=0（非有毒），ToxiCN也判为hard_negative。",
            "2. 文本没有包含任何已知的歧视编码或攻击性词汇。"
        ],
        "counter_evidence": [
            "1. 无有效反方证据——文本太模糊，不足以得出任何风险判断。"
        ],
        "final_rationale": "Risk: none (hard_negative)。文本过于简短模糊，在缺乏原帖上下文的情况下无法识别任何风险。"
    }
    return s

def rev_004350(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "high"
    s["evidence_strength"] = "weak"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本描述一个叫'果子狸'的用户在美国驻成都领事馆关闭当天注销账号跑路，然后说'什么成分就不用多说了'（what faction they belong to goes without saying）。",
            "'成分'（faction/makeup）在中文互联网中指'政治成分'或'政治站位'——说话者暗示该用户跑路行为证明其亲美/友军。\U0001f436表情可能是'狗头保命'（表明在玩梗）。"
        ],
        "encoding_analysis": [
            "无编码机制。这是一条关于特定用户行为+政治推测的评论，不涉及任何群体攻击或歧视编码。",
            "原标注none/无编码，正确。但原risk_level low被误判——应降为none。"
        ],
        "context_analysis": [
            "知乎种族话题标签可能为误标——更像是政治评论（中美关系/领事馆关闭）。'果子狸'可能是某个因政治立场争议而知名的知乎用户。"
        ],
        "supporting_evidence": [
            "1. 文本讨论的是特定个体（果子狸）的行为和动机。",
            "2. '什么成分'是中文互联网政治讨论中常见的用语，指政治倾向。",
            "3. 不针对任何受保护群体（种族/性别/宗教）。",
            "4. 被ToxiCN标注为toxic=0（非有毒），是hard_negative。",
            "5. '\U0001f436'（狗头）可能是玩梗/免责标记，显示说话者意识到这可能是敏感评论。"
        ],
        "counter_evidence": [
            "1. 如果原话题是种族/外国人相关讨论，'成分'可能指向'亲外国人'的负面评价。但文本本身没有攻击性。"
        ],
        "final_rationale": "Risk: none (hard_negative)。讨论特定用户在美国领事馆事件中的行为，政治推测但不针对受保护群体。"
    }
    return s

def rev_004351(s):
    s["risk_level"] = "medium"
    s["encoding_primary"] = "A1_谐音"
    s["encoding_secondary"] = ["A4_外语谐音"]
    s["needs_context"] = True
    s["ambiguity"] = "high"
    s["evidence_strength"] = "weak"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "表面是一句歌词/情话风格：'尼说真艾可以永远~，一起去有尼的地方~'（Ni says true love can be forever~, let's go to where Ni is~）。看起来像一首歌的仿写。",
            "但'尼'（Ni）在种族话题中用于隐喻'黑'（因为'尼'是'黑鬼/尼哥'的早期谐音缩略）。'艾'（Ai）是'艾滋'（AIDS）的谐音。'尼说真艾'解码后隐含：'黑人真的有艾滋'。"
        ],
        "encoding_analysis": [
            "主编码A1（谐音）：'尼'是'黑鬼->尼哥->尼'缩略谱系中的一环——用'尼'字谐音替换种族侮辱词。'艾'是'艾滋'（AIDS）的取首字谐音编码。",
            "次编码A4（外语谐音）：'尼'也源自英语'nigga/nigger'的音译首字（尼格->尼），是外语->中文的谐音跨编码。",
            "整句伪装成爱情歌词，实际在传播'黑人有艾滋病'的种族刻板印象。编码链：尼->黑->黑人，艾->艾滋->艾滋病。"
        ],
        "context_analysis": [
            "贴吧种族话题，这是典型的'歌词伪装'式种族编码——表面无害的浪漫歌词，内部嵌入了种族+疾病的编码映射。需要了解'尼'和'艾'的编码背景才能解码。"
        ],
        "supporting_evidence": [
            "1. '尼'（Ni）在中文互联网种族讨论中是'黑鬼/尼哥'的缩略谐音编码，已知的种族歧视码。",
            "2. '艾'（Ai）在此不是正常用法（爱->艾），而是'艾滋'的首字编码映射。",
            "3. 整句话的'歌词'外表是伪装——语句不通顺（'有尼的地方'），正是为了让'尼'和'艾'嵌入。",
            "4. 被ToxiCN标注为toxic=1且expression=2（隐晦表达），确认有编码。"
        ],
        "counter_evidence": [
            "1. '尼说真艾'如果拆开解读也可能被理解为无意义的网络歌词片段。'尼'在某些方言/口语中是'你'的变体（如闽南语电影中'尼'的使用）。",
            "2. 整句的歌词风格明显，可能是某首歌曲的歌词而非自创编码。需要确认是否存在以'尼说真艾'为歌词的歌曲。"
        ],
        "final_rationale": "Risk: medium。通过'尼'（->黑）和'艾'（->艾滋）的谐音编码将种族歧视内容伪装成歌词，编码链存在但解码需要特定知识。硬负面的可能性（纯粹歌词）也不能完全排除。"
    }
    return s

def rev_004352(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "weak"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本说'现在社会上的情绪都挺过激的，令人感到担忧'。是对当前社会氛围的总体评价——表达了一种担忧。",
            "非常中立的社会观察，无指向性。"
        ],
        "encoding_analysis": [
            "无编码机制。纯中文日常表达，无攻击性。"
        ],
        "context_analysis": [
            "知乎种族话题标签下，本评论可能是在担心种族相关的网络讨论过激。但文本本身是通用的。"
        ],
        "supporting_evidence": [
            "1. '令人感到担忧'表达的是忧虑而非攻击。",
            "2. '社会情绪都挺过激的'是对社会宏观氛围的评价。",
            "3. 被ToxiCN标注为toxic=0（非有毒），是hard_negative样本。"
        ],
        "counter_evidence": [
            "1. 无风险证据。"
        ],
        "final_rationale": "Risk: none (hard_negative)。对网络/社会氛围的担忧表达，无攻击性。"
    }
    return s

def rev_004353(s):
    s["risk_level"] = "medium"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "medium"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本声称'刚果首都的艾滋病人占到50%'（the AIDS patient rate in Congo's capital is 50%）。是一个数字化的'事实'陈述。",
            "在种族话题讨论中，该数据被引用以佐证'非洲=艾滋病'的刻板印象。无论数据是否准确（50%是极高且可疑的数字），它在语境中的作用是强化非洲与艾滋病的负面关联。"
        ],
        "encoding_analysis": [
            "无明显编码机制。文本是直接的数据陈述形式——没有使用谐音、隐喻、反讽等编码手段。",
            "原标注D2_隐喻不适用——没有隐喻关系。风险来自数据在语境中的使用方式（种族话题下呈现非洲艾滋病数据以强化负面刻板印象），而非编码。"
        ],
        "context_analysis": [
            "知乎种族话题，此数据大概率被用作'支持'对非洲/黑人的负面评价。单独看是一个数据点，在种族话题上下文中变为种族刻板印象的佐证。"
        ],
        "supporting_evidence": [
            "1. '刚果首都的艾滋病人占到50%'——给出具体的数字和地点，增加了陈述的'可信度'外表。",
            "2. 在种族话题中呈现非洲的高艾滋病率数据，是常见的'用事实进行负面标签化'的策略。",
            "3. 50%的数字过高（更现实的数据是刚果金成人HIV感染率约0.5-1%，远低于50%），数字本身可能有捏造/夸大成分。"
        ],
        "counter_evidence": [
            "1. 如果原帖就在讨论全球艾滋病分布，引用刚果数据可能是正常的医学/流行病学讨论，不必然是种族歧视。",
            "2. 单独一条数据陈述无法判断发帖人的意图。"
        ],
        "final_rationale": "Risk: medium。在种族话题语境中引用刚果高艾滋病率数据，可能为强化'非洲/黑人=艾滋病'的负面刻板印象，但数据本身可能是客观信息引用。"
    }
    return s

def rev_004354(s):
    s["risk_level"] = "high"
    s["encoding_primary"] = "literal_keyword"
    s["encoding_secondary"] = ["D3_借代"]
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "strong"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本对一位30岁女性说：'老阿姨别折腾了！找个厂上班吧'。'老阿姨'（old auntie）是贬低大龄女性的网络用语（暗指年纪大、嫁不出去、不再年轻）。",
            "'别折腾了'（stop messing around）——暗示她当前的行为（可能是创业/追梦/感情选择）是徒劳的。'找个厂上班吧'（go work in a factory）——'厂'在此是贬低，暗示对方只能做低端工作。"
        ],
        "encoding_analysis": [
            "主编码literal_keyword：'老阿姨'是已知的对大龄女性的贬义称呼——未包装的直接贬低。",
            "次编码D3（借代）：'厂'（工厂）在此不是字面指具体工厂，而是借代'低端劳动'、'社会底层'等概念。整个句式为：30岁->老->别再想好事了->滚去工厂干活吧。"
        ],
        "context_analysis": [
            "贴吧性别话题，这是典型的性别+年龄交叉攻击（ageism+sexism）。不需要额外上下文即可判断攻击性。"
        ],
        "supporting_evidence": [
            "1. '老阿姨'在30岁的年龄用——30岁在现实中不算老，用'老阿姨'是恶意贬低，强调'过季'。",
            "2. '别折腾了'否定对方的行为/选择的价值。",
            "3. '找个厂上班吧'是经典的'认清你我的社会地位'式阶层攻击——暗示对方只配在工厂上班。",
            "4. 被ToxiCN标注为toxic=1且expression=1（直接表达）。"
        ],
        "counter_evidence": [
            "1. '老阿姨'在某些网络语境中可以是自嘲/调侃（比如'老阿姨我也……'），但用于他人（'你'）通常为贬义。"
        ],
        "final_rationale": "Risk: high。使用'老阿姨'贬低30岁女性+阶层攻击'找个厂上班'，是性别+年龄+阶层的多重攻击。"
    }
    return s

def rev_004355(s):
    s["risk_level"] = "high"
    s["encoding_primary"] = "literal_keyword"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "strong"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本说'放心吧，正常男人不会喜欢黑女的'——'正常男人'（normal men）与'喜欢黑女'（liking Black women）对立，暗示'喜欢黑女的男人不是正常男人'。",
            "'黑女'（Black women）是种族+性别交叉的群体标签。'放心吧'（rest assured）是安慰语气，将'不喜欢黑女'预设为所有人应持有的态度。"
        ],
        "encoding_analysis": [
            "主编码literal_keyword：直接使用'黑女'（Black women）作为贬低对象，'正常男人'作为排斥工具。没有隐喻或反讽——是直接的表态。",
            "原标注C4（典故/符号借用）不适用。"
        ],
        "context_analysis": [
            "知乎种族话题。文本公开表达对黑人群体的拒绝（'不喜欢黑女'）并将此态度正常化（'正常男人'都这样）。不需要额外上下文。"
        ],
        "supporting_evidence": [
            "1. '正常男人'的用法制造了'正常vs不正常'的二分法——喜欢黑女=不正常男人。",
            "2. '不会喜欢黑女'是绝对论断（不会喜欢），不包含例外。",
            "3. '放心吧'的安慰语气暗示'不用担心，没有正常男人会喜欢她们'——同时否定了所有黑女的吸引力。",
            "4. 被ToxiCN标注为toxic=1且expression=1（直接表达）。"
        ],
        "counter_evidence": [
            "1. 可能是在安慰某个担心被抢走伴侣的女性——但即使在此情境中，'黑女'作为群体的贬低依然成立。"
        ],
        "final_rationale": "Risk: high。通过'正常男人不会喜欢黑女的'句式同时歧视黑女群体和排除喜欢黑女的男人，是明确的种族+性别攻击。"
    }
    return s

def rev_004356(s):
    s["risk_level"] = "high"
    s["encoding_primary"] = "D2_隐喻"
    s["encoding_secondary"] = ["literal_keyword"]
    s["needs_context"] = True
    s["ambiguity"] = "medium"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本说'主动进笼子的人基本就不应该算人了，当然不应该还算什么女孩子'。'笼子'（cage）为核心意象——某群体主动进入了笼子。",
            "'不应该算人了'（shouldn't be considered human）是明确的去人化（dehumanization）声明——剥夺被描述者作为'人'的资格。'当然不应该还算什么女孩子'——将女性身份也剥夺了。"
        ],
        "encoding_analysis": [
            "主编码D2（隐喻）：'笼子'（cage）不是字面的笼子，而是隐喻某类关系/处境/选择。主动'进笼子'的隐喻意味着被描述者的处境是自愿的。",
            "次编码literal_keyword：'不应该算人了'（not human）是直接的、无编码的去人化攻击——虽然从'笼子'隐喻延伸而来，但'不算人了'的表述本身是字面的非人化声明。",
            "最后去掉'女孩子'身份也是直接的性别认同剥夺。"
        ],
        "context_analysis": [
            "知乎种族话题标签下，'笼子'可能隐喻跨种族关系？'进笼子'在中文网络语境中有多种可能（进入婚姻、加入某个群体、选择某种生活方式）。需要原帖上下文确定'笼子'指什么。"
        ],
        "supporting_evidence": [
            "1. '主动进笼子的'——'主动'强调自主选择，使'不应该算人了'的判定带上'既然是自找的就不值得同情'意味。",
            "2. '不应该算人了'（not human）是最高级别的去人化语言。",
            "3. '当然不应该还算什么女孩子'——从'人'到'女人'到否定整个身份等级。",
            "4. 被ToxiCN标注为toxic=1且expression=1（直接表达），原始标注者确认高风险。"
        ],
        "counter_evidence": [
            "1. 缺乏原帖内容，无法确定'笼子'的准确隐喻对象——可能是'为钱结婚'、'加入黑帮'或任何被广泛认为'自降身份'的选择。",
            "2. 文本可能指向特定行为而非整个群体，但去人化语言的性质不变。"
        ],
        "final_rationale": "Risk: high。通过'笼子'隐喻+直接'不算人了'的去人化语言攻击某类选择的女性，语言暴力程度高，但具体目标需更多上下文确定。"
    }
    return s

def rev_004357(s):
    s["risk_level"] = "high"
    s["encoding_primary"] = "literal_keyword"
    s["encoding_secondary"] = ["A2_拼音缩写"]
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "strong"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本构建了一个完整的反同论证链条：同性恋滥交->传播艾滋->增加社会医疗负担->减少全社会福利->因此社会对同性恋的认同度低是'自食恶果'。",
            "关键词：'同性恋滥交'（gay promiscuity）、'传播艾滋'（spread AIDS）、'txl的恶行'（gay evils/evildoings）、'自食恶果'（reap what you sow）。整段将同性恋群体与疾病传播直接挂钩。"
        ],
        "encoding_analysis": [
            "主编码literal_keyword：'同性恋滥交'是直接的反同负面标签化，'恶行'是直接的道德谴责，'自食恶果'是直接的价值判断。没有使用隐喻或编码包装。",
            "次编码A2（拼音缩写）：'txl'=同性恋（tong xing lian）是拼音缩写形式，在该段中用于替换完整的'同性恋'一词。但不改变其literal_keyword的性质。"
        ],
        "context_analysis": [
            "知乎反LGBTQ话题。文本不是reporting/转述，而是作者本人的论证主张。不需要额外上下文即可判断。"
        ],
        "supporting_evidence": [
            "1. '同性恋滥交和传播艾滋造成的苦果'——将同性恋与滥交和艾滋病传播直接因果关系绑定。",
            "2. 'txl的恶行'——'恶行'是对整个群体的道德定性。",
            "3. '自食恶果'——用因果报应逻辑合法化对同性恋的歧视。",
            "4. '减少每个人得到的社会福利'——将反同立场包装成'维护公共利益'，是经典的反同修辞策略。"
        ],
        "counter_evidence": [
            "1. 如果文本是在转述'有些人认为……'的论点（reporting），则可能不是本人立场。但全文是主动断言语气，无转述标记。"
        ],
        "final_rationale": "Risk: high。构建完整的反同论证，将同性恋与艾滋传播和社会负担挂钩，使用'恶行''自食恶果'等直接谴责词，是明确的反同仇恨言论。"
    }
    return s

def rev_004358(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "low"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本列举四个地理区域（河南东部、安徽西北部、江苏北部、山东西南部），指出历史上称为'黄泛区'（Yellow River Flood Plain）。",
            "这是一个纯粹的地理/历史事实陈述。'黄泛区'是1938年花园口决堤后形成的真实地理概念。"
        ],
        "encoding_analysis": [
            "无编码机制。这是标准的地理/历史名称使用，不包含任何编码或攻击性。原标注E3不适用。"
        ],
        "context_analysis": [
            "知乎地域报告话题，可能有人质疑这些地区名声不好的原因，回复用'黄泛区'的历史标签来解释这些地区有共同的历史背景。"
        ],
        "supporting_evidence": [
            "1. '黄泛区'是真实的历史地理术语，不是一个歧视性称呼。",
            "2. 文本以'史上称呼'作为前缀，表明是在报告历史事实。",
            "3. 无任何评价性语言——只有地名和归类。",
            "4. 被ToxiCN标注为toxic=0（非有毒），是hard_negative样本。"
        ],
        "counter_evidence": [
            "1. '黄泛区'在某些语境下可能被误读为对这些地区的负面归类（黄泛区=穷/落后的地区），但这是历史上的客观地理划分，说话者没有附加负面评价。"
        ],
        "final_rationale": "Risk: none (hard_negative)。纯粹的地理/历史事实陈述，列出黄泛区范围，无攻击性。"
    }
    return s

def rev_004359(s):
    s["risk_level"] = "medium"
    s["encoding_primary"] = "E1_平台黑话"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "medium"
    s["evidence_strength"] = "moderate"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本说'我也不理解，外来户怎么还敢这样高调'——无法理解为什么'外来户'（outsiders/non-locals）敢如此高调/张扬。",
            "'外来户'指代外来者、外乡人、移民。'高调'指高调、张扬的行为方式。整句表达了对'外来者高调'的不满和不解。"
        ],
        "encoding_analysis": [
            "无明显编码机制。'外来户'是标准中文词汇（外来户=外来人家/移民户），不是歧视性编码词汇。",
            "风险来自'我也不理解……怎么还敢'的句式——表达了'外来者应该低调'的期望，隐含了'外来者不配高调'的排斥态度。"
        ],
        "context_analysis": [
            "贴吧种族话题，'外来户'可能指代外国人或移民群体。需要原帖上下文才能确定具体指哪个群体。"
        ],
        "supporting_evidence": [
            "1. '怎么还敢'（how dare they still）——'敢'暗示外来者'高调'是越界行为。",
            "2. '高调'对某种行为模式的负面评价。",
            "3. '我也不理解'——'也'表示与其他人共有这一看法，暗示发帖者认为这是一种共识。"
        ],
        "counter_evidence": [
            "1. '外来户'这个词在特定语境中可能指代具体被讨论的'新搬来的人'（如小区外来户），不一定有群体歧视含义。",
            "2. 文本的态度是不解和不满，但没有使用侮辱性词汇或主张暴力/排斥。"
        ],
        "final_rationale": "Risk: medium。用'外来户'指代非本地/外来群体并表达'怎么敢高调'的不满，有排外情绪但编码模糊、攻击间接。"
    }
    return s

def rev_004360(s):
    s["risk_level"] = "low"
    s["encoding_primary"] = "E1_平台黑话"
    s["encoding_secondary"] = []
    s["needs_context"] = False
    s["ambiguity"] = "low"
    s["evidence_strength"] = "weak"
    s["hard_negative"] = False
    s["target_known"] = True
    s["reasoning"] = {
        "literal_analysis": [
            "文本声称'体制内打拳的最多了'——政府体制/公共部门中最多的就是'打拳'的人（女权/激进女性主义者），而且他们'优越感很多很强'。",
            "'打拳'（punching/fighting）是中文网络对激进女性主义/女权运动的贬义代称（源于'打拳'与'女权'的关联比喻）。"
        ],
        "encoding_analysis": [
            "主编码E1（平台黑话）：'打拳'是中文互联网特定社区（贴吧/虎扑/知乎等）中用来贬义指代女性主义运动的黑话。字面是'打拳/出拳'，实际指'激进的性别对立言论或女权评论'。",
            "原标注D2_隐喻不准确——'打拳'虽然原本是隐喻，但在当前网络用法中已固化为性别话题的特指黑话，更适合E1编码。"
        ],
        "context_analysis": [
            "知乎种族话题标签可能为误标——'打拳'几乎只用于性别话题讨论。文本是对女性主义者（在体制内群体中居多）的刻板印象式批评。"
        ],
        "supporting_evidence": [
            "1. '打拳'是性别对立话题中女性主义者的贬义代称（E1平台黑话），需要了解网络社区语境才能解码。",
            "2. '优越感很多很强'——印象式断言体制内的女权主义者傲慢/自负。",
            "3. '体制内'给批评加上了具体的社会阶层定位。"
        ],
        "counter_evidence": [
            "1. '打拳'虽然带贬义但攻击程度相对温和——本质是一种generalization/stereotype，不是直白的群体辱骂。",
            "2. 文本是对'体制内女性主义者'行为的概括性批评，而不是对所有女性的攻击。"
        ],
        "final_rationale": "Risk: low。用'打拳'（E1平台黑话）代称女性主义者并断言其体制内居多且优越感强，是刻板印象化批评而非仇恨言论。"
    }
    return s

def rev_004361(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "low"
    s["evidence_strength"] = "weak"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本简单陈述：'我在B站贴吧发了帖子，直接被秒删'。在Bilibili贴吧（B站吧）发帖，被秒删。",
            "叙述者报告了自己发帖被迅速删除的经历。"
        ],
        "encoding_analysis": [
            "无编码机制。这是一条简单的事实陈述，没有任何攻击性词汇或编码。"
        ],
        "context_analysis": [
            "贴吧性别话题下，发帖内容可能涉及性别争议话题所以被删除。但文本本身只是报告被删的事实，不包含攻击性。"
        ],
        "supporting_evidence": [
            "1. 纯粹的事实陈述——发帖->被删。",
            "2. 无任何攻击性语言或目标。",
            "3. 被ToxiCN标注为toxic=0（非有毒），是hard_negative样本。"
        ],
        "counter_evidence": [
            "1. 无风险证据。即使知道发帖内容有争议，文本本身只是报事。"
        ],
        "final_rationale": "Risk: none (hard_negative)。简单报告发帖被删经历，无任何风险。"
    }
    return s

def rev_004362(s):
    s["risk_level"] = "none"
    s["encoding_primary"] = "none"
    s["encoding_secondary"] = []
    s["needs_context"] = True
    s["ambiguity"] = "high"
    s["evidence_strength"] = "weak"
    s["hard_negative"] = True
    s["target_known"] = False
    s["reasoning"] = {
        "literal_analysis": [
            "文本是'第二代这人真的是……'（This second generation person is really...）——句子不完整，以省略号结尾。",
            "'第二代'（second generation）可能指第二代移民。'真的是……'是中文中表达无奈/感慨/吐槽的句式，但未完成的省略号使完整语义缺失。"
        ],
        "encoding_analysis": [
            "无编码机制。句子过于简短和不完整，无法确定任何编码或攻击意图。"
        ],
        "context_analysis": [
            "贴吧反LGBTQ话题标签。'第二代'可能是在LGBTQ语境中指代'第二代移民中的同性恋者'或类似的群体。但文本的不完整性使判断极为困难。高度依赖原帖。"
        ],
        "supporting_evidence": [
            "1. 被标注为toxic=0（非有毒），是hard_negative样本。",
            "2. 句子不完整，无法确定具体的含义和态度。"
        ],
        "counter_evidence": [
            "1. '真的是……'在中文表达中通常带有负面评价倾向（如'他真的是……太让人无语了'），但缺少后续内容无法确认具体指向。"
        ],
        "final_rationale": "Risk: none (hard_negative)。句子不完整，缺乏语义确定性的情况下不宜判为有风险。"
    }
    return s

# ====== APPLY ======

review_map = {
    "004313": rev_004313, "004314": rev_004314, "004315": rev_004315,
    "004316": rev_004316, "004317": rev_004317, "004318": rev_004318,
    "004319": rev_004319, "004320": rev_004320, "004321": rev_004321,
    "004322": rev_004322, "004323": rev_004323, "004324": rev_004324,
    "004325": rev_004325, "004326": rev_004326, "004327": rev_004327,
    "004328": rev_004328, "004329": rev_004329, "004330": rev_004330,
    "004331": rev_004331, "004332": rev_004332, "004333": rev_004333,
    "004334": rev_004334, "004335": rev_004335, "004336": rev_004336,
    "004337": rev_004337, "004338": rev_004338, "004339": rev_004339,
    "004340": rev_004340, "004341": rev_004341, "004342": rev_004342,
    "004343": rev_004343, "004344": rev_004344, "004345": rev_004345,
    "004346": rev_004346, "004347": rev_004347, "004348": rev_004348,
    "004349": rev_004349, "004350": rev_004350, "004351": rev_004351,
    "004352": rev_004352, "004353": rev_004353, "004354": rev_004354,
    "004355": rev_004355, "004356": rev_004356, "004357": rev_004357,
    "004358": rev_004358, "004359": rev_004359, "004360": rev_004360,
    "004361": rev_004361, "004362": rev_004362,
}

for s in samples:
    sid = s["id"]
    if sid in review_map:
        s = review_map[sid](s)
    s["quality_status"] = "reviewed"
    existing = s.get("review_notes", "").rstrip(";").strip()
    s["review_notes"] = existing + "; reviewed_by=claude; chunk=034"

with open(dst, "w", encoding="utf-8") as f:
    for s in samples:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")

risk_counts = Counter(s["risk_level"] for s in samples)
enc_counts = Counter(s["encoding_primary"] for s in samples)

print(f"Written {len(samples)} samples to {dst}")
print(f"Risk distribution: high={risk_counts.get('high',0)} medium={risk_counts.get('medium',0)} low={risk_counts.get('low',0)} none={risk_counts.get('none',0)}")
print(f"Encoding distribution: {dict(enc_counts)}")

# Quick validation
for s in samples:
    assert s["quality_status"] == "reviewed", f"quality_status not set for {s['id']}"
    assert "reviewed_by=claude" in s["review_notes"], f"review_notes missing for {s['id']}"
    assert "chunk=034" in s["review_notes"], f"chunk tag missing for {s['id']}"
    assert "reasoning" in s
    for field in ["literal_analysis", "encoding_analysis", "context_analysis", "supporting_evidence", "counter_evidence", "final_rationale"]:
        assert field in s["reasoning"], f"{field} missing in {s['id']}"
        content = s["reasoning"][field]
        if isinstance(content, list):
            assert len(content) >= 1, f"Empty {field} in {s['id']}"
        elif isinstance(content, str):
            assert len(content) > 0, f"Empty {field} in {s['id']}"
    assert "evidence_strength" in s
    assert "ambiguity" in s
    assert "needs_context" in s
    assert s["evidence_strength"] in ("strong", "moderate", "weak"), f"bad evidence_strength {s['id']}"

print("All 50 samples validated successfully.")
print(f"Total output file size: {len(open(dst).read())} bytes")
