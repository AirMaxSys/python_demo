#!/usr/bin/env python

# -*- conding: utf-8 -*-

import serial
from serial.tools import list_ports
import platform
import sys
import os
import time

def sys_port_info() -> list:
  portinfolist = serial.tools.list_ports.comports()

  portlist = []
  for i in portinfolist:
    portlist.append(i.device)

  return portlist


def get_sys_port() -> str:
  portlist = sys_port_info()
  portliststr = ''

  for i in portlist:
    portliststr += i + " "

  usr_input = input("请输入端口号 [ " + portliststr + "]: ")
  while usr_input not in portlist:
    print("port input error!")
    usr_input = input("请输入端口号 [ " + portliststr + "]: ")

  return usr_input

# Hex bytes packages
tx_sta = [b'\xFE', b'\xFF']
tx_ack = [b'\xFF', b'\xFF']

# ser = serial.Serial(port = get_sys_port(), baudrate = 115200, timeout = 1)
ser = serial.Serial(port = get_sys_port(), baudrate = 115200)

while True:
  # tx start pkg
  ser.write(tx_sta[0])
  ser.write(tx_sta[1])

  time.sleep(1)

  # tx ack pkg
  ser.write(tx_ack[0])
  ser.write(tx_ack[1])

  time.sleep(1)

  print("pkg send!")

sys.exit(0)
