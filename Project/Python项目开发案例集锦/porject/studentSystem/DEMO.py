import re


# # 将匹配的数字乘于 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)
#
#
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))

# !/usr/bin/python

# import re
#
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('www', 'www.runoob.com').groups())
# print(re.match('www', 'www.runoob.com').group())
# print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配


import re

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.groups())
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")