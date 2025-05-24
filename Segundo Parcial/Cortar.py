# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 07:25:21 2025

@author: lizet
"""

""" Practica de Contar """
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import sys
import cv2
import colorsys

class MiClase(QtWidgets.QMainWindow):
    def _init_(self):
        super()._init_()
        uic.loadUi('contar.ui', self)
        self.rojo = 0
        self.verde = 0
        self.azul = 0
        self.mnuAbrir.triggered.connect(self.Abrir)
        self.mnuSalir.triggered.connect(self.Salir)
        #filtro Gaussiano
        self.SliderGauss.setMinimum(3)
        self.SliderGauss.setMaximum(30)
        self.SliderGauss.setSingleStep(2)
        self.SliderGauss.setValue(5)
        g = self.SliderGauss.value()
        self.label_3.setText(f"GuassianBlur: {g}")
        self.SliderGauss.valueChanged.connect(self.Gauss)
        #filtro Threshold
        self.SliderThres.setMinimum(3)
        self.SliderThres.setMaximum(250)
        self.SliderThres.setSingleStep(2)
        self.SliderThres.setValue(200)
        t = self.SliderThres.value()
        self.label_4.setText(f"Threshold: {t}")
        self.SliderThres.valueChanged.connect(self.Thres)
        #Kernel
        self.SliderKernel.setMinimum(3)
        self.SliderKernel.setMaximum(30)
        self.SliderKernel.setSingleStep(2)
        self.SliderKernel.setValue(6)
        k = self.SliderKernel.value()
        self.label_5.setText(f"Kernel: {k}")
        self.SliderKernel.valueChanged.connect(self.Kernel)
        self.btnContar.clicked.connect(self.contar)
        self.show()
        self.nombreArchivo = None
        
    def contar(self):
        if self.negroblanco.isCheked():
            self.rojo = 0
            self.verde = 0
            self.azul = 0
        else:
            self.rojo = 255
            self.verde = 255
            self.azul = 255
            
        img = cv2.imread(self.nombreArchivo)
        a, an, _ = img.shape
        print(str(a)+" "+str(an))
        copia = img.copy()

        copia = cv2.resize(copia, (int(an/3),int(a/3)))
        alto, ancho, _= copia.shape
        print(alto," ",ancho)
        copia = cv2.cvtColor(copia, cv2.COLOR_BGR2GRAY)
        
        g = self.SliderGauss.value()
        
        filtro = cv2.GaussianBlur(copia, (g,g), 0)
        
        t = self.SliderThres.value()
        
        _, valor = cv2.threshold(filtro, t, 255, cv2.THRESH_BINARY)
        
        k = self.SliderKernel.value()
        
        kernel = np.ones((k,k),np.uint8)
        figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)
        borde = cv2.Canny(figura, 3, 3)

        contornos, _ = cv2.findContours(borde, 
                                        cv2.RETR_EXTERNAL, 
                                        cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(copia, contornos, -1, (self.rojo,self.verde,self.azul,255,255,255),5)
        print(len(contornos))
        
        img_rgb = cv2.cvtColor(copia, cv2.COLOR_BGR2RGB)
        alto, ancho, canales = img_rgb.shape
        byteslines = canales * ancho
        imgFinal = QImage(img_rgb, ancho, alto, byteslines, QImage.Format_RGB888)
        imgFinal = imgFinal.scaled(250,250,Qt.KeepAspectRatio)
        self.lblResultado.setPixmap(QtGui.QPixmap.fromImage(imgFinal))
        self.lblResultado.setScaledContents(True)
        self.lblObjetos.setText(str(len(contornos)))
        
        
        
    def Gauss(self):
        g = self.SliderGauss.value()
        self.label_3.setText(f"GuassianBlur: {g}")
        
    def Thres(self):
        t = self.SliderThres.value()
        self.label_4.setText(f"Threshold: {t}")
        
    def Kernel(self):
        k = self.SliderKernel.value()
        self.label_5.setText(f"Kernel: {k}")
    
    
    def Salir(self):
        self.destroy()
        QtWidgets.QApplication.quit()
        
    def Abrir(self):
        self.nombreArchivo, _ = QFileDialog.getOpenFileName(self, "Abrir Imagen","",
                                                         "Imagenes (.png *.jpg *.jpeg);;Todos los archivos(.*)")
        
        img = QPixmap(self.nombreArchivo).scaled(300,400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.lblOriginal.setPixmap(img)
        self.lblOriginal.setScaledContents(False)


if _name=='main_':
    ventana = QtWidgets.QApplication(sys.argv)
    ven = MiClase()
    sys.exit(ventana.exec_())