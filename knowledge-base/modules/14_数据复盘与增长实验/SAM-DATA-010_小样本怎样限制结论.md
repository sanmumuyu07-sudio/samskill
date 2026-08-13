---
id: SAM-DATA-010
title: 小样本怎样限制结论
type: 证据边界原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-NIST-DOE-2026, SRC-PAWSON-TILLEY-1997, SRC-SAM-DATA-001]
tool_ids: [SAM-DATA-TOOL-004]
case_ids: [SAM-DATA-CASE-001]
required_inputs: [样本量, 采样方式, 差异大小, 环境变化, 结论强度]
outputs: [可说结论, 不可说结论, 下一证据]
next_atoms: [SAM-DATA-011, SAM-DATA-012]
stop_conditions: [一两条内容写成规律, 忽略选择偏差, 只保留成功样本]
---

# 小样本怎样限制结论

## 叁木判断

小样本不是完全无用，它适合发现问题、排除明显错误和生成下一步假设；不适合给出稳定比例和普遍因果。

## 结论强度

一条内容可以说“出现过”；少量相似内容可以说“值得继续观察”；跨时间、题材和项目反复出现，才逐步形成条件性规则。仍要保留反例和平台变化。

## 选择偏差

只拆爆款、只看成功学员、只保存数据好的版本，都会让规律显得比实际稳定。失败内容和未发布候选同样是证据。

## 输出标准

样本边界、可用判断、不可外推对象、可能偏差、需要增加的比较和当前置信标签。

## 验证

后续样本到来时重新计算和审阅，不让旧方法因为已写进知识库就免于修正。
