# 公众号排版组件库 —— 石墨极简

> **使用说明**：本组件库为「石墨极简（Graphite Minimal）」主题（经典编辑风的极简变体），所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：石墨灰 + 纯白 + 几何细线 + 超大留白。克制的现代极简排版，几乎无色块，以 1px 细线与大间距建立秩序感。正文关键词用石墨下划线（`border-bottom:2px solid #52525B;font-weight:600;`）标记，超大水印编号章节、上下细线引言卡、几何签名区的编辑骨架，气质极简克制、留白理性。适合设计、科技评论、专业观点、高端品牌类文章。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id/`<div>`、`position:fixed/absolute/sticky`、`float`、`@media`/`@keyframes`、`display:grid`、CSS 变量 `var(--x)`
> - ✅ 支持内联 `style`、`display:flex`（有限）、`linear-gradient`（可渲染但有暗色模式检测风险，文字背景默认用纯色）、`border-radius`、`box-shadow`、`position:relative`、`<section>/<p>/<span>/<strong>/<img>` 等基础标签
> - font-size ≤ 24px；正文强调用左竖条/石墨下划线/小标签，**不用四周虚线框**（dashed）
>
> **WeChat 兼容铁律**（本主题组件全部已按此写好，改动时必须遵守）：
> - 所有"装饰性空元素"（细线分割线、END 短线、水印编号旁装饰、数据卡分隔、时间线竖线）**必须在内部放 `<span leaf=""><br></span>` 占位**，否则微信会剥掉样式
> - **不要把 `font-size`/`border-bottom` 打在 `<strong>` 上**，也不要在同一个 `<p>` 里混多个不同 `font-size`——微信编辑器会自动"纠正"导致样式被重写。正确做法：拆成多个 `<p>`，每个 `<p>` 只有一个字号；高亮样式统一挂在外层 `<span>` 上
> - 不用 `position:absolute` 做划线/高亮，删除线用 `text-decoration:line-through`
> - 结构化区域（如引言卡右下署名、图片说明、水印编号旁标签）没有内容时**整块删掉**，不留空 section

---

## 设计变量速查表

```
主色（石墨灰）：   #52525B（正文色 / 下划线专用）
标题色（深炭）：   #27272A
深灰强调：         #3F3F46
辅助文字色：       #A1A1AA（署名 / 说明 / 编号小字）
次要文字色：       #71717A
极细线色：         #E4E4E7（分割线 / 边框 / 大号水印编号）
标签底色：         #F4F4F5（关键词标签底）
极浅灰底：         #FAFAFA（引用块 / 目录卡 / 提示块，正文底保持纯白）
纯白底：           #FFFFFF
强调色（暖橙）：   #F97316（全篇 ≤3 处，仅用于锚点点睛）
正文字号：         15px（不可改）
行高：             1.8
字间距：           0.3px
最大宽度：         677px
内容区边距：       0 10px（左右各 10px）
章节间距：         56px（后续章节 margin-top）
```

字体栈：`-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif`

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#FFFFFF;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#52525B;line-height:1.8;letter-spacing:0.3px;overflow-x:hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 开头引言卡片（纯白 + 上下细线 + 大字金句）

> **文案策略（先读，比代码重要）**：
> - 引言卡金句和公众号外标题是**两层**，视角要错开——外标题卖"为什么点开"，引言卡卖"核心观点是什么"
> - 已知外标题时，金句**禁止原样复述**其核心关键词；从文章第一段或核心论点提炼一句有张力的判断句
> - 右下署名按文章实际作者填，未知则整行删掉，**不要固定写"甲木"**
> - 纯白底 + 上下各 1px 石墨极细线框定 + 大号金句，无色块、无阴影、无圆角，完全依靠细线与留白产生质感

```html
<section style="margin:10px 10px 40px;padding:32px 24px 24px;border-top:1px solid #E4E4E7;border-bottom:1px solid #E4E4E7;background:#FFFFFF;">
  <p style="font-size:11px;color:#A1A1AA;letter-spacing:2px;margin:0 0 18px;font-weight:400;">
    <span leaf="">QUOTE</span>
  </p>
  <p style="font-size:18px;font-weight:700;color:#27272A;margin:0 0 8px;line-height:1.7;letter-spacing:0.5px;">
    <span leaf="">{{金句前段}}</span>
    <span style="border-bottom:2px solid #52525B;"><span leaf="">{{石墨下划线关键词}}</span></span>
    <span leaf="">{{金句收尾}}</span>
  </p>
  <p style="text-align:right;font-size:12px;color:#A1A1AA;margin:16px 0 0;letter-spacing:1px;">
    <span leaf="">—— {{作者名，未知则删整行}}</span>
  </p>
</section>
```

> **注意**：金句里默认用石墨下划线（`border-bottom:2px solid #52525B`）标记关键词。若要更强的橙色下划线点睛（`border-bottom:2px solid #F97316`），计入全篇 ≤3 处橙色配额，慎重使用。

---

## 组件 3 前言导读区域（本文看点，三列极简线框目录卡）

> 3 个及以上章节时生成。上方极细线 + 极浅灰底，石墨灰编号 + 深炭标题，纯灰阶无橙色，大留白。展示**精选 3 个核心看点**，不是全量章节列表。

