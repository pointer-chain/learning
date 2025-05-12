import re

def validate_id_card(id_card: str) -> bool:
    """
    校验身份证号是否合法
    :param id_card: 身份证号
    :return: True（合法） / False（不合法）
    """
    # 校验长度和格式
    if not re.match(r"^\d{17}[\dXx]$", id_card):
        return False

    # 校验出生日期
    birth_date = id_card[6:14]
    try:
        year = int(birth_date[:4])
        month = int(birth_date[4:6])
        day = int(birth_date[6:8])
        # 简单校验日期是否合理
        if year < 1900 or month < 1 or month > 12 or day < 1 or day > 31:
            return False
    except ValueError:
        return False

    # 校验码校验
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    total = sum(int(id_card[i]) * weights[i] for i in range(17))
    remainder = total % 11
    if id_card[-1].upper() != check_codes[remainder]:
        return False
    return True
