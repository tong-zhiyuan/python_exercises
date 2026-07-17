# 练习题：编写一个程序，将字符串中所有字符的大小写互换（大写变为小写，反之亦然）。
#
# 练习目的：本练习演示大小写转换。虽然大小写转换很简单，但它常用于搜索算法中以规范化数据，或在文本编辑器中提供“切换大小写”功能。
#
# 给定输入： str1 = "PyThOn"
#
# 预期输出： pYtHoN

input_string = input("请输入字符串: ")


def string_handler(s: str):
    # res = ''
    # for char in s:
    #     if char.islower():
    #         res += char.upper()
    #     else:
    #         res += char.lower()

    res = s.swapcase() # 笨办法和真正的好方法对比
    return res


result = string_handler(input_string)
print(f"{result}")
