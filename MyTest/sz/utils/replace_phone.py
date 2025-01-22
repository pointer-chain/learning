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
