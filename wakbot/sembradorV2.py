import pyautogui, sys, time
import pywhatkit
import telebot 
TOKEN = "5793926590:AAFpP0gB_pEekRuw4Qk9jVX3jwKcILyHrYA"

bot=telebot.TeleBot(TOKEN)
centro=[400,300]

direcciones ={
    "centro":[400,307],
    "adelante":[442,307],
    "adelante2" : [484,307], #para no tener obstaculos
    "atras":[358,307],
    "atras2":[316,307],
    "derecha":[400,329],
    "derecha2" : [400,351],
    "izquierda":[400,285],
    "izquierda2":[400,263]
}

siembraSegura = "img\siembra_segura.png"
contador_sembrado=0
limite_siembra_por_sembrado=1

def moverse(direccion,boton='left'):
    pyautogui.click(direccion[0],direccion[1],button=boton)
    time.sleep(3)

def sembrado_seguro():
    #me ubico en  pos central (segura)
    pyautogui.click(direcciones.get('centro'),button='left')
    # escojo la semilla a cultivar (esta en  los atajos rapidos de wakfu)
    pyautogui.press('6')
    #siembra
    pyautogui.click(direcciones.get('derecha'),button='left')
    time.sleep(3)
    pyautogui.click(direcciones.get('derecha'),button='right')
    time.sleep(1)
    pyautogui.click(direcciones.get('derecha'),button='right')
    time.sleep(2)
    confirmacion=pyautogui.locateOnScreen(siembraSegura,confidence=0.5,region=(0,0,800,600))
    time.sleep(0.4)
    if confirmacion is None:
            sembrado=0
            print("no sembro")
    else:
            print("si sembpro")
            sembrado=1
    return sembrado

def sembrando(limite_siembra,poscicion,contador_sembrado):
    
    while contador_sembrado < limite_siembra:
        #caso para  la segunda casilla
        if limite_siembra == 3 :
            moverse(direcciones.get('izquierda'))
        moverse(direcciones.get('adelante'))
        moverse(direcciones.get(poscicion))
        time.sleep(0.7)
        contador_sembrado=0
        pyautogui.moveTo(centro[0],centro[1])
        #caso para  la segunda casilla
        if limite_siembra == 3 :
            contador_sembrado += sembrado(direcciones.get('izquierda'))
        contador_sembrado += sembrado(direcciones.get('adelante'))
        contador_sembrado += sembrado(direcciones.get(poscicion))
        
        #print(contador_sembrado)
    
bot.send_message(906440079,"siembra iniciada")
pyautogui.click(centro[0],centro[1],button='right')


sembrado_seguro()


  
pyautogui.click(centro[0],centro[1],button='right')
bot.send_message(906440079,"siembra terminada")