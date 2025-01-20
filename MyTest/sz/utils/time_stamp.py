import time


def return_strftime(time_stamp):
    time_array = time.localtime(int(time_stamp))
    return time.strftime("%Y-%m-%d %H:%M:%S", time_array)


if __name__ == '__main__':
    a = 1730671263723
    print(return_strftime(a))
