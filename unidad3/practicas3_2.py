# -*- coding: utf-8 -*-

#NOTA EN LA PLACA DEL  MICROCONTROLADOR SE RECOMIENDA NO COLOCAR COMPONENTES DE LECTURA ANALOGICA EN
#LOS PINES 2,12 Y 15
import serial
import time

from tkinter import *
from tkinter import messagebox

class Principal:
    #self es el apuntador de la clase

    #Creamos el constructor
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Impresion de datos")
        self.ventana.geometry(f"400x200")
        self.n = 0
        self.conexion = None

    def inicio(self):
        #Inicializamos la ventana
        self.mensaje = Label(self.ventana,text="Hola Mundo")
        self.mensaje.place(x=10,y=10)
        Button(self.ventana,text="Aceptar",command=self.recibir).place(x=10,y=50)
        #Button(self.ventana,text="Cerrar",command=self.cerrar).place(x=30,y=60)
        #Mandamos a llamar al metodo de construccion de crear conexion
        # self.crearConexion()
        self.ventana.mainloop()

    def crearConexion(self):
        try:
            self.conexion = serial.Serial("COM5",115200,timeout=1)
            messagebox.showinfo("Exitoso","Conectado a la esp32")
        except:
            messagebox.showerror("Error","Error al conectar")
        
    def recibir(self):
        #Creamos el canal de comunicacion con esp32
        self.crearConexion()
        while(True):
            datos = self.conexion.readline().strip()
            #Decodificamos el dato recibido para evitar contaminacion en la cadena de informacion
            texto = datos.decode("utf-8",errors='ignore')
            if datos != None:
                self.mensaje.config(text=f"{texto}")
                self.ventana.update_idletasks() #recargamos la pagina
            self.n += 1

            if self.n > 10:
                break
        
            time.sleep(0.1)
        self.n = 0
        self.conexion.close()

app = Principal()
app.inicio()

#Creamos el arrancador del archivo

if __name__=='__main__':
    app.inicio()