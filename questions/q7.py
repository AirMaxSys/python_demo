#!/usr/env python

'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
'''

input_str = input("plz input(x,y):")

x = int(input_str.split(',')[0])
y = int(input_str.split(',')[1])

arr = [[0 for i in range(y)] for j in range(x)]

for i in range(x):
  for j in range(y):
    arr[i][j] = i * j

print(arr)