```html
<section style="padding:0 10px 40px;">
  <p style="font-size:11px;color:#A1A1AA;margin:0 0 16px;letter-spacing:2px;">
    <span leaf="">本文看点</span>
  </p>
  <section style="display:flex;justify-content:space-between;">
    <section style="flex:1;background:#FAFAFA;border-top:1px solid #E4E4E7;padding:18px 12px 16px;margin-right:8px;">
      <p style="font-size:11px;color:#A1A1AA;font-weight:500;margin:0 0 8px;letter-spacing:1px;"><span leaf="">01</span></p>
      <p style="font-size:13px;font-weight:700;color:#27272A;margin:0;line-height:1.5;"><span leaf="">{{看点一}}</span></p>
    </section>
    <section style="flex:1;background:#FAFAFA;border-top:1px solid #E4E4E7;padding:18px 12px 16px;margin-right:8px;">
      <p style="font-size:11px;color:#A1A1AA;font-weight:500;margin:0 0 8px;letter-spacing:1px;"><span leaf="">02</span></p>
      <p style="font-size:13px;font-weight:700;color:#27272A;margin:0;line-height:1.5;"><span leaf="">{{看点二}}</span></p>
    </section>
    <section style="flex:1;background:#FAFAFA;border-top:1px solid #E4E4E7;padding:18px 12px 16px;">
      <p style="font-size:11px;color:#A1A1AA;font-weight:500;margin:0 0 8px;letter-spacing:1px;"><span leaf="">03</span></p>
      <p style="font-size:13px;font-weight:700;color:#27272A;margin:0;line-height:1.5;"><span leaf="">{{看点三}}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 4 章节分割线（1px 石墨细线）

> 无渐变、无颜色变化，单纯 1px 横向石墨极细线，两侧超大留白，呼吸感即来自此。

```html
<section style="padding:0 10px;">
  <section style="height:1px;background:#E4E4E7;margin:0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5 章节标题（超大水印编号 + 标题 + 细线）

> 核心特征：极大号石墨灰水印数字（作为背景层视觉锚）+ 英文小标签 + 深炭标题 + 底部 1px 细线。编号大字非常"现代极简"。第一章 `margin-top:16px`，后续章节 `margin-top:56px`。

```html
<section style="margin-top:56px;margin-bottom:32px;padding:0 10px;">
  <section style="position:relative;padding-bottom:20px;border-bottom:1px solid #E4E4E7;">
    <p style="font-size:48px;font-weight:900;color:#E4E4E7;margin:0;line-height:1;letter-spacing:-2px;">
      <span leaf="">01</span>
    </p>
    <section style="margin-top:-8px;">
      <p style="font-size:10px;color:#A1A1AA;font-weight:500;letter-spacing:3px;margin:0 0 6px;text-transform:uppercase;">
        <span leaf="">{{ENGLISH TAG}}</span>
      </p>
      <h3 style="font-size:20px;font-weight:800;color:#27272A;margin:0;letter-spacing:0.5px;line-height:1.4;">
        <span leaf="">{{中文章节标题}}</span>
      </h3>
    </section>
  </section>

  <!-- 本章节正文内容放在这里 -->

</section>
```

**结语章节变体**（编号用 `∞` 替代数字，契合极简的无限循环意象，英文标签用 `THE END` / `EPILOGUE`）：

```html
<p style="font-size:48px;font-weight:900;color:#E4E4E7;margin:0;line-height:1;letter-spacing:-2px;">
  <span leaf="">∞</span>
</p>
```

> **说明**：大号编号字颜色为 `#E4E4E7`（与细线同色），仅作几何形态装饰，不抢正文视觉；深炭标题叠在其下方，层次分明。此处 `position:relative` 在微信公众号被允许（仅 fixed/absolute/sticky 被禁）。

---

## 组件 6 正文段落

> **关键规则**：每段主动识别 1~3 个关键短语，用**石墨下划线（7d）**标记——这是本风格的核心视觉特征，灰阶下划线低调而精准，让读者快速扫到每段重点。

**基础段落**：

```html
<p style="margin-bottom:22px;font-size:15px;line-height:1.8;text-align:justify;color:#52525B;letter-spacing:0.3px;">
  <span leaf="">{{正文内容}}</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认）：

```html
<p style="margin-bottom:22px;font-size:15px;line-height:1.8;text-align:justify;color:#52525B;letter-spacing:0.3px;">
  <span leaf="">{{前半句}}</span>
  <span style="border-bottom:2px solid #52525B;font-weight:600;color:#27272A;"><span leaf="">{{需要强调的关键短语}}</span></span>
  <span leaf="">{{后半句}}</span>
</p>
```

**标记原则**：每段选 1~3 个关键短语（4~15 字）加下划线，不要整段都标；优先标核心观点、结论判断、关键数据、专有名词；无重点的段落可不标。

---

## 组件 6b 子标题（`###` 小节标题）

> `###` 子标题用石墨左竖条 + 深炭标题，**不套用组件 5 的水印编号章节样式**（水印编号只给 `##`）。竖条 3px 石墨灰，贴合极简气质。

```html
<p style="font-size:15px;font-weight:800;color:#27272A;margin:28px 0 14px;padding-left:12px;border-left:3px solid #52525B;line-height:1.4;">
  <span leaf="">{{子标题}}</span>
</p>
```

---

## 组件 7 正文高亮样式（6 种变体 + 使用策略）

> **核心理念**：几乎全灰阶，橙色只在真正关键的锚点出现（全篇 ≤3 处总配额，含引言卡）。
>
> **优先级**：① 7d 石墨下划线（正文默认标记，每段都应考虑）→ ② 7a 普通/深炭加粗为主 → ③ 7b 极浅灰底深炭字标签（每篇 2~4 个）→ ④ 7c 极浅灰背景（次要）→ ⑤ 7e 荧光笔（偶尔长句强调）→ ⑥ 7f 橙色下划线（全篇最强锚点，总计 ≤3 处含引言卡）

### 7a. 加粗强调

普通/深炭加粗（默认，绝大部分加粗用这个）：

```html
<strong style="color:#27272A;"><span leaf="">深炭加粗强调</span></strong>
```

