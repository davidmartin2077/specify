#!/usr/bin/env python3
"""Review chunk_025.jsonl — rewrite all reasoning fields with text-specific analysis."""

import json
import sys

INPUT = "/Users/davidchankong/Documents/审查微调/data/raw/batch23_chunks/chunk_025.jsonl"
OUTPUT = "/Users/davidchankong/Documents/审查微调/data/raw/batch23_chunks/chunk_025_reviewed.jsonl"

REVIEW_TAG = "; reviewed_by=claude; chunk=025"

def overwrite(sample, updates):
    """Apply updates dict to sample and return modified copy."""
    s = dict(sample)
    for k, v in updates.items():
        s[k] = v
    s["quality_status"] = "reviewed"
    notes = s.get("review_notes", "")
    if REVIEW_TAG not in notes:
        notes += REVIEW_TAG
    s["review_notes"] = notes
    return s


def review_all(samples):
    """Return generator of reviewed samples, one yield per original."""
    # ── Sample 1 (003863) ──────────────────────────
    s1 = overwrite(samples[0], {
        "risk_level": "high",
        "encoding_primary": "B3_形近字",
        "encoding_secondary": ["literal_keyword"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本表面讨论婚育和家庭分工，通过'畒的托词'、'借冠姓权做文章'、'80以后的女人'、'抛去这一项畒还有什么'等一系列表达，系统性地贬低女性的家庭贡献，将女性在婚姻中的角色贬为'托词'和'借口'。",
                "关键词'畒'是字形编码——使用罕见的古汉字/异体字替代'女'，在贴吧/虎扑等社区中是已知的女性贬称写法。",
                "末尾反问句'畒还有什么'是总结性攻击，暗示女性除了生育外无其他价值。"
            ],
            "encoding_analysis": [
                "'畒'是B3_形近字编码：用字形接近'女'但更生僻的异体字替代，在网络社区中形成了固定的贬义称呼惯例，字面看似'不是直接骂人'但实际上攻击性极强。",
                "其余内容（'托词'、'做文章'、'大有人在'、'无稽之谈'）均为直接攻击性表达（literal_keyword），没有经过编码包装，属于直白的贬低。"
            ],
            "context_analysis": [
                "贴吧性别讨论语境中，这类对女性婚育角色整体否定的文本是典型的性别攻击。无需额外上下文即可明确攻击意图。"
            ],
            "supporting_evidence": [
                "使用字形编码词'畒'替代'女'，该写法在贴吧性别攻击中频繁出现，意图规避平台过滤",
                "连续使用'托词'、'借口'、'做文章'三个贬义词汇系统性质疑女性的家庭付出",
                "'80以后的女人让她包揽全部家务伺候男人起居住行'——通过极端假设强化攻击，暗示现代女性不如传统女性",
                "'抛去这一项畒还有什么'——反问句式总结性否定女性价值，是典型的misogyny表达"
            ],
            "counter_evidence": [
                "文本含有对婚姻现实的观察成分（如'现实中不需要父母帮忙看护孩子的家庭极少'），但整体语境仍是贬低女性，不是中性社会讨论",
                "部分表达（'伺候男方更是无稽之谈'）可能是基于个人经验反驳某种观点，但全篇的攻击性方向明确"
            ],
            "final_rationale": "Risk: high。使用B3编码词'畒'和大量直接贬低女性的表达，系统性质疑和否定女性的家庭社会价值，攻击目标明确，攻击性极强。"
        }
    })
    yield s1

    # ── Sample 2 (003864) ──────────────────────────
    s2 = overwrite(samples[1], {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "medium",
        "evidence_strength": "weak",
        "needs_context": False,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本评论'社达'（社会达尔文主义）——指出其在理论上被批判但在社会发展现实中'却是支持的'，并称此为讽刺。全文是对一种意识形态概念的一般性观察。",
                "'社达'是该文唯一可能与风险相关的关键词，但文本没有将社会达尔文主义应用于任何具体种族或群体，没有表达攻击性。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本以字面意义发表对社会达尔文主义的观察，'社达'是常见的缩写（社会+达尔文主义），不是编码。'真讽刺了'直接表达'讽刺'的概念，不是在使用反讽编码。",
                "没有使用隐喻——文本没有通过意象或场景映射任何隐藏态度。'社达一直在理论上被批判'是对该思想地位的客观描述。"
            ],
            "context_analysis": [
                "话题标签为race_discussion但文本本身未提及任何种族或群体。唯一的风险路径是社会达尔文主义与种族主义的间接关联，但这种关联在这段文本中完全没有被激活。"
            ],
            "supporting_evidence": [
                "文本仅讨论了'社达'的理论与实践地位，没有对任何群体做出负面评价",
                "'真讽刺了'表达的是对理论/现实张力的个人感受，而非攻击",
                "没有使用任何攻击性词汇或编码机制"
            ],
            "counter_evidence": [
                "社会达尔文主义在历史语境中与种族歧视有关联，因此该文本出现在race话题下有一定话题合理性",
                "文本未明确反对社达，而是说社会现实'支持'它——可被解读为认可社达的实践价值，但这不是对任何群体的攻击"
            ],
            "final_rationale": "Risk: low。文本是对社会达尔文主义的一般性评论，未针对任何群体表达攻击或偏见，风险完全来自话题背景而非文本本身。"
        }
    })
    yield s2

    # ── Sample 3 (003865) ──────────────────────────
    s3 = overwrite(samples[2], {
        "risk_level": "high",
        "encoding_primary": "A2_拼音缩写",
        "encoding_secondary": ["literal_keyword"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本描述一名女性与黑人男性的性行为，使用'黑g'和'黑d'两个缩写词以及'透烂了'、'吃烂了'等极端暴力的性描写词汇。",
                "'黑g'是'黑鬼'（对黑人的种族歧视称呼）的拼音首字母缩写；'黑d'是'黑屌'（对黑人男性生殖器的种族化侮辱）的缩写。",
                "全文以极端色情暴力语言进行种族侮辱，攻击性极强。"
            ],
            "encoding_analysis": [
                "'黑g'和'黑d'使用A2_拼音缩写编码——'黑鬼'和'黑屌'的首字母缩写形式，在中文网络社区中被用作规避平台内容过滤的种族侮辱编码。",
                "除两个缩写词外，其余内容（'透烂了'、'吃烂了'）是直白的性暴力描写，不属于任何编码机制，属于literal_keyword。"
            ],
            "context_analysis": [
                "贴吧平台的不实名和低内容审核环境使得这类极端种族攻击可以公开传播。文本攻击目标明确（黑人），不需要额外上下文。"
            ],
            "supporting_evidence": [
                "'黑g'是已知的种族侮辱缩写——'g'代表'鬼'，是中文互联网对黑人的经典辱称",
                "'黑d'是公开的种族色情侮辱——'d'代表'屌'，将种族歧视与性侮辱结合",
                "'透烂了'和'吃烂了'使用极端暴力语言，将攻击推向极致",
                "目标明确（黑人）且攻击直接，毫无歧义"
            ],
            "counter_evidence": [
                "缩写词（'黑g'、'黑d'）具有一定的模糊性，脱离网络社区语境的读者可能无法立即解码。但在当前语境下解码路径是明确的。"
            ],
            "final_rationale": "Risk: high。使用A2编码（'黑g'='黑鬼'、'黑d'='黑屌'）配合直接性暴力语言，对黑人群体进行极端种族色情攻击，攻击直接、目标明确、语言极端。"
        }
    })
    yield s3

    # ── Sample 4 (003866) ──────────────────────────
    s4 = overwrite(samples[3], {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": True,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本批评某人幼稚、看人不准——'自以为是其实幼稚的不得了'、'谁是你的朋友你看的清楚吗'。核心批评点是这个人在'国家朋友'（国际关系）问题上缺乏辨别力。",
                "'你觉得是朋友就是国家的朋友了吗'——指的是个人判断与国家利益之间的区别，讨论的是国际关系中的外交认知，而非种族话题。",
                "末尾'真是笑话😅😅'明确表达了不赞同，但这是针对个人观点的批评，不是群体攻击。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本使用通用评价词（'幼稚'、'笑话'）批评一个人的判断力，没有使用任何编码词或攻击性隐喻。",
                "'国家的朋友'指的是国际关系中的盟友/伙伴概念，不是编码表达。"
            ],
            "context_analysis": [
                "文本被标注为race_discussion，但内容讨论的是国际关系/外交话题。如果原文主题涉及种族的国际维度（如中外关系），则文本是回应性的批评，文本本身不具种族攻击性。",
                "由于缺乏上下文（被批评的原话），难以判断对话背景，但文本本身的攻击目标是个体而非群体。"
            ],
            "supporting_evidence": [
                "文本批评对象是'你'（个体），而非任何种族群体",
                "ToxiCN标注为toxic=0，说明原文被判定为非有毒样本",
                "'国家的朋友'讨论的是国际关系概念，不是种族概念"
            ],
            "counter_evidence": [
                "如果原文是在中外关系语境下为对外政策辩护，该批评可能隐含对持不同立场者的政治性攻击。但即使如此，攻击目标是个体观点，不是种族群体。"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本批评个人在国际关系判断上的幼稚，不针对任何群体，虽有讽刺语气但不构成风险内容。"
        }
    })
    yield s4

    # ── Sample 5 (003867) ──────────────────────────
    s5 = overwrite(samples[4], {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本以引号转述他人的观点——'只是歧视国男，对国男高标准，对外国男性放宽要求'，然后用做法不对明确表态不认同该观点。'虽然给你点了赞'表明被回应的原文有可取之处但仍持保留态度。",
                "整段话是对一种'歧视国男'做法的批评——叙述者认为这种内外有别的双重标准是错误的。",
                "文本立场是反歧视的，谴责的是'歧视国男'的行为。"
            ],
            "encoding_analysis": [
                "不存在编码机制。引号中的内容是对他人言论的直接转述（reporting/转述），叙述者的表态'这种做法不对'是直接的观点表达，无编码。",
                "没有使用反讽——'虽然给你点了赞，但我觉得……不对'是正常的让步转折结构，不是反讽。"
            ],
            "context_analysis": [
                "标注为race_reporting（种族报道/揭露），文本转述并批评的所谓'歧视国男'具体指什么需要上下文——可能是指中国女性对外国男性的偏好。但文本本身不包含攻击，而是批判歧视。",
                "上下文对判断很重要——原贴上下文可能影响读者的解读，但文本本身的anti-bias立场是清晰的。"
            ],
            "supporting_evidence": [
                "文本明确批评歧视做法——'这种做法不对'是clear position",
                "转述的歧视内容放在引号内，表明是在引用而非表达",
                "ToxiCN标注为expression=3（揭露/报告类型），符合文本的转述立场"
            ],
            "counter_evidence": [
                "转述的'歧视国男'内容提及了性别群体（国男/外国男性），可能强化刻板印象，但叙述者明确不认同",
                "缺乏原始上下文——被批评的'歧视国男'具体是怎样的表述不可知"
            ],
            "final_rationale": "Risk: low。文本转述并明确批评歧视国男的做法，叙述者立场是反歧视。风险来自话题敏感性和转述内容，而非文本本身的攻击性。"
        }
    })
    yield s5

    # ── Sample 6 (003868) ──────────────────────────
    s6 = overwrite(samples[5], {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "medium",
        "evidence_strength": "weak",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本评论江西人结婚彩礼高——'只能说江西人真有钱结个婚彩礼都好几十万'。这句话可理解为中性观察（江西彩礼确实高），也可理解为泛泛的刻板印象。",
                "'真有钱'可能是字面意义（表示有钱），也可能是反讽（表示对高彩礼的无奈）。但无论哪种解读，文本都没有针对江西人进行贬低或攻击。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是直白的口语化评论，没有使用任何编码手段。'只能说'是常见的语气副词。",
                "没有使用反讽——如果'真有钱'是反讽，那意图是对高彩礼现象的无奈评论，而不是攻击江西人。但反讽的意图不明确。",
                "没有使用双关——文本只有一种表面含义。"
            ],
            "context_analysis": [
                "标注为gender_discussion但内容是关于江西（地域）的高彩礼现象。话题标签与内容有偏差。",
                "需要上下文：如果该评论是在讨论'江西女生要价高'之类的性别话题中，则可能包含性别刻板印象。"
            ],
            "supporting_evidence": [
                "文本涉及敏感话题（地域彩礼刻板印象），但表达方式是评述性的而非攻击性的",
                "'真有钱'的语气中性偏惊讶，不是侮辱性表达",
                "没有使用任何攻击性词汇"
            ],
            "counter_evidence": [
                "即使作为中性观察，'江西人真有钱+彩礼好几十万'强化了'江西彩礼贵'的地域刻板印象，可能被解读为地域歧视",
                "缺乏上下文——如果原贴是在攻击江西女性，则此评论可能是附和"
            ],
            "final_rationale": "Risk: low。文本以近似中性的语气评论江西高彩礼现象，虽有地域刻板印象之嫌但缺乏攻击性表达，证据不足以上升至medium。"
        }
    })
    yield s6

    # ── Sample 7 (003869) ──────────────────────────
    s7 = overwrite(samples[6], {
        "risk_level": "high",
        "encoding_primary": "E1_平台黑话",
        "encoding_secondary": ["A1_谐音"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "'我185'是身高声明——在网络性别讨论中常用于建立'有资格评论女性'的男性身份。'但这幕刃是鲨bee'是两个攻击性词组的组合。",
                "'幕刃'是贴吧/虎扑等社区对女性的贬义黑话代称，通过字形组合（幕+刃）创作的新词。'鲨bee'是'傻逼'的谐音变体。",
                "全文结构：先建立身份（185cm男性），然后攻击特定女性。"
            ],
            "encoding_analysis": [
                "'幕刃'使用E1_平台黑话编码——该词是男性社区（贴吧/虎扑）内创造的女性贬称，是平台特定黑话，跨出该社区不懂梗的读者无法理解。",
                "'鲨bee'使用A1_谐音编码——'鲨'音似'傻'，'bee'是英文谐音'逼'，经过双层语音转换以规避直接脏话过滤。",
                "编码的复合使用（平台黑话+谐音）反映了文本作者有意使用隐晦攻击手段。"
            ],
            "context_analysis": [
                "贴吧性别讨论语境中，'幕刃'是已知的女性攻击词。文本没有歧义——攻击目标和攻击意图都非常明确。",
                "不需要额外上下文即可判断。"
            ],
            "supporting_evidence": [
                "'幕刃'在男性社区是固定编码词，专门用于贬低女性，相当于平台黑话",
                "'鲨bee'是双层语音编码（汉语谐音+英文谐音），指向脏话'傻逼'",
                "'我185'作为开场白建立身份意图（我是高个子男性），为后续攻击增强语气",
                "攻击对象明确（'这幕刃'=这个女人），目标_known=true"
            ],
            "counter_evidence": [
                "如果不知道'幕刃'的社区编码含义，表面看是难以理解的组合词，但鉴于文本在贴吧和gender话题下，解码路径明确。"
            ],
            "final_rationale": "Risk: high。使用E1平台黑话'幕刃'+A1谐音'鲨bee'对女性进行攻击，双层编码掩饰直白侮辱，攻击目标明确、编码意图明显。"
        }
    })
    yield s7

    # ── Sample 8 (003870) ──────────────────────────
    s8 = overwrite(samples[7], {
        "risk_level": "medium",
        "encoding_primary": "D1_反讽",
        "encoding_secondary": ["literal_keyword"],
        "ambiguity": "medium",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "开头的'你说的太对了'与后续内容形成张力——可能是反讽开场。然后文本自称'尊重同性恋'，但后续批评两种人：双标腐女（对帅哥同性恋尖叫、对不好看的同性恋'内啥'）和道德绑架者（打着不歧视的名号强迫别人喜欢）。",
                "关键词'掰弯'（扳弯/convert to gay）、'内啥'（委婉省略粗话）、'恶心'表达了负面评价。",
                "文本的核心是对LGBT圈内某些行为的批评（腐女的双标审美、道德绑架式的强迫认同），而非对同性恋群体的直接攻击。"
            ],
            "encoding_analysis": [
                "'你说的太对了'可能是反讽（D1）——从后续批评语气推断，叙述者并非真的完全赞同。",
                "'内啥'是含蓄省略（不算是编码机制），'掰弯'是通用网络词。其余表达为直接评论（literal_keyword）。",
                "没有使用平台黑话——文本没有依赖社区特定编码词汇。"
            ],
            "context_analysis": [
                "标注为lgbt_discussion但文本批评的是LGBT相关议题中的特定行为（腐女文化、道德绑架），而非同性恋群体。",
                "需要上下文来判断叙述者整体立场——是同志社区内部分歧还是外部攻击。从'我本人还是尊重同性恋的'来看，更像是内部批评者。"
            ],
            "supporting_evidence": [
                "'我本人还是尊重同性恋的'——明确表态不针对性取向群体",
                "批评对象是具体行为（'想把别人掰弯'、'道德绑架'），而非身份群体",
                "'可以相爱'——承认同性恋者的相爱权利",
                "ToxiCN标注为toxic=1/expr=1但文本本身有矛盾"
            ],
            "counter_evidence": [
                "'恶心了'是强烈的负面词汇，整体批评语气较强",
                "对'看见不太好看的同性恋就内啥'的批评可能强化了'同性恋注重外表'的刻板印象",
                "开头反讽语气可能模糊文本的真实立场"
            ],
            "final_rationale": "Risk: medium。文本自称尊重同性恋但批评LGBT圈内行为（双标腐女、道德绑架者），使用反讽开场和较强负面词汇，有争议风险但非直接反同攻击。"
        }
    })
    yield s8

    # ── Sample 9 (003871) ──────────────────────────
    s9 = overwrite(samples[8], {
        "risk_level": "high",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["D2_隐喻"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本评论某人的外貌——'在所有🦍中确实算是好看的'，然后建议将其送动物园'回归大自然'，称'人类社会不适合它'。",
                "🦍（大猩猩emoji）是中文互联网中黑人的种族歧视符号。'送到动物园'、'回归大自然'、'人类社会不适合它'是种族非人化(dehumanization)的经典话语模式。"
            ],
            "encoding_analysis": [
                "🦍使用C4_符号借用编码——大猩猩emoji被借用为黑人的种族歧视代称，是中文互联网种族歧视社区中高度固化的视觉符号。",
                "'送到动物园'、'回归大自然'、'人类社会不适合它'使用D2_隐喻编码——通过'野生动物不适合人类社会'这一隐喻框架来传达'黑人不属于文明社会'的种族主义信息。",
                "整个文本建立了'黑人=猩猩=野生动物'的隐喻对应关系。"
            ],
            "context_analysis": [
                "贴吧的匿名性和松散的审核使得这类种族攻击得以传播。emoji作为编码工具规避了内容过滤。",
                "攻击意图极度明确，无需额外上下文。"
            ],
            "supporting_evidence": [
                "🦍在种族语境中是已知的黑人侮辱符号——用动物指代人类群体是最典型的非人化种族歧视",
                "'送到动物园'——将人类送往动物场所，明确表达了'不是人类'的含义",
                "'回归大自然'——呼应'野生动物'框架",
                "'人类社会不适合它'——用'它'而非'他/她'，进一步非人化，否定主体作为'人'的资格"
            ],
            "counter_evidence": [
                "如果没有种族话题标注和emoji使用语境，字面上是对大猩猩的评论。但鉴于上下文（race_discussion、贴吧），编码意图非常明确。"
            ],
            "final_rationale": "Risk: high。使用🦍符号（C4）构建'黑人=猩猩=野生动物'的隐喻编码，通过送动物园/回归自然/不适合人类社会等表达系统性地进行种族非人化攻击。"
        }
    })
    yield s9

    # ── Sample 10 (003872) ──────────────────────────
    s10 = overwrite(samples[9], {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": True,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本反驳某种地域歧视的说法。'可拉倒吧'是口语化反驳（意为'算了吧/别扯了'）。然后指出在东北做生意的浙江人很多，逻辑上质问'我们东北人歧视浙江人，浙江人能有那么多吗'。",
                "叙述者通过反问暗示：如果歧视真的很严重，不会有这么多浙江人来东北做生意。这是在质疑歧视的程度或存在。",
                "文本是在反对地域歧视叙事，而非传播歧视。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本使用逻辑论证（援引人口流动事实）和反问来反驳歧视说法，是直白的观点表达。",
                "'可拉倒吧'是口语表达，不是编码。"
            ],
            "context_analysis": [
                "标注为region_discussion，文本是在回应有关东北地域歧视的讨论。如果原帖主张'东北人歧视浙江人'，此文本是反驳，认为实际情况并非如此。",
                "需要上下文来确定具体的反驳对象，但文本本身的反歧视立场是明确的。"
            ],
            "supporting_evidence": [
                "'可拉倒吧'表明反驳立场——对某种言论不认同",
                "用实际现象（浙江人在东北做生意很多）作为反歧视论据",
                "反问句'浙江人能有那么多吗'——逻辑上质疑歧视叙事"
            ],
            "counter_evidence": [
                "文本承认'我们东北人歧视浙江人'（虽然用引述语气），这种承认本身可能强化地域刻板印象",
                "部分读者可能将'歧视浙江人'解读为'在东北的浙江人确实被歧视'而非转述"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本通过事实逻辑和反问质疑地域歧视说法，立场是反地域刻板印象而非传播歧视。"
        }
    })
    yield s10

    # ── Sample 11 (003873) ──────────────────────────
    s11 = overwrite(samples[10], {
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
                "文本评论'失足妇女'（性工作者委婉称呼）——'是要钱，可以理解'。这是一个非常简短的对性工作者动机的解释（为了钱），并表示理解。",
                "文本没有攻击任何人。'失足妇女'是中文中较为体面的性工作者委婉语，不是侮辱性词汇。",
                "在race_discussion语境下，此文本看起来完全不相关——可能是回答串中针对某个特定论证的一句回应。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本没有使用任何编码或攻击性词汇。'失足妇女'本身是委婉语，但在此语境中的使用是常规的社会讨论，不是编码攻击。"
            ],
            "context_analysis": [
                "文本与种族话题完全不相关，可能是串中跑题的回答。在race_discussion话题标签下，缺乏足够的上下文来理解为何出现此内容。",
                "由于文本过于简短且偏离话题，应标为需要上下文。"
            ],
            "supporting_evidence": [
                "文本对性工作者持中性至同情的态度（'可以理解'）",
                "没有使用任何攻击性词汇",
                "没有涉及种族话题——与标签完全脱节"
            ],
            "counter_evidence": [
                "缺乏上下文——'可以理解'可能是在特定争议语境中对性工作者行为的一种简化的合理化，但文本本身没有提供任何攻击性或偏见内容。"
            ],
            "final_rationale": "Risk: none (hard_negative)。极度简短的文本评论失足妇女的动机并表示理解，无任何攻击性内容，话题标签与内容脱节。"
        }
    })
    yield s11

    # ── Sample 12 (003874) ──────────────────────────
    s12 = overwrite(samples[11], {
        "risk_level": "medium",
        "encoding_primary": "D1_反讽",
        "encoding_secondary": ["literal_keyword"],
        "ambiguity": "medium",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本讨论回族（Hui）是否真的被歧视。以异族婚姻子女的民族登记为例——'假如你和汉族结婚有孩子，请问户口报什么民族？现实中我还真没看到谁报汉的'——声称没见过回汉通婚子女报汉族。然后反问'那真的被黑被歧视吗？'",
                "'被黑'在此语境中意为'被抹黑/被冤枉/被歧视'。文本质疑回族受到的歧视是否存在或严重。",
                "核心逻辑：如果回族真的被歧视，为什么通婚子女不会选择登记为汉族（以避免被歧视）？——这个论证有简化之嫌（回避了结构性歧视等复杂因素）。"
            ],
            "encoding_analysis": [
                "'那真的被黑被歧视吗？'使用了D1_反讽编码——表面上是疑问句，暗示的答案是'其实没有'，通过反问形式质疑歧视叙事。",
                "其余内容为直接论证（literal_keyword），使用'我还没看到谁报汉的'作为论据。"
            ],
            "context_analysis": [
                "文本出现在region_discussion话题下，但讨论的是民族（回族/Hui）而非地域问题。话题标签有偏差。",
                "需要原帖上下文来判断叙述者是在善意质疑还是恶意否认少数民族受歧视的事实。"
            ],
            "supporting_evidence": [
                "文本使用具体论据（民族登记选择）来质疑歧视的存在，具有论证结构",
                "'我没看到谁报汉的'是基于个人观察的事实性声称",
                "目标明确（回族/民族关系）"
            ],
            "counter_evidence": [
                "反问'那真的被黑被歧视吗'可解读为对少数民族受歧视经历的否认或轻视，有'扪心自问体'的语气",
                "'我还没看到'是个人有限观察，不能作为反歧视的充分证据",
                "如果原帖是在讨论回族受歧视的经历，则该回复可能是否认/削弱的对立立场"
            ],
            "final_rationale": "Risk: medium。文本通过反问（D1反讽）和简化论据质疑回族受歧视的事实，可能构成对少数民族受歧视经历的否认，但论证框架使其争议性有限。"
        }
    })
    yield s12

    # ── Sample 13 (003875) ──────────────────────────
    s13 = overwrite(samples[12], {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": False,
        "hard_negative": True,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本以吴亦凡（Kris Wu，加拿大籍华裔艺人）为例进行类比论证——'我也没因为吴亦凡是异性恋就讨厌所有异性恋啊'。核心论点是'性取向和道德水平不相关'，批评'因为谁谁谁做了坏事所以就讨厌这个人所属群体'的逻辑。",
                "文本明确反对群体偏见（'这段时间偏见吧？'），认为将个体的行为归咎于整个群体是错误的。",
                "这是一个清晰的反对成见和歧视的论证文本。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本使用清晰的类比论证和逻辑推理来表达反对偏见的立场，没有任何编码或掩盖。",
                "'这段时间偏见吧？'中的偏見一词是直接概念表达，不是编码。"
            ],
            "context_analysis": [
                "文本出现在lgbt_discussion话题下——吴亦凡的例子可能是对LGBT相关内容中某种偏见的回应。文本本身无风险，是反偏見论点的范例。"
            ],
            "supporting_evidence": [
                "明确反对群体归罪——'因为谁谁谁做了坏事所以就讨厌这个人的群体里的所有人。这是啥？这段时间偏见吧？'",
                "用具体实例（吴亦凡/异性恋）使论证直观化",
                "ToxiCN标注为toxic=0，符合文本的非攻击性"
            ],
            "counter_evidence": [
                "无。文本是标准反偏见论证。"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本通过类比论证（吴亦凡例子）明确反对基于个体行为仇恨整个群体的偏见，是反歧视立场。"
        }
    })
    yield s13

    # ── Sample 14 (003876) ──────────────────────────
    s14 = overwrite(samples[13], {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": ["C4_典故/物品/符号借用"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本激烈批评高校教育政策，称其'崇洋媚外'（崇拜外国、谄媚外国人）、'畸形'、'茶毒整个教育体制'（毒害整个教育体系），导致'校风败坏、以丑为美、以黑为荣、道德沦丧'。",
                "'以黑为荣'在此语境中意为'以黑人为荣/以黑皮肤为荣'——批评教育体系推崇黑人/外来文化。这是种族保守主义话语中的经典表述。",
                "'茶毒'是'荼毒'（毒害）的常见错别字，不影响语义。"
            ],
            "encoding_analysis": [
                "主要攻击是直接的（literal_keyword）：'崇洋媚外'、'畸形'、'茶毒'、'道德沦丧'等词汇都是直接的负面评价，没有编码包装。",
                "'以黑为荣'中的'黑'使用了C4符号借用——'黑'字在这里既是'黑色/黑人'的字面意义，也是'外来/异族文化'的象征性代称。",
                "没有使用平台黑话或隐喻编码——文本直接表达观点。"
            ],
            "context_analysis": [
                "贴吧语境中，'崇洋媚外'和'以黑为荣'是排外/种族保守话语中的常见口号。文本攻击对象是'教育政策'（机构层面）而非直接攻击黑人群体，但隐喻路径明确。",
                "不需要额外上下文——表达在种族保守话语中高度可识别。"
            ],
            "supporting_evidence": [
                "'崇洋媚外'是强烈的排外指责用语，暗示对本国文化的背叛",
                "'以黑为荣'明确将'黑'（黑人/外来文化）作为需要批判的对立面",
                "'畸形'、'败坏'、'沦丧'连续使用极端贬义词形成系统批判",
                "攻击对象虽然表面是教育政策，但'以黑为荣'暗指针对黑人群体的排外态度"
            ],
            "counter_evidence": [
                "文本表面攻击对象是'教育政策'而非直接攻击黑人群体。'以黑为荣'可能有多种解读（黑=黑暗面？黑=黑幕？），但在种族话题下歧义较小。"
            ],
            "final_rationale": "Risk: high。文本以direct_keyword（崇洋媚外、畸形、茶毒）为主，配合C4编码（以黑为荣），激烈攻击教育政策的外来文化包容取向，表达种族保守/排外立场。"
        }
    })
    yield s14

    # ── Sample 15 (003877) ──────────────────────────
    s15 = overwrite(samples[14], {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": False,
        "hard_negative": True,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "'别的不说，家暴确实不可取'——一个简短明确的反家暴声明。'别的不说'意味着说话者搁置争议/保留其他意见，但在家暴问题上立场明确：家暴不可取（unacceptable）。",
                "文本是对家庭暴力的明确谴责，没有任何歧义。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本使用直白的'不可取'（undesirable/unacceptable）表达反对立场，没有使用任何编码或修辞手段。"
            ],
            "context_analysis": [
                "标注为gender_discussion但内容是反家暴声明。在性别讨论中，家暴是一个高度相关的议题，该文本是在表达反对家暴的标准立场。",
                "不需要额外上下文。"
            ],
            "supporting_evidence": [
                "'家暴确实不可取'——明确的反对家暴立场",
                "ToxiCN标注为toxic=0",
                "反家暴是社会共识立场"
            ],
            "counter_evidence": [
                "无。文本没有任何攻击性或偏见内容。"
            ],
            "final_rationale": "Risk: none (hard_negative)。简短明确的反家暴声明，立场正面、表达直接、无任何攻击性内容。"
        }
    })
    yield s15

    # ── Sample 16 (003878) ──────────────────────────
    s16 = overwrite(samples[15], {
        "risk_level": "medium",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["D1_反讽"],
        "ambiguity": "medium",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "'正黄旗'是清朝八旗之一（Plain Yellow Banner），在此语境中代指具有满族/北京旗人身份背景的人。文本声称'正黄旗看不起人是事实'，然后反问'怎么这也叫黑'。",
                "'黑'在此语境中指'批评/抹黑'（如'地域黑'）。叙述者认为指出正黄旗'看不起人'不是抹黑而是事实陈述。",
                "文本涉及一个历史性/地域性的负面刻板印象（旗人/北京人的傲慢）。"
            ],
            "encoding_analysis": [
                "'正黄旗'使用C4_典故/符号借用编码——用特定的历史建制名称（八旗之一）指代整个具有旗人/北京本地人身份的群体，通过历史典故进行群体代指。",
                "'怎么这也叫黑'使用了D1_反讽编码——假装不解的疑问形式，实际是在主张'这就是事实，不是黑'。带有挑衅/理直气壮的语气。"
            ],
            "context_analysis": [
                "在网络语境中，'正黄旗'常被用作对北京本地（尤其是老北京/满族背景）人的贬称或刻板印象标签。",
                "需要上下文：如果原帖是在批判地域歧视，该回复是在质疑'歧视'的标签——可能是在'歧视不算歧视'方向上的论证。"
            ],
            "supporting_evidence": [
                "'正黄旗看不起人是事实'——将一个负面特征归因于一个群体并声称是'事实'",
                "'怎么这也叫黑'——对歧视标签的质疑，带有轻视语气",
                "使用了历史典故（正黄旗）来代指当代群体"
            ],
            "counter_evidence": [
                "文本可能是在讨论一个具体的'正黄旗'相关的帖子/事件，并非一般性攻击整个群体",
                "'看不起人'是一个可讨论的行为特征，不一定是严重的攻击",
                "反问句式'怎么这也叫黑'可读为对过度使用'黑'标签的疲惫反应"
            ],
            "final_rationale": "Risk: medium。文本通过C4编码（正黄旗历史典故）对特定群体进行负面特征归因，并配合D1反讽质疑'歧视'标签，有地域/群体刻板印象风险。"
        }
    })
    yield s16

    # ── Sample 17 (003879) ──────────────────────────
    s17 = overwrite(samples[16], {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "high",
        "evidence_strength": "weak",
        "needs_context": True,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "'我只说一句，现在皈依伊斯兰还来得及。'——极度简短的陈述，建议某人/某群体皈依伊斯兰教。",
                "在缺乏上下文的情况下，这句话有多种可能的解读：①讽刺性建议（如：只有伊斯兰教能拯救你）；②善意建议（如：考虑伊斯兰教）；③对某个话题的终结性评论。",
                "文本本身没有任何攻击性词汇或明确的歧视内容。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是简单直白的陈述句，没有使用任何编码或修辞手段。",
                "'皈依伊斯兰'是常规宗教术语。"
            ],
            "context_analysis": [
                "标注为gender_discussion但文本是宗教建议，与性别话题完全不相关。",
                "缺乏上下文——不知道谁在皈依什么。可能是在特定性别讨论中引用宗教来解决某个性别争议。但文本本身的风险完全取决于上下文。",
                "应标为需要上下文。"
            ],
            "supporting_evidence": [
                "文本没有包含任何攻击性词汇或编码",
                "ToxiCN标注为toxic=0",
                "宗教建议本身不构成风险"
            ],
            "counter_evidence": [
                "在性别讨论语境中突然插入宗教皈依建议可能具有特定立场（如伊斯兰教法对性别角色的特定规定），但文本本身不包含任何论证或攻击。",
                "极度歧义——没有上下文无法准确评估"
            ],
            "final_rationale": "Risk: none (hard_negative)。极度简短且歧义性强的文本，没有攻击性词汇或歧视内容。风险完全取决于不可知的上下文，文本本身无风险。"
        }
    })
    yield s17

    # ── Sample 18 (003880) ──────────────────────────
    s18 = overwrite(samples[17], {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": False,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本以新闻播报风格描述一个事件：外籍男子醉酒闹事并袭警，被制服后群众拍手叫好。",
                "这是典型的社会新闻/事件描述。'群众纷纷拍手叫好'表达了对警方执法行为（制服肇事者）的群众支持。",
                "文本没有使用任何攻击性词汇或表达任何群体偏见。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是客观式的新闻报道语言，没有使用编码或攻击性修辞。",
                "'外籍男子'是对肇事者的中性描述，没有负面修辞加注。"
            ],
            "context_analysis": [
                "标注为race_discussion——如果该新闻事件被用于推广'外国人素质差'的刻板印象，则原帖可能具有排外色彩。但此文本本身仅是中性事件叙述。",
                "文本本身作为孤立样本不构成风险。"
            ],
            "supporting_evidence": [
                "中性的事件描述语言，无攻击性词汇",
                "'外籍男子'是中性称谓，未使用贬义代称",
                "ToxiCN标注为toxic=0",
                "'拍手叫好'是对执法结果的反应，不是种族反应"
            ],
            "counter_evidence": [
                "在讨论'外籍'相关事件的上下文中，选择报道此类事件本身可能具有选择性曝光的倾向，但单条文本无法判断。",
                "文本标签为race_discussion，说明该新闻被置于种族讨论的语境中。"
            ],
            "final_rationale": "Risk: none (hard_negative)。中性新闻式事件描述，无攻击性词汇或编码，硬性negative样本。"
        }
    })
    yield s18

    # ── Sample 19 (003881) ──────────────────────────
    s19 = overwrite(samples[18], {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": False,
        "hard_negative": True,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本是一段系统性的反种族主义论述。论点包括：①'按皮肤归纳人种本来就不对'——批评以肤色划分人种；②黑人智力差异主要是教育原因；③黑人精英存在的客观事实；④来中国做生意的黑人往往是有能力的；⑤建议'尊重一些还是能做到的'。",
                "叙述者承认'文化处不来'（文化差异），但同时强调尊重和做生意没问题。整体立场是理性、谨慎的反偏见。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本使用清晰的说理结构论证反种族主义观点，没有使用任何编码或间接表达。",
                "'文化处不来'是诚实地承认文化差异，不是编码或歧视。"
            ],
            "context_analysis": [
                "在race_discussion话题下，此文本展示了理性和克制地讨论种族问题的模式。既有反偏见的明确立场，又承认文化差异的客观存在。",
                "不需要额外上下文，文本自足。"
            ],
            "supporting_evidence": [
                "'按皮肤归纳人种本来就不对'——直接批评种族分类",
                "'黑人不聪明很多是教育的原因'——用环境因素解释智力差异，而非种族本质论",
                "'能到中国做生意的黑人，很多时候也是非洲比较聪明厉害有行动力的'——承认能力和多样性",
                "'尊重一些还是能做到的'——明确表达尊重立场"
            ],
            "counter_evidence": [
                "'文化处不来'可能被解读为文化本质主义的表述，但联系上下文（'就文化我们和他们处不来，但是做生意，尊重一些还是能做到的'），是承认差异+提倡尊重的模式。"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本是系统性的反种族主义/反偏见论述，承认差异但明确主张尊重。"
        }
    })
    yield s19

    # ── Sample 20 (003882) ──────────────────────────
    s20 = overwrite(samples[19], {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本讨论河南的地域刻板印象——'河南这个谁还当真了？电信诈骗又不是河南最多，现在谁看见被偷的井盖还会在心里默念是河南人偷的'。",
                "'河南人偷井盖'是中文互联网历史悠久的河南地域黑梗。文本指出这个梗's已不再流行/不再被当真。",
                "文本不是在传播刻板印象，而是在说刻板印象已经过时了/不再有效。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是对地域刻板印象现状的评述，使用直白语言。'井盖'梗是公众已知的刻板印象的引用，不是编码。",
                "没有使用反讽——文本是认真在说刻板印象不再被当真。"
            ],
            "context_analysis": [
                "标注为region_reporting——符合文本的'评论地域刻板印象现状'的性质。",
                "需要原帖上下文：如果原帖是在传播河南刻板印象，此回复是反驳/制止；如果原帖是反对刻板印象，此回复是附和。但无论如何，文本本身不构成攻击。"
            ],
            "supporting_evidence": [
                "'谁还当真了'——质疑刻板印象的可信度",
                "'电信诈骗又不是河南最多'——用事实论据反驳",
                "'现在谁看见被偷的井盖还会在心里默念是河南人偷的'——暗示刻板印象已经过时"
            ],
            "counter_evidence": [
                "提及井盖梗和电信诈骗梗本身可能重新激活这些刻板印象，但叙述者明显是在否定它们的有效性。"
            ],
            "final_rationale": "Risk: low。文本对河南地域刻板印象的现状进行评述，立场是否定刻板印象的有效性而非传播偏见，但刻板印象的提及本身有一定风险。"
        }
    })
    yield s20

    # ── Sample 21 (003883) ──────────────────────────
    s21 = overwrite(samples[20], {
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
                "文本叙述个人经历：被人用学历攻击（'说我不用写作业不上学是文盲辍学者'），然后回应'我寻思着这个社会上还在上学的才是少数吧'。",
                "叙述者认为自己被攻击是因为没学历，随后反问指出社会上大部分人都不是在学生身份。这是一个关于学历/工作歧视的个人回应。",
                "文本与种族话题完全无关。话题标签race_reporting有误。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是个人经历的直白叙述。'喷我'=攻击我/骂我，是网络通用口语，不是编码。",
                "没有使用反讽——'我寻思着'是口语开头，后面的反问句是理性的观察陈述。"
            ],
            "context_analysis": [
                "话题标签为race_reporting但与种族无关——可能是数据集标注错误。内容是关于学历/教育背景的社会偏见。",
                "需要原帖上下文来理解为什么这个关于学历歧视的回复被归类为race_reporting。"
            ],
            "supporting_evidence": [
                "文本清楚说明被攻击的原因是学历（'拿学历说事'）",
                "'社会上还在上学的才是少数吧'——回应关于'不上学'的指责",
                "没有涉及任何种族内容"
            ],
            "counter_evidence": [
                "如果原帖讨论的是某种族的教育差异话题，此回复可能是在该语境下对批评的回应。但文本本身不涉及种族。"
            ],
            "final_rationale": "Risk: low。文本叙述个人被学历攻击的经历并作出回应，内容关于教育/社会偏见，与种族无关。风险来自话题标签与内容的不匹配。"
        }
    })
    yield s21

    # ── Sample 22 (003884) ──────────────────────────
    s22 = overwrite(samples[21], {
        "risk_level": "medium",
        "encoding_primary": "D1_反讽",
        "encoding_secondary": ["literal_keyword"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本转述并嘲讽一些广东人的观点：自称'汉族正统'、称北方人为'胡杂'（胡人杂种）。然后叙述者假装附和：'你们说的都对，华夏发源地都在广东好不好😆😆😆'。",
                "'胡杂'是极端的地域/族群侮辱词，指北方人是'胡人'（古代中原对北方游牧民族的贬称）的杂种后代。",
                "叙述者通过夸张的方式（'华夏发源地都在广东'）表达对上述观点的嘲讽——这显然不是真的认同。"
            ],
            "encoding_analysis": [
                "整段话使用D1_反讽编码——叙述者假装同意'正统汉人在广东、华夏发源地在广东'的夸张claim，实际是在嘲讽。结尾的😆😆😆表情符号明确表示这是玩笑/嘲讽。",
                "'胡杂'是直接的地域/族群侮辱词（literal_keyword），在原转述中使用。'正统汉人'、'纯正血统'也是使用原文的直接词汇。"
            ],
            "context_analysis": [
                "文本明显是在嘲讽'广东人自称正统汉人'的地域文化优越论。虽使用了'胡杂'等强烈的族群标签，但这是在转述和批判他人的言论。",
                "不需要额外上下文——反讽意图通过😆😆😆明确表达。"
            ],
            "supporting_evidence": [
                "'你们说的都对'——反讽标志，字面同意但实际否定",
                "'华夏发源地都在广东好不好😆😆😆'——明显夸张到荒谬程度的'承认'",
                "表情符号😆😆明确了嘲讽语气",
                "转述'胡杂'是为了批评而非认同该说法"
            ],
            "counter_evidence": [
                "使用了'胡杂'这一极端族群侮辱词（即使是转述），可能造成该词的二次传播",
                "反讽可能被误读——部分读者可能无法识别反讽意图而误以为是地域攻击"
            ],
            "final_rationale": "Risk: medium。文本使用D1反讽编码嘲讽地域文化优越论（广东人自称正统汉人），虽转述了极端词汇'胡杂'但明显是在批判而非认同时，反讽的模糊性带来一定风险。"
        }
    })
    yield s22

    # ── Sample 23 (003885) ──────────────────────────
    s23 = overwrite(samples[22], {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本从进化心理学/生物学角度解释人类的厌恶反应——'吃屎不卫生'，类比尸体和密集事物引发厌恶是因为它们代表'疾病、死亡'，基因编码了这些厌恶反应以保护生存。",
                "这是在讨论进化论/生物学中的厌恶机制(harm/disgust avoidance theory)。使用'吃屎'、'尸体'、'密集'作为例子。",
                "文本完全是科学式的讨论，没有任何攻击性。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本使用进化生物学的解释框架讨论人类本能反应，是学术/科普式的论证表达。",
                "'吃屎'虽然是粗俗词汇但在此语境中是作为生物学例子使用，不是编码攻击。"
            ],
            "context_analysis": [
                "标注为lgbt_discussion——文本讨论的是进化心理学中的厌恶机制，可能与LGBT话题的某些论证有关（如同性恋厌恶的进化根源）。但文本本身使用中性学术框架。",
                "需要上下文才能理解该进化解释与LGBT话题的具体关联。"
            ],
            "supporting_evidence": [
                "文本使用生物学/学术框架讨论厌恶反应",
                "没有针对任何群体或个人",
                "ToxiCN标注为toxic=0"
            ],
            "counter_evidence": [
                "厌恶机制的进化解释曾被用于'论证'对同性恋的厌恶是'自然的'从而为恐同辩护。该文本的学术框架在LGBT话题语境中可能被用来支持反同观点，但文本本身没有这种指向。"
            ],
            "final_rationale": "Risk: none (hard_negative)。学术性的进化心理学讨论，无攻击性内容。虽出现在LGBT话题中但文本本身持中性论述框架。"
        }
    })
    yield s23

    # ── Sample 24 (003886) ──────────────────────────
    s24 = overwrite(samples[23], {
        "risk_level": "medium",
        "encoding_primary": "D1_反讽",
        "encoding_secondary": ["literal_keyword"],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本以反讽语气回应某种观点：如果要嫁外国人且不要彩礼的女生都出国不要回来，那应该都走了，'可惜好像不是呢'——暗示实际情况并非如此。",
                "'不要外国人彩礼且结果的女生'指的是与外国人结婚且不要求彩礼的中国女性。叙述者质疑'要求她们出国'的极端主张，用事实（没都走）来反驳。",
                "文本隐含对中国女性嫁外国人的负面态度——将'不要彩礼嫁外国人'视为需要惩罚的行为（'出国不要回来'），然后用事实（没走）来讽刺。"
            ],
            "encoding_analysis": [
                "'那就应该是……可惜好像不是呢'是典型的D1_反讽句式——提出极端假设然后指出现实不符，从而讽刺原主张也者是讽刺现象。",
                "'全都出国不要回来'是极端化表述，用于放大论证的荒谬性。"
            ],
            "context_analysis": [
                "在race_discussion话题下，文本是在回应关于中外婚姻的讨论。文本对中国女性嫁外国人的态度有负面倾向——至少在质疑这种选择的合理性。",
                "需要原帖上下文来完全理解文本的批评指向。"
            ],
            "supporting_evidence": [
                "反讽句式'那就应该是……'提出极端化主张",
                "'可惜好像不是呢'——用事实反讽，语气带轻视",
                "目标群体明确（与外国人结婚的中国女性）"
            ],
            "counter_evidence": [
                "文本的反讽对象可能是原帖的极端主张而非中国女性本身",
                "没有直接使用攻击性词汇——通过逻辑和事实进行反驳"
            ],
            "final_rationale": "Risk: medium。文本通过D1反讽质疑中外婚姻的选择（不要外国人彩礼且结果），隐含对中国女性嫁外国人选择的负面态度，但攻击通过逻辑反驳而非直接侮辱。"
        }
    })
    yield s24

    # ── Sample 25 (003887) ──────────────────────────
    s25 = overwrite(samples[24], {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "'他自称，想演变态同性恋，他是反同态度吗？'——文本引用某个人的自述（'想演变态同性恋'），然后提出问题：这个人是不是反同？",
                "文本本身是在提问/质疑一个人的立场。'演变态同性恋'是引用他人的原话——'变态同性恋'这个词本身是贬义的，但在此是转述。",
                "叙述者不清楚这个人的立场（反同？），试图通过分析其语言来推断。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是直接提问，转述他人的语言并请求判断。",
                "'变态同性恋'虽然带有贬义色彩，但此处是转述他人的自称/原话。"
            ],
            "context_analysis": [
                "出现在lgbt_discussion话题下。文本似乎是在讨论'一个人自称想变成同性恋是否表明此人是反同'这个语言使用问题。",
                "需要上下文了解'他'是谁以及整个对话背景。"
            ],
            "supporting_evidence": [
                "文本是在提问/分析，而不是发表个人攻击",
                "'他自称'——明确表示转述他人的自称",
                "没有表达叙述者自身的反同立场"
            ],
            "counter_evidence": [
                "转述'变态同性恋'一词可能被误解为叙述者本人的用词",
                "缺乏上下文——不知道'他'指的是谁"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本转述他人的自称并提问分析其立场，文本本身不表达个人攻击或偏见。"
        }
    })
    yield s25

    # ── Sample 26 (003888) ──────────────────────────
    s26 = overwrite(samples[25], {
        "risk_level": "high",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["literal_keyword"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本包含多个种族侮辱词：'国际鬼子'（鬼子原指侵华日军，这里扩展为泛指外国人/敌人）、'黑猩猩'（对黑人的动物化种族侮辱）、'猩混'（混血儿的动物化侮辱）、'野生动物'、'生物物种间'。",
                "文本将人类群体描述为不同的'生物物种'和'野生动物'，推行极端的种族非人化和种族隔离观点。",
                "叙述者论证的是'不同'生物物种之间'它们自己'内部的歧视——是在嘲讽/讨论种族歧视概念，但使用的词汇本身就是极端的种族侮辱。"
            ],
            "encoding_analysis": [
                "'国际鬼子'使用C4_典故编码——鬼子是抗日战争时期对日军的贬称，此处扩展使用。'黑猩猩'使用C4_符号借用编码——用动物指代人类群体。",
                "'猩混'是创造性的混合词（猩猩+混血），也是一种C4+literal_keyword的复合编码。",
                "其余'野生动物'、'它们'、'生物物种'等是直接的动物化/非人化表达（literal_keyword）。"
            ],
            "context_analysis": [
                "贴吧匿名环境允许这类极端种族言论的传播。文本结构复杂、用词创新（'猩混'），显示作者有意使用多种编码手段来包装种族攻击。",
                "不需要额外上下文——种族攻击意图和手段都非常明确。"
            ],
            "supporting_evidence": [
                "'黑猩猩'是中文互联网中对黑人的经典动物化侮辱词",
                "'猩混'是创新的复合侮辱词——将混血儿与猩猩类比",
                "'国际鬼子'将华人以外的人泛化为'敌人'",
                "全文使用'它们'和'生物物种'框架进行非人化"
            ],
            "counter_evidence": [
                "文本似乎在'讨论'种族歧视（'它们自己生物物种间的自己物种歧视'），这可能是一种反讽式的揭露而非直接的种族攻击。但即便如此，使用的词汇本身就是极端的种族侮辱。"
            ],
            "final_rationale": "Risk: high。使用多个C4编码（鬼子/黑猩猩/猩混）和动物化语言对黑人和混血儿进行极端种族非人化攻击，编码手段多样但攻击意图明确。"
        }
    })
    yield s26

    # ── Sample 27 (003889) ──────────────────────────
    s27 = overwrite(samples[26], {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本叙述亲身经历：在南京读书时，英语老师是南京本地人，批评学生时用南京脏话；班上老师对外地学生存在明显歧视。",
                "这是对地域歧视经历的第一人称叙述——叙述者可能是外地学生，亲身感受到了歧视。内容包含对南京教师行为的批评。",
                "'南京市骂'指南京方言中的脏话/侮辱用语。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是个人经历的直白叙述（reporting），使用叙事语言描述教师的歧视行为。没有使用编码或修辞手段。"
            ],
            "context_analysis": [
                "标注为region_reporting——符合文本的'揭露地域歧视经历'的性质。",
                "叙述者站在被歧视者（外地学生）的立场，揭露教师的歧视行为。文本是反地域歧视的证据报告而非传播歧视。"
            ],
            "supporting_evidence": [
                "文本描述了具体的歧视行为（老师对外地学生'明显的歧视'）",
                "叙述者是受害者或目击者立场",
                "'印象最深'、'明显'——表达了对歧视的确切感受"
            ],
            "counter_evidence": [
                "文本没有明确批评老师的歧视行为，只是客观描述了经历。'也能感觉出'的措辞较为谨慎。但整体是揭露性质。"
            ],
            "final_rationale": "Risk: low。个人经历的客观叙事，描述教师的地域歧视行为，叙述者站在被歧视者立场，属于揭露/报告性质。"
        }
    })
    yield s27

    # ── Sample 28 (003890) ──────────────────────────
    s28 = overwrite(samples[27], {
        "risk_level": "low",
        "encoding_primary": "E3_互动/热点触发",
        "encoding_secondary": ["D1_反讽"],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本批评答主（原帖作者）将反同偏见包装成体面的说法——'答主把自己反同性恋，歧视同性恋的倾向换一种说法说得如此清新脱俗也是醉了。'",
                "'清新脱俗'在此语境中使用D1反讽，字面夸奖但在批评语境中意为'真会美化自己'。'也是醉了'是网络用语表示无语/服了。",
                "文本立场是揭露和批评原帖作者的同性恋歧视倾向——正在呼唤歧视而非传播歧视。"
            ],
            "encoding_analysis": [
                "文本是对原帖作者的回应（E3_互动触发）——'答主'（楼主）表明是在回帖语境中，针对他人言论的批评。",
                "文本使用D1_反讽编码——字面意思是赞扬优雅脱俗，实际是讽刺对方巧妙包装偏见。"
            ],
            "context_analysis": [
                "标注为lgbt_reporting——符合揭露原帖反同倾向的性质。文本是反偏见立场——批评原帖的隐性恐同。",
                "需要原帖上下文来确认'换一种说法'具体指什么，但文本本身的批评立场是清晰的。"
            ],
            "supporting_evidence": [
                "直接指出答主的'反同性恋、歧视同性恋的倾向'",
                "'换一种说法说得如此清新脱俗'——指出编码和包装行为",
                "'也是醉了'表达对掩饰偏见的无奈/反感"
            ],
            "counter_evidence": [
                "反偏见文本本身通常不构成风险。但'歧视同性恋的倾向'的指控需要原帖证据支撑。"
            ],
            "final_rationale": "Risk: low。文本揭露和批评原帖作者包装反同偏见的做法，是反偏见立场，使用D1反讽批评对方，风险低。"
        }
    })
    yield s28

    # ── Sample 29 (003891) ──────────────────────────
    s29 = overwrite(samples[28], {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "medium",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本由两部分组成：①批评某人作为一个'无知的人'，通过'极端又片面的例子'发表对一个群体的'主观憎恨言论'——这是在批评发表仇恨言论的人。②'别人问候你父母也是合情合理的🙂'——说对表恨言论者的反击（问候父母=诅咒）是合理的。",
                "第一部分是明确的anti-hate立场——批评使用极端例子发表群体仇恨的人。第二部分比较复杂：叙述者认为对仇恨言论者的反击是合理的。",
                "'问候你父母'（问候=诅咒/骂人）和'合情合理'（合理）构成了一个从道德层面正当化反击的表述。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本使用直白的语言批评仇恨言论并论证反击的合理性。",
                "'问候你父母'是中文网络中的常见委婉说法（代指谩骂/诅咒），但在此语境中是直接表述而非编码。"
            ],
            "context_analysis": [
                "标注为lgbt_discussion——文本可能在批评某个发表反同言论的人。叙述者站在反对仇恨言论的立场。",
                "需要原帖上下文来理解'极端又片面的例子'具体指什么，以及被批评的群体仇恨具体内容。"
            ],
            "supporting_evidence": [
                "文本明确批评'对一个群体的主观憎恨言论'——这是反仇恨立场",
                "批评对方'举极端又片面的例子'——指对方论证不公",
                "'在这方面很无知'——攻击的是对方的无知而非群体身份"
            ],
            "counter_evidence": [
                "'问候你父母也是合情合理的'可能被解读为正当化网络暴力/人身攻击",
                "虽然批评的是仇恨言论，但'问候父母'的合法性主张可能引发争议"
            ],
            "final_rationale": "Risk: low。文本批评仇恨言论发表者，是反偏见立场；但后半部分正当化'问候父母'式的反击具有争议性，略高于none。"
        }
    })
    yield s29

    # ── Sample 30 (003892) ──────────────────────────
    s30 = overwrite(samples[29], {
        "risk_level": "low",
        "encoding_primary": "E3_互动/热点触发",
        "encoding_secondary": ["literal_keyword"],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本比较成都和河南的'被黑'程度——'成都还没说话呢😅在知乎被黑都，成都称第二，没人敢称第一'，然后使用河南的刻板印象梗（'去把他家门口的井盖偷了都轮不到'）来表达'成都被黑得更严重'。",
                "'井盖'梗是经典的河南地域黑。叙述者使用该梗来暗示：即使在偷井盖这个刻板印象上，河南都不是最被黑的，成都才是。",
                "文本是在调侃地域黑的排名/竞争，而非刻意攻击某个地域群体。但使用了已知的地域刻板印象。"
            ],
            "encoding_analysis": [
                "文本是对原帖的回应（E3_互动触发）——'成都还没说话呢'说明是在延续原帖讨论。",
                "'井盖'梗是引用已知的刻板印象符号，不是编码手段。"
            ],
            "context_analysis": [
                "标注为region_reporting——文本在讨论和比较地域被黑的程度。虽有玩梗性质但内容涉及敏感的地域刻板印象。",
                "需要原帖上下文来理解整个对话的基调和目的。"
            ],
            "supporting_evidence": [
                "文本核心是比较不同地区的被黑程度",
                "使用河南梗（井盖）作为排名的比较基准",
                "整体语气是调侃而非恶意攻击"
            ],
            "counter_evidence": [
                "使用'井盖'梗可能强化河南的刻板印象（即使是在比较语境中）",
                "将地域'被黑'作为竞争话题本身可能鼓励地域歧视话语"
            ],
            "final_rationale": "Risk: low。文本以调侃语气比较成都和河南的'被黑'程度，使用已知的刻板印象梗（井盖）但非恶意攻击，属于地域话题中的低风险讨论。"
        }
    })
    yield s30

    # ── Sample 31 (003893) ──────────────────────────
    s31 = overwrite(samples[30], {
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
                "文本使用类比论证：穷人家即使家徒四壁也需要防盗门（因为贼是外部威胁），从而推出论点——'同性恋是贼'（类比威胁），'不管怎么都应该提防变态基佬'。",
                "'同性恋是贼'——这是一个明确的'同性恋=威胁'的映射。'变态基佬'是直接用贬义词指称同性恋男性，'提防'进一步强化了'同性恋=危险的陌生人'的框架。",
                "文本结构：穷人也要防盗门（前提）→ 同性恋是贼（暗含类比）→ 所以应该提防基佬（结论）。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本直接使用了攻击性词汇'变态基佬'和'提防'——这是直接的反同表达。",
                "'基佬'是中文中对gay men的常见贬称（相当于英文faggot的轻蔑程度），没有编码包装。",
                "类比论证（防盗门/同性恋是贼）是修辞手段而非编码。"
            ],
            "context_analysis": [
                "在lgbt_discussion话题下，文本明确表达了对同性恋男性的恐惧和敌意——'提防变态基佬'。该攻击是直接的，不需要额外上下文。",
                "定位明确——攻击对象是同性恋男性群体。"
            ],
            "supporting_evidence": [
                "'同性恋是贼'——直接的'同性恋=威胁'的比拟",
                "'变态基佬'——使用明确的贬义词指称同性恋男性",
                "'提防'——暗示同性恋者是需要警惕的危险人物",
                "全文结构构建了'同性恋=需要防范的外部威胁'的叙事"
            ],
            "counter_evidence": [
                "文本使用了类比（防盗门/贼）的论证结构，可以解读为对某种社会现象（'变态基佬'）的个人防范建议，而非一般性攻击全体同性恋者。但'同性恋是贼'的概括过于宽泛。"
            ],
            "final_rationale": "Risk: high。文本直接使用'变态基佬'贬称并构建'同性恋=需要提防的贼'的威胁叙事，是明确的反同攻击，目标明确、表达直接。"
        }
    })
    yield s31

    # ── Sample 32 (003894) ──────────────────────────
    s32 = overwrite(samples[31], {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本讨论南京话（方言）的特点——最接近普通话、带脏话、南部高淳的话难懂。根据个人大学中与江苏各地同学的交流经验。",
                "这是典型的方言/地域语言讨论，中性与知识分享性质。",
                "'除了有点脏话'——提及方言中带脏话成分是语言事实描述。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是方言话题的个人经验分享，没有使用任何编码或攻击性表达。",
                "'脏话'是直接描述，不是编码。"
            ],
            "context_analysis": [
                "标注为region_discussion——符合文本讨论地域方言的性质。文本是中性的文化/语言交流。",
                "需要上下文了解该方言讨论是在什么话题下进行。"
            ],
            "supporting_evidence": [
                "中性描述方言差异，无攻击性",
                "'感觉南京话就是最接近普通话的'——个人观点",
                "ToxiCN标注为toxic=0"
            ],
            "counter_evidence": [
                "无。文本是中性方言讨论。"
            ],
            "final_rationale": "Risk: none (hard_negative)。中性方言话题的讨论，无任何攻击性或偏见表达。"
        }
    })
    yield s32

    # ── Sample 33 (003895) ──────────────────────────
    s33 = overwrite(samples[32], {
        "risk_level": "medium",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "'我是不觉得广东人长得好看'——一个简短的个人审美偏好声明，但对一个地域群体的外貌进行了概括性负面评价。",
                "严格来说这是对'广东人'这一群体外观的负面刻板印象表达——'不觉得……好看'意味着否定了整个群体的外貌。",
                "语气是主观的（'我是不觉得'），但内容是对群体的概括性评价。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本直接表达了负面群体评价，没有使用编码进行包装或掩饰。",
                "'不觉得……好看'是直白的否定表达。"
            ],
            "context_analysis": [
                "在region_discussion话题下，该评论可能出现在关于广东人/南方人外貌的讨论串中。虽然是个人审美表达，但涉及地域群体外貌的概括性负面评价。",
                "需要上下文来判断是否是恶意攻击还是普通的审美表达差异。"
            ],
            "supporting_evidence": [
                "'广东人'——明确以地域群体为评价对象",
                "'不觉得……好看'——对群体的负面审美评价",
                "地域外貌的概括性评价属于地域偏见的范畴"
            ],
            "counter_evidence": [
                "'我是不觉得'表明是个人主观审美偏好，不是攻击性言论",
                "简短的个人意见表达，没有使用任何侮辱性词汇或极端表述",
                "可能在回应某种'广东人好看'的论调"
            ],
            "final_rationale": "Risk: medium。对广东人群体外貌的概括性负面审美评价构成地域偏见，但表达为个人意见且未使用攻击性词汇，介于轻度偏见和日常刻板印象之间。"
        }
    })
    yield s33

    # ── Sample 34 (003896) ──────────────────────────
    s34 = overwrite(samples[33], {
        "risk_level": "medium",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": ["E1_平台黑话"],
        "ambiguity": "medium",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "'她们也就知道几个娘炮了，你说对吧彦祖'——'她们'指女性群体，'娘炮'是贬低男性阴柔气质/同性恋男性的侮辱词，'彦祖'指代吴彦祖（帅男代称）。",
                "文本含义：女性只知道少数'娘炮'（不认识的/不帅的男性被视为娘炮），而真正的男性（像吴彦祖/我这样的）女性不认识。暗含对女性审美能力的贬低和对'娘炮'（不阳刚男性）的贬低。",
                "'你说对吧彦祖'——称呼对方为'彦祖'是互动的调侃，表明这位回帖者/读者在叙述者看来是真正的帅哥。"
            ],
            "encoding_analysis": [
                "'娘炮'是直接的贬义关键词（literal_keyword），是对非传统男性/同性恋男性的蔑称。",
                "'彦祖'使用E1_平台黑话编码——吴彦祖作为'帅男'的代称在贴吧社区中是固定用法，类似于'说帅哥=彦祖'的社区黑话。",
                "'她们也就知道几个'——暗示女性孤陋寡闻。"
            ],
            "context_analysis": [
                "在gender_discussion话题下，文本涉及性别刻板印象。'娘炮'同时涉及性别和性取向维度。",
                "需要上下文——如果可以确定'她们'和'彦祖'的具体所指，能更准确判断攻击性。"
            ],
            "supporting_evidence": [
                "'娘炮'是贬低男性非阳刚气质的侮辱性词汇",
                "'她们也就知道几个'——对女性识人能力的轻视",
                "整段话在性别刻板印象框架下贬低女性和阴柔男性"
            ],
            "counter_evidence": [
                "'彦祖'的调侃语气表明这是一个轻松的互动场合，可能攻击性有限",
                "'她们也就知道几个娘炮'可能是对特定话题的回应而非一般性攻击"
            ],
            "final_rationale": "Risk: medium。文本使用literal_keyword'娘炮'+E1黑话'彦祖'，在性别框架下贬低女性和非阳刚男性，但调侃语气使其强度有限。"
        }
    })
    yield s34

    # ── Sample 35 (003897) ──────────────────────────
    s35 = overwrite(samples[34], {
        "risk_level": "low",
        "encoding_primary": "E1_平台黑话",
        "encoding_secondary": ["literal_keyword"],
        "ambiguity": "high",
        "evidence_strength": "weak",
        "needs_context": True,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "'跑到反同群里面开盒，真的是狗啊'——'开盒'=开盒/人肉搜索（doxxing），'狗'=狗（骂人）。文本批评进入反同群并进行开盒行为的人，称他们为'狗'。",
                "文本的攻击对象是'开盒者'（实施人肉搜索的人），而非LGBTQ群体。'反同群'是描述性提及。",
                "文本的批评方向是谴责开盒行为——开盒是一种网络暴力行为。"
            ],
            "encoding_analysis": [
                "'开盒'使用E1_平台黑话编码——'开盒/开盒'是网络社区中对人肉搜索的特定黑话称呼，源于游戏/直播社区。",
                "'真的是狗啊'是直接的侮辱性表达（literal_keyword），'狗'在此是骂人用词。"
            ],
            "context_analysis": [
                "标注为lgbt_discussion——文本提到'反同群'，表明这个讨论与性取向话题有关。但文本批评的是开盒行为而非表达对同性恋的态度。",
                "高度歧义——文本有至少两种解读：①说话者在反同群中，批评来开盒的人（亲反同立场）；②说话者批评那些进入反同群进行开盒的人（反开盒立场）。",
                "缺乏上下文无法确定叙述者的性取向立场。"
            ],
            "supporting_evidence": [
                "文本明确批评'开盒'行为——谴责网络暴力",
                "'真的果狗啊'的愤怒指向开盒者举而非反同群本身",
                "'反同群'是中性描述"
            ],
            "counter_evidence": [
                "无法判断叙述者是否赞同反同群的内容——'跑到反同群里面开盒'可能暗示开盒者'攻击错了对象'",
                "'狗'是强烈的辱骂词汇，攻击情绪强烈",
                "缺乏上下文——有'叙述者在反同群中'或'叙述者在批评对反同群的开盒行为'两种完全不同的解读"
            ],
            "final_rationale": "Risk: low。文本批评进入反同群进行开盒的行为，攻击对象是开盒者而非LGBTQ群体。但叙述者立场因缺乏上下文存在歧义，标为低风险。"
        }
    })
    yield s35

    # ── Sample 36 (003898) ──────────────────────────
    s36 = overwrite(samples[35], {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本讨论汉族祖先与河南人的关系：承认'汉人祖先都是中原来的'但反对'河南人是全中国人祖宗'的优越感论调。叙述者讲述祖先'从中原来走南闯北抢占异族生存空间开疆拓土'的历史叙事。",
                "核心论点：不要因河南在中原而产生'河南人是祖宗'的优越感。'抢占异族生存空间'使用了历史扩张话语，但对'异族'的提及可能引发种族联想。",
                "文本结尾称'看到网上一群说河南人是外地人祖宗的 给你们拉仇恨'——认为这种论调是给河南人招黑。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是历史/地域话题的论述，直接表达观点和论据。",
                "'抢占异族生存空间'虽然使用'异族'这个词，但在历史叙述语境中是对汉族扩张史的客观描述，不是编码攻击。"
            ],
            "context_analysis": [
                "标注为region_reporting——符合文本对河南与其他地区关系的探讨性质。",
                "文本立场：反对河南人祖先优越论，强调汉族祖先的多元扩张历史。"
            ],
            "supporting_evidence": [
                "明确反对'河南人是全中国人祖宗'的优越论",
                "提供历史论据支持观点",
                "结尾'给你们拉仇恨'——认为部分河南人的言论反而损害了河南形象"
            ],
            "counter_evidence": [
                "'抢占异族生存空间'在当代语境中可能被解读为对少数民族的遗忘或否定",
                "对河南人优越论的批评可能被极端化为对整个河南群体的攻击，但该文本本身有具体明确的反驳对象"
            ],
            "final_rationale": "Risk: low。文本反驳'河南人是全中国人祖宗'的优越论，虽是地域话题争论但立场是反对优越感而非攻击群体。"
        }
    })
    yield s36

    # ── Sample 37 (003899) ──────────────────────────
    s37 = overwrite(samples[36], {
        "risk_level": "high",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["D1_反讽"],
        "ambiguity": "medium",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "'现在辩证的来看小胡子错就错在输了战争'——'小胡子'是希特勒（Hitler）的互联网代称/编码（因希特勒的经典小胡子形象），'错就错在输了战争'暗示希特勒唯一错误是战败。",
                "文本使用'辩证地来看'（dialectically）作为伪装性的学术框架，实际表达了极端修正主义/新纳粹观点：希特勒的种族灭绝政策不是错，错的是军事失败。",
                "这种表述在中文互联网的极端民族主义/纳粹同情者社区中是一句经典口号。"
            ],
            "encoding_analysis": [
                "'小胡子'使用C4_典故/符号借用编码——用希特勒的物理特征（小胡子）代指希特勒本人。这是中文互联网中用于规避内容过滤的经典编码。",
                "'错就错在输了战争'使用D1_反讽编码——表面宣称'辩证地看'，实际用简化归因（仅输战争）来合理化/轻描淡写纳粹罪行。反讽在于假装学术客观实则表达极端观点。"
            ],
            "context_analysis": [
                "出现在race_discussion话题下，在种族讨论语境中提及希特勒并为其辩护，是很明确的种族主义/极端主义信号。",
                "虽然单句表达可能被误读为网上玩梗，但在种族话题上下文中，表达纳粹同情/希特勒辩护具有明确的风险指向。"
            ],
            "supporting_evidence": [
                "'小胡子'是已知的希特勒编码代称，用于规避内容审查",
                "'错就错在输了战争'——暗示除战败外没有其他错误，这是纳粹修正主义的核心表述",
                "'辩证的来看'——使用学术包装掩盖极端立场",
                "出现在race_discussion话题中——意味着在种族相关讨论中表达对希特勒的支持"
            ],
            "counter_evidence": [
                "该表述也可能仅仅是网上黑暗幽默/政治不正确玩笑，不是真实的新纳粹立场。但即使在网络梗的语境中，内容本身仍然具有高风险。"
            ],
            "final_rationale": "Risk: high。使用C4编码'小胡子'+D1反讽'错就错在输了战争'表达纳粹修正主义观点，在种族语境中为希特勒辩护，即使作为网络梗也具有高度风险。"
        }
    })
    yield s37

    # ── Sample 38 (003900) ──────────────────────────
    s38 = overwrite(samples[37], {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本讨论江西彩礼问题：'江西本地女的几年不结婚马上问题解决'（如果江西女性几年不结婚，问题自然解决？）。'彩礼贵不贵不都是人炒的？一边给一边骂之会越来越高'（彩礼是炒出来的，一边给钱一边骂只会越来越贵）。",
                "叙述者认为解决方法掌握在本地女性手中（不结婚），认为彩礼价格是市场炒作的结果，批评'边给边骂'的矛盾行为。",
                "话题涉及地域（江西）和性别（彩礼）的交叉。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是对社会现象的评论，使用直接的语言表达观点。",
                "'求婚本地女的'是地域指向，但不是编码。"
            ],
            "context_analysis": [
                "标注为gender_reporting——符合文本评论彩礼这一性别相关社会议题的性质。",
                "需要原帖上下文了解讨论的起点和对方观点。文本本身的立场是评论性而非攻击性。"
            ],
            "supporting_evidence": [
                "'不都是人炒的'——质疑高彩礼的真实性，认为是人为炒作",
                "'一边给一边骂之会越来越高'——批评买家和卖家的矛盾行为",
                "无攻击性语言"
            ],
            "counter_evidence": [
                "'江西本地女的几年不结婚马上问题解决'可被解读为将彩礼问题的责任归咎于江西女性——'只要你们不结婚就解决了'。可能隐含对女性在彩礼问题中的作用的责备。"
            ],
            "final_rationale": "Risk: low。文本评论江西彩礼问题的社会机制，虽有将责任归咎于本地女性的倾向，但整体是观点表达而非攻击。"
        }
    })
    yield s38

    # ── Sample 39 (003901) ──────────────────────────
    s39 = overwrite(samples[38], {
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
                "'这个基佬人面兽心还叫帅天理何在！'——'基佬'（gay man贬称）、'人面兽心'（human face beast heart=衣冠禽兽）、'还叫帅'（还被叫作帅）、'天理何在'（where is justice）。",
                "文本攻击一个特定的同性恋男性（'这个基佬'），称其表里不一、内在外在反差大，并质疑为什么这样'坏'的人还能被认可为'帅'。",
                "这是对特定个体的攻击，但'基佬'作为贬称具有群体攻击性——将个体的负面特征与性取向身份绑定。"
            ],
            "encoding_analysis": [
                "不存在编码机制。'基佬'是直接的对同性恋男性的贬称（literal_keyword），'人面兽心'是直接的负面评价词语，两者都没有经过编码包装。",
                "没有使用平台黑话或任何编码手段。"
            ],
            "context_analysis": [
                "在lgbt_discussion话题下，文本明确攻击同性恋个体。'这个基佬'的'这个'表明文本是针对特定人物/角色。",
                "不需要额外上下文——攻击意图和对象明确。"
            ],
            "supporting_evidence": [
                "'基佬'——使用明确的贬称指代同性恋男性",
                "'人面兽心'——强烈的负面道德评价",
                "'天理何在'——对承认该人物'帅'的社会现象表达强烈不满",
                "将个体负面特征与性取向身份绑定"
            ],
            "counter_evidence": [
                "文本可能是在针对特定公众人物（如影视角色里的'人面兽心'角色），而非一般性地攻击同性恋群体。但'基佬'的使用本身就是群体标签。"
            ],
            "final_rationale": "Risk: high。文本使用'基佬'贬称+强烈负面评价（人面兽心/天理何在）攻击同性恋个体，将负面特征与性取向身份绑定。"
        }
    })
    yield s39

    # ── Sample 40 (003902) ──────────────────────────
    s40 = overwrite(samples[39], {
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
                "文本讨论一名患艾滋病女性的婚姻选择——'得个艾滋而已总好过去非洲送死吧'（得艾滋总比去非洲送死好，暗示去非洲=死亡），'她可以嫁给男艾滋病人嘛……中国同胞干嘛便宜非洲佬'（建议她嫁给中国男艾滋病患者而不是外国人，避免'便宜'非洲人）。",
                "文本有多个种族歧视/排外表达点：①'去非洲送死'——将非洲与死亡等同；②'便宜非洲佬'——'佬'是粤语/南方方言中对特定人群的贬义后缀；③'中国同胞干嘛便宜非洲佬'——表达不能让外国人/非洲人'得利'的强烈排外立场。",
                "叙述者在女性健康问题中嵌入了种族优劣论：中国男性>非洲男性。"
            ],
            "encoding_analysis": [
                "没有使用复杂的编码手段——文本直接表达了种族歧视观点。'非洲佬'中的'佬'是直接的地域贬称后缀（literal_keyword），'去非洲送死'是直接的种族刻板印象表述。",
                "'干嘛便宜非洲佬'使用D1_反讽——以反问形式表达'完全不应该让非洲人获益'的态度。"
            ],
            "context_analysis": [
                "在race_discussion话题下，文本在讨论涉外婚姻/关系时表达了清晰的种族等级观和排外立场。",
                "攻击意图明确——认为中国女性嫁给非洲男性是'便宜'了非洲人。"
            ],
            "supporting_evidence": [
                "'去非洲送死'——将非洲与死亡等同，强化'非洲=危险'的负面刻板印象",
                "'便宜非洲佬'——使用贬损后缀'佬'，'便宜'暗示非洲人不配获得中国女性的婚配",
                "'中国同胞干嘛便宜非洲佬'——构建中国/非洲的二元对立，维护种族隔离式的婚恋观",
                "'解决中国男艾滋病人的结婚需求'——将女性物化为解决男性需求的资源"
            ],
            "counter_evidence": [
                "文本的讽刺语气（D1反讽）可能部分削弱极端主张的严重性——叙述者可能在使用极端假设来讽刺某种观点。但总体上文本表达了种族优劣和排外立场。"
            ],
            "final_rationale": "Risk: high。文本在讨论女性婚配选择时明确表达种族歧视观点（非洲=死亡、非洲佬=不应'便宜'的对象），使用直接贬称和种族等级话语。"
        }
    })
    yield s40

    # ── Sample 41 (003903) ──────────────────────────
    s41 = overwrite(samples[40], {
        "risk_level": "high",
        "encoding_primary": "A2_拼音缩写",
        "encoding_secondary": ["literal_keyword"],
        "ambiguity": "medium",
        "evidence_strength": "strong",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本质疑某人：表面宣扬'正确婚恋价值观'但背地里'天天xingqin女儿'——'xingqin'是拼音缩写替代'性侵'（sexual assault/insex of daughter）。",
                "这是一个严重的指控——称某人猥亵/性侵自己的女儿。'xingqin'是为了规避内容过滤而使用的拼音缩写编码。",
                "在lgbt_discussion话题下，被质疑的人可能是反同婚姻倡导者（'说正确婚恋价值观'），叙述者指责他的实际行为与公开言论相反。"
            ],
            "encoding_analysis": [
                "'xingqin'使用A2_拼音缩写编码——将'性侵'（两字的首字母或全拼音）改写为拼音形式，绕过平台对'性侵'等敏感词的内容过滤。",
                "'他也补累的谁知道'和'是不是就是他'是直接的语言表达（literal_keyword），没有编码。"
            ],
            "context_analysis": [
                "在lgbt_discussion话题下，文本可能是在讨论一个公开宣扬反同立场的人被指控有性侵行为——'说正确婚恋价值观'可能指反同婚姻倡导者。",
                "需要上下文验证：①被指控的人是谁；②指控是否有依据。但文本本身涉及严重的未经证实的性侵指控。"
            ],
            "supporting_evidence": [
                "'xingqin'明确指向性侵（拼音编码），是最严重的犯罪指控之一",
                "'天天'暗示是持续性行为而非单一事件",
                "'表面上……背地里……'构建了contrast：公开形象与实际行为的反差"
            ],
            "counter_evidence": [
                "文本是未经证实的指控——没有提供任何证据",
                "'谁知道'表明叙述者自己也不确定（是猜测）",
                "在lgbt话题中，这种'反同者自己就是性侵者'的指控是一种常见的话语策略，可能是基于推理而非事实"
            ],
            "final_rationale": "Risk: high。使用A2拼音缩写编码（'xingqin'=性侵）对他人物化严重犯罪指控（猥亵女儿），涉及儿童性安全和他人名誉的重大风险。"
        }
    })
    yield s41

    # ── Sample 42 (003904) ──────────────────────────
    s42 = overwrite(samples[41], {
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
                "'我中国人，你喜欢黑人麻烦你走😠😠😠'——明确的身份声明（我是中国人）+指向性要求（喜欢黑人的请你离开中国/离开对话）+愤怒表情。",
                "文本表达了清晰的排外/种族歧视立场：如果在中国境内喜欢黑人，就应该离开。这是典型的'排他性民族主义'表述——将种族偏好作为划定'谁有资格留在中国'的标准。",
                "表情😠😠😠强化了愤怒情绪。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本直接表达了种族排斥观点，没有任何编码包装。",
                "'麻烦你走'是直接的驱赶性语言，'我中国人'是排他性的身份主张。"
            ],
            "context_analysis": [
                "在race_discussion话题下，该文本明确表达了基于种族偏好排斥他人（中国人不能喜欢黑人）的立场。",
                "不需要额外上下文——文本的歧视立场非常明确。"
            ],
            "supporting_evidence": [
                "'我中国人'——建立排他性的民族身份立场",
                "'你喜欢黑人麻烦你走'——直接基于种族偏好的排斥性要求",
                "'😠😠😠'——愤怒情绪强化",
                "没有提供任何论据，纯情绪性排他表达"
            ],
            "counter_evidence": [
                "该文本可能是对特定语境（如'国人应该以什么标准交友'）的回应，但直接要求喜欢黑人的人离开是明确的种族排斥。",
                "文本过于简短，缺乏论证逻辑——这使得它更像情绪发泄而非理性论辩。"
            ],
            "final_rationale": "Risk: high。文本直接要求喜欢黑人的人'离开'，表达基于种族偏好的排他性立场，是明确的种族歧视/排外言论。"
        }
    })
    yield s42

    # ── Sample 43 (003905) ──────────────────────────
    s43 = overwrite(samples[42], {
        "risk_level": "low",
        "encoding_primary": "D2_隐喻",
        "encoding_secondary": [],
        "ambiguity": "medium",
        "evidence_strength": "weak",
        "needs_context": True,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本发出对出国的警告：'别轻易出国'、'到了国外了，太难了'、'真的就是人家板上的肉，让你生就生，让你死就死'。",
                "'板上的肉'（meat on the chopping block）是一个D2隐喻，表示任人宰割的无力状态。文本整体表达了对海外生活的恐惧和无力感。",
                "文本没有针对任何特定种族或国家（除了泛指'国外'），而是一种普遍性的对异国生存的焦虑表达。"
            ],
            "encoding_analysis": [
                "'板上的肉'使用了D2_隐喻编码——通过'砧板上任由宰割的肉'这一具体意象比喻在国外环境中无力反抗的状态。",
                "这是常用的比喻，不是高度编码化的社区黑话。其余'太难了'、'别轻易出国'都是直接表达。"
            ],
            "context_analysis": [
                "在race_discussion话题下，该文本可能是在回应关于'在外国经历种族歧视'的讨论。'板上的肉'的恐惧源于作为弱势群体（如少数族裔）在国外缺乏保护的状态。",
                "需要上下文来确定'国外'的具体指向和讨论背景。"
            ],
            "supporting_evidence": [
                "'板上的肉'是具体的隐喻意象——表达严重的无力感",
                "'让你生就生，让你死就死'——极端化的表述表达信念",
                "'唉，是的呀'——附和语气，表明是对他人言论的赞同"
            ],
            "counter_evidence": [
                "文本没有攻击任何群体或个人，只是表达对出国境遇的恐惧",
                "'国外'是极宽泛的概念，没有针对特定国家或种族",
                "恐惧表达可能源自真实的歧视经历而非偏见"
            ],
            "final_rationale": "Risk: low。文本使用D2隐喻（'板上的肉'）表达对出国境遇的恐惧，无群体攻击性，是基于焦虑的个人感受表达。"
        }
    })
    yield s43

    # ── Sample 44 (003906) ──────────────────────────
    s44 = overwrite(samples[43], {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "'游戏账号就和自己的孩子一样，你把人家孩子扔了人家不和他拼命？'——将游戏账号类比为孩子，认为删除/丢弃人家的账号会引发激烈的反抗。",
                "这完全是游戏社区的讨论内容。与性别话题无关——话题标签gender_discussion似乎有误。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是游戏社区中的常见表达方式，'账号=孩子'是一种通俗比喻而非编码攻击。"
            ],
            "context_analysis": [
                "标注为gender_discussion但内容完全是游戏话题。可能是数据集标注错误。",
                "需要上下文来理解该文本在性别讨论中的位置（如果有的话）。"
            ],
            "supporting_evidence": [
                "只有游戏相关的内容（'游戏账号'），无攻击性",
                "温和的语气表达对他人财物的尊重",
                "ToxiCN标注为toxic=0"
            ],
            "counter_evidence": [
                "无。完全无害的游戏社区表达。"
            ],
            "final_rationale": "Risk: none (hard_negative)。游戏社区中对账号价值的常见类比表达，无任何攻击性或偏见内容。"
        }
    })
    yield s44

    # ── Sample 45 (003907) ──────────────────────────
    s45 = overwrite(samples[44], {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "high",
        "evidence_strength": "weak",
        "needs_context": True,
        "hard_negative": False,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "'你以为国女她们不知道这些吗？'——一个简短的反问句：'你以为中国女人们不知道这些吗？'",
                "'国女'（中国女性）+ '不知道这些吗'（反问，暗示'她们其实知道'）。文本在暗示中国女性对某些事实/真相是知情的。",
                "没有上下文无法知道'这些'指的是什么——可能涉及涉外婚姻、择偶偏好等话题。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是反问句，没有使用任何编码手段。",
                "'国女'是中文网络中的常见简称（国+女=中国女性），不是编码。"
            ],
            "context_analysis": [
                "在race_discussion话题下，'这些'可能指代与种族相关的某些事实（如外国人的负面信息、文化差异等）。",
                "高度歧义——不知道'这些'指什么，也不知道'国女'在此语境中是被什么框架judged的。",
                "需要上下文才能评估。"
            ],
            "supporting_evidence": [
                "缺乏足够上下文，难以判断文本的风险等级",
                "无攻击性词汇或编码",
                "反问句本身不构成攻击"
            ],
            "counter_evidence": [
                "在race_discussion语境中，反问'你以为国女不知道这些'可能暗示中国女性'明知故犯'（如明知外国人不可靠却仍选择），这可能隐含对中国女性的负面判断",
                "'这些'的具体所指决定文本的风险程度"
            ],
            "final_rationale": "Risk: low。简短反问句缺乏足够上下文评估风险，无攻击性词汇或编码，标为低风险并标注需要上下文。"
        }
    })
    yield s45

    # ── Sample 46 (003908) ──────────────────────────
    s46 = overwrite(samples[45], {
        "risk_level": "high",
        "encoding_primary": "A1_谐音",
        "encoding_secondary": ["D1_反讽"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "'写得好，爱紫病爱你😅😅'——表面是赞扬（'写得好'），但结合'爱紫病'和😅表情，是反讽性的攻击。",
                "'爱紫病'是'艾滋病'（AIDS）的谐音变体——'紫'（zǐ）替换'滋'（zī/滋），形成了'爱紫病'这个有颜色的变体写法，在种族语境中，这是对AIDS话题的编码性提及。",
                "在race_discussion语境中，将'写得好'与AIDS编码性提及结合，大概率是种族歧视性攻击——将原帖内容与AIDS联系（常见的种族刻板印象，将黑人/AIDS关联）。"
            ],
            "encoding_analysis": [
                "'爱紫病'使用A1_谐音编码——将'艾滋病'中的'滋'替换为同音字'紫'，形成'爱紫病'这一变体。这种谐音替换常用于规避内容过滤。",
                "'写得好'使用D1_反讽编码——在攻击性的上下文中，表面的赞扬是讽刺性的。😅😅表情进一步强调了讽刺/嘲笑语气。"
            ],
            "context_analysis": [
                "在race_discussion话题下，提及AIDS（即使是编码形式）通常是在种族歧视框架中关联黑人与AIDS。",
                "不需要额外的上下文——编码手段和攻击意图可识别。"
            ],
            "supporting_evidence": [
                "'爱紫病'是已知的艾滋病的谐音编码写法",
                "'写得好'+😅😅构成反讽——实际是在嘲笑/攻击",
                "race_discussion话题下，AIDS的提及与黑人/AIDS的种族刻板印象直接相关",
                "简短但有明确的编码结构：反讽框架+谐音编码"
            ],
            "counter_evidence": [
                "如果原帖内容真的涉及AIDS话题讨论（而非种族话题），该回应可能只是AIDS话题内部的语言使用。但'爱紫病'的编码形式和race话题标签指向种族攻击。"
            ],
            "final_rationale": "Risk: high。文本使用A1谐音编码（'爱紫病'=艾滋病）和D1反讽（'写得好'），在种族语境中通过AIDS关联进行种族攻击。"
        }
    })
    yield s46

    # ── Sample 47 (003909) ──────────────────────────
    s47 = overwrite(samples[46], {
        "risk_level": "high",
        "encoding_primary": "B4_符号干扰",
        "encoding_secondary": ["literal_keyword"],
        "ambiguity": "low",
        "evidence_strength": "strong",
        "needs_context": False,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "'慕✓口嗨一贯可以的，毕竟不用为自己的言行负责，果然是劣等生物啊。'——'慕✓'是'慕洋犬'（崇拜外国人的/extreme nationalist骂人的话）的符号过滤版，'口嗨'=嘴上爽/光说不练，'劣等生物'=inferior creatures。",
                "文本攻击慕洋犬（崇拜外国人的人）'光说不练'并且不用负责，最终定性为'劣等生物'——这是极端的侮辱性总结。",
                "在gender_discussion语境中，攻击对象可能是崇拜外国男性的中国女性（'慕洋犬'在性别讨论中常指称偏好外国男性的中国女性）。"
            ],
            "encoding_analysis": [
                "'慕✓'使用B4_符号干扰编码——用✓符号替代'洋犬'部分，既规避了对'洋犬'的内容过滤，又通过符号保留了原词的识别度。这在中文社区的骂人话语中是常见的规避手段。",
                "'口嗨'是E1_平台黑话——'口嗨'是弹幕/论坛中的黑话，意为口头吹牛/光说不做。",
                "'劣等生物'是直接的攻击性语言（literal_keyword）——极端侮辱性的总结。"
            ],
            "context_analysis": [
                "在gender_discussion语境中，攻击对象可能是在性别讨论中被贬低为'慕洋犬'的女性群体。",
                "虽然使用了符号编码，但'劣等生物'的总结使攻击意图非常明确。"
            ],
            "supporting_evidence": [
                "'慕✓'使用✓符号替代'洋犬'，是已知的B4编码手段",
                "'口嗨'是贴吧/论坛平台黑话，意为光说不做",
                "'劣等生物'——极端的群体侮辱总结",
                "'不用为自己的言行负责'——指责对方"
            ],
            "counter_evidence": [
                "'慕✓'的具体解码需要社区知识（'慕洋犬'的识别），但在gender_discussion语境下，解码路径较为明确。"
            ],
            "final_rationale": "Risk: high。文本使用B4符号编码（'慕✓'=慕洋犬）+E1黑话（'口嗨'）+极端侮辱（'劣等生物'），对特定群体进行复合型编码攻击。"
        }
    })
    yield s47

    # ── Sample 48 (003910) ──────────────────────────
    s48 = overwrite(samples[47], {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "'广西的默默刷评论默默走开'——广西人（我）默默浏览评论后悄然离开。这是网络社区中常见的自嘲表述，来自某个地域的用户在相关讨论中不作评论、悄悄退出。",
                "没有任何攻击性——这句只是在描述一个人。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是简单的自述语句，没有使用编码手段。"
            ],
            "context_analysis": [
                "在region_discussion语境中，该回应可能出现在关于各个地区的讨论中——广西人表示自己没什么好说的。",
                "需要上下文了解讨论的主题。"
            ],
            "supporting_evidence": [
                "无任何攻击性词汇",
                "典型的网络潜水留言",
                "ToxiCN标注为toxic=0"
            ],
            "counter_evidence": [
                "无。完全无害。"
            ],
            "final_rationale": "Risk: none (hard_negative)。网络潜水留言，自嘲式地域身份表达，无任何攻击性或偏见内容。"
        }
    })
    yield s48

    # ── Sample 49 (003911) ──────────────────────────
    s49 = overwrite(samples[48], {
        "risk_level": "medium",
        "encoding_primary": "D2_隐喻",
        "encoding_secondary": ["literal_keyword"],
        "ambiguity": "medium",
        "evidence_strength": "moderate",
        "needs_context": True,
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本从自然法则角度反对同性恋：'地球上的任何以族群生活的生物哪个不是雌雄搭配的'（所有群居生物都是雌雄配对），声称同性恋违背'自然规律'，并警告'有你这样想法的族群在历史的长河中不知道消失了多少年了'。",
                "核心论点：同性恋违反自然规律，自然（通过历史）会淘汰那些认同同性恋的族群。",
                "文本还批评了原帖回答者：'把各种异性的不好说成是同性的优点，然后再找各种冠冕堂皇的理由和数据来替自己证明'——指控原帖选择性论证。"
            ],
            "encoding_analysis": [
                "文本使用D2_隐喻编码——通过'自然规律'、'自然的选择'、'族群消失'这一自然/生物隐喻框架来论证反对同性恋的立场。同性恋被比喻为违背生物规律的异常行为。",
                "'雌雄搭配'、'雌雄同体'是生物学词汇的移用（隐喻性使用）。其余'冠冕堂皇'、'历史长河'是常规修辞。"
            ],
            "context_analysis": [
                "在lgbt_discussion话题下，该文本表达了对同性恋的反对立场，但框架是'自然法则'而非直接辱骂——是经过包装的反同论证。",
                "需要原帖上下文来验证叙述者对原文论证方法的批评是否合理。"
            ],
            "supporting_evidence": [
                "使用'自然规律/自然选择'论证否定同性恋的合法性",
                "'雌雄搭配的'——将生物界的异配生殖作为唯一可接受的模式",
                "'会告诉你，有你这样想法的族群在历史的长河中不知道消失了多少年了'——警告/威胁暗示同性恋族群会被'自然淘汰'",
                "批评原帖'找各种冠冕堂皇的理由和数据'——使用揭露策略包装自己的论证"
            ],
            "counter_evidence": [
                "文本的论证框架（自然规律）在表面上是生物学/进化论讨论，可以解读为学术性讨论而非攻击",
                "文本没有使用直接辱骂词（'基佬'、'变态'等），较为克制",
                "批评原帖论证方法的部分是理性的方法论批评"
            ],
            "final_rationale": "Risk: medium。文本使用D2隐喻（自然规律框架）包装反对同性恋的立场，没有直接辱骂但隐含'同性恋违反自然'和'会被自然淘汰'的修辞，有中度风险。"
        }
    })
    yield s49

    # ── Sample 50 (003912) ──────────────────────────
    s50 = overwrite(samples[49], {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "ambiguity": "high",
        "evidence_strength": "weak",
        "needs_context": True,
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "'你看看，何必发言来佐证我的话🤔'——'你看看'（你看吧）、'何必发言来佐证我的话'（何必发言来证明我说的没错）。叙述者说对方的发言恰好证明了自己的观点。",
                "这是对他人评论的回应——说我之前说的没错，你的评论就是证据。🤔表情表示思考/得意。",
                "文本没有任何攻击性——它是meta层次的评论（关于之前言论的评论）。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是直接的对他人评论的元评论，没有编码手段。"
            ],
            "context_analysis": [
                "在race_discussion话题下，叙述者可能之前发表了某种关于种族的观点，现在引用对方的发言作为自己观点的佐证。",
                "高度歧义——文本本身的立场完全取决于之前叙述者说的'我的话'是什么。"
            ],
            "supporting_evidence": [
                "无攻击性词汇或编码",
                "ToxiCN标注为toxic=0",
                "只是元评论"
            ],
            "counter_evidence": [
                "'我的话'的内容未知，可能本身具有攻击性（但该文本不是攻击，而是对攻击的引用确认）",
                "高度依赖上下文"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本是对他人评论的元回应，无攻击性词汇或编码，风险完全取决于不可知的上下文。"
        }
    })
    yield s50


def main():
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.readlines()

    samples = [json.loads(line) for line in lines if line.strip()]
    if len(samples) != 50:
        print(f"WARNING: expected 50 samples, got {len(samples)}", file=sys.stderr)

    reviewed = list(review_all(samples))
    if len(reviewed) != 50:
        print(f"ERROR: generated {len(reviewed)} reviewed samples, expected 50", file=sys.stderr)
        sys.exit(1)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        for s in reviewed:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")

    print(f"Written {len(reviewed)} reviewed samples to {OUTPUT}")


if __name__ == "__main__":
    main()
