import pyautogui
import time
from .base import *
from .comunication import *

__all__ = ['recorrido_leñador']

def click_fuerte(posicion, button='left'):
    """Hace clic simulando mouseDown y mouseUp separados, útil en juegos o apps protegidas."""
    pyautogui.moveTo(posicion)
    time.sleep(0.1)
    pyautogui.mouseDown(button=button)
    time.sleep(0.05)
    pyautogui.mouseUp(button=button)
"""
-----<------<-----<----<-----X
|
|
>----->----->----->---->---->fin
"""
def ruta_simebra_arboles():
    sembrado_seguro("izquierda")
    time.sleep(2) 
    click_fuerte(direcciones.get("atras"), button='left')
    time.sleep(2)
    for i in range(16):
        sembrado_seguro("derecha")
        sembrado_seguro("izquierda")
        time.sleep(3) 
        print('hola')
        click_fuerte(direcciones.get("atras"), button='right')
        click_fuerte(direcciones.get("atras"), button='left')
        time.sleep(2)
    sembrado_seguro("izquierda")
    time.sleep(2) 
    click_fuerte(direcciones.get("derecha"), button='left')
    time.sleep(2) 
    click_fuerte(direcciones.get("derecha"), button='left')
    time.sleep(2) 
    click_fuerte(direcciones.get("derecha"), button='left')
    time.sleep(2) 
    sembrado_seguro("derecha")
    click_fuerte(direcciones.get("adelante"), button='left')
    time.sleep(2) 
    for j in range(16):
        sembrado_seguro("derecha")
        sembrado_seguro("izquierda")
        time.sleep(2) 
        click_fuerte(direcciones.get("adelante"), button='left')
        time.sleep(2)
    sembrado_seguro("izquierda")
    sembrado_seguro("derecha")

def ruta_recolecta_arboles(accion, root):
    for i in range(17):
        ejecutar_accion("derecha", accion[0], root)
        ejecutar_accion("izquierda", accion[0], root)
        time.sleep(1) 
        click_fuerte(direcciones.get("atras"), button='left')
        time.sleep(2) 
    ejecutar_accion("derecha", accion[0], root)
    click_fuerte(direcciones.get('izquierda'), button='left')
    time.sleep(1) 
    click_fuerte(direcciones.get("adelante"), button='left')
    time.sleep(1) 
    for i in range(17):
        ejecutar_accion("izquierda", accion[0], root)
        time.sleep(1) 
        click_fuerte(direcciones.get("adelante"), button='left')
        time.sleep(2) 
    click_fuerte(direcciones.get('izquierda'), button='left')
    time.sleep(1) 
    click_fuerte(direcciones.get('izquierda'), button='left')
    time.sleep(1) 
    for i in range(17):
        ejecutar_accion("izquierda", accion[1], root)
        ejecutar_accion("izquierda", accion[1], root)
        time.sleep(1) 
        click_fuerte(direcciones.get("atras"), button='left')
        time.sleep(2) 

def recorrido_leñador(raiz, siembra=True, recolecta=True):
    send_telegram_msg("siembra iniciada")
    corta_o_tala = [imagenes.get('talar_recurso'), imagenes.get('tijera_recurso')]
    
    if siembra:
        print('inicia la siembra')
        ruta_simebra_arboles()
        print('esperar a que crezca algo')
        send_telegram_msg("siembra terminada, esperando ... ") 
        time.sleep(600)  # espera de 10 minutos
    
    if recolecta:
        send_telegram_msg("recolecta iniciada")
        print('recolecta iniciada')
        ruta_recolecta_arboles(corta_o_tala, raiz)
        for i in range(17):
            click_fuerte(direcciones.get('adelante'), button='left')
            time.sleep(1) 
        send_telegram_msg("recolecta terminada")
