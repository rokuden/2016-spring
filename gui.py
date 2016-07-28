# coding:utf-8


import cv
import cv2
from control import *
from datetime import datetime


if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    imwidth=cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    imheight=cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
    cascade = cv2.CascadeClassifier('cascade.xml')
    #print cascade
    mouse_handle = MouseHandler(0, 0)

    while(True):
        ret, frame = cap.read()
        t = datetime.now().strftime("%Y%m%d%H%M%S")

        roomba = cascade.detectMultiScale(frame, 1.1, 3)
        #print roomba

        for (x, y, w, h) in roomba:
            center = (int(x+w/2), int(y+h/2))
            radius = int(w/2+5)
            cv2.circle(frame, center, radius, cv.RGB(255, 20, 147), thickness = 3)

        # 画面に表示する
        cv2.imshow('frame',frame)
        #print center, radius
        xcenter = int(x+w/2)
        ycenter = int(y+h/2)
        mouse_handle.xcenter = xcenter
        mouse_handle.ycenter = ycenter
        cv2.setMouseCallback('frame', mouse_handle.onMouse)

        # キーボード入力待ち
        key = cv2.waitKey(1) & 0xFF

        # qが押された場合は終了する
        if key == ord('q'):
            subprocess.call(["ssh","nagumo","logout"])
            break

        # sが押された場合は保存する
        if key == ord('s'):
            path = "photo"+t+".jpg"
            cv2.imwrite(path,frame)
            print "captured!"

    # キャプチャの後始末と，ウィンドウをすべて消す
    cap.release()
    cv2.destroyAllWindows()
