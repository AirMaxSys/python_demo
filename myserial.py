#! /usr/bin/env python

# -*- coning: utf-8 -*-

import sys
import threading
import time
import serial

# Hex bytes packages
rx_buf = []
tx_sta = [b'\xFE', b'\xFF']
tx_ack = [b'\xFF', b'\xFF']

# crc8
def crcInvert(dat:int) -> int:
  tmp = 0
  for i in range(0, 8):
    if(dat & (1 << i)):
      tmp |= (1 << (7 - i))
  return tmp


def crc8(buf:list) -> int:
  crc_val, crc_ploy, tmp = 0, 0x31, 0

  for i in range(len(buf)-1):
    tmp = crcInvert(buf[i])
    crc_val ^= tmp

    for i in range(0,8):
      if(crc_val & 0x80):
        crc_val = (crc_val << 1) ^ crc_ploy
      else:
        crc_val <<= 1
  return crcInvert(crc_val) ^ 0


def tx_start():
  # starting tx package 
  ser.write(tx_sta[0])
  ser.write(tx_sta[1])
 

def tx_ack_pkg():
  ser.write(tx_ack[0])
  ser.write(tx_ack[1])


def serial_read(serial, len:int) ->list:
  p_list = []

  for i in range(len): 
    k = int.from_bytes(serial.read(), "big")
    p_list.append(k)

  return p_list


data_dict = {"vol" : 0, "cur" : 0, "temp1" : 0, "temp2" : 0, "temp3" : 0}
pkg_len = 11
crc_len = pkg_len - 1

# init open serial port
ser = serial.Serial("COM5", baudrate = 115200)

while True:
  tx_start()
  rx_buf = serial_read(ser, pkg_len)
  crc_val = crc8(rx_buf, crc_len)
  print("crc is: ", crc_val)
  
  if crc_val == rx_buf[pkg_len - 1]:
    # cp data
    data_dict["vol"] = ((rx_buf[0] << 8) & rx_buf[1]) / 100
    data_dict["cur"] = ((rx_buf[2] << 8) & rx_buf[3]) / 100
    data_dict["temp1"] = ((rx_buf[4] << 8) & rx_buf[5]) / 100 - 55
    data_dict["temp2"] = ((rx_buf[6] << 8) & rx_buf[7]) / 100 - 55
    data_dict["temp3"] = ((rx_buf[8] << 8) & rx_buf[9]) / 100 - 55

    # show
    print(data_dict)

    tx_ack_pkg()
  else:
    print("serial no data")
    sys.exit(1)

# clear
rx_buf.clear()

ser.close()

sys.exit(0)
