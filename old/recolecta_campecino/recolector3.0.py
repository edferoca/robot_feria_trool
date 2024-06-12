import variables as v
import pyautogui, sys, time
import telebot

TOKEN = "5793926590:AAFpP0gB_pEekRuw4Qk9jVX3jwKcILyHrYA"
bot=telebot.TeleBot(TOKEN)

centroX=400
centroY=300
centro=[400,300]
direcciones ={
    "adelante":[445,330],
    "adelante2" : [495,352], #para no tener obstaculos
    "atras":[360,290],
    "derecha":[360,330],
    "derecha2" : [310,360],
    "izquierda":[440,288],
    "izquierda2":[495,260]
}

semilla='gracia.png'

def moverse(direccion,boton):
    pyautogui.click(direccion[0],direccion[1],button=boton)
    time.sleep(1)

def recolectar(direccion):
   # print(f'esta sembrada la parcela: { verificador_recolecta(direccion)}')  
    verificador= verificador_recolecta(direccion)
    while verificador_recolecta(direccion) == True:
        ejecuta_recolecta(direccion)
    if verificador_recolecta(direccion) == False:
        CapitanMiau(direccion)
  
        

######################
#funciones secundarias
######################

#funcion se hubica en la direccion desea y realiza el porceso de recolectar,
# o segar o ver si es el capitan miu dependidodne de loque se requeira,
def ejecuta_recolecta(direccion):
    moverse(direccion,'right')
    #print(direccion)
    time.sleep(0.8)
    ManitaRecolecta=pyautogui.locateOnScreen('seleccion.png',confidence=0.9,region=(0,0,794,558))
    if ManitaRecolecta is None:
        moverse(direccion,'right')
        pinzaRecolecta=pyautogui.locateOnScreen('talar.png',confidence=0.9,region=(0,0,800,600))
        time.sleep(0.4)
        #print(1)
        if pinzaRecolecta is None:
            time.sleep(3)
            CapitanMiau(direccion)
            #print(2)
            time.sleep(5)
        else:
            #print("corte")
            pinzaRecolecta_pos=pyautogui.center(pinzaRecolecta)
            pyautogui.moveTo(pinzaRecolecta_pos)
            pyautogui.click(button='left')
            time.sleep(3)          
    else:
        #print("manita")
        ManitaRecolecta_pos=pyautogui.center(ManitaRecolecta)
        pyautogui.moveTo(ManitaRecolecta_pos)
        pyautogui.click(button='left')
        time.sleep(3)

def verificador_recolecta(direccion):  
    pyautogui.moveTo(direccion[0],direccion[1])
    time.sleep(0.5)
    confirmacion=pyautogui.locateOnScreen(semilla,confidence=0.6,region=(0,0,800,600))
    time.sleep(0.4)
    if confirmacion is None:
            sembrado=False
            #print("no")
    else:
            sembrado=True
            #print("si")
   
    return sembrado

######################
# funciones Terciarias
######################

    
def CapitanMiau(direccion):
    
    CapitanMiau=pyautogui.locateOnScreen('capitan_miau_2.png',confidence=0.6,region=(400,400,800,600))
    #print("capitan Miau?")
    if CapitanMiau is None:
        #print("no era el capitan")
        pass
    else:
        bot.send_message(906440079,"<b>!capitanmiau</b>",parse_mode="html")
        paso=input("presione 1 si ya paso:")  
        while verificador_recolecta(direccion) == True:
            ejecuta_recolecta(direccion)




def recolectar_y_desplazarse(tipo,IdaVuelta):
    if IdaVuelta == 'ida':
        sentido='derecha'
        setnidoContrario='izquierda'
    elif IdaVuelta == 'vuelta':
        sentido='izquierda'
        setnidoContrario='derecha'
    if tipo == 1:
        recolectar(direcciones.get('adelante'))
        #print('paso a siguietne parcela')
        recolectar(direcciones.get(sentido))
        moverse(direcciones.get(sentido),'left')
    if tipo == 2:
        recolectar(direcciones.get(setnidoContrario))
        recolectar(direcciones.get('adelante'))
        recolectar(direcciones.get(sentido))
        moverse(direcciones.get(sentido),'left')
    if tipo == 3:
        recolectar(direcciones.get('adelante'))
        recolectar(direcciones.get(sentido))
        moverse(direcciones.get('adelante'),'left')


bot.send_message(906440079,"recolecta iniciada")

recolectar_y_desplazarse(1,'ida')
for i in range(4):
    recolectar_y_desplazarse(2,'ida')
    for i in range(2):
        recolectar_y_desplazarse(1,'ida')
    recolectar_y_desplazarse(3,'ida')
    recolectar_y_desplazarse(3,'ida')
    recolectar_y_desplazarse(2,'vuelta')
    for i in range(2):
        recolectar_y_desplazarse(1,'vuelta')
    recolectar_y_desplazarse(3,'vuelta')
    recolectar_y_desplazarse(3,'vuelta')
    #v.moverse(v.direcciones.get('adelante'),'left')
recolectar_y_desplazarse(2,'ida')   
for i in range(3):
        recolectar_y_desplazarse(1,'ida') 
moverse(centro,'right')
bot.send_message(906440079,"siembra terminada")
