---
id: SAM-AI-006
title: 负反馈怎样变成规则资产
type: 规则学习机制
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SAM-AI-001, SRC-OPENAI-EVALS-OFFICIAL-202608]
tool_ids: [SAM-AI-TOOL-003]
case_ids: [SAM-AI-CASE-001]
required_inputs: [错误输出, 具体反馈, 正确样例, 适用范围]
outputs: [错误归因, 新规则, 回归样本]
next_atoms: [SAM-AI-008, SAM-AI-009]
stop_conditions: [只有喜欢不喜欢, 原因未定位, 单次偏好升级全局规则]
---

# 负反馈怎样变成规则资产

“这版不对”不是资产。只有把错误定位到输入、来源、路由、判断、表达、工具或验收中的具体一层，负反馈才可能被复用。

先保存错误样本和正确样本，再写适用条件、检查信号和修正动作。偶发偏好留在项目层；重复错误进入规则；跨项目稳定机制才进入原子；需要固定输入、分支与输出时再变成 Skill。

新增规则后要用旧错误和正常样本一起复测。只修复一个案例，却让其他任务变差，不算学习成功。
