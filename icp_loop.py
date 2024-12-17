import vtk
import numpy as np
import util as u
import pandas as pd

def ICP(name):
    """Compute ICP for point clouds in the image 'name'

    Parameters
    ----------
    name : string
        the name of the png file (without '.png')

    Returns
    -------
    
    """
    points = pd.read_csv(name).to_numpy()

    
    # INITIALISATION 
    # les plans sont définis par un point d et un vecteur normal n
    n0 = np.array([1,1,1])
    d0 = 0
    newP = (n0,d0) # pour avoir une valeur à comparer dans la première boucle
    n = np.array([0,0,1])
    d = np.linalg.norm(points.mean(axis=0))
    P = (n,d) # article [10], ou calculer centre de masse des points + orientation random


    # points =    #trouver comment sortir une liste des points 3D de data
    # icp loop
    while d != d0 or np.dot(n,n0) != 0 : # tant que P bouge
        
        print("début")

        left, right = u.divide(points, n, d) # ensemble de points à gauche (droite) du plan (n,d)

        print("fin divide")

        # pour chaque point à gauche du plan, match le plus proche à son symétrique à droite du plan
        y = []
        for point in left : # à gauche du plan par exemple
            pt = u.closest_sym(point, n, d, right)
            y.append(pt)
        y = np.array(y)
        
        print("fin boucle paires")

        # calculer le plan
        xg = np.mean(left)
        yg = np.mean(right)
        A = np.zeros((3,3))
        for i in range (len(left)) :
            A = A + (left[i] - xg + y[i] - yg) * (left[i] - xg + y[i] - yg).T - (left[i] - y[i])(left[i] - y[i]).T

        print("fin boucle A")

        eig = np.linalg.eig(A)
        val_min = eig.eigenvalues[0]
        for i in range(1,3):
            if eig.eigenvalues[i] < val_min:
                val_min = eig.eigenvalues[i]
                new_n = eig.eigenvectors[i]
        
        new_d = 1/2 * (xg +yg).T * n

        # compute nouveau plan de symmetrie
        P = newP
        newP = (new_n, new_d) # compute nouveau n et nouveau d

        print("n : ", new_n)
        print("d : ", d)
    
    return (n, d)