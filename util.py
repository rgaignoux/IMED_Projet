import numpy as np

def divide(points, n,d):
    left = []
    right = []

    for point in points:
        if np.dot(n, point-d)<0:
            left.append(point)
        else:
            right.append(point)

    return(left, right)


def closest(point, n, d, right):
    symm = np.dot(np.identity(3) - 2*np.dot(n, n.T), point) + 2* np.dot(d,n)
    dmin = 100
    pmin = point
    for p in right:
        if np.dot(p-symm, p-symm)<dmin:
            dmin = np.dot(p-symm, p-symm)
            pmin = p
    return(pmin)