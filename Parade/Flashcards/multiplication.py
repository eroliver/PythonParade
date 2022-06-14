from random import randint
from sys import getwindowsversion
from PIL import Image
from win32gui import SetActiveWindow,EnumWindows

training = True

incorrect_img = Image.open("die.jpg")
while(training):
    number1 = randint(0, 13)
    number2 = randint(0, 13)
    answer = number1 * number2
    entered = input(" what is " + str(number1) + "x" + str(number2) + "? ")
    if(int(entered) == answer):
        print("correct")
    else:
        incorrect_img.show()

stuff = EnumWindows

internetCode = """def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "notepad" in i[1].lower():
            print i
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])
            break"""