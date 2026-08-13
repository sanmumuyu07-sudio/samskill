---
id: SAM-DATA-002
title: 平台指标必须先统一口径
type: 字段治理原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-DOUYIN-ANALYTICS-OFFICIAL-202608, SRC-PLATFORM-RULES-OFFICIAL-202608, SRC-SAM-DATA-001]
tool_ids: [SAM-DATA-TOOL-001]
case_ids: [SAM-DATA-CASE-001]
required_inputs: [平台页面, 字段名称, 官方定义, 采集时间, 统计窗口]
outputs: [指标字典, 可比范围, 时效状态]
next_atoms: [SAM-DATA-003, SAM-DATA-005]
stop_conditions: [字段定义不可查, 不同页面同名字段混用, 周期不一致]
---

# 平台指标必须先统一口径

## 叁木判断

同名指标在不同平台、后台页面和业务场景中可能使用不同分母、去重方式和归因窗口。没有口径，比较只是数字并排。

## 字典内容

字段原名、页面、官方定义、分子分母、是否去重、更新延迟、统计周期、自然流或投流范围、可导出范围和核验日期。

播放次数不一定是独立人数；互动率可能由系统提供，也可能由运营自行计算；交易数据还受归因窗口、退款和支付状态影响。

## 输出标准

指标字典、跨期可比字段、不可比字段、需要重算字段和下次复查日期。

## 验证

保存后台截图或导出表头。页面改版、字段消失或定义变化时，切断旧数据连续性并明确标注，不静默拼接。
