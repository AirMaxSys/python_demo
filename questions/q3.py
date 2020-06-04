#!/bin/env python

'''
With a given integral number n, write a program to generate a
dictionary that contains (i, i*i) such that is an integral number 
between 1 and n (both included). and then the program should print 
the dictionary.
'''
n_dict={}
n = int(input("plz input number(1~n):"))
for i in range(1, n + 1):
  n_dict[i] = i*i

print(n_dict)
