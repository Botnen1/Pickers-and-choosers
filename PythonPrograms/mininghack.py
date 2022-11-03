""" mininghack.py """



#for minning for a long time

from pynput.keyboard import Key, Controller
from tkinter import W
import pyautogui as pg
import time
keyboard = Controller()


def mining(x):
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
#counts down and gives you 5 sec to get ready ingame
   
    counter = x
    while counter != 0:
        pg.mouseDown(button="left")
        pg.keyDown("W")
        print(counter)
        counter -= 1
    
mining(2000)
#insert amount of times you want your "mouse_one" to be clicked