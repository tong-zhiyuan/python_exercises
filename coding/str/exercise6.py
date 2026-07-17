# 练习题：编写一个程序，查找给定字符串中子字符串“Emma”的最后一个索引。
#
# 练习目的：虽然该.find()方法从字符串开头开始搜索，但.rfind()反向查找方法可以找到指定模式最近一次出现的位置。在解析需要识别最终分隔符的文件路径或 URL 时，此功能至关重要。
#
# 给定输入： str1 = "Emma is a data scientist who knows Python. Emma works at google."
#
# 预期输出： Last occurrence of Emma starts at index 43

input_string = input('请输入字符串: ')


def string_handler(s: str):
    index = s.rfind('Emma')

    return index


print(f"Last occurrence of Emma starts at index {string_handler(input_string)}")
