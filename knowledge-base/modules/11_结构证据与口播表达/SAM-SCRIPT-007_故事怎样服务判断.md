---
id: SAM-SCRIPT-007
title: 故事怎样服务判断
type: 叙事应用原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SAM-SCRIPT-001, SRC-SAM-CASE-RULE-001]
tool_ids: [SAM-SCRIPT-TOOL-001, SAM-SCRIPT-TOOL-003]
case_ids: [SAM-SCRIPT-CASE-001]
required_inputs: [核心判断, 真实事件, 关键选择, 结果, 不确定变量]
outputs: [故事任务, 事件序列, 判断落点, 省略项]
next_atoms: [SAM-SCRIPT-008, SAM-SCRIPT-010]
stop_conditions: [虚构经历冒充事实, 故事与结论无关, 用结果倒推唯一原因]
---

# 故事怎样服务判断

## 叁木判断

故事的价值不是让内容显得真实，而是让用户看见一个判断在具体处境中如何产生后果。

## 最小故事结构

处境说明用户为什么在乎；目标说明人物想得到什么；限制说明为什么不能直接得到；选择暴露判断；结果提供反馈；复盘指出哪些关系可迁移。

如果删掉故事以后结论完全不受影响，这段故事可能只是气氛。若故事很精彩却不能回答“它证明了什么”，它也不该占据正文中心。

## 归因边界

项目故事不能把团队、平台、产品和时间窗口全部抹掉，只留下“我做了一个动作就成功”。叁木案例必须分开已知事实、个人贡献、其他贡献与未知变量。

## 输出标准

六段事件卡：处境、目标、限制、选择、结果、复盘；另附省略理由与证据状态。

## 验证

听众能否说出人物为什么这样选、这个选择产生了什么影响，以及哪些条件换了以后结论可能失效。
