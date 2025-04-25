import logging
import clickhouse_connect
from click_house_log.log_click import ColoredFormatter
from init_conf import read_ini_file
from colorama import init, Fore, Back, Style
import time
from datetime import datetime

# 创建日志记录器
logger = logging.getLogger(__name__)
# 设置日志级别
logger.setLevel(logging.DEBUG)
# 创建控制台处理器
console_handler = logging.StreamHandler()
# 设置控制台处理器的日志级别
console_handler.setLevel(logging.DEBUG)
# 创建自定义格式化器
formatter = ColoredFormatter()
# 为控制台处理器设置格式化器
console_handler.setFormatter(formatter)
# 为日志记录器添加控制台处理器
logger.addHandler(console_handler)

class CK(object):
    def __init__(self):
        self.client = None
        self.connect_dict = read_ini_file('CLICKHOUSE')
        self.color = read_ini_file('COLOR')

    def init_connect(self):
        try:
            self.client = clickhouse_connect.get_client(**self.connect_dict)
        except clickhouse_connect.driver.exceptions.InterfaceError as e:
            logger.error(f"连接 ClickHouse 时出错: {e}")
        except Exception as e:
            logger.error(f"发生未知错误: {e}")

    @staticmethod
    def get_timestamp(date_str):
        datetime_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        timestamp = int(datetime_obj.timestamp())
        return timestamp

    def sql(self, sql):
        table_result = self.client.query(sql)
        for row in table_result.result_rows:
            logger.info(row)
        # table_names = [row for row in table_result.result_rows]
        # logger.info(f"数据:{table_names}")
        self.client.close()

if __name__ == '__main__':
    ck = CK()
    ck.init_connect()
    # start_time = ck.get_timestamp('2025-04-08 11:22:00')
    # end_time = ck.get_timestamp('2025-04-08 13:00:00')
    start_time = ck.get_timestamp('2025-04-09 20:30:00')
    end_time = ck.get_timestamp('2025-04-09 20:35:00')
    log_id = '9a5a9801e70e93a66c4b490ec1850e20'
    sql = f"""SELECT * FROM `rpa_log` WHERE asctime >= toDateTime64({start_time}, 3, 'America/Los_Angeles') AND asctime < toDateTime64({end_time}, 3, 'America/Los_Angeles') AND log_id='{log_id}' AND (1='1') ORDER BY asctime"""
    sql = f"""SELECT * FROM `rpa_log` WHERE asctime >= toDateTime64({start_time}, 3) AND asctime < toDateTime64({end_time}, 3) AND levelname='INFO' AND filename='runlogin.py' AND funcname='check_company_info' AND (1='1') ORDER BY asctime"""
    # ['log_id', 'asctime', 'levelname', 'filename', 'funcname', 'lineno', 'message', 'pid']
    ck.sql(sql)
