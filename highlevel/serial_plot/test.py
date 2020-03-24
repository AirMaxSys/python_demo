#!/usr/bin/env python

# -*- conding: utf-8 -*-

import serial

buf = ['h', 'e', 'l']
x = hex(100)
print(buf[0], "len=", len(buf), buf.index("h"))

for i in range(0,5):
  print("hhhh")


a, b = [1, 2, 3], [4, 5, 6]
print(a[0],b[1])

def serial_read(serial, len:int) ->list:
  p_list = []

  for i in range(len): 
    k = int.from_bytes(serial.read(), "big")
    p_list.append(k)

  return p_list


ser = serial.Serial("COM4", baudrate = 115200)
print(serial_read(ser, 11))

