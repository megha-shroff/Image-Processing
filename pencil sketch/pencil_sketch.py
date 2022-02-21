# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 16:26:29 2022

@author: lenovo
"""

# -*- coding: utf-8 -*-

import cv2
#import numpy as np

img = cv2.imread('E:\Image processing\photos\BTS-V.jpg')
imgr = cv2.resize(img,(600,600))

image = cv2.cvtColor(imgr,cv2.COLOR_BGR2GRAY)



#window name

cv2.namedWindow("Color Adjustments",cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Color Ajustments", (300, 300))
cv2.createTrackbar("Scale", "Color Adjustments", 0, 255,lambda x:x)
cv2.createTrackbar("Color", "Color Adjustments", 0, 255,lambda x:x)

while True :
    scale = cv2.getTrackbarPos("Scale", "Color Adjustments")
    clr = cv2.getTrackbarPos("Color", "Color Adjustments")
    
    # cv2.imshow("Original Image",imgr)
    
    inverted_gray = clr - image
    
    # cv2.imshow("Inverted Image",inverted_gray)
    
    blur_img = cv2.GaussianBlur(inverted_gray, (41,41), 0)
    
    # cv2.imshow("Blur Image",blur_img)
    
    inverted_blur = clr -  blur_img
    
    # cv2.imshow("Inverted Blur Image",inverted_blur)
    
    filtr = cv2.divide(image , inverted_blur , scale = scale)   # scr1 *scale / scr2
    cv2.imshow("Original Image",imgr)
    cv2.imshow('Pencil sketch',filtr)
    
    k = cv2.waitKey(1) # 0 means static image , 1 fordynamic performance
    if k == ord("q"):
        break
    if k == ord("s"):
        cv2.imwrite('Pencil sketch',filtr)

cv2.destroyAllWindows()

