

import pyautogui, sys, time
import telebot
import tkinter as tk
import time


TOKEN = "5793926590:AAFpP0gB_pEekRuw4Qk9jVX3jwKcILyHrYA"

bot=telebot.TeleBot(TOKEN)
centro=[400,300]

direcciones ={
    "centro":[400,307],
    "adelante":[442,329],#"adelante":[442,329],
    "adelante2" : [484,351], #para no tener obstaculos
    "atras":[358,285],
    "atras2":[316,263],
    "derecha":[358,329],
    "derecha2" : [316,351],
    "izquierda":[442,285], #"izquierda":[442,285],
    "izquierda2":[484,263]
}

recojida_semilla = "img\seleccion.png"
tala_recurso = "img\calar.png"
#tala_recurso = "img/segar.png"
corta_arbol_recurso = "img\calar2.png"
capitanMiau_img = "img\capitan_miau_3.png"
siembraSegura = "img\siembra_segura.png"

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

######################
# funciones de recolecta y talla
######################

def CapitanMiau(imagen):
    
    CapitanMiau=pyautogui.locateOnScreen(imagen,confidence=0.5,region=(0,400,800,600))
    #print("capitan Miau?")
    if CapitanMiau is None:
        #print("no era el capitan")
        pass
    else:
        bot.send_message(906440079,"<b>!capitanmiau</b>",parse_mode="html")
        abrir_ventana()
        pyautogui.moveTo(direcciones.get('centro'))

def ejecutar_accion(direccion, accion):
        
    # Realizar clicks en los pixeles circundantes para activar la acción
    for offset_y in range(-3, 3):
        for offset_x in range(-1, 1):
            
            pyautogui.click(direcciones.get(direccion)[0] + offset_x, 
                            direcciones.get(direccion)[1] + offset_y, 
                            button='right')
           # print(f'hola{direcciones.get(direccion)[0] + offset_x},{direcciones.get(direccion)[1] + offset_y}')
            time.sleep(1)
            # buscar la accion a realizar
            confirmacion = pyautogui.locateOnScreen(accion, confidence=0.8, region=(0, 0, 520, 370)) #800, 600 
            time.sleep(0.8)
            # si la accion esta disponible la ejecutara, si no, pues pasa
            if confirmacion is None:
                
                pass
            else:
                confirmacion_pos = pyautogui.center(confirmacion)
                # mueve el mouse al lugar de la accion y le ejecuta
                pyautogui.moveTo(confirmacion_pos)
                pyautogui.click(button='left')
                # tiempo de espera para recolectar
                time.sleep(5)
                # reviso si aparece el capitan miau
                CapitanMiau(capitanMiau_img)
                break
        else:
            continue
        break


    
######################
# funciones sembrado
######################

def sembrado_seguro(direccion):
    sembrado = False
    while not sembrado:
        for offset_x in range(-3, 4):  # Cambiado de -3, 3 a -3, 4
            for offset_y in range(-1, 2):  # Cambiado de -1, 1 a -1, 2
                pyautogui.click(direcciones.get(direccion)[0] + offset_x, 
                                direcciones.get(direccion)[1] + offset_y, 
                                button='right')
                time.sleep(1)  # Aumentado el tiempo de espera
                pyautogui.click(direcciones.get(direccion)[0] + offset_x, 
                                direcciones.get(direccion)[1] + offset_y, 
                                button='right')
                time.sleep(1.5)  # Aumentado el tiempo de espera
                confirmacion = pyautogui.locateOnScreen(siembraSegura, confidence=0.7, region=(0, 0, 800, 600))
                time.sleep(0.8)  # Aumentado el tiempo de espera
                if confirmacion is None:
                    pyautogui.press('3')
                    time.sleep(1.2)  # Aumentado el tiempo de espera
                    pyautogui.click(direcciones.get(direccion), button='left')
                    time.sleep(3.5)  # Aumentado el tiempo de espera
                else:
                    sembrado = True
                    break
            if sembrado:
                break

            

######################
# funciones recorrido
######################
        


    
def ruta_siembra():
    #siembra recorriendo de derecha a izquierda 
    for i in range(16):
        sembrado_seguro("derecha")
        sembrado_seguro("atras")
        sembrado_seguro("izquierda")
        time.sleep(2) 
        pyautogui.click(direcciones.get("atras"),button='left')
        time.sleep(2)
    #sube tres casillas para empesar una nueva hilera 
    for i in range(3):
        sembrado_seguro("derecha")
        sembrado_seguro("atras")
        sembrado_seguro("izquierda")
        time.sleep(2) 
        pyautogui.click(direcciones.get("izquierda"),button='left')
        time.sleep(2) 
    for i in range(16):
        sembrado_seguro("derecha")
        sembrado_seguro("adelante")
        sembrado_seguro("izquierda")
        time.sleep(2) 
        pyautogui.click(direcciones.get("adelante"),button='left')
        time.sleep(2)
    for i in range(3):
        pyautogui.click(direcciones.get('derecha'),button='left')
        time.sleep(1) 

