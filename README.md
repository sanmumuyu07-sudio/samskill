# Samskill

Samskill 是一套面向一人媒体、个人 IP、自然流短视频、内容获客与知识产品项目的 Agent Skill 系统。

它不只生成一篇内容。

它帮助用户从真实项目出发，判断市场、产品、用户、定位、对标、内容、生产、承接、数据和数字资产中的当前问题，并把结果交给下一轮行动。

当前版本：`1.0.0-beta.3`。

## 它解决什么

Samskill 目前包含一个总入口和 17 个专项 Skill：

| 任务 | Skill |
|---|---|
| 不知道先做什么、项目问题混在一起 | `samskill` / `sam-project-diagnosis` |
| 市场、赛道、交易与商业条件 | `sam-business` |
| 产品、价格、交付与变现 | `sam-product` |
| 用户深描、人群图谱与定位 | `sam-position` |
| 对标账号、内容和商业案例 | `sam-benchmark` |
| 参考型改写、洗稿、仿写与独立原创重构 | `sam-reconstruct` |
| 陌生问题与事实研究 | `sam-research` |
| 长期命题、栏目与内容组合 | `sam-strategy` |
| 具体选题 | `sam-topic` |
| 作者表达标准 | `sam-style` |
| 完整创作 | `sam-write` |
| 修改已有稿件 | `sam-edit` |
| 发布前审计 | `sam-audit` |
| 拍摄、剪辑、包装与发布 | `sam-operations` |
| 线索、成交、交付与复购 | `sam-relationship` |
| 发布后数据复盘 | `sam-retro` |
| AI 协作、知识库与数字资产 | `sam-assets` |

## 三分钟开始

不知道用哪个 Skill，直接说：

> 使用 `$samskill` 帮我判断下一步。我正在做【项目】，最近发生【结果】，现在最卡【问题】，已有材料是【】。

新项目可以说：

> 使用 `$sam-project-diagnosis` 诊断这个项目。我未来 30—90 天希望【】，已有【能力／产品／账号／结果】，最近一次动作和结果是【】。

已有具体任务，可以直接使用对应 Skill 的输入卡。

每个 Skill 的 `assets/input-card.md` 都写明：最少提供什么、什么材料会提高准确度、没有材料时怎样降级、最后会得到什么。

18 个 Skill 的完整交付结构见 [18 个 Skill 详细输出框架](docs/08_18个Skill详细输出框架.md)。

## 输入与输出

Samskill 允许用户说得不完整。

它会先使用当前对话和已有材料，只追问会改变判断的问题。

每轮最多问两个主要问题。

输出分三档：

- 快速判断：一屏左右。
- 工作方案：默认完整档，可以执行和验收。
- 专业全景：完整研究、客户方案或内部审计。

用户版结果不会默认展示 YAML、机器状态与内部交接字段。

## 安装

请先阅读 [安装、升级与卸载](docs/02_安装升级与卸载.md)。

建议先预检，再安装：

```bash
python3 scripts/install.py --target ~/.codex/skills --dry-run
python3 scripts/install.py --target ~/.codex/skills
python3 scripts/verify_install.py --target ~/.codex/skills
```

也可以从 GitHub 克隆后安装：

```bash
git clone https://github.com/sanmumuyu07-sudio/samskill.git
cd samskill
python3 scripts/install.py --target ~/.codex/skills --dry-run
python3 scripts/install.py --target ~/.codex/skills
```

安装器不会静默覆盖同名 Skill。

出现冲突时，只有显式加入 `--force` 才会先备份再替换。

也可以手动把 `skills/` 下的 18 个目录复制到 Agent 支持的 Skills 目录。

安装后重启或重新加载 Agent。

## 当前边界

- 不保证流量、成交、收入或平台审核结果。
- 不替用户确认产品、价格、身份、案例真实性与结果承诺。
- 不执行逐句同义替换、标志性表达复制或规避版权检测。
- 不把单条爆款、单次成交或单一相关性当作稳定规律。
- 平台规则、法律、医疗、金融和税务问题需要核对当期官方来源或专业人士。

## 隐私

提交客户聊天、后台截图、合同、付款和未成年人资料前，请先脱敏。

详见 [隐私、安全与权限](docs/04_隐私安全与权限.md)。

## 开源状态

这是公开测试版。

当前已经建立结构校验、输入输出校验、路径和泄漏检查，以及任务触发与质量测试集。

测试集存在不等于所有效果已经通过真实项目证明。

建议先在副本或非关键项目中测试。

当前包收入的是从叁木原子库编译出的运行子集，不是完整原子库本体。

原子库、统一标准和真实样例的完整度见 [原子库与标准完整度审计](docs/09_原子库与标准完整度审计.md)。

`beta.3` 是首个 GitHub 公开测试版。

它继承 `beta.2` 的参考内容双模式，并完成发布净化、品牌边界、反馈入口、GitHub 模板与 CI 校验。

用户口中的“洗稿”不会被统一强制改成从零原创，而是先区分“参考型改写”和“独立原创重构”。前者保留原稿的问题、核心判断、信息重点、功能结构与开头机制；后者建立新问题、新论证与独立贡献。两种模式都受来源、权限、事实真实性和高识别度表达边界约束。

## 反馈与贡献

- 普通问题、建议和可公开复现：提交 [GitHub Issue](https://github.com/sanmumuyu07-sudio/samskill/issues)。
- 安全、隐私、未授权材料或客户信息：不要粘贴原文到公开 Issue，按 [安全说明](SECURITY.md) 提交最小化报告。
- 修改规范见 [贡献指南](CONTRIBUTING.md)。

“Samskill”与“叁木”用于标识本项目及其官方发布。MIT 许可证允许使用代码与文档，但不自动授予官方身份、背书、商标或品牌视觉使用权。详见 [品牌与名称规则](TRADEMARKS.md)。

## 开源包结构

```text
Samskill/
├── skills/       # 一个总入口和 17 个专项 Skill
├── docs/         # 安装、输入输出、权限和任务说明
├── examples/     # 脱敏交付示例
├── scripts/      # 安装、校验、卸载和发布检查
├── tests/        # 输入输出回归清单
├── manifest.json # 版本和安装清单
└── README.md
```

## 验证

```bash
python3 scripts/validate_public_release.py
python3 scripts/validate_skills.py
python3 -m unittest tests/test_release.py -v
```

发布门禁见 [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md)。
