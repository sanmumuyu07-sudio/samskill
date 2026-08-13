---
id: SAM-OPS-006
title: 内容库存怎样建立
type: 生产缓冲原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SAM-WORKFLOW-001, SRC-SAM-OPS-001]
tool_ids: [SAM-OPS-TOOL-002]
case_ids: [SAM-OPS-CASE-001]
required_inputs: [内容状态, 发布节奏, 时效性, 制作周期]
outputs: [库存分层, 状态字段, 最低缓冲, 过期规则]
next_atoms: [SAM-OPS-007, SAM-OPS-009]
stop_conditions: [只堆选题不推进, 时效内容长期积压, 库存没有负责人]
---

# 内容库存怎样建立

## 叁木判断

内容库存不是收藏夹数量，而是已经达到明确状态、能被下一环节直接接收的内容资产。

## 状态分层

素材待核、选题通过、脚本通过、待拍、待剪、待审、待发、已发待复盘。每一层都要有完成定义和过期规则。

时效内容、常青内容和商业节点内容分开管理。热点可能当天过期，核心方法可以长期加工，销售节点需要倒推发布日期。

## 输出标准

每条内容的 ID、状态、负责人、截止时间、上游材料、下一动作、时效等级和阻塞原因。

## 验证

团队任何时点都能回答未来一周能发布什么，以及若某人缺席，哪些库存可以继续推进。
