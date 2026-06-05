#!/usr/bin/env python3
"""Generate natural review candidates from lexicon seed terms.

This is a candidate generator, not an approval pipeline. It intentionally keeps
all output in data/raw and marks every record as needs_revision.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SEEDS_PATH = ROOT / "data/processed/lexicon_seed_terms.jsonl"
OUTPUT_PATH = ROOT / "data/raw/lexicon_seed_candidates.jsonl"


STRICT_REDLINE = {
    "cyber_abuse",
    "illegal_goods",
    "sexual_content",
    "violence_extremism",
    "weapons_explosives",
}

CONTEXTUAL_RISK = {
    "gambling",
    "insulting_abuse",
    "platform_censorship_evasion",
    "political_history",
    "public_affairs",
}

TRANSACTIONAL_RISK = {
    "spam_ads_fraud",
}

CATEGORY_NAMES = {
    "cyber_abuse": "网络黑产/安全风险",
    "gambling": "赌博相关表达",
    "illegal_goods": "违禁交易",
    "insulting_abuse": "辱骂攻击",
    "platform_censorship_evasion": "平台规避/自我审查",
    "political_history": "政治历史语境",
    "public_affairs": "公共事务语境",
    "sexual_content": "色情低俗",
    "spam_ads_fraud": "广告诈骗导流",
    "violence_extremism": "暴恐极端",
    "weapons_explosives": "枪爆武器",
}

CATEGORY_PRIMARY = {
    "cyber_abuse": "C4_典故/物品/符号借用",
    "gambling": "C4_典故/物品/符号借用",
    "illegal_goods": "C4_典故/物品/符号借用",
    "insulting_abuse": "D1_反讽",
    "platform_censorship_evasion": "E1_平台黑话",
    "political_history": "C4_典故/物品/符号借用",
    "public_affairs": "E2_时间节点触发",
    "sexual_content": "C4_典故/物品/符号借用",
    "spam_ads_fraud": "C4_典故/物品/符号借用",
    "violence_extremism": "C4_典故/物品/符号借用",
    "weapons_explosives": "C4_典故/物品/符号借用",
}

PLATFORMS = ["B站", "微博", "抖音", "贴吧", "知乎", "微信群", "小红书"]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {exc.msg}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_number}: expected object")
            rows.append(value)
    return rows


def risk_family(category: str) -> str:
    if category in STRICT_REDLINE:
        return "strict_redline"
    if category in CONTEXTUAL_RISK:
        return "contextual_risk"
    if category in TRANSACTIONAL_RISK:
        return "transactional_risk"
    return "manual_review"


def evidence_for_risk(risk: str) -> str:
    return {"high": "strong", "medium": "moderate", "low": "weak", "none": "weak"}[risk]


def ambiguity_for_risk(risk: str) -> str:
    return {"high": "medium", "medium": "medium", "low": "high", "none": "low"}[risk]


def secondary_for_seed(seed: dict[str, Any], primary: str) -> list[str]:
    tags = [tag for tag in seed.get("mechanism_tags", []) if isinstance(tag, str)]
    secondary = [tag for tag in tags if tag != "literal_keyword" and tag != primary]
    if seed.get("bucket") == "obfuscated_or_variant" and "F_组合编码" not in secondary:
        secondary.append("F_组合编码")
    return secondary[:3]


def context(topic: str, title: str, parent: str = "", replies: list[str] | None = None) -> dict[str, Any]:
    return {
        "title": title,
        "description": "",
        "parent_comment": parent,
        "reply_chain": replies or [],
        "time": "",
        "topic": topic,
    }


def reasoning(
    *,
    text: str,
    risk: str,
    primary: str,
    family: str,
    category_name: str,
    context_note: str,
) -> dict[str, Any]:
    if risk == "none":
        return {
            "literal_analysis": [f"字面上是在表达：{text}"],
            "encoding_analysis": ["词库命中只作为召回线索，不能单独决定风险。"],
            "context_analysis": [context_note],
            "supporting_evidence": [],
            "counter_evidence": [
                "上下文明确是宣传、科普、新闻、课程、引用或安全教育。",
                "没有招揽、交易、攻击、规避检测或异常互动共识。",
            ],
            "final_rationale": "普通解释和反证更强，暂标为 none；该条用于训练模型避免关键词误杀。",
        }

    if risk == "low":
        return {
            "literal_analysis": [f"字面上是在表达：{text}"],
            "encoding_analysis": [f"候选类别为{category_name}，主编码暂归为 {primary}。"],
            "context_analysis": [context_note],
            "supporting_evidence": ["存在词库命中或弱风险信号。"],
            "counter_evidence": ["缺少明确招揽、交易、攻击、规避或目标映射。", "普通解释仍有较强可能。"],
            "final_rationale": "仅保留低风险复核价值，暂标为 low。",
        }

    support = ["文本和上下文共同提供风险信号。"]
    if family == "strict_redline":
        support.append("该类更接近强规则召回，不宜训练模型寻找放行理由。")
    elif family == "transactional_risk":
        support.append("出现导流、联系方式、交易或引流暗示。")
    else:
        support.append("存在语境依赖的非字面、攻击、规避或敏感讨论信号。")

    return {
        "literal_analysis": [f"字面上是在表达：{text}"],
        "encoding_analysis": [f"候选类别为{category_name}，主编码暂归为 {primary}。"],
        "context_analysis": [context_note],
        "supporting_evidence": support,
        "counter_evidence": ["仍需人工复核，避免只根据词库命中下最终结论。"],
        "final_rationale": f"综合词库召回和上下文，暂标为 {risk}；该条为词库种子候选。",
    }


def strict_templates(category: str) -> list[dict[str, Any]]:
    name = CATEGORY_NAMES[category]
    if category == "cyber_abuse":
        return [
            {
                "variant": "strict_cyber_lead",
                "risk": "high",
                "text": "这库都能拖出来，后台也太纸糊了吧",
                "context": context(name, "安全新闻评论区", "疑似泄露截图被反复转发", ["这不是演示环境吧", "别扩散"]),
                "note": "上下文含疑似数据泄露和异常炫耀信号。",
            },
            {
                "variant": "strict_cyber_evasion",
                "risk": "high",
                "text": "防护文章下面问怎么复现，这味儿就不对了",
                "context": context(name, "技术帖回复区", "这里只能讲防护", ["别发教程", "容易被封"]),
                "note": "上下文区别于防护讨论，出现索要复现方法的风险。",
            },
            {
                "variant": "strict_cyber_report",
                "risk": "medium",
                "text": "刚才那人是不是在卖号库啊，看着有点吓人",
                "context": context(name, "社区管理反馈", "不要复述原文", ["已举报"]),
                "note": "文本是在举报可疑内容，风险低于直接发布但仍需复核。",
            },
        ]

    if category == "illegal_goods":
        return [
            {
                "variant": "strict_goods_lead",
                "risk": "high",
                "text": "这批成色怎么样？别又拿上次那种糊弄人",
                "context": context(name, "二手交易评论区", "评论里多人使用暗号", ["看货再说", "别写全名"]),
                "note": "上下文含暗号、异常交易和疑似违禁物品讨论。",
            },
            {
                "variant": "strict_goods_evasion",
                "risk": "high",
                "text": "老规矩，名字别写全，懂货的自然知道",
                "context": context(name, "同城帖子回复区", "评论区疑似使用暗号", ["老规矩", "别打全名"]),
                "note": "上下文含谐音规避和疑似违禁交易共识。",
            },
            {
                "variant": "strict_goods_report",
                "risk": "medium",
                "text": "这个标题看着正常，评论里那几个暗号有点怪",
                "context": context(name, "用户举报记录", "标题写得很正常", ["评论里有暗号"]),
                "note": "文本是复核提醒，证据不如直接招揽充分。",
            },
        ]

    if category == "sexual_content":
        return [
            {
                "variant": "strict_sexual_lead",
                "risk": "high",
                "text": "同城有人吗，晚上无聊，主页第一条",
                "context": context(name, "同城生活评论区", "刚注册的小号", ["主页有联系方式", "类似评论重复出现"]),
                "note": "上下文含同城、联系方式和疑似低俗导流。",
            },
            {
                "variant": "strict_sexual_evasion",
                "risk": "high",
                "text": "写直了发不出来，那就换个大家都看得懂的说法",
                "context": context(name, "交友帖回复区", "评论被删了几次", ["别写那么直", "看懂就行"]),
                "note": "上下文含符号规避、低俗导流和异常互动。",
            },
            {
                "variant": "strict_sexual_report",
                "risk": "medium",
                "text": "主页第一条自己看，问就是普通交友",
                "context": context(name, "同城生活评论区", "缺少上级评论", ["刚才类似评论被删过"]),
                "note": "文本是审核备注，证据不足以直接判最高风险。",
            },
        ]

    if category == "violence_extremism":
        return [
            {
                "variant": "strict_extremism_lead",
                "risk": "high",
                "text": "别光看了，真有胆子的今晚就出来",
                "context": context(name, "突发新闻评论区", "有人开始带节奏", ["别冲动", "这话过了"]),
                "note": "上下文含煽动和现实动员风险。",
            },
            {
                "variant": "strict_extremism_evasion",
                "risk": "high",
                "text": "前半句我发了，后半句你们接，别连着打",
                "context": context(name, "直播弹幕", "同一个账号连续刷屏", ["分开发就看不出来"]),
                "note": "上下文含拆分规避和连续刷屏。",
            },
            {
                "variant": "strict_extremism_report",
                "risk": "medium",
                "text": "那张图别再转了，真的会出事",
                "context": context(name, "群聊提醒", "不要扩散原图", ["已提醒群主"]),
                "note": "文本是在阻止传播，仍需注意是否复述危险内容。",
            },
        ]

    if category == "weapons_explosives":
        return [
            {
                "variant": "strict_weapon_lead",
                "risk": "high",
                "text": "这个不像摆件啊，真有现货的话报个价",
                "context": context(name, "模型论坛评论区", "前面还在聊收藏", ["别问渠道", "有人提醒越界"]),
                "note": "上下文从爱好讨论转向疑似交易和渠道询问。",
            },
            {
                "variant": "strict_weapon_evasion",
                "risk": "high",
                "text": "这几个字拆开写就行，连起来太扎眼",
                "context": context(name, "短视频评论区", "评论区有人看懂了", ["别写全", "老地方"]),
                "note": "上下文含字形规避、暗号和线下/外部转移信号。",
            },
            {
                "variant": "strict_weapon_report",
                "risk": "medium",
                "text": "电影道具哪有这个质感，真渠道有吗",
                "context": context(name, "影视道具视频", "道具和现实渠道混在一起聊", ["别乱问"]),
                "note": "文本包含反证和疑点，需要人工复核。",
            },
        ]

    return [
        {
            "variant": "strict_alert",
            "risk": "high",
            "text": "这条别留了，明显是在换说法发灰产暗号，还一直让人加私聊",
            "context": context(name, f"{name}相关评论区", "刚才那条又被顶上来了", ["换个字就能发", "懂的去私聊"]),
            "note": "上下文含规避、私聊和灰产暗号信号。",
        },
        {
            "variant": "strict_evasion",
            "risk": "high",
            "text": "他把关键词拆得七零八落，后面还补了联系方式，这种不用犹豫",
            "context": context(name, f"{name}相关短视频评论", "怎么又有人发这种", ["中间加符号就行", "别在评论区说太细"]),
            "note": "上下文含符号规避、联系方式和规避检测意图。",
        },
        {
            "variant": "strict_report",
            "risk": "medium",
            "text": "我只是提醒一下，刚才有人在评论区发了很危险的交易话术，建议管理员看一眼",
            "context": context(name, "社区管理反馈", "不是复述内容，就是提醒处理", ["已举报", "别把原话贴出来"]),
            "note": "文本是在举报或提醒，风险低于直接发布，但仍需要复核。",
        },
    ]


def contextual_templates(category: str) -> list[dict[str, Any]]:
    name = CATEGORY_NAMES[category]
    if category == "gambling":
        return [
            {
                "variant": "contextual_warning",
                "risk": "none",
                "text": "看完后背发凉，真别碰，都是从小钱开始陷进去的",
                "context": context(name, "反赌宣传片评论区", "学校统一组织看的", ["珍爱生活，远离赌博"]),
                "note": "上下文明确是反赌宣传和风险教育。",
                "hard_negative": True,
            },
            {
                "variant": "contextual_suspicious",
                "risk": "medium",
                "text": "这场水太深了，临场那个变化懂球的都懂",
                "context": context(name, "体育比赛直播评论", "有人反复提盘口和赔率", ["这话题别展开", "看比赛就行"]),
                "note": "上下文有盘口、赔率等疑似赌博语境，但缺少完整证据。",
            },
            {
                "variant": "contextual_news",
                "risk": "none",
                "text": "这个案子太典型了，普通人千万别碰，真不是闹着玩的",
                "context": context(name, "法治新闻评论", "警方通报解读", ["这是警示案例"]),
                "note": "上下文明确是新闻和警示，不是招揽。",
                "hard_negative": True,
            },
        ]

    if category == "insulting_abuse":
        return [
            {
                "variant": "contextual_attack",
                "risk": "medium",
                "text": "你别装理中客了，刚才那几句就是冲着人去骂的",
                "context": context(name, "热点争议评论区", "别骂人，讲事情", ["他又开始贴标签了"]),
                "note": "上下文指向人身攻击，但未复述具体攻击词。",
            },
            {
                "variant": "contextual_quote",
                "risk": "none",
                "text": "课堂上放这些是讲网暴案例，不是让大家学着骂人",
                "context": context(name, "媒介素养课程", "课堂案例分析", ["讨论的是网暴后果"]),
                "note": "上下文明确是课程引用和反面教材。",
                "hard_negative": True,
            },
            {
                "variant": "contextual_low",
                "risk": "low",
                "text": "我俩一直这么互怼，别上纲上线啊",
                "context": context(name, "游戏队友聊天", "两个人平时就这么说话", ["后面又一起开黑了"]),
                "note": "上下文存在玩笑或熟人互怼可能。",
                "hard_negative": True,
            },
        ]

    if category == "platform_censorship_evasion":
        return [
            {
                "variant": "contextual_evasion",
                "risk": "medium",
                "text": "首字母都打不出来了，这评论区也太安静了",
                "context": context(name, "时事视频评论区", "刚删了一批评论", ["懂的都懂", "别写全"]),
                "note": "上下文含规避平台检测和群体默契。",
            },
            {
                "variant": "contextual_normal_abbrev",
                "risk": "none",
                "text": "NB 这双偏大半码吗？脚背高能穿不",
                "context": context(name, "运动鞋测评", "求尺码建议", ["偏大半码"]),
                "note": "上下文明确是商品缩写，不是规避表达。",
                "hard_negative": True,
            },
            {
                "variant": "contextual_self_censor",
                "risk": "low",
                "text": "最近少发声吧，吵来吵去也没意思",
                "context": context(name, "小群闲聊", "大家别争了", ["先冷静两天"]),
                "note": "存在自我审查语气，但目标不明确。",
            },
        ]

    if category == "political_history":
        return [
            {
                "variant": "contextual_history_course",
                "risk": "none",
                "text": "老师讲的是史料版本差异，别啥都往现实上带",
                "context": context(name, "历史公开课", "老师在讲文献来源", ["只讨论史实"]),
                "note": "上下文明确是历史课程和史料讨论。",
                "hard_negative": True,
            },
            {
                "variant": "contextual_allusion",
                "risk": "medium",
                "text": "这一段越看越眼熟，历史剧都不敢这么拍",
                "context": context(name, "历史剧剪辑", "评论突然少了一片", ["别点名", "懂的人自然懂"]),
                "note": "上下文有借古讽今和规避点名信号。",
            },
            {
                "variant": "contextual_quote",
                "risk": "low",
                "text": "这本书哪个版本注释更全？我只想补一下背景",
                "context": context(name, "读书笔记区", "求这本书的版本", ["有电子版吗"]),
                "note": "上下文更支持正常阅读讨论。",
                "hard_negative": True,
            },
        ]

    return [
        {
            "variant": "contextual_public_news",
            "risk": "none",
                "text": "先看通报和科普链接吧，别看到关键词就说带节奏",
            "context": context(name, "公共事件信息整理", "来源是新闻和科普材料", ["别传谣"]),
            "note": "上下文明确是信息整理和科普。",
            "hard_negative": True,
        },
        {
            "variant": "contextual_public_suspicious",
            "risk": "medium",
                "text": "那天的事就不展开了，评论区突然安静得很真实",
            "context": context(name, "公共事件回顾评论", "别写具体名字", ["会被删", "换个说法"]),
            "note": "上下文有时间节点和规避表达。",
        },
        {
            "variant": "contextual_public_low",
            "risk": "low",
                "text": "排了三个小时还没轮到，窗口能不能多开一个啊",
            "context": context(name, "生活吐槽", "排队排了很久", ["窗口人太少了"]),
            "note": "公共事务抱怨较弱，普通解释仍强。",
            "hard_negative": True,
        },
    ]


def transactional_templates(category: str) -> list[dict[str, Any]]:
    name = CATEGORY_NAMES[category]
    return [
        {
            "variant": "transactional_lead",
            "risk": "high",
                "text": "日结不压，名额不多，想做的看置顶",
            "context": context(name, "兼职信息评论区", "别在平台聊，容易没", ["加号发你", "名额不多"]),
            "note": "上下文有导流、联系方式和疑似欺诈招揽。",
        },
        {
            "variant": "transactional_soft",
            "risk": "medium",
                "text": "流程别问太细，能办就是能办，急的看置顶",
            "context": context(name, "同城生活帖", "评论区突然冒出好几个类似账号", ["私信你了"]),
            "note": "有导流和疑似灰产服务，但证据仍需复核。",
        },
        {
            "variant": "transactional_hard_negative",
            "risk": "none",
                "text": "公司官网也有这个岗位，面试地址在邮件里，别加私人号",
            "context": context(name, "正规招聘帖", "企业账号已认证", ["官网也能查到"]),
            "note": "上下文支持普通招聘，不是诈骗导流。",
            "hard_negative": True,
        },
    ]


def templates_for_category(category: str) -> list[dict[str, Any]]:
    if category in STRICT_REDLINE:
        return strict_templates(category)
    if category in TRANSACTIONAL_RISK:
        return transactional_templates(category)
    return contextual_templates(category)


def make_sample(seed: dict[str, Any], index: int, template: dict[str, Any]) -> dict[str, Any]:
    category = str(seed["category"])
    family = risk_family(category)
    category_name = CATEGORY_NAMES.get(category, category)
    risk = str(template["risk"])
    hard_negative = bool(template.get("hard_negative", False)) and risk in {"none", "low"}
    primary = "none" if risk == "none" else CATEGORY_PRIMARY.get(category, "C4_典故/物品/符号借用")
    secondary = [] if primary == "none" else secondary_for_seed(seed, primary)

    return {
        "id": f"LEXICON_SEED_{index:04d}_{str(template['variant']).upper()}",
        "split": "train",
        "source_type": "synthetic",
        "platform": PLATFORMS[(index - 1) % len(PLATFORMS)],
        "text": str(template["text"]),
        "context": template["context"],
        "risk_level": risk,
        "encoding_primary": primary,
        "encoding_secondary": secondary,
        "context_required": risk != "none",
        "ambiguity": ambiguity_for_risk(risk),
        "evidence_strength": evidence_for_risk(risk),
        "freshness": "stable",
        "hard_negative": hard_negative,
        "target_known": risk == "high",
        "target_reference": "匿名化目标对象或事件" if risk in {"high", "medium"} else "",
        "should_explain_target": False,
        "reasoning": reasoning(
            text=str(template["text"]),
            risk=risk,
            primary=primary,
            family=family,
            category_name=category_name,
            context_note=str(template["note"]),
        ),
        "quality_status": "needs_revision",
        "review_notes": (
            f"source=sensitive_lexicon_seed; category={category}; risk_family={family}; "
            f"variant={template['variant']}; bucket={seed.get('bucket', '')}; "
            f"matched_term={seed.get('term', '')}; term_source_files={','.join(seed.get('source_files', []))}; "
            "needs_human_review; not_merged"
        ),
    }


def main() -> int:
    seeds = [seed for seed in load_jsonl(SEEDS_PATH) if seed.get("category") in STRICT_REDLINE | CONTEXTUAL_RISK | TRANSACTIONAL_RISK]
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for seed in seeds:
        by_category[str(seed["category"])].append(seed)

    samples: list[dict[str, Any]] = []
    index = 1
    for category in sorted(by_category):
        category_seeds = by_category[category]
        for offset, template in enumerate(templates_for_category(category)):
            seed = category_seeds[offset % len(category_seeds)]
            samples.append(make_sample(seed, index, template))
            index += 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        for sample in samples:
            handle.write(json.dumps(sample, ensure_ascii=False, separators=(",", ":")) + "\n")

    print(f"Wrote {len(samples)} lexicon seed candidate samples to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
