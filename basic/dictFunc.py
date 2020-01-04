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

print('--------------------------------------------------')

# 字典中的get()和setdefault()方法
# 检测键是否存在于字典当中，存在返回键对应的值，不存在返回传递给get函数的第二个参数
w_length = {
    "hello" : 5,
    "world" : 5,
    "all"   : 3,
    "communicate"   : 11,
    "target"        : 6    
}

if w_length.get("shrimp", 0) == 0:
    print("\"shrimp\" is not in dict!")

if(w_length.get("hello", 0) == w_length["hello"]):
    print("\"hello\" is in dict!")

print('--------------------------------------------------')

# setdefault()方法
# 用于检测键是否在字典中，若在返回字典中的值，若不则将传入setdefault()方法的第二个参数
# 用于第一个参数的值并且添加到列表中
broad_info = {
    "lcd" : True, 
    "multiKeys" : False,
    "wi-fi" : True,
    "debuger" : True,
    "leds" : True,
    "co2 sensor" : False            
}

print(broad_info.setdefault("lcd", False) )
print(broad_info.setdefault("exterl flash", True))
print(broad_info)
