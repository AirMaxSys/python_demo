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

# 'not in' list
pet = ['cat', 'pig', 'dog', 'parrot']
if 'parrot' in pet:
    print('Parrot is a kind of pet.')
else if 'tiger' not in pet:
    print('Tiger is not a kind of pet.')

# 多重赋值技巧(注意：等号左边的变量数目必须要和列表元素数目一致)
num = [0x10, 0x20, 0x30, 0x40, 0x50]
num1, num2, num3, num4, num5 = num
print(num1, num2, num3, num4, num5)

