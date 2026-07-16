# 练习题：编写一个程序，找出给定字符串中子字符串“USA”的总数，忽略大小写（即，“usa”和“USA”都应该被计数）。
#
# 练习目的：本练习旨在讲解大小写规范化。在实际数据科学和网络爬虫应用中，文本数据通常不一致。在处理之前将所有文本转换为小写被认为是一种标准的最佳实践。
#
# 给定输入： str1 = "Welcome to USA. usa awesome, isn't it?"
#
# 预期输出： The USA count is: 2

input_string = input("请输入字符串: ")


def string_handler(s):
    l = s.lower()  # 千万别指望s.lower()直接改变s、字符串是不可变类型别忘了
    return l.count('usa')


print(string_handler(input_string))
