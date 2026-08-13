---
id: SAM-HOOK-011
title: 标题 A/B 测试的正确方法
type: 实验原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-HOPKINS-OFFER-TEST-1923, SRC-HACKING-GROWTH-001, SRC-SAM-HOOK-001]
tool_ids: [SAM-HOOK-TOOL-004]
case_ids: [SAM-HOOK-CASE-001]
required_inputs: [同一内容, 两个版本, 平台测试能力, 指标, 样本, 时间窗]
outputs: [实验设计, 结果, 归因边界, 下一测试]
next_atoms: [SAM-HOOK-012, SAM-DATA-001]
stop_conditions: [内容同时变化, 样本不可比, 平台无真正随机分流]
---

# 标题 A/B 测试的正确方法

## 叁木判断

两个标题先后发布，不自动构成严格 A/B 测试。时间、受众、平台分发和账号状态都可能变化。

## 一、最低要求

内容主体不变；只改变一个明确变量；预先定义指标和时间；记录平台是否真正随机分流。

无法随机时，只能称顺序对照，结论降低置信度。

## 二、指标邻近

标题先观察展示后的点击、进入或停留，不直接用成交判断标题优劣。

商业指标可以作为后续质量检查。

## 三、反例

重发时同时改标题、封面、开头和发布时间，数据上涨后归因给标题。

## 四、输出标准

假设、变量、控制项、指标、样本、异常、结论强度和下一轮。

## 五、成熟度说明

K5：实验、指标、顺序偏差和归因完整。

E4：广告测试、增长实验和项目记录支持。

V2：待真实平台测试。
