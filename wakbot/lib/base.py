import telebot
import time


#base variables for the diferents works
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

mano_recojida = "img\seleccion.png"
tijera_recurso = "img\calar.png"
segar_recurso = "img/segar.png"
talar_recurso = "img\calar2.png"
siembraSegura = "img\siembra_segura.png"
capitanMiau_img = "img\capitan_miau_3.png"

###################
# funcion Telegram
###################
TOKEN = "5793926590:AAFpP0gB_pEekRuw4Qk9jVX3jwKcILyHrYA"

bot=telebot.TeleBot(TOKEN)

def send_telegram_msg(texto):
    bot.send_message(906440079,texto,parse_mode="html")


###################
# funcion CapitanMiau
###################

def CapitanMiau(imagen):
    
    CapitanMiau=pyautogui.locateOnScreen(imagen,confidence=0.5,region=(0,400,800,600))
    #print("capitan Miau?")
    if CapitanMiau is None:
        #print("no era el capitan")
        pass
    else:
        send_telegram_msg("<b>!capitanmiau</b>"):
        abrir_ventana()
        pyautogui.moveTo(direcciones.get('centro'))