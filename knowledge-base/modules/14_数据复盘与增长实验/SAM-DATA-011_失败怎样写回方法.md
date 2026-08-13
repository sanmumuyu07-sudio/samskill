---
id: SAM-DATA-011
title: 失败怎样写回方法
type: 负反馈资产原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-HACKING-GROWTH-001, SRC-SAM-DATA-001, SRC-SAM-WORKFLOW-001]
tool_ids: [SAM-DATA-TOOL-004]
case_ids: [SAM-DATA-CASE-001]
required_inputs: [原假设, 实际执行, 结果, 偏差, 项目条件]
outputs: [失败类型, 规则修订, 保留问题, 下次设计]
next_atoms: [SAM-DATA-012, SAM-AI-006]
stop_conditions: [用情绪代替记录, 把失败全归执行, 删除原版本]
---

# 失败怎样写回方法

## 叁木判断

失败只有在能改变下一次判断时才成为资产。否则它只是一次不舒服的经历。

## 四类失败

假设错误、执行偏差、测量错误和信息不足。先分类再改规则。假设错了要修方法；执行偏差要修流程或训练；测量错了要修口径；信息不足要补观察，不急着下结论。

保留原假设与版本，不用事后解释把自己写成一直正确。失败也可能揭示项目条件变化，而不是方法本身无效。

## 输出标准

原判断、预期、实际、差异、失败类型、证据、规则修改、仍未知和复测条件。

## 验证

下一次相同信号出现时，系统能更早识别或避免；否则没有真正写回。
