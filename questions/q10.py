#!/usr/env python

'''
Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them alphanumerically.
'''

words = [w for w in input("input words:").split(' ')]
print(','.join(sorted(list(set(words)))))
