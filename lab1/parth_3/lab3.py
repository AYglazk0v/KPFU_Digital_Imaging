import os
import random
import imageio
import numpy as np
import matplotlib.pyplot as plt

def ft_createAnimation(a, b):
    filenames = []
    s_axis=max(a,b)*1.2
    polygon = ft_createPolygon(np.pi, a, b);
    for i in range(0, 360, 10):
        x = []
        y = []
        angle = np.radians(i)
        M = np.float32([ [np.cos(angle), -(np.sin(angle)), 0],
                       [np.sin(angle), np.cos(angle), 0],
                       [0, 0, 1] ])
        ret = polygon.dot(M)
        for j in range(np.size(polygon, 0)):
            x.append(ret[j][0])
            y.append(ret[j][1])
        plt.plot(x,y);
        plt.axis([-s_axis, s_axis, -s_axis, s_axis]);
        filenames.append("tmp_fig" + str(i) + ".png")
        plt.savefig("tmp_fig" + str(i) + ".png")
        plt.close()
        x.clear()
        y.clear()
    with imageio.get_writer('rotate.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
    for filename in set(filenames):
        os.remove(filename)
        
def ft_createPolygon(B, a, b):
    n = 0
    phi = []
    phi.append(0)
    while (phi[n] <= np.pi * 2):
        dphi = B * random.random()
        phi.append(phi[n] + dphi)
        n+=1
    mat_1 = np.zeros((1, n))
    for i in range(0, n):
        mat_1[0][i] = a + (b - a) * random.random();
    mat_2 = np.ones((n + 1, 3))
    for i in range(n):
        mat_2[i][0] = mat_1[0][i] * np.cos(phi[i])
        mat_2[i][1] = mat_1[0][i] * np.sin(phi[i])
    mat_2[n] = mat_2[0]
    return (mat_2)

def ft_drawDiogram(a,b):
    vals = []
    pol_1 = ft_createPolygon(np.pi, a, b)
    vals.append(np.size(pol_1, 0) - 1)
    pol_2= ft_createPolygon(np.pi + np.pi / 3, a, b)
    vals.append(np.size(pol_2, 0) - 1)
    pol_3= ft_createPolygon(np.pi + 2 * np.pi / 3, a, b)
    vals.append(np.size(pol_3, 0) - 1)
    pol_4= ft_createPolygon(2 * np.pi, a, b)
    vals.append(np.size(pol_4, 0) - 1)
    labels = ["90", "120", "150", "180"]
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels)
    plt.draw()
    plt.waitforbuttonpress()
    plt.close(fig)

def main():
    a = int(input("a="))
    b = int(input("b="))
    ft_drawDiogram(a, b)
    ft_createAnimation(a, b)


main()