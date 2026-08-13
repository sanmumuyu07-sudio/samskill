# Samskill 公开原子库 V0.1

这是从叁木内部知识真源编译、净化并用于公开测试的知识底座。

它不是书摘合集，也不是完整私人研发库的镜像。

它公开的是可以解释、判断、行动和验证的方法原子，以及这些原子与 Samskill 任务的关系。

## 当前包含

- 17 个方法模块。
- 203 张 `SAM-*` 方法原子。
- 78 张可公开来源证据卡。
- 1 张仅登记、不复制正文的受限来源卡。
- 跨模块冲突、案例证据、时效版本和渐进加载协议。
- [原子卡到 Skill 的映射](atom-skill-map.csv)。映射会区分运行资料中已明确引用，与仅按模块职责建立的候选关系。
- [公开来源登记表](source-register.csv)。

## 怎样阅读

- 想系统理解方法：按 01—17 顺序进入模块。
- 想检查一个 Skill 的依据：打开 `atom-skill-map.csv`，先看 `mapping_basis`。`explicit_runtime_reference` 表示当前运行包明确提到该原子；`module_scope_candidate` 只表示方法职责相关，不能当作已经调用。
- 想核对理论和证据：从方法原子的 `source_ids` 进入 `sources/` 或来源登记表。
- 想测试 Samskill：先记录输入和输出，再定位错误来自用户材料、Skill 流程还是原子判断。

## 17 个模块

| 模块 | 主题 | 方法原子 | 主要关联 Skill |
|---:|---|---:|---|
| 01 | [内容时代与一人媒体](modules/01_内容时代与一人媒体/README.md) | 12 | `samskill`, `sam-project-diagnosis` |
| 02 | [行业市场与商业环境](modules/02_行业市场与商业环境/README.md) | 12 | `sam-business`, `sam-project-diagnosis` |
| 03 | [个人资产与项目起点](modules/03_个人资产与项目起点/README.md) | 12 | `sam-project-diagnosis`, `sam-assets` |
| 04 | [产品、价值与变现](modules/04_产品、价值与变现/README.md) | 12 | `sam-product`, `sam-project-diagnosis`, `sam-relationship` |
| 05 | [用户、需求与决策](modules/05_用户、需求与决策/README.md) | 12 | `sam-position`, `sam-project-diagnosis` |
| 06 | [定位公共角色与账号承诺](modules/06_定位公共角色与账号承诺/README.md) | 12 | `sam-position`, `sam-strategy` |
| 07 | [平台分发与账号基础](modules/07_平台分发与账号基础/README.md) | 12 | `sam-operations`, `sam-retro` |
| 08 | [对标研究与机制迁移](modules/08_对标研究与机制迁移/README.md) | 11 | `sam-benchmark`, `sam-reconstruct` |
| 09 | [选题与内容研究](modules/09_选题与内容研究/README.md) | 12 | `sam-research`, `sam-strategy`, `sam-topic` |
| 10 | [标题封面与开头](modules/10_标题封面与开头/README.md) | 12 | `sam-write`, `sam-edit`, `sam-audit`, `sam-operations` |
| 11 | [结构证据与口播表达](modules/11_结构证据与口播表达/README.md) | 12 | `sam-style`, `sam-write`, `sam-edit`, `sam-audit`, `sam-reconstruct` |
| 12 | [传播信任与影响力](modules/12_传播信任与影响力/README.md) | 12 | `sam-strategy`, `sam-write`, `sam-edit`, `sam-audit` |
| 13 | [生产发布与自然流运营](modules/13_生产发布与自然流运营/README.md) | 12 | `sam-operations`, `sam-assets` |
| 14 | [数据复盘与增长实验](modules/14_数据复盘与增长实验/README.md) | 12 | `sam-retro`, `sam-operations` |
| 15 | [线索销售交付与复购](modules/15_线索销售交付与复购/README.md) | 12 | `sam-relationship`, `sam-product`, `sam-retro` |
| 16 | [AI协作数字资产与团队交接](modules/16_AI协作数字资产与团队交接/README.md) | 12 | `sam-assets` |
| 17 | [行动学习与长期迭代](modules/17_行动学习与长期迭代/README.md) | 12 | `sam-assets`, `sam-project-diagnosis` |

## 证据与成熟度

每张方法原子使用三类成熟度：

- `knowledge_maturity`：解释和结构是否完整。
- `evidence_maturity`：当前来源能支持到什么程度。
- `validation_maturity`：是否经过现实任务和连续结果验证。

K5、E4 或 V2 不是质量保证，也不代表结论可以无条件外推。

平台规则、价格、法律、AI 能力和近期行业数据，使用前必须核验当前官方来源。

## 公开边界

公开版删除或不收入：

- 本机绝对路径、个人身份与联系方式。
- 客户身份、合同、付款、后台原件和未脱敏经营数据。
- 未确认再分发权限的第三方 Skill 或长文本原文。
- 内部评审对话、研发比较记录和重复版本。

受限来源不会被伪装成已公开证据，而会记录在 `source-register.csv`，让测试者看到知识缺口。

## 与 `skills/` 的关系

`skills/` 是自包含运行包；单独安装某个 Skill 仍然能够工作。

`knowledge-base/` 是公开审核、贡献和测试真源，不在当前 Beta 中成为强制运行依赖。

后续只有在映射、版本和外部测试稳定后，才考虑让多个 Skill 直接引用根级唯一真源。
