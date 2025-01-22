import json
from sz.internal.model.activity_records_model import ac_activity_record
from sz.internal.model.activity_records_model import activityRecordFrom
from sz.internal.model.activity_records_model import activity_dict
from sz.utils.excel_data import return_address, judge_data_list
from sz.utils.sql_operate import SqlOperate
from sz.utils.time_stamp import return_strftime


if __name__ == '__main__':
    # 数据库操作
    cur = SqlOperate()
    cur.init_cursor()  # 初始化链接
    count_sql = """SELECT COUNT(*) FROM shuzhou_move.activity_records;"""
    count_res = cur.select_sql(count_sql)
    range_index = count_res[0][0] // 500 + 1  # 确定循环最大值
    for ran in range(0, range_index):
        search_sql = f"""SELECT t.activity_content, t.publisher, t.creation_date, t.activity_type, t.latest_modification_date,
         t.is_agency_company, t.location, t.location_details, t.visit_target, t.visit_purpose, t.next_action_plan,
          t.activity_id, t.source FROM shuzhou_move.activity_records t LIMIT {500 * ran},500"""
        insert_sql_1 = f"""INSERT INTO fastapp.yzf_crm.ac_activity_record (content, creator_id, create_time, follow_method, update_time, ac_is_agency_company__c,
         ac_location__c, account_address, ac_visit_target__c, ac_visit_purpose__c, ac_next_action_plan__c, id, account_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        insert_sql_11 = f"""INSERT INTO fastapp.yzf_crm.ac_activity_record (content, creator_id, create_time, follow_method, update_time, ac_is_agency_company__c,
         ac_location__c, account_address, ac_visit_target__c, ac_visit_purpose__c, ac_next_action_plan__c, id, lead_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        insert_sql_3 = f"""INSERT INTO fastapp.yzf_crm.ac_activity_record (content, creator_id, create_time, follow_method, update_time, ac_is_agency_company__c,
         ac_location__c, account_address, ac_visit_target__c, ac_visit_purpose__c, ac_next_action_plan__c, id, opportunity_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        sql_datas = cur.select_sql(search_sql)  # 查询结果
        insert_sql_list_1 = []
        insert_sql_list_11 = []
        insert_sql_list_3 = []
        for sql_data in sql_datas:
            source = json.loads(sql_data[-1])
            activity_type_id = source.get("activityRecordFrom", {})
            ids = activityRecordFrom.get(activity_type_id, {})
            source_id = source.get("activityRecordFrom_data")
            activity_list = list(ac_activity_record.keys())
            insert_row_list = []
            for col_index in range(len(activity_list)):
                col_id = activity_list[col_index]
                if col_id in activity_dict:
                    if col_id == "publisher":
                        value = activity_dict.get(col_id).get(sql_data[col_index], "")
                        if not value:
                            value = "0JJV7CK864FAG"
                    else:
                        values = judge_data_list(sql_data[col_index])
                        if isinstance(values, list):
                            value = [activity_dict.get(col_id).get(da_ele, "") for da_ele in values]
                        else:
                            value = activity_dict.get(col_id).get(sql_data[col_index], "")
                            if col_id == "visit_purpose":
                                if not value:
                                    value = 10
                            elif col_id == "is_agency_company":
                                if not value:
                                    value = 5
                elif "date" in col_id or "time" in col_id:
                    value = return_strftime(sql_data[col_index])
                elif col_id == "location_details":
                    value = return_address(sql_data[col_index])
                else:
                    value = sql_data[col_index]
                insert_row_list.append(value)
            insert_row_list.append(source_id)
            if activity_type_id == 1:
                insert_sql_list_1.append(insert_row_list)
            elif activity_type_id == 11:
                insert_sql_list_11.append(insert_row_list)
            elif activity_type_id == 3:
                insert_sql_list_3.append(insert_row_list)
            else:
                continue
        if insert_sql_list_1:
            cur.insert_pg(insert_sql_1, insert_sql_list_1)
        if insert_sql_list_11:
            cur.insert_pg(insert_sql_11, insert_sql_list_11)
        if insert_sql_list_3:
            cur.insert_pg(insert_sql_3, insert_sql_list_3)
        break
    cur.close_cursor()
