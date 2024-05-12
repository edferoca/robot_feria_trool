

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
tala_recurso = "img/talar.png"
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
    
    CapitanMiau=pyautogui.locateOnScreen(imagen,confidence=0.5,region=(0,500,800,600))
    #print("capitan Miau?")
    if CapitanMiau is None:
        #print("no era el capitan")
        pass
    else:
        bot.send_message(906440079,"<b>!capitanmiau</b>",parse_mode="html")
        abrir_ventana()
        pyautogui.moveTo(direcciones.get('centro'))

def ejecutar_accion(direccion, accion):
    # esta funcion recoje o tala un recurso segun se especifique en la pos determinada
    pyautogui.click(direcciones.get(direccion), button='right')
    time.sleep(1)
    
    # Realizar clicks en los pixeles circundantes para activar la acción
    for offset_x in range(-3, 4):
        for offset_y in range(-3, 4):
            
            pyautogui.click(direcciones.get(direccion)[0] + offset_x, 
                            direcciones.get(direccion)[1] + offset_y, 
                            button='right')
            print(f'hola{direcciones.get(direccion)[0] + offset_x},{direcciones.get(direccion)[1] + offset_y}')
            time.sleep(0.5)
            # buscar la accion a realizar
            confirmacion = pyautogui.locateOnScreen(accion, confidence=0.8, region=(0, 0, 800, 600))
            time.sleep(0.4)
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

"""
def ejecutar_accion(direccion,accion):
    ## esta funcion recoje o tala un recurso segun se especifique en la  pos determinada
    pyautogui.click(direcciones.get(direccion),button='right')
    time.sleep(2)
    #buscara la accion a realizar
    confirmacion=pyautogui.locateOnScreen(accion,confidence=0.8,region=(0,0,800,600))
    
    time.sleep(0.4)
    #si la accion esta disponible la eejecutara, si no pues pasa
    if confirmacion is None:
        pass
    else:
        confirmacion_pos = pyautogui.center(confirmacion)
        #mueve el mouse al lugar de la accion y le ejecuta
        pyautogui.moveTo(confirmacion_pos)
        pyautogui.click(button='left')
        #tiempo de espera para recolectar
        time.sleep(5)
        #reviso si aparece el capitan miau
        CapitanMiau(capitanMiau_img)   
        
     """   
    
######################
# funciones sembrado
######################

def sembrado_seguro(direccion):
    sembrado = False
    while sembrado == False:
        #revisa si se ha sembrado algo en el lugar
        #acciones del raton para revisar
        for offset_x in range(-3, 4):
            for offset_y in range(-3, 4):
                
                pyautogui.click(direcciones.get(direccion)[0] + offset_x, 
                                direcciones.get(direccion)[1] + offset_y, 
                                button='right')
                time.sleep(0.5)
                pyautogui.click(direcciones.get(direccion)[0] + offset_x, 
                                direcciones.get(direccion)[1] + offset_y, 
                                button='right')
                time.sleep(1)
                #revisa que la imagen que confirma sea correcta
                # buscar la accion a realizar
                confirmacion=pyautogui.locateOnScreen(siembraSegura,confidence=0.8,region=(0,0,800,600))
                time.sleep(0.4)
                #si es correcta o no cambia el estado del indicador "sembrado" para salir del bucle
                if confirmacion is None:
                    # escojo la semilla a cultivar (esta en  los atajos rapidos de wakfu)
                    pyautogui.press('3')
                    #siembra
                    pyautogui.click(direcciones.get(direccion),button='left')
                    time.sleep(3) 
                else:
                        sembrado = True
                        print(f'hola{direcciones.get(direccion)[0] + offset_x},{direcciones.get(direccion)[1] + offset_y}')
                        break
            else:
                continue
            break

            

######################
# funciones recorrido
######################
        

def recorrido_de_accion(direccion_recorrido,accion):
    if len(accion) == 1:
        sembrado_seguro("derecha")
        sembrado_seguro("adelante")
        sembrado_seguro("izquierda")
    else:
        ejecutar_accion("derecha",accion[0])
        ejecutar_accion("derecha",accion[1])
        ejecutar_accion("adelante",accion[0])
        ejecutar_accion("adelante",accion[1])
        ejecutar_accion("izquierda",accion[0])
        ejecutar_accion("izquierda",accion[1])
    
        
    time.sleep(2) 
    pyautogui.click(direcciones.get(direccion_recorrido),button='left')
    time.sleep(2) 
    
def ruta(acciones):
    for i in range(4):
        for i in range(3):
            recorrido_de_accion('derecha',acciones)
        for i in range(2):
            recorrido_de_accion('adelante',acciones)
        for i in range(3):
            recorrido_de_accion('izquierda',acciones)
        for i in range(2):
            recorrido_de_accion('adelante',acciones)

######################
# ejecucion programa
######################

bot.send_message(906440079,"recolecta iniciada")
siembre = [recojida_semilla]
reco_y_tala=[recojida_semilla,tala_recurso]

print('inicia la siembra')
ruta(siembre)

for i in range(8):
    pyautogui.click(direcciones.get('atras2'),button='left')
    time.sleep(1) 
print('esperar a que cresca algo')
time.sleep(150)  
print('inicia la recolecta')
ruta(reco_y_tala)

for i in range(8):
    pyautogui.click(direcciones.get('atras2'),button='left')
    time.sleep(1) 
    

bot.send_message(906440079,"siembra terminada")