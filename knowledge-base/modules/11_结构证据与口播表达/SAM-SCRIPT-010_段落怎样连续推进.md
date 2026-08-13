---
id: SAM-SCRIPT-010
title: 段落怎样连续推进
type: 逻辑连续性原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-MINTO-PYRAMID-2002, SRC-TOULMIN-ARGUMENT-1958, SRC-SAM-SCRIPT-001]
tool_ids: [SAM-SCRIPT-TOOL-003]
case_ids: [SAM-SCRIPT-CASE-001]
required_inputs: [完整草稿, 每段任务, 论证链]
outputs: [段间关系, 跳步位置, 重复段落, 转场修复]
next_atoms: [SAM-SCRIPT-011, SAM-SCRIPT-012]
stop_conditions: [核心主张未定, 段落只是素材堆积, 需要靠连接词掩盖逻辑断裂]
---

# 段落怎样连续推进

## 叁木判断

段落连续不是多写几个“所以”“但是”，而是上一段产生的疑问，恰好由下一段回答。

## 六种有效关系

定义、原因、证据、例子、反例和行动。每一段至少与上一段存在一种明确关系，并让核心判断前进一步。

## 检查方法

给每段只写一句旁注：它在回答什么。再把正文隐藏，只看旁注。如果顺序无法构成完整推理，正文再顺也只是语句连续。

还要检查两个风险：段内出现多个独立任务；作者认为显然的中间一步没有说。后者常导致“听起来都对，但不知道怎么得出的”。

## 边界

有些段落看似偏题，实际在补必要背景、处理异议或建立情绪。不能只凭关键词不同删段，要先判断它是否承担推理任务。

## 输出标准

段落任务序列、段间关系、跳步、重复、前置依赖与修复建议。

## 验证

随机抽掉一段，看前后是否仍成立；让盲听者在暂停处预测下一段应该回答什么。预测方向长期偏离，说明推进关系不清。
