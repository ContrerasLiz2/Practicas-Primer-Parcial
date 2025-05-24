# -*- coding: utf-8 -*-
"""
Created on Fri May  9 07:15:33 2025

@author: lizet
"""

import cv2
import mediapipe as mp


manos = mp.solutions.hands

manos = manos.Hands(static_image_mode = False, max_num_hands=2, min_detection_confidence=0.5)

dibujo = mp.solutions.drawing_utils 

#manos = manos.Hands()

video = cv2.VideoCapture(0)  

while video.isOpened():
    r, frame = video.read()
    if not r:
        break

    frame = cv2.flip(frame, 1)
    
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
    resultado = manos.process(rgb) 
    
    total_dedos = 0
    
    if resultado.multi_hand_landmarks:
        for landmark in resultado.multi_hand_landmarks:  
            dibujo.draw_landmarks(frame, landmark, mp.solutions.hands.HAND_CONNECTIONS)
            
            dedos = []
            
            for punta in [8,12,16,20]:
                if landmark.landmark[punta].y < landmark.landmark[punta - 2].y:
                    dedos.append(1)
                else:
                    dedos.append(0)
            pulgarizquierdo = landmark.landmark[4] 
            pulgarderecho = landmark.landmark[2]
            if pulgarizquierdo.x < pulgarderecho.x: 
                dedos.append(1)
            else:
                dedos.append(0)
                
            total_dedos += sum(dedos)
            
    cv2.putText(frame,f"Dedos Contados Son:{total_dedos}",(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5)
    cv2.imshow("Cuantos dedos son ", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break


video.release()
cv2.destroyAllWindows() 