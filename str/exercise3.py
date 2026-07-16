# 练习题：给定两个字符串，s1和，通过在中间s2添加来创建一个新字符串。s2s1
#
# 练习目的：本位置修改字符串。练习介绍字符串分区和字符串连接。在编程中，您经常需要将数据“注入”到模板中，或在特定
#
# 给定输入： s1 = "Ault" s2 = "Kelly"
#
# 预期输出： AuKellylt

input_string1 = input("请输入第一个字符串: ")
input_string2 = input("请输入第二个字符串: ")


def string_handler(s1: str, s2):
    s1_left = s1[:int((len(s1) - 1) / 2) + 1]  # 想要不管奇偶都获得中间的下标、就是int((len(x)-1)/2)、奇数长度就正好在中间、偶数是中间偏左的那个
    s1_right = s1[int((len(s1) - 1) / 2) + 1:]

    return s1_left + s2 + s1_right


print(string_handler(input_string1, input_string2))
