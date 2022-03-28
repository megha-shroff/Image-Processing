# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:00:49 2022

@author: Megha Shroff
"""

import cv2 as cv
import numpy as np
import dlib

camera = cv.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')



while True :
    _ , frame  = camera.read()
    
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    try: 
        detect= detector(frame)
    
        pred = predictor(frame,detect[0])
    
        
        i= 1
        for i in range(36,48):
            cv.circle(frame,(int(pred.part(i).x),int(pred.part(i).y)),2,(0,0,255),-1)   # -1 means solid points , if we remove that then only circle will be displayed
            cv.putText(frame,str(i),(int(pred.part(i).x),int(pred.part(i).y)),cv.FONT_HERSHEY_SIMPLEX,0.3,(0,114,114),1)         # image , text , where ? (points), fonts , size, color , thickness
            i += 1
            
        x1 = pred.part(38).x
        y1 = pred.part(38).y
        
        x2 = pred.part(42).x
        y2 = pred.part(42).y
        
        x3 = pred.part(44).x
        y3 = pred.part(44).y
        
        x4 = pred.part(48).x
        y4 = pred.part(48).y
        
        if(abs(y2-y1) > 6 and abs(y3-y4) > 6):
            print(abs(y2-y1) > 6 , abs(y3-y4), 'Open')
            cv.putText(frame,"Eyes Open",(40,80),cv.FONT_HERSHEY_SIMPLEX,3,(255,70,220),2)         # image , text , where ? (points), fonts , size, color , thickness
        else:
            print(abs(y2-y1) , abs(y3-y4), 'Close')
            cv.putText(frame,"Eyes Close",(40,80),cv.FONT_HERSHEY_SIMPLEX,3,(100,70,220),2)         # image , text , where ? (points), fonts , size, color , thickness
            
        cv.imshow('detect',frame)
    except:
        cv.imshow('detect',frame)
        
    key = cv.waitKey(3)        #if 0 then you have continuosly press any key to see the video working, instead write any other thing than 0
    
    if(key == 27): # when you press esc program will quit  #   esc - 27, enter - 13
        cv.destroyAllWindows()
        break
camera.release()

 

