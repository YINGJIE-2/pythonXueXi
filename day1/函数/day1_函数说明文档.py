def sum_len (str):
    """
    sum_len函数接收一个字符串，统计字符串的长度并返回长度值
    :param str: 参数str需要统计的字符串
    :return: 返回字符串的长度
    """

    lens=0
    for i in str:
        lens+=1
    return lens

stra="djkladbak"
print(sum_len(stra))