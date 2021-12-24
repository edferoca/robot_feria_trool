import pyautogui, sys, time
def mina():
    time.sleep(0.4)
    mina=pyautogui.locateOnScreen('mina.png',confidence=0.7,region=(0,0,794,558))
    if mina is None:
        pass
    else:

        mina_pos=pyautogui.center(mina)
        pyautogui.moveTo(mina_pos)
        pyautogui.click(button='right')
        

def picar():
    time.sleep(0.4)
    pico=pyautogui.locateOnScreen('pico.png',confidence=0.8,region=(0,0,794,558))
    if pico is None:
        pass
    else:

        pico_pos=pyautogui.center(pico)
        pyautogui.moveTo(pico_pos)
        pyautogui.click(button='left')
        

    
for i in range(500):
    
    mina()
    picar()
    time.sleep(5)
    
