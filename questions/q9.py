#!/usr/env python

'''
Write a program that accepts sequence of lines as input and prints the lines 
after making all characters in the sentence capitalized.
'''

lines = []
while True:
    line = input("input:")
    if line:
        lines.append(line.upper())
    else:
        break;
        
for i in lines:
    print(i)
