# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 12:22:14 2025

@author: gaodg
"""

import cv2
import socket
import numpy as np
import json

host = "0.0.0.0"
puerto = 5001

lista = []

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.bind((host,puerto))

servidor.listen(1)

con, addr = servidor.accept()
print(f"se conecto {addr}")

while True:
    try:
        dato = con.recv(1024).decode().strip()
        if not dato:
            continue
        print(dato)
        lista.append(dato)
        if len(lista) > 5:
            break
        
    except Exception as e:
        print(f"Error {e}")
        break
    
con.close()
servidor.close()
