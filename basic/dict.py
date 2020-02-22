#!/bin/python3

# 字典(dict)是可以是不同类型键-值对的的集合
# 字典以花括号声明(元组->括号     列表->中括号)

m_dict = {'bill' : 18, 'old dog' : 24, 'chicken' : 23, 'force gun' : 25}
print(m_dict)

print('bill' in m_dict)

# 字典以键(索引)来访问
print(m_dict['chicken'])

m_dict['old dog'] = 30
print(m_dict['old dog'])

m_dict['hh'] = 'hello he'
print(m_dict)
