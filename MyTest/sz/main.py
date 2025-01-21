from sz.internal.model.lead_model import lead_pool_name
from sz.internal.routers.api.routers import SzApi
from sz.utils.excel_temp import CustomerXlrd


if __name__ == '__main__':
    excel = CustomerXlrd("./customer_com.xlsx", "./customer.xlsx", "Result 1")
    excel.numpy_excel_ac_account()
    # 新建线索池配置
    # sz = SzApi()
    # for lead in lead_pool_name:
    #     sz.add_lead_pool(lead)
