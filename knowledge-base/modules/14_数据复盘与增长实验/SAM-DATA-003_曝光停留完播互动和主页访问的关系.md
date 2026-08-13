---
id: SAM-DATA-003
title: 曝光、停留、完播、互动和主页访问的关系
type: 内容行为链原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-DOUYIN-ANALYTICS-OFFICIAL-202608, SRC-PLATFORM-RECOMMENDATION-OFFICIAL-202608, SRC-SAM-DATA-001]
tool_ids: [SAM-DATA-TOOL-001, SAM-DATA-TOOL-003]
case_ids: [SAM-DATA-CASE-001]
required_inputs: [曝光或播放, 停留字段, 时长, 互动明细, 主页行为, 流量来源]
outputs: [行为链, 异常节点, 多重解释]
next_atoms: [SAM-DATA-005, SAM-DATA-008]
stop_conditions: [字段缺失仍强行归因, 把互动类型合并后解释心理, 不看流量来源]
---

# 曝光、停留、完播、互动和主页访问的关系

## 叁木判断

这些指标描述用户在不同节点做了什么，不直接说明为什么。一个指标异常通常有多种解释，需要结合前后节点、内容版本与用户反馈缩小范围。

曝光受平台分发和题材环境影响；停留与开头、包装和人群匹配有关；完播还受时长、结构和观看场景影响；点赞、评论、收藏、分享承担不同动作；主页访问更接近对账号的进一步兴趣。

## 禁止映射

“收藏高=信息密度高”“评论低=没共鸣”“完播低=开头差”都只能是候选解释，不是唯一因果。

## 输出标准

平台行为链、指标定义、相邻节点比较、三项候选解释、支持与反证材料、下一次采集动作。

## 验证

用留存曲线、具体评论、流量来源、时长相近内容和同栏目历史共同判断，不能只看一个百分比。
