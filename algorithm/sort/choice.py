#!/usr/bin/python3
# 选择排序

def swapTwoNum(a, b):
    return b, a

# Choice sort with descending order
def choiceSort(a):
    for i in range(len(a)):
        max = a[i]
        for j in a[i + 1:]:
            if(max < j):
                max = j
        # exchange
        idx = a.index(max)
        a[i], a[idx] = a[idx], a[i]

a = [15, 60, 22, 100, 81, 90, 27, 102, 2.5e100]
choiceSort(a)
print("a[] = ", a)

