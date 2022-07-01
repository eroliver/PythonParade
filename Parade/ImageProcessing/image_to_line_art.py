from PIL import Image, ImageFilter, ImageChops

pic = Image.open("yes.jpg")
edit = pic.filter(ImageFilter.FIND_EDGES)
invert = ImageChops.invert(edit)
invert.save("edited.jpg")
