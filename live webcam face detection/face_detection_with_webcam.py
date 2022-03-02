# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:19:03 2022

@author: Megha Shroff
"""


import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0) # 0 for default camera , 1 for camera second camera
classifier = cv.CascadeClassifier('C:\\Users\\lenovo\\Downloads\\haarcascade_frontalface_default.xml')

while True :
    _ , frame  = camera.read()
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.imshow('gray',gray)
    
    faces = classifier.detectMultiScale(gray,1.7,5)       # 1.5 scale factor , lessersize = less time for execution , 3 is the minimum neighbor
                                                            # lesser scale factor is equal to more computation. So you will see lagging on your video. We less this value to detect more face 
                                                            # minimum neighbour size  = 0 then you will see multiple rectangular on one face and false detections
                                                            # suppose you are having 2 squares on one face 'A' and 4 square on face 'B' then you set min neighbor = 4 then only face 'B' will be detected and not face 'A'
                                                            # more square means model is more confident
                                                            
    
    for x,y,w,h in faces:
        cv.rectangle(frame, (x, y), (x+w,y+h), (0,70,255),2)
         
    cv.imshow('detect',frame)
    key = cv.waitKey(3)        #if 0 then you have continuosly press any key to see the video working, instead write any other thing than 0
    
    if(key == 27): # when you press esc program will quit  #   esc - 27, enter - 13
        cv.destroyAllWindows()
        break
camera.release()
 