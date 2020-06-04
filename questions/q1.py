#!/bin/env python

'''
Find all such numbers which are divisible by 7 but are not a 
multiple of 5,between 2000 and 3200 (both included).
'''

num_list=[]
for num in range(2000, 3201):
  if num%7==0 and num%5!=0:
    num_list.append(str(num))

cnt = 1
for i in num_list:
  if cnt != len(num_list):
    print(str(i) + ',', end='')
  else:
    print(str(i), end='')
  cnt += 1
