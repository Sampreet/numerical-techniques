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
    ops = 0
    mat = np.array(A, dtype=np.float)
    b = np.array(b, dtype=np.float)
    size = len(b)

    # form upper-triangular matrix
    for j in range(0, size):
        divisor = mat[j][j]
        if (divisor != 0):
            mat[j] = np.array(list(map(lambda ele: ele / divisor, mat[j])), dtype=np.float)
            b[j] /= divisor
            ops += size + 1
        for i in range(j+1, size):
            multiplier = mat[i][j]
            for k in range(0, size):
                mat[i][k] -= mat[j][k] * multiplier 
            b[i] -= b[j] * multiplier
            ops += size + 1

    # find root by reverse substitution
    x = np.array(b, dtype=np.float)
    for i in range(1, size):
        for k in range(size - 1 - i, size):
            x[size - 1 - i] -= mat[size - 1 - i][k] * x[k]

    return x.tolist(), ops, None


            
