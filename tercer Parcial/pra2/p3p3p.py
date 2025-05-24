# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 07:48:59 2025

@author: lizet
"""

import cv2
import numpy as np

c = 0

camara = cv2.VideoCapture('rojo.mp4')
while(camara.isOpened()):
    ret, frame = camara.read()
    if ret == True:
        img  = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        azulclaro = np.array([100,100,20], np.uint8)
        azuloscuro = np.array([125,255,255], np.uint8)
        mascara = cv2.inRange(img, azulclaro, azuloscuro)
        seleccion = cv2.bitwise_and(img, img, mask=mascara)
        seleccion[mascara>0]=(255,255,255)
        cv2.namedWindow('cambio',cv2.WINDOW_NORMAL)
        cv2.imshow('cambio',seleccion)
        cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
        cv2.imshow('frame',frame)
        if cv2.waitKey(30) == ord('a'):
            break
        if cv2.waitKey(30) == ord('g'):
            cv2.imwrite(frame, 'img'+str(c)+'.jpg')
            c+=1
    else:
        break
camara.release()
cv2.destroyAllWindows()