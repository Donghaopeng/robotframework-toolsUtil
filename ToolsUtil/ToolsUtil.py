# coding:utf-8

import datetime
import hashlib
import json
import time
import random

import pytz


def get_utc_stamp():
    """产生毫秒级时间戳-UTC时间

    :return:

    Examples:
    | ${time_stamp}= | Get Utc Stamp |
    =>
    | ${time_stamp} = 1535596350000
    """
    return str(int(round(time.mktime(datetime.datetime.now(pytz.utc).timetuple()) * 1000)))


def get_local_stamp():
    """产生毫秒级时间戳-本地时间

    :return:

    Examples:
    | ${time_stamp}= | Get Utc Stamp |
    =>
    | ${time_stamp} = 1535596350000
    """
    return str(int(round(time.time()) * 1000))


def salt_md5(password):
    """对字符串进行md5加密

    :param password: 要加密的密码

    :return:

    Examples:
    | ${password_md5}= | Salt Md5 |
    """
    string = ("MO9~E4F060E1A3F44542854F20B87EE0EDC2~GLUTTON" + password).encode('utf-8')
    return hashlib.md5(string).hexdigest().upper()


def log_json(json_string):
    """格式化Json数据输出

    :param json_string: Json数据类型或字典数据类型

    :return:
    """
    print(json.dumps(json_string, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False))


def generator_random_email():
    """生成随机的10位数邮箱

    :return:

    Examples:
    | ${email} | Generator Random Email |
    =>
    | ${email} = 45tghmju79@email.com
    """
    char_num = [a for a in range(0, 10)]
    char_lower_case = list('abcdefghijklmnopqrstuvwxyz')
    char_capital = list('abcdefghijklmnopqrstuvwxyz'.upper())
    char_list = char_num + char_lower_case + char_capital
    email_first = ''
    for i in range(0, 10):
        random_index = random.randint(0, len(char_list) - 1)
        email_first += str(char_list[random_index])
    email_second_list = ['@qq.com', '@mo9.com', '@gmail.com', '@163.com']
    email_second = email_second_list[random.randint(0, len(email_second_list) - 1)]
    email = email_first + email_second
    return email


def generator_random_telephone():
    """随机生成手机号

    :return:

    Examples:
    | ${telephone} | Generator Random Telephone |
    =>
    | ${telephone} = 13244443333
    """
    tele_first_list = '134,135,136,137,138,139,150,151,152,157,158,159,130,131,132,155,156,133,153'.split(',')
    tele_first = str(tele_first_list[random.randint(0, len(tele_first_list) - 1)])
    tele_second = random_four_number() + random_four_number()
    return tele_first + tele_second


def random_four_number():
    """随机生成4位数字字符串

    :return:

    Examples:
    | ${num1} | Random Four Number |
    | ${num2} | Random Four Number |
    | ${num3} | Random Four Number |
    | ${num4} | Random Four Number |
    =>
    | ${num1} = 0001
    | ${num2} = 0011
    | ${num3} = 0111
    | ${num4} = 1111
    """
    number = random.randint(0, 9999)
    if number < 10:
        number_s = '000' + str(number)
    elif 10 <= number < 100:
        number_s = '00' + str(number)
    elif 100 <= number < 1000:
        number_s = '0' + str(number)
    else:
        number_s = str(number)
    return number_s


def include_string(string1, string2):
    """判断string2 是否包含string1,

    :param string1:

    :param string2:

    :return:[Boolean]

    Examples:
    | ${string1} | set variable | aa |
    | ${string2} | set variable | abceaahh |
    | ${res} | Include String | ${string1} | ${string2} |
    =>
    | ${res} = True
    """
    if string1 in string2:
        return True
    else:
        return False


if __name__ == '__main__':
    # print(get_utc_stamp())
    # print(get_local_stamp())
    # print(salt_md5('mo911111'))
    # print(generator_random_email())
    print(generator_random_telephone())
    # print(random_four_number())
