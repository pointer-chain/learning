import numpy as np
import timeit


def calculate_levenshtein_distance(t1, t2):
    m, n = len(str(t1)), len(str(t2))
    dp = np.zeros((m + 1, n + 1))

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if t1[i - 1] == t2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[m][n]


def te():
    text_all = {
        "宁夏回族自治区银川市兴庆区上海东路南侧都市阳光13春熙苑4号楼2单元101室(自主申报)": "宁夏回族自治区银川市兴庆区上海东路南侧都市阳光22春熙苑4号楼2单元101室(自主申报)",
        "321321321": "",
        "宁夏回族自治区银川市兴庆区上海东路南侧都市阳光春熙苑4号楼2单元101室(自主申报)": "宁夏回族自治区银川市兴庆区上海东路南侧都市阳光・春熙苑4号楼2单元101室(自主申报)",
        "宁夏回族自治区银川市兴庆区上海东路南侧都市阳光春熙苑号楼2单元101室(自主申报)": "宁夏回族自治区银川市兴庆区上海东路南侧都市阳光・春熙苑4号楼2单元101室(自主申报)",
        "宁夏回族自治区银川市兴庆区上海东路南侧都市阳光春熙苑4号楼单元101室(自主申报)": "宁夏回族自治区银川市兴庆区上海东路南侧都市阳光・春熙苑4号楼2单元101室(自主申报)",
        "宁夏回族自治区银川市兴庆区上海东路南侧都市阳光春熙苑4号楼2单元01室(自主申报)": "宁夏回族自治区银川市兴庆区上海东路南侧都市阳光・春熙苑4号楼2单元101室(自主申报)",
        "宁夏回族自治区银川市兴庆区上海东路南侧都市阳光春熙苑4号楼2单元11室(自主申报)": "宁夏回族自治区银川市兴庆区上海东路南侧都市阳光・春熙苑4号楼2单元101室(自主申报)",
        "宁夏回族自治区银川市兴庆区上海东路南侧都市阳光春熙苑4号楼2单元10室(自主申报)": "宁夏回族自治区银川市兴庆区上海东路南侧都市阳光・春熙苑4号楼2单元101室(自主申报)",
    }
    for t1 in text_all.keys():
        print("{}{}".format(calculate_levenshtein_distance(t1, text_all[t1]),
                            type(calculate_levenshtein_distance(t1, text_all[t1]))))
        # print(calculate_levenshtein_distance(t1, text_all[t1]) < 3)


if __name__ == '__main__':
    # text1 = "宁夏回族自治区银川市"
    # text2 = "宁夏回族自治区・银川市"
    # levenshtein_distance = calculate_levenshtein_distance(text1, text2)
    # print(levenshtein_distance)
    te()
