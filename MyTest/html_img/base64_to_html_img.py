import os
import base64
import re
from pathlib import Path


def convert_images_to_base64(html_path, static_dir="static", output_path="output.html"):
    """
    将HTML文件中的本地图片转换为Base64编码
    参数：
        html_path: HTML文件路径
        static_dir: 静态文件目录（相对于HTML文件所在目录）
        output_path: 输出文件路径
    """
    # 获取HTML文件所在目录
    html_dir = os.path.dirname(os.path.abspath(html_path))

    # 读取HTML内容
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # 处理CSS中的url
    html_content = convert_css_urls_to_base64(html_content, html_dir, static_dir)

    # 匹配所有img标签的正则表达式
    img_pattern = re.compile(r'<img[^>]+src="([^">]+)"[^>]*>', re.IGNORECASE)

    # 查找所有图片路径
    img_matches = img_pattern.findall(html_content)

    # 遍历所有匹配的图片路径
    for img_rel_path in set(img_matches):  # 使用set去重
        # 处理相对路径
        if img_rel_path.startswith(('http://', 'https://')):
            print(f"跳过网络图片: {img_rel_path}")
            continue

        # 构建完整图片路径
        img_full_path = os.path.normpath(os.path.join(html_dir, static_dir, img_rel_path))

        # 检查文件是否存在
        if not os.path.exists(img_full_path):
            print(f"警告：图片文件不存在，跳过处理 {img_full_path}")
            continue

        # 获取文件扩展名
        file_ext = Path(img_full_path).suffix.lower().lstrip('.')

        # 确定MIME类型
        mime_types = {
            'png': 'image/png',
            'jpg': 'image/jpeg',
            'jpeg': 'image/jpeg',
            'gif': 'image/gif',
            'webp': 'image/webp'
        }
        mime_type = mime_types.get(file_ext, 'application/octet-stream')

        # 读取图片并转换为Base64
        try:
            with open(img_full_path, 'rb') as img_file:
                img_data = img_file.read()
                base64_data = base64.b64encode(img_data).decode('utf-8')
                data_uri = f"data:{mime_type};base64,{base64_data}"

                # 替换HTML中的图片路径
                html_content = html_content.replace(
                    f'src="{img_rel_path}"',
                    f'src="{data_uri}"'
                )
        except Exception as e:
            print(f"处理图片 {img_rel_path} 时出错: {str(e)}")
            continue

    # 保存处理后的HTML
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"转换完成，已保存到 {output_path}")


def convert_css_urls_to_base64(html_content, html_dir, static_dir="static"):
    """
    转换CSS中的url引用为base64
    参数：
        html_content: HTML内容
        html_dir: HTML文件所在目录
        static_dir: 静态文件目录
    """
    # 匹配CSS中的url引用（支持单引号、双引号和无引号）
    url_pattern = re.compile(
        r"url\(['\"]?(.*?)['\"]?\)",
        re.IGNORECASE
    )

    # 查找所有url引用
    urls = set(url_pattern.findall(html_content))  # 去重处理

    for url_path in urls:
        # 跳过网络资源和data URI
        if url_path.startswith(('http://', 'https://', 'data:')):
            continue

        # 构建完整图片路径
        img_full_path = os.path.normpath(
            os.path.join(html_dir, static_dir, url_path)
        )

        # 检查文件是否存在
        if not os.path.exists(img_full_path):
            print(f"警告：文件不存在 {img_full_path}")
            continue

        # 处理文件
        try:
            with open(img_full_path, 'rb') as f:
                file_ext = Path(img_full_path).suffix.lower().lstrip('.')
                mime_type = {
                    'png': 'image/png',
                    'jpg': 'image/jpeg',
                    'jpeg': 'image/jpeg',
                    'gif': 'image/gif',
                    'webp': 'image/webp'
                }.get(file_ext, 'application/octet-stream')

                base64_str = base64.b64encode(f.read()).decode('utf-8')
                data_uri = f"data:{mime_type};base64,{base64_str}"

                # 替换所有匹配的url路径（考虑引号情况）
                html_content = re.sub(
                    r'url\([\'"]?{}[\'"]?\)'.format(re.escape(url_path)),
                    f"url('{data_uri}')",
                    html_content
                )
        except Exception as e:
            print(f"处理文件 {url_path} 出错: {str(e)}")

    return html_content
# 使用示例
if __name__ == "__main__":
    # 参数说明：
    # 第一个参数：原始HTML文件路径
    # static_dir：静态文件目录（相对于HTML文件的位置）
    # output_path：输出文件路径
    convert_images_to_base64(
        "neimenggu_nvwa.html",
        static_dir="",  # 根据实际情况调整
        output_path="neimenggu_homepage.html"
    )
