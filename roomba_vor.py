#coding:utf-8


import serial
import time


ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1)


ser.write(chr(128))#start
ser.write(chr(131))#safe mode
ser.write(chr(146))#drive PWM
ser.write(chr(0))#R PWM HIGH
ser.write(chr(255))#R PWM LOW
ser.write(chr(0))#L PWM HIGH
ser.write(chr(255))#L PWM LOW

time.sleep(0.5)

ser.write(chr(145))
ser.write(chr(0))
ser.write(chr(0))
ser.write(chr(0))
ser.write(chr(0))
ser.close()
