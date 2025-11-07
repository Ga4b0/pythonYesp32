# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 13:33:01 2025

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
        
        fig, graf = plt.subplots(2,2,figsize=(10,4))
        ax = graf[0,0]
        bx = graf[0,1]
        cx = graf[1,0]
        dx = graf[1,1]

        
        #grafico = ax.plot(lista, color='skyblue')
        #ax.set_ylim(0,410q)
        grafico = ax.bar(range(len(lista)),lista)
        ax.set_ylim(0,410)
        
        #grafico 2       
        valornuevo = 409 - valor
        bx.pie([valor,valornuevo], labels=["Potenciometro","restante"], autopct="%1.1f") 
        bx.set_title('Grafico de Pie')
        
        #grafico 3
        valornuevo1 = 409 - valor
        cx.pie([valor,valornuevo1], labels=["Potenciometro","restante"], autopct="%1.1f") 
        cx.set_title('Grafico de Pie 2')
        
        #grafico 4
        grafico = dx.bar(range(len(lista)),lista)
        dx.set_title('Grafico de barras 2')
        dx.set_ylim(0,410)

        for _grafico, _lista in zip(grafico, lista):
            altura = _grafico.get_height()
            dx.text(_grafico.get_x() + _grafico.get_width() / 2,
                    _lista + 1,
                    str(_lista),
                    ha='center', va='bottom',
                    fontsize=9, color='black')

        
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
