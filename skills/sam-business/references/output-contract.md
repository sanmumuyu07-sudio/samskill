# 内部状态与交接合同

本文件只供保存状态和跨 Skill 交接。

普通用户与客户的最终结果必须使用 `assets/output-template.md`，不得把本文件直接拼在报告正文后。

## 生成条件

只有以下情况生成：

- 用户明确要求保存项目。
- 当前结论需要交给另一个 Skill 继续。
- 团队成员需要接手。
- 需要版本、权限或回退审计。

## 最低状态

```yaml
intake:
  task: ""
  delivery_audience: "self|team|client|project"
  output_depth: "quick|working|panorama"
  confirmed: []
  tentative: []
  ambiguous: []
  conflicting: []
  unknown: []
  blocking_confirmations: []
  affected_sections: []
```

## 最低交接

```yaml
handoff:
  from_skill: ""
  to_skill: ""
  current_task: ""
  confirmed_inputs: []
  tentative_judgments: []
  conflicts: []
  key_unknowns: []
  do_not_break: []
  permission_boundary: []
  completion_signal: ""
```

## 规则

1. 只给一个当前必要的 `to_skill`；没有就留空。
2. 未经授权不写入本地、不覆盖旧状态。
3. 客户正式方案只用自然语言说明已确认、暂定、待确认和下一任务。
4. 专项状态字段继续使用各 Skill 的 `assets/state-delta.schema.json`。

