#!/usr/bin/python3

# 元组类型: 指包含多个元素的类型，元素之间用逗号分隔，元组是不可变的数据类型

# 元组可以是空的：
t1 = ()

# 元组可以只包含一个元素
t2 = (123,)

# 元组外侧可以使用括号，也可以不使用，为了格式统一元组加括号
# 元组中的元素可以是不同类型
# t3包含数字类型,字符串类型和元组类型的成员
t3 = (123, "tuple", ("hello", "中国"))

# 可以用索引访问元组成员,类似数组
print(t3[2][1])

# 元组一旦声明就不能更改且不能删除
# 元组可以以区间访问,可以用+和*运算(与字符串类似)
print(t3[1:])
print(t3 + t2)
print(t3*2)


# 列表和元组之间的转换函数 list() & tuple
print("Pet contain: ")
print(tuple(['cat', 'pig', 'parrot']))

print("Pet contain: ")
print(list( ('cat', 'pig', 'parrot') ))
