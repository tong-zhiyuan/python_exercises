# 练习题：从给定的字符串中删除所有空格，包括单词之间的空格。
#
# 练习目的：本练习旨在突出字符串修剪和字符串过滤之间的区别。字符串修剪.strip()仅移除字符串开头和结尾的空格，而.replace()字符串过滤可以深入字符串内部，全局移除字符。
#
# 给定输入： str1 = " P y t h o n "
#
# 预期输出： Python

input_string = input("请输入字符串: ")


def string_handler(s: str):
    return s.replace(" ", "")


result = string_handler(input_string)
print(f"{result}")
