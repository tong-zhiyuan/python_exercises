# 练习题：编写一个程序，创建一个由奇数长度输入字符串的中间三个字符组成的新字符串。
#
# 练习目的：本练习在索引的基础上，引入字符串切片。切片是 Python 的一项强大功能，可以高效地提取整个数据“块”。
#
# 给定输入： str1 = "JhonDipPeta"
#
# 预期输出： Dip

input_string = input("请输入长度大于3的奇数字符串: ")


def get_middle_three_char(odd_string):
    if len(odd_string) < 3 or len(odd_string) % 2 == 0:
        print('字符串格式错误')
        return None
    else:
        return odd_string[int(((len(odd_string) - 1) / 2) - 1):int(((len(odd_string) - 1) / 2) + 2)] # 切片的参数必须是int


print(get_middle_three_char(input_string))
