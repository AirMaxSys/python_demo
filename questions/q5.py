#!/bin/env python

'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
'''

class Mstr():
  def __init__(self):
    self.s = ""

  def getString(self):
    self.s = input("plz input str:")
  
  def printString(self):
    print(self.s.upper())

mstr = Mstr()
mstr.getString()
mstr.printString()
