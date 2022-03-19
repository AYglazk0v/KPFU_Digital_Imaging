from PIL import Image
from easygui import fileopenbox, filesavebox

def ft_linearContrast(img):
    width, height = img.size
    pixel = img.load()
    y_min, y_max = 0, 255
    x_min, x_max = 255, 0
    for i in range(height):
        for j in range(width):
            bright = sum(pixel[j, i]) / 3
            if bright < x_min:
                x_min = bright
            if bright > x_max:
                x_max = bright
    for i in range(height):
        for j in range(width):
            bright = sum(pixel[j, i]) / 3
            y_new = ((bright - x_min) / (x_max - x_min)
                        * (y_max - y_min) + y_min)
            img.putpixel((j, i),
                        (int(y_new), int(y_new), int(y_new)))
    return img

def main():
    flt=["*.jpg", "*.png"]
    path = fileopenbox("image",
                       "select file",
                       default = flt[0],
                       filetypes = flt)
    if path:
        try:
            img = Image.open(path)
            new_img = ft_linearContrast(img)
            path = filesavebox(default = "contrast")
            if path == None:
                path = "Yuuuuhuu"
            new_img.save(path + ".jpg", 'JPEG')
        except IOError:
            print("Are you crazy?!")
main()