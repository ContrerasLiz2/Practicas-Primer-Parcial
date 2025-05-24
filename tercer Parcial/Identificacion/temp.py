# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyttsx3

audio = pyttsx3.init()

voces = audio.getProperty('voices')

for i, voice in enumerate(voces):
    print(f"Voz {i}:{voice.name} ({voice.languages})")
    
    audio.setProperty('voice', voces[0].id)
    audio.setProperty('rate', 150)
    audio.setProperty('volume',1)
    
    mensaje = "Hay lulu "
    
    audio.say(mensaje)
    audio.runAndWait()