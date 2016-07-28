#coding:utf-8


import serial
import time


SLEEP = 1000
SLEEP_RATE = 0.1


ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1)

def check(ser):
    ser.write(chr(128))#start
    ser.write(chr(131))#safe mode
    ser.write(chr(142))#sensor
    ser.write(chr(7))#packet id:7(bumpers)
    r = ser.read(1)

    if ord(r) == 0:
        bs = "n" #bump state = normal
        ser.write(chr(128))#start
        ser.write(chr(131))
        ser.write(chr(145))
        ser.write(chr(00))
        ser.write(chr(250))
        ser.write(chr(00))
        ser.write(chr(250))
        time.sleep(2.0)
        ser.write(chr(145))
        ser.write(chr(0))
        ser.write(chr(0))
        ser.write(chr(0))
        ser.write(chr(0))

    elif ord(r) == 1:

        ser.write(chr(128))#start
        ser.write(chr(131))
        ser.write(chr(145))
        ser.write(chr(0))
        ser.write(chr(32))
        ser.write(chr(1))
        ser.write(chr(44))
        time.sleep(2.0)
        ser.write(chr(145))
        ser.write(chr(0))
        ser.write(chr(0))
        ser.write(chr(0))
        ser.write(chr(0))
        bs = "r" #bump state = right bump
    elif ord(r) == 2:
        bs = "l" #bump state = left bump

        ser.write(chr(128))#start
        ser.write(chr(131))
        ser.write(chr(145))
        ser.write(chr(1))
        ser.write(chr(44))
        ser.write(chr(0))
        ser.write(chr(32))
        time.sleep(2.0)
        ser.write(chr(145))
        ser.write(chr(0))
        ser.write(chr(0))
        ser.write(chr(0))
        ser.write(chr(0))
    elif ord(r) == 3:
        bs = "f" #bump state = front bump

        ser.write(chr(128))#start
        ser.write(chr(131))
        ser.write(chr(145))
        ser.write(chr(1))
        ser.write(chr(44))
        ser.write(chr(1))
        ser.write(chr(44))
        time.sleep(2.0)
        ser.write(chr(145))
        ser.write(chr(0))
        ser.write(chr(0))
        ser.write(chr(0))
        ser.write(chr(0))
    else:
        bs = "d" #wheel drop
    print "-----result------"
    print "r     :", r
    print "len(r):", len(r)
    print "type  :", type(r)
    print "ord(r):", ord(r)
    print "status", bs
    print "-----------------"
    return ord(r)


def plot_state(states):
    for s in states:
        print "#"*s


if __name__=="__main__":
    states = []
    for _ in xrange(SLEEP):
        print "count:", _
        time.sleep(SLEEP_RATE)
        r = check(ser)
        states.append(r)

    print "len(states):", len(states)
    print states
    plot_state(states)
    print "".join([chr(x) for x in states])

"""
if len(r)==0:
    print "Connection Failed(or Normal...)"
eles:
    if ord(r)==3:
        print "Normal"
    elif ord(r)==2:
        print "maybe bump left"
    elif ord(r)==1:
        print "maybe bump right"

"""

"""
# written by cozy
if ord(r)==0:
    print "ord(r)=0, normal?"
elif ord(r)==1:
    print "ord(r)=1, normal?"
else:
    print "ord(r)=%s, bump?"%ord(r)
"""
"""
if r == "0":
    print "normal"
else:
    print "bump"
"""

"""
f = open('sensor1.txt','w')

f.write(r)
f.close()
"""
