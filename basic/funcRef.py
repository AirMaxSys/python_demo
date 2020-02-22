#!/bin/python3

# 列表和字典传递给函数时是按址传递(引用)

def foo(para):
    para.append("hello")

def show_list(m_list):
    for i in range(len(m_list)):
        print(m_list[i], end = ' ')
    print()
    
m_list = [0, 1, 2]
show_list(m_list)
foo(m_list)
show_list(m_list)

