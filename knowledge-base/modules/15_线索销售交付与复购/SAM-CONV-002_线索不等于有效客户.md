---
id: SAM-CONV-002
title: 线索不等于有效客户
type: 资格判断原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SAM-CONV-001, SRC-STRATEGYZER-VPC-2026]
tool_ids: [SAM-CONV-TOOL-001]
case_ids: [SAM-CONV-CASE-001]
required_inputs: [线索来源, 用户任务, 时间, 预算或资源, 决策者, 不适用条件]
outputs: [资格状态, 分流, 缺失信息, 无效原因]
next_atoms: [SAM-CONV-003, SAM-CONV-005]
stop_conditions: [只凭一句私信算有效, 用户未同意联系, 无隐私与信息边界]
---

# 线索不等于有效客户

## 叁木判断

线索表示有人采取了接触动作；有效客户表示他的任务、时间、资源、决策条件和产品边界存在进一步匹配可能。

“怎么收费”“发我资料”可能只是信息需求；高意愿也不代表适配。知识库适合愿意自学的人，线下课适合需要现场判断和系统搭建的人，专业服务还要检查具体资格与风险。

## 分流

有效进入诊断；信息不足补问；暂不适合进入内容或等待；明确不适合直接说明边界；超出能力转专业人士。

## 输出标准

来源、任务、紧迫性、已有替代、决策权、资源、适配状态、下一步和隐私授权。

## 验证

按无效原因和后续成交回看资格规则。若大量合格线索不适配交付，应修产品或筛选，不单纯提高销售强度。
