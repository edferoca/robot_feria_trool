import pyautogui, sys, time
import pywhatkit

centroX=400
centroY=300

def recolectar():
    time.sleep(0.4)
    manita=pyautogui.locateOnScreen('seleccion.png',confidence=0.9,region=(0,0,794,558))
    time.sleep(0.4)
    if manita is None:
        CapitanMiau()
    else:

        manita_pos=pyautogui.center(manita)
        print("recolectar",manita_pos)
        pyautogui.moveTo(manita_pos)
        pyautogui.click(button='left')
        time.sleep(2.9)
        

def talar():
    time.sleep(0.4)
    pinza=pyautogui.locateOnScreen('talar.png',confidence=0.9,region=(0,0,800,600))
    time.sleep(0.4)
    if pinza is None:
        CapitanMiau()
    else:

        pinza_pos=pyautogui.center(pinza)
        pyautogui.moveTo(pinza_pos)
        pyautogui.click(button='left')
        time.sleep(2.9)
        
        
        
def CapitanMiau():
    time.sleep(5)
    CapitanMiau=pyautogui.locateOnScreen('capitan_miau_2.png',confidence=0.6,region=(400,400,800,600))
    print("capitan Miau?")
    if CapitanMiau is None:
        pass
    else:
        pywhatkit.sendwhatmsg_instantly("+34611131367", "hello", 15, True, 4)
        paso=input("presione 1 si ya paso:")   
               
    

#movimientos
def Derecha():
    pyautogui.click(360,330,button='right')
    recolectar()
    pyautogui.click(360,330,button='right')
    talar()
def Izqierda(): 
    pyautogui.click(445,290,button='right')
    recolectar()
    pyautogui.click(445,290,button='right')
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



for i in range(2):#8
#ida
    
    for j in range(3):
        Derecha()
        Adelante()
        pyautogui.click(centroX-50,centroY+30,button='left')
        time.sleep(0.6)
    Derecha()
    Adelante()
    pyautogui.click(centroX+50,centroY+30,button='left') 
    time.sleep(0.6)
    Derecha()
    Adelante()
    pyautogui.click(centroX+50,centroY+30,button='left') 
    time.sleep(0.6)
    Derecha()
    
    for j in range(3):
        Izqierda()
        Adelante()
        pyautogui.click(centroX+50,centroY-30,button='left')
        time.sleep(0.6)
    Izqierda()
    Adelante()
    pyautogui.click(centroX+50,centroY+30,button='left')
    time.sleep(0.6)
    Izqierda()
    Adelante() 
    pyautogui.click(centroX+50,centroY+30,button='left')
    time.sleep(0.6)
    Izqierda() 
    