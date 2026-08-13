---
id: SAM-DATA-001
title: 数据不是结果的同义词
type: 数据总原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SAM-DATA-001, SRC-PAWSON-TILLEY-1997]
tool_ids: [SAM-DATA-TOOL-001, SAM-DATA-TOOL-002]
case_ids: [SAM-DATA-CASE-001]
required_inputs: [项目目标, 数据字段, 统计周期, 内容版本, 业务结果]
outputs: [数据层级, 真实结果, 不可推断项]
next_atoms: [SAM-DATA-002, SAM-DATA-003]
stop_conditions: [目标未定义, 数据口径不明, 把播放当统一结果]
---

# 数据不是结果的同义词

## 叁木判断

数据是对某段行为的记录；结果是项目原本想改变的现实。播放、评论、咨询、付款和交付都可以是数据，但只有与当前任务对应时才是主要结果。

品牌广告 IP 可能关心品牌预算认可与接单；线索 IP 关心有效咨询和成交；公共表达还可能关心复述、关系和机会。不能用“这条爆了”省略结果定义。

## 判断方法

先写项目结果，再写内容在链路中承担哪一步，最后选择能够观察该步骤的指标。指标越靠前，越不能自动代表下游。

## 输出标准

项目结果、内容中间结果、观察指标、统计周期、可能滞后和不能由当前数据推出的结论。

## 验证

每次复盘先回答“即使这个数字变好，项目目标也可能不变吗”。若答案是可能，它只是中间信号。
