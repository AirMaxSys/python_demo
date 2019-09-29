#!/usr/bin/python3
# Bubble sort with python3
# 分片：
# [s:j:k]-->s 起始 
#           j 结尾(不包括j元素)
#           k 步长
# reange(s, j, k) 同上

def Bubble(a):
    for i in range( len(a) ):
        # for j in range( -1, i-len(a), -1):
        for j in range( len(a) - 1, i, -1):
            # print("%2d " % a[j] , end='')
            if(a[j] > a[j - 1]):
                # Exchange
                a[j], a[j - 1] = a[j - 1], a[j]
        # print()

a = [12, 3, 6, 7, 0, 23]
Bubble(a)
print("Bubble sort: a[] = ", a)