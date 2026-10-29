# 阶段四：公众号排版与装配流程（Layout Pipeline）

本模块将 Markdown 文章装配为可直接粘贴到微信公众号编辑器的纯 HTML 代码片段，确保样式不丢失、0 平台报警。

---

## 1. 核心流程

### Step 0: 输入与格式归一化
* Markdown 文件/文本直接进入装配。
* Word (.docx)、PDF 或纯文本，先依 `references/format-normalize.md` 进行结构提取与归一化。

### Step 1: 主题选择（默认石墨极简风）
* **默认首选**：`references/theme-graphite-minimal.md`（石墨极简风，最契合极客去 AI 味与白板美学）。
* 备选主题参考 `references/theme-index.md`（摸鱼绿、红白等）。

### Step 2: Markdown 结构解析与组件装配
* **正文关键词下划线（高频核心）**：对每个段落主动挑选 1~2 个最关键的名词/结论，添加该主题的下划线（4~15 字，不用整段划线）。
* **代码块与 Prompt**：使用通用库 1a/1b 紧凑代码块，每一行包装为 `<p style="margin:0">`，**严禁使用 `white-space:pre`**（避免产生大左缩进）。
* **尾部组件 16 装配**：
  - 默认使用 **16a（实战追更型）**。
  - 带资料时使用 **16b（资料交付卡）**。
  - 严禁出现“求三连”旧模板。

### Step 3: 平台合规校验（强制执行）
生成的 HTML 必须通过自动化脚本校验：
```bash
python scripts/validate_gzh_html.py <生成的html文件路径>
```
* **红线检查**：
  - 严禁 `<style>`、`<script>`、`<div>`、`class`、`id`、`@media`、外部 CSS。
  - 所有文本节点必须严格包裹在 `<span leaf="">` 内，否则微信富文本粘贴后样式整片丢失。
  - 正文标点必须全部转换为中文全角符号（弯引号 `“”‘’`，中文逗号句号等）。

### Step 4: 生成一键复制预览页
运行包装脚本生成预览页：
```bash
python scripts/wrap_preview.py <生成的html文件路径>
```
产出 `{原文件名}_预览.html`。用户在浏览器打开后，点击右上角「复制到公众号」按钮，即可完成富文本复制并在公众号后台完美粘贴。
