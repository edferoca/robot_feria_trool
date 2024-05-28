from .base import*
from .comunication import *
import pyautogui, time

__all__=['recorrido_leñador']

def ruta_simebra_arboles():
    sembrado_seguro("izquierda")
    time.sleep(2) 
    pyautogui.click(direcciones.get("atras"), button='left')
    time.sleep(2)
    for i in range(16):
        sembrado_seguro("derecha")
        sembrado_seguro("izquierda")
        time.sleep(2) 
        pyautogui.click(direcciones.get("atras"), button='left')
        time.sleep(2)
    sembrado_seguro("izquierda")
    time.sleep(2) 
    pyautogui.click(direcciones.get("derecha"), button='left')
    time.sleep(2) 
    pyautogui.click(direcciones.get("derecha"), button='left')
    time.sleep(2) 
    pyautogui.click(direcciones.get("derecha"), button='left')
    time.sleep(2) 
    sembrado_seguro("derecha")
    pyautogui.click(direcciones.get("adelante"), button='left')
    time.sleep(2) 
    for j in range(16):
        sembrado_seguro("derecha")
        sembrado_seguro("izquierda")
        time.sleep(2) 
        pyautogui.click(direcciones.get("adelante"), button='left')
        time.sleep(2)
    sembrado_seguro("izquierda")
    sembrado_seguro("derecha")
    
def ruta_recolecta_arboles(accion):
    for i in range(17):
        ejecutar_accion("derecha",accion[0])
        ejecutar_accion("izquierda",accion[0])
        time.sleep(1) 
        pyautogui.click(direcciones.get("atras"),button='left')
        time.sleep(2) 
    #print("1")
    ejecutar_accion("derecha",accion[0])   
    #sube 2 casillas
    pyautogui.click(direcciones.get('izquierda'),button='left')
    time.sleep(1) 
    pyautogui.click(direcciones.get("adelante"),button='left')
    time.sleep(1) 
    for i in range(17):
        ejecutar_accion("izquierda",accion[0])
        time.sleep(1) 
        pyautogui.click(direcciones.get("adelante"),button='left')
        time.sleep(2) 
        #print(f'vualta{i} de vuelta')
    pyautogui.click(direcciones.get('izquierda'),button='left')
    time.sleep(1) 
    pyautogui.click(direcciones.get('izquierda'),button='left')
    time.sleep(1) 
    for i in range(17):
        ejecutar_accion("izquierda",accion[1])
        ejecutar_accion("izquierda",accion[1])
        time.sleep(1) 
        pyautogui.click(direcciones.get("atras"),button='left')
        time.sleep(2) 
        
def recorrido_leñador(siembra =True,recolecta = True):
    send_telegram_msg("siembra iniciada")
    corta_o_tala=[imagenes.get('talar_recurso'),imagenes.get('tijera_recurso')]
    if siembra==True:
        print('inicia la siembra')
        ruta_simebra_arboles()
        print('esperar a que cresca algo')
        send_telegram_msg("siembra terminada, esperando ... ") 
        time.sleep(600)  
    if recolecta == True:
        send_telegram_msg("recolecta iniciada")
        print('recolecta iniciada')
        ruta_recolecta_arboles(corta_o_tala)
        for i in range(17):
            pyautogui.click(direcciones.get('atras'),button='left')
            time.sleep(1) 
        send_telegram_msg("recolecta terminada")

        