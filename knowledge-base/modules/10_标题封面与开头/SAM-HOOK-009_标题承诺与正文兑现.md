---
id: SAM-HOOK-009
title: 标题承诺与正文兑现
type: 兑现原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-HOPKINS-DEMAND-1923, SRC-KELLER-BRAND-EQUITY-1993, SRC-SAM-HOOK-001]
tool_ids: [SAM-HOOK-TOOL-002]
case_ids: [SAM-HOOK-CASE-001]
required_inputs: [标题承诺, 正文结论, 证据, 适用条件, 行动建议]
outputs: [兑现表, 缺口, 修正版本]
next_atoms: [SAM-HOOK-010, SAM-HOOK-012, SAM-SCRIPT-001]
stop_conditions: [承诺无法证明, 标题与正文不同问题, 省略关键限制]
---

# 标题承诺与正文兑现

## 叁木判断

标题不是获得点击后就完成任务。它向用户借了一次注意力，正文必须归还相应信息、证据和边界。

## 三项对照

- 对象一致：标题说谁，正文就服务谁。
- 问题一致：标题提出什么，正文就回答什么。
- 强度一致：标题承诺的范围、数字和结果，正文都能证明。

## 反例

标题写“普通人做 IP 的完整方法”，正文只讲昵称和简介；或标题写“算法最大变化”，正文没有任何官方或后台证据。

## 输出标准

逐句列标题承诺、正文位置、证据、限制和未兑现项。

## 成熟度说明

K5：对象、问题、强度和检查完整。

E4：广告与品牌信任支持。

V2：待完读和负反馈对照。
