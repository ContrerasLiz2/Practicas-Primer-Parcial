# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 08:36:17 2025

@author: lizet
"""

from  PyQt5 import QtWidgets,uic

from PyQt5.QtGui import QPixmap //Para visualizar imagens 
import sys
import cv2


class MiClase(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app.ui',self) //Para mandar llamar la aplicaion como tal 
        img = QPixmap('figuras.jpg')
        self.lblImagen2.setPixmap(img)
        self.lblImagen2.setScaledContents(True)

        
        self.show()
    

if _name_='__main__':
    ventana  = QtWidgets.QApplication(sys.argv)
    ven  = MiClase()
    sys.exit(ventana.exec_())
    
    
