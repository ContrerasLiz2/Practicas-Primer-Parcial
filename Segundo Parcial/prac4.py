# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 07:23:04 2025

@author: lizet
"""



import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread('figuras.jpg')

# Verificar que la imagen se cargó correctamente
if img is None:
    print("Error al cargar la imagen")
    exit()

# Crear copias de la imagen
img2 = img.copy()
img3 = img.copy()

# Redimensionar imagen
img3 = cv2.resize(img3, (824, 404))
img2 = cv2.resize(img2, (824, 404))

# Convertir a escala de grises
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Aplicar umbral binario
_, valor = cv2.threshold(img2, 250, 150, cv2.THRESH_BINARY)

# Aplicar operación morfológica para mejorar la detección
kernel = np.ones((6, 6), np.uint8)
figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)

# Encontrar contornos
contornos, _ = cv2.findContours(figura, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos y calcular áreas
areas = []
for contorno in contornos:
    area = cv2.contourArea(contorno)
    areas.append(area)
    cv2.drawContours(img3, [contorno], -1, (255, 0, 100), 2)

# Mostrar cantidad de objetos detectados
cv2.putText(img3, f"Objetos: {len(contornos)}", (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 200, 255), 2, cv2.LINE_AA)

# Mostrar imagen en escala de grises con contornos
cv2.imshow('Imagen con contornos', img3)

# Esperar una tecla y cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