橙色加粗（仅限极少数关键锚点，全篇 ≤3 处总配额）：

```html
<strong style="color:#F97316;"><span leaf="">橙色加粗锚点</span></strong>
```

### 7b. 极浅灰底深炭字标签（核心概念，每篇 2~4 个）

```html
<span style="background:#F4F4F5;color:#27272A;padding:2px 7px;border-radius:3px;font-weight:700;font-size:14px;"><span leaf="">关键词标签</span></span>
```

### 7c. 极浅灰背景高亮（次要关键词）

```html
<span style="background:#F4F4F5;padding:1px 6px;border-radius:2px;font-weight:600;color:#3F3F46;"><span leaf="">浅灰背景关键词</span></span>
```

### 7d. 石墨下划线（最常用，本风格标志性标记）

```html
<span style="border-bottom:2px solid #52525B;font-weight:600;color:#27272A;"><span leaf="">石墨下划线关键词</span></span>
```

### 7e. 荧光笔效果（偶尔用于长句强调，纯色浅灰背景高亮）

```html
<span style="background:#E4E4E7;font-weight:700;color:#27272A;"><span leaf="">荧光笔效果的重要长句</span></span>
```

### 7f. 橙色下划线（点睛锚点，全篇 ≤3 处含引言卡）

```html
<span style="border-bottom:2px solid #F97316;font-weight:700;color:#27272A;"><span leaf="">橙色下划线点睛词</span></span>
```

### 7g. 行内代码

```html
<span style="background:#F4F4F5;color:#27272A;padding:2px 6px;border-radius:4px;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:14px;"><span leaf="">code</span></span>
```

---

## 组件 8 引用高亮块（4 种变体）

### 8a. 石墨竖条金句引用（视觉焦点最强，核心金句）

> 左侧 3px 石墨灰竖条 + 大留白 + 深炭字，无底色，靠竖条与缩进建立层级，呼吸感极强。

```html
<section style="border-left:3px solid #52525B;padding:16px 0 16px 24px;margin:0 10px 28px;">
  <p style="font-size:16px;font-weight:700;color:#27272A;margin:0;line-height:1.7;letter-spacing:0.5px;">
    <span leaf="">「{{核心观点或关键金句}}」</span>
  </p>
</section>
```

### 8b. 极浅灰底内容引用块（Prompt / 引用内容）

> 极浅灰底 + 1px 细线边框，用于展示 Prompt、引用内容、示例等较长内容。

```html
<section style="background:#FAFAFA;border:1px solid #E4E4E7;padding:20px 22px;margin:0 10px 28px;">
  <p style="font-size:11px;color:#A1A1AA;margin:0 0 8px;letter-spacing:2px;font-weight:500;">
    <span leaf="">REFERENCE</span>
  </p>
  <p style="font-size:15px;color:#3F3F46;margin:0;line-height:1.8;text-align:justify;">
    {{引用内容，可含 7d 石墨下划线等内联样式}}
  </p>
</section>
```

### 8c. 辅助色竖条轻量旁注（个人吐槽 / 补充说明）

> 极细辅助灰竖条 + 小号文字，用于轻量旁注、作者旁白，不抢主文视觉。

```html
<section style="border-left:2px solid #E4E4E7;padding:12px 0 12px 20px;margin:0 10px 24px;">
  <p style="font-size:13px;color:#A1A1AA;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">{{轻量旁注内容}}</span>
  </p>
</section>
```

### 8d. 居中金句分隔（章节间的过渡金句）

> 上下 1px 细线 + 居中深炭字，用于章节之间的过渡金句。

```html
<p style="font-size:15px;margin:0 10px 24px;text-align:center;color:#27272A;font-weight:700;letter-spacing:1px;border-top:1px solid #E4E4E7;border-bottom:1px solid #E4E4E7;padding:14px 10px;">
  <span leaf="">{{居中金句}}</span>
</p>
```

---

## 组件 9 提示 / 警示条（3 种变体）

### 9a. 石墨竖条提示条（默认，重要提醒 / 核心结论）

> 石墨竖条 + 深炭文字，无背景色，极简提醒。

```html
<section style="border-left:3px solid #27272A;padding:14px 0 14px 22px;margin:0 10px 24px;">
  <p style="font-size:14px;font-weight:700;color:#27272A;margin:0;line-height:1.8;">
    <span leaf="">{{重要提示或核心结论}}</span>
  </p>
</section>
```

### 9b. 橙色竖条提示条（强调，全篇 ≤3 处配额共享）

> 橙色竖条 + 深炭文字，无背景色，是橙色在正文中最自然的出现方式。

```html
<section style="border-left:3px solid #F97316;padding:14px 0 14px 22px;margin:0 10px 24px;">
  <p style="font-size:14px;font-weight:700;color:#27272A;margin:0;line-height:1.8;">
    <span leaf="">{{最需要引起注意的内容}}</span>
  </p>
</section>
```

### 9c. 踩坑提示（极浅灰底，风险 / 注意事项，内容量大时）

> 极浅灰底 + 顶部深炭细线 + 多行内容，适合提示内容较多时。

```html
<section style="background:#FAFAFA;border-top:2px solid #27272A;padding:18px 22px;margin:0 10px 24px;">
  <p style="font-size:11px;color:#A1A1AA;margin:0 0 10px;letter-spacing:2px;font-weight:500;">
    <span leaf="">NOTE</span>
  </p>
  <p style="font-size:14px;color:#52525B;margin:0;line-height:1.8;">
    <span leaf="">{{较多的提示内容}}</span>
  </p>
</section>
```

---

## 组件 10 内容标签组（STEP / SKILL / TOOL / CASE）

> 教程用 STEP、盘点用 SKILL/TOOL、案例用 CASE。深炭实底编号标签 + 标题，极简克制。

