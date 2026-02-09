import pyautogui, sys, time
import pywhatkit
import telebot
TOKEN = "5793926590:AAFpP0gB_pEekRuw4Qk9jVX3jwKcILyHrYA"

bot=telebot.TeleBot(TOKEN)

centroX=400
centroY=300

def recolectar():
    time.sleep(0.4)
    manita=pyautogui.locateOnScreen('seleccion.png',confidence=0.9,region=(0,0,794,558))
    time.sleep(0.4)
    if manita is None:
        CapitanMiau()
        time.sleep(5)
    else:

        manita_pos=pyautogui.center(manita)
        pyautogui.moveTo(manita_pos)
        pyautogui.click(button='left')
        time.sleep(3)
        

def talar():
    time.sleep(0.4)
    pinza=pyautogui.locateOnScreen('talar.png',confidence=0.9,region=(0,0,800,600))
    time.sleep(0.4)
    if pinza is None:
        CapitanMiau()
        time.sleep(5)
    else:

        pinza_pos=pyautogui.center(pinza)
        pyautogui.moveTo(pinza_pos)
        pyautogui.click(button='left')
        time.sleep(3)
        
        
        
def CapitanMiau():
    time.sleep(5)
    CapitanMiau=pyautogui.locateOnScreen('capitan_miau_2.png',confidence=0.6,region=(400,400,800,600))
    print("capitan Miau?")
    if CapitanMiau is None:
        pass
    else:
        bot.send_message(906440079,"<b>!capitanmiau</b>",parse_mode="html")
        paso=input("presione 1 si ya paso:")   
        
    
               
    
#movimientos
def Derecha():
    pyautogui.click(360,330,button='right')
    recolectar()
    pyautogui.click(360,330,button='right')
    talar()
def Izquierda(): 
    pyautogui.click(440,280,button='right')
    recolectar()
    pyautogui.click(440,280,button='right')
    talar()
def Adelante(): 
    pyautogui.click(445,330,button='right')
    recolectar()
    pyautogui.click(445,330,button='right')
    talar()
def Atras(): 
    pyautogui.click(360,290,button='right')
    recolectar()
    pyautogui.click(360,290,button='right')
    talar()

#acciones
def ejecutar_accion(x,y,direccion):
    if direccion == "ida":
        Derecha()
        Adelante()
        time.sleep(3)
        pyautogui.click(centroX+x,centroY+y,button='left')
        time.sleep(0.6)
    elif direccion == "vuelta":
        Izquierda()
        Adelante()
        pyautogui.click(centroX+x,centroY+y,button='left')
        time.sleep(0.6)

bot.send_message(906440079,"recolecta iniciada")
    
ejecutar_accion(-50,30,"ida")
Izquierda()

    
for i in range(4):#5,5
#ida    
    for j in range(3):
        ejecutar_accion(-50,30,"ida")
        
    ejecutar_accion(50,30,"ida")
    ejecutar_accion(50,30,"ida")
    Derecha()
    
    for j in range(3):
        ejecutar_accion(50,-30,"vuelta")
    ejecutar_accion(50,30,"vuelta")
    ejecutar_accion(50,30,"vuelta")
    Izquierda()

    print(f"vualta: {i+1}")
for j in range(4):
        ejecutar_accion(-50,30,"ida")
print("tarea termianda")
bot.send_message(906440079,"recolecta Terminada")
