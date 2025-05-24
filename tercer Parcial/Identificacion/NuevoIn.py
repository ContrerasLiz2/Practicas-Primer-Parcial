# -*- coding: utf-8 -*-
"""
Created on Tue May  6 07:46:18 2025

@author: lizet
"""

import numpy as np
import os
import json
import sys
import cv2
import face_recognition
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from Identificacion import Ui_MainWindow

class MiClase(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        self.ventana.mnuAGuardar.triggered.connect(self.MostrarGuardar)
        self.ventana.mnuIdentificar.triggered.connect(self.Identificar)
        self.ventana.mnuSalir.triggered.connect(self.Salir)
        self.ventana.btnGuardar.clicked.connect(self.guardar)
        self.ventana.btnIdentificar.clicked.connect(self.Identificar)
        self.Work = None
        self.Work2 = None

    def guardar(self):
        texto = self.ventana.lineEdit.text()
        if texto == "":
            QMessageBox.warning(self, "Advertencia", "No se escribió el nombre")
        else:
            if self.Work:
                self.Work.recibirNombre(texto)
                self.Work.capturar = 2
                QMessageBox.information(self, "Información", "Imagen Guardada Correctamente")

    def Salir(self):
        self.close()

    def closeEvent(self, event):
        if self.Work and self.Work.isRunning():
            self.Work.hilo = False
            self.Work.quit()
            self.Work.wait()
        if self.Work2 and self.Work2.isRunning():
            self.Work2.hilo = False
            self.Work2.quit()
            self.Work2.wait()
        event.accept()

    def Identificar(self):
        self.ventana.frame1.setEnabled(False)
        self.ventana.frame2.setEnabled(True)
        self.ActivarCamara2()

    def MostrarGuardar(self):
        self.ventana.frame1.setEnabled(True)
        self.ventana.frame2.setEnabled(False)
        self.ActivarCamara()

    def ActivarCamara(self):
        if self.Work is None:
            self.Work = Work()
            self.Work.start()
            self.Work.ImagenC.connect(self.lblImagen_cargar)

    def ActivarCamara2(self):
        if self.Work2 is None:
            self.Work2 = Work2()
            self.Work2.start()
            self.Work2.ImagenC.connect(self.lblImagen_cargar)
            self.Work2.lblMostrarNombre.connect(self.MostrarNombre)

    def MostrarNombre(self, nombre):
        self.ventana.lblNombre.setText(nombre)

    def lblImagen_cargar(self, Image):
        self.ventana.lblimagen.setPixmap(QPixmap.fromImage(Image))

class Work(QThread):
    ImagenC = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self.capturar = 0
        self.nombre = ""
        self.hilo = True

    def recibirNombre(self, texto):
        self.nombre = texto

    def run(self):
        video = cv2.VideoCapture(0)
        if not video.isOpened():
            print("Error: No se pudo abrir la cámara.")
            return

        while self.hilo:
            ret, frame = video.read()
            if ret:
                Image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

                if self.capturar == 2:
                    carpeta = "rostros"
                    if not os.path.exists(carpeta):
                        os.makedirs(carpeta)
                    rutaimagen = os.path.join(carpeta, self.nombre + ".jpg")
                    cv2.imwrite(rutaimagen, frame)

                    lista = []
                    if os.path.exists('fotos.json'):
                        with open("fotos.json", "r") as f:
                            lista = json.load(f)

                    lista.append({"nombre": self.nombre, "imagen": rutaimagen})
                    with open("fotos.json", "w") as f:
                        json.dump(lista, f, indent=4)

                    self.capturar = 0

                conversion = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                p = conversion.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
                self.ImagenC.emit(p)

        video.release()

class Work2(QThread):
    ImagenC = pyqtSignal(QImage)
    lblMostrarNombre = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.hilo = True
        self.caras = []
        self.nombres = []
        self.bandera = True

        try:
            if os.path.exists("fotos.json"):
                with open("fotos.json", "r") as f:
                    personas = json.load(f)

                for persona in personas:
                    img = face_recognition.load_image_file(persona["imagen"])
                    personaEncontrada = face_recognition.face_encodings(img)
                    if personaEncontrada:
                        self.caras.append(personaEncontrada[0])
                        self.nombres.append(persona["nombre"])
        except Exception as e:
            print(f"Error cargando rostros: {e}")

    def run(self):
        video = cv2.VideoCapture(0)
        if not video.isOpened():
            print("Error: No se pudo abrir la cámara.")
            return

        while self.hilo:
            ret, frame = video.read()
            if ret:
                Image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

                if self.bandera:
                    self.bandera = False

                    ubicaciones = face_recognition.face_locations(Image)
                    codigos = face_recognition.face_encodings(Image, ubicaciones)

                    for (top, right, bottom, left), cara_frame in zip(ubicaciones, codigos):
                        nombre = "Desconocido"
                        if self.caras:
                            distancias = face_recognition.face_distance(self.caras, cara_frame)
                            min_dist = min(distancias)
                            indice_min = distancias.tolist().index(min_dist)
                            if min_dist < 0.5:
                                nombre = "Hola " + self.nombres[indice_min]
                        self.lblMostrarNombre.emit(nombre)

                conversion = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                p = conversion.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
                self.ImagenC.emit(p)

        video.release()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiClase()
    ventana.show()
    sys.exit(app.exec_())
