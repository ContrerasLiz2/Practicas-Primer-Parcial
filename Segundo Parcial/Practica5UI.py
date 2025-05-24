# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 08:37:09 2025

@author: Saulap
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
import sys
import cv2

class MiClase(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app.ui', self)  # Carga la interfaz de usuario desde un archivo .ui
        
        # Carga la primera imagen y la muestra en el QLabel correspondiente
        img1 = QPixmap('mon.jpg')
        self.lblImagen1.setPixmap(img1)
        self.lblImagen1.setScaledContents(True)  # Permite ajustar la imagen al QLabel
        
        # Carga la segunda imagen y la muestra en el QLabel correspondiente
        img2 = QPixmap('clavos.webp')
        self.lblImagen2.setPixmap(img2)
        self.lblImagen2.setScaledContents(self.Abrir)  # Error: `self.Abrir` no debería estar aquí
        
        # Conecta el botón "Abrir" con la función `guardar`
        self.btnAbrir.clicked.connect(self.guardar)
        
        self.nombreArchivo = None  # Variable para almacenar el nombre del archivo seleccionado
        self.imagenfinal = None  # Variable para almacenar la imagen procesada
        
        self.show()  # Muestra la ventana
    
    def guardar(self):
        """
        Abre un cuadro de diálogo para seleccionar una imagen y la guarda con OpenCV.
        """
        imgguardar = QFileDialog.getOpenFileNames(filter="Imagen (*.*) ")[0]  # Obtiene el nombre del archivo seleccionado
        cv2.imwrite(imgguardar, self.imgguardar)  # Error: `self.imgguardar` no existe, debería ser `self.nombreArchivo`
        print('Imagen guardada')
    
    def Abrir(self):
        """
        Abre una imagen, la muestra en un QLabel y convierte la imagen a escala de grises.
        """
        self.nombreArchivo = QFileDialog.getOpenFileName(filter="Imagen (*.*)")[0]  # Selecciona un archivo de imagen
        if not self.nombreArchivo:
            return
        print(self.nombreArchivo)
        
        # Carga y muestra la imagen original en `lblImagen3`
        img3 = QPixmap(self.nombreArchivo)
        self.lblImagen3.setPixmap(img3)
        self.lblImagen3.setScaledContents(True)
        
        # Carga la imagen con OpenCV y la convierte a escala de grises
        img4 = cv2.imread(self.nombreArchivo)
        gris = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)  # Convierte la imagen a escala de grises
        altura, ancho = gris.shape  # Obtiene las dimensiones de la imagen
        
        # Convierte la imagen en escala de grises a un formato compatible con PyQt
        img5 = QImage(gris.data, ancho, altura, gris.strides[0], QImage.Format_Grayscale8)
        img5 = img5.scaled(350, 350, Qt.KeepAspectRatio)
        self.imagenfinal = img5  # Guarda la imagen procesada
        
        # Muestra la imagen en escala de grises en `lblImagen4`
        self.lblImagen4.setPixmap(QtGui.QPixmap.fromImage(img5))
        self.lblImagen4.setScaledContents(True)
        
# Verifica si el script se ejecuta directamente
if __name__ == '__main__':
    ventana = QtWidgets.QApplication(sys.argv)  # Crea una aplicación PyQt
    ven = MiClase()  # Instancia la clase principal
    sys.exit(ventana.exec_())  # Ejecuta el bucle de eventos de la aplicación
