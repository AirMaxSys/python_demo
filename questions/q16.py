#!/usr/env python

'''
Use a list comprehension to square each odd number in a list. The list is 
input by a sequence of comma-separated numbers.
'''

nums = [n for n in input("nums:").split(',') if int(n) % 2 == 1]
print(','.join(nums))
