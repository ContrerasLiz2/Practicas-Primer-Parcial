# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 09:52:05 2025

@author: lizet
"""

import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow
import sys
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from main import Ui_MainWindow



class MiClase(QtWidgets.QMainWindow):
    def _init_(self):
        super()._init_()
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        self.ventana.mnuAGuardar.triggered.connect(self.MostrarGuardar)
        self.ventana.mnuAIdentificar.triggered.connect(self.Identificar)
        self.ventana.mnuASalir.triggered.connect(self.Salir)
        self.ventana.pushButton.clicked.connect(self.guardar)
        
        
    def guardar(self):
        
        texto = self.ventana.txtNombre.Text()
        if texto=="":
            QMessageBox.warnig(self,"Advertencia","No se escribio el nombre")
        else:
            if self.work:
                self.work.recibirNombre(texto)
                self.Work.capturar = 2
                QMessageBox.information(self,"Ventana","Imagen Guardada Correctamente ")
                
        
    def Salir(self):
        self.destroy()
        QtWidgets.QApplication.quit()
        
        
    def Identificar(self):
        self.ventana.frame1.setEnabled(False)
        self.ventana.frame2.setEnabled(True)
        
    def MostrarGuardar(self):
        self.ventana.frame1.setEnabled(True)
        self.ventana.frame2.setEnabled(False)
        self.ActivarCamara()
    
    def ActivarCamara(self):
        self.Work = Work()
        self.Work.start()
        self.Work.ImagenC.connect(self.lblImagen_cargar)
        
    def lblImagen_cargar(self, Image):
        self.ventana.lblImagen.setPixmap(QPixmap.fromImage(Image))

class Work(QThread):
    def _init_(self):
        super()._init_()
        self.capturar = 0
        self.nombre = " "
        
    def recibirNombre(self,texto):
        self.nombre = texto
        
    ImagenC = pyqtSignal(QImage)
    def run(self):
        self.hilo = True
        
        video = cv2.VideoCapture(0)
        while True:
            ret, frame = video.read()
            if ret:
                Image = cv2.cvtColor(cv2.flip(frame1), cv2.COLOR_BGR2RGB)
                if self.capturar == 2:
                    archivo = self.nombre + ".jpg"
                    cv2.imwerite(archivo,frame)
                    self.capturar = 0
                
                
                conversion = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                p = conversion.scaled(300,200, Qt.KeepAspectRatio)
                self.ImagenC.emit(p)
                      

if _name=='main_':
    vent = QApplication(sys.argv)
    ventana = MiClase()
    ventana.show()
    sys.exit(vent.exec_())