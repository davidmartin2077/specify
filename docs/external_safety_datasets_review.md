# 外部安全数据集接入评估

本报告只评估外部数据，不修改正式 `data/processed/combined_candidates.*`。
外部标签只作为候选信号，不能替代本项目的人工复核、语境判断和推理链重塑。

## 数据集概览

| 数据集 | 行数 | 文本字段 | 标签字段 | 唯一文本 | 重复额外行 | 平均长度 | P90 长度 | 风险提示词命中行 |
|---|---:|---|---|---:|---:|---:|---:|---:|
| ToxiCN | 12011 | `content` | `toxic` | 12011 | 0 | 37.96 | 82 | 654 |
| COLD | 25726 | `TEXT` | `label` | 25656 | 70 | 47.89 | 98 | 1777 |
| ChineseSafe | 20000 | `text` | `label` | 19998 | 2 | 82.37 | 193 | 1838 |

## 标签/主题分布

### ToxiCN

标签分布：

- `1`：6461
- `0`：5550

主题分布：

- `race`：4770
- `gender`：2874
- `region`：2370
- `lgbt`：1997

### COLD

标签分布：

- `0`：13003
- `1`：12723

主题分布：

- `race`：10698
- `region`：8449
- `gender`：6579

### ChineseSafe

标签分布：

- `违规`：10000
- `不违规`：10000

subject 分布：

- `不违规`：10000
- `偏见歧视`：1000
- `淫秽色情`：1000
- `财产隐私`：1000
- `心理健康`：1000
- `违法犯罪`：1000
- `脏话侮辱`：1000
- `身体伤害`：1000
- `政治错误`：1000
- `道德伦理`：1000
- `变体词`：1000

## 转换预览

ChineseSafe 加载状态：`loaded`。

已生成 `data/raw/external_safety_import_preview.jsonl/.json`。这些样本全部保持：

- `source_type=real`
- `quality_status=needs_revision`
- `review_notes` 包含 `external_import_preview` 与 `not_merged`
- 不进入正式 processed

预览来源计数：

- COLD：120
- ChineseSafe：100
- ToxiCN：120

## 初步判断

1. ToxiCN/COLD 的真实评论质感明显优于当前项目中早期 AI 扩写样本，适合补充辱骂、歧视、地域/性别/race/lgbt 边界。
2. ChineseSafe 更接近安全评测基准，适合补类别体系、变体/谐音和外部评测，不应直接全量转训练。
3. 外部数据普遍缺少标题、话题、真实背景和反证；接入后必须重塑 `context` 与 `reasoning`。
4. 下一步应人工抽查转换预览，再决定每个来源保留比例和映射规则。
