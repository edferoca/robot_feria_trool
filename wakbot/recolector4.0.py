

import pyautogui, sys, time
import telebot


TOKEN = "5793926590:AAFpP0gB_pEekRuw4Qk9jVX3jwKcILyHrYA"

bot=telebot.TeleBot(TOKEN)
centro=[400,300]

direcciones ={
    "centro":[400,307],
    "adelante":[442,329],
    "adelante2" : [484,351], #para no tener obstaculos
    "atras":[358,285],
    "atras2":[316,263],
    "derecha":[358,329],
    "derecha2" : [316,351],
    "izquierda":[442,285],
    "izquierda2":[484,263]
}

recojida_semilla = "img\seleccion.png"
tala_recurso = "img\talar.png"
capitanMiau_img = "img\capitan_miau_3.png"

def CapitanMiau(imagen):
    
    CapitanMiau=pyautogui.locateOnScreen(imagen,confidence=0.7,region=(0,500,800,600))
    #print("capitan Miau?")
    if CapitanMiau is None:
        #print("no era el capitan")
        pass
    else:
        bot.send_message(906440079,"<b>!capitanmiau</b>",parse_mode="html")
        paso=input("presione 1 si ya paso:")  
        time.sleep(5)
        pyautogui.moveTo(direcciones.get('centro'))

def ejecutar_accion(direccion,accion):
    ## esta funcion recoje o tala un recurso segun se especifique en la  pos determinada
    pyautogui.click(direcciones.get(direccion),button='right')
    time.sleep(1)
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
        time.sleep(3.5)
        #reviso si aparece el capitan miau
        CapitanMiau(capitanMiau_img)   
        
        
    
######################
# funciones Terciarias
######################



            

   
        
######################
# funciones Primarias
######################
def recorrido_de_siembra(direccion_recorrido,accion):
    
    ejecutar_accion("derecha",accion)
    ejecutar_accion("adelante",accion)
    ejecutar_accion("izquierda",accion)
    time.sleep(2) 
    pyautogui.click(direcciones.get(direccion_recorrido),button='left')

######################
# ejecucion programa
######################

bot.send_message(906440079,"recolecta iniciada")

for i in range(4):
    for i in range(3):
        recorrido_de_siembra('derecha',recojida_semilla)
    for i in range(2):
        recorrido_de_siembra('adelante',recojida_semilla)
    for i in range(3):
        recorrido_de_siembra('izquierda',recojida_semilla)
    for i in range(2):
        recorrido_de_siembra('adelante',recojida_semilla)


bot.send_message(906440079,"siembra terminada")