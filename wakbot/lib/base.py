"""
Este archivo se llama base ya que contiene
variables y funciones que son usadas para todos
los siguietnes archivos
-> herbolario_campecino.py
->leñador.py
->pocima_espanto.py
"""
import pyautogui, time
import time
from .capitan_miau import CapitanMiau

__all__=['sembrado_seguro','ejecutar_accion','direcciones','imagenes']


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
imagenes={
    'mano_recojida':  "..\img\seleccion.png",
    'tijera_recurso': "..\img\calar.png",
    'segar_recurso': "..\img/segar.png",
    'talar_recurso': "..\img\calar2.png",
    'siembraSegura' : "..\img\siembra_segura.png",
    'capitanMiau_img': "..\img\capitan_miau_3.png"
}


####################
# Funciones usadas en oficos
# herb-camp-leñador
####################

"""
Esta funcionse asegura de sembrar semillas
en una celda especifica (direccion)
"""
def sembrado_seguro(direccion):
    sembrado = False
    while not sembrado:
        for offset_x in range(-3, 4):  # Cambiado de -3, 3 a -3, 4
            for offset_y in range(-1, 2):  # Cambiado de -1, 1 a -1, 2
                pyautogui.click(direcciones.get(direccion)[0] + offset_x, 
                                direcciones.get(direccion)[1] + offset_y, 
                                button='right')
                time.sleep(1)  # Aumentado el tiempo de espera
                pyautogui.click(direcciones.get(direccion)[0] + offset_x, 
                                direcciones.get(direccion)[1] + offset_y, 
                                button='right')
                time.sleep(1.5)  # Aumentado el tiempo de espera
                confirmacion = pyautogui.locateOnScreen(imagenes.get("siembraSegura"), confidence=0.7, region=(0, 0, 800, 600))
                time.sleep(0.8)  # Aumentado el tiempo de espera
                if confirmacion is None:
                    pyautogui.press('3')
                    time.sleep(1.2)  # Aumentado el tiempo de espera
                    pyautogui.click(direcciones.get(direccion), button='left')
                    time.sleep(3.5)  # Aumentado el tiempo de espera
                else:
                    sembrado = True
                    break
            if sembrado:
                break

"""
Esta funcionse asegura de recolectar 
las diferetnes cosas despues de que el
recurso crecio
depende de la imagen (accion)
y de la celda requerida (direccion)
"""
def ejecutar_accion(direccion, accion):
        
    # Realizar clicks en los pixeles circundantes para activar la acción
    for offset_y in range(-3, 3):
        for offset_x in range(-1, 1):
            
            pyautogui.click(direcciones.get(direccion)[0] + offset_x, 
                            direcciones.get(direccion)[1] + offset_y, 
                            button='right')
           # print(f'hola{direcciones.get(direccion)[0] + offset_x},{direcciones.get(direccion)[1] + offset_y}')
            time.sleep(1)
            # buscar la accion a realizar
            confirmacion = pyautogui.locateOnScreen(accion, confidence=0.8, region=(0, 0, 520, 370)) #800, 600 
            time.sleep(0.8)
            # si la accion esta disponible la ejecutara, si no, pues pasa
            if confirmacion is None:
                
                pass
            else:
                confirmacion_pos = pyautogui.center(confirmacion)
                # mueve el mouse al lugar de la accion y le ejecuta
                pyautogui.moveTo(confirmacion_pos)
                pyautogui.click(button='left')
                # tiempo de espera para recolectar
                time.sleep(5)
                # reviso si aparece el capitan miau
                CapitanMiau(imagenes.get("capitanMiau_img"),direcciones.get('centro'))
                break
        else:
            continue
        break


