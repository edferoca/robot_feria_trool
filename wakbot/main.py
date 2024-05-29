#import lib
import time
import tkinter as tk
from tkinter import ttk
import time
import threading
import os

def contar_hasta(n):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Wakbot - beta 2.0")
        icon_path = os.path.join(os.path.dirname(__file__), "img/portada.ico")
        root.iconbitmap(icon_path)
        self.root.geometry("400x300+850+400")
        
        self.frames = []  # Lista para almacenar los marcos de las ventanas

        self.funcion_seleccionada = tk.StringVar()

        self.opciones = [
            (" Herbolario / campecino", os.path.join(os.path.dirname(__file__),"img/herbCampe.png")),
            (" Leñador",  os.path.join(os.path.dirname(__file__),"img/calar2.png")),
            (" Pocimas espanto",  os.path.join(os.path.dirname(__file__),"img/espanto.png"))
        ]

        self.crear_interfaz()

    def crear_interfaz(self):
        self.seleccion_funcion_frame = tk.Frame(self.root)
        self.seleccion_funcion_frame.pack(pady=15)

        # Crear un botón que abrirá el menú personalizado
        self.menu_button = tk.Menubutton(self.seleccion_funcion_frame, text="Seleccionar función", relief=tk.RAISED)
        self.menu = tk.Menu(self.menu_button, tearoff=0)

        # Cargar imágenes y agregar opciones al menú
        self.images = []
        for text, image_path in self.opciones:
            image = tk.PhotoImage(file=image_path)
            self.images.append(image)  
            self.menu.add_command(label=text, image=image, compound=tk.LEFT, command=lambda t=text: self.seleccionar_funcion(t))

        self.menu_button["menu"] = self.menu
        self.menu_button.pack()

    def seleccionar_funcion(self, text):
        self.funcion_seleccionada.set(text)
        print(f"Función seleccionada: {text}")

        # Actualizar la interfaz para confirmar la selección y mostrar los parámetros
        self.confirmar_seleccion()

    def confirmar_seleccion(self):
        funcion = self.funcion_seleccionada.get()
        if funcion:
            self.volver_atras()  # Volver a la ventana anterior antes de crear una nueva
            frame = tk.Frame(self.root)
            frame.pack()
            self.frames.append(frame)  # Agregar el nuevo marco a la lista
            confirmacion_label = tk.Label(frame, text=f"Función seleccionada: {funcion}")
            confirmacion_label.pack()

            self.parametros_frame = tk.Frame(frame)
            self.parametros_frame.pack(pady=15)

            if funcion == " Herbolario / campecino":
                self.param1_var = tk.BooleanVar()
                self.param2_var = tk.BooleanVar()
                self.param3_var = tk.BooleanVar()

                self.menu_desplegable_parametro("Tijera o Segar", ["Tijera", "Segar"], self.param1_var)
                self.crear_checkbox_parametro("Siembra", self.param2_var)
                self.crear_checkbox_parametro("Recolecta", self.param3_var)

            self.ejecutar_btn = tk.Button(frame, text="Ejecutar", command=self.iniciar_ejecucion)
            self.ejecutar_btn.pack(pady=15)
    
    def menu_desplegable_parametro(self, label_text, opciones, variable):
        def actualizar_parametro(event):
            if variable.get() == "Tijera":
                variable.set(True)
            else:
                variable.set(False)

        frame = tk.Frame(self.parametros_frame)
        frame.pack(pady=2)
        label = tk.Label(frame, text=label_text)
        label.pack(side=tk.LEFT)
        menu = ttk.Combobox(frame, values=opciones, state="readonly")
        menu.pack(side=tk.LEFT)
        menu.bind("<<ComboboxSelected>>", actualizar_parametro)

    def crear_checkbox_parametro(self, label_text, variable):
        frame = tk.Frame(self.parametros_frame)
        frame.pack(pady=2)
        label = tk.Label(frame, text=label_text)
        label.pack(side=tk.LEFT)
        checkbox = tk.Checkbutton(frame, variable=variable)
        checkbox.pack(side=tk.LEFT)

    def volver_atras(self):
        if self.frames:
            frame = self.frames.pop()  # Obtener el último marco de la lista
            frame.pack_forget()  # Ocultar el marco

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
            if funcion == " Herbolario / campecino":
                param1 = self.param1_var.get()
                param2 = self.param2_var.get()
                param3 = self.param3_var.get()
                thread = threading.Thread(target=recorrido_herb_camp, args=(root,param1, param2, param3,))
            elif funcion == " Leñador":
                thread = threading.Thread(target=ruta_siembra)
            elif funcion == " Pocimas espanto":
                thread = threading.Thread(target=ruta_recolecta, args=(["acción1", "acción2"],))
            thread.start()

        threading.Thread(target=cuenta_regresiva).start()

def recorrido_herb_camp(root,param1, param2, param3, ):
    print(f'aqui iria una funcion: {param1}, {param2}, {param3}')
    
def ruta_siembra():
    print(f'ahola')
def ruta_recolecta():
    print(f'adios')

if __name__ == "__main__":
    root = tk.Tk()
    
    app = App(root)
    root.mainloop()