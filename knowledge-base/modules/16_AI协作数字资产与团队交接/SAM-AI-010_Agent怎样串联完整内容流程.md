---
id: SAM-AI-010
title: Agent怎样串联完整内容流程
type: 工作流编排原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-OPENAI-EVALS-OFFICIAL-202608, SRC-SAM-AI-001, SRC-SAM-WORKFLOW-001]
tool_ids: [SAM-AI-TOOL-004]
case_ids: [SAM-AI-CASE-001]
required_inputs: [用户任务, 当前阶段, 项目状态, 可用Skill, 权限]
outputs: [动态调用链, 中间产物, 下一路由]
next_atoms: [SAM-AI-011, SAM-AI-012]
stop_conditions: [不识别阶段直接跑全流程, 中间状态不保存, 路由无法解释]
---

# Agent 怎样串联完整内容流程

完整不等于每次把定位、选题、文案、发布和复盘全跑一遍。Agent 先识别用户处境和当前断点，再读取项目状态，调用相关原子、工具与 Skill，保存中间产物并把用户送到正确下一步。

每次运行要留下：输入、调用理由、使用来源、工具动作、人工审批、输出、失败和状态。这样才能检查是选错了方法、工具执行错了，还是现实假设本身错误。

工作流质量要用代表性轨迹和固定测试集比较，而不是只挑一份漂亮结果展示。
