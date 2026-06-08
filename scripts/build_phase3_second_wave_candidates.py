#!/usr/bin/env python3
"""Build the second phase-3 targeted expansion batch.

This batch follows the refreshed 675-candidate coverage plan. It writes raw
needs_revision candidates only and never merges into processed data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from build_phase3_first_wave_candidates import MODE_META


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "data/raw/phase3_second_wave_candidates.jsonl"
BATCH = "phase3_v2_long_tail_boundaries"
MODES = ("direct", "obfuscated", "contextual", "weak_signal", "safe_context")


PROFILES: list[dict[str, Any]] = [
    {
        "category": "sexual_content",
        "name": "色情低俗",
        "quota": 25,
        "primary": "E1_平台黑话",
        "secondary": ["D3_借代", "B4_符号/空格/Unicode 干扰"],
        "platforms": ["小红书", "抖音", "微博", "贴吧", "微信群"],
        "texts": {
            "direct": [
                "只聊成年人项目，能接受价目表的再加",
                "今晚酒店附近可约，先说时长和预算",
                "陪酒之后还能安排别的，费用另算",
                "同城上门服务，照片和价格私下发",
                "要特殊陪玩的直接报需求，别只问在不在",
            ],
            "obfuscated": [
                "夜里那种活用月亮代，数字就是价位",
                "把约字拆开说，平台最近查得紧",
                "不方便写项目，菜单末尾带星号的就是",
                "联系方式藏在尺码表里，按最大码找",
                "成年人看的那页换了字母，老客知道入口",
            ],
            "contextual": [
                "今晚临时空出来，附近有人想见面吗",
                "只接待懂规矩的，普通聊天不用问",
                "主页最后一张有今晚安排，自己看条件",
                "深夜档还差一位，能来的先发位置",
                "有些服务不能在公开区细说，合适再聊",
            ],
            "weak_signal": [
                "深夜档是直播排班吧，这个标题别想太多",
                "成年人限定可能只是电影分级，不一定擦边",
                "同城见面正常，但他老提预算我有点膈应",
                "菜单末尾那个星号，像店里普通促销标记",
                "陪玩不就是游戏上分吗，别一看到陪就歪",
            ],
            "safe_context": [
                "酒店群里有人提醒别信陌生招揽，直接举报就行",
                "性健康门诊面向成年人提供正规咨询和检测",
                "这纪录片是在讲治理问题，不是在帮谁打广告",
                "家长群转这个课，是教孩子识别擦边诱导的",
                "平台那条公告是在说处罚规则，不是擦边内容",
            ],
        },
    },
    {
        "category": "spam_ads_fraud",
        "name": "广告诈骗导流",
        "quota": 25,
        "primary": "E1_平台黑话",
        "secondary": ["A2_拼音/首字母缩写", "C4_典故/物品/符号借用"],
        "platforms": ["小红书", "微信群", "抖音", "微博", "QQ群"],
        "texts": {
            "direct": [
                "先付认证金就能领高额退款，十分钟到账",
                "内部渠道代抢名额，交定金后保证成功",
                "兼职只要代收一笔款，当天结算三百",
                "征信不好也能下款，包装费先转过来",
                "跟单群今晚开新仓，入群费交完发代码",
            ],
            "obfuscated": [
                "退款两个字别写，发一个退字加箭头就行",
                "联细方式在九宫格里，按数字顺序拼",
                "想做任务的搜昵称少最后一个字，防限流",
                "想进果汁群的别问钱，几杯自己报",
                "那个币用水果名代，群里不要出现原名",
            ],
            "contextual": [
                "名额锁定前要做一次身份认证，费用之后退",
                "先帮平台走个流水，完成后工资一起结",
                "这个客服说只能通过私人会议处理退款",
                "群里老师让大家今晚统一换到另一个软件",
                "他一直催我先垫钱，说错过就不能恢复",
            ],
            "weak_signal": [
                "怎么又让我换软件开会，正常面试也这样吗",
                "内部名额听着像卖课话术，但还没让交钱",
                "这个私人客服怪怪的，我先不点他发的链接",
                "兼职一上来就要实名，我得先查下公司名",
                "他说退款今晚截止，我越听越像催人转账",
            ],
            "safe_context": [
                "派出所刚发提醒了，先交认证金的退款别信",
                "正规兼职结算不会要求员工代收陌生资金",
                "我妈差点把验证码报出去，还好银行客服拦住了",
                "学校今天讲的虚假兼职，和这个话术一模一样",
                "退款还是从订单页走吧，私人链接我是不敢点",
            ],
        },
    },
    {
        "category": "insulting_abuse",
        "name": "辱骂群体攻击",
        "quota": 15,
        "primary": "D3_借代",
        "secondary": ["D1_反讽", "A2_拼音/首字母缩写"],
        "platforms": ["微博", "贴吧", "B站"],
        "texts": {
            "direct": [
                "这种口音的人都别来，来了只会坏事",
                "他们那个职业没一个好东西，见到就绕开",
                "这类病人活该被排斥，别让他们进社区",
            ],
            "obfuscated": [
                "地域名换成车牌首字母，骂起来不容易删",
                "那类人统一叫灰头像，别打真实群体名",
                "职业后两个字用表情替掉，大家照样懂",
            ],
            "contextual": [
                "果然又是那个地方的，难怪会这样",
                "一听他说做什么工作的，我就知道评论没法看",
                "这种头像每次出现都带来一样的问题",
            ],
            "weak_signal": [
                "他说那个地方来的，也可能只是说快递发货地",
                "他骂的是这一个司机吧，别扩大到整个职业",
                "灰头像不就是默认头像吗，别见一个就扣帽子",
            ],
            "safe_context": [
                "这个公益片明明是在反歧视，别只截那句脏话",
                "方言课比较口音差异，不是在嘲笑哪个地方",
                "社区群刚说了，别因为病名就排斥邻居",
            ],
        },
    },
    {
        "category": "weapons_explosives",
        "name": "枪爆武器",
        "quota": 15,
        "primary": "C4_典故/物品/符号借用",
        "secondary": ["B3_形近字替换", "E1_平台黑话"],
        "platforms": ["论坛", "贴吧", "微信群"],
        "texts": {
            "direct": [
                "能击发的整套还有两件，想要的报城市",
                "需要起爆部件的说规格，我这边能配齐",
                "这批管制刀具不开票，同城可以当面拿",
            ],
            "obfuscated": [
                "老钟表还有吗，走得响不响你应该懂",
                "起爆器别写，用遥控门铃的简称问",
                "刀具型号拆成三个车牌号，按顺序发",
            ],
            "contextual": [
                "这根管子和弹簧尺寸能对上吗，想拼完整",
                "远程按一下能不能稳定触发，最好别有延迟",
                "这把收藏品开刃了吗，带出去方便不方便",
            ],
            "weak_signal": [
                "这不就是修车用的管子和弹簧吗，别吓人",
                "远程触发也可能是智能门铃，先看他接哪儿",
                "收藏刀具有人只摆柜子里，带出去才不对劲",
            ],
            "safe_context": [
                "机械课展示弹簧结构，不涉及武器组装",
                "消防课讲这个，是提醒别乱碰危险品",
                "博物馆那把刀具只让看，谁也不能带走",
            ],
        },
    },
    {
        "category": "public_affairs",
        "name": "公共事务",
        "quota": 15,
        "primary": "E3_话题/热点触发",
        "secondary": ["D1_反讽", "E2_时间节点触发"],
        "platforms": ["微博", "知乎", "微信群"],
        "texts": {
            "direct": [
                "今晚统一去门口堵着，谁都别提前走",
                "名单已经整理好，明天按表逐个施压",
                "别走正常渠道了，直接把现场围起来",
            ],
            "obfuscated": [
                "今晚看房的还是老地方，别在群名里写集合",
                "名单只发编号，行动内容用天气符号表示",
                "围门口别直说，群里统一叫排队领票",
            ],
            "contextual": [
                "正常流程没用，明天大家都到门口再谈",
                "这次别只转发，得让他们真正看到人数",
                "时间定了以后统一回复收到，别外传安排",
            ],
            "weak_signal": [
                "到门口可能是正常办事，也可能带有聚集动员",
                "他说多叫几个人去门口，也可能只是想有人作证",
                "不外传安排值得关注，也可能只是内部会议",
            ],
            "safe_context": [
                "小区群说去公开听证会提意见，流程挺正常",
                "办事大厅让大家按预约排队，别现场挤成一团",
                "新闻把当事人电话打码了，这点还挺必要",
            ],
        },
    },
    {
        "category": "political_history",
        "name": "政治历史鉴证梗",
        "quota": 15,
        "primary": "C2_历史事件影射",
        "secondary": ["C1_历史人物类比", "C3_数字代指"],
        "platforms": ["B站", "微博", "知乎"],
        "texts": {
            "direct": [
                "今天这场面和书里那次清场几乎一模一样",
                "他又在复刻那位末代掌权者的最后几年",
                "这个日期一到，评论区都知道在纪念什么",
            ],
            "obfuscated": [
                "年份别写全，用前两位加后两位相减",
                "那位名字换成同朝代的年号，懂历史的能对上",
                "事件名用课本页码代，评论只发页数",
            ],
            "contextual": [
                "历史总在押同一个韵，只是角色换了名字",
                "这集人物关系怎么看着像现实里的旧剧本",
                "每年到这个晚上，时间线都会突然安静",
            ],
            "weak_signal": [
                "他说历史又押韵，可能只是吐槽剧情套路吧",
                "同学问课本页码而已，先别往别处联想",
                "我发这个日期是家里纪念日，别往大事上带",
            ],
            "safe_context": [
                "这节课就是讲制度变迁，老师没提现实人物",
                "博物馆只是按年代讲人物生平，别过度解读",
                "读书会在核史料版本，不是看到日期就有暗指",
            ],
        },
    },
    {
        "category": "platform_censorship_evasion",
        "name": "平台规避审查黑话",
        "quota": 15,
        "primary": "B4_符号/空格/Unicode 干扰",
        "secondary": ["A2_拼音/首字母缩写", "E1_平台黑话"],
        "platforms": ["B站", "微博", "贴吧"],
        "texts": {
            "direct": [
                "原词发不出，我中间垫几个看不见的字符试试",
                "那句话文字版又没了，我改成图再发一遍",
                "全称别写了，三个首字母评论区自己懂",
            ],
            "obfuscated": [
                "左右各垫一点空白，看起来还是原来那几个字",
                "我把每个字隔成小图，你们连着看就行",
                "先写同音字，括号里补个偏旁，老用户能懂",
            ],
            "contextual": [
                "文字版一直发不出，换张截图应该就行",
                "名字别完整出现，评论区最近盯得很紧",
                "按旧暗号回复，公开解释容易被处理",
            ],
            "weak_signal": [
                "截图发出来好看一点吧，不一定是怕被删",
                "首字母常用于正常缩写，仍需判断共同指向",
                "说发不出也可能是网络问题，证据暂时有限",
            ],
            "safe_context": [
                "无障碍设计课程讲零宽字符可能影响阅读器",
                "论文使用首字母缩写并在首次出现时给出定义",
                "图片版通知是为了保留格式，不包含规避内容",
            ],
        },
    },
    {
        "category": "cyber_abuse",
        "name": "网络黑产安全风险",
        "quota": 15,
        "primary": "E1_平台黑话",
        "secondary": ["A2_拼音/首字母缩写", "C4_典故/物品/符号借用"],
        "platforms": ["论坛", "微信群", "贴吧"],
        "texts": {
            "direct": [
                "批量过验证码的接口还有，按调用次数收费",
                "能查手机号实名信息，报号码直接出结果",
                "企业后台账号一批，登录正常的单独计价",
            ],
            "obfuscated": [
                "门票几秒能出来？我这边要批量验一波",
                "实名数据用快递单代称，别发字段名称",
                "后台账号只发域名尾字母和库存数字",
            ],
            "contextual": [
                "这个接口不限次数，拿来跑注册应该挺快",
                "只知道号码也能查到住址吗，有现成渠道没",
                "这批账号权限挺高，先测试哪些还能登录",
            ],
            "weak_signal": [
                "批量接口可能用于授权测试，也可能被滥用",
                "查实名是查我自己的账号，别乱开别人信息",
                "账号登录测试若在企业内部授权范围内可以合规",
            ],
            "safe_context": [
                "安全团队在授权环境中测试验证码防护强度",
                "用户查询本人实名信息应通过官方隐私入口",
                "离职同事的账号今天统一下线，权限别留着",
            ],
        },
    },
    {
        "category": "violence_extremism",
        "name": "暴力极端",
        "quota": 15,
        "primary": "E3_话题/热点触发",
        "secondary": ["D2_夸张/反话", "E1_平台黑话"],
        "platforms": ["微信群", "贴吧", "微博"],
        "texts": {
            "direct": [
                "今晚带工具去堵他，必须让他长记性",
                "人够了就一起冲进去，别给对面反应时间",
                "名单上的人一个都别放过，按地址分组找",
            ],
            "obfuscated": [
                "动手改叫敲门，带什么用工具颜色表示",
                "冲进去用进场代替，时间发成球赛比分",
                "名单不写名字，只发头像编号和地图点",
            ],
            "contextual": [
                "今晚见面别空手，事情总得有个结果",
                "大家到了听统一口令，不要自己先行动",
                "地址已经确认，就看谁真的敢过去",
            ],
            "weak_signal": [
                "别空手可能只是提醒带材料，也可能暗示工具",
                "统一口令可能用于演出排练，需结合现场话题",
                "他说敢不敢过去，听着冲，但也可能只是吵架嘴硬",
            ],
            "safe_context": [
                "邻居群都在劝先报警，别再往现场凑了",
                "影视排练中的冲锋口令属于剧本表演",
                "安全课拿这种话术做反面例子，让大家别跟着起哄",
            ],
        },
    },
    {
        "category": "illegal_goods",
        "name": "违禁交易",
        "quota": 15,
        "primary": "C4_典故/物品/符号借用",
        "secondary": ["E1_平台黑话", "B4_符号/空格/Unicode 干扰"],
        "platforms": ["微信群", "贴吧", "小红书"],
        "texts": {
            "direct": [
                "处方管制药可以散出，数量多价格另谈",
                "这批粉纯度高，同城当天可以送到",
                "需要伪造证件的发照片和用途，最快当天出",
            ],
            "obfuscated": [
                "管制药叫蓝糖，问几盒就是问数量",
                "那种粉只发色卡编号，别写名字",
                "证件模板用毕业照代称，群里不要说办理",
            ],
            "contextual": [
                "医院开不到的那种药，有没有别的渠道",
                "这批货成色比上次好，先给老客户留",
                "照片和信息发过去，能不能做得像真的一样",
            ],
            "weak_signal": [
                "医院没号我才问哪里能买药，不是要走歪门路",
                "货和成色含义不明确，需要结合交易对象",
                "做得像真的可能指设计稿，也可能涉及伪造",
            ],
            "safe_context": [
                "这药还是得拿处方去医院开，别找私人卖家",
                "禁毒课放那些伪装图，是提醒大家别上当",
                "证件照最多修下光线，信息不能乱改",
            ],
        },
    },
    {
        "category": "gambling",
        "name": "赌博",
        "quota": 15,
        "primary": "E1_平台黑话",
        "secondary": ["C3_数字代指", "A2_拼音/首字母缩写"],
        "platforms": ["微信群", "QQ群", "贴吧"],
        "texts": {
            "direct": [
                "今晚盘口已经开了，想下注的报金额",
                "牌局还差两位，带现金来直接上桌",
                "彩票内部号今晚发，先交跟单费",
            ],
            "obfuscated": [
                "今晚点菜按老规矩，几盘就是几手",
                "盘口用水深水浅代替，别在群里发赔率",
                "牌局地点写成快递取件码，到附近再问",
            ],
            "contextual": [
                "今晚这场水位变得快，跟哪边比较稳",
                "老地方桌子开了，还是按以前的底",
                "这组号码老师说把握很大，要不要一起跟",
            ],
            "weak_signal": [
                "水位可能是体育数据讨论，也可能指盘口",
                "老地方开桌也可能就是朋友打牌，不一定下钱",
                "号码推荐也可能是普通概率娱乐，需要看收费和投注",
            ],
            "safe_context": [
                "反赌宣传片里那个内部号套路，和骗子说的一样",
                "家庭聚会玩纸牌不涉及金钱输赢",
                "体育节目聊赔率，也一直提醒别拿它下注",
            ],
        },
    },
]


def context_for(profile: dict[str, Any], mode: str, index: int) -> dict[str, Any]:
    contexts = {
        "direct": ("评论区私聊暗示", "有人继续追问具体条件", ["具体怎么走", "公开区别留细节"]),
        "obfuscated": ("群聊暗号接话", "上级评论提醒最近别写太直", ["收到暗号", "换个说法"]),
        "contextual": ("回复链里的追问", "前文正在讨论类似情况", ["这话接着前面看", "感觉不太对劲"]),
        "weak_signal": ("二次回复里的普通解释", "有人把原话往风险方向理解", ["也可能就是普通意思", "先看前后文"]),
        "safe_context": ("普通用户转述正常场景", "前文在分享新闻、课程或正规流程", ["这个是在提醒大家", "别只截半句话"]),
    }
    suffix, parent, replies = contexts[mode]
    return {
        "title": f"{profile['name']}{suffix}",
        "description": "",
        "parent_comment": parent,
        "reply_chain": replies,
        "time": "",
        "topic": profile["name"],
    }


def reasoning(profile: dict[str, Any], mode: str, text: str) -> dict[str, Any]:
    meta = MODE_META[mode]
    risk = meta["risk"]
    encoding = (
        ["上下文明确提供正常用途或反风险目的，未形成稳定风险编码。"]
        if risk == "none"
        else [
            f"主要按 {profile['primary']} 解构，属于{profile['name']}的长尾语境。",
            f"辅助机制包括：{'、'.join(profile['secondary'])}。",
        ]
    )
    if mode in {"obfuscated", "contextual", "weak_signal"}:
        encoding.append("该表达保留普通解释，需要结合互动链和行为意图判断。")
    return {
        "literal_analysis": [f"字面上是在表达：{text}"],
        "encoding_analysis": encoding,
        "context_analysis": [meta["context_note"]],
        "supporting_evidence": meta["support"],
        "counter_evidence": meta["counter"],
        "final_rationale": {
            "high": "文本与互动语境共同呈现较明确风险意图，暂标为 high。",
            "medium": "存在需要召回的编码或行为信号，但具体链路仍不完整，暂标为 medium。",
            "low": "存在弱风险联想，普通解释仍较强，作为困难边界暂标为 low。",
            "none": "正常、教育、新闻或反风险语境提供完整反证，暂标为 none。",
        }[risk],
    }


def build_rows() -> list[dict[str, Any]]:
    rows = []
    serial = 1
    for profile in PROFILES:
        per_mode = profile["quota"] // len(MODES)
        for mode in MODES:
            texts = profile["texts"][mode]
            if len(texts) != per_mode:
                raise ValueError(f"{profile['category']} {mode}: expected {per_mode}, got {len(texts)}")
            for local_index, text in enumerate(texts, start=1):
                meta = MODE_META[mode]
                risk = meta["risk"]
                rows.append(
                    {
                        "id": f"PHASE3_W2_{serial:04d}_{profile['category'].upper()}_{mode.upper()}",
                        "source_type": "synthetic",
                        "platform": profile["platforms"][(local_index - 1) % len(profile["platforms"])],
                        "text": text,
                        "context": context_for(profile, mode, local_index),
                        "risk_level": risk,
                        "encoding_primary": "none" if risk == "none" else profile["primary"],
                        "encoding_secondary": [] if risk == "none" else profile["secondary"],
                        "context_required": True,
                        "ambiguity": meta["ambiguity"],
                        "evidence_strength": meta["evidence"],
                        "hard_negative": meta["hard_negative"],
                        "target_known": False,
                        "target_reference": "匿名化风险语境",
                        "should_explain_target": False,
                        "freshness": "stable",
                        "reasoning": reasoning(profile, mode, text),
                        "quality_status": "needs_revision",
                        "review_notes": (
                            f"source=phase3_second_wave; batch={BATCH}; category={profile['category']}; "
                            f"contrast_mode={mode}; cluster={profile['category']}_{mode}_w2; "
                            "not_merged; needs_human_review"
                        ),
                    }
                )
                serial += 1
    return rows


def main() -> int:
    rows = build_rows()
    if len(rows) != 185:
        raise ValueError(f"Expected 185 rows, got {len(rows)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"Wrote {len(rows)} phase-3 second-wave candidates to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
