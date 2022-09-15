import variables as v
import pyautogui, sys, time
import telebot

def recolectar_y_desplazarse(tipo,IdaVuelta):
    if IdaVuelta == 'ida':
        sentido='derecha'
        setnidoContrario='izquierda'
    elif IdaVuelta == 'vuelta':
        sentido='izquierda'
        setnidoContrario='derecha'
    if tipo == 1:
        v.recolectar(v.direcciones.get('adelante'))
        v.recolectar(v.direcciones.get(sentido))
        v.moverse(v.direcciones.get(sentido),'left')
    if tipo == 2:
        v.recolectar(v.direcciones.get(setnidoContrario))
        v.recolectar(v.direcciones.get('adelante'))
        v.recolectar(v.direcciones.get(sentido))
        v.moverse(v.direcciones.get(sentido),'left')
    if tipo == 3:
        v.recolectar(v.direcciones.get('adelante'))
        v.recolectar(v.direcciones.get(sentido))
        v.moverse(v.direcciones.get('adelante'),'left')


v.bot.send_message(906440079,"recolecta iniciada")
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
v.moverse(v.centro,'right')
v.bot.send_message(906440079,"siembra terminada")