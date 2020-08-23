# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:39:57 2019

@author: Prithvi
"""

import numpy as np
import cv2
import math

cap = cv2.VideoCapture(0)
olist = []
blist = []
glist = []
wlist = []

ops = ["Clear","Orange","Blue","Green","White"]
color = (0,0,255)

while (True):
    
    
    
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    x1 = y1 = w1 = h1 = 0
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([99,115,150])
    upper_blue = np.array([110,255,255])

    mask = cv2.inRange(hsv,lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    flag = 0
    
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours :
        pass
    else :
        cont_sorted = sorted(contours, key=cv2.contourArea, reverse=True)#[:5]
        M = cv2.moments(cont_sorted[0])
        flag = 1
    
    
    
    
   
   # calculate x,y coordinate of center
    if flag == 1:
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
        # set values as what you need in the situation
            cX, cY = 0, 0
        if cY > 95 :#and cY > 70 : 
            if color == (0,165,255) :
                olist.append((cX,cY))
            elif color == (255,0,0) :
                blist.append((cX,cY))
            elif color == (0,255,0) :
                glist.append((cX,cY))
            elif color == (255,255,255) :
                wlist.append((cX,cY))
            else :
                pass
                
       
    for x in olist:    
        cv2.circle(frame, (x[0], x[1]), 5, (0,165,255), -1)
    for x in blist:    
        cv2.circle(frame, (x[0], x[1]), 5, (255,0,0), -1)
    for x in glist:    
        cv2.circle(frame, (x[0], x[1]), 5, (0,255,0), -1)
    for x in wlist:    
        cv2.circle(frame, (x[0], x[1]), 5, (255,255,255), -1)    
        
    
    
    x = 30
    y = 20
    w = 120
    h = 60
    
    for i in range(5) :
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,ops[i],(x+8,y+30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        cx = (int)((2*x+w)/2.0)
        cy = (int)((2*y+h)/2.0)
        if (math.sqrt((cX - cx)**2 + (cY - cy)**2))<30 :
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),8)
            if i==0 :
                 olist = []
                 blist = []
                 glist = []
                 wlist = []
            elif i== 1 :
                color = (0,165,255)
            elif i==2 :
                color = (255,0,0)
            elif i==3 :
                color = (0,255,0)
            else :
                color = (255,255,255)
        x = x+w
    
    cv2.imshow('myBoard',frame)
    #cv2.imshow('jj',black_img)
    #cv2.imshow('frame',frame)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

    
