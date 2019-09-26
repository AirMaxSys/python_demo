#!/usr/bin/python3
# while 循环:计算输入平均数
# eval():函数执行字符串表达式，并返回结果结果

def main():
    sum = 0.0
    s = input("请输入数字：")
    x = s.split(' ')
    for i in range(len(x)):
        sum += int(x[i])
    print("平均数:", sum/i)

main()

