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