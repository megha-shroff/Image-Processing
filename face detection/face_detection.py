# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 17:20:29 2022

@author: lenovo
"""


# import cv2

# face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #Note the change

# img = cv2.imread('E:\Image processing\photos\BTS-V.jpg')
# gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,minNeighbors=5)

# for x, y, w, h in faces:
#     img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

# resized=cv2.resize(img,(int(img.shape[1]/3), int(img.shape[0]/3))) 

# cv2.imshow("Deteced-face",resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
#import numpy as np

img = cv2.imread('E:\\Image processing\\photos\\manu.jpg')
imgr = cv2.resize(img,(600,600))

image = cv2.cvtColor(imgr,cv2.COLOR_BGR2GRAY)

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #Note the change

print(face_cascade)

faces  = face_cascade.detectMultiScale(image , scaleFactor  = 1.05 , minNeighbors = 5)

print(faces)

for x, y, h, w in faces :
    imgr= cv2.rectangle(imgr, (x,y), (x+w,y+h), (0,255,0),3)

# cv2.imshow("Original Image",imgr)

# cv2.waitKey(2000) # 0 means static image , 1 fordynamic performance

cv2.imshow('Detect Image',imgr)

cv2.waitKey(0)

cv2.destroyAllWindows()