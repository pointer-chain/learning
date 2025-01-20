from datetime import datetime


def return_strftime(time_stamp):
    if len(str(time_stamp)) >= 10:
        date_array = datetime.utcfromtimestamp(int(str(time_stamp)[:10]))
    else:
        date_array = datetime.utcfromtimestamp(int(time_stamp))
    res = date_array.strftime("%Y-%m-%d %H:%M:%S")
    return res


if __name__ == '__main__':
    a = 1737820799000
    print(return_strftime(a))
