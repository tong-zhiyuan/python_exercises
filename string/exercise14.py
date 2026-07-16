# 练习题：i编写一个程序，从字符串中删除索引为 的字符。
#
# 练习目的：由于 Python 字符串是不可变的（你不能直接删除索引处的字符），本练习将教你如何通过跳过特定部分来“重建”字符串。
#
#
# 给定输入： str1 = "Python"，i = 2
#
# 预期输出：Pyhon（索引为 2 的字符“t”已被删除）


input_string = input("请输入字符串: ")
input_number = int(input('请输入索引: '))


def string_handler(s: str):
    left = s[:input_number]
    right = s[input_number + 1:]
    return left + right


result = string_handler(input_string)
print(f"{result}")
