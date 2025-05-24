# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 07:28:09 2025

@author: lizet
"""



import cv2

camara = cv2.VideoCapture(0)

salida = cv2.VideoWriter('Video.avi',
                         cv2.VideoWriter_fourcc(*'XVID'),
                                      20.0,(640,480))

while(camara.isOpened()):
    ret,frame = camara.read()
    if ret == True:
        frame = cv2.flip(frame,1)
        cv2.imshow('video', frame)
        salida.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break
    else:
        break
camara.release()
salida.release()
cv2.destroyAllWindows()

camara = cv2.VideoCapture('Video.avi')
while(camara.isOpened()):
    ret,frame = camara.read()
    if ret == True:
        cv2.imshow('frame',frame)
        if cv2.waitKey(30) == ord('a'):
            break
    else:
        break
camara.release()   
cv2.destroyAllWindows()    