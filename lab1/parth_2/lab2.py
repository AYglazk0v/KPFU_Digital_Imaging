import cv2
import imageio
import matplotlib.pyplot as plt
from imutils import rotate_bound as rb
from easygui import fileopenbox, filesavebox

def ft_size(img):
    (h, w) = img.shape[:2]
    print(h, "x", w)

def ft_crop(img):
    (y, x) = img.shape[:2]
    (y0, x0) = (y, x)
    (y, x) = (y // 2, x // 2)
    res = []
    title = ["X0.25", "X4"]
    crop = img[y: 2 * y, x: 2 * x]
    for i in range(8, 0 , -7):
        res.append(cv2.resize(crop,
                              dsize = (x0 // i, y0 // i),
                              interpolation = cv2.INTER_LINEAR))
    for i in range (2):
        plt.subplot(1, 2, i + 1),plt.imshow(res[i])
        plt.title(title[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

def ft_animation(img):
    frames = []
    for i in range(45, 360+45, 15):
        frames.append(rb(img, i))
    path = filesavebox(default = "rotate.gif")
    if path == None:
        path = "Yuuuuhuu.gif"
    with imageio.get_writer(path, mode = "I") as writer:
        for frame in frames:
            writer.append_data(frame)

def main():
    flt=["*.jpg", "*.png"]
    path = fileopenbox("image",
                       "select file",
                       default = flt[0],
                       filetypes = flt)
    if path:
        img = cv2.imread(path, cv2.IMREAD_ANYCOLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        ft_size(img)
        ft_crop(img)
        ft_animation(img)

main()