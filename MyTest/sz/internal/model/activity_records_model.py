table_id = {
    'id': '主键ID',
    'activity_content': '活动记录内容',
    'publisher': '发布人',
    'department': '所属部门',
    'creation_date': '创建日期',
    'source': '来自',
    'activity_type': '活动记录类型',
    'publish_time': '发布时间',
    'latest_modification_date': '最新修改日',
    'customer': '客户',
    'is_agency_company': '是否是代账公司',
    'employee_id': '员工编号',
    'location': '位置',
    'location_details': '位置详情',
    'visit_target': '拜访对象',
    'visit_purpose': '拜访目的',
    'next_action_plan': '下一步行动计划',
    'activity_id': 'id'
}

ac_activity_record = {
    'activity_content': 'content',
    'publisher': 'creator_id',
    'department': 'owner_org_ids',
    'creation_date': 'create_time',
    'activity_type': 'follow_method',
    'latest_modification_date': 'update_time',
    'is_agency_company': 'ac_is_agency_company__c',
    'location': 'ac_location__c',
    'location_details': 'account_address',
    'visit_target': 'ac_visit_target__c',
    'visit_purpose': 'ac_visit_purpose__c',
    'next_action_plan': 'ac_next_action_plan__c',
    'activity_id': 'id',
}

ac_activity_record_insert = {
    "content": "activity_content",
    "creator_id": "publisher",
    "owner_org_ids": "department",
    "create_time": "creation_date",
    "follow_method": "activity_type",
    "update_time": "latest_modification_date",
    "ac_is_agency_company__c": "is_agency_company",
    "ac_location__c": "location",
    "account_address": "location_details",
    "ac_visit_target__c": "visit_target",
    "ac_visit_purpose__c": "visit_purpose",
    "ac_next_action_plan__c": "next_action_plan",
    'id': 'activity_id'
}

activityRecordFrom = {
    1: "account_id",  # 客户
    11: "lead_id",  # 线索
    3: "opportunity_id",  # 机会
}


activity_type = {
    "电话": 1,
    "拜访签到": 2,
    "快速记录": 3,
    "Email": 5,
    "任务": 6,
}

# TODO 非标准枚举 只是针对此表映射
is_agency_company = {
    "个人版客户": 7,
    "代账公司": 2,
    "企业版客户": 6,
    "加盟意向": 13,
    "待确定": 5,
    "找代理记账公司": 14,
    "无效（无意向/空号）": 4,
    "有代账版需求（非代账公司）": 3
}

visit_target = {
    "关键决策人": 1,
    "其他关键人": 2,
    "会计主管": 3,
    "销售主管": 4,
    "未见到关键人": 5,
}

visit_purpose = {
    "关键决策人": 1, "其他关键人": 2, "会计主管": 3, "销售主管": 4, "未见到关键人": 5
}

activity_dict = {
    "activity_type": activity_type,
    "is_agency_company": is_agency_company,
    "visit_target": visit_target,
    "visit_purpose": visit_purpose,
}
