class Config:
    def __init__(self):
        self.home_url = "https://fastapp-beta.yunzhangfang.com"

    def add_account_url(self):
        """
        新建客户
        :return:
        """
        return self.home_url + "/fast_app/fa/api/v1/livelydata/ark_crm/0G93QRJR364RA/create"

    def add_lead_pool_url(self):
        """
        线索池新建
        :return:
        """
        return self.home_url + "/fast_app/fa/api/v1/livelydata/ark_crm/0HTRZ3B92FTN3/create"

    def get_city(self):
        """
        获取页面城市数据url
        :return:
        """
        return self.home_url + "/fast_app/cbn/api/v1/region/getList/{num}"

    def get_user(self):
        """
        获取页面城市数据url
        :return:
        """
        return self.home_url + "/fast_app/fa/api/v1/livelydata/metabase/mb_user/getList"
