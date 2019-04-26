"""
A collection of methods to find solutions of a system of linear equations using Gaussian Elimination Method.
"""

__all__ = ["solve_using_upper_triangle"]

import numpy as np

def solve_using_upper_triangle(A, b):
    """
    Find the roots of a given system of linear equations represented as A*x = b using Upper-Triangular Gaussian Elimination Method.

    Parameters
    ----------
    A : list (list (float))
        Given coefficient matrix.
    b : list (float)
        Given constant vector.

    Returns
    -------
    root, ops, msg : float, int, String
        The root and the operation count with error string.
    """

    # initialize values
    ops = 0                             # number of operations
    mat = np.array(A, dtype=np.float)   # coefficient matrix as numpy array
    b = np.array(b, dtype=np.float)     # constant vector as numpy array
    dim = len(b)                       # number of variables

    # form upper-triangular matrix
    for j in range(0, dim):
        divisor = mat[j][j]
        if (divisor != 0):
            mat[j] = np.array(list(map(lambda ele: ele / divisor, mat[j])), dtype=np.float)
            b[j] /= divisor
            ops += dim + 1
        for i in range(j+1, dim):
            multiplier = mat[i][j]
            for k in range(0, dim):
                mat[i][k] -= mat[j][k] * multiplier 
            b[i] -= b[j] * multiplier
            ops += dim + 1

    # find root by reverse substitution
    x = np.array(b, dtype=np.float)
    for i in range(1, dim):
        for k in range(dim - 1 - i, dim):
            x[dim - 1 - i] -= mat[dim - 1 - i][k] * x[k]

    return x.tolist(), ops, None


            
