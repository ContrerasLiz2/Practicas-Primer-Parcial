# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:10:52 2025

@author: lizet
"""
#Ejercicio 2: Recorte de imagen con ROI (Región de Interés)

import cv2

# Cargar la imagen original
imagen = cv2.imread("img.jpg")

# Seleccionar una región de la imagen (ROI)
roi = cv2.selectROI("Selecciona un área", imagen, fromCenter=False, showCrosshair=True)

# Extraer la región seleccionada
x, y, w, h = roi
corte = imagen[y:y+h, x:x+w]

# Guardar la imagen recortada
cv2.imwrite("corte.jpg", corte)

# Mostrar la imagen original y el recorte
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Recorte", corte)

# Esperar una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
