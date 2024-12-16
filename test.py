import vtk
import numpy as np
from matplotlib import image

def ICP(name, nb):
    """Compute ICP for point clouds in the image 'name'

    Parameters
    ----------
    name : string
        the name of the png file (without '.png')
    nb : int
        number of iterations of ICP

    Returns
    -------
    
    """
    reader = vtk.vtkUnstructuredGridReader()
    reader.SetFileName("" + name + ".vtk")
    reader.Update()
    data = reader.GetOutput()
    
    x_source = x
    # INITIALISATION article [10]

    
    
    # icp loop
    for i in range(nb): # à modifier
        # for each point in the source point cloud match the closest point to its symmetry in the reference point cloud
        y = []
        for elem in x :
            coord, i = u.closest(elem[0],elem[1],reference)
            y.append(coord)
        y = np.array(y)
        
        # compute transform with least squares
        centroidSource = np.mean(x, axis=0)
        centroidRef = np.mean(reference, axis=0)
        cov = np.dot(np.transpose(x-centroidSource), y-centroidRef)
        svd = np.linalg.svd(cov)
        Vt = svd[2]
        
        rotation = np.dot(svd[0], np.transpose(Vt))
            
        t = np.transpose(centroidRef) - np.dot(rotation, np.transpose(centroidSource))
        
        # compute new position with transform
        x = np.dot(x, rotation) + t
        
        # homogeneous coordinates
        T = np.identity(3)
        T[:2, :2] = rotation
        #
        T[:2, 2] = t
        
        # final transform
        Tf = np.dot(Tf, T)
    
    return (x_source, reference, x, Tf)