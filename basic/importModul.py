#!/usr/bin/python3

# python3 two way to import module

# import <M>
# from <M> import *     -> directe using function name

import random
from sys import *

for i in range(5):
    print(random.randint(1, 100), end = " ")
print()

while True:
    print("Plz input exit to end programe: ", end = "")

    if input() == 'exit':
        exit()  # sys.exit()
        # end !
        print("P end")
