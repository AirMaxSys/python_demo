#!/usr/bin/python3
# python random libary:
# NOTE:需要导入random库
import random

# seed(x): 给随机数一个种子值，默认随机种子是系统时钟
random.seed()
# random():生成一个[0, 1.0]之间的随机小数
print("使用整数生成的随即数", random.random())
# uniform(a,b):生成一个a到b之间的随机小数
print("uniform(1,10):", random.uniform(1, 10))
# randint(a,b): 生成一个a到b之间的随机整数
print("randint(1, 100):", random.randint(1,100))
# randrange(a,b,c): 随机生成一个从a开始到b以c递增的数
print("randrange(1, 100, 10):", random.randrange(1, 100, 10))
# choice(<list>): 从列表中随机返回一个元素
a = ["doufu", "boluo", "huolongguo","caiji"]
print("choice(a):", random.choice(a))
# shuffle(<list>): 将列表中的元素随机打乱
print("a[]=", a)
print("shuffle(a):", random.shuffle(a))
# sample(<list>, k): 从指定列表随机获取k个元素
print("sample(a, 2):", random.sample(a,2))