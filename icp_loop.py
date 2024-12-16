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
    
    
    # INITIALISATION article [10]
    newP = (n0,d0) #initialiser à n'importe quoi
    P = (n,d) #initialiser normalement
    
    # icp loop
    while d != d0 or np.det(n,n0) != 0 : # tant que P bouge
        
        left, right = u.divide(points, n, d) # ensemble de points à gauche (droite) du plan (n,d)

        # pour chaque point à gauche du plan, match le plus proche à sa symétrie à droite du plan
        y = []
        for elem in left : # à gauche du plan par exemple
            coord, i = u.closest(elem[0],elem[1], right)
            y.append(coord)
        y = np.array(y)
        
        # compute nouveau plan de symmetrie
        P = newP
        newP = (new_n, new_d) # compute nouveau n et nouveau d
    
    return (n, d)