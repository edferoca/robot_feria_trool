
import variables 
from variables import Cosntructor_Principal
import pyautogui, sys, time
import telebot



TOKEN = "5793926590:AAFpP0gB_pEekRuw4Qk9jVX3jwKcILyHrYA"
bot=telebot.TeleBot(TOKEN)

centroX=400
centroY=300
centro=[400,300]
direcciones ={
    "adelante":[445,330],
    "adelante2" : [495,352], 
    "atras":[360,290],
    "derecha":[360,330],
    "derecha2" : [310,360],
    "izquierda":[440,288],
    "izquierda2":[495,260]
}

semilla='gracia.png'
      
######################
# funciones Terciarias
######################

def moverse(direccion,boton):
    pyautogui.click(direccion[0],direccion[1],button=boton)
    time.sleep(1)
    
    
#funcion se hubica en la direccion desea y realiza el porceso de recolectar,
# o segar o ver si es el capitan miu dependidodne de loque se requeira,
def ejecuta_recolecta(direccion):
    moverse(direccion,'right')   
    time.sleep(0.8)
    ManitaRecolecta=pyautogui.locateOnScreen('seleccion.png',confidence=0.9,region=(0,0,794,558))
    if ManitaRecolecta is None:
        #print("no manita")
        pinzaRecolecta=pyautogui.locateOnScreen('talar.png',confidence=0.9,region=(0,0,800,600))
        if pinzaRecolecta is None:
            #print("no pinsa")
            #time.sleep(5)
            #CapitanMiau(direccion)
            pass
        else:
            #print("corte")
            pinzaRecolecta_pos=pyautogui.center(pinzaRecolecta)
            pyautogui.moveTo(pinzaRecolecta_pos)
            pyautogui.click(button='left')
            time.sleep(3.5)          
    else:
        #print("manita")
        ManitaRecolecta_pos=pyautogui.center(ManitaRecolecta)
        pyautogui.moveTo(ManitaRecolecta_pos)
        pyautogui.click(button='left')
        time.sleep(3.5)

def CapitanMiau(direccion):
    
    CapitanMiau=pyautogui.locateOnScreen('capitan_miau_3.png',confidence=0.7,region=(0,500,800,600))
    #print("capitan Miau?")
    if CapitanMiau is None:
        #print("no era el capitan")
        pass
    else:
        bot.send_message(906440079,"<b>!capitanmiau</b>",parse_mode="html")
        paso=input("presione 1 si ya paso:")  
        time.sleep(5)
        pyautogui.moveTo(centro[0],centro[1])
        
######################
#funciones secundarias
######################       

def verifica_y_recolecta(direccion):  
    pyautogui.moveTo(direccion[0],direccion[1])
    time.sleep(1)
    confirmacion=pyautogui.locateOnScreen(semilla,confidence=0.5,region=(0,0,800,600))
    time.sleep(1)
    if confirmacion is None:
            CapitanMiau(direccion)       
    else:
            ejecuta_recolecta(direccion)
            time.sleep(5)
            CapitanMiau(direccion)
            #print("si")
            

   
        
######################
# funciones Primarias
######################

def recolectar_y_desplazarse(tipo,IdaVuelta):
    if IdaVuelta == 'ida':
        sentido='derecha'
        setnidoContrario='izquierda'
    elif IdaVuelta == 'vuelta':
        sentido='izquierda'
        setnidoContrario='derecha'
    if tipo == 1:  
        #print('colecta1')
        verifica_y_recolecta(direcciones.get('adelante'))
        #print('colecta1a')
        verifica_y_recolecta(direcciones.get('adelante'))
        #print('colecta2')
        verifica_y_recolecta(direcciones.get(sentido))
        #print('colecta2a')
        verifica_y_recolecta(direcciones.get(sentido))
        #print('me meuvo')
        time.sleep(1.2)
        moverse(direcciones.get(sentido),'left')
    if tipo == 2:
        verifica_y_recolecta(direcciones.get(setnidoContrario))
        verifica_y_recolecta(direcciones.get(setnidoContrario))
        verifica_y_recolecta(direcciones.get('adelante'))
        verifica_y_recolecta(direcciones.get('adelante'))
        verifica_y_recolecta(direcciones.get(sentido))
        verifica_y_recolecta(direcciones.get(sentido))
        time.sleep(1.2)
        moverse(direcciones.get(sentido),'left')
    if tipo == 3:
        ejecuta_recolecta(direcciones.get('adelante'))
        ejecuta_recolecta(direcciones.get('adelante'))
        ejecuta_recolecta(direcciones.get(sentido))
        ejecuta_recolecta(direcciones.get(sentido))
        time.sleep(1.2)
        moverse(direcciones.get('adelante'),'left')


######################
# ejecucion programa
######################

bot.send_message(906440079,"recolecta iniciada")
recolectar_y_desplazarse(1,'ida')
for i in range(4):
    recolectar_y_desplazarse(2,'ida')
    print("1")
    for i in range(2):
        recolectar_y_desplazarse(1,'ida')
        print("2")
    recolectar_y_desplazarse(3,'ida')
    print("3")
    recolectar_y_desplazarse(3,'ida')
    print("4")
    recolectar_y_desplazarse(2,'vuelta')
    print("5")
    for i in range(2):
        recolectar_y_desplazarse(1,'vuelta')
        print("6")
    recolectar_y_desplazarse(3,'vuelta')
    print("7")
    recolectar_y_desplazarse(3,'vuelta')
    print("8")
recolectar_y_desplazarse(2,'ida')  
print("9")

for i in range(3):
        recolectar_y_desplazarse(1,'ida') 
moverse(centro,'right')
bot.send_message(906440079,"siembra terminada")