import numpy as np

def divide(points, n,d):
    left = []
    right = []

    for point in points:
        if np.dot(n, point) + d < 0:
            left.append(point)
        else:
            right.append(point)

    return np.array(left), np.array(right)


def closest_sym(pt_left, n, d, pts_right):
    pt_symm_right = np.dot(np.identity(3) - 2*np.dot(n, n.T), pt_left) + 2* np.dot(d,n)

    pt_right_min = pts_right[0]
    
    for pt_right in pts_right:
        if np.linalg.norm(pt_symm_right - pt_right) < np.linalg.norm(pt_symm_right - pt_right_min):
            pt_right_min = pt_right

    return (pt_right_min)