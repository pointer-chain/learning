import configparser
import re
from datetime import datetime
from urllib.parse import urlparse
import scrapy
from items import OutputItem


class DahuaSpider(scrapy.Spider):
    name = "dahua"

    def __init__(self, config_path='config.ini', *args, **kwargs):
        super(DahuaSpider, self).__init__(*args, **kwargs)
        self.config = configparser.ConfigParser()
        self.config.read(config_path, encoding='utf-8')
        self._load_config()
        self.domain_uri = self.allowed_domains[0]

    def _load_config(self):
        """从配置文件加载参数"""
        # 基础配置
        self.max_depth = self.config.getint(self.name, 'max_depth', fallback=3)

        # 处理多行配置
        self.start_urls = [
            url.strip() for url in
            self.config.get(self.name, 'start_urls').split('\n')
            if url.strip()
        ]

        # 处理逗号分隔的域名
        self.allowed_domains = [
            domain.strip() for domain in
            self.config.get(self.name, 'allowed_domains').split(',')
            if domain.strip()
        ]

        # 关键词配置
        self.keywords = [
            kw.strip() for kw in
            self.config.get(self.name, 'keywords', fallback='').split(',')
            if kw.strip()
        ]
        self.logger.info(f"加载配置完成 - 爬虫名称: {self.name}")
        self.logger.info(f"起始URL: {self.start_urls}")
        self.logger.info(f"允许域名: {self.allowed_domains}")
        self.logger.info(f"最大深度: {self.max_depth}")
        self.logger.info(f"关键词: {self.keywords}")

    def parse(self, response: object, depth=1):
        """
        :param depth:
        :type response: object
        """
        if depth > self.max_depth:
            return

        # 获取完全清理后的文本内容
        text_content = self._get_clean_text(response)

        # 检查是否包含中文字符
        has_chinese = self._contains_chinese(text_content)

        # 如果不包含中文，记录并返回（不再爬取该页面的链接）
        if not has_chinese:
            self.logger.info(f"跳过无中文内容页面: {response.url}")
            return
        # 检查是否包含任何关键词
        contains_keyword = any(keyword in text_content for keyword in self.keywords)

        # 提取页面中的所有链接（无论是否包含关键词都继续爬取）
        links = list(set(
            response.urljoin(href)
            for href in response.css('#content a::attr(href)').extract()
            if self._is_valid_html_url(href)
        ))
        self.logger.info(f"当前页面: {response.url}, 获取到的链接: {links}")

        # 如果包含关键词，则保存数据
        if contains_keyword:
            item = OutputItem()
            item['filename'] = self.name
            item['url'] = response.url
            item['depth'] = depth
            item['title'] = response.css('title::text').get()
            item['text_content'] = text_content
            item['links'] = links
            item['timestamp'] = datetime.now().isoformat()
            item['matched_keywords'] = [
                kw for kw in self.keywords if kw in text_content
            ]
            yield item
        else:
            self.logger.debug(f"跳过不包含关键词的页面: {response.url}")

        # 无论是否包含关键词，都继续爬取下一层
        for url in links:
            yield scrapy.Request(
                url,
                callback=self.parse,
                cb_kwargs={'depth': depth + 1},
                errback=self.errback_handler
            )

    def errback_handler(self, failure):
        """错误处理"""
        self.logger.error(repr(failure))

    def _contains_chinese(self, text):
        """更精确的中文检测，排除标点符号"""
        return bool(re.search('[\u4e00-\u9fa5]{2,}', text))  # 至少两个连续中文字符

    def _is_valid_html_url(self, href):
        """验证URL是否有效、属于目标域名"""
        if not href or href.startswith(('mailto:', 'javascript:', 'tel:')):
            return False
        if "dahua-insight" not in href and "professional-viewpoint" not in href:
            return False
        parsed = urlparse(href)
        return (not parsed.netloc or parsed.netloc.endswith(self.domain_uri))

    def _get_clean_text(self, response):
        """获取完全清理后的文本内容"""
        # 移除script和style标签及其内容
        cleaned = re.sub(r'<(script|style).*?>.*?</\1>', '', response.text, flags=re.DOTALL | re.IGNORECASE)
        # 移除所有HTML标签
        cleaned = re.sub(r'<[^>]+>', ' ', cleaned)
        # 移除HTML实体
        cleaned = re.sub(r'&[a-z0-9]+;', ' ', cleaned, flags=re.IGNORECASE)
        # 移除多余的空白字符
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        # 移除常见的JS代码片段
        cleaned = re.sub(r'(?i)function\s*\([^)]*\)\s*\{[^}]*\}', ' ', cleaned)
        cleaned = re.sub(r'(?i)var\s+\w+\s*=\s*[^;]+;', ' ', cleaned)
        # 移除CSS规则
        cleaned = re.sub(r'(?i)\.[a-z0-9_-]+\s*{[^}]*}', ' ', cleaned)
        cleaned = re.sub(r'(?i)#[a-z0-9_-]+\s*{[^}]*}', ' ', cleaned)
        # 再次移除多余空白
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        return cleaned

    def _clean_text(self, text):
        """清理简单文本"""
        if not text:
            return ''
        return re.sub(r'\s+', ' ', text).strip()
