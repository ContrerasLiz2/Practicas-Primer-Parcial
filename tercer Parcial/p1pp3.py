# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 09:10:05 2025

@author: lizet
"""

import cv2
import numpy as np 

# Capturar video desde la cámara
camara = cv2.VideoCapture(0)

# Configurar la salida de video
salida = cv2.VideoWriter('rojo.mp4',
                         cv2.VideoWriter_fourcc(*'XVID'),
                         20.0, (640, 480))

while camara.isOpened():
    ret, frame = camara.read()
    if ret:
        # Convertir el frame a HSV
        img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Definir los rangos de color rojo en HSV
        rojo_claro = np.array([0, 100, 20], np.uint8)
        rojo_oscuro = np.array([5, 255, 255], np.uint8)

        rojo2_claro = np.array([175, 100, 20], np.uint8)
        rojo2_oscuro = np.array([179, 255, 255], np.uint8)

        # Crear máscaras para los tonos de rojo
        mascara1 = cv2.inRange(img_hsv, rojo_claro, rojo_oscuro)
        mascara2 = cv2.inRange(img_hsv, rojo2_claro, rojo2_oscuro)

        # Combinar ambas máscaras
        mascara = cv2.bitwise_or(mascara1, mascara2)

        # Aplicar la máscara a la imagen original
        seleccion = cv2.bitwise_and(frame, frame, mask=mascara)

        # Voltear la imagen para una mejor visualización
        frame_flip = cv2.flip(frame, 1)
        seleccion_flip = cv2.flip(seleccion, 1)
        mascara_flip = cv2.flip(mascara, 1)

        # Mostrar las imágenes procesadas
        cv2.imshow('Original', frame_flip)
        cv2.imshow('Máscara', mascara_flip)
        cv2.imshow('Selección', seleccion_flip)

        # Guardar el frame en el video de salida
        salida.write(frame)

        # Salir con la tecla 'a'
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break
    else:
        break

# Liberar recursos
camara.release()
salida.release()
cv2.destroyAllWindows()
