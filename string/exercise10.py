# 练习题：编写一个程序，计算给定字符串中元音字母（a、e、i、o、u）的总数。
#
# 给定输入： str1 = "Hello World"
#
# 预期输出： Vowel Count: 3

input_string = input('请输入字符串: ')


def string_handler(s: str):
    i: int = 0
    for char in s:
        if char in 'aeiou':
            i += 1

    return i

print(string_handler(input_string))