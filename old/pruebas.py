import pyautogui, sys, time
pyautogui.useImageNotFoundException()
while 1:
    time.sleep(0.4)
    palita=pyautogui.locateOnScreen('entrada2.png',confidence=0.8,region=(0,0,794,558))
    if palita is None:
        print('no encontrado')
    else:

        print(" SI encontrado")