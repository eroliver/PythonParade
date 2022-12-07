from PIL import Image, ImageFilter, ImageChops

pic = Image.open("sketch1.png")
edit = pic.filter(ImageFilter.FIND_EDGES)
invert = ImageChops.invert(edit)
invert.save("edited.jpg")
