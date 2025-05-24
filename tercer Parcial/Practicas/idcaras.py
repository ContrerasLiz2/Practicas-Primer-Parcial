# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 07:59:01 2025

@author: lizet
"""


import cv2
import face_recognition
import pyttsx3

hablar = pyttsx3.init()
voces = hablar.getProperty('voices')
hablar.setProperty('voices', voces[2].id)

caras = []
nombre = []
personasencontradas = []


persona1 = face_recognition.load_image_file('Emmanuel.png')
persona2 = face_recognition.load_image_file('David.png')
persona3 = face_recognition.load_image_file('Uriel.jpeg')

if face_recognition.face_encodings(persona1):
    personaEncontrada1 = face_recognition.face_encodings(persona1)[0]
    caras.append(personaEncontrada1)
    nombre.append("Emmanuel")

if face_recognition.face_encodings(persona2):
    personaEncontrada2 = face_recognition.face_encodings(persona2)[0]
    caras.append(personaEncontrada2)
    nombre.append("David")
    
if face_recognition.face_encodings(persona3):
    personaEncontrada3 = face_recognition.face_encodings(persona3)[0]
    caras.append(personaEncontrada2)
    nombre.append("Uriel")
    
    
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break
    personas = face_recognition.face_locations(frame)
    caras_frame = face_recognition.face_encodings(frame, personas)
    
    for (arriba, derecha, abajo, izquierda), caras_frame in zip(personas, caras_frame):
        encontradas =  face_recognition.compare_faces(caras, caras_frame)
        nom = "Desconocido"
        
        if True in encontradas:
            primer_cara_encontrada = encontradas.index(True)
            nom = nombre[primer_cara_encontrada]
            
            if nom in personasencontradas:
                pass
            else:
                personasencontradas.append(nom)
                hablar.say('Zi'+ nom)
                hablar.runAndWait()
                break
        cv2.putText(frame, nom, (izquierda, arriba), cv2.FONT_HERSHEY_SIMPLEX, 0.9 ,(0,255,255), 2)

    cv2.imshow("persona", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("a"):
        break
    
video.release()
cv2.destroyAllWindows()