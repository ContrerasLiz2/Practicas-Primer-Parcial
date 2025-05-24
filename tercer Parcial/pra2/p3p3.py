# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 08:58:57 2025

@author: lizet
"""

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

# Definir los rangos de color rojo en HSV (dos rangos debido a la naturaleza del rojo en HSV)
rojo_claro = np.array([0, 100, 20], np.uint8)
rojo_oscuro = np.array([5, 255, 255], np.uint8)

rojo2_claro = np.array([175, 100, 20], np.uint8)
rojo2_oscuro = np.array([179, 255, 255], np.uint8)

# Crear máscaras para ambos rangos de rojo
mascara1 = cv2.inRange(img_hsv, rojo_claro, rojo_oscuro)
mascara2 = cv2.inRange(img_hsv, rojo2_claro, rojo2_oscuro)

# Combinar ambas máscaras
mascara = cv2.bitwise_or(mascara1, mascara2)

# Aplicar la máscara a la imagen original
seleccion = cv2.bitwise_and(img, img, mask=mascara)

# Mostrar las imágenes procesadas
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow('Original', img)

cv2.namedWindow('Máscara', cv2.WINDOW_NORMAL)
cv2.imshow('Máscara', mascara)

cv2.namedWindow('Selección', cv2.WINDOW_NORMAL)
cv2.imshow('Selección', seleccion)

cv2.waitKey(0)
cv2.destroyAllWindows()
