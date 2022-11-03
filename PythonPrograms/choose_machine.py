import random as rnd
from time import *

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


choose("Counter Strike", "Rocket Leauge", "Leauge of Legends")