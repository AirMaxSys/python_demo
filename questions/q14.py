#!/bin/env python

'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
'''

low_cnt = 0
upp_cnt = 0

sen = input("input:")

for s in sen:
    if s.isupper():
        upp_cnt += 1
    elif s.islower():
        low_cnt += 1
    else:
        pass
print(f"UPPER CASE:{upp_cnt}\nLOWER CASE:{low_cnt}")

