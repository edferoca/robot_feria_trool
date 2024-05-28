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

        self.funcion_seleccionada = tk.StringVar(value="recorrido_herb_camp")

        # Crear los botones de selección de función
        self.crear_seleccion_funcion()

        # Crear el marco para los parámetros de entrada
        self.parametros_frame = tk.Frame(root)
        self.parametros_frame.pack(pady=10)

        # Crear el botón de ejecutar
        self.ejecutar_btn = tk.Button(root, text="Ejecutar", command=self.ejecutar_funcion)
        self.ejecutar_btn.pack(pady=10)

        # Crear la barra de progreso
        self.progress_var = tk.IntVar()
        self.progress_bar = ttk.Progressbar(root, maximum=100, variable=self.progress_var)
        self.progress_bar.pack(pady=10)

        # Crear los campos de entrada de parámetros para la función seleccionada
        self.actualizar_parametros()

    def crear_seleccion_funcion(self):
        opciones = [("Recorrido Herb Camp", "recorrido_herb_camp"),
                    ("Recorrido Leñador", "recorrido_leñador"),
                    ("Recorrido Espanto", "recorrido_espanto")]
        for (texto, valor) in opciones:
            radio_btn = tk.Radiobutton(self.root, text=texto, variable=self.funcion_seleccionada, value=valor, command=self.actualizar_parametros)
            radio_btn.pack(anchor=tk.W)

    def actualizar_parametros(self):
        for widget in self.parametros_frame.winfo_children():
            widget.destroy()

        funcion = self.funcion_seleccionada.get()
        if funcion == "recorrido_herb_camp":
            self.param1_entry = self.crear_entrada_parametro("Param 1")
            self.param2_entry = self.crear_entrada_parametro("Param 2")
        elif funcion == "recorrido_leñador":
            self.param1_entry = self.crear_entrada_parametro("Param 1")
            self.param2_entry = self.crear_entrada_parametro("Param 2")
            self.param3_entry = self.crear_entrada_parametro("Param 3")
        elif funcion == "recorrido_espanto":
            self.param1_entry = self.crear_entrada_parametro("Param 1")

    def crear_entrada_parametro(self, label_text):
        frame = tk.Frame(self.parametros_frame)
        frame.pack(pady=2)
        label = tk.Label(frame, text=label_text)
        label.pack(side=tk.LEFT)
        entry = tk.Entry(frame)
        entry.pack(side=tk.LEFT)
        return entry

    def ejecutar_funcion(self):
        funcion = self.funcion_seleccionada.get()
        if funcion == "recorrido_herb_camp":
            param1 = self.param1_entry.get()
            param2 = self.param2_entry.get()
            thread = threading.Thread(target=lib.recorrido_herb_camp, args=(param1, param2, self.progress_var))
        elif funcion == "recorrido_leñador":
            param1 = self.param1_entry.get()
            param2 = self.param2_entry.get()
            param3 = self.param3_entry.get()
            thread = threading.Thread(target=lib.recorrido_leñador, args=(param1, param2, param3, self.progress_var))
        elif funcion == "recorrido_espanto":
            param1 = self.param1_entry.get()
            thread = threading.Thread(target=lib.recorrido_espanto, args=(param1, self.progress_var))
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
