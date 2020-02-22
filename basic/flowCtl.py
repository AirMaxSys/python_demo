#!/usr/bin/python3

for i in range(10):
    print("#" + str(i) + " .")
    if i == 8:
        print("Max times")
        break

j = 0
while j < 5:
    if j == 3:
        j += 1
        continue
    elif j == 4:
        print("j is 4 now")
    else:
        print("num j is " + str(j))
    j += 1

