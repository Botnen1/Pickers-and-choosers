import random as rnd 
from time import sleep


def flip(x):
    while x != 0:
        terning = rnd.randint(1, 2)
        print("Flipping... 50/50")
        sleep(0.2)
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)
        if terning == 1:
            print("Heads!\n\n\n")
        else:
            print("Tails!\n\n\n")
        x -= 1

flip(1)