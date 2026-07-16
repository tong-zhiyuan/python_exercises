# 练习题：检查给定的网址是否以“https”开头并以“.com”结尾。
#
# 练习目的：本练习旨在教授布尔验证。与手动切片相比，使用.startswith()`and`等方法.endswith()可以更简洁、更不容易出错地验证文件格式、协议或命名约定。
#
# 给定输入： str1 = "https://google.com"
#
# 预期输出： Is valid URL: True

input_string = input("请输入地址: ")


def string_handler(s: str):
    if s.startswith("https") and s.endswith(".com"):
        return True
    return False


result = string_handler(input_string)
print(f"Is valid URL: {result}")
