from sz.utils.excel_temp import CustomerXlrd


if __name__ == '__main__':
    # excel操作
    excel = CustomerXlrd(create_table="./customer_com.xlsx", read_table="./customer.xlsx",
                         sheet_name="Result 1", csv_name="example.csv")
    excel.numpy_excel_ac_account()
    excel.excel_to_csv()
