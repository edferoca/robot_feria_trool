from .comunication import *
import tkinter as tk
import pyautogui,time, os

__all__=['CapitanMiau']

###################
# funcioes de visualizacion
###################
def cerrar_ventana():
    ventana.destroy()

def contar(ventana):
    label_contador = tk.Label(ventana, font=("Helvetica", 32))
    label_contador.pack(pady=20)

    for i in range(5, 0, -1):
        label_contador.config(text=str(i))
        ventana.update()
        time.sleep(1)

    ventana.destroy()

def abrir_ventana():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("150x150+850+400")
    boton_cerrar = tk.Button(ventana, text="Cerrar", command=lambda: iniciar_conteo(ventana))
    boton_cerrar.place(relx=0.5, rely=0.5, anchor="center")
    ventana.mainloop()

def iniciar_conteo(ventana):
    ventana.after(0, contar, ventana)

def capture_screen_region(left, top, width, height):
    # Determinar la ruta de guardado relativa al archivo actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    destination_folder = os.path.join(current_dir, os.pardir, 'img_IA')  
    # Buscar el siguiente número disponible para nombrar la imagen
    existing_files = os.listdir(destination_folder)
    existing_numbers = [int(f.split('.')[0]) for f in existing_files if f.split('.')[0].isdigit()]
    next_number = max(existing_numbers) + 1 if existing_numbers else 1
    output_path = os.path.join(destination_folder, f'{next_number}.png')
    # Capturar la región de la pantalla
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    # Guardar la imagen
    screenshot.save(output_path)
    print(f"Imagen guardada en: {output_path}")
    



###################
# funcion principal de CapitanMiau
###################

def CapitanMiau(imagen, direccion_final, root):
    CapitanMiau = pyautogui.locateOnScreen(imagen, confidence=0.5, region=(0, 400, 800, 600))
    if CapitanMiau is None:
        pass
    else:
        pyautogui.click(600,500,button='left')
        capture_screen_region(0,0,600,800)
        send_telegram_msg("<b>!capitanmiau</b>")
        print("!capitanmiau")
        abrir_ventana()
        root.after(5000, lambda: pyautogui.moveTo(direccion_final))
        