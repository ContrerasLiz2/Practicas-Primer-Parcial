# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 07:32:40 2025

@author: lizet
"""
#practica 5
import cv2 
img = cv2.imread('EX.jpg')

img1 = img.copy()
img1 = img.copy()
img1 =cv2.resize(img1,(720,720))


alto, ancho,_= img1.shape
print(alto,"  " ,ancho)
#arreglo y secuencia 
corte = img1[0:alto,0:int(ancho/2)]
corte2 =img1[0:alto,int(ancho/2):]

cv2.namedWindow('Ventanacorte2',cv2.WINDOW_NORMAL)
cv2.imshow('Ventanacorte2',corte2)

cv2.namedWindow('VentanaCort',cv2.NDOW_NORMAL)
cv2.imshow('Ventanacorte',corte)
 
cv2.namedWindow('Ventana',cv2.WINDOW_NORMAL)
cv2.imshow('Ventanacopia',img1)
cv2.namedWindow('Ventana',cv2.WINDOW_NORMAL)
cv2.imshow('Ventana', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Arreglos Recoremos arra=[1,2,3,4,5,6,7,8,9,10] rint(arra[5:])