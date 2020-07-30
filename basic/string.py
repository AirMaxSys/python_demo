#!/usr/bin/python3

# 字符串是用双引号或单引号括起来的一个或多个字符
# 字符串可以保存在变量中也可以单独存在
# 可以用type()函数测试一个字符串的类型
str = "hello"
print("type(str):", type(str))

# 输出带引号的字符串，用转义字符\
print("str", "=", "\"hello\"")

# 字符串是一个字符序列：字符串最左端的位置标记为0依次增加，字符串中的编号叫索引
# 可以通过索引来访问字符串中的特定位置
print("str[0] =", str[0])

# python中可以使用反响索引，最右边的索引为-1
for i in range(-5, 0):
     print("str[" , i , "]" + "=" + str[i])
# NOTE:print()中使用+号只能连接字符串

# 通过两个索引确定一个字符串字串的范围
# <string>[<start>:<end>]，字符串字串从start开始到end前一个结束(类似range函数)
print("str[1:3]=" + str[1:3])

# 字符串连接:
#   +:连接两个字符串
#   *:将字符串本身重复连接N次
print("str*3 = " + str * 3)

# len()函数返回字符串的长度
print("len(str) =", len(str))

# str()函数可以将大多数数据类型转换成字符串
# NOTE:之前定义了与str方法同名的变量需要先解除变量才能使用该方法
del str
print("str(123) = " + str(123))
print("str(2.5e-4) = " + str(2.5e-4))

# 注意python中的字符串是不可变的数据类型
S1 = "damn"
# error
# S1[0] = 'c'

# 修改字符串只能用分片的技巧
S2 = 'The ' + S1[:]
del S1
S1 = S2
print(S1)

# e.g:输入一个月份数字，返回对应月份名称的缩写
# NOTE:用户输入是字符串,作为索引要转换为数字类型
# 方法一：list
# mon=["Jan","Feb","Mar","May", "Apr", "Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
# index = input()
# print(mon[int(index) - 1])

# 方法二: string
# mon = "JanFebMarAprMayJunJulAugSepOctNovDec"
# n = input("请输入月份数(1~12):")
# pos = (int(n) - 1) * 3
# print("月份英文缩写:" + mon[pos:pos+3]) 

# python与str有关的内置方法
mstr1 = 'hello, world'
print(mstr1.capitalize()) #Hello, world
print(mstr1.title()) #Hello, World
print(mstr1.upper()) #HELLO, WORLD
print(mstr1.startwith('He')) #False
print(mstr1.startwith('HEL')) #True

mstr2 = 'abcd123'
print(mstr2.isdigit()) #False
print(mstr2.isalpha()) #False
print(mstr2.isalnum()) #True

# 判断字符串是否在一个字符串中
mstr3 = 'today is good'
msubstr = 'is'
if msubstr in mstr3:
    print(f'{msubstr} is a substring of {mstr3}')


