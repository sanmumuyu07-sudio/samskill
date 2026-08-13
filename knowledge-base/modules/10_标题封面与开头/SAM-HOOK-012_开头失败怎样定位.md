---
id: SAM-HOOK-012
title: 开头失败怎样定位
type: 诊断原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SAM-HOOK-001, SRC-SAM-TOPIC-001, SRC-PLATFORM-RECOMMENDATION-OFFICIAL-202608]
tool_ids: [SAM-HOOK-TOOL-002, SAM-HOOK-TOOL-004]
case_ids: [SAM-HOOK-CASE-001]
required_inputs: [选题卡, 标题封面开头, 正文, 平台数据, 用户反馈]
outputs: [失败层级, 第一修正, 不可归因项, 重测方案]
next_atoms: [SAM-TOPIC-011, SAM-SCRIPT-012, SAM-DATA-001]
stop_conditions: [正文不完整, 数据字段不明, 样本过少且无用户证据]
---

# 开头失败怎样定位

## 叁木判断

开头留存差不一定是第一句话问题。可能是选题无关、标题误导、画面不可读、正文承诺不足或分发人群错误。

## 排查顺序

1. 选题是否与目标用户有关。
2. 标题封面是否准确。
3. 开头是否建立话题、理由和必要可信度。
4. 第一段是否进入正文而非继续铺垫。
5. 分发是否进入预期人群。

## 停止优化

正文没有新判断、证据或可用内容时，不批量生成更多开头；先回模块09、11。

## 输出标准

失败层级、证据、最小改动、控制项、复查指标。

## 成熟度说明

K5：跨层诊断、停止和实验完整。

E4：选题、平台和项目数据支持。

V2：待失败样本回填。
