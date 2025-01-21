def replace_num(num: str, add_str: list = None):
    """
    数据去空格 后缀 处理
    """
    num = str(num)
    if num.endswith(".00"):
        num = num.replace(".00", "")
    replace_list = ["（", "）", "\n", "(", ")", " ", ",", "\t", "<br>", ";", "；", "-"]
    if add_str:
        replace_list = replace_list + add_str
    for x in replace_list:
        num = num.replace(x, "")
    return num
