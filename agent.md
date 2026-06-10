# 项目记忆

## 当前基准

正式数据已经从 860 条清洗为 775 条，重复文本人工反馈已应用。当前不要再回头复核那 53 组重复 text。

核心产物：

- `data/processed/combined_candidates.jsonl`：正式样本 775 条。
- `data/mvp/sft_candidates.jsonl`：SFT 样本 775 条。
- `data/processed/splits/`：train 621、validation 77、test 77。
- `docs/risk_coverage_report.md`：基于 775 条重新生成的覆盖报告。

正式分布：

```text
high    152
medium  272
low     163
none    188

hard_negative     315
context_required  242
```

来源分布：

```text
grok                      50
user                       7
meme_expansion            35
gemini_expansion         120
sensitive_lexicon_seed    33
phase2_seed              100
phase3_first_wave        245
phase3_second_wave       185
```

## 已做完

- phase3 第二波已入正式数据，不要重复导入。
- 用户已复核正式数据里的 53 组重复文本。
- 已按复核结果应用清洗：正式数据从 860 条降到 775 条。
- 已重建 SFT 数据和 train/validation/test split。
- `scripts/build_sft_dataset.py` 已移除 SFT 输入里的合成回复上下文。
- 覆盖分析已基于 775 条重跑。

## 当前决策

- 不再把合成回复上下文当强证据。
- 不再围绕合成互动上下文单独精修样本。
- 单条文本能判断风险的，就训练模型裸判。
- 单条文本正常的，不为了制造风险而补上下文。
- high 不强制需要上下文；上下文只给真正单句无法稳定判断的样本。
- SFT 输入已改为：`context_required=false` 时不喂标题/话题，只给“无明确上下文”。
- 外部数据的真实评论感有价值，但标签和推理链都要重塑后再入库。

## 下一步

1. 继续替换人机感强、像说明书、像审核员视角的样本。
2. 筛外部 340 条真实评论预览，挑一批适合重塑进正式数据。
3. 建第一版离线评测脚本，分别测 unsafe recall 和 false positive。

## 工作纪律

- 不要重新跑已完成的导入 apply。
- 不要再生成大堆审计文档；需要报告时尽量短。
- 不要 `git push`，除非用户明确要求。
- 修改正式数据后必须重建 SFT、split，并校验 JSONL。
