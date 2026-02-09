import pyautogui, sys, time
while True:
    
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    print(currentMouseX,currentMouseY)