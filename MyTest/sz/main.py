import json

from sz.internal.model.lead_model import lead_pool_name
from sz.internal.routers.api.routers import SzApi
from sz.utils.excel_temp import CustomerXlrd
from sz.utils.sql_operate import SqlOperate

if __name__ == '__main__':
    # excel操作
    # excel = CustomerXlrd(create_table="./customer_com.xlsx", read_table="./customer.xlsx",
    #                      sheet_name="Result 1", csv_name="example.csv")
    # excel.numpy_excel_ac_account()
    # excel.excel_to_csv()
    # 新建线索池配置
    # sz = SzApi()
    # for lead in lead_pool_name:
    #     sz.add_lead_pool(lead)
    # 数据库操作
    cur = SqlOperate()
    # 初始化链接
    cur.init_cursor()
    # 确定循环初始值
    count_sql = """SELECT COUNT(*) FROM shuzhou_move.activity_records;"""
    count_res = cur.select_sql(count_sql)
    range_index = count_res[0][0] // 500 + 1
    for ran in range(0, range_index):
        search_sql = f"""SELECT t.* FROM shuzhou_move.activity_records t LIMIT {500*ran},{500}"""
        sql_datas = cur.select_sql(search_sql)
        for sql_data in sql_datas:
            source = json.loads(sql_data[5])
            if source.get("activityRecordFrom") in [1, 11, 3]:
                print(sql_data)
    cur.close_cursor()
