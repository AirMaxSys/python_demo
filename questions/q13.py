#!/usr/env python

'''
Write a program that accepts a sentence and calculate 
the number of letters and digits.
'''

sentence = input("input:")
letters = 0
digits = 0

for i in sentence:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1
    else:
        pass

print(f"LETTERS {letters}")
print(f"DIGITALS {digits}")

