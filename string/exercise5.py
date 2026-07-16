# 练习题：编写一个程序来反转给定的字符串。
#
# 练习目的：反转字符串是经典的逻辑思维训练。在 Python 中，最有效的方法是使用切片（Slicing），这体现了 Python 使用“步骤”操作序列的能力。它是解决诸如回文检测等问题的先决条件。
#
# 给定输入： str1 = "PYnative"
#
# 预期输出： evitanYP

input_string = input("请输入字符串: ")


def string_handler(s):
    return "".join(reversed(s))


print(string_handler(input_string))
