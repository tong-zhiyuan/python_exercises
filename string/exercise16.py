# 练习题：给定一个字符串形式的文件名，仅提取文件扩展名（例如，.png或.pdf）。
#
# 练习目的：本练习旨在教授字符串解析。在软件开发中，您需要在处理上传文件之前验证文件类型。本练习可以帮助您练习查找字符（点号）的最后一个出现位置，以便正确处理包含多个点号的文件（例如archive.tar.gz）。
#
# 给定输入： file_name = "report_final_v2.pdf"
#
# 预期输出： pdf

input_string = input("请输入字符串: ")


def string_handler(s: str):
    return s.split('.')[-1]


result = string_handler(input_string)
print(f"{result}")
