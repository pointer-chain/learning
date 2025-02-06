from sz.utils.excel_temp import CustomerXlrd


if __name__ == '__main__':
    # excel操作
    # 客户表
    # excel = CustomerXlrd(create_table="D:/data/test/customer_convert.xlsx", read_table="D:/data/test/customer.xlsx",
    #                      sheet_name="Result 1", csv_name="D:/data/test/customer_convert.csv")
    # excel.numpy_excel_ac_account()
    # excel.excel_to_csv()

    # 联系人表
    # excel = CustomerXlrd(create_table="D:/data/test/contacts_convert.xlsx", read_table="D:/data/test/contacts.xlsx",
    #                      sheet_name="Result 1", csv_name="D:/data/test/contacts_convert.csv")
    # excel.numpy_excel_ac_contact()
    # excel.excel_to_csv()

    # 销售机会表
    # excel = CustomerXlrd(create_table="D:/data/test/sales_opportunity_convert.xlsx", read_table="D:/data/test/sales_opportunity.xlsx",
    #                      sheet_name="Result 1", csv_name="D:/data/test/sales_opportunity_convert.csv")
    # excel.numpy_excel_ac_opportunity()
    # excel.excel_to_csv()

    # 线索表
    excel = CustomerXlrd(create_table="D:/data/test/sales_leads_convert.xlsx", read_table="D:/data/test/sales_leads.xlsx",
                         sheet_name="Result 1", csv_name="D:/data/test/sales_leads_convert.csv")
    excel.numpy_excel_ac_lead()
    excel.excel_to_csv()
