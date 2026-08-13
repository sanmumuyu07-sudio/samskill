---
id: SAM-AI-001
title: AI是执行合作者不是最终决策者
type: 人机分工原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SAM-AI-001, SRC-OPENAI-GUARDRAILS-OFFICIAL-202608]
tool_ids: [SAM-AI-TOOL-001]
case_ids: [SAM-AI-CASE-001]
required_inputs: [现实任务, 错误成本, 所需证据, 决策责任人]
outputs: [人机分工, 权限边界, 审批点]
next_atoms: [SAM-AI-002, SAM-AI-004]
stop_conditions: [责任人不明, 高风险动作未授权, 要求AI承担现实责任]
---

# AI 是执行合作者，不是最终决策者

## 叁木判断

AI 可以检索、整理、生成、比较和执行明确步骤，但谁承担错误后果，谁就必须保留最终判断。所谓“AI 决策”通常只是把选择藏进了提示词、数据、模型或默认参数里，并没有让责任消失。

## 怎样分工

低风险、可回退、标准明确的工作可以让 AI 直接执行；需要业务取舍、用户理解和内容审美的工作由 AI 给候选，人做选择；发布、付款、删除真源、合同和承诺等外部动作必须单独审批。

## 验证

回看错误时能否找到决策人、证据、批准记录和回退点。若只能说“AI 是这么建议的”，说明分工失败。
