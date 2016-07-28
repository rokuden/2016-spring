# -*- coding: utf-8 -*-


import cv2
import subprocess
from datetime import datetime
import time


ROOMBA_MOVE   = "/home/pi/roomba/roomba_move.py"
ROOMBA_VOR    = "/home/pi/roomba/roomba_vor.py"
ROOMBA_RIGHT = "/home/pi/roomba/roomba_rr.py"
ROOMBA_LEFT  = "/home/pi/roomba/roomba_rl.py"
ROOMBA_STOP = "/home/pi/roomba/roomba_fin.py"


def remote_exec(fpath):
    subprocess.call(["ssh", "nagumo", "python", fpath])

class MouseHandler:
    def __init__(self, xcenter, ycenter):
        self.xcenter = xcenter
        self.ycenter = ycenter

    def onMouse(self, event, x, y, flag, params):
        if event != cv2.EVENT_LBUTTONDOWN:
            return -1

        print (x, y), "click"

        if self.xcenter > x + 100:
            subprocess.call(["ssh","nagumo","python","/home/pi/roomba/roomba_rr.py"])
            while (True):
                if ycenter > y + 100:
                    remote_exec(ROOMBA_VOR)
                    break

                elif ycenter < y - 100:
                    remote_exec(ROOMBA_LEFT)
                    remote_exec(ROOMBA_LEFT)
                    remote_exec(ROOMBA_VOR)
                    break

                elif y - 100 <= self.xcenter <= y + 100:
                    remote_exec(ROOMBA_MOVE)
                    time.sleep(5.0)
                    remote_exec(ROOMBA_STOP)
                    break

        elif self.xcenter < x - 100:
            remote_exec(ROOMBA_LEFT)
            while (True):
                if self.ycenter > y + 100:
                    remote_exec(ROOMBA_VOR)
                    break

                elif self.ycenter < y - 100:
                    remote_exec(ROOMBA_LEFT)
                    remote_exec(ROOMBA_LEFT)
                    remote_exec(ROOMBA_VOR)
                    break

                elif y - 100 <= self.xcenter <= y + 100:
                    remote_exec(ROOMBA_MOVE)
                    time.sleep(5.0)
                    remote_exec(ROOMBA_STOP)
                    break

        elif x - 100 <= self.xcenter <= x + 100:
            while (True):
                if self.ycenter > y + 100:
                    remote_exec(ROOMBA_VOR)
                    break

                elif self.ycenter < y - 100:
                    remote_exec(ROOMBA_LEFT)
                    remote_exec(ROOMBA_LEFT)
                    remote_exec(ROOMBA_VOR)
                    break

                elif y - 100 <= self.xcenter <= y + 100:
                    remote_exec(ROOMBA_MOVE)
                    time.sleep(5.0)
                    remote_exec(ROOMBA_STOP)
                    break

        return 0;
