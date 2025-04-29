# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Practica 1 
import  cv2
img = cv2.imread('img.jpg')
print(img)  #ectura de imagen 

imagen_gris = cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE)
imgen_gris =cv2.imread('img.jpg',0) #Convcierte a escala de grises 
print(imagen_gris)

cv2.namedWindow(' original', cv2.WINDOW_NORMAL)#creacmos una veentana para la imagen 
cv2.imshow('original',img)#mostramos la imegen de la ventana 
cv2.namedWindow('imagengris', cv2.WINDOW_NORMAL)
cv2.imshow('imagengris',imagen_gris)
cv2.imwrite('gris.jpg', imgen_gris)#guarda la imagen 

cv2.waitKey(0)
cv2.destroyAllWindows()  #Simpre tienen que ir al final 




