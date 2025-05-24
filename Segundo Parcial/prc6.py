# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 07:53:51 2025

@author: lizet
"""

import sys
import cv2
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog

class MiClase(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Cargar la interfaz de usuario
        
        # Abrir cuadro de diálogo para seleccionar una imagen
        self.nombreArchivo, _ = QFileDialog.getOpenFileName(
            self, "Abrir Imagen", "", "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        
        if not self.nombreArchivo:
            return  # Si no se selecciona ninguna imagen, salir del método
        
        print(f"Imagen seleccionada: {self.nombreArchivo}")
        
        # Cargar y mostrar la imagen en `lblImagen1`
        img = QPixmap(self.nombreArchivo).scaled(350, 350, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.lblImagen1.setPixmap(img)
        self.lblImagen1.setScaledContents(True)  # Permitir que la imagen se ajuste mejor
        
        # Conectar el botón a la función `contar`
        self.btnContar.clicked.connect(self.contar)
        
        self.show()

    def contar(self):
        # Cargar la imagen con OpenCV
        img = cv2.imread(self.nombreArchivo)

        if img is None:
            print("Error: No se pudo cargar la imagen.")
            return
        
        # Hacer una copia de la imagen
        copia = img.copy()
        alto, ancho, _ = copia.shape
        print(f"Dimensiones de la imagen: {alto} x {ancho}")

        # Redimensionar la copia
        copia = cv2.resize(copia, (200, 200))
        
        # Convertir la imagen a escala de grises
        copia_gris = cv2.cvtColor(copia, cv2.COLOR_BGR2GRAY)

        # Aplicar un umbral
        _, valor = cv2.threshold(copia_gris, 180, 255, cv2.THRESH_BINARY)

        # Crear un kernel para operaciones morfológicas
        kernel = np.ones((6, 6), np.uint8)
        
        # Aplicar cierre morfológico
        figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)

        # Detectar bordes con Canny
        borde = cv2.Canny(figura, 133, 255)

        # Encontrar contornos
        contornos, _ = cv2.findContours(borde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Dibujar contornos en la imagen
        cv2.drawContours(copia, contornos, -1, (0, 255, 0), 2)

        # Convertir la imagen procesada a formato compatible con PyQt
        copia_rgb = cv2.cvtColor(copia, cv2.COLOR_BGR2RGB)
        alto, ancho, canales = copia_rgb.shape
        bytes_linea = canales * ancho
        imagen_resultado = QImage(copia_rgb.data, ancho, alto, bytes_linea, QImage.Format_RGB888)
        imagen_resultado = imagen_resultado.scaled(350, 350, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Mostrar la imagen procesada en lblImg3
        self.lblImg3.setPixmap(QPixmap.fromImage(imagen_resultado))
        self.lblImg3.setScaledContents(True)

        # Mostrar la cantidad de contornos detectados
        self.lblcontar.setText(f"Objetos detectados: {len(contornos)}")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Crea la aplicación PyQt
    ventana = MiClase()  # Instancia la clase principal
    sys.exit(app.exec_())  # Ejecuta el loop de eventos
