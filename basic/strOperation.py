#!/usr/bin/python3
# 字符串的常用操作方法:
#   <string>.func()

s = "hello python!"
# upper():将字符串中的字母大写
print(s.upper())
# lower()：将字符串中的字母小写
print(s.lower())
# capitalize()：字符串首字母大写
print(s.capitalize())
# strip()：去除字符串两边的空格和指定字符
s = s + " " + "strip"
print(s)
print(s.strip('p'))
# split()：按指定字符分割字符串为数组
print(s.split(" "))
# isdigital()：判断是否为数字类型的字符串,返回true或者false
print(s.isdigit())
# find()：搜索指定字符串，可以指定字符串中的搜索范围
print(s.find("python"))
# replace()：字符串替换
print(s.replace("python", "python3"))
# for循环遍历字符串中的字符
# NOTE:python3 print()函数不换行，指定end参数为''
for var in s:
    print(var, end='') 