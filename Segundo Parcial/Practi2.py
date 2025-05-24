# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 07:24:52 2025

@author: lizet
"""
import numpy as np
import cv2 

# Cargar la imagen
img = cv2.imread('OIP.jpeg')

# Verificar si la imagen se cargó correctamente
if img is None:
    print("Error: No se pudo cargar la imagen.")
else:
    # Hacer una copia de la imagen
    copia = img.copy()
    alto, ancho, _ = copia.shape
    print(alto, " ", ancho)

    # Redimensionar la copia
    copia = cv2.resize(copia, (200, 200))
    
    # Convertir la copia a escala de grises
    copia_gris = cv2.cvtColor(copia, cv2.COLOR_BGR2GRAY)

    # Aplicar un umbral
    _, valor = cv2.threshold(copia_gris, 180, 255, cv2.THRESH_BINARY)

    # Crear un kernel para operaciones morfológicas
    kernel = np.ones((6, 6), np.uint8)  # Cambiado 'np.unit8' a 'np.uint8'
    
    # Aplicar cierre morfológico
    figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)

    # Detectar bordes
    borde = cv2.Canny(figura, 133, 255)

    # Encontrar contornos
    contornos, _ = cv2.findContours(borde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Corregido el uso de 'findChessboardCorners'

    # Dibujar contornos en la copia
    cv2.drawContours(copia, contornos, -1, (0, 255, 0), 2)

    # Mostrar la imagen original
    cv2.namedWindow('original', cv2.WINDOW_NORMAL)
    cv2.imshow('original', img)

    # Mostrar la copia con contornos
    cv2.namedWindow('copia con contornos', cv2.WINDOW_NORMAL)
    cv2.imshow('copia con contornos', copia)

    # Esperar a que se presione una tecla
    cv2.waitKey(0)
    cv2.destroyAllWindows()