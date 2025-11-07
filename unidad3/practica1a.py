import serial
from tkinter import *
from tkinter import messagebox
import threading
import time

class Principal():
    def __init__(self):
        self.ven = Tk()
        self.ven.title("Lector Serial ESP32")

        # Dimensiones de ventana
        ancho_ventana = 400
        alto_ventana = 200

        # Centrar ventana
        ancho_pantalla = self.ven.winfo_screenwidth()
        alto_pantalla = self.ven.winfo_screenheight()
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        self.ven.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        self.conexion = None
        self.running = False

    def recibir_datos(self):
        """que lee datos del puerto serial sin congelar la interfaz"""
        while self.running:
            if self.conexion and self.conexion.in_waiting > 0:
                try:
                    datos = self.conexion.readline().decode('utf-8').strip()
                    if datos:
                        self.mensaje.config(text=f"Distancia: {datos} cm")
                except:
                    pass
            time.sleep(0.1)

    def recibir(self):
        """Inicia la lectura continua"""
        if not self.conexion:
            try:
                self.conexion = serial.Serial('COM5', 115200, timeout=1)
                messagebox.showinfo("Éxito", "Conectado al puerto COM5")
            except:
                messagebox.showerror("Error", "No se pudo conectar al puerto COM5")
                return

        self.running = True
        hilo = threading.Thread(target=self.recibir_datos)
        hilo.daemon = True
        hilo.start()

    def detener(self):
        #Detiene la lectura
        self.running = False
        if self.conexion:
            self.conexion.close()
            self.conexion = None
            messagebox.showinfo("Info", "Conexión cerrada")

    def inicio(self):
        self.mensaje = Label(self.ven, text="Esperando datos...", font=("Arial", 12))
        self.mensaje.place(x=10, y=10)

        Button(self.ven, text='Iniciar lectura', command=self.recibir).place(x=10, y=50)
        Button(self.ven, text='Detener', command=self.detener).place(x=120, y=50)

        self.ven.protocol("WM_DELETE_WINDOW", self.detener)
        self.ven.mainloop()

if __name__ == "__main__":
    app = Principal()
    app.inicio()
