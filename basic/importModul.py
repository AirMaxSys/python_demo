#!/usr/bin/python3

# python3 two way to import module

# import <M>
# from <M> import *     -> directe using function name

import random
from sys import *



# diference of range(10), range(0, 10), range(0, 10, 1)
for i in range(10):
    print(i, end = " ")
print()

print("---------cut line---------")
for i in range(0, 10):
    print(i, end = " ")
print()

print("---------cut line---------")
for i in range(0, 10, 1):
    print(i, end = " ")
print()


for i in range(5):
    print(random.randint(1, 100), end = " ")
print()

while True:
    print("Plz input exit to end programe: ", end = "")

    if input() == 'exit':
        exit()  # sys.exit()
        # end !
        print("P end")