### 10a. step-label（教程步骤）

```html
<section style="margin-bottom:22px;">
  <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
    <span style="display:inline-block;background:#27272A;color:#fff;font-size:11px;font-weight:700;padding:2px 8px;border-radius:3px;letter-spacing:0.5px;"><span leaf="">STEP 01</span></span>
    <span style="font-size:15px;font-weight:800;color:#27272A;"><span leaf="">{{步骤标题}}</span></span>
  </section>
  <p style="font-size:15px;margin:0 0 16px;color:#52525B;line-height:1.8;text-align:justify;">
    {{步骤内容}}
  </p>
</section>
```

`STEP 01` 可替换为 `SKILL 1`、`TOOL 摄像机`、`CASE 01`（盘点/案例场景）；盘点次级层次可把编号标签底色改极浅灰 `#F4F4F5` + 字 `#27272A`。

### 10b. skill/tool-label（盘点编号标签）

```html
<section style="margin-bottom:22px;">
  <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
    <span style="display:inline-block;background:#27272A;color:#fff;font-size:11px;font-weight:700;padding:2px 8px;border-radius:3px;letter-spacing:0.5px;"><span leaf="">SKILL 1</span></span>
    <span style="font-size:15px;font-weight:800;color:#27272A;"><span leaf="">{{名称}}</span></span>
  </section>
</section>
```

`SKILL 1` 可替换为 `TOOL 摄像机` 等。

### 10c. tool-card（工具 / 条目说明卡，极简线框版）

```html
<section style="border:1px solid #E4E4E7;padding:16px 20px;margin:0 10px 24px;">
  <p style="font-size:14px;color:#52525B;margin:0;line-height:1.8;">
    {{条目说明内容}}
  </p>
</section>
```

---

## 组件 11 列表组件

### 11a. ordered-list（石墨圆标数字编号列表）

```html
<section style="margin-bottom:24px;">
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#27272A;color:#fff;font-size:12px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">1</span></span>
    <p style="font-size:15px;color:#52525B;margin:0;line-height:1.8;flex:1;"><span leaf="">{{列表项内容}}</span></p>
  </section>
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#27272A;color:#fff;font-size:12px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">2</span></span>
    <p style="font-size:15px;color:#52525B;margin:0;line-height:1.8;flex:1;"><span leaf="">{{列表项内容}}</span></p>
  </section>
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#27272A;color:#fff;font-size:12px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">3</span></span>
    <p style="font-size:15px;color:#52525B;margin:0;line-height:1.8;flex:1;"><span leaf="">{{列表项内容}}</span></p>
  </section>
</section>
```

### 11b. pill-list（无序要点，石墨圆点前缀 + 说明）

```html
<section style="margin-bottom:14px;">
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;font-size:14px;font-weight:700;color:#27272A;background:#F4F4F5;padding:3px 10px;border-radius:999px;"><span style="display:inline-block;width:6px;height:6px;background:#52525B;border-radius:50%;margin-right:5px;vertical-align:middle;"><span leaf=""><br></span></span><span leaf="">{{要点标题}}</span></span>
  </p>
  <p style="font-size:14px;color:#71717A;margin:0;line-height:1.7;text-align:justify;">
    <span leaf="">{{要点说明}}</span>
  </p>
</section>
```

### 11c. timeline（时间线 / 递进脉络，访谈经历、案例演进）

```html
<section style="display:flex;margin-bottom:24px;">
  <section style="display:flex;flex-direction:column;align-items:center;margin-right:16px;flex-shrink:0;">
    <section style="width:14px;height:14px;border-radius:50%;border:3px solid #52525B;background:#fff;margin-top:4px;"><span leaf=""><br></span></section>
    <section style="width:2px;background:#E4E4E7;flex:1;margin-top:4px;min-height:44px;"><span leaf=""><br></span></section>
  </section>
  <section style="flex:1;padding-bottom:12px;">
    <p style="margin:0 0 6px;font-size:15px;font-weight:800;color:#27272A;"><span leaf="">{{节点标题}}</span></p>
    <p style="font-size:15px;margin:0;color:#52525B;line-height:1.8;text-align:justify;">{{节点内容}}</p>
  </section>
</section>
```

最后一个节点去掉竖线段（删掉内层 `width:2px` 的 section）。

---

## 组件 12 数据 / 要点卡片组

### 两列数据卡（极简线框版）

```html
<section style="display:flex;margin:0 10px 28px;">
  <section style="flex:1;border:1px solid #E4E4E7;padding:22px 16px;margin-right:8px;text-align:center;">
    <p style="font-size:32px;font-weight:900;color:#27272A;margin:0 0 6px;line-height:1;letter-spacing:-1px;"><span leaf="">{{数字}}</span></p>
    <p style="font-size:11px;color:#A1A1AA;margin:0;letter-spacing:1px;"><span leaf="">{{说明}}</span></p>
  </section>
  <section style="flex:1;border:1px solid #E4E4E7;padding:22px 16px;text-align:center;">
    <p style="font-size:32px;font-weight:900;color:#27272A;margin:0 0 6px;line-height:1;letter-spacing:-1px;"><span leaf="">{{数字}}</span></p>
    <p style="font-size:11px;color:#A1A1AA;margin:0;letter-spacing:1px;"><span leaf="">{{说明}}</span></p>
  </section>
</section>
```

### 三列要点卡（顶部细线版）

