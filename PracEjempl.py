# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:10:21 2025

@author: lizet
"""
#EJEMPLO DE Conversión a escala de grises y guardado de imagen

import cv2

# Cargar la imagen original
imagen = cv2.imread("img.jpg") 

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Guardar la imagen en escala de grises
cv2.imwrite("gris.jpg", gris)

# Mostrar la imagen original y la imagen en escala de grises
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Imagen en Grises", gris)

# Esperar una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
