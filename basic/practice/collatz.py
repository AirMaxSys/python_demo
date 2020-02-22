#!/usr/bin/python3


def collatz(num):
    while True:
        if num % 2 == 0:
            num = num // 2
        elif num == 1:
            break
        else:
            num = 3 * num + 1
        print(num)

while True:
    try:
        collatz(int(input()))
        break
    except:
        print("Plz input a integer!")
        