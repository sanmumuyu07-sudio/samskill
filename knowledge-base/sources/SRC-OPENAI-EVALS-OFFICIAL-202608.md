---
source_id: SRC-OPENAI-EVALS-OFFICIAL-202608
title: OpenAI Agent 工作流评测官方文档
source_type: 官方产品文档
evidence_grade: A
verification_status: 已核验
checked_at: 2026-08-12
url: https://developers.openai.com/api/docs/guides/agent-evals
---

# OpenAI Agent 工作流评测

## 能支持什么

- 端到端记录需要覆盖模型、工具、规则和交接，而不只看最终文本。
- 调试阶段可先检查代表性轨迹；规则稳定后应用固定数据集重复评测。
- 路由、提示、工具和防护变化都应比较是否造成回退。

## 不能支持什么

- 自动评分等于真实用户反馈。
- 一个测试样本可以证明普遍有效。
- 技术评测可以替代平台、市场、交易与交付结果。

## 进入叁木系统

把内容流程的输入、调用链、审批、输出和回填保存为可检查记录，并用三类用户样本做版本回归。
