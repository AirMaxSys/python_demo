#!/usr/env python

'''
Write a program that accepts a comma separated sequence of words as input and 
prints the words in a comma-separated sequence after sorting them alphabetically.
'''

words = [x for x in input("input words:").split(',')]
print(words)
words.sort()
print(','.join(words))

