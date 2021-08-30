import ctypes
import time


def cycle_wallpapers():
    pass


image_folder_path = 'E:\Projects\PycharmProjects\PythonParade\Parade\images'
image_name = '\sample_name'
ctypes.windll.user32.SystemParametersInfoW(20, 0, image_folder_path + image_name, 0)
