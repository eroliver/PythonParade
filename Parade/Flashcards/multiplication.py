from asyncio.windows_events import NULL
from random import randint
from sys import getwindowsversion
import os

def main():
    training = True

    incorrect_img = 'die.jpg'
    correct_img = 'yes.jpg'

    while(training):
        number1 = randint(0, 13)
        number2 = randint(0, 13)
        answer = number1 * number2
        entered = input(" what is " + str(number1) + "x" + str(number2) + "? ")
        if(int(entered) == answer):
            os.system(f'start { correct_img }')
        else:
            os.system(f'start { incorrect_img }')

if __name__ == "__main__":
    main()
