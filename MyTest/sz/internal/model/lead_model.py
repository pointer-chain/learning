from sz.internal.model.user_js import user_data

lead_pool_map = {'黑龙江': '669353209296441729',
                 '青新': '669353208633743761',
                 '青岛': '669353208029762039',
                 '陕西': '669353207413502418',
                 '重庆': '669353206708860295',
                 '辽宁': '669353206079716014',
                 '苏州': '669353205463153608',
                 '湖南': '669353204821122882',
                 '湖北': '669353204212948423',
                 '深圳': '669353203608968993',
                 '浙江': '669353202984014466',
                 '河南': '669353200660371127',
                 '河北': '669353200035418637',
                 '江西': '669353199376913630',
                 '服务中心': '669353198714213873',
                 '废弃/测试数据': '669353198093457632',
                 '广西': '669353197489475715',
                 '广州': '669353196885499603',
                 '常州': '669353196247964842',
                 '山西': '669353195648178959',
                 '山东': '669353195044199940',
                 '安徽': '669353194406665618',
                 '天津': '669353193777516619',
                 '外部代账客户': '669353193119013324',
                 '四川': '669353192515031246',
                 '厦门': '669353191781028041',
                 '南京': '669353191156079972',
                 '北京': '669353190552099834',
                 '内蒙': '669353189960702737',
                 '公共公海池': '669353189256058988',
                 }

# 线索池
lead_pool_name = ["上海", "云贵", "公共公海池", "内蒙", "北京", "南京", "厦门", "四川", "外部代账客户", "天津", "安徽",
                  "山东", "山西", "常州", "广州", "广西", "废弃/测试数据", "服务中心", "江西", "河北", "河南", "浙江",
                  "深圳", "湖北", "湖南", "苏州", "辽宁", "重庆", "陕西", "青岛", "青新", "黑龙江"]

household_scale = {'客户暂未透露': 1, '300户以下': 2, '300-500户': 3, '500-800户': 4, '800-2000户': 5, '2000-5000户': 6,
                   '5000户以上': 7}

contact_channel = {'销售自拓': 1, '400来电': 2, '企查查数据': 3, '百度推广（有度）': 4,
                   '历史数据': 5, 'SEM百度搜索': 6, 'SDR数据清洗': 7,
                   '会计工厂': 8, '官方抖音号': 9, '线下市场活动': 10, 'SEO官网注册': 11, 'SEO电脑端商桥': 12,
                   'SEM抖音': 13, '线上市场活动': 14, '微信公众号': 15, '微信私域社群': 16, '财政部数据': 17}

is_accounting_company = {
    "个人版客户": 7,
    "代账公司": 2,
    "是代账公司": 2,
    "企业版客户": 6,
    "加盟意向": 13,
    "待确定": 5,
    "找代理记账公司": 14,
    "无效（无意向/空号）": 4,
    "有代账版需求（非代账公司）": 3
}

follow_up_status = {
'未处理': 1,'已转换': 2,'第一次联系': 3,'第二次联系': 4,'第三次联系': 5,'多次联系': 6
}

status = {
'自建': 1,'未领取': 2,'已领取': 3,'已转换': 4,'已废弃': 5,'已冻结': 6
}

return_reason = {
'电话不存在': 1,'不是代记账公司': 2,'是代账公司': 3, '没有购买需求': 4,'已合作客户': 5,'已经购买其他产品': 6,'价格超过预算': 7,'与分公司重复': 8,'其它': 9,'销售人员离职': 10
}

leads_dict_config = {
    "household_scale": household_scale,
    "contact_channel": contact_channel,
    "is_accounting_company": is_accounting_company,
    "public_sea": lead_pool_map,
    "follow_up_status": follow_up_status,
    "status": status,
    "return_reason": return_reason
}

lead_user_config = {
    "sales_lead_owner": user_data,
    "creator": user_data,
    "latest_modifier": user_data,
}

ac_lead_map_ = {
    'company_name': 'company_name',
    'contact_name': 'user_name',
    'phone': 'ac_other_phone__c',
    'mobile': 'phone',
    'household_scale': 'ac_staff_size__c',
    'lead_create_date': 'create_time',
    'creator': 'creator_id',
    'contact_channel': 'ac_channel__c',
    'is_accounting_company': 'ac_accounting_agency__c',
    'sales_lead_owner': 'owner_id',
    'department': 'org_id',
    'public_sea': 'lead_pool',
    'follow_up_status': 'ac_follow_up_status__c',
    'address': 'address',
    'claim_date': 'ac_collection_time__c',
    'expiration_date': 'ac_due_time__c',
    'status': 'ac_status__c',
    'customer': 'ac_customer__c',
    'latest_modification_date': 'update_time',
    'latest_modifier': 'updater_id',
    'return_reason': 'ac_repossessed_reason__c',
    'return_reason_description': 'ac_repossessed_description__c',
    'lead_number': 'name',
    'communication_attitude': 'ac_communication_attitude__c',
    'remarks': 'description',
    'contact_person': 'contact_id',
    'opportunity': 'opportunity_id',
    'leads_id': 'id'
}
