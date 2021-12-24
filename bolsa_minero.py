import pyautogui,sys
import time
def min_up():
    pyautogui.moveTo(490,194,2.7)
    pyautogui.click(button='right')
    pyautogui.moveTo(490,166,1)
    pyautogui.click(button='left')
def min_abj():
    pyautogui.moveTo(354,330,2.7)
    pyautogui.click(button='right')
    pyautogui.moveTo(354,305,1)
    pyautogui.click(button='left')

for i in range(10):
    pyautogui.moveTo(401,310)
    min_up()
    #in_abj()
    pyautogui.moveTo(401,310,15)
