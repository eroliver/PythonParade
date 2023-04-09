# This should allow for images to be turned into sketches. I want to make these colorable so that users can create
# a coloring page out of any picture they like. This current function is from a youtuber that can be found here:
# https://www.youtube.com/channel/UC8k9jpaeyitFgB0tanVPB9g but I think it could be improved to have more distinct lines
# like found on coloring pages.'''
import cv2
from os import scandir, getcwd, path


image_folder = path.abspath(path.join(getcwd(), "images\\"))
edited_folder = path.abspath(path.join(getcwd(), "edited_images\\"))


def create_sketch(file_name: str) -> str:
    image = cv2.imread(f"{image_folder}/{file_name}")
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_img = cv2.bitwise_not(grey_img)
    blurred_img = cv2.GaussianBlur(inverted_img, (21,21), 0)
    inverted_blurred = cv2.bitwise_not(blurred_img)
    sketch = cv2.divide(grey_img, inverted_blurred, scale= 240.0)
    cv2.imwrite(f"{edited_folder}/{file_name}", sketch)
    print(f"image: {image}, grey_img: {grey_img}, \nfile_name: {file_name}")

# Used to test image on different blur scales, will modify main function to take multiple args, for ever int arg passed,
# it will blur at that scale and return an image for each
def create_multiple_line_art(file_name: str) -> str:
    image = cv2.imread(f"images/{file_name}")
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_img = cv2.bitwise_not(grey_img)
    blurred_img = cv2.GaussianBlur(inverted_img, (21,21), 0)
    inverted_blurred = cv2.bitwise_not(blurred_img)
    sketch = cv2.divide(grey_img, inverted_blurred, scale= 220.0)
    sketch0 = cv2.divide(grey_img, inverted_blurred, scale= 230.0)
    sketch1 = cv2.divide(grey_img, inverted_blurred, scale= 240.0)
    sketch2 = cv2.divide(grey_img, inverted_blurred, scale= 250.0)
    sketch3 = cv2.divide(grey_img, inverted_blurred, scale= 260.0)
    cv2.imwrite(f"edited_images/220{file_name}", sketch)
    cv2.imwrite(f"edited_images/230{file_name}", sketch0)
    cv2.imwrite(f"edited_images/240{file_name}", sketch1)
    cv2.imwrite(f"edited_images/250{file_name}", sketch2)
    cv2.imwrite(f"edited_images/260{file_name}", sketch3)


# method to grab all images from the images folder for testing
def group_process():
    # grab all images from images and run through create_line_art()
    all_images = [entry.name for entry in scandir(image_folder) if entry.is_file()]
    for image in all_images:
        create_line_art(image)
    print(image_folder, "\n", edited_folder, "\n", all_images)


def display_image(image):
    global k
    cv2.imshow("Display window", image)
    k = cv2.waitKey(0)
    if k == ord("s"):
        cv2.imwrite("sketch.png", image)


