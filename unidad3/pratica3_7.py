# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 09:26:36 2025

@author: gaodg
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import serial
import json

puerto = serial.Serial("COM5",115200)
lista = []
plt.ion() # modo interactivo

while True:
    try:
        linea = puerto.readline().decode().strip()
        if not linea:
            continue
        objeto = json.loads(linea)
        print(objeto)
        ejesx = objeto["labels"]
        ejesy = objeto["values"]
        valor = objeto["values"]
        lista.append(valor)
        
        if len(lista)> 100:
            lista.pop(0)
        
        fig, ax = plt.subplots()
        grafico = ax.plot(lista, color='skyblue')
        ax.set_ylim(0,410q)
        '''for grafico, ejesy in zip(grafico,ejesy):
            ax.text(grafico.get_x()+ grafico.get_width()/2,
                    ejesy +1, str(ejesy), ha='center', va= 'bottom', fontsize=10, color='black')
        '''
        ax.set_xlabel('Sensor')
        ax.set_ylabel('Valores')
        ax.set_title('Grafico de barras con Open cv')
        fig.canvas.draw()
        img = np.array(fig.canvas.buffer_rgba())
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imshow('Grafico', img)
        cv2.waitKey(1)
        plt.close(fig)
        
        
        
        #letra =cv2.waitKey(1)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            puerto.close()
            break
            
    except json.JSONDecodeError:
        print('Error de lectura')
        
    except Exception as e:
        print('Error', e)
        break
puerto.close()
cv2.destroyAllWindows()
