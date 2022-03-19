import random
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from easygui import fileopenbox

def ft_imgСomparison(name_files):
    name_files.append("saltPepper.jpg")
    name_files.append("medianFilter.jpg")
    for i in range(3):
        img = cv2.imread(name_files[i], cv2.IMREAD_ANYCOLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.subplot(1, 3 , i + 1),plt.imshow(img)
        plt.title(name_files[i])
        plt.xticks([]),plt.yticks([])        
    plt.show()

def ft_saltPepper(data, s1, p1):
    width, height = len(data[0]), len(data)
    for i in range(height):
        for j in range(width):
            a1 = random.random()<s1
            a2 = random.random()<p1
            if (a1 & a2):
                y = 0
            elif (a1 & ~a2):
                y = 255
            else:
                continue
            data[i][j] = y
    return(data)

def ft_medianFilter(data):
    members = [(0,0)] * 9
    width, height = len(data), len(data[0])
    for i in range(1,width-1):
        for j in range(1,height-1):
            members[0] = tuple(data[i-1,j-1])
            members[1] = tuple(data[i-1,j])
            members[2] = tuple(data[i-1,j+1])
            members[3] = tuple(data[i,j-1])
            members[4] = tuple(data[i,j])
            members[5] = tuple(data[i,j+1])
            members[6] = tuple(data[i+1,j-1])
            members[7] = tuple(data[i+1,j])
            members[8] = tuple(data[i+1,j+1])
            members.sort()
            data[i][j] = members[4]
    return(data)

def main():
    name_files = []
    flt=["*.jpg", "*.png"]
    path = fileopenbox("image",
                       "select file",
                       default = flt[0],
                       filetypes = flt)
    if path:
        try:
            img = Image.open(path)
            name_files.append(path.rpartition('/')[2])
            data = np.array(img)
            data = ft_saltPepper(data, 0.05, 0.1)
            img = Image.fromarray(data)
            img.show()
            img.save("saltPepper.jpg", 'JPEG')
            data = ft_medianFilter(data)
            img = Image.fromarray(data)
            img.show()
            img.save("medianFilter.jpg", 'JPEG')
            ft_imgСomparison(name_files)            
        except IOError:
            print("Are you crazy?!")
main()