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

    def get_user(self):
        user_dict = {}
        count_len = 0
        self.header.update({"content-type": "application/json;charset=UTF-8"})
        result = []
        for lens in range(1, 10):
            data = {"pageSize": 1000, "pageNum": lens, "sort": "id+",
                    "query": "", "filter": {},
                    "quickSearch": {"query": "", "columns": ["id", "nick_name", "name"]},
                    "options": {"fetchButton": True, "viewId": "0H1MRKG5W5Z8Y"}}
            res = requests.post(self.config.get_user(), data=json.dumps(data), headers=self.header)
            res = json.loads(res.text)
            if not res:
                break
            result += res.get("result").get("data")
        list_del_all = []
        for x in result:
            list_del_all.append(x.get('name', {}))
        list_del = []
        for x in list_del_all:
            if list_del_all.count(x) > 1:
                list_del.append(x)
        for x in result:
            count_len += 1
            if x not in list_del:
                user_dict[x.get('name', {})] = x.get('id', {})
        print(user_dict)
        # print(count_len)
        # print(user_dict)


if __name__ == '__main__':
    sz = SzApi()
    sz.get_user()
