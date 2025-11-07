# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 21:03:25 2025

@author: gaodg
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import serial
import json
#import time # tiempo 

# Configura el puerto correcto según tu PC
puerto = serial.Serial("COM5", 115200)
#time.sleep(2)  # Espera que se estabilice la conexión serial

# Listas para guardar valores recientes
tempC_list = []
humedad_list = []
luz_list = []
dist_list = []

plt.ion()  # modo interactivo

while True:
    try:
        linea = puerto.readline().decode().strip()
        if not linea:
            continue
        
        # Intenta cargar el JSON del ESP32
        objeto = json.loads(linea)
        print(objeto)

        # Extraer valores
        tempC = objeto.get("temperatura_C", 0)
        humedad = objeto.get("humedad", 0)
        luz = objeto.get("luz", 0)
        distancia = objeto.get("distancia_cm", 0)

        # Guardar los últimos 10 valores
        tempC_list.append(tempC)
        humedad_list.append(humedad)
        luz_list.append(luz)
        dist_list.append(distancia)

        if len(tempC_list) > 10:
            tempC_list.pop(0)
            humedad_list.pop(0)
            luz_list.pop(0)
            dist_list.pop(0)

        # Crear figura con 2x2 subgráficos
        fig, graf = plt.subplots(2, 2, figsize=(10, 6))
        ax1, ax2, ax3, ax4 = graf[0,0], graf[0,1], graf[1,0], graf[1,1]

        #Temperatura(°C)
        ax1.plot(tempC_list, color='red', marker='o')
        ax1.set_title('Temperatura (°C)')
        ax1.set_ylim(0, 50)
        #ax1.text(len(tempC_list)-1, tempC_list[-1] + 1, sirve para poner le el valor a la ultima medicion
         #     f"{tempC_list[-1]:.1f} °C",
          #    ha='center', va='bottom', fontsize=10, color='black')
        ax1.grid(True)
        for i, valor in enumerate(tempC_list):
            ax1.text(i, valor + 0.8, f"{valor:.1f}", 
                     ha='center', va='bottom', 
                     fontsize=9, color='black')
            
        

        #Humedad 
        humedaT = 100 - humedad
        ax2.pie([humedad, humedaT],
        labels=["Humedad total", "restante"],
        autopct="%1.1f",
        colors=['skyblue', 'lightgray'])
        ax2.set_title('Humedad (%)')





        #Luz
        grafico = ax3.bar(range(len(luz_list)), luz_list, color='orange')
        ax3.set_title('Luz (%)')
        ax3.set_ylim(0, 100)
        for barra, valor in zip(grafico, luz_list):
            altura = barra.get_height()
            ax3.text(barra.get_x() + barra.get_width() / 2,
             altura + 2,          # un poco arriba de la barra
             f"{valor:.1f}",
             ha='center', va='bottom',
             fontsize=9, color='black')



        
        # Distancia (cm) - tipo medidor
        dist_restante = max(0, 60 - distancia)
        ax4.pie([distancia, dist_restante],
         colors=['limegreen', 'lightgray'],
         startangle=180,
         counterclock=False,
         wedgeprops={'width':0.3})
        ax4.set_title(f"Distancia: {distancia:.1f} cm")

        
        
        #Distancia (cm)
        #ax4.barh([0], [distancia], color='green')
        #ax4.set_xlim(0, 40)
        #ax4.set_title('Distancia (cm)')
        #ax4.set_yticks([])  # quita el eje Y
        #ax4.text(distancia + 1, 0, f"{distancia:.1f} cm", va='center', fontsize=10)
        
        
        
        '''ax4.scatter(range(len(dist_list)), dist_list, color='green')
        ax4.set_title('Distancia (cm)')
        ax4.set_ylim(0, 40)
        ax4.grid(True)'''

        plt.tight_layout()
        fig.canvas.draw()

        # Convertir la figura a imagen y mostrar con OpenCV
        img = np.array(fig.canvas.buffer_rgba())
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
        cv2.imshow('Sensores ESP32', img)
        plt.close(fig)

        # Salir con tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            puerto.close()
            break

    except json.JSONDecodeError:
        print('Error: JSON inválido recibido')
        continue
    except Exception as e:
        print('Error:', e)
        break

puerto.close()
cv2.destroyAllWindows()
