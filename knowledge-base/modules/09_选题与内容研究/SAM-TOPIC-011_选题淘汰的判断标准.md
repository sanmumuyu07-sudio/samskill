---
id: SAM-TOPIC-011
title: 选题淘汰的判断标准
type: 判断标准
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SAM-TOPIC-001, SRC-SAM-POS-001, SRC-PLATFORM-RULES-OFFICIAL-202608]
tool_ids: [SAM-TOPIC-TOOL-004]
case_ids: [SAM-TOPIC-CASE-001]
required_inputs: [选题卡, 来源证据, 账号承诺, 合规, 内容任务, 制作成本]
outputs: [保留打磨测试淘汰, 致命项, 修正动作]
next_atoms: [SAM-TOPIC-012, SAM-HOOK-001]
stop_conditions: [事实错误, 侵犯隐私, 与账号承诺根本冲突]
---

# 选题淘汰的判断标准

## 叁木判断

不采用简单总分决定生死。某些问题是致命项，不能被其他高分抵消。

## 一、四种结论

- 保留：证据、任务、定位和执行都可用。
- 打磨：关系成立，但角度、证据或范围不清。
- 测试：价值不确定，但成本和风险可控。
- 淘汰：事实、伦理、合规、定位或资源存在致命冲突。

## 二、六项判断

用户相关、问题真实、判断新增、证据可得、账号一致、成本风险可控。

每项写事实，不只打分。

## 三、致命项

造假、侵权、隐私暴露、无法兑现的结果、错误行业资质和吸引明确错误用户。

## 四、反例

一个题数据潜力很高、也能讲，但会让账号长期吸引与产品完全无关的人。总分可能及格，经营上仍应淘汰。

## 五、输出标准

结论、依据、致命项、可修正项、最小测试和回填日期。

## 六、成熟度说明

K5：四种动作、六项证据和致命项完整。

E4：选题、定位与平台规则支持。

V2：待淘汰规则一致性测试。
