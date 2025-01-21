import json
import requests

from sz.config import api_config
from sz.config import req_config
from sz.internal.model import account_model as ac


class SzApi(object):
    def __init__(self):
        self.config = api_config.Config()
        self.header = req_config.COMMON_HEAD

    def get_city(self, num):
        res = requests.get(self.config.get_city().format(num), headers=self.header)
        return json.loads(res.text)

    def add_lead_pool(self, name):
        self.header.update({"content-type": "application/json;charset=UTF-8"})
        a = {"values": {"name": name, "belong_org": ["1"], "admin_roles": ["0HDTGHKTC2592"], "lead_confirm_limit": 0,
                        "lead_loop_confirm_interval": 0,
                        "lead_first_follow_limit": 0, "lead_record_follow_limit": 0, "lead_to_opportunity_limit": 0,
                        "collection_limit": 0, "opportunity_record_follow_limit": 0,
                        "opportunity_transaction_limit": 0}}
        res = requests.post(self.config.add_lead_pool_url(), data=json.dumps(a), headers=self.header)
        print(res.text)
        return res

    def add_account(self, name):
        data = {
        "values": {
            "ac_accountant_count__c": 321,
            "ac_business_registration__c": 1,
            "ac_company_name_2__c": "公司名称2",
            "ac_competitors__c": "竞争对手",
            "ac_current_accounting_software__c": "现用记账报税软件",
            "ac_customer_needs__c": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7"
            ],
            "ac_is_accounting_company__c": 2,
            "ac_lead_pool__c": "669092244671461644",
            "ac_position__c": 1,
            "ac_total_account_books__c": 123,
            "account_level_id": "6",
            "company_name": "姓名",
            "contact_name": "姓名",
            "customer_type": 2,
            "location": {
                "code": "130303",
                "ids": [
                    "13",
                    "1303",
                    "130303"
                ],
                "names": [
                    "河北省",
                    "秦皇岛市",
                    "山海关区"
                ]
            },
            "org_id": "1",
            "owner_id": "0J0FWTCAKN5PA",
            "phone_number": "13395353356",
        }
    }
        res = requests.post(self.config.add_account_url(), data=json.dumps(data), headers=self.header)
        # TODO 调试
