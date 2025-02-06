import re
import pandas as pd


def replace_num(num: str):
    """
    数据去空格 后缀 处理
    """
    num = str(num)
    num = "".join(filter(lambda s: s in '0123456789.', num))
    try:
        num = num[0:11]
    except:
        num = num
    return num


def clean_and_extract_phone(text):
    """
    筛选电话号码
    :param text: 未处理电话号码数据
    :return:
    """
    phone_pattern = re.compile(r"1[3-9]\d{9}|0\d{2,3}-?\d{7,8}")
    if pd.isna(text) or not isinstance(text, str):
        return None
    # 去除特殊字符（如空格、括号、横线等）
    cleaned_text = re.sub(r"[^\d-]", "", text)
    # 匹配电话号码
    match = phone_pattern.search(cleaned_text)
    if match:
        return match.group()
    return None
