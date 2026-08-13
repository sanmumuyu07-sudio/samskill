# 贡献指南

感谢你帮助 Samskill 变得更可靠。

公开反馈入口：<https://github.com/sanmumuyu07-sudio/samskill/issues>

## 先说明问题

提交修改前，请写清：

1. 哪个 Skill。
2. 什么真实任务触发了问题。
3. 实际输出哪里失败。
4. 期望输出是什么。
5. 哪条证据或边界支持修改。

不要只提交“感觉更好”“更犀利”“更像人”之类无法检查的修改。

## 修改原则

- 保留 `SKILL.md` 的任务边界与渐进读取。
- 专业细节放 `references/`，用户模板放 `assets/`。
- 用户版输出不混入机器 YAML。
- 不增加外部私有 Skill 运行依赖。
- 不写绝对流量、收益和因果承诺。
- 新规则必须提供正例、反例、适用范围和失效条件。

## 测试

修改后至少运行：

```bash
python3 scripts/validate_public_release.py
python3 scripts/validate_public_knowledge_base.py
```

涉及触发、输入或输出时，同时更新对应 `evals` 或 `tests/`。

涉及 Skill 定义时，同时运行：

```bash
python3 scripts/validate_skills.py
python3 -m unittest tests/test_release.py -v
```

## 提交说明

提交贡献代表你有权提供这些内容，并同意它们按本仓库 MIT 许可证发布。

建议在提交信息中加入开发者来源证明：

```text
Signed-off-by: Your Name <your-email@example.com>
```

这不是索取身份证明。

它用于声明：提交是你创作的、你有权提交的，或你有权在相同开源条件下转交。

详细规则见 [Developer Certificate of Origin 1.1](https://developercertificate.org/)。

## 材料与版权

只提交你有权公开的内容。

案例必须脱敏。

书籍、课程、文章和其他 Skill 只能引用必要信息与公共方法，不能打包受保护全文。

不要把客户、雇主或合作项目的私有信息作为测试样例提交。
