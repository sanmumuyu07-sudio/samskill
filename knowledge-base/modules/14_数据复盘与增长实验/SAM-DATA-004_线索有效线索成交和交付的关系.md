---
id: SAM-DATA-004
title: 线索、有效线索、成交和交付的关系
type: 业务数据链原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-DOUYIN-ANALYTICS-OFFICIAL-202608, SRC-SAM-PROJECTS-001, SRC-SAM-OFFER-001]
tool_ids: [SAM-DATA-TOOL-001, SAM-DATA-TOOL-002]
case_ids: [SAM-DATA-CASE-001]
required_inputs: [线索定义, 有效标准, 成交状态, 收入退款, 交付结果]
outputs: [业务漏斗, 口径, 断点, 滞后]
next_atoms: [SAM-DATA-008, SAM-CONV-002]
stop_conditions: [把私信都算客资, 订单不扣退款, 不同产品合并转化率]
---

# 线索、有效线索、成交和交付的关系

## 叁木判断

线索只是表达了某种兴趣；有效线索满足产品预设条件；成交完成约定交换；交付结果说明产品是否真的帮助用户完成任务。四者不能互相替代。

## 必须定义

线索入口、去重规则、有效条件、失效原因、成交时间、收入确认、退款、交付开始与完成、复购和推荐。

地产、留学、知识库和线下课的有效标准、销售周期与结果窗口不同，应分产品计算。广告合作还需要单独记录品牌预算、执行和回款。

## 输出标准

分产品漏斗、每层数量与定义、转化周期、流失原因、负责人和可归因内容。

## 验证

随机抽查线索原文、付款与交付记录，确保数字能回到真实对象；无法回查的汇总数不进入方法结论。
