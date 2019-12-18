#!/usr/bin/python3

# 函数定义、(默认)参数、返回值
# 函数内部定义的变量是“局部变量”，函数外的变量是“全局变量”
# 局部变量的作用域通常在函数内部， 而全局变量的作用域为全局
# 变量超过的作用域时就无法再被使用，不同咋作用域中可以使用同名的相同变量

def hello(name = 'bill'):
    print("hello " + name)
    return None

def getArrMax(arr):
    max = 0
    for i in arr[0 : ]:
        if max < i:
            max = i
    return max

a = [1, 2, 3]
print("Arr max val is " + str(getArrMax(a)))

# check list element
if 1 in a:
    print("True 1 in a")

hello()
hello('jason')

