#!/bin/env python

'''
Write a program which can compute the factorial of a given numbers.
'''

'''
def comp_fact(tmp):
  if tmp == 0:
    return 1
  multi = 1
  while tmp >= 1:
    multi *= tmp
    tmp -= 1
  return multi
'''

def comp_fact(num):
  if num==0:
    return 1
  return num*comp_fact(num-1)

num = int(input("plz input a number:"))

print(f"{num} factorial is:{comp_fact(num)}")
