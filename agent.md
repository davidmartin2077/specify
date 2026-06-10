# 项目记忆

## 当前基准

正式数据已经从 860 条清洗为 775 条，随后融合 ToxiCN/COLD/ChineseSafe 各 160 条。当前正式数据为 1255 条。

核心产物：

- `data/processed/combined_candidates.jsonl`：正式样本 1255 条。
- `data/mvp/sft_candidates.jsonl`：SFT 样本 1255 条。
- `data/processed/splits/`：train 1005、validation 125、test 125。
- `docs/risk_coverage_report.md`：基于 1255 条重新生成的覆盖报告。

正式分布：

```text
high    251
medium  460
low     162
none    382

needs_context  237
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
toxicn                  160
cold                    160
chinesesafe             160
```

## 已做完

- phase3 第二波已入正式数据，不要重复导入。
- 用户已复核正式数据里的 53 组重复文本。
- 已按复核结果应用清洗：正式数据从 860 条降到 775 条。
- 已重建 SFT 数据和 train/validation/test split。
- `scripts/build_sft_dataset.py` 已移除 SFT 输入里的合成回复上下文。
- `scripts/fuse_external_real_datasets.py` 已把 ToxiCN、COLD、ChineseSafe 各 160 条融合进正式数据；脚本会先移除旧外部融合样本再重融，避免重复追加。
- 覆盖分析已基于 1255 条重跑。

## 当前决策

- 不再把合成回复上下文当强证据。
- 不再围绕合成互动上下文单独精修样本。
- 单条文本能判断风险的，就训练模型裸判。
- 单条文本正常的，不为了制造风险而补上下文。
- high 不强制需要上下文；上下文只给真正单句无法稳定判断的样本。
- SFT 输入已改为：`needs_context=false` 时不喂标题/话题，只给“无明确上下文”。
- 目标场景是弹幕、应用宝应用评论、QQ 音乐评论等短文本；不可公开存在或不可观测的敏感事件背景不能硬套到普通句子上。
- 但已固化、出圈、高频的鉴证圈结构梗本身就是文本证据，例如用户指出的“我家狗不让我用”“小懿你好”“这个问题我想了一百遍都想不通”“黄轩再不演就老了”“我是来xx的，你们要干什么？”均已恢复为 high。
- 外部数据的真实评论感有价值；当前已融合三源各 160 条，并过滤 ChineseSafe 中的问答题、填空题、改写题、应用简介等非评论文本。

## 下一步

1. 继续替换人机感强、像说明书、像审核员视角的旧合成样本。
2. 建第一版离线评测脚本，分别测 unsafe recall 和 false positive。
3. 后续扩充优先复用真实评论数据，不再批量生成模板评论。

## 工作纪律

- 不要重新跑已完成的导入 apply。
- 不要再生成大堆审计文档；需要报告时尽量短。
- 不要 `git push`，除非用户明确要求。
- 修改正式数据后必须重建 SFT、split，并校验 JSONL。
