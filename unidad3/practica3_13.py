# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 13:34:19 2025

@author: gaodg
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
import serial 
from collections import deque

puerto = serial.Serial("COM12", 115200, timeout=1)
ancho, alto = 800, 600

#Deque para un solo valor
valor1 = deque(maxlen=100) 


plt.ioff() 
fig, ax = plt.subplots(1, 1, figsize=(7, 6))

ax.set_title("Valor 1 (Datos de ESP32)")
ax.set_ylim(0, 100) 
ax.set_xlim(0, 100) 
ax.set_ylabel("Valores")
ax.grid(True)

linea1, = ax.plot([], [], color='red', linewidth=2)


print("Conectado a COM12. Graficando...")
print("Presiona 'q' en la ventana del gráfico para salir.")

while True:    
    key = cv2.waitKey(25) & 0xFF
    if key == ord('q'):
        print("Cerrando...")
        break
    try:
        # 1. Leer la línea (ej: "42\n")
        dato = puerto.readline().decode().strip()
        if not dato:
            continue
            
        # 2. Convertir directamente a número
        v1 = float(dato) 
        
        # 3. Añadir al deque
        valor1.append(v1)
        
        # 4. Actualizar Matplotlib
        linea1.set_data(range(len(valor1)), list(valor1))
        
        # 5. Redibujar y convertir para OpenCV
        fig.canvas.draw()
        img = np.array(fig.canvas.buffer_rgba())
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
        img = cv2.resize(img, (ancho, alto))
        
        cv2.imshow("Grafico valor", img)

        
    except ValueError:
        # Esto se activará si el dato no es un número
        print(f"Dato no válido recibido: '{dato}'")
    except serial.SerialException:
        print("Error: Se perdió la conexión con el puerto serial.")
        break
    except Exception as e:
        print(f'Error inesperado: {e}')
            

puerto.close() 
cv2.destroyAllWindows()