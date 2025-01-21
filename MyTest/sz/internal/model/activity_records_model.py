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
    'customer': 'account_id',
    'is_agency_company': 'ac_is_agency_company__c',
    'location': 'ac_location__c',
    'location_details': 'account_address',
    'visit_target': 'ac_visit_target__c',
    'visit_purpose': 'ac_visit_purpose__c',
    'next_action_plan': 'ac_next_action_plan__c',
}

activityRecordFrom = {
    1: "account_id",  # 客户
    11: "lead_id",  # 线索
    3: "opportunity_id",  # 机会
}