def ruta_simebra_arboles():
    sembrado_seguro("izquierda")
    time.sleep(2) 
    pyautogui.click(direcciones.get("atras"), button='left')
    time.sleep(2)
    for i in range(16):
        sembrado_seguro("derecha")
        sembrado_seguro("izquierda")
        time.sleep(2) 
        pyautogui.click(direcciones.get("atras"), button='left')
        time.sleep(2)
    sembrado_seguro("izquierda")
    time.sleep(2) 
    pyautogui.click(direcciones.get("derecha"), button='left')
    time.sleep(2) 
    pyautogui.click(direcciones.get("derecha"), button='left')
    time.sleep(2) 
    pyautogui.click(direcciones.get("derecha"), button='left')
    time.sleep(2) 
    sembrado_seguro("derecha")
    pyautogui.click(direcciones.get("adelante"), button='left')
    time.sleep(2) 
    for j in range(16):
        sembrado_seguro("derecha")
        sembrado_seguro("izquierda")
        time.sleep(2) 
        pyautogui.click(direcciones.get("adelante"), button='left')
        time.sleep(2)
    sembrado_seguro("izquierda")
    sembrado_seguro("derecha")
    
        
def ruta_recolecta(accion):
    for i in range(16):
        ejecutar_accion("derecha",accion[0])
        ejecutar_accion("derecha",accion[1])
        ejecutar_accion("atras",accion[0])
        ejecutar_accion("atras",accion[1])
        ejecutar_accion("izquierda",accion[0])
        ejecutar_accion("izquierda",accion[1])
        time.sleep(2) 
        pyautogui.click(direcciones.get("atras"),button='left')
        time.sleep(2) 
    for i in range(3):
        ejecutar_accion("derecha",accion[0])
        ejecutar_accion("derecha",accion[1])
        ejecutar_accion("atras",accion[0])
        ejecutar_accion("atras",accion[1])
        ejecutar_accion("izquierda",accion[0])
        ejecutar_accion("izquierda",accion[1])
        time.sleep(2) 
        pyautogui.click(direcciones.get("izquierda"),button='left')
        time.sleep(2) 
    for i in range(16):
        ejecutar_accion("derecha",accion[0])
        ejecutar_accion("derecha",accion[1])
        ejecutar_accion("adelante",accion[0])
        ejecutar_accion("adelante",accion[1])
        ejecutar_accion("izquierda",accion[0])
        ejecutar_accion("izquierda",accion[1])
        time.sleep(2) 
        pyautogui.click(direcciones.get("adelante"),button='left')
        time.sleep(2) 

def ruta_recolecta_arboles(accion):
    for i in range(17):
        ejecutar_accion("derecha",accion[0])
        ejecutar_accion("izquierda",accion[0])
        time.sleep(1) 
        pyautogui.click(direcciones.get("atras"),button='left')
        time.sleep(2) 
    #print("1")
    ejecutar_accion("derecha",accion[0])   
    #sube 2 casillas
    pyautogui.click(direcciones.get('izquierda'),button='left')
    time.sleep(1) 
    pyautogui.click(direcciones.get("adelante"),button='left')
    time.sleep(1) 
    for i in range(17):
        ejecutar_accion("izquierda",accion[0])
        time.sleep(1) 
        pyautogui.click(direcciones.get("adelante"),button='left')
        time.sleep(2) 
        #print(f'vualta{i} de vuelta')
    pyautogui.click(direcciones.get('izquierda'),button='left')
    time.sleep(1) 
    pyautogui.click(direcciones.get('izquierda'),button='left')
    time.sleep(1) 
    for i in range(17):
        ejecutar_accion("izquierda",accion[1])
        ejecutar_accion("izquierda",accion[1])
        time.sleep(1) 
        pyautogui.click(direcciones.get("atras"),button='left')
        time.sleep(2) 
        #print(f'vualta{i} de ida')
    

######################
# ejecucion programa
######################

bot.send_message(906440079,"siembra iniciada")
siembre = [recojida_semilla]
reco_y_tala=[recojida_semilla,tala_recurso]
corta_o_tala=[corta_arbol_recurso,tala_recurso]


"""
"""

print('inicia la siembra')
ruta_siembra()
#ruta_simebra_arboles()


  
print('esperar a que cresca algo')
bot.send_message(906440079,"siembra terminada")
#time.sleep(150)  
time.sleep(600)  


bot.send_message(906440079,"recolecta iniciada")

print('inicia la recolecta')
ruta_recolecta(reco_y_tala)

#ruta_recolecta_arboles(corta_o_tala)

for i in range(3):
    pyautogui.click(direcciones.get('derecha'),button='left')
    time.sleep(1) 

bot.send_message(906440079,"recolecta terminada")