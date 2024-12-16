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
    symm = R = 2* (point - np.dot(point-d, n) * n) - point
    dmin = 100
    pmin = point
    for p in right:
        if np.dot(p-symm, p-symm)<dmin:
            dmin = np.dot(p-symm, p-symm)
            pmin = p
    return(pmin)