#!/usr/bin/python3
# python 异常处理

# try: 
#   <body>
# except:
#   <body>
# excep:
#   <body>
# ...
# else:
#   <body>
# finally:
#   <body>
#
# NOTE:except中可以加上异常类型或者参数
#       无论是否发生异常finally中的语句都将被执行
try:
    fd = open("/home/bill/ioTest.txt", "w")
    fd.write("This is a test!")
except IOError:
    print("open() orror!")
else:
    print("Write successfully!")
    fd.close()