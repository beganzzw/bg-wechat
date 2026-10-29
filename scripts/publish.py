#!/usr/bin/env python3
"""bg-unified-publisher 集成发布脚本。

支持将生成的公众号 HTML 直接推送到微信公众号草稿箱（自动上传本地配图与封面至微信 CDN 并替换路径），
并可扩展推送到小红书等平台。

用法:
    python scripts/publish.py <html文件路径> --title "文章标题" [--digest "摘要"] [--cover <封面路径>] [--update <media_id>]
"""

import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

# 默认凭据从环境变量或内置安全存储获取
DEFAULT_APPID = os.environ.get("WECHAT_OA_APPID", "wx6ad9de0a2bdfcb42")
DEFAULT_SECRET = os.environ.get("WECHAT_OA_SECRET", os.environ.get("WECHAT_OA_APPSECRET", "2c913d57c3d3ad4e610402514e2e4f05"))
DEFAULT_COVER_MEDIA_ID = "8Ore6s5-I7xpG5-S_hHgpaGvn1OGDxmYrq1AG6U3GwvFGTmpCNyo8Y9LUDMj5SQt"


def get_access_token(appid, secret):
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    if "access_token" not in data:
        raise RuntimeError(f"获取微信 Token 失败: {data}")
    return data["access_token"]


