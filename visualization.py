import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import util

def plot_plane(ax, normal, d, xlim, ylim):
    normal = np.array(normal)
    a, b, c = normal

    x = np.linspace(xlim[0], xlim[1], 20)
    y = np.linspace(ylim[0], ylim[1], 20)
    x, y = np.meshgrid(x, y)
    
    z = -(a * x + b * y + d) / c

    return ax.plot_surface(x, y, z, alpha=0.7, cmap='viridis', edgecolor='none')

def interactive_plane_update(n, d, points, xyz_min, xyz_max):   
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xlim = (xyz_min[0], xyz_max[0])
    ylim = (xyz_min[1], xyz_max[1])
    zlim = (xyz_min[2], xyz_max[2])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    plt.ion()
    plane = None

    nb_iterations = 0

    try:
        while plt.fignum_exists(fig.number):
            ax.clear()
            ax.set_xlim(xlim)
            ax.set_ylim(ylim)
            ax.set_zlim(zlim)

            left, right = util.divide(points, n, d)
            ax.scatter(left[:, 0], left[:, 1], left[:, 2], c='red', s=1)
            ax.scatter(right[:, 0], right[:, 1], right[:, 2], c='green', s=1)

            plane = plot_plane(ax, n, d, xlim, ylim)
            plt.draw()
            plt.pause(0.5)
            n[0] += 1
            
            nb_iterations += 1

    except KeyboardInterrupt:
        pass

    finally:
        plt.ioff()
        plt.close(fig)

csv_file = "Visage_symetrique_decimated.csv"
points = pd.read_csv(csv_file).to_numpy()

xyz_min = np.min(points, axis=0)
xyz_max = np.max(points, axis=0)

# Step 0
normal = [5, 2, 3]
d = np.linalg.norm(points.mean(axis=0))
print(d)

interactive_plane_update(normal, d, points, xyz_min, xyz_max)
