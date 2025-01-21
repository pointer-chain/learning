from sz.config.db import Mysql
from sz.config.db import PostGreSql
import psycopg2
import pymysql


class SqlOperate(object):
    def __init__(self):
        self.pg_info = PostGreSql()
        self.sql_info = Mysql()
        self.sql = None
        self.pg = None
        self.pg_cur = None
        self.sql_cur = None

    def init_cursor(self):
        self.pg = psycopg2.connect(database=self.pg_info.pg_database, user=self.pg_info.pg_user,
                                   password=self.pg_info.pg_password,
                                   host=self.pg_info.pg_host, port=self.pg_info.pg_port)
        self.pg_cur = self.pg.cursor()
        self.sql = pymysql.connect(database=self.sql_info.database, user=self.sql_info.user,
                                   password=self.sql_info.password,
                                   host=self.sql_info.host, port=self.sql_info.port)
        self.sql_cur = self.sql.cursor()

    def close_cursor(self):
        self.pg.close()
        self.sql.close()

    def select_sql(self, sql):
        try:
            # 执行SQL语句
            self.sql_cur.execute(sql)
            # 获取所有记录列表
            results = self.sql_cur.fetchall()
            return results
        except Exception as e:
            print(e)

    def insert_pg(self, query):
        # 执行查询
        self.pg_cur.execute(query)
        # 获取查询结果
        self.pg_cur.commit()
