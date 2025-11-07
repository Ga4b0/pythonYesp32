# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 13:05:31 2025

@author: gaodg
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 11:06:38 2025

@author: gaodg
"""

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
        
        if len(lista)> 5:
            lista.pop(0)
        
        fig, [ax,bx] = plt.subplots(1,2,figsize=(10,4))
        #grafico = ax.plot(lista, color='skyblue')
        #ax.set_ylim(0,410q)
        grafico = ax.bar(range(len(lista)),lista)
        ax.set_ylim(0,410)
        
        #grafico 2       
        valornuevo = 409 - valor
        bx.pie([valor,valornuevo], labels=["Potenciometro","restante"], autopct="%1.1f") 
        bx.set_title('Grafico de Pie')

        
        for _grafico, _lista in zip(grafico, lista):
            altura = _grafico.get_height()
            ax.text(_grafico.get_x() + _grafico.get_width() / 2,
                    _lista + 1,
                    str(_lista),
                    ha='center', va='bottom',
                    fontsize=9, color='black')
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
