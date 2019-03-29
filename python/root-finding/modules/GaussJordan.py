"""
A collection of methods to find solutions of a system of linear equations using Gauss Jordan Method.
"""

__all__ = ["find_inverse"]

import numpy as np

def find_inverse(A):
    """
    Find the inverse of a given matrix.

    Parameters
    ----------
    A : list (list (float))
        Given matrix.

    Returns
    -------
    Ainv, ops, msg : float, int, String
        The inverse and the operation count with error string.
    """

    # initialize values
    ops = 0
    mat = np.array(A, dtype=np.float)
    size = len(A[0])
    Ainv = np.eye(size, dtype=np.float) 

    # check if determinant is zero
    if (np.linalg.det(mat) == 0):
        return None, ops, "Determinant is zero."

    # form upper-triangular matrix
    for j in range(0, size):
        divisor = mat[j][j]
        if (divisor != 0):
            mat[j] = np.array(list(map(lambda ele: ele / divisor, mat[j])), dtype=np.float)
            Ainv[j] = np.array(list(map(lambda ele: ele / divisor, Ainv[j])), dtype=np.float)
            ops += size + 1
        for i in range(j+1, size):
            multiplier = mat[i][j]
            for k in range(0, size):
                mat[i][k] -= mat[j][k] * multiplier 
                Ainv[i][k] -= Ainv[j][k] * multiplier 
            ops += size + 1

    # form identity matrix
    for i in range(1, size):
        for j in range(size - 1 - i + 1, size):
            multiplier = mat[size - i - 1][j]
            for k in range(0, size):
                mat[size - i - 1][k] -= mat[j][k] * multiplier 
                Ainv[size - i - 1][k] -= Ainv[j][k] * multiplier 
            ops += size + 1

    return Ainv.tolist(), ops, None


            
