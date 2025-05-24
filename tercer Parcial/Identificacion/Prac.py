# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 07:41:53 2025

@author: lizet
"""
import numpy as np
from PyQt5 import  QtCore,QtGui,QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog,QApplication,QMainWindow
import sys
import cv2
from PyQt5

class MiClase(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Identificacion.ui', self)
        self.mnuAGuardar.triggered.connect(self.MostrarGuardar)
        self.mnuIdentificar.triggered.connect(self.Identificar)
        self.mnuSalir.triggered.connect(self.Salir)
        self.show()
        
    def MostrarGuardar(self):
        self.frame1.setEnabled(False) 
        self.frame2.setEnabled(True)
        video = cv2.VideoCapture(0) 
        
        while True:
            ret, frame = video.read()
            if not ret:
                break
            ancho, alto, canales = copia.shape
        bytes_linea = canales * ancho
        imgresultado = QImage(copia.data, ancho, alto, bytes_linea, QImage.Format_RGB888)
        imgresultado = imgresultado.scaled(250,250,Qt.KeepAspectRatio)
        self.lblImg3.setPixmap(QtGui.QPixmap.fromImage(imgresultado))
        self.lblImg3.setScaledContents(True)
        self.lblContar.setText(str(len(contornos)))
       
            
        video.release()
        
        cv2.destroyAllWindows()
    
    def Salir(self):
        self.close() 
        QtWidgets.QApplication.quit()
        
    def Identificar(self):
        self.frame1.setEnabled(True)  
        self.frame2.setEnabled(False)
        
    def ActivarCamara(self,Imagen):
        self.Work = Work()
        self.Work.Imagen.connect(self.lblImagen_cargar)
        
    def lblImagen_cargar(self,Imagen):
        self.ventana.lblImagen.setPixmap(QPixmap.fromImage(Image))
        
        
class Work(QThread):
    def __init__(self):
        super().__init__()
        
        
    def run(self):
        self.hilo=True
        
        video = cv2.VideoCapture(0)
        while True:
            ret,frame = video.read()
            if ret:
                Image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                conversion = QImage(Image.data,Image.shape[1],Image.shape[0],QImage.Format_RGB888)
                p = cocnvers
        

if __name__ == "__main__":
    vent = QApplication(sys.argv)
    app = QtWidgets.QApplication(sys.argv)
    ventana = MiClase()  
    sys.exit(app.exec_())