```html
<section style="display:flex;margin:0 10px 28px;">
  <section style="flex:1;border-top:2px solid #27272A;padding:18px 12px 16px;margin-right:8px;">
    <p style="font-size:11px;color:#A1A1AA;margin:0 0 8px;letter-spacing:1px;font-weight:500;"><span leaf="">01</span></p>
    <p style="font-size:13px;font-weight:700;color:#27272A;margin:0 0 6px;line-height:1.4;"><span leaf="">{{要点标题}}</span></p>
    <p style="font-size:12px;color:#71717A;margin:0;line-height:1.6;"><span leaf="">{{要点说明}}</span></p>
  </section>
  <section style="flex:1;border-top:2px solid #27272A;padding:18px 12px 16px;margin-right:8px;">
    <p style="font-size:11px;color:#A1A1AA;margin:0 0 8px;letter-spacing:1px;font-weight:500;"><span leaf="">02</span></p>
    <p style="font-size:13px;font-weight:700;color:#27272A;margin:0 0 6px;line-height:1.4;"><span leaf="">{{要点标题}}</span></p>
    <p style="font-size:12px;color:#71717A;margin:0;line-height:1.6;"><span leaf="">{{要点说明}}</span></p>
  </section>
  <section style="flex:1;border-top:2px solid #27272A;padding:18px 12px 16px;">
    <p style="font-size:11px;color:#A1A1AA;margin:0 0 8px;letter-spacing:1px;font-weight:500;"><span leaf="">03</span></p>
    <p style="font-size:13px;font-weight:700;color:#27272A;margin:0 0 6px;line-height:1.4;"><span leaf="">{{要点标题}}</span></p>
    <p style="font-size:12px;color:#71717A;margin:0;line-height:1.6;"><span leaf="">{{要点说明}}</span></p>
  </section>
</section>
```

### 表格（真实数据表用）

```html
<section style="margin:0 10px 24px;overflow-x:auto;">
  <table style="width:100%;border-collapse:collapse;font-size:14px;">
    <thead>
      <tr>
        <th style="background:#27272A;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题}}</span></th>
        <th style="background:#27272A;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题}}</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:8px 12px;border-bottom:1px solid #E4E4E7;color:#52525B;"><span leaf="">{{内容}}</span></td>
        <td style="padding:8px 12px;border-bottom:1px solid #E4E4E7;color:#52525B;"><span leaf="">{{内容}}</span></td>
      </tr>
      <tr>
        <td style="padding:8px 12px;border-bottom:1px solid #E4E4E7;color:#52525B;background:#FAFAFA;"><span leaf="">{{内容}}</span></td>
        <td style="padding:8px 12px;border-bottom:1px solid #E4E4E7;color:#52525B;background:#FAFAFA;"><span leaf="">{{内容}}</span></td>
      </tr>
    </tbody>
  </table>
</section>
```

---

## 组件 13 标签胶囊

石墨描边（默认）：

```html
<span style="display:inline-block;border:1px solid #A1A1AA;color:#52525B;font-size:11px;font-weight:500;padding:2px 10px;border-radius:2px;margin-right:6px;letter-spacing:0.5px;"><span leaf="">标签名</span></span>
```

深炭实底（强调标签）：

```html
<span style="display:inline-block;background:#27272A;color:#FFFFFF;font-size:11px;font-weight:600;padding:2px 10px;border-radius:2px;margin-right:6px;letter-spacing:0.5px;"><span leaf="">标签名</span></span>
```

橙色描边（点睛标签，全篇 ≤3 处配额共享）：

```html
<span style="display:inline-block;border:1px solid #F97316;color:#F97316;font-size:11px;font-weight:600;padding:2px 10px;border-radius:2px;margin-right:6px;letter-spacing:0.5px;"><span leaf="">核心标签</span></span>
```

---

## 组件 14 图片容器

> 极简线框图片容器，无圆角、无阴影，1px 细线边框延续几何极简语言。

```html
<section style="border:1px solid #E4E4E7;padding:4px;margin:0 10px 12px;">
  <section style="margin:0;overflow:hidden;">
    <span leaf=""><img src="{{图片URL}}" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
  </section>
</section>
```

带说明文字时，图片容器 `margin-bottom` 改 `8px`，其后加：

```html
<p style="font-size:12px;color:#A1A1AA;text-align:center;margin:0 10px 28px;letter-spacing:0.5px;">
  <span leaf="">— {{图片说明}}</span>
</p>
```

GIF 动图角标改极简描边胶囊：边框与字色用石墨主色 `#52525B`、背景透明。多行代码块用通用增量库 `common-components.md` 的 1a 深色 / 1b 浅色（左竖条换 `#52525B`），禁 `white-space:pre`。

---

## 组件 15 END 结尾分割线

> 纯几何，1px 细线 + 居中 "END" 字样，石墨灰，简洁收尾。

```html
<section style="padding:0 10px;">
  <section style="text-align:center;margin:0 0 36px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:1px;width:48px;background:#E4E4E7;margin-right:16px;"><span leaf=""><br></span></span>
      <span style="font-size:10px;color:#A1A1AA;letter-spacing:4px;font-weight:500;"><span leaf="">END</span></span>
      <span style="height:1px;width:48px;background:#E4E4E7;margin-left:16px;"><span leaf=""><br></span></span>
    </section>
  </section>
</section>
```

---

## 组件 16 尾部转化与作者签名区（高粉留存闭环）

> 彻底淘汰“求点赞转发三连”的低效套话，改为高转化闭环组件。根据文章是否有配套资料，二选一使用：

### 16a. 白板微动图 + 官方原生名片（默认推荐·零加戏标准）

> 彻底杜绝冗长自白与自我感动。上方为纯白留白手绘微动图（呼应作者头像）+ 单句功能性交代，下方紧接微信官方原生 `<mp-common-profile>` 关注名片。

