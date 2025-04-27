# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
from pathlib import Path
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AiInfrastructurePipeline:
    def __init__(self):
        self.output_dir = None

    def process_item(self, item, spider):
        self.output_dir = f'{item["filename"]}_filtered_text_data' if item['filename'] else 'filtered_text_data'
        os.makedirs(self.output_dir, exist_ok=True)
        # 按深度存储
        depth_file = os.path.join(f'{self.output_dir}', f'level_{item["depth"]}.jsonl')
        self._save_to_jsonl(item, depth_file)

        # 额外存储包含多个关键词的页面到单独文件
        if len(item['matched_keywords']) > 1:
            multi_key_file = os.path.join(f'{self.output_dir}', f'multi_keyword.jsonl')
            self._save_to_jsonl(item, multi_key_file)

        return item

    def _save_to_jsonl(self, item, file_path):
        """以JSON Lines格式追加数据"""
        with open(file_path, 'a', encoding='utf-8') as f:
            line = json.dumps(dict(item), ensure_ascii=False)
            f.write(line + '\n')
