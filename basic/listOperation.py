#!/usr/bin/python3

# 列表常用操作方法：

a = [1]
# append(x):将元素x插入到列表最后
a.append('h')
print(a)

# insert(i, x):在索引i处插入元素x
a.insert(0,'b')
print(a)

# remove(x):删除列表中第一次出现的元素x
c.remove(1)
print(c)

# pop(i):取出列表中索引为i处的元素，并删除它
elem = a.pop(0)
print("elem =", elem)
print("a =", a)

# sort():将列表元素排序
b = ['a','c','b','f']
b.sort()
print(b)

# reverse():反转列表元素
a.reverse()
print(a)

# index(x):返回第一次出现x的索引值
print("b.index(f) =", b.index('f'))

# count(x):返回元素x在列表中的数量
c = [1,1,2,2,2]
print("c.count(2) =", c.count(2))