```html
<section style="padding:0 10px 24px;">

  <!-- 1. 白板手绘微动图（GIF·零自嗨） -->
  <section style="text-align:center;margin:24px auto 14px;">
    <span leaf=""><img src="{{动图CDN地址，如微信官方CDN墨镜猫GIF}}" alt="{{作者名}}" style="max-width:240px;height:auto;display:block;margin:0 auto;"></span>
    <p style="font-size:13px;color:#71717A;margin:8px 0 0;letter-spacing:0.3px;">
      <span leaf="">规则包后台发「{{暗号关键词}}」自取。明晚复盘出海落地页实测。</span>
    </p>
  </section>

  <!-- 2. 微信官方原生公众号名片组件 -->
  <section style="margin:16px 0 6px;">
    <mp-common-profile class="js_uneditable custom_select_card mp_profile_iframe" data-pluginname="mpprofile" data-nickname="AIGC小曾" data-from="0" data-headimg="http://mmbiz.qpic.cn/mmbiz_png/Wzmje8vCQA3hapvocJ9kJ8TTcQiakbDOpqhFAS6kxWGeVkpaewDLia3icXIWmc1FWCgZyE0QSTuol9CWHTicW8XICbXarFVlouggqGictOBasNN8/0?wx_fmt=png" data-signature="每月实打实扣 API 账单的独立开发者，只记录真实跑通的商业模式与踩坑血泪" data-id="MzI0OTUwNTAwNw==" data-is_biz_ban="0" data-service_type="1" contenteditable="false"></mp-common-profile>
  </section>

</section>
```

### 16b. 干货资料 / 自查清单交付型（高粉转化型）

> 极简线框卡片呈现资料名 + 明确关注路径闭环（避免读者在评论区留1造成粉丝流失）。

```html
<section style="padding:0 10px 24px;">
  <section style="border:1px solid #E4E4E7;background:#FAFAFA;padding:20px 18px;margin-bottom:24px;">
    <p style="font-size:11px;color:#A1A1AA;letter-spacing:2px;margin:0 0 8px;font-weight:600;">
      <span leaf="">RESOURCE / 资料清单</span>
    </p>
    <p style="font-size:16px;font-weight:700;color:#27272A;margin:0 0 10px;line-height:1.5;">
      <span leaf="">{{资料名，如：OpenAI Pro 额度抵扣避坑清单与自查表.xlsx}}</span>
    </p>
    <p style="font-size:14px;color:#52525B;margin:0 0 14px;line-height:1.7;">
      <span leaf="">涵盖文中梳理的全部约束条件、10 条避坑自查项与权限核验核对单，已整理为在线文档。</span>
    </p>
    <section style="padding:10px 14px;background:#FFFFFF;border:1px solid #E4E4E7;display:inline-block;border-radius:4px;">
      <p style="font-size:13px;color:#27272A;margin:0;font-weight:600;line-height:1.6;">
        <span leaf="">获取方式：关注公众号，在后台对话框发送「{{关键词，如：1}}」直接获取</span>
      </p>
    </section>
  </section>
  <section style="border-top:1px solid #E4E4E7;padding-top:20px;">
    <p style="margin-bottom:0;font-size:14px;line-height:1.8;color:#71717A;text-align:justify;">
      <span leaf="">我是 {{作者名}}，每月实打实扣 API 账单的独立开发者。点击上方蓝字关注，下周带你拆解真实跑通的商业模式。</span>
    </p>
  </section>
</section>
```

### 16c. 极客终端暗色兑换卡（个性化科技感最强·高转化）

> macOS 终端暗色窗体 + 命令行提示符 + 资源卡 + 虚线代码指令胶囊，视觉冲击力极强。

```html
<section style="border:1px solid #27272A;border-radius:8px;background:#18181B;overflow:hidden;box-shadow:0 8px 24px rgba(0,0,0,0.06);margin:0 10px 24px;">
  <!-- 终端标题栏 -->
  <section style="background:#27272A;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #3F3F46;">
    <section style="display:flex;align-items:center;gap:6px;">
      <span style="width:10px;height:10px;border-radius:50%;background:#71717A;display:inline-block;"><span leaf=""><br></span></span>
      <span style="width:10px;height:10px;border-radius:50%;background:#52525B;display:inline-block;"><span leaf=""><br></span></span>
      <span style="width:10px;height:10px;border-radius:50%;background:#3F3F46;display:inline-block;"><span leaf=""><br></span></span>
    </section>
    <span style="font-family:'SF Mono',Consolas,Monaco,monospace;font-size:11px;color:#A1A1AA;letter-spacing:1px;"><span leaf="">{{脚本名，如：get-rules.sh}}</span></span>
    <span style="display:inline-block;background:#3F3F46;color:#E4E4E7;font-size:10px;padding:2px 6px;border-radius:3px;font-family:monospace;"><span leaf="">UTF-8</span></span>
  </section>

  <!-- 终端内页 -->
  <section style="padding:20px 16px 18px;">
    <p style="font-family:'SF Mono',Consolas,Monaco,monospace;font-size:12px;color:#10B981;margin:0 0 10px;letter-spacing:0.5px;">
      <span leaf="">➜  ~ /aigc-xiaozeng $ cat PACKAGE_INFO.md</span>
    </p>

    <!-- 资源卡片框 -->
    <section style="background:#27272A;border:1px solid #3F3F46;border-radius:6px;padding:16px 14px;margin-bottom:14px;">
      <p style="font-size:15px;font-weight:700;color:#FFFFFF;margin:0 0 8px;line-height:1.4;">
        <span leaf="">📦 {{资料包标题}}</span>
      </p>
      <p style="font-size:13px;color:#A1A1AA;margin:0;line-height:1.6;">
        <span leaf="">{{资料简短介绍，如：规则表 + 公式 + 配置文件}}</span>
      </p>
    </section>

    <!-- 指令兑换胶囊 -->
    <section style="background:#09090B;border:1px dashed #52525B;border-radius:6px;padding:12px 14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;">
      <section style="display:flex;align-items:center;gap:6px;">
        <span style="font-size:12px;color:#71717A;"><span leaf="">执行指令：</span></span>
        <span style="font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;color:#F4F4F5;font-weight:600;"><span leaf="">后台发送暗号「{{关键词}}」</span></span>
      </section>
      <span style="background:#FFFFFF;color:#18181B;font-size:11px;font-weight:700;padding:4px 10px;border-radius:4px;letter-spacing:0.5px;"><span leaf="">直接获取 ZIP</span></span>
    </section>

    <p style="font-size:11px;color:#71717A;margin:12px 0 0;text-align:center;">
      <span leaf="">* 点击上方蓝字关注公众号后，在会话窗口回复触发自动下发</span>
    </p>
  </section>
</section>
```

