# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 07:34:45 2025

@author: lizet
"""
#practica 2
import  cv2
img = cv2.imread('img.jpg')
img2 = img.copy()#Para poder generar una copia de la imagen original

#Operaciones Basicas para las imagenes 
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)#Cambiar el tamaño a la imagen original 
cv2.imwrite('imgpeque.jpg', img)#guarda la imagen 
cv2.namedWindow(' ventana',img)#creacmos una veentana para la imagen 
cv2.imshow('ventanaOrinigal',img2)#mostramos la imegen de la ventana 

cv2.waitKey(0)
cv2.destroyAllWindows()  #Simpre tienen que ir al final 

