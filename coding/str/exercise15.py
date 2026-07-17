# 练习题：使用该.partition()方法将字符串拆分为三个部分：分隔符之前的部分、分隔符本身和分隔符之后的部分。
#
# 练习目的： .split()非常适合将字符串拆分成多个部分。.partition()是一个始终返回三元组的专用工具。它尤其适用于解析电子邮件地址或键值对等数据，因为这类数据需要保留或考虑分隔符。
#
# 给定输入： str1 = "username@company.com"，sep = "@"
#
# 预期输出： ('username', '@', 'company.com')

input_string = input("请输入字符串: ")
input_split = input('请输入分隔符: ')


def string_handler(s: str, k: str):
    return s.partition(k) # 了解即可


result = string_handler(input_string, input_split)
print(f"{result}")
