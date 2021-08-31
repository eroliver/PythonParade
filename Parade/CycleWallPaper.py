import ctypes
import random
from time import time, sleep


def cycle_wallpapers(images):
    image_list = [i for i in range(1, images + 1)]
    chosen_bg = random.choice(image_list)
    image_name = f'BG ({chosen_bg})'
    image_folder_path = f'E:\Projects\PycharmProjects\PythonParade\Parade\images\{image_name}.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_folder_path, 0)
    print(image_folder_path)


while True:
    sleep(5 - time() % 5)
    cycle_wallpapers(22)

