#!/usr/env python

net = 0

while True:
    s = input()
    if not s:
        break
    val = s.split(' ')
    op,cnt = val[0],int(val[1])
    if op == "D":
        net += cnt
    elif op == "W":
        net -= cnt
    else:
        pass
print(net)
    
