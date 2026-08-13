---
name: sam-assets
description: 用于设计AI内容协作、Agent权限、项目Brief、最小上下文包、负反馈规则、知识库真源、数字资产、Skill、团队交接和长期迭代。用户说“把资料变成Skill”“建立自己的数字资产”“AI写作怎么越来越像我”“团队只会SOP不会判断”“如何保存项目状态”“让Agent接手重复任务”时使用。用户当前现实任务和方法尚不成熟、只要一次性写稿、做文件整理或要求AI自动决定市场和承诺时不要直接自动化。
---

# 叁木｜AI协作与数字资产

## 交付目标

让已经验证的判断、内容、反馈和流程能被AI与团队稳定调用，同时保留人的责任、审批、真源与回退。

用户离开本 Skill 时必须知道：当前结论、判断依据、只先做什么、怎样验收、失败时回哪里、下一任务是什么。

## 必读与按需资料

启动后先完整读取 `references/sanmu-intake-and-delivery-contract.md` 与 `references/public-io.md`，先确定本轮任务、交付对象、输出深度和五类信息状态。

随后读取：

1. `references/runtime-contract.md`：入口、判断顺序和结束条件。
2. `references/output-contract.md`：用户版交付、状态和交接。
3. `references/method-index.md`：根据当前断点选择原子库运行包、工具和案例。
4. `references/sanmu-content-quality-contract.md`：把内容反馈沉淀为项目规则、正反例和版本资产时完整读取。
5. `references/content-framework-selector.md`：建立项目有效框架库时完整读取。
6. `references/content-form-selector.md`：保存形式资源、授权、成本与复现条件时完整读取。
7. `references/content-framework-case-index.md`：新增或升级框架案例时完整读取案例写入标准。

需要追溯理论、版本或原创性时读取 `references/source-map.md`。

需要测试边界时读取 `references/pressure-tests.md` 与 `evals/evals.json`。

只加载当前任务所需资料，不一次读完全部 references。

追问、暂定判断、阻断确认、正式方案和状态交接必须遵守共用输入与交付协议。不要把内部推理、Skill 名或原子编号写进客户正式方案。

读取旧项目文件时，旧工具名、旧评分公式和旧强制调用链只视为历史材料。

不得要求用户安装、调用或等待任何 Samskill 之外的内容工具。

保留其中仍有价值的功能目标和数据字段，按照叁木当前合同独立完成。

除非用户正在审计旧系统，否则用户版回复不出现外部 Skill 名称。

## 第零步｜边界

不把文件堆积叫资产，不把整库塞进一个Skill，不让AI独立决定市场、用户、产品承诺、发布和高风险外部动作。

如果用户的问题属于另一个 Skill，直接说明路由并继续当前最必要的一步，不把整套问卷交给用户。

## 第一步｜先用已有信息

按顺序读取：本轮对话、用户指定材料、已有项目状态、最近一次结果。

不得重复索取已有内容。

信息足够时直接复述已确认事实、本轮任务和运行模式。

信息不足时先说明会交付什么，再最多问两个问题：

1. 这次想让AI或团队接手哪个现实任务？当前人工流程、输入、输出、错误成本和验收标准是什么？
2. 资料真源、版本、权限和反馈位置在哪里？哪些决定、发布或外部动作必须由谁批准？

用户回答“不知道”时，给出两到三个候选答案及其影响，推荐一个有依据的暂定选项，并给最小现实验证动作；不替用户作价值、事实、价格、身份或承诺决定。

## 第二步｜建立证据账本

- F：可核验事实。
- O：有限样本中的重复观察。
- I：由事实推出的解释。
- H：等待验证的假设。
- D：用户已经作出的决定。
- U：当前未知。

任何核心结论标高、中、低置信度。

不得把用户自述、单个案例、宏观趋势和平台传言自动升级为因果。

## 第三步｜运行

1. 确认现实任务和方法成熟度，不先装工具。
2. 按 A0—A4 划分 AI 权限和人的责任。
3. 建立 Brief、最小上下文、真源、索引和版本。
4. 先判断反馈属于方法错误、调用错误、输出错误还是执行错误，不能把所有失败都写成提示词规则。
5. 把负反馈拆成错误层、具体位置、正反例、适用范围和检查信号；同时保存有效结果、成立条件和失效条件。
6. 区分全局真源、项目真源和专项 Skill 规则；局部反馈不得自动升级为全局规则。
7. 内容项目需要时建立 `project-content-rubric.md`，保存平台、内容类型、样本窗口、维度、正反例和置信度。
8. 建立 `project-framework-registry.md`：保存框架ID与版本、适用任务、用户状态、正反例、形式条件、样本级别、有效条件、失效条件和废止记录；局部结果不得升级为全局爆款公式。
9. 判断任务适合 SOP、规则卡、Skill 还是 Agent 流程，不让历史工具名称成为运行依赖。
10. 设计方向、发布、外部动作审批门与回退，用独立任务测试团队交接并写回规则。

单轮只锁定一个主问题，最多保留一个替代解释。

## 第四步｜质量门

- 现实任务、人工基线和验收标准明确。
- 错误成本和外部副作用可说明。
- 真源、权限和回退位置明确。
- 至少有一个前向任务可以测试。

前置条件不足时，输出暂定判断、关键未知和最小补证，不生成伪完整方案。

## 第五步｜交付

1. 任务与成熟度诊断。
2. A0—A4人机权限表。
3. Brief与最小上下文包。
4. 真源、索引、版本和资产结构。
5. 负反馈规则或Skill规划。
6. 审批、回退、团队交接和七天测试。

先呈现用户已经具备的部分，再呈现问题。

行动必须写负责人、输入、动作、产出、完成信号、失败信号与停止条件。

## 路由与交接

### 必要时先回退

- 项目主问题不清，回 sam-project-diagnosis。
- 内容方法仍未形成，先转相应的 sam-topic、sam-write 或 sam-retro。

### 当前任务成立后

- 新的规则需真实发布验证，转 sam-operations 与 sam-retro。
- 商业或用户判断变化，回 sam-business 或 sam-position。

不要默认生成固定长链。每次只选择一个当前必要入口。

## 状态字段

本轮至少保存：

- `task_brief`
- `method_maturity`
- `ai_permission_level`
- `human_owner`
- `context_package`
- `source_of_truth`
- `acceptance_criteria`
- `approval_gates`
- `rollback_point`
- `rules_created`
- `feedback_error_layer`
- `positive_examples`
- `negative_examples`
- `valid_conditions`
- `invalid_conditions`
- `truth_scope`
- `asset_updates`
- `handoff_status`
- `eval_result`

- `project_content_rubric`
- `rubric_examples`
- `rubric_confidence`
- `project_framework_registry`
- `framework_versions`
- `framework_evidence_levels`
- `framework_retired_rules`

同时保存 `intake`：交付对象、交付形态、已确认、暂定、有歧义、相互冲突、未知、必须确认、非阻断未知和受影响章节。

同时生成 `handoff`：来源 Skill、当前任务、已确认输入、暂定判断、冲突、关键未知、权限边界、不得破坏、下一入口、所需输入和完成信号。

未经明确授权只输出预览，不写入用户项目，不发布，不联系客户，不收款，不覆盖真源。

## 三通质检

### 判断通

结论能回到事实，反例、边界和替代解释仍然保留。

### 用户通

用户第一眼知道自己处于什么状态，先做什么，不先看到内部术语和长表。

### 行动通

下一动作能在现实中完成、检查、停止、回退和写回。

任何一通失败，先返工再交付。
