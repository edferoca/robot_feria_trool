import pyautogui, time

__all__=['recorrido_espanto']

def cabar():
    time.sleep(0.4)
    palita=pyautogui.locateOnScreen('pala.png',confidence=0.8,region=(0,0,794,558))
    if palita is None:
        pass
    else:

        palita_pos=pyautogui.center(palita)
        pyautogui.moveTo(palita_pos)
        pyautogui.click(button='left')
        time.sleep(1.3)

def recorrido_espanto():
    for i in range(80):
        while 1:
            pyautogui.click(x=200,y=200,button='right')
            time.sleep(0.5)
            manita=pyautogui.locateOnScreen('entrada2.png',confidence=0.9,region=(0,0,794,558))
            if manita is None:
                pass
            else:
                break
        manita_pos=pyautogui.center(manita)
        pyautogui.moveTo(manita_pos)
        pyautogui.click(button='left')
        pyautogui.moveTo(401,310,5)
        pyautogui.click(x=422,y=281,button='right')
        time.sleep(0.6)
        cerrojo=pyautogui.locateOnScreen('candado.png',confidence=0.9,region=(0,0,794,558))
        if cerrojo is None:
            pyautogui.click(354,285,button='right')#izq
            time.sleep(0.5)
            manita=pyautogui.locateOnScreen('entrada2.png',confidence=0.9,region=(0,0,794,558))
            if manita is None:
                pass
            else:
                break
        cerojo_pos=pyautogui.center(cerrojo)
        pyautogui.click(cerojo_pos,button='right')
        time.sleep(0.4)
        pyautogui.click(x=660,y=350,button='left')

        pyautogui.moveTo(401,310,2.7)
        for i in range(4):
            pyautogui.click(478,350,button='right')#2 a der
            cabar()
            pyautogui.click(357,328,button='right')#abajo
            cabar()
            pyautogui.click(440,280,button='right')#arriba
            cabar()

        pyautogui.click(440,330,button='left')#desplaza a nuevo punto
        time.sleep(0.5)

        for i in range (5) :
            pyautogui.click(318,350,button='right')#2 a abajo
            cabar()
            pyautogui.click(440,330,button='right')#der
            cabar()
            pyautogui.click(354,285,button='right')#izq
            cabar()
            time.sleep(0.9)
        time.sleep(4)
