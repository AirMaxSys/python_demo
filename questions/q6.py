#!/bin/env python

'''
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
'''

from math import sqrt
c = 50
h = 30
q = []
items = [x for x in input("plz input numbers:").split(',')]
for d in items:
  q.append(str(round(sqrt((2*c*int(d))/h))))

print(','.join(q))