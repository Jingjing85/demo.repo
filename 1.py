# import numpy as np
# a = [1, 2, 3.4, 5]
# print(a[1])
# b = a[:2]
# print(b)

# a = 3
# b = 5
# print(a - b)
# if len(a) > len(b):
#     lc = len(a) - len(b)
#     b = '{}{}'.format(r'0' * lc, b)
# elif len(a) < len(b):
#     lc = len(b) - len(a)
#     a = '{}{}'.format(r'0' * lc, a)
str1 = "21.345"
str2 = "3423.56"
# print(str1.split("."))
subStr1 = str1.split(".")
subStr2 = str2.split(".")

print(subStr1)
print(subStr2)

subFirst = subStr1[0] + subStr2[0]
subSecond = subStr1[1] + subStr2[1]
#如果输入的数据中包含小数点，则把整数部分和小数部分分开后，在调用加减函数
#如果刚开始比较长度，短的那部分在前面补0，就不用后面分情况另计算不等长的那部分了

print(subFirst)
print(subSecond)