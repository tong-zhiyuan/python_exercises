# 练习题：给定两个字符串 as1和s2b，分别取每个输入字符串的第一个、中间和最后一个字符，创建一个新字符串。
#
# 练习目的：本练习旨在练习复杂数据拼接。它需要将多个独立的数据提取结果组织成一个单一的结果，这在从用户数据生成 ID 或代码时很常见。
#
# 给定输入： s1 = "America" s2 = "Japan"
#
# 预期输出： AJrpan

input_string1 = input("请输入第一个字符串: ")
input_string2 = input("请输入第二个字符串: ")


def string_handler(s1, s2):
    first_middle_char = s1[int((len(s1) - 1) / 2)] # 想要不管奇偶都获得中间的下标、就是int((len(x)-1)/2)、奇数长度就正好在中间、偶数是中间偏左的那个
    second_middle_char = s2[int((len(s2) - 1) / 2)]
    return f'{s1[0]}{s2[0]}{first_middle_char}{second_middle_char}{s1[-1]}{s2[-1]}'


print(string_handler(input_string1, input_string2))
