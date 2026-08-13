---
id: SAM-AI-009
title: Skill为什么需要原子库
type: 系统分层原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-OPENAI-SKILLS-OFFICIAL-202608, SRC-SAM-AI-001]
tool_ids: [SAM-AI-TOOL-003, SAM-AI-TOOL-004]
case_ids: [SAM-AI-CASE-001]
required_inputs: [现实任务, 判断原子, 工具, 案例, 路由]
outputs: [Skill边界, 原子调用表, 缺失基石]
next_atoms: [SAM-AI-010, SAM-AI-011]
stop_conditions: [只有提示词没有判断标准, 原子来源不明, Skill包办所有问题]
---

# Skill 为什么需要原子库

Skill 保存“遇到什么任务，读取什么，按什么步骤输出什么”。但流程中的判断标准、概念边界、证据和反例必须来自原子库。否则 Skill 只是一个更长、更稳定的提示词外壳。

原子库不直接替用户跑流程；Skill 也不重新发明方法。一个成熟 Skill 要声明入口、所需输入、调用原子、分支、工具、停止条件、输出和下一路由。

如果更换模型后结论完全漂移，或 Skill 无法解释为什么这样判断，说明它没有真正接上方法底座。
