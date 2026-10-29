# 主题与核心组件库 (Themes & Components)

本模块定义微信公众号排版主题体系与标准组件 HTML 代码。

---

## 1. 主题选择矩阵

| 主题名称 | 核心色调 | 适用场景 | 下划线 CSS |
| :--- | :--- | :--- | :--- |
| **石墨极简风（默认推荐）** | `#52525B` 灰阶 | 科技评论、架构拆解、去AI味首选 | `border-bottom:2px solid #52525B;font-weight:600;` |
| **摸鱼绿** | `#059669` 翠绿 | 保姆级教程、环境配置、工具清单 | `border-bottom:2px solid #A7F3D0;font-weight:600;` |
| **红白色系** | `#DC2626` 正红 | 犀利观点、行业批判、重磅事件 | `border-bottom:2px solid #FECACA;font-weight:600;` |
| **橄榄手记** | `#1e1f23` 墨黑/橙 | 踩坑复盘手记、工程实战沉淀 | `border-bottom:2px solid #ed7b2f;font-weight:600;` |
| **摸鱼票据风** | `#059669` 翠绿 | 多模型横评、跑分对决、打分PK | `border-bottom:2px solid #A7F3D0;font-weight:600;` |
| **留白禅意风** | `#4A5D52` 灰绿 | 独立思考、慢随笔、高呼吸感 | `border-bottom:1.5px solid #B5C8BC;font-weight:500;` |

---

## 2. 核心组件代码速查（以石墨极简风为例）

### 全局外壳容器
```html
<section style="max-width:677px;margin:0 auto;background:#FFFFFF;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#52525B;line-height:1.8;letter-spacing:0.3px;overflow-x:hidden;">
  <!-- 内容 -->
</section>
```

### 组件 1：开头引言卡片
```html
<section style="margin:10px 10px 36px;padding:28px 22px 22px;border-top:1px solid #E4E4E7;border-bottom:1px solid #E4E4E7;background:#FFFFFF;">
  <p style="font-size:11px;color:#A1A1AA;letter-spacing:2px;margin:0 0 16px;font-weight:500;"><span leaf="">QUOTE</span></p>
  <p style="font-size:17px;font-weight:700;color:#27272A;margin:0;line-height:1.7;letter-spacing:0.5px;">
    <span leaf="">{{引言金句，核心词配下划线}}</span>
  </p>
</section>
```

### 组件 2：章节大标题
```html
<section style="margin-top:36px;margin-bottom:28px;padding:0 10px;">
  <section style="padding-bottom:16px;border-bottom:1px solid #E4E4E7;">
    <p style="font-size:42px;font-weight:900;color:#E4E4E7;margin:0;line-height:1;letter-spacing:-2px;"><span leaf="">01</span></p>
    <section style="margin-top:-6px;">
      <p style="font-size:10px;color:#A1A1AA;font-weight:500;letter-spacing:3px;margin:0 0 4px;text-transform:uppercase;"><span leaf="">BREAKTHROUGH</span></p>
      <h3 style="font-size:19px;font-weight:800;color:#27272A;margin:0;letter-spacing:0.5px;line-height:1.4;"><span leaf="">{{章节标题}}</span></h3>
    </section>
  </section>
</section>
```

### 组件 3：正文段落与关键词下划线
```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;color:#52525B;">
  <span leaf="">正文普通文字……</span><span style="border-bottom:2px solid #52525B;font-weight:600;color:#27272A;"><span leaf="">核心关键词下划线</span></span><span leaf="">，继续正文内容。</span>
</p>
```

### 组件 4：左竖条金句引用
```html
<section style="border-left:3px solid #52525B;padding:14px 0 14px 20px;margin:0 10px 32px;">
  <p style="font-size:15px;font-weight:700;color:#27272A;margin:0;line-height:1.7;">
    <span leaf="">「{{核心观点金句}}」</span>
  </p>
</section>
```

### 组件 5：紧凑代码块（禁 white-space:pre）
```html
<section style="background:#27272A;border-radius:6px;padding:14px 16px;margin:0 10px 24px;overflow-x:auto;">
  <p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#E4E4E7;">
    <span leaf="">curl -X POST https://api.example.com</span>
  </p>
</section>
```

### 组件 6：END 结尾分割线
```html
<section style="padding:0 10px;margin-top:36px;">
  <section style="text-align:center;margin:0 0 32px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:1px;width:48px;background:#E4E4E7;margin-right:16px;"><span leaf=""><br></span></span>
      <span style="font-size:10px;color:#A1A1AA;letter-spacing:4px;font-weight:500;"><span leaf="">END</span></span>
      <span style="height:1px;width:48px;background:#E4E4E7;margin-left:16px;"><span leaf=""><br></span></span>
    </section>
  </section>
</section>
```

### 组件 7：尾部转化区（16a 动图 + 官方原生名片·默认标准）
```html
<section style="padding:0 10px 24px;">
  <!-- 白板微动图（零自嗨） -->
  <section style="text-align:center;margin:24px auto 14px;">
    <span leaf=""><img src="http://mmbiz.qpic.cn/sz_mmbiz_gif/Wzmje8vCQA1vGuoxiaBic9VibBdKSJmF2fUakClic5MVwS93uq9GU2iaic4uPbY0z0VWQwMMdVxGMHibU0rphJprC60wpBnwB2ZsygY4icxUE4Apib4w/0?from=appmsg" alt="AIGC小曾" style="max-width:240px;height:auto;display:block;margin:0 auto;"></span>
    <p style="font-size:13px;color:#71717A;margin:8px 0 0;letter-spacing:0.3px;">
      <span leaf="">规则包后台发「{{暗号}}」自取。明晚复盘出海实测。</span>
    </p>
  </section>

  <!-- 微信官方原生名片标签 -->
  <section style="margin:16px 0 6px;">
    <mp-common-profile class="js_uneditable custom_select_card mp_profile_iframe" data-pluginname="mpprofile" data-nickname="AIGC小曾" data-from="0" data-headimg="http://mmbiz.qpic.cn/mmbiz_png/Wzmje8vCQA3hapvocJ9kJ8TTcQiakbDOpqhFAS6kxWGeVkpaewDLia3icXIWmc1FWCgZyE0QSTuol9CWHTicW8XICbXarFVlouggqGictOBasNN8/0?wx_fmt=png" data-signature="每月实打实扣 API 账单的独立开发者，只记录真实跑通的商业模式与踩坑血泪" data-id="MzI0OTUwNTAwNw==" data-is_biz_ban="0" data-service_type="1" contenteditable="false"></mp-common-profile>
  </section>
</section>
```
