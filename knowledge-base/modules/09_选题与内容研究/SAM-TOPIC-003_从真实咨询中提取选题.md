---
id: SAM-TOPIC-003
title: 从真实咨询中提取选题
type: 研究方法
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-CHRISTENSEN-JTBD-2016, SRC-SAM-USER-001, SRC-SAM-TOPIC-001]
tool_ids: [SAM-TOPIC-TOOL-002]
case_ids: [SAM-TOPIC-CASE-001]
required_inputs: [咨询原话, 触发事件, 已尝试方案, 决策疑问, 后续行为]
outputs: [重复问题簇, 决策断点, 选题候选, 隐私处理]
next_atoms: [SAM-TOPIC-009, SAM-TOPIC-010, SAM-TOPIC-011]
stop_conditions: [无授权公开隐私, 用一个客户代表市场, 只抄问句不提炼判断]
---

# 从真实咨询中提取选题

## 叁木判断

咨询的价值不只是提供用户原话，更重要的是暴露用户在哪一步需要判断、比较和证明。

## 一、提取五层

1. 用户怎样描述问题。
2. 最近发生了什么。
3. 已经尝试过什么。
4. 为什么仍然犹豫。
5. 最终采取了什么行动。

只记录第一层，会得到问答清单；连接五层，才可能得到决策型选题。

## 二、从个案到候选问题

同类问题至少跨多次咨询、评论或行为互证后，才升级为稳定栏目。

单个高情绪客户只能产生个案假设。

## 三、隐私边界

删除姓名、联系方式、具体机构和可识别细节；必要时合并多个案例，并明确是综合情境。

## 四、输出标准

用户原话、任务断点、旧方案、选题判断、证据等级、匿名方式和下一验证。

## 五、成熟度说明

K5：提取、升级、隐私与输出完整。

E4：JTBD、用户证据和项目咨询支持。

V2：待咨询语料前向回填。