### 16d. 个性化创作者手记名片卡 (Creator Profile Card)

> 圆形徽章头像 + 认证身份胶囊 + 下期实测悬念框 + 一键关注指引。

```html
<section style="margin:0 10px 24px;border-top:1px solid #E4E4E7;padding-top:24px;">
  <section style="display:flex;align-items:flex-start;gap:12px;margin-bottom:16px;">
    <section style="width:42px;height:42px;border-radius:50%;background:#27272A;display:flex;align-items:center;justify-content:center;color:#FFFFFF;font-weight:800;font-size:16px;flex-shrink:0;">
      <span leaf="">{{姓氏或首字，如：曾}}</span>
    </section>
    <section style="flex:1;">
      <section style="display:flex;align-items:center;gap:8px;margin-bottom:4px;flex-wrap:wrap;">
        <span style="font-size:15px;font-weight:800;color:#27272A;"><span leaf="">{{作者名，如：AIGC小曾}}</span></span>
        <span style="font-size:11px;background:#F4F4F5;color:#52525B;padding:1px 6px;border-radius:3px;font-weight:500;"><span leaf="">{{身份认证标签，如：独立开发者 / 扣 API 账单实战派}}</span></span>
      </section>
      <p style="font-size:13px;color:#71717A;margin:0;line-height:1.6;">
        <span leaf="">{{一句话宣言，如：不发通稿吹泡沫，只记录真实跑通的商业模式与踩坑血泪。}}</span>
      </p>
    </section>
  </section>

  <!-- 下期悬念与关注引导 -->
  <section style="background:#FAFAFA;border:1px solid #E4E4E7;border-radius:6px;padding:16px 16px 14px;">
    <p style="font-size:13px;color:#52525B;margin:0 0 12px;line-height:1.7;">
      <span leaf="">{{下期悬念预告正文}}</span>
    </p>
    <section style="display:flex;align-items:center;justify-content:space-between;border-top:1px dashed #E4E4E7;padding-top:10px;">
      <span style="font-size:12px;color:#71717A;"><span leaf="">如果你也在折腾出海或独立开发：</span></span>
      <strong style="color:#27272A;font-size:13px;"><span leaf="">点击顶部「关注」，一起少交点学费 ➔</span></strong>
    </section>
  </section>
</section>
```

### 16e. 微信原生高保真公众号关注名片卡 (Official Account Card)

> 1:1 还原微信官方内置名片视窗：左侧 48px 圆形头像 + 加粗公众号名称 + 认证简介，右侧标志性微信官方绿底「+ 关注」按钮。

```html
<section style="margin:20px 0 6px;background:#FFFFFF;border:1px solid #E5E5E5;border-radius:8px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 2px 8px rgba(0,0,0,0.02);">
  <section style="display:flex;align-items:center;gap:12px;flex:1;min-width:0;">
    <section style="width:46px;height:46px;border-radius:50%;background:#27272A;display:flex;align-items:center;justify-content:center;color:#FFFFFF;font-weight:700;font-size:17px;flex-shrink:0;">
      <span leaf="">{{头像单字或图片}}</span>
    </section>
    <section style="flex:1;min-width:0;padding-right:10px;">
      <section style="display:flex;align-items:center;gap:6px;margin-bottom:3px;">
        <span style="font-size:15px;font-weight:700;color:#000000;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;"><span leaf="">{{公众号名称，如：AIGC小曾}}</span></span>
      </section>
      <p style="font-size:12px;color:#888888;margin:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;line-height:1.4;">
        <span leaf="">{{功能介绍，如：每月实打实扣 API 账单的独立开发者}}</span>
      </p>
    </section>
  </section>
  <section style="flex-shrink:0;">
    <section style="background:#07C160;color:#FFFFFF;font-size:13px;font-weight:500;padding:6px 14px;border-radius:4px;display:inline-block;text-align:center;">
      <span leaf="">+ 关注</span>
    </section>
  </section>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background:#FFFFFF;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#52525B;line-height:1.8;letter-spacing:0.3px;overflow-x:hidden;">

  <!-- 1. 开头引言卡片（组件2，纯白 + 上下细线 + 大字金句） -->

  <!-- 2. 前言正文（组件6 段落 × N，放 0 10px 边距 section，第一章之前的开场白） -->

  <!-- 3. 前言导读（组件3，3+ 章节时生成，精选 3 看点） -->

  <!-- 4. 第一章（组件5 章节标题，margin-top:16px） -->
  <!--    章内：组件6 正文 + 6b 子标题 + 7 行内高亮 + 8 引用 + 9 提示 + 10 标签组 + 11 列表 + 12 数据 + 14 图片 -->

  <!-- 5. 章节分割线（组件4）+ 第二章…第N章（组件5，margin-top:56px） -->

  <!-- 6. 结语章（组件5 变体：编号 ∞，英文 THE END） -->

  <!-- 7. END 分割线（组件15） -->

  <!-- 8. 尾部签名（组件16） -->

</section>
```

