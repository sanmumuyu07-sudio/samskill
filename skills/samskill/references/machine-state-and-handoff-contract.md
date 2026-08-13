# Samskill 机器状态与交接协议 V1.0

本文件只供 Agent 内部保存状态和跨 Skill 交接。

不得默认展示给普通用户或客户。

## 生成条件

只有用户授权保存、需要跨 Skill 接续、团队交接或版本审计时生成。

## 最低结构

```yaml
schema_version: "1.0"
release_version: "1.0.0-beta.2"
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
  nonblocking_unknowns: []
  affected_sections: []
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

1. `to_skill` 只能写一个当前必要入口。
2. 没有明确下一任务时留空，不得猜测。
3. 未经授权不写入本地。
4. 状态更新不得覆盖旧版本；保留来源、时间和修改原因。
5. 客户正式方案只呈现自然语言结论，不呈现本结构。
