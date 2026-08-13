---
id: SAM-DATA-007
title: 中位表现比单条峰值更接近稳定能力
type: 稳定性判断原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-NIST-DOE-2026, SRC-SAM-DATA-001]
tool_ids: [SAM-DATA-TOOL-002]
case_ids: [SAM-DATA-CASE-001]
required_inputs: [连续样本, 统一指标, 分组, 异常内容]
outputs: [中位表现, 分布, 峰值解释, 稳定性判断]
next_atoms: [SAM-DATA-010, SAM-DATA-012]
stop_conditions: [样本不可比, 只取最好内容, 自动删除异常值]
---

# 中位表现比单条峰值更接近稳定能力

## 叁木判断

峰值说明某次内容在特定条件下获得过高结果；中位表现更接近当前系统通常能做到什么。两者都重要，但回答不同问题。

一条爆款可能来自题材窗口、外部转发、平台波动或内容能力。不能自动删除，也不能代表全体。先调查它为什么偏离，再决定它是错误数据、特殊事件还是新机会。

## 判断方法

在可比内容组中查看中位数、四分位、最大最小、样本量和完成率；把峰值单独做机制与条件拆解。

## 输出标准

稳定区间、峰值条件、低值原因、可重复关系、不可重复条件和下一轮验证。

## 验证

若某关系只能解释最强一条，不能改善大多数内容，就不把它写成系统能力。
