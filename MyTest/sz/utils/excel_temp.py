import xlwt
import pandas as pd
from sz.internal.model.account_model import ac_account_map_
from sz.internal.model.account_model import DICT_CONFIG
from sz.utils.excel_data import return_city
from sz.utils.excel_data import return_address
from sz.utils.excel_data import judge_nan
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
                    if judge_nan(value):
                        self.row += 1
                        continue
                    if x in DICT_CONFIG:
                        if isinstance(da, list):
                            value = [DICT_CONFIG.get(x).get(da_ele) for da_ele in da]
                            value = str(value).replace("'", '"')
                        else:
                            value = DICT_CONFIG.get(x).get(da)
                    if "date" in x or "time" in x:
                        value = return_strftime(da)
                    if x == "detailed_address":
                        value = return_address(da)
                    print(f"正在处理第【{self.row}】行, 第【{self.col}】数据")
                    self.ws.write(self.row, self.col, value)
                    self.row += 1
                self.col += 1
                self.row = 1
        self.ws.write(0, self.col, "city_id")
        province = data.get("province")
        city = data.get("city")
        district = data.get("district")
        for index_city in range(len(province)):
            res = return_city(province, city, district, index_city)
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