**骨架铁律**：引言卡在最前；导读区在前言正文之后、第一章之前；章节之间用组件 4 石墨细线分隔；一篇只有一个 END + 一个签名区。这是经典编辑向的极简骨架——开头引言/封面 → 前言 → 编号章节 → 结语 → 签名。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 橙色下划线 7f / 橙色竖条 9b / 橙色加粗 7a（`#F97316`） | 全文最关键锚点 | 全篇 ≤3 处（含引言卡） |
| **标记层** | 石墨下划线 7d（默认）+ 字重 600 / 极浅灰底标签 7b | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | 石墨竖条引用 8x / 提示 9x / 标签组 10 / 卡片 11-12 | 引用、旁注、提示、结构化信息 | 按需 |

**克制原则**：
- 橙色（`#F97316`）全篇 ≤3 处，所有橙色使用共享此配额（引言卡橙下划线、正文橙竖条、橙标签各算一处）
- 石墨下划线是默认正文标记，高频使用
- 极浅灰底（`#FAFAFA`）仅在目录卡、引用块、提示块内使用，正文底色保持纯白
- 数据卡片用线框而非色块，完全贴合极简调性
- 章节编号是超大水印灰字，装饰性而非功能性；引用/提示统一用左竖条 + 大留白，**不用四周虚线框**（dashed）

---

## 文章类型 → 组件组合配方

按 SKILL.md 第 3 步判定的文章类型选配方；核心组件构成本篇排版主旋律，点缀组件按内容出现处使用，一篇文章点缀组件种类 ≤3，避免花哨。

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 观点/深度分析 | 正文6 + 石墨竖条金句8a + 居中金句8d | 极浅灰引用8b、辅助竖条旁注8c |
| 教程/操作指南 | step-label 10a + 代码块（通用库1a）+ ordered-list 11a | 石墨提示9a、tool-card 10c |
| 盘点/工具清单 | skill/tool-label 10b + tool-card 10c + pill-list 11b | 数据卡12、标签胶囊13 |
| 访谈/人物特稿 | 正文6 + 石墨竖条金句8a（引语）+ timeline 11c（经历脉络） | 居中金句8d、辅助竖条旁注8c |
| 数据复盘/报告 | 数据卡12（两列/三列）+ 表格12 + ordered-list 11a | 石墨提示9a、荧光笔7e |
| 生活/情感随笔 | 正文6 + 居中金句8d + 辅助竖条旁注8c | 石墨竖条金句8a（少量） |
| 案例实战 | case-label 10a / timeline 11c + step-label 10a | 极浅灰引用8b、踩坑提示9c |

所有类型共用固定结构：引言卡 2 + 导读 3（3+ 章节）+ 水印编号章节 5 + END 15 + 签名 16。

---

## Markdown → 石墨极简排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| 文章开头 `> 引言金句` | 组件 2 纯白上下细线引言卡 | 视角与外标题错开 |
| `## 章节标题` | 组件 5 超大水印编号 + 标题 | 自动编号 01/02…，末章 ∞ + THE END |
| `### 子标题` | 组件 6b 石墨左竖条小标题 | 不套水印编号章节样式 |
| 普通段落 | 组件 6 正文段落 | 每段主动标 1~3 处石墨下划线 7d |
| `**加粗文字**` | 组件 7a 深炭加粗（默认）/ 橙色加粗（锚点 ≤3） | 深炭加粗为主 |
| `==高亮文字==` | 组件 7b 极浅灰底深炭字标签 | 核心概念 |
| `<u>下划线</u>` / `++文字++` | 组件 7d 石墨下划线 | `2px #52525B` |
| `~~删除线~~` | `text-decoration:line-through` + 辅助灰字 | 被淘汰概念 |
| 行内 `` `code` `` | 组件 7g 行内代码 | |
| `> 引用段落`（金句） | 组件 8a 石墨竖条金句 | 核心金句，无底色 |
| `> 引用段落`（内容块） | 组件 8b 极浅灰底引用块 | 有 REFERENCE 标签行 |
| `> 引用段落`（旁注） | 组件 8c 辅助色竖条轻量旁注 | 极细辅助灰竖条 |
| 核心金句 | 组件 8a / 8d 居中金句 | 视觉焦点 |
| 操作步骤 | 组件 10a step-label | STEP 01/02… |
| 技能/工具清单 | 组件 10b skill/tool-label + 10c tool-card | |
| 案例/经历脉络 | 组件 10a case-label / 11c timeline | |
| Prompt 提示词 | 组件 8b 极浅灰引用块 / 通用库 1a（长多行） | |
| ` ``` 多行代码块 ``` ` | 通用库 1a 深色 / 1b 浅色（左竖条换 #52525B） | 每行一个 `<p style="margin:0">` |
| 并列要点 | 组件 11b pill-list | |
| `1. 2. 3.` 编号列表 | 组件 11a ordered-list | 石墨圆标 |
| 数据展示 | 组件 12 数据/要点卡片组 | 线框版，深炭大号数字 |
| Markdown 表格 | 组件 12 表格 | 偶数行极浅灰底 |
| 注意/警告 | 组件 9a 石墨提示 / 9b 橙色提示 / 9c 踩坑提示 | |
| 行内标签 | 组件 13 标签胶囊 | 石墨描边默认 |
| `---` | 组件 4 章节分割线 | 1px 石墨极细线 |
| `![](图片)` | 组件 14 图片容器 | 极简线框，无圆角 |
| 文末 | 组件 15 END + 16 签名 | END线 + 签名 |
</content>
</invoke>
