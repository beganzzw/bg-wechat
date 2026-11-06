# bg-wechat：微信公众号写作、排版与主题管理

为科技内容提供真实材料整理、大纲确认、写作与编辑、HTML 装配、主题管理和复制预览。安装本仓库即可使用核心流程，不需要同目录下的其他技能，也不需要发布账号或生图服务。

## 三个明确分支

| 分支 | 行为 | 边界 |
| --- | --- | --- |
| `write` | 选题、事实台账、大纲、新稿、按要求编辑与检查 | 新稿确认大纲；已有确认直接继续；已有稿不自动重写 |
| `layout` | Markdown、Docx、PDF、纯文本归一化并装配正文 HTML 与复制预览 | 保留原文、代码、图片和来源；不要求写作大纲，不自动加标题方案、签名或文末承诺 |
| `theme` | 查看包内基础方案，配置颜色、字号和间距；明确选择外部主题时才加载可选依赖 | 配置→整页预览→检查→保存项目参数；不触发文章创作 |

新稿默认附痛点提问、底层机制、实操利差、短促断言四类标题。非虚构规则始终有效：不编造经历、测试、引语、参考资料、后续计划或可领取资源。已授权事项和已有确认可复用。白板图是可选视觉风格，不是所有作者的强制偏好。

## 安装与环境

需要 Python 3.10 或更新版本。所附脚本只使用 Python 标准库。将仓库克隆到所用 Agent 的技能目录，例如：

```bash
git clone https://github.com/beganzzw/bg-wechat.git ~/.workbuddy-ai/skills/bg-wechat
```

让 Agent 读取根目录 `SKILL.md`。不需要运行未随包提供的初始化脚本。这里的排版和主题生成由 Agent 按参考文件装配，仓库没有声称提供自动 Markdown 渲染 CLI。

示例请求：

- `/bg-wechat write 根据这些真实材料先整理事实和大纲。`
- `/bg-wechat layout 把 article.md 按包内基础方案排版，保留原稿，直接处理。`
- `/bg-wechat theme 列出主题。`
- `/bg-wechat theme 按白底、深灰正文、蓝色强调生成自定义主题。`

Markdown 和纯文本的核心写作、排版可独立使用。Docx/PDF 提取依赖当前 Agent 环境的文档工具，本包不附带提取器；工具不可用时使用已提取文本。合并单元格与复杂结构须对照原件复核。图片参考需要当前环境图像查看能力。基础主题预览不需要联网生图。

## 包内路径与组件来源

`BG_ROOT` 是根 `SKILL.md` 所在目录。默认仅使用包内 `references/themes-and-components.md` 的 `basic` 基础方案，自定义参数保存在当前项目。

**gzh-design 是可选依赖，不随包分发。** 仅明确选择外部主题时，将用户提供或已确认配置的独立安装绝对路径记为 `GZH_ROOT`，按 `references/layout-pipeline.md` 核验主题索引、所选文件与脚本。默认不查找兄弟技能、不自动安装；缺少依赖只阻塞所选外部主题，可选择继续使用基础方案。write、基础 layout 和基础 theme 配置均不需要 GZH_ROOT。

每次锁定一种来源并使用对应脚本，外部主题的数量和能力以实际安装版本为准。本包不附带六套外部主题，也不将基础方案冒充外部主题。

以下命令在仓库根运行；其他工作目录请将脚本路径和输入路径换成实际绝对路径。测试不调用发布或生图接口。

```bash
python scripts/check_prose.py tests/fixtures/prose.txt
python scripts/component_lint.py .
python scripts/validate_gzh_html.py tests/fixtures/valid.html
python scripts/wrap_preview.py tests/fixtures/valid.html
python -m unittest discover -s tests -v
```

反例 `tests/fixtures/invalid.html` 的校验退出码应为 1；渐变样例 `gradient.html` 应产生 WARNING、退出码 0。警告需逐项复核，不等于检查完全通过。独立回归仅复制 `release-files.txt` 白名单中的文件，不带外部依赖或私有记录。

脚本只证明已编码检查的结果。HTML 校验不证明完整语法、所有英文文本包装、微信粘贴后的显示、事实、版权或平台审核通过。`check_prose.py` 提供风格提示，不鉴定作者身份或文章是否由 AI 生成；专业术语、引用和用户要求优先，不能为清零破坏原意。预览只用于本地检查，复制按钮和原生名片在不同浏览器、微信客户端仍需实际验证。

## 作者记忆与隐私

`references/author-memory.md` 是用户自填模板。将其复制为 `references/author-memory.local.md` 后记录已确认规则；本机文件不进入版本控制。未填写时执行通用规则，不默认任何账号身份。

完整稿件、修改反馈和复盘存用户指定位置，缺省为工作区 `content-system/`。记录自动验证、AI 评估、人工确认、未验证四种依据；没有发布数据不推断传播效果。分发前检查文件清单，`.gitignore` 不能替代隐私审查。

## 可选草稿同步

`scripts/publish.py` 直接调用微信公众号接口，仅新增或更新草稿，不正式发布，不依赖 `bg-unified-publisher`。只有用户授权后才运行。

配置环境变量 `WECHAT_OA_APPID` 和 `WECHAT_OA_SECRET`（兼容 `WECHAT_OA_APPSECRET`），并提供 `--cover` 本地封面或环境变量 `WECHAT_OA_COVER_MEDIA_ID`。凭据不写文件、不写源码；缺少配置或图片时在网络请求前失败。正文 ERROR/WARNING 必须先处理。作者默认留空，可用 `--author` 指定。

```bash
python scripts/publish.py article.html --title "文章标题" --author "作者署名" --cover cover.png
python scripts/publish.py article.html --title "文章标题" --update "用户提供的草稿标识"
```

更新默认处理该草稿中的第一个图文项。同步成功不代表正式发布；预览地址可能为空，以接口实际结果为准。失败时不自动切换凭据或接口重试。本准备版的测试全部离线，未验证真实账号接口。

## 来源、许可与分发范围

根 [LICENSE](LICENSE) 保留远程 main 基线 `f1f5bd89e4bed90d5f7cc8a683853c8439d222d3` 的 MIT 原文与完整版权。基线已含的脚本及预览模板继续保留原有许可状态，本次不对其来源或许可作重新定性；已有安全修正保留。基础主题参数与示例为本次独立编写。

可选 gzh-design-skill 的官方来源为 https://github.com/isjiamu/gzh-design-skill ，由甲木 (Jiamu) × 摸鱼小李 (Moyu Xiaoli) 创作，其独立安装的许可随该依赖保留。未将该依赖的源码、主题、提取器或许可文件纳入本次发行包，也未把其许可改为 MIT。

发行文件严格逐项列于 `release-files.txt`，只从白名单构建干净发行目录后打包，不递归打包准备工作树。临时 `vendor/`、`LICENSE.original*`、`License.original*`、`THIRD*`、本机作者记录和市场元数据由 `.gitignore` 排除且不在白名单；本地临时文件可以保留。新增发布文件需先审查并显式加入白名单。公开作者模板保留，私有记录不发布。

本准备版保留写作、排版、预览与离线校验流程，未执行提交、推送或全局技能更新。
