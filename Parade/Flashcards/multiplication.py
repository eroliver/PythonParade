from asyncio.windows_events import NULL
from random import randint
from sys import getwindowsversion
from PIL import Image
import win32gui
import cv2

training = True

incorrect_img = Image.open("die.jpg")
cvImage = cv2.imread("F:\Projects\PycharmProjects\PythonParade\Parade\Flashcards\die.jpg")

while(training):
    number1 = randint(0, 13)
    number2 = randint(0, 13)
    answer = number1 * number2
    entered = input(" what is " + str(number1) + "x" + str(number2) + "? ")
    if(int(entered) == answer):
        print("correct")
    else:
        cv2.imshow("Display window", cvImage)

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


    