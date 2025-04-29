# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 08:18:30 2025

@author: lizet
"""


import cv2 
img = cv2.imread('img.jpg') 
img2 = img.copy() #Copia de la imgen 

corte1 = cv2.selectROI("corte1",img2)#Generamos un corte  haciendo referencia a la imagen copiada 
#Para poder cortar las imagenes 
imagencorte1 = img2[int(corte1[1]):int(corte1[1]+corte1[3]), int(corte1[0]):int(corte1[0]+corte1[2])]

corte2 = cv2.selectROI("corte2",img2)#Generamos un corte  haciendo referencia a la imagen copiada 
#para mostrar mas cortes
imagencorte2 = img2[int(corte2[1]):int(corte2[1]+corte2[3]), int(corte2[0]):int(corte2[0]+corte2[2])]
cv2.namedWindow('corte2',cv2.WINDOW_NORMAL)
cv2.imshow('corte2',imagencorte1)
cv2.imwrite('corte2.jpg', imagencorte1)#guarda la imagen 

#imgcorte1 = cv2.imwrite("corte1.jpg",imagencorte1)                  
cv2.namedWindow('corte1',cv2.WINDOW_NORMAL)
cv2.imshow('corte1',imagencorte1)
cv2.imwrite('corte1.jpg', imagencorte1)#guarda la imagen 
cv2.namedWindow('original',cv2.WINDOW_NORMAL)
cv2.imshow('original',img)
 
cv2.waitKey(0)#Siempre tien e  que estar  estos dos  
cv2.destroyAllWindows()