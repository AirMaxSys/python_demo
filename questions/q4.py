#!/bin/env python

'''
Write a program which accepts a sequence of comma-separated 
numbers from console and generate a list and a tuple which 
contains every number.
'''

num_list = input("input numbers:").split(",")
num_tuple = tuple(num_list)
print(num_list)
print(num_tuple)
