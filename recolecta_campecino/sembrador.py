import pyautogui, sys, time
import pywhatkit

centro=[400,300]

direcciones ={
    "adelante":[445,330],
    "atras":[360,290],
    "derecha":[360,330],
    "dercha2" : [310,360]
    "izquierda":[445,290]
}

semilla='amanita.png'
contador_sembrado=0
limite_siembra_por_sembrado=1

def moverse(direccion):
    pyautogui.click(direccion[0],direccion[1],button='left')
    time.sleep(3)

def sembrado(direccion):
    pyautogui.moveTo(direccion[0],direccion[1])
    time.sleep(1)
    confirmacion=pyautogui.locateOnScreen(semilla,confidence=0.7,region=(0,0,800,600))
    time.sleep(0.4)
    if confirmacion is None:
            sembrado=0
    else:

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
        
        print(contador_sembrado)
    

pyautogui.click(centro[0],centro[1],button='right')
pyautogui.press('6')

sembrando(2,'derecha',contador_sembrado)
moverse(direcciones.get('derecha2'))
time.sleep(1)
sembrando(3,'derecha',contador_sembrado)
print("pase por aqui")

for j in range(3):
    moverse(direcciones.get('derecha2'))
    time.sleep(1)
    sembrando(2,'derecha',contador_sembrado)   
   

pyautogui.click(centro[0],centro[1],button='right')
