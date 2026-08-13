---
id: SAM-CONV-005
title: 私信和咨询怎样完成问题诊断
type: 咨询对话原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-RACKHAM-SPIN-1988, SRC-SAM-CONV-001, SRC-CHRISTENSEN-JTBD-2016]
tool_ids: [SAM-CONV-TOOL-002]
case_ids: [SAM-CONV-CASE-001]
required_inputs: [用户原问题, 处境, 已有尝试, 影响, 目标, 约束]
outputs: [真问题, 信息缺口, 适配状态, 下一步]
next_atoms: [SAM-CONV-006, SAM-CONV-007]
stop_conditions: [医疗法律财务等越界, 用户只需公开信息, 产品明显不适配]
---

# 私信和咨询怎样完成问题诊断

## 叁木判断

咨询的首要任务不是介绍产品，而是判断用户的问题是否成立、问题在哪一层、当前信息够不够，以及双方是否适配。

## 对话顺序

让用户完整描述；澄清模糊词；确认事实与已有尝试；理解不处理的影响；识别目标、约束和决策者；再判断产品是否能改变结果。

不是每个问题都要成交。信息问题可直接给出处；情绪或专业越界问题应转介；条件不足先让用户采集信息；不适配明确结束。

## 输出标准

原问题、重写后的问题、事实、假设、缺失信息、适配结论、理由、下一步和未承诺事项。

## 验证

用户即使不购买，也能准确理解自己下一步；成交用户进入交付后不需要重新推翻销售阶段的诊断。
