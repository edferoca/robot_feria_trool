import pyautogui, sys, time
import pywhatkit
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

siembraSegura = "img\siembra_segura.png"
contador_sembrado=0
limite_siembra_por_sembrado=1



def sembrado_seguro(direccion):
    sembrado = False
    while sembrado == False:
        #revisa si se ha sembrado algo en el lugar
        #acciones del raton para revisar
        pyautogui.click(direcciones.get(direccion),button='right')
        time.sleep(0.5)
        pyautogui.click(direcciones.get(direccion),button='right')
        time.sleep(1)
        #revisa que la imagen que confirma sea correcta
        confirmacion=pyautogui.locateOnScreen(siembraSegura,confidence=0.8,region=(0,0,800,600))
        time.sleep(0.4)
        #si es correcta o no cambia el estado del indicador "sembrado" para salir del bucle
        if confirmacion is None:
            # escojo la semilla a cultivar (esta en  los atajos rapidos de wakfu)
            pyautogui.press('6')
            #siembra
            pyautogui.click(direcciones.get(direccion),button='left')
            time.sleep(3) 
        else:
                sembrado = True
        

def recorrido_de_siembra(direccion_recorrido):
    
    sembrado_seguro("derecha")
    sembrado_seguro("adelante")
    sembrado_seguro("izquierda")
    time.sleep(2) 
    pyautogui.click(direcciones.get(direccion_recorrido),button='left')

 
    
bot.send_message(906440079,"siembra iniciada")
pyautogui.click(centro[0],centro[1],button='right')
for i in range(4):
    for i in range(3):
        recorrido_de_siembra('derecha')
    for i in range(2):
        recorrido_de_siembra('adelante')
    for i in range(3):
        recorrido_de_siembra('izquierda')
    for i in range(2):
        recorrido_de_siembra('adelante')



bot.send_message(906440079,"siembra terminada")