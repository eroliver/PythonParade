from PIL import Image, ImageFilter, ImageChops
from os import scandir, getcwd, path
from picture_to_sketch import create_sketch

image_folder = path.abspath(path.join(getcwd(), "images\\"))
edited_folder = path.abspath(path.join(getcwd(), "edited_images\\"))


def create_line_art(file_name: str) -> str:
    pic = Image.open(f"images/{file_name}")
    edit = pic.filter(ImageFilter.FIND_EDGES)
    invert = ImageChops.invert(edit)
    invert.save(f"edited_images/PIL{file_name}")


# method to grab all images from the images folder for testing
def group_process():
    # grab all images from images and run through create_line_art()
    all_images = [entry.name for entry in scandir(image_folder) if entry.is_file()]
    for image in all_images:
        create_line_art(image)
    print(image_folder, "\n", edited_folder, "\n", all_images)

if __name__ == "__main__":
    create_sketch("F:/Projects/PycharmProjects/PythonParade/Parade/ImageProcessing/images/neebs logo.png")