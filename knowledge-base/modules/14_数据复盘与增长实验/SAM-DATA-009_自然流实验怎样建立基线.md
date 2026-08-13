---
id: SAM-DATA-009
title: 自然流实验怎样建立基线
type: 增长实验原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-NIST-DOE-2026, SRC-HACKING-GROWTH-001, SRC-SAM-DATA-001]
tool_ids: [SAM-DATA-TOOL-004]
case_ids: [SAM-DATA-CASE-001]
required_inputs: [假设, 基线样本, 主要变化, 响应指标, 不可控因素, 资源]
outputs: [实验登记, 比较组, 观察周期, 停止条件]
next_atoms: [SAM-DATA-010, SAM-DATA-011]
stop_conditions: [同时改变过多变量, 无基线, 结果指标事后挑选, 安全合规风险]
---

# 自然流实验怎样建立基线

## 叁木判断

自然流无法完全控制平台、题材和时间环境，因此多数内容实验只能提供更好的比较证据，不能声称严格因果。

## 最小登记

先写假设、为什么值得测、主要改变、保持不变项、响应指标、观察周期、同时变化、风险和成功／停止条件。

“一次只改一个变量”适合初步排查，但不同变量会相互作用，连续发布也不是真正随机分配。结论必须保留这些限制。

## 输出标准

基线范围、版本 A/B、样本与周期、主要响应、次要响应、外部事件和回填日期。

## 验证

实验开始后不因中途数据好看修改成功指标；失败、无差异和无法判断都要记录。
