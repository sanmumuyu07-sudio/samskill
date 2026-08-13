---
id: SAM-SCRIPT-012
title: 文案质检与返工路径
type: 综合质检原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-TOULMIN-ARGUMENT-1958, SRC-SAM-SCRIPT-001, SRC-SAM-WORKFLOW-001]
tool_ids: [SAM-SCRIPT-TOOL-002, SAM-SCRIPT-TOOL-003, SAM-SCRIPT-TOOL-004]
case_ids: [SAM-SCRIPT-CASE-001]
required_inputs: [完整草稿, 选题任务, 来源, 说话者样本, 发布形式]
outputs: [问题定位, 返工层级, 可发布稿, 未解决风险]
next_atoms: [SAM-SPREAD-001, SAM-OPS-008]
stop_conditions: [关键事实未核, 承诺无法兑现, 论证断裂, 说话者拒绝承担观点]
---

# 文案质检与返工路径

## 叁木判断

质检不是把每句话润色得更顺，而是从上游到下游找到第一个会让内容失效的断点。上游没通过，不进入下游美化。

## 三通质检

### 第一通：判断与证据

选题任务是否明确；主张是否具体；材料能否支持；边界与反例是否保留；事实是否可追溯。

### 第二通：结构与理解

段落是否连续推进；概念是否有前置解释；案例是否承担明确任务；包装是否被正文兑现。

### 第三通：口播与发布

本人能否自然说出；镜头、字幕或画面是否承担部分解释；是否合规；结尾行动是否与前文一致。

## 返工优先级

先改选题与主张，再改证据和结构，最后才改措辞。若问题来自定位、用户或产品，退回对应模块，不在文案里硬补。

## 输出标准

第一个断点、问题证据、返工层级、具体修改动作、停止项、可发布条件和下一模块。

## 验证

保留修改前后版本及修改理由；发布后把停留、反馈质量和事实纠错写回。没有结果回填的“优秀文案”只算内部判断。
