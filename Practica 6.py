# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 08:51:46 2025

@author: lizet
"""
#practica6
import cv2 
img = cv2.imread('img.jpg')

img1 = img.copy()
img1 = img.copy()

img1 =cv2.resize(img1,(720,720))


alto, ancho,_= img1.shape
print(alto," ",ancho)
mitad = int(alto/2)
mitad2 = int(ancho/2)


#arreglo y secuencia 
corte1 = img1[0:mitad,0:mitad2]
corte2 =img1[0:mitad,mitad2:ancho]
corte3 = img1[mitad:alto,0:mitad2]
corte4 =img1[mitad:alto,mitad2:ancho]

cv2.namedWindow('corte1',cv2.WINDOW_NORMAL)
cv2.imshow('corte1',corte1)

cv2.namedWindow('corte2',cv2.NDOW_NORMAL)
cv2.imshow('corte2',corte2)
 
cv2.namedWindow('corte3',cv2.WINDOW_NORMAL)
cv2.imshow('corte3',corte3)
cv2.namedWindow('corte4',cv2.WINDOW_NORMAL)
cv2.imshow('corte4', corte4)
cv2.waitKey(0)
cv2.destroyAllWindows()