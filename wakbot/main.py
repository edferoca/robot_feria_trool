import lib
import time
import tkinter as tk
from tkinter import ttk
import time
import threading

def contar_hasta(n):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Ejemplo")
        self.funcion_seleccionada = tk.StringVar()

        self.crear_interfaz()

    def crear_interfaz(self):
        self.seleccion_funcion_frame = tk.Frame(self.root)
        self.seleccion_funcion_frame.pack(pady=15)

        label = tk.Label(self.seleccion_funcion_frame, text="Seleccione una función:")
        label.pack(anchor=tk.W)

        opciones = ["recorrido_herb_camp", "ruta_siembra", "ruta_recolecta"]
        self.funcion_combobox = ttk.Combobox(self.seleccion_funcion_frame, textvariable=self.funcion_seleccionada)
        self.funcion_combobox['values'] = opciones
        self.funcion_combobox.pack()

        self.confirmar_btn = tk.Button(self.root, text="Aceptar", command=self.confirmar_seleccion)
        self.confirmar_btn.pack(pady=10)

    def confirmar_seleccion(self):
        funcion = self.funcion_seleccionada.get()
        if funcion:
            self.seleccion_funcion_frame.pack_forget()
            self.confirmar_btn.pack_forget()

            confirmacion_label = tk.Label(self.root, text=f"Función seleccionada: {funcion}")
            confirmacion_label.pack()

            self.parametros_frame = tk.Frame(self.root)
            self.parametros_frame.pack(pady=15)

            if funcion == "recorrido_herb_camp":
                self.param1_var = tk.BooleanVar()
                self.param2_var = tk.BooleanVar()
                self.param3_var = tk.BooleanVar()

                self.crear_checkbox_parametro("Tijera o Segar", self.param1_var)
                self.crear_checkbox_parametro("Siembra", self.param2_var)
                self.crear_checkbox_parametro("Recolecta", self.param3_var)

            self.ejecutar_btn = tk.Button(self.root, text="Ejecutar", command=self.iniciar_ejecucion)
            self.ejecutar_btn.pack(pady=15)

    def crear_checkbox_parametro(self, label_text, variable):
        frame = tk.Frame(self.parametros_frame)
        frame.pack(pady=2)
        label = tk.Label(frame, text=label_text)
        label.pack(side=tk.LEFT)
        checkbox = tk.Checkbutton(frame, variable=variable)
        checkbox.pack(side=tk.LEFT)

    def iniciar_ejecucion(self):
        self.parametros_frame.pack_forget()
        self.ejecutar_btn.pack_forget()

        contador_label = tk.Label(self.root, text="", font=("Helvetica", 32))
        contador_label.pack(pady=20)

        def cuenta_regresiva():
            for i in range(3, 0, -1):
                contador_label.config(text=str(i))
                self.root.update()
                time.sleep(1)

            contador_label.config(text="Ejecutando función...")
            self.root.update()
            time.sleep(1)
            contador_label.pack_forget()

            # Obtener los parámetros y ejecutar la función en un hilo separado
            funcion = self.funcion_seleccionada.get()
            if funcion == "recorrido_herb_camp":
                param1 = self.param1_var.get()
                param2 = self.param2_var.get()
                param3 = self.param3_var.get()
                thread = threading.Thread(target=lib.recorrido_herb_camp, args=(root,param1, param2, param3))
        
            elif funcion == "ruta_siembra":
                thread = threading.Thread(target=lib.ruta_siembra)
            elif funcion == "ruta_recolecta":
                thread = threading.Thread(target=lib.ruta_recolecta, args=(["acción1", "acción2"],))
            thread.start()

        threading.Thread(target=cuenta_regresiva).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()