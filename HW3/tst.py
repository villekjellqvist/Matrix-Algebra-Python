from sympy import *

def plane_rotation_matrix(n:int, i:int, j:int, theta:float):
    """Constructs a plane rotation matrix that rotates the
    i:th and j:th axis counter-clockwise by theta.

    Arguments:
        n -- rotation dimension
        i -- i:th axis
        j -- j:th axis
        theta -- rotation angle

    Returns:
        U: U(theta, i, j): NDArray
    """
    s,c = symbols('s c', Real=True)
    U = Matrix.eye(n,n)
    U[i,i] = c
    U[j,j] = c
    U[i,j] = -s
    U[j,i] = s
    return U