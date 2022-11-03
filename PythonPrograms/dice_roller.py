from random import randint

def dice(dice):
    terning = randint(1, int(dice))
    print(str(terning))

dice(6)