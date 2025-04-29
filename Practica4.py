# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 08:44:34 2025

@author: lizet
"""

#practica4
import  cv2
import easygui as ventana 
extension = ['*.jpg','*.png']
archivo = None
archivo = ventana.fileopenbox(msg='Abrir Archivo',
                              title='Control: Ventana abrir',
                              default='',
                              filetypes=extension) 
print (archivo)


img = cv2.imread('img.jpg')
#tamano de la imagen original 
alto, largo, _ = img.shape 
print (alto,'',largo)


img2= img.cpy()
img2= cv2.rotate(img2,cv2.ROTATE_90_CLOCKWISE)#Para mostrar  la rotacion de
#la copia de la imagen
cv2.imwrite('img90.jpg', img2)#para guardar la copia de la imagen 
img3 = cv2.imread('img.jpg')
#tamano de la imagen rotada la copiada 
alto2, largo2, _ = img.shape 
print (alto2,'',largo2)

#cv2.namedWindow(' ventana',cv2.WINDOW_NORMAL)#creacmos una veentana para la imagen 
cv2.imshow('Ventana2',img2)#Para mostrar la copia de la imagen para no modificar la imagen original 
#cv2.imshow('ventana',cv2.WINDOW_NORMAL)#mostramos la imegen de la ventana 
cv2.waitKey(0)
cv2.destroyAllWindows()  #Simpre tienen que ir al final 