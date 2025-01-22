from sz.internal.model.lead_model import lead_pool_name
from sz.internal.routers.api.routers import SzApi

if __name__ == '__main__':
    # 新建线索池配置
    sz = SzApi()
    for lead in lead_pool_name:
        sz.add_lead_pool(lead)
