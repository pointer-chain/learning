import math

import xlwt
import xlrd
import pandas as pd
from sz.internal.model.account_model import ac_account_map_
from sz.internal.model.account_model import DICT_CONFIG
from sz.internal.model.account_model import city_id
from sz.utils.time_stamp import return_strftime


class CustomerXlrd(object):
    def __init__(self, create_table, read_table, sheet_name, csv_name):
        """
        :param create_table: 创建的表名
        :param read_table: 读取的表名
        """
        self.read_table_name = read_table
        self.create_table_name = create_table
        self.sheet_name = sheet_name
        self.csv_name = csv_name
        # 创建写入表
        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet(self.sheet_name)
        self.row = 0
        self.col = 0

    def save_table(self):
        self.wb.save(self.create_table_name)
        pass

    def read_excel(self):
        pass

    def numpy_excel_ac_account(self):
        data = pd.read_excel(self.read_table_name)
        # 修改表头
        for x in data.keys():
            if x in ac_account_map_:
                self.ws.write(self.row, self.col, ac_account_map_.get(x))
                self.col += 1
        self.col = 0
        self.row += 1
        for x in data.keys():
            if x in ac_account_map_:
                datas = data.get(x)
                for da in datas:
                    value = da
                    try:
                        if math.isnan(value):
                            self.row += 1
                            continue
                    except:
                        ...
                    if x in DICT_CONFIG:
                        value = DICT_CONFIG.get(x).get(da)
                    if "date" in x or "time" in x:
                        value = return_strftime(da)
                    if x == "detailed_address":
                        value = {"name": da, "search_key": f"{da},"}
                        value = str(value).replace("'", '"')
                    print(f"正在处理第【{self.row}】行, 第【{self.col}】数据")
                    self.ws.write(self.row, self.col, value)
                    self.row += 1
                self.col += 1
                self.row = 1
        province = data.get("province")
        city = data.get("city")
        district = data.get("district")
        self.ws.write(0, self.col, "city_id")
        for index_city in range(len(province)):
            city1 = city_id.get(province[index_city], {}).get("id", {})
            city2 = city_id.get(province[index_city], {}).get("city", {}).get(city[index_city], {}).get("id", {})
            city3 = city_id.get(province[index_city], {}).get("city", {}).get(city[index_city], {}).get("city", {}).get(district[index_city], {})
            ids = [x for x in [city1, city2, city3] if x]
            names_list = [province[index_city], city[index_city], district[index_city]]
            names = []
            for x in names_list:
                try:
                    if math.isnan(x):
                        continue
                except:
                    ...
                names.append(x)
            if not ids:
                self.row += 1
                continue
            res = {
                "ids": ids,
                "code": ids[-1],
                "names": names,
                "search_key": "".join(names),
            }
            print(f"正在处理第【{self.row}】行, 第【{self.col}】数据")
            self.ws.write(self.row, self.col, str(res).replace("'", '"'))
            self.row += 1
        self.save_table()

    def excel_to_csv(self):
        # 读取Excel文件
        excel_data = pd.read_excel(self.create_table_name)
        # 将数据保存为CSV文件
        excel_data.to_csv(self.csv_name, index=False)

    def numpy_excel_ac_contact(self):
        pass
