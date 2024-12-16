import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_plane_and_pointcloud(ax, normal, d, points, xlim, ylim, zlim):
    normal = np.array(normal)
    a, b, c = normal
    x = np.linspace(xlim[0], xlim[1], 20)
    y = np.linspace(ylim[0], ylim[1], 20)
    x, y = np.meshgrid(x, y)
    z = -(a * x + b * y + d) / c
    ax.plot_surface(x, y, z, alpha=0.7, cmap='viridis', edgecolor='none')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='red', s=10)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_zlim(zlim)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

def interactive_plane_update(normal, d, csv_file, xlim=(-100, 100), ylim=(-100, 100), zlim=(-100, 100)):
    data = pd.read_csv(csv_file).to_numpy()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.ion()
    while True:
        ax.clear()
        plot_plane_and_pointcloud(ax, normal, d, data, xlim, ylim, zlim)
        plt.draw()
        plt.pause(0.1)
        normal[0] += 0.1
        d += 0.1
        if normal[0] > 10: break
    plt.ioff()
    plt.show()


csv_file = "Visage_symetrique_decimated.csv"

# Step 1 : Initialisation du plan
normal = [1, 2, 3]
d = -5
interactive_plane_update(normal, d, csv_file)

