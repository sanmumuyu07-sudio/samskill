---
id: SAM-AI-005
title: Context怎样影响产出质量
type: 上下文工程原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SAM-AI-001]
tool_ids: [SAM-AI-TOOL-002]
case_ids: [SAM-AI-CASE-001]
required_inputs: [稳定背景, 项目状态, 本轮材料, 版本优先级]
outputs: [最小上下文包, 冲突清单, 缺失信息]
next_atoms: [SAM-AI-006, SAM-AI-007]
stop_conditions: [上下文相互冲突未标版本, 全库无差别塞入, 真源不明]
---

# Context 怎样影响产出质量

AI 不只受一句指令影响，也受它本轮看见的背景、规则、项目状态、案例和历史错误影响。上下文缺失会让它猜；上下文冲突会让它随机取舍；上下文过多会稀释当前任务。

叁木把上下文分为稳定背景、项目状态、本轮材料和禁止边界。每轮只装载完成任务需要的最小集合，并标明真源、版本与优先级。

检验标准不是文件数量，而是 AI 能否准确复述当前阶段、已确认结论、未知问题、允许动作和交付标准。
