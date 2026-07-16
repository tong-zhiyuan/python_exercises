# 练习题：编写一个程序，用连字符分割给定的字符串，并显示每个子字符串。
#
# 练习目的：本练习介绍分词的概念。根据分隔符（例如逗号、空格或连字符）将字符串分割成更小的组成部分，是处理 CSV 文件、日志和用户输入列表的常用技术。
#
# 给定输入： str1 = "Emma-is-a-data-scientist"
#
# 预期输出：
# Displaying each substring:
# Emma
# is
# a
# data
# scientist


input_string = input("请输入字符串: ")


def string_handler(s: str):
    return s.split('-')


result = string_handler(input_string)
for s in result:
    print(s)
