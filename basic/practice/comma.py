#!/bin/python3

# 4.10.1 逗号代码

def list_formmat(m_list):
    string = ''
    list_len = len(m_list)
    
    if 0 == list_len:
        string = 'and'
    elif 1 == list_len:
        m_list.insert(0, 'and')
    else:
        m_list.insert(list_len - 2, 'and')

    # update list len
    list_len = len(m_list)

    for i in range(list_len):
        if m_list[i] == 'and':
            string = string + m_list[i] + ' '
        elif i == list_len - 1:
            string += m_list[i]
        else: 
            string = string + m_list[i] + ', '

    return string

name = ['anni', 'guigui', 'xiaxia']
string = list_formmat(name)
print(string, end = '')

print()
foo=['he']
string = list_formmat(foo)
print(string, end = '')

print()
foo=[]
string = list_formmat(foo)
print(string, end = '')
