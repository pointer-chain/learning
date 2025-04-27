# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OutputItem(scrapy.Item):
    filename = scrapy.Field()
    url = scrapy.Field()
    depth = scrapy.Field()
    title = scrapy.Field()
    text_content = scrapy.Field()
    links = scrapy.Field()
    timestamp = scrapy.Field()
    matched_keywords = scrapy.Field()  # 新增字段，记录匹配的关键词
