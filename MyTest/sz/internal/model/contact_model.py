from sz.internal.model.account_model import user_data

contact_map = {
    'contact_owner': 'owner_id',
    'name': 'name',
    'company_name': 'ac_company_name__c',
    'department': 'department',
    'job_title': 'title',
    'phone': 'other_phone',
    'mobile_phone': 'phone',
    'province': 'ac_city_id__c',
    'address': 'address',
    'create_date': 'create_time',
    'creator': 'creator_id',
    'latest_modifier': 'updater_id',
    'latest_modification_date': 'update_time',
    'belonging_department': 'org_id',
    'contacts_id': 'id',
}

contact_user_config = {
    "contact_owner": user_data,
    "creator": user_data,
    "latest_modifier": user_data,
}
