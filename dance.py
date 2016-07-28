#coding:utf-8


import serial
import time
from vor import vor
from hinter import hinter
from rr import rr
from rl import rl
from fin import fin

vor()
hinter()
rr()
rl()

print 'key w = forward, s = back, a = left turn, d = right turn, q = finish...'

while(True):
    if __name__ == '__main__':
        input_data = raw_input('>>> ')

        if input_data == 'w':
            vor()
            print 'forward'
        elif input_data == 's':
            hinter()
            print 'back'
        elif input_data == 'a':
            rl()
            print 'left turn'
        elif input_data == 'd':
            rr()
            print 'right turn'
        elif input_data == 'q':
            fin()
            print 'finish'
            break
