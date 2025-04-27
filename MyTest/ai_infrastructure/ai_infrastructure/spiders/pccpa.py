import configparser
import json
import re
from datetime import datetime
from urllib.parse import urlparse
import scrapy
from items import OutputItem


class PccpaSpider(scrapy.Spider):
    name = "pccpa"

    def __init__(self, config_path='config.ini', *args, **kwargs):
        super(PccpaSpider, self).__init__(*args, **kwargs)
        self.config = configparser.ConfigParser()
        self.config.read(config_path, encoding='utf-8')
        self._load_config()
        self.domain_uri = self.allowed_domains[0]

    def _load_config(self):
        """从配置文件加载参数"""
        id_page = {
            "5": 3,
            "6": 2,
            "7": 4,
            "8": 1,
        }
        # 基础配置
        self.max_depth = self.config.getint(self.name, 'max_depth', fallback=3)

        # 处理多行配置
        start_urls = [
            url.strip() for url in
            self.config.get(self.name, 'start_urls').split('\n')
            if url.strip()
        ][0]
        self.start_urls = []
        for group_id, page_nums in id_page.items():
            for page_num in range(1, page_nums + 1):
                self.start_urls.append(start_urls.format(group_id, page_num))
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
        if depth == 2:
            insight_content = response.css('#js_content ::text').getall()
            text_content = ' '.join([text.strip() for text in insight_content if text.strip()])
            contains_keyword = any(keyword in text_content for keyword in self.keywords)
            self.logger.info(f"当前页面: {response.url}")
            # 如果包含关键词，则保存数据
            if contains_keyword:
                item = OutputItem()
                item['filename'] = self.name
                item['url'] = response.url
                item['depth'] = depth
                item['title'] = response.css('title::text').get()
                item['text_content'] = text_content
                item['links'] = []
                item['timestamp'] = datetime.now().isoformat()
                item['matched_keywords'] = [
                    kw for kw in self.keywords if kw in text_content
                ]
                yield item
            else:
                self.logger.debug(f"跳过不包含关键词的页面: {response.url}")
        else:
            text_content = self._get_links(response)
            # 提取页面中的所有链接（无论是否包含关键词都继续爬取）
            links = list(set(text_content))
            # 无论是否包含关键词，都继续爬取下一层
            for url in links:
                yield scrapy.Request(
                    url,
                    callback=self.parse,
                    cb_kwargs={'depth': depth + 1},
                    errback=self.errback_handler
                )

    def _get_links(self, response):
        self.logger.info(repr(f"get_links{response.text}"))
        res = json.loads(response.text)
        urls = [
            url.get("link") for url in res['data']['data']
            if self._is_valid_html_url(url.get("link"))
        ]
        self.logger.info(repr(f"page_res: {urls}"))
        return urls

    def errback_handler(self, failure):
        """错误处理"""
        self.logger.error(repr(failure))

    def _is_valid_html_url(self, href):
        """验证URL是否有效、属于目标域名"""
        if href.endswith("pdf"):
            return False
        return True
