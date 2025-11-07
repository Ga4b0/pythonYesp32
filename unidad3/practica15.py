# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 13:43:35 2025

@author: gaodg
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import socket
ancho, alto = 800, 600
fondo = np.ones((alto, ancho, 3), dtype=np.uint8) * 255


lista = []
ipesp32 = "192.168.16.184"
puerto= 12345
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.connect((ipesp32,puerto)) 
while True:
    try:
        servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        dato = servidor.recv(1024).decode().strip()
        if not dato:
            continue
        print(dato)
        lista.append(dato)
        
        
        fondo = np.ones((alto, ancho, 3), dtype=np.uint8) * 255
        cv2.putText(fondo, dato, (50, alto // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

        
        if len(lista)>= 10:
            break
    except Exception as e:
        print("Error",e)
    
servidor.close()
cv2.destroyAllWindows()