# This should allow for images to be turned into sketches. I want to make these colorable so that users can create
# a coloring page out of any picture they like. This current function is from a youtuber that can be found here:
# https://www.youtube.com/channel/UC8k9jpaeyitFgB0tanVPB9g but I think it could be improved to have more distinct lines
# like found on coloring pages.'''
import cv2

image = cv2.imread("imageName.jpg")
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_img = cv2.bitwise_not(grey_img)
blurred_img = cv2.GaussianBlur(inverted_img, (21,21), 0)
inverted_blurred = cv2.bitwise_not(blurred_img)
#sketch0 = cv2.divide(grey_img, inverted_blurred, scale= 230.0)
sketch = cv2.divide(grey_img, inverted_blurred, scale= 240.0)
#sketch2 = cv2.divide(grey_img, inverted_blurred, scale= 250.0)
#cv2.imwrite("sketch.png", sketch0)
cv2.imwrite("sketch1.png", sketch)
#cv2.imwrite("sketch2.png", sketch2)

def display_image(image):
    global k
    cv2.imshow("Display window", image)
    k = cv2.waitKey(0)
    if k == ord("s"):
        cv2.imwrite("starry_night.png", image)