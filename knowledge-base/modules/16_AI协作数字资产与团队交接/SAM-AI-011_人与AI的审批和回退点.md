---
id: SAM-AI-011
title: 人与AI的审批和回退点
type: 风险控制原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-OPENAI-GUARDRAILS-OFFICIAL-202608, SRC-SAM-AI-001]
tool_ids: [SAM-AI-TOOL-004]
case_ids: [SAM-AI-CASE-001]
required_inputs: [动作清单, 副作用, 权限, 版本, 恢复方式]
outputs: [审批门, 检查项, 回退方案]
next_atoms: [SAM-AI-012, SAM-DATA-011]
stop_conditions: [不可逆动作无确认, 无备份覆盖真源, 审批范围模糊]
---

# 人与 AI 的审批和回退点

审批不是流程最后让人看一眼，而是放在错误成本最高的节点。方向、发布和外部动作承担不同风险，必须分别确认。

方向门检查研究问题、用户、定位和承诺；发布门检查事实、表达、隐私和平台风险；外部动作门控制发布、发送、付款、删除和覆盖。AI 可以提出动作，但执行前要显示目标、参数、影响和恢复方法。

每个节点还要保存当前状态和上一版本。若发生错误只能重新开始，不能定位和回退，说明工作流仍是一次性对话。
