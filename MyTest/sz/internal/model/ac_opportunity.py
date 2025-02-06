from sz.internal.model.user_js import user_data

opportunity_type = {"新客户机会": 1, "老客户续费": 2}

loss_reason = {"价格原因": 1, "质量原因": 2, "客户关系原因": 3, "其他": 4}

lead_source = {"销售自拓": 1, "400来电": 2, "企查查数据": 3, "百度推广（有度）": 4, "历史数据": 5, "SEM百度搜索": 6,
               "SDR数据清洗": 7, "会计工厂": 8, "官方抖音号": 9, "线下市场活动": 10, "SEO官网注册": 11,
               "SEO电脑端商桥": 12, "SEM抖音": 13, "线上市场活动": 14, "微信公众号": 15, "微信私域社群": 16,
               "财政部数据": 17, }

product_opportunity_type = {"代账系统": 1, "云开票": 2, "云微互联": 3, "易云簿": 4, "数字生态平台": 5, "代账Mini": 6,
                            "代账托管": 7, "其他": 8, }

sales_stage = {'初步接洽(找到关键人）': 62339839,'已面谈': 1282882909,'需求诊断': 628568445,'确认需求': 775369234,
'商务谈判及报价': 666317092,'推进打款中': 1941385754,'赢单': 473382624,'输单': 1802973884}

loss_stage = {'初步接洽(找到关键人）': 1,'已面谈': 2,'需求诊断': 3,'确认需求': 4,
'商务谈判及报价': 5,'推进打款中': 6,'赢单': 7}

opportunity_dict_config = {
    "opportunity_type": opportunity_type,
    "loss_reason": loss_reason,
    "lead_source": lead_source,
    "product_opportunity_type": product_opportunity_type,
    "sales_stage": sales_stage,
    "loss_stage": loss_stage,
}

opportunity_user_config = {
    "opportunity_owner": user_data,
    "creator": user_data,
    "latest_modifier": user_data,
}

ac_opportunity_map_ = {
    'customer_name': 'ac_customer_name__c',
    'opportunity_owner': 'owner_id',
    'opportunity_name': 'name',
    'opportunity_type': 'opportunity_type',
    'sales_amount': 'ac_sales_amount__c',
    'loss_reason': 'lose_reason',
    'closing_date': 'expected_deal_time',
    'sales_stage': 'sale_stage',
    'current_project_progress': 'ac_current_project_progress__c',
    'opportunity_creation_time': 'create_time',
    'creator': 'creator_id',
    'latest_modification_date': 'update_time',
    'latest_modifier': 'updater_id',
    'department': 'org_id',
    'loss_stage': 'ac_loss_stage__c',
    'loss_description': 'lose_description',
    'lead_source': 'lead_source',
    'phone': 'contact_information',
    'win_date': 'ac_win_date__c',
    'product_opportunity_type': 'ac_product_opportunity_type__c',
    'opportunity_id': 'id',
    'account_id': 'account_id',
}
