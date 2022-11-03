import random as rnd
from time import *

def teams(*names):
    navn = []
    for e in names:
        navn.append(str(e))
    rnd.shuffle(navn)
    length = len(navn)
    midten = length//2
    lag1 = []
    lag2 = []
    lag1.append(navn[:midten])
    lag2.append(navn[midten:])
    print("Dette blir spennede...")
    sleep(3)
    print("LAG 1 -->   " + str(lag1))
    print("LAG 2 --> " + str(lag2))
    
    

""" teams("Navn", "Navn") """



def flip(x):
    if x == 1:
        terning = rnd.randint(1, 2)
        print("Flipping... 50/50")
        sleep(0.2)
        print("5")
        sleep(1)
        print("4")
        sleep(1)
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)
        if terning == 1:
            print("Heads!")
        else:
            print("Tails!")

""" flip(1) """



def choose(*choices):
    liste = []
    for e in choices:
        liste.append(str(e))

    rnd.shuffle(liste)
    
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    print("Vi skal spille . . . "+" "+str(liste[0]))


""" choose("Counter Strike", "Rocket Leauge", "Leauge of Legends") """



def dice(dice):
    terning = rnd.randint(1, int(dice))
    print(str(terning))

""" dice(6) """