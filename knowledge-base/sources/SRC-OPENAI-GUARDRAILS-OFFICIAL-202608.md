---
source_id: SRC-OPENAI-GUARDRAILS-OFFICIAL-202608
title: OpenAI Agent Guardrails 与人工审批官方文档
source_type: 官方产品文档
evidence_grade: A
verification_status: 已核验
checked_at: 2026-08-12
url: https://developers.openai.com/api/docs/guides/agents/guardrails-approvals
---

# OpenAI Agent Guardrails 与人工审批

## 能支持什么

- 输入、输出和工具动作需要不同位置的校验。
- 涉及编辑、命令和敏感副作用时，可暂停并等待人工批准或拒绝。
- 审批后应从已保存状态续跑，而不是丢失前序状态重新开始。

## 不能支持什么

- 所有内容业务都必须使用相同技术实现。
- 有防护规则就不会犯错。
- 一次入口确认可以代替工具节点的局部审批。

## 进入叁木系统

转成方向门、发布门和外部动作门，并要求每个副作用节点有责任人、状态与回退方式。
