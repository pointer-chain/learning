from sz.utils.excel_temp import CustomerXlrd


if __name__ == '__main__':
    excel = CustomerXlrd("./customer_com.xlsx", "./customer.xlsx", "Result 1")
    excel.numpy_excel_ac_account()
