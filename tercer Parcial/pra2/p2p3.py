# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 08:29:18 2025

@author: lizet
"""

'''
     Colores base de RGB 
   
    rojo claro 0,100,20
   rojo oscuro 5,255,255
   
   rojo2 claro  175,100,20
   rojo oscuro 179,255,255
   
   verde claro 25,20,20
   verde oscuro 100,255,255
   
   axul claro 100,100,20
   azul oscuro 125,255,255
   
   
'''


import cv2
import numpy as np 

# Cargar la imagen
img = cv2.imread('R.JPEG')

# Verificar si la imagen se cargó correctamente
if img is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Convertir la imagen a espacio de color HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Definir los rangos de color verde en HSV
verde_claro = np.array([25, 20, 20], np.uint8)
verde_oscuro = np.array([100, 255, 255], np.uint8)

# Crear una máscara para los tonos de verde
mascara = cv2.inRange(img_hsv, verde_claro, verde_oscuro)

# Crear un kernel para operaciones morfológicas
kernel = np.ones((7, 7), np.uint8)

# Aplicar transformaciones morfológicas para mejorar la máscara
mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)

# Aplicar la máscara a la imagen original
seleccion = cv2.bitwise_and(img, img, mask=mascara)

# Encontrar contornos en la máscara
contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos en la imagen original
cv2.drawContours(img, contornos, -1, (0, 255, 0), 2)



# Mostrar las imágenes procesadas
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow('Original', img)

cv2.namedWindow('Máscara', cv2.WINDOW_NORMAL)
cv2.imshow('Máscara', mascara)

cv2.namedWindow('Selección', cv2.WINDOW_NORMAL)
cv2.imshow('Selección', seleccion)

cv2.waitKey(0)
cv2.destroyAllWindows()
