---
id: SAM-AI-007
title: 从文件夹到可调用知识库
type: 知识工程原理
owner: 叁木
version: 1.0
knowledge_maturity: K5
evidence_maturity: E4
validation_maturity: V2
status: 公开测试版
source_ids: [SRC-SAM-AI-001, SRC-SAM-WORKFLOW-001]
tool_ids: [SAM-AI-TOOL-002, SAM-AI-TOOL-003]
case_ids: [SAM-AI-CASE-001]
required_inputs: [文件清单, 真源, 主题索引, 更新责任]
outputs: [分层结构, 索引, 调用规则, 待清理项]
next_atoms: [SAM-AI-008, SAM-AI-009]
stop_conditions: [原文和结论混写, 无索引, 无版本, 不可追溯]
---

# 从文件夹到可调用知识库

文件夹只解决存放，知识库还要解决找到、理解、引用、更新和回退。叁木把原始材料、结构化知识、工作规则、项目产物和反馈记录分开，并用索引、唯一 ID、来源和版本连接。

可调用意味着：面对一个具体任务，系统能找到相关原子、案例和工具；能区分事实、判断与过期材料；产出后知道写回哪里。

随机搜到几份文件后拼接答案，不叫知识调用。若无法追溯结论来源、当前版本和适用范围，资料越多，错误可能越稳定。
