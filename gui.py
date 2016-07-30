# coding:utf-8


import cv
import cv2
import numpy as np
from control import *
from datetime import datetime


def find_rect_of_target_color(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    mask = np.zeros(h.shape, dtype=np.uint8)
    mask[((h < 20) | (h > 200)) & (s > 128)] = 255
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    rects = []
    for contour in contours:
        approx = cv2.convexHull(contour)
        rect = cv2.boundingRect(approx)
        rects.append(np.array(rect))
        global rect_xcenter
        global rect_ycenter
        rect_xcenter = sx + (rect[0]+rect[3]/2)
        rect_ycenter = sy + (rect[2]+rect[3]/2)
        #print rect[0]
        #print x,"rect"
        print rect_xcenter, rect_ycenter

    return rects

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
            cv2.circle(frame, center, radius, cv.RGB(0, 0, 255), thickness = 3)
            global sx
            global sy
            sx = x - 5
            sy = y - 5
            ex = x + w + 5
            ey = y + h + 5
            roi = frame[sy:ey,sx:ex]
            rects = find_rect_of_target_color(roi)
            mouse_handle.rect_xcenter = rect_xcenter
            mouse_handle.rect_ycenter = rect_ycenter
            print center,"center"
            #print rect_xcenter, rect_ycenter

            if len(rects) > 0:
                rect = max(rects, key=(lambda x: x[2] * x[3]))
                cv2.rectangle(roi, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (0, 0, 255), thickness=2)
                cv2.imshow('red', roi)


        # 画面に表示する
        cv2.imshow('frame',frame)
        #print center, radius
        global xcenter
        xcenter = int(x+w/2)
        global ycenter
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
