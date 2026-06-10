# 重复文本清洗预览

本报告基于 `data/raw/duplicate_text_human_feedback.json` 生成，只是预览，不修改正式 `data/processed/combined_candidates.*`。

## 总览

- 输入正式样本：860
- 预览输出样本：775
- 预览删除样本：85
- 需重写组数：3
- 保留样本中的标签建议数：14

## 删除/保留动作

| action | count |
|---|---:|
| `delete_or_exclude` removed | 49 |
| `keep_or_keep_one` removed | 15 |
| `keep_with_label_change` removed | 14 |
| `rewrite` removed | 7 |

## 需重写组

- 重复组 01：`rewrite_keep_one`；NB 是 New Balance 的鞋款缩写，不是别的意思；退回重写，且保留一条就够了。nb 是鞋款本身就是在对 nb 做解释，文本可以变成“这块 nb 真好看”，然后解读 nb 对意思，也就是这里出现的是审核视角的词，并非评论本身。其实这个例子很好，nb 可以理解成牛逼，可以理解成新百伦，但就是样例不太行。
- 重复组 42：`rewrite_group`；英明两个字刷得太整齐，像反话又像真粉；病句，重写，不像正常评论。
- 重复组 52：`rewrite_style_statement`；这部历史纪录片讲的是史料争议，不涉及现实类比；陈述句，以后少点这种陈述句行不行，跟说明书一样。

## 输出文件

- `data/processed/combined_candidates_duplicate_cleaning_preview.jsonl`
- `data/processed/combined_candidates_duplicate_cleaning_preview.json`
- `data/raw/duplicate_text_rewrite_candidates.json`
- `data/processed/duplicate_cleaning_preview_report.json`

下一步：人工确认本预览后，才能考虑 apply 到正式 processed，并重建 SFT/split。
