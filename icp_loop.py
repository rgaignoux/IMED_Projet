import vtk
import numpy as np
import util as u

def ICP(name):
    """Compute ICP for point clouds in the image 'name'

    Parameters
    ----------
    name : string
        the name of the png file (without '.png')

    Returns
    -------
    
    """
    reader = vtk.vtkUnstructuredGridReader()
    reader.SetFileName("" + name + ".vtk")
    reader.Update()
    data = reader.GetOutput()
    
    
    # INITIALISATION 
    # les plans sont définis par un point d et un vecteur normal n
    newP = (n0,d0) # pour avoir une valeur à comparer dans la première boucle
    P = (n,d) # article [10], ou calculer centre de masse des points + orientation random


    # points =    #trouver comment sortir une liste des points 3D de data
    # icp loop
    while d != d0 or np.det(n,n0) != 0 : # tant que P bouge
        
        left, right = u.divide(points, n, d) # ensemble de points à gauche (droite) du plan (n,d)

        # pour chaque point à gauche du plan, match le plus proche à son symétrique à droite du plan
        y = []
        for elem in left : # à gauche du plan par exemple
            coord, i = u.closest(point, n, d, right)
            y.append(coord)
        y = np.array(y)
        
        # calculer le plan
        xg = np.mean(left)
        yg = np.mean(right)

        # compute nouveau plan de symmetrie
        P = newP
        newP = (new_n, new_d) # compute nouveau n et nouveau d
    
    return (n, d)