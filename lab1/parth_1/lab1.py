import cv2
import matplotlib.pyplot as plt
from easygui import fileopenbox, filesavebox

def ft_imgСomparison(name_file):
    for i in range(4):
        img = cv2.imread(name_file[i], cv2.IMREAD_ANYCOLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.subplot(2, 2 , i + 1),plt.imshow(img)
        plt.title(name_file[i].rpartition('/')[2])
        plt.xticks([]),plt.yticks([])        
    plt.show()
    
def main():
    flt = ["*.jpg", "*.png", "*.gif", "*.bmp"]
    name_file = []
    path = fileopenbox("image",
                       "select file",
                       default = flt[0],
                       filetypes = flt)
    if path:
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        img = cv2.imread(path)
        name_file.append(path)
        cv2.imshow("image", img)
        cv2.waitKey()
        cv2.destroyWindow("image")
        path = filesavebox(default = "copy")
        if path == None:
            path = "img"
        for i in range(0, 101, 50):
            cv2.imwrite(path + "_quality_" + str(i) + ".jpg",
                        img,
                        [int(cv2.IMWRITE_JPEG_QUALITY), i])
            name_file.append(path + "_quality_" + str(i) + ".jpg")
        ft_imgСomparison(name_file)
        
main()