def upload_image_to_cdn(token, image_path):
    """上传本地图片到微信 CDN (仅返回 URL，不占用素材库容量)"""
    url = f"https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={token}"
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    filename = os.path.basename(image_path)
    content_type = "image/gif" if filename.lower().endswith(".gif") else "image/jpeg" if filename.lower().endswith((".jpg", ".jpeg")) else "image/png"

    with open(image_path, "rb") as f:
        file_bytes = f.read()

    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="media"; filename="{filename}"\r\n'
        f"Content-Type: {content_type}\r\n\r\n"
    ).encode("utf-8") + file_bytes + f"\r\n--{boundary}--\r\n".encode("utf-8")

    req = urllib.request.Request(url, data=body, headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    if "url" not in res:
        raise RuntimeError(f"上传图片到微信 CDN 失败: {res}")
    return res["url"]


def upload_cover_material(token, cover_path):
    """上传永久图文封面到素材库，返回 thumb_media_id"""
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=image"
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    filename = os.path.basename(cover_path)
    content_type = "image/jpeg" if filename.lower().endswith((".jpg", ".jpeg")) else "image/png"

    with open(cover_path, "rb") as f:
        file_bytes = f.read()

    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="media"; filename="{filename}"\r\n'
        f"Content-Type: {content_type}\r\n\r\n"
    ).encode("utf-8") + file_bytes + f"\r\n--{boundary}--\r\n".encode("utf-8")

    req = urllib.request.Request(url, data=body, headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    if "media_id" not in res:
        raise RuntimeError(f"上传封面素材失败: {res}")
    return res["media_id"]


def replace_local_images(content_html, token, base_dir):
    """检测 HTML 中的本地图片并自动上传至微信 CDN 替换"""
    img_pattern = re.compile(r'<img\s+[^>]*src=["\']([^"\']+)["\']', re.I)
    matches = img_pattern.findall(content_html)
    uploaded = {}
    for src in matches:
        if src.startswith("http://") or src.startswith("https://") or src.startswith("data:"):
            continue
        # 本地文件路径解析
        local_path = os.path.join(base_dir, src) if not os.path.isabs(src) else src
        if os.path.exists(local_path) and local_path not in uploaded:
            print(f"  正在自动上传本地配图至微信 CDN: {os.path.basename(local_path)}...")
            cdn_url = upload_image_to_cdn(token, local_path)
            uploaded[src] = cdn_url

    for src, cdn_url in uploaded.items():
        content_html = content_html.replace(f'src="{src}"', f'src="{cdn_url}"')
        content_html = content_html.replace(f"src='{src}'", f"src='{cdn_url}'")
    return content_html


def publish_to_wechat(html_path, title=None, author="AIGC小曾", digest=None, cover_path=None, update_media_id=None, appid=DEFAULT_APPID, secret=DEFAULT_SECRET):
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    base_dir = os.path.dirname(os.path.abspath(html_path))
    token = get_access_token(appid, secret)

    # 1. 自动处理正文中出现的本地图片
    html = replace_local_images(html, token, base_dir)

    # 2. 处理封面
    if cover_path and os.path.exists(cover_path):
        print(f"  正在上传自定义封面: {os.path.basename(cover_path)}...")
        thumb_media_id = upload_cover_material(token, cover_path)
    else:
        thumb_media_id = DEFAULT_COVER_MEDIA_ID

    # 3. 提取或兜底标题和摘要
    if not title:
        m = re.search(r"<h[1-3][^>]*>(.*?)</h[1-3]>", html, re.I | re.S)
        title = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else "未命名文章"

    if not digest:
        # 提取第一段正文作为摘要
        m = re.search(r"<p[^>]*>(.*?)</p>", html, re.I | re.S)
        digest = re.sub(r"<[^>]+>", "", m.group(1)).strip()[:100] if m else title

    article = {
        "title": title,
        "author": author,
        "digest": digest,
        "content": html,
        "content_source_url": "",
        "thumb_media_id": thumb_media_id,
        "need_open_comment": 1,
        "only_fans_can_comment": 0
    }

    if update_media_id:
        url = f"https://api.weixin.qq.com/cgi-bin/draft/update?access_token={token}"
        payload = {"media_id": update_media_id, "index": 0, "articles": article}
        print(f"  正在更新既有草稿箱文章 (media_id: {update_media_id})...")
    else:
        url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
        payload = {"articles": [article]}
        print("  正在创建全新草稿箱文章...")

    req = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))

    if update_media_id:
        if res.get("errcode", 0) != 0:
            raise RuntimeError(f"更新草稿失败: {res}")
        media_id = update_media_id
    else:
        media_id = res.get("media_id")
        if not media_id:
            raise RuntimeError(f"创建草稿失败: {res}")

    # 获取临时预览链接
    get_url = f"https://api.weixin.qq.com/cgi-bin/draft/get?access_token={token}"
    req_get = urllib.request.Request(get_url, data=json.dumps({"media_id": media_id}).encode("utf-8"), headers={"Content-Type": "application/json"})
    preview_url = ""
    try:
        with urllib.request.urlopen(req_get) as resp_get:
            res_get = json.loads(resp_get.read().decode("utf-8"))
            preview_url = res_get.get("news_item", [{}])[0].get("url", "")
    except Exception:
        pass

    return {
        "success": True,
        "media_id": media_id,
        "preview_url": preview_url,
        "title": title
    }


def main():
    parser = argparse.ArgumentParser(description="bg-unified-publisher 微信公众号集成发布工具")
    parser.add_argument("html", help="HTML 文件路径")
    parser.add_argument("--title", help="文章标题")
    parser.add_argument("--author", default="AIGC小曾", help="文章作者")
    parser.add_argument("--digest", help="文章摘要")
    parser.add_argument("--cover", help="本地封面图片路径")
    parser.add_argument("--update", help="更新已有的 draft media_id")
    args = parser.parse_args()

    if not os.path.exists(args.html):
        print(f"错误: 找不到文件 {args.html}")
        sys.exit(1)

    print(f"🚀 开始执行发布流水线: {args.html}")
    try:
        res = publish_to_wechat(
            html_path=args.html,
            title=args.title,
            author=args.author,
            digest=args.digest,
            cover_path=args.cover,
            update_media_id=args.update
        )
        print("✅ 成功同步至微信公众号草稿箱！")
        print(f"  • Media ID: {res['media_id']}")
        if res["preview_url"]:
            print(f"  • 微信真机预览链接: {res['preview_url']}")
    except Exception as e:
        print(f"❌ 发布失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
