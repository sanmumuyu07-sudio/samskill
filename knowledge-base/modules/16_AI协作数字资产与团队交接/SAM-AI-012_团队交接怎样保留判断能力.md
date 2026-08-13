---
id: SAM-AI-012
title: 团队交接怎样保留判断能力
type: 组织交接原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SAM-AI-001, SRC-APQC-BENCHMARK-001, SRC-SAM-OPS-001]
tool_ids: [SAM-AI-TOOL-004]
case_ids: [SAM-AI-CASE-001]
required_inputs: [项目状态, 规则理由, 正反例, 权限, 最近失败]
outputs: [交接包, 试运行任务, 升级条件]
next_atoms: [SAM-ACT-009, SAM-ACT-011]
stop_conditions: [只交步骤不交理由, 受让人无法判断异常, 权限责任不清]
---

# 团队交接怎样保留判断能力

过去多次项目都说明：SOP 可以让新人模仿执行，却不自动让他识别人群变化、内容疲劳和商业断点。真正的交接不能只给“怎么做”，还要给“为什么这样做、什么情况下不能这样做”。

交接包至少包含当前状态、目标、规则理由、正反例、权限、异常信号、最近失败、升级路径和下一次复盘字段。受让人先完成一项低风险真实任务，再由原负责人检查他的判断过程，而不只看产物。

只有在负责人离场后，团队仍能发现异常、解释选择并正确回退，判断能力才算被部分保留。
