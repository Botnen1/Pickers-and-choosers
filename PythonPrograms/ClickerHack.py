""" CLICKERHACK.py """



import pyautogui as pg
import time

def clicker(x):
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
        pg.click()
        """ pg.mouseDown(button="left") """
        print(counter)
        counter -= 1
              
clicker(10000)
#insert amount of times you want your "mouse_one" to be clicked


def spam(x):
    

    counter = x
    while counter != 0:
        time.sleep(2)
        pg.click()
        time.sleep(1)
        pg.write("-rep")
        time.sleep(1)
        pg.write(" you piece ")
        time.sleep(1)
        pg.write("of human")
        time.sleep(1)
        pg.write(" garbage!")
        time.sleep(1)
        pg.click()
        """ pg.mouseDown(button="left") """
        print(counter)
        counter -= 1


""" spam(10) """
    