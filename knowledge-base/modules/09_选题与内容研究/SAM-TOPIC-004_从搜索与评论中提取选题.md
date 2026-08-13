---
id: SAM-TOPIC-004
title: 从搜索与评论中提取选题
type: 研究方法
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SIMON-ATTENTION-1971, SRC-PLATFORM-RECOMMENDATION-OFFICIAL-202608, SRC-SAM-TOPIC-001]
tool_ids: [SAM-TOPIC-TOOL-002]
case_ids: [SAM-TOPIC-CASE-001]
required_inputs: [搜索词, 联想词, 结果页, 评论原文, 内容上下文, 时间]
outputs: [表达语言, 问题假设, 竞争供给, 待验证选题]
next_atoms: [SAM-TOPIC-009, SAM-TOPIC-011]
stop_conditions: [搜索词等同支付需求, 高赞评论代表全部用户, 脱离原内容引用]
---

# 从搜索与评论中提取选题

## 叁木判断

搜索更接近主动表达的问题，评论更接近内容刺激后的公开反应。两者都重要，但回答不同问题。

## 一、搜索能告诉什么

用户使用什么词、问题是否反复出现、现有内容怎样回答、供给在哪些角度拥挤。

它不能单独证明支付意愿和问题严重程度。

## 二、评论能告诉什么

用户在哪里认同、反对、补充、提问和讲述经历。

评论受到原内容立场、评论排序和愿意发言人群影响，不等于沉默用户整体意见。

## 三、互证方式

搜索词提供主动问题，评论提供反应语言，咨询与行为验证行动，产品与交付验证价值。

## 四、反例

看到“我也是”高赞评论，就认定这是集体潜意识并批量做同类内容。

共鸣是真实反应，不自动说明商业需求和长期价值。

## 五、输出标准

来源链接、原话、上下文、可以推出、不能推出、选题候选和补证动作。

## 六、成熟度说明

K5：搜索、评论、偏差和互证完整。

E4：注意力、平台机制和项目记录支持。

V2：待多源选题对照。
