# 练习题：编写一个程序来检查两个字符串是否平衡。例如，如果字符串 a 中的所有字符都存在于字符串 b 中，则称字符串s1a 和 b是平衡的。字符的位置无关紧要。s2s1s2
#
# 练习目的：本练习侧重于成员资格测试。这一基本概念应用于数据验证，例如验证密码是否包含必需字符或确定搜索查询是否与数据库条目匹配。
#
# 给定输入：
#
# 案例1：，s1 = "yn"案例s2 = "PyNative"
# 2 s1 = "ynf"：，s2 = "PyNative"

# 预期输出：
# 情况 1：True；
# 情况 2：False


input_string = input("请输入字符串")
input_key = input("请输入key值")


def string_handler(s:str, k:str):
    ls = s.lower()
    lk = k.lower()
    for char in lk:
        if char not in ls: # 是否包含要用in、最简单
            return False
    return True

print(string_handler(input_string, input_key))
