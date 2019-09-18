#!/usr/bin/python3

# python数据类型:
#   数字类型、字符串类型、元组类型、列表类型、文件类型、字典类型

# python数字类型:
#   整数类型、浮点数类型、复数类型
#   NOTE:三种数字类型的关系:整数是浮点数的特例,浮点数是复数的特例

# 整数类型:
#   十进制、二进制(0b)、八进制(0o)、十六进制(0x)
# pow(x,y)函数:计算x的y次幂(x^y)

import sys

a = 10
b = 0b1111
c = 0xff
d = 0o77
print("a =",a,"b =",b,"c =",c, "d = ",d)
print("pow(2,10) =",pow(2,10))

# 浮点数类型:
#   带有小数点及小数的数字
#   python的浮点数值范围和小数精度存在限制,这种限制与不同计算机系统有关

# 查看系统的浮点数类型限制:
print(sys.float_info)
e = 3.1415
f = 1.2e4 # 1.2*10^4
print("e = ",e,"f = ",f)

# 复数类型:
#   z=a+jb(a:实数部分,b:虚数部分;a和b都是浮点类型)
#   z.imag:虚数部分,z.real实数部分
z = 1.3+10j
print("z.imag = ",z.imag,"z.real = ",z.real)

# 三种数据类型之间的转换:
#   函数int()、float()、complex()
print("int(2.5) = ",int(2.5))
print("float(2) = ",float(2))
print("complex(4) = ",complex(4))

# 判断整数类型:
print("type(1.3+1j)",type(1.3+1j))

# 整数类型的运算:
# + - * /(除法) //(除法取整数部分) % **(x^y)
# abs(x):x的绝对值
# divmod(x, y):(同时返回x//y, x%y)
# pow(x^y)

print("3/2 = ", 3/2)
print("3//2 = ", 3//2)
print("2**3 = ", 2**3)
print("abx(-3) = ", abs(-3))
print("divmod(3,2) = ", divmod(3,2))
