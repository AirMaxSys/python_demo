#!/usr/bin/python3
# 求文件中数字的平均值
# file path: ./average.txt

fn = "average.txt"
def creatFile():
    fd = open(fn, "w")
    fd.write("1,2,3,4,5\n")
    fd.write("2,3,4,5,6\n")
    fd.close()
def average():
    try:
        fd = open(fn, "r")
        sum = 0.0
        count = 0
        line = fd.readline()
        while line != "":
            for str in line.split(","):
                sum += eval(str)
                count += 1
            line = fd.readline()
        print("average is:", sum/count)
    except IOError:
        print("File limits of authority.")
    finally:
        fd.close()
creatFile()
average()