

import cv2
import numpy as np
import time


def draw_rect(event, x, y, flags, param): #Q2 - modify MousePosition.py
    global ix, iy, jx, jy
    if event == cv2.EVENT_LBUTTONDOWN:
        ix = x
        iy = y
        print(ix)
    
    elif event == cv2.EVENT_LBUTTONUP:
        jx = x
        jy = y
        cv2.rectangle(param, pt1=(ix,iy), pt2=(jx, jy),color=(255,0,255),thickness=3)
        

img_name = 'TestImages/UnderExposedPortrait.jpg'

img = cv2.imread(img_name)
cloneImg = img.copy()
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rect, cloneImg) #display window

while (1):
    cv2.imshow('image',cloneImg)
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break
    elif k == ord('c'):
        J = img[iy:jy, ix:jx]
    elif k == ord('h'):
        bonus = J #copy ROI for bonus
        cloneImg_bns = cloneImg
        imgYCC = cv2.cvtColor(bonus, cv2.COLOR_BGR2YCR_CB) #convert

        yImg = imgYCC[:,:,0] #get y channel

        y_eq = cv2.equalizeHist(yImg)

        imgYCC[:,:,0] = y_eq

        imgYCC = cv2.cvtColor(imgYCC, cv2.COLOR_YCR_CB2BGR)

        #get b, g, r channels
        bImg = J[:,:,0]
        gImg = J[:,:,1]
        rImg = J[:,:,2]

        #equalize each channel 
        r_eq = cv2.equalizeHist(rImg)
        J[:,:,2] = r_eq

        g_eq = cv2.equalizeHist(gImg)
        J[:,:,1] = g_eq

        b_eq = cv2.equalizeHist(bImg)
        J[:,:,0] = b_eq

        #replace ROI with equalization
        cloneImg[iy:jy, ix:jx] = J
        
        





cv2.destroyAllWindows() 
