---
id: SAM-CONV-004
title: 主页与行动入口怎样承接内容
type: 入口设计原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SAM-CONV-001, SRC-SAM-HOOK-001, SRC-PLATFORM-RULES-OFFICIAL-202608]
tool_ids: [SAM-CONV-TOOL-001]
case_ids: [SAM-CONV-CASE-001]
required_inputs: [内容承诺, 账号承诺, 产品路径, 平台规则, 用户下一步]
outputs: [主页信息, 单一入口, 路径, 规则风险]
next_atoms: [SAM-CONV-005, SAM-CONV-012]
stop_conditions: [违规导流, 多入口无优先级, 主页承诺与内容冲突]
---

# 主页与行动入口怎样承接内容

## 叁木判断

内容让用户产生进一步需求，主页要在较低理解成本下回答：你长期解决什么、有什么证明、我下一步能做什么。

入口不一定都是私信或加微信。它可以是查看系列、领取公开资料、填写问卷、预约咨询、购买产品或到店。高风险与高客单服务通常需要更多资格和信息步骤。

## 设计原则

一次给一个主要行动；明确用户会得到什么；遵守平台规则；记录来源；行动后立即有确认和下一步。

## 输出标准

主页角色、证明、主要入口、备选路径、点击后反馈、来源字段、合规核验和负责人。

## 验证

让陌生用户在短时间内找到与自己任务匹配的下一步，并复述不会得到什么。大量误解说明入口承诺不清。
