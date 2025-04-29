# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 07:39:07 2025

@author: lizet
"""
#practica7

import cv2 
img = cv2.imread('img.jpg')
#Para mostrar los colores en RGB   
#B,G,R= cv2.split(img)#Divimos los canales de RGB 

img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HV)
H,S,V = cv2.split(img2)

cv2.imshow('H',cv2.WINDOW_NORMAL)
cv2.imwrite('H', img)#guarda la imagen 

cv2.imshow('S',cv2.WINDOW_NORMAL)
cv2.imwrite('S', img)#guarda la imagen 

cv2.imshow('R',cv2.WINDOW_NORMAL)
cv2.imwrite('R', img)#guarda la imagen 






#cv2.imshow('B',cv2.WINDOW_NORMAL)
#cv2.imwrite('B', img)#guarda la imagen 

#cv2.imshow('G',cv2.WINDOW_NORMAL)
#cv2.imwrite('G', img)#guarda la imagen 

#cv2.imshow('R',cv2.WINDOW_NORMAL)}
#cv2.imwrite('R', img)#guarda la imagen e la muestra 

cv2.imshow('original',cv2.WINDOW_NORMAL)
cv2.imwrite('original ', img)#guarda la imagen 
cv2.waitKey(0)#Siempre tien e  que estar  estos dos  
cv2.destroyAllWindows()