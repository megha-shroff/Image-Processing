# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:58:28 2022

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
        for i in range(48,68):
            cv.circle(frame,(int(pred.part(i).x),int(pred.part(i).y)),2,(0,0,255),-1)   # -1 means solid points , if we remove that then only circle will be displayed
            cv.putText(frame,str(i),(int(pred.part(i).x),int(pred.part(i).y)),cv.FONT_HERSHEY_SIMPLEX,0.3,(0,114,114),1)         # image , text , where ? (points), fonts , size, color , thickness
            i += 1
            
        x1 = pred.part(51).x
        y1 = pred.part(51).y
        
        x2 = pred.part(57).x
        y2 = pred.part(57).y
        
        print(abs(x1-x2) , abs(y1-y2))
        
        if(abs(y1-y2) > 55 ):
            # print(abs(x1-x2) > 6 ,'Open')
            cv.putText(frame,"Yawning",(40,80),cv.FONT_HERSHEY_SIMPLEX,3,(255,70,220),2)         # image , text , where ? (points), fonts , size, color , thickness
        else:
            # print(abs(x1-x2) , 'Close')
            cv.putText(frame,"Normal",(40,80),cv.FONT_HERSHEY_SIMPLEX,3,(100,70,220),2)         # image , text , where ? (points), fonts , size, color , thickness
            
        cv.imshow('detect',frame)
    except:
        cv.putText(frame,"Face not detect",(40,80),cv.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
        cv.imshow('detect',frame)
        
    key = cv.waitKey(3)        #if 0 then you have continuosly press any key to see the video working, instead write any other thing than 0
    
    if(key == 27): # when you press esc program will quit  #   esc - 27, enter - 13
        cv.destroyAllWindows()
        break
camera.release()
