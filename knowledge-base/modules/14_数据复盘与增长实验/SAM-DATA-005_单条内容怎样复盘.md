---
id: SAM-DATA-005
title: 单条内容怎样复盘
type: 单条复盘原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SAM-DATA-001, SRC-PAWSON-TILLEY-1997]
tool_ids: [SAM-DATA-TOOL-002, SAM-DATA-TOOL-003]
case_ids: [SAM-DATA-CASE-001]
required_inputs: [内容版本, 发布时间, 平台数据, 用户反馈, 业务数据, 对比基线]
outputs: [事实摘要, 候选解释, 下一步, 不确定性]
next_atoms: [SAM-DATA-006, SAM-DATA-009]
stop_conditions: [无内容版本, 无基线, 用结果倒推唯一原因]
---

# 单条内容怎样复盘

## 叁木判断

单条复盘用来发现问题和生成假设，不足以证明稳定规律。

## 六步

确认版本与口径；写数据事实；与相近时长、题材、来源和账号阶段的基线比较；定位首个异常节点；列出多个候选解释；选择下一轮最有信息价值的动作。

用户原话必须进入复盘。数据告诉你行为变化，原话帮助解释用户如何理解，但两者都不能单独证明因果。

## 输出标准

事实、对比对象、异常节点、候选解释、反证、下一轮动作和暂不判断项。

## 验证

下一轮结果若不支持解释，就修改假设，不把失败归为执行不到位。
