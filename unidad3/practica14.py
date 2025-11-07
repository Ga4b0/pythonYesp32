# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 13:26:52 2025

@author: gaodg
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import socket

lista = []
ipesp32 = "192.168.16.184"
puerto= 12345
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.connect((ipesp32,puerto)) 
while True:
    try:
        
        dato = servidor.recv(1024).decode().strip()
        if not dato:
            continue
        print(dato)
        lista.append(dato)
        if len(lista)>= 10:
            break
    except Exception as e:
        print("Error",e)
    
servidor.close()