"""
Python program for splitting a set of people into two random teams
"""

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
    
    
"""Enter all names as str seperated by comma"""

teams("Navn", "Navn")
