# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:13:15 2025

@author: lizet
"""
#Ejercicio 3: Rotación de imagen 90° en sentido horario 
import cv2

# Cargar la imagen original
imagen = cv2.imread("img.jpg")

# Rotar la imagen 90° en sentido horario
rotada = cv2.rotate(imagen, cv2.ROTATE_90_CLOCKWISE)

# Guardar la imagen rotada
cv2.imwrite("rotada.jpg", rotada)

# Mostrar la imagen original y la rotada
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Imagen Rotada", rotada)

# Esperar una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
