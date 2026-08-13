---
id: SAM-DATA-008
title: 数据异常怎样定位到具体节点
type: 断点诊断原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-PAWSON-TILLEY-1997, SRC-SAM-DATA-001, SRC-DOUYIN-ANALYTICS-OFFICIAL-202608]
tool_ids: [SAM-DATA-TOOL-003]
case_ids: [SAM-DATA-CASE-001]
required_inputs: [异常指标, 相邻节点, 内容版本, 流量来源, 历史基线, 系统变更]
outputs: [首个异常, 候选原因, 排除项, 路由]
next_atoms: [SAM-DATA-009, SAM-DATA-012]
stop_conditions: [单指标直接下结论, 没有基线, 关键字段缺失]
---

# 数据异常怎样定位到具体节点

## 叁木判断

从结果逆推原因时，先找链路中最早出现异常的位置，再列出多个解释。越靠后的异常，越可能受多个上游共同影响。

曝光异常先查来源、规则、账号和题材环境；停留异常查人群、包装、开头与播放体验；中段异常查结构、理解成本与制作；主页低查角色预期；咨询低查产品、入口与信任；成交低查销售、适配与风险。

## 输出标准

异常事实、首个异常节点、三个候选原因、支持证据、反证、还缺什么、转入哪个模块。

## 验证

用下一轮有记录的变化区分候选原因。没有足够信息时明确写“不确定”，不强行给唯一诊断。
