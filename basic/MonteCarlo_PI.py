#!/usr/bin/python3
# 蒙特卡洛(Mont Carlo)方法计算PI

import random
import math
import time
DARTS = 10000
hits = 0000
time.clock()
for i in range(1, DARTS):
    x, y = random.random(), random.random()
    dist = math.sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("PI的值是%s" % pi)
print("程序运行时间是%-5.5ss" % time.clock())
