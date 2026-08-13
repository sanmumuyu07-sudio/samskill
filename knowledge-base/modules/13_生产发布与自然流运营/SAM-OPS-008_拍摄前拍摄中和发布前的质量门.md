---
id: SAM-OPS-008
title: 拍摄前、拍摄中和发布前的质量门
type: 质量控制原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SAM-SCRIPT-001, SRC-SAM-OPS-001, SRC-PLATFORM-RULES-OFFICIAL-202608]
tool_ids: [SAM-OPS-TOOL-003]
case_ids: [SAM-OPS-CASE-001]
required_inputs: [通过脚本, 拍摄方案, 成片, 平台规则, 事实来源]
outputs: [三门结果, 返工层级, 发布条件]
next_atoms: [SAM-OPS-009, SAM-DATA-005]
stop_conditions: [事实未核, 本人不认同, 声画改变原意, 合规高风险]
---

# 拍摄前、拍摄中和发布前的质量门

## 叁木判断

越晚发现问题，返工成本越高。三道门分别阻止判断错误、表达失真和发布风险进入下一阶段。

## 三道门

拍摄前检查选题、论证、本人语气、场景和必要画面；拍摄中检查人物状态、声音、信息遗漏和可补镜头；发布前检查剪辑是否改变含义、字幕事实、包装兑现、合规和行动入口。

## 回退原则

脚本错误退模块 11；选题错误退模块 09；包装错误退模块 10；平台规则不明退模块 07。不要在剪辑阶段用节奏和特效掩盖上游问题。

## 输出标准

每道门的通过项、问题证据、返工负责人、截止时间、停止项和最终批准人。

## 验证

记录问题在哪道门被发现及返工工时，逐月把高频错误前移到更早阶段解决。
