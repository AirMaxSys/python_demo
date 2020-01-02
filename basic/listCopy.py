#!/bin/python3

# 列表和字典在传递给函数时若不希望其值改可使用python内建的copy模块

import copy

def copy_menu(menu):
    __menu = copy.copy(lunch_menu)
    __menu.remove('juice')
    return __menu

def deepcopy_menu(menu):
    __menu = copy.deepcopy(menu)
    __menu.remove('beef')
    return __menu

def show_list(m_list):
    for i in range(len(m_list)):
        print(m_list[i], end = ' ')
    print()

lunch_menu = ['rice', 'beef', 'pork', 'juice']

show_list(lunch_menu)
print("--------------------")
dinner_menu = copy_menu(lunch_menu)
print("This is lunch menu:")
show_list(lunch_menu)
print("--------------------")
print("This is dinner menu:")
show_list(dinner_menu)
print("--------------------")

# copy.deepcopy()深拷贝将列表中的列表也一起拷贝

lunch_menu.append(['apple', 'peer'])
dinner_menu = deepcopy_menu(lunch_menu)

def show_deep_list(_menu):
    for i in range(len(_menu)):
        for j in range(len(_menu[i])):
            if type(_menu[i]) != type([]):
                print(_menu[i], end = ' ')
                break
            else:
                print(_menu[i][j], end = ' ')
        print() 
    return 0


print("This is lunch menu:")
show_deep_list(lunch_menu)
print("--------------------")
print("This is dinner menu:")
show_deep_list(dinner_menu)
print("--------------------")

deep_list = [['H', 'E', 'L', 'L', 'O', 'W'], ['L', 'O', 'V', 'E']]
show_deep_list(deep_list)
print("--------------------")

print(lunch_menu)
print(dinner_menu)
