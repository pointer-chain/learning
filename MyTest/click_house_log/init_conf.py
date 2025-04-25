import configparser


def read_ini_file(section):
    config = configparser.ConfigParser()
    try:
        config.read("conf.ini")
        res = {}
        for key, value in config.items(section):
            res[key] = value
        return res
    except Exception as e:
        print(f"读取文件时出错: {e}")

if __name__ == '__main__':
    print(read_ini_file("CLICKHOUSE"))
