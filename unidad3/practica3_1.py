# -*- coding: utf-8 -*-


#Instala pip install pyserial
import serial
import time

conexion = serial.Serial("COM5",115200,timeout=1)
lista = []

def leer():
    n = 0
    while(True):
        datos = conexion.readline().decode().strip()
        if datos != None:
            lista.append(datos)
            print(datos[1:])
        n += 1

        if n > 10:
            break
        
        time.sleep(0.1)

if __name__=='__main__':
    leer()