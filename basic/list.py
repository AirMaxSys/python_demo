#!/usr/bin/pyton3
# 列表类型:列表是有序的元素集合
# 列表元素可以通过索引访问
a = [1,2,3,4,5,6,7,8,9,0]
print(a[1:])
print(a)

# 列表中的每个元素可以是不同类型
# 与元组不同列表没有大小限制可以修改
a[-1] = 10
print(a)

# 列表基本操作：
#   +:连接两个列表
print(a + ['h','e','l','l','o'])
#   *:列表重复N次
print(a*2)
#   len():列表中元素的个数
print("len(a[2:]) =",len(a[2:]))
#   for循环遍历列表
for var in a:
    print(var, end='')
print()
#   <expr> in <list>:检查<expr>是否在列表中
print("hello" in a)