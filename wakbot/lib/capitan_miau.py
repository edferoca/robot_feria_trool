from .comunication import *
import tkinter as tk
import pyautogui,time

__all__=['CapitanMiau']

###################
# funcioes de visualizacion
###################
def cerrar_ventana():
    ventana.destroy()

def contar():
    for i in range(4, 0, -1):
        print(i)
        time.sleep(1)

def abrir_ventana():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("150x150")
    boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
    boton_cerrar.place(relx=0.5, rely=0.5, anchor="center")
    ventana.mainloop()
    contar()


###################
# funcion principal de CapitanMiau
###################

def CapitanMiau(imagen,direccion_final):
    
    CapitanMiau=pyautogui.locateOnScreen(imagen,confidence=0.5,region=(0,400,800,600))
    #print("capitan Miau?")
    if CapitanMiau is None:
        #print("no era el capitan")
        pass
    else:
        send_telegram_msg("<b>!capitanmiau</b>")
        abrir_ventana()
        pyautogui.moveTo(direccion_final)
