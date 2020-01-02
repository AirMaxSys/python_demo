#!/bin/python3

# dict的 keys() values() items()方法
# 分别返回字典中的键、值、键-值对

wether_dict = {'today':'sunny', 'tommory':'rain','the day after tommory':'snow'}

for i in wether_dict.keys():
    print(i)

# keys()转换成列表
print(wether_dict.keys()) # key()返回的不是列表，是dict_key的类型，可以用于迭代
w_list = list(wether_dict.keys())
print(w_list)

print('--------------------------------------------------')

for i in wether_dict.values():
    print(i)

# values()转换成列表
print(wether_dict.values()) # values()返回的不是列表，是dict_values的类型，可以用于迭代
w_list = list(wether_dict.values())
print(w_list)

print('--------------------------------------------------')

for i in wether_dict.items():
    print(i)

# items()转换成元组
print(wether_dict.items())
w_tuple = tuple(wether_dict.items())
print(w_tuple)
