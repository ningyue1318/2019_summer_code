def write2file(filename, content):
    """
    :param filename: 传入文件的名称
    :param content: 传入文件的内容
    :return: 无
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(content)


def statistic_str(string):
    """
    统计字符串的数字，字符，空格，以及其他个数
    :param string: 传入统计的字符串
    :return: 统计结果
    """
    result = {'digit': 0,
              'character': 0,
              'space': 0,
              'other': 0}
    for i in string:
        if i.isnumeric():
            result['digit'] += 1
        elif i.isalpha():
            result['character'] += 1
        elif i.isspace():
            result['space'] += 1
        else:
            result['other'] += 1

    return result


def length_bigger_5(data):
    """
    :param data: 源数据
    :return: 长度大于5，返回True,否则返回False
    """
    if len(data) > 5:
        return True
    else:
        return False


def bigger_2(data):
    """
    :param data: 传入数据
    :return: 如果data长度大于2，返回前两位，否则返回原数据
    """
    return data[:2] if len(data) > 2 else data


def odd_index(data):
    """
    :param data: 返回奇数索引的列表
    :return:返回奇数列索引组成的元素
    """
    return [x for index, x in enumerate(data, 1) if index % 2 != 0]


def bigger_2_dict(data):
    for i in data.keys():
        if len(data[i]) > 2:
            data[i] = data[i][:2]
    return data


if __name__ == '__main__':
    write2file('file1.txt', 'this is my first func')
    print(statistic_str('123qwer  43+'))
    print(length_bigger_5("fhuerihuiehiuehr"))
    print(bigger_2("qwer"))
    print(bigger_2("qw"))
    print(odd_index('qwertyu'))
    print(bigger_2_dict({"k1": 'v1v2', "k2": [11, 22, 33, 44]}))