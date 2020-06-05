#!/usr/env python

'''
Write a program which accepts a sequence of comma separated 4 digit
binary numbers as its input and then check whether they are divisible
by 5 or not. The numbers that are divisible by 5 are to be printed 
in a comma separated sequence.
'''

nums = [n for n in input("input nums:").split(',')]
ret_nums = []

for num in nums:
    tmp = int(num, 2)
    if tmp % 5 == 0:
        ret_nums.append(num)

print(','.join(ret_nums))

