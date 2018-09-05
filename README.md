# robotframework-toolsUtil
ToolsUtil for robotframework.

## get_utc_stamp
    """产生毫秒级时间戳-UTC时间

    :return:

    Examples:
    | ${time_stamp}= | Get Utc Stamp |
    =>
    | ${time_stamp} = 1535596350000
    """
    
## get_local_stamp
    """产生毫秒级时间戳-本地时间

    :return:

    Examples:
    | ${time_stamp}= | Get Utc Stamp |
    =>
    | ${time_stamp} = 1535596350000
    """
    
## salt_md5
    """对字符串进行md5加密

    :param password: 要加密的密码

    :return:

    Examples:
    | ${password_md5}= | Salt Md5 |
    """
    
## log_json
    """格式化Json数据输出

    :param json_string: Json数据类型或字典数据类型

    :return:
    """
    
## generator_random_email
    """生成随机的10位数邮箱

    :return:

    Examples:
    | ${email} | Generator Random Email |
    =>
    | ${email} = 45tghmju79@email.com
    """
    
## generator_random_telephone
    """随机生成手机号

    :return:

    Examples:
    | ${telephone} | Generator Random Telephone |
    =>
    | ${telephone} = 13244443333
    """
    
## include_string
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
