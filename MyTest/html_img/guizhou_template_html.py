import datetime
import time

from jinja2 import Template
import os
from guizhou_json import res
from decimal import Decimal
from urllib.parse import urlencode
from urllib.parse import quote


def number_to_chinese(num):
    # 定义数字对应的中文
    chinese_num = {'0': '零', '1': '壹', '2': '贰', '3': '叁', '4': '肆',
                   '5': '伍', '6': '陆', '7': '柒', '8': '捌', '9': '玖'}
    # 定义单位
    units = ['元', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿']
    # 定义小数单位
    decimal_units = ['角', '分']

    # 分离整数和小数部分
    integer_part, decimal_part = str(num).split('.')

    # 处理整数部分
    chinese_integer = ''
    for i, char in enumerate(integer_part[::-1]):
        chinese_integer = chinese_num[char] + units[i] + chinese_integer

    # 处理小数部分
    chinese_decimal = ''
    for i, char in enumerate(decimal_part):
        chinese_decimal += chinese_num[char] + decimal_units[i]

    # 合并整数和小数部分
    return chinese_integer + chinese_decimal
nsrsbh = "91520390MADKAAKN6P"
nsrmc = "贵州遵义博依亿市场服务有限公司"
gdslxDm = "1"
dyrq = str(datetime.datetime.today())[:10]
with open("guizhou_wspz.html", "r", encoding="utf-8") as f:
    template = Template(f.read())
rows = res.get("body").get("jkcxsj")
if rows:
    jgmc = rows[0].get("swjgmc")
    yhzh = rows[0].get("yhzh")
    je = []
    for row in rows:
        je.append(row.get("sjje"))
    jexx = sum([Decimal(i) for i in je])
    jedx = number_to_chinese(jexx)
    rendered_html = template.render(nsrsbh=nsrsbh, nsrmc=nsrmc, gdslxDm=gdslxDm, dyrq=dyrq, jgmc=jgmc, yhzh=yhzh,
                                    jexx=jexx, jedx=jedx, rows=rows)
    print(rendered_html)
    print(quote(rendered_html))
    with open('guizhou_wspz_test.html', 'w', encoding='utf-8') as file:
        file.write(rendered_html)
