"""
Created on Tue Nov  4 11:42:04 2025

@author: gaodg
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import serial 
from collections import deque
import json

try:
    puerto = serial.Serial("COM5", 115200, timeout=1) # <-- Añadido timeout por seguridad
except serial.SerialException as e:
    print(f"Error al abrir el puerto COM5: {e}")
    print("Verifica que el dispositivo esté conectado y el puerto sea correcto.")
    exit()


transmitiendo = False
ancho, alto = 800, 600

valor1 = deque(maxlen=100)
valor2 = deque(maxlen=100)

plt.ioff() # Desactiva el modo interactivo de Matplotlib

fig, (x1, x2) = plt.subplots(2, 1, figsize=(7, 6)) 
fig.subplots_adjust(hspace=0.4)

x1.set_title("Valor 1")
x1.set_ylim(0, 100) # Asumiendo valores de 0 a 100
x1.set_xlim(0, 100) # 100 es el maxlen del deque
x1.set_ylabel("Valores")
x1.grid(True)

x2.set_title("Valor 2")
x2.set_ylim(0, 100) # Asumiendo valores de 0 a 100
x2.set_xlim(0, 100)
x2.set_ylabel("Valores")
x2.grid(True)

linea1, = x1.plot([], [], color='red', linewidth=2)
linea2, = x2.plot([], [], color='blue', linewidth=2)

#Pantalla de inicio de OpenCV
fondo = np.ones((alto, ancho, 3), dtype=np.uint8) * 255
texto = "Presiona 'i' inicia, 'o' detiene, 'q' termina"


cv2.putText(fondo, texto, (50, alto // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
cv2.imshow("Graficos valores", fondo)

while True:
    key = cv2.waitKey(25) & 0xFF
    
    if key == ord('i'):
        print("Iniciando transmisión...")
        transmitiendo = True
        puerto.write(b'1') # <-- Sugerencia: enviar 'i' para iniciar
        
    if key == ord('o'):
        print("Deteniendo transmisión...")
        transmitiendo = False
        puerto.write(b'1') # <-- Sugerencia: enviar 'o' para detener
        
    if key == ord('q'):
        print("Cerrando...")
        break
    
    if transmitiendo and puerto.in_waiting > 0:
        try:
            dato = puerto.readline().decode().strip()
            if not dato:
                continue
                
            datos = json.loads(dato)
            
            # Validaciones robustas
            if not isinstance(datos, dict) or "values" not in datos:
                print(f"JSON ignorado (formato incorrecto): {dato}")
                continue
            
            valores = datos.get("values", [])
            
            if not isinstance(valores, (list, tuple)) or len(valores) != 2:
                print(f"JSON ignorado (lista 'values' incorrecta): {dato}")
                continue
    
            v1, v2 = valores 
            
            valor1.append(v1)
            valor2.append(v2)
            
            #set_data ahora funciona porque linea1/2 son objetos Line2D
            linea1.set_data(range(len(valor1)), list(valor1))
            linea2.set_data(range(len(valor2)), list(valor2))
            
            # Redibuja el canvas de Matplotlib
            fig.canvas.draw()
            
            # Convierte el canvas a una imagen de OpenCV
            img = np.array(fig.canvas.buffer_rgba())
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR) # <- El buffer es RGBA
            img = cv2.resize(img, (ancho, alto))
            
            cv2.imshow("Graficos valores", img)
            
        except json.JSONDecodeError:
            print(f"Error de JSON: No se pudo decodificar el dato: {dato}")
        except Exception as e:
            print(f'Error inesperado: {e}')
    
    elif not transmitiendo:
        cv2.imshow("Graficos valores", fondo)
        
puerto.close()
cv2.destroyAllWindows()