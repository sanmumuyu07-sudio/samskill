# 状态增量与交接

## 一、原则

诊断不直接覆盖项目真源。

先生成 `state_delta` 预览。

只有用户明确授权并指定位置后才写入。

每次写回必须保留旧版本、日期和来源。

## 二、状态增量字段

```yaml
state_delta:
  intake:
    delivery_audience: "self|team|client|project"
    delivery_mode: "conversation|tentative|internal|client|ledger"
    confirmed: []
    tentative: []
    ambiguous: []
    conflicting: []
    unknown: []
    blocking_confirmations: []
    nonblocking_unknowns: []
    affected_sections: []
  project_id: ""
  generated_at: ""
  diagnosis_mode: "new|checkup|symptom"
  user_role: "owner|subject|operator|advisor"
  target:
    statement: ""
    window: ""
    primary_metric: ""
    guardrail_metric: ""
  stage:
    code: "S0-S6"
    scope: ""
    confidence: "high|medium|low"
  capabilities:
    formed: []
    signals: []
    unvalidated: []
  evidence_added:
    - id: ""
      label: "F|O|I|H|D|U"
      statement: ""
      source: ""
  bottleneck:
    module: "01-17"
    statement: ""
    rationale: ""
    alternative_explanation: ""
  decisions:
    keep: []
    change: []
    defer: []
  seven_day_plan:
    - owner: ""
      action: ""
      output: ""
      done_signal: ""
      stop_condition: ""
  experiment:
    hypothesis: ""
    variable: ""
    constants: []
    window: ""
    pass_condition: ""
    fail_condition: ""
    stop_condition: ""
    scale_condition: ""
  next_route:
    function: ""
    why_now: ""
    required_inputs: []
  handoff:
    confirmed_inputs: []
    tentative_judgments: []
    conflicts: []
    key_unknowns: []
    permission_boundary: []
    do_not_break: []
    completion_signal: ""
  permission:
    preview_only: true
    approved_write_path: null
  versions:
    skill: "2.2.0-beta"
    atom_library: "2.0"
```

## 三、阶段代码

- S0｜只有愿望或模糊方向，现实任务还没有被定义。
- S1｜已经有能力、经历、产品或资源，但尚未形成可检查的机会假设。
- S2｜已经形成市场、用户、产品或定位假设，尚未取得稳定公开信号。
- S3｜已经开始发布、触达或测试，并取得部分传播、关系或需求信号。
- S4｜已经形成相对稳定的内容与关系链，但交易或交付还不稳定。
- S5｜已经发生交易与交付，正在验证复购、利润、产能与可持续性。
- S6｜已有稳定链路，正在进行团队交接、AI 协作、资产治理或规模化。

阶段不是账号年龄，也不是粉丝等级。

同一个项目可能在内容端接近 S5，在交付端只有 S3。

报告必须说明本次阶段判断对应哪条结果链。

## 四、交接包

下一个 Skill 最少收到：

- 当前目标和窗口。
- 已确认事实。
- 关键未知。
- 主断点。
- 不得破坏的已有结果。
- 本轮只允许改变的变量。
- 完成信号和停止条件。
- 写回字段。

交接时不得只写“去做内容”“优化转化”。

必须写明下一 Skill 接收的输入、要解决的问题、不得破坏的变量和完成信号。

## 五、冲突处理

新状态与旧状态冲突时：

1. 不自动覆盖。
2. 列出两个版本、来源、日期和口径。
3. 判断是事实变化、口径变化还是旧结论错误。
4. 生成版本裁决建议。
5. 用户确认后再废止旧状态。

## 六、隐私与权限

- 客户姓名、联系方式、合同和敏感经营数据默认不进入公开状态。
- 只保存诊断所需的最小字段。
- 案例公开前必须有授权状态。
- Agent 不得自行扩大读取、发布或外发权限。
