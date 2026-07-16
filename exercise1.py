# 练习题：编写一个程序，创建一个由输入字符串的第一个字符、中间字符和最后一个字符组成的新字符串。
#
# 练习目的：本练习旨在教授字符串索引的基础知识。访问特定位置，尤其是需要计算长度的中间位置，是数据解析和文本操作的基础技能。
#
# 给定输入： str1 = "James"
#
# 预期输出： Jms

input_str = input("请输入字符串: ")


def string_handler(string: str):
    first_char = string[0]
    char_len = len(string)
    middle_char = string[int(char_len / 2)] # int(char_len / 2)奇中偶右 int((char_len-1) / 2)奇中偶左
    last_char = string[-1]
    return f"{first_char}{middle_char}{last_char}"


print(string_handler(input_str))
