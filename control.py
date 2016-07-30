# -*- coding: utf-8 -*-


import cv2
import subprocess
from datetime import datetime
import math


ROOMBA_MOVE   = "/home/pi/roomba/roomba_move.py"
ROOMBA_VOR    = "/home/pi/roomba/roomba_vor.py"
ROOMBA_RIGHT = "/home/pi/roomba/roomba_rr.py"
ROOMBA_LEFT  = "/home/pi/roomba/roomba_rl.py"
ROOMBA_STOP = "/home/pi/roomba/roomba_fin.py"
ROOMBA_RIGHT_SLOW = "/home/pi/roomba/roomba_rr_s.py"
ROOMBA_LEFT_SLOW = "/home/pi/roomba/roomba_rl_s.py"


def remote_exec(fpath):
    subprocess.call(["ssh", "nagumo", "python", fpath])

class MouseHandler:
    def __init__(self, xcenter, ycenter):
        self.xcenter = xcenter
        self.ycenter = ycenter
        self.rect_xcenter = 0
        self.rect_ycenter = 0

    def onMouse(self, event, x, y, flag, params):
        if event != cv2.EVENT_LBUTTONDOWN:
            return -1

        print (x, y), "click"
        #self.xcenter = xcenter
        #self.ycenter = ycenter

        oxleng = x - self.xcenter #モノとルンバの距離x
        oyleng = y - self.ycenter #モノとルンバの距離y
        oradians = math.atan2(oxleng, oyleng) #画面の下の線をラジアン0としてモノとルンバを結んだ線の角度ラジアン
        odigrees = math.degrees(oradians) #モノとルンバを結んだ線の角度°
        print self.xcenter ,"xcenter"

        rxleng = self.rect_xcenter - self.xcenter #ルンバの中心とルンバの先の赤マーカの距離x
        ryleng = self.rect_ycenter - self.ycenter #ルンバの中心とルンバの先の赤マーカの距離y

        print self.rect_xcenter, "rect_xcenter"
        #print rxleng, ryleng

        rradians = math.atan2(rxleng, ryleng) #ルンバの中心とルンバの先の赤マーカを結んだ線の角度ラジアン
        rdigrees = math.degrees(rradians) #同度数法°
        print rradians, "rradians",rxleng,"rxleng",ryleng,"ryleng"

        omrdegrees = odigrees - rdigrees # モノとルンバを結んだ線の角度°　−　ルンバの中心とルンバの先の赤マーカ結んだ角度°    

        if 40 >=omrdegrees > 20:
            remote_exec(ROOMBA_LEFT_SLOW)
        elif 60 >= omrdegrees > 40:
            for var in range (0,2):
                remote_exec(ROOMBA_LEFT_SLOW)
        elif 80 >= omrdegrees > 60:
            for var in range (0,3):
                remote_exec(ROOMBA_LEFT_SLOW)
        elif 100 >= omrdegrees > 80:
            for var in range (0,4):
                remote_exec(ROOMBA_LEFT_SLOW)
        elif 120 >= omrdegrees > 100:
            for var in range (0,5):
                remote_exec(ROOMBA_LEFT_SLOW)
        elif 140 >= omrdegrees > 120:
            for var in range (0,6):
                remote_exec(ROOMBA_LEFT_SLOW)
        elif 160 >= omrdegrees > 140:
            for var in range (0,7):
                remote_exec(ROOMBA_LEFT_SLOW)
        elif 180 >= omrdegrees > 160:
            for var in range (0,8):
                remote_exec(ROOMBA_LEFT_SLOW)
        elif 200 >= omrdegrees > 180:
            for var in range (0,9):
                remote_exec(ROOMBA_LEFT_SLOW)
        elif 220 >= omrdegrees > 200:
            for var in range (0,8):
                remote_exec(ROOMBA_RIGHT_SLOW)
        elif 240 >= omrdegrees > 220:
            for var in range (0,7):
                remote_exec(ROOMBA_RIGHT_SLOW)
        elif 260 >= omrdegrees > 240:
            for var in range (0,6):
                remote_exec(ROOMBA_RIGHT_SLOW)
        elif 280 >= omrdegrees > 260:
            for var in range (0,5):
                remote_exec(ROOMBA_RIGHT_SLOW)
        elif 290 >= omrdegrees > 280:
            for var in range (0,4):
                remote_exec(ROOMBA_RIGHT_SLOW)
        elif 320 >= omrdegrees > 300:
            for var in range (0,3):
                remote_exec(ROOMBA_RIGHT_SLOW)
        elif 340 >= omrdegrees > 320:
            for var in range (0,2):
                remote_exec(ROOMBA_RIGHT_SLOW)
        elif 360 > omrdegrees > 340:
            remote_exec(ROOMBA_RIGHT_SLOW)

        if oxleng^2 + oyleng^2 < 60:
            remote_exec(ROOMBA_VOR)
        elif 60 <= oxleng^2 + oyleng^2 <100:
            for var in range (0,2):
                remote_exec(ROOMBA_VOR)
        elif 100 <= oxleng^2 + oyleng^2 <140:
            for var in range (0,3):
                remote_exec(ROOMBA_VOR)
        elif 140 <= oxleng^2 + oyleng^2 <180:
            for var in range (0,4):
                remote_exec(ROOMBA_VOR)
        elif 180 <= oxleng^2 + oyleng^2 <220:
            for var in range (0,5):
                remote_exec(ROOMBA_VOR)
        elif 220 <= oxleng^2 + oyleng^2 <260:
            for var in range (0,6):
                remote_exec(ROOMBA_VOR)
        elif 260 <= oxleng^2 + oyleng^2 <300:
            for var in range (0,7):
                remote_exec(ROOMBA_VOR)
        elif 300 <= oxleng^2 + oyleng^2 <340:
            for var in range (0,8):
                remote_exec(ROOMBA_VOR)
        elif 340 <= oxleng^2 + oyleng^2 <380:
            for var in range (0,9):
                remote_exec(ROOMBA_VOR)
        elif 380 <= oxleng^2 + oyleng^2 <420:
            for var in range (0,10):
                remote_exec(ROOMBA_VOR)
        elif 420 <= oxleng^2 + oyleng^2 <460:
            for var in range (0,11):
                remote_exec(ROOMBA_VOR)
        elif 460 <= oxleng^2 + oyleng^2 <500:
            for var in range (0,12):
                remote_exec(ROOMBA_VOR)
        elif 500 <= oxleng^2 + oyleng^2 <540:
            for var in range (0,13):
                remote_exec(ROOMBA_VOR)
        elif 540 <= oxleng^2 + oyleng^2 <580:
            for var in range (0,14):
                remote_exec(ROOMBA_VOR)
        elif 580 <= oxleng^2 + oyleng^2 <620:
            for var in range (0,15):
                remote_exec(ROOMBA_VOR)
        elif 620 <= oxleng^2 + oyleng^2 <660:
            for var in range (0,16):
                remote_exec(ROOMBA_VOR)
        elif 660 <= oxleng^2 + oyleng^2 <700:
            for var in range (0,17):
                remote_exec(ROOMBA_VOR)
        elif 700 <= oxleng^2 + oyleng^2 <740:
            for var in range (0,18):
                remote_exec(ROOMBA_VOR)
        elif 740 <= oxleng^2 + oyleng^2 <780:
            for var in range (0,19):
                remote_exec(ROOMBA_VOR)
        elif 780 <= oxleng^2 + oyleng^2 <820:
            for var in range (0,20):
                remote_exec(ROOMBA_VOR)
        elif 820 <= oxleng^2 + oyleng^2 <860:
            for var in range (0,21):
                remote_exec(ROOMBA_VOR)
        elif 860 <= oxleng^2 + oyleng^2 <900:
            for var in range (0,22):
                remote_exec(ROOMBA_VOR)
        elif 900 <= oxleng^2 + oyleng^2 <940:
            for var in range (0,23):
                remote_exec(ROOMBA_VOR)
        elif 940 <= oxleng^2 + oyleng^2 <980:
            for var in range (0,24):
                remote_exec(ROOMBA_VOR)
        elif 980 <= oxleng^2 + oyleng^2 <1020:
            for var in range (0,25):
                remote_exec(ROOMBA_VOR)
        elif 1020 <= oxleng^2 + oyleng^2:
            for var in range (0,26):
                remote_exec(ROOMBA_VOR)






        """while abs(odigrees - rdigrees) > 10:
            print odigrees, rdigrees
            print abs(odigrees - rdigrees)
            
            remote_exec(ROOMBA_RIGHT_SLOW)
            print odigrees, rdigrees
            print abs(odigrees - rdigrees)

        while oxleng^2 + oyleng^2 > 90:
            remote_exec(ROOMBA_VOR)"""

        print "I am in class method 'onMouse'! and rect_xcenter is%s and rect_ycenter is %s"%(self.rect_xcenter, self.rect_ycenter)

        remote_exec(ROOMBA_MOVE)
        remote_exec(ROOMBA_STOP)

