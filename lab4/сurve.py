import turtle
import numpy as np
from PIL import Image
import cv2
import os

def get_threshold(Z: np.ndarray):
    return Z.mean()

def boxcount(Z: np.ndarray, k: int):
    S = np.add.reduceat(
        np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
        np.arange(0, Z.shape[1], k), axis=1)
    return len(np.where((S > 0) & (S < k * k))[0])

def ft_fractalDimension(Z: np.ndarray):
    assert (len(Z.shape) == 2)
    Z = (Z < get_threshold(Z))
    p = min(Z.shape)
    n = 2 ** (np.log(p) / np.log(2))
    n = int(np.log(n) / np.log(2))
    sizes = 2 ** np.arange(n, 1, -1)
    counts = []
    for size in sizes:
        counts.append(boxcount(Z, size))
    coeffs = np.polyfit(np.log(sizes), np.log(counts), 1)
    return -coeffs[0]

def ft_kochTurns(n):
    route = []
    for i in range(n):
        for j in range(4**i):
            route.insert(j*4, 60)
            route.insert(j*4, -120)
            route.insert(j*4, 60)
    return route

def ft_turtleKoch(n, line_lenght=10, width=450,
                height=450, fileName = "turtle_img"):
    wn = turtle.Screen()
    wn.setup(width, height)
    turtle.setx(-200)
    turtle.clear()
    turtle.pensize(2)
    turtle.speed(0)
    for move in ft_kochTurns(n):
        turtle.forward(line_lenght)
        turtle.left(move)
    turtle.forward(line_lenght)
    turtle.hideturtle()
    canvas = wn.getcanvas()
    canvas.postscript(file= fileName+'.eps', width=width, height=height)
    img = Image.open(fileName + '.eps')
    img.save(fileName + '.png')
    wn.exitonclick()
    os.remove(fileName+'.eps')

def main():
    n = int(input("n = "))
    ft_turtleKoch(n)
    image = cv2.imread('turtle_img.png', 0)
    fd = np.around(ft_fractalDimension(image), decimals=4)
    print(f"Фрактальная размерность: {fd}")

main()
