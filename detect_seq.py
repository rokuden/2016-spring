# -*- coding: utf-8 -*-

import cv2
import cv
from datetime import datetime


cap = cv2.VideoCapture(1)
imwidth=cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
imheight=cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
cascade = cv2.CascadeClassifier('cascade.xml')#分類器の指定

print 'img width %d height %d ' % (imwidth,imheight)

while(True):
    # フレームをキャプチャする
    ret, frame = cap.read()
    t = datetime.now().strftime("%Y%m%d%H%M%S")

    roomba = cascade.detectMultiScale(frame, 1.1, 3)#物体検出

    for (x, y, w,h) in roomba:
		print x, y, w, h
		center = (int(x+w/2), int(y+h/2))
		radius = int(w/2+5)
		cv2.circle(frame, center, radius, cv.RGB(255, 20, 147), thickness = 3) #円の描画
	# 画面に表示する
    cv2.imshow('frame',frame)

    #マウスイベントを取得する
    def onMouse(event, x, y, flag, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            print (x,y), "click"
    cv2.setMouseCallback('frame', onMouse)

    # キーボード入力待ち
    key = cv2.waitKey(1) & 0xFF

    # qが押された場合は終了する
    if key == ord('q'):
        break
    # sが押された場合は保存する
    if key == ord('s'):
        path = "photo"+t+".jpg"
        cv2.imwrite(path,frame)
        print "captured!"

# キャプチャの後始末と，ウィンドウをすべて消す
cap.release()
cv2.destroyAllWindows()
