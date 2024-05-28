from .base import*
from .comunication import *
import pyautogui, time

__all__ = ['recorrido_herb_camp']
def ruta_siembra():
    #siembra recorriendo de derecha a izquierda 
    for i in range(16):
        sembrado_seguro("derecha")
        sembrado_seguro("atras")
        sembrado_seguro("izquierda")
        time.sleep(2) 
        pyautogui.click(direcciones.get("atras"),button='left')
        time.sleep(2)
    #sube tres casillas para empesar una nueva hilera 
    for i in range(3):
        sembrado_seguro("derecha")
        sembrado_seguro("atras")
        sembrado_seguro("izquierda")
        time.sleep(2) 
        pyautogui.click(direcciones.get("derecha"),button='left')
        time.sleep(2) 
    for i in range(16):
        sembrado_seguro("derecha")
        sembrado_seguro("adelante")
        sembrado_seguro("izquierda")
        time.sleep(2) 
        pyautogui.click(direcciones.get("adelante"),button='left')
        time.sleep(2)
    for i in range(3):
        pyautogui.click(direcciones.get('izquierda'),button='left')
        time.sleep(1) 


def ruta_recolecta(accion,root):
    for i in range(16):
        ejecutar_accion("derecha",accion[0],root)
        ejecutar_accion("derecha",accion[1],root)
        ejecutar_accion("atras",accion[0],root)
        ejecutar_accion("atras",accion[1],root)
        ejecutar_accion("izquierda",accion[0],root)
        ejecutar_accion("izquierda",accion[1],root)
        time.sleep(2) 
        pyautogui.click(direcciones.get("atras"),button='left')
        time.sleep(2) 
    for i in range(3):
        ejecutar_accion("derecha",accion[0],root)
        ejecutar_accion("derecha",accion[1],root)
        ejecutar_accion("atras",accion[0],root)
        ejecutar_accion("atras",accion[1],root)
        ejecutar_accion("izquierda",accion[0],root)
        ejecutar_accion("izquierda",accion[1],root)
        time.sleep(2) 
        pyautogui.click(direcciones.get("derecha"),button='left')
        time.sleep(2) 
    for i in range(16):
        ejecutar_accion("derecha",accion[0],root)
        ejecutar_accion("derecha",accion[1],root)
        ejecutar_accion("adelante",accion[0],root)
        ejecutar_accion("adelante",accion[1],root)
        ejecutar_accion("izquierda",accion[0],root)
        ejecutar_accion("izquierda",accion[1],root)
        time.sleep(2) 
        pyautogui.click(direcciones.get("adelante"),button='left')
        time.sleep(2)


def recorrido_herb_camp(raiz,tijeraOsegar_selector = True,siembra =True,recolecta =True,  ):
    send_telegram_msg("siembra iniciada")
    #si  tijeraOsegar_selector = True se seleccionan las tijeras
    tijeraOsegar = imagenes.get('tijera_recurso') if tijeraOsegar_selector == True else  imagenes.get('segar_recurso')
    reco_y_tala=[imagenes.get('mano_recojida'),tijeraOsegar]
    if siembra==True:
        print('inicia la siembra')
        ruta_siembra()
        print('esperar a que cresca algo')
        send_telegram_msg("siembra terminada, esperando ... ")
        time.sleep(150) 
    if recolecta == True: 
        send_telegram_msg("recolecta iniciada")
        print('recolecta iniciada')
        ruta_recolecta(reco_y_tala,raiz)
        for i in range(3):
            pyautogui.click(direcciones.get('derecha'),button='left')
            time.sleep(1) 
        send_telegram_msg("recolecta terminada")
