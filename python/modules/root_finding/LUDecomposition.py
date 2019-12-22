#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-04-07
# Updated: 2019-12-22

"""Module to find solutions of a system of linear equations using LU Decomposition Method."""

# dependencies
import numpy as np

def get_LU_with_ones_in_L(a):
    """
    Find the Lower-Triangular and Upper-Triangular matrices of a given matrix.

    Parameters
    ----------
    a : numpy.array
        Given coefficient matrix.

    Returns
    -------
    l, u, ops : numpy.array, numpy.array, int
        The lower-triangular and upper-triangular matrices along with the operation count.
    """

    # initialize values
    ops = 0                             # number of operations
    dim = len(a)                        # number of variables
    l = np.eye(dim)                     # lower-triangular matrix
    u = np.eye(dim)                     # upper-triangular matrix

    for i in range(0, dim):
        # find the elements in each column i of U
        for j in range(0, i + 1):
            prod_sum = 0
            for k in range (0, j):
                prod_sum += l[j][k] * u[k][i]
                ops += 1
            u[j][i] = a[j][i] - prod_sum
            ops += 1

        # find the elements in each column i of L
        for j in range(i + 1, dim):
            prod_sum = 0
            for k in range (0, i):
                prod_sum += l[j][k] * u[k][i]
                ops += 1
            l[j][i] = (a[j][i] - prod_sum) / u[i][i]
            ops += 1

    return l, u, ops

def get_root_of_L(l, b):
    """
    Find the root of the Lower-Triangular matrix.

    Parameters
    ----------
    l : numpy.array
        Lower-triangular matrix

    Returns
    -------
    y, ops : numpy.array, int
        The root with the operation count.
    """

    # initialize values
    ops = 0                             # number of operations
    dim = len(b)                        # number of variables
    y = np.zeros(dim, dtype=np.float)   # the root array

    for i in range(0, dim):
        # multiply matrix rows and substitute elements of y
        prod_sum = 0
        for j in range(0, i):
            prod_sum += l[i][j] * y[j]
            ops += 1
        y[i] = (b[i] - prod_sum) / l[i][i]
        ops += 1

    return y, ops
    
def get_root_of_U(u, y):
    """
    Find the root of the Upper-Triangular matrix.

    Parameters
    ----------
    u : numpy.array
        Upper-triangular matrix

    Returns
    -------
    x, ops : numpy.array, int
        The root with the operation count.
    """

    # initialize values
    ops = 0                             # number of operations
    dim = len(y)                        # number of variables
    x = np.zeros(dim, dtype=np.float)   # the root array

    for i in range(0, dim):
        # multiply matrix rows and back-substitute elements of x
        prod_sum = 0
        for j in range(0, i):
            prod_sum += u[dim - 1 - i][dim - 1 - j] * x[dim - 1 - j]
            ops += 1
        x[dim - 1 - i] = (y[dim - 1 - i] - prod_sum) / u[dim - 1 - i][dim - 1 - i]
        ops += 1

    return x, ops

def find_root_with_ones_in_L(A, b):
    """
    Find the roots of a given system of linear equations represented as A*x = b using LU Decomposition Method with 1s in L.

    Parameters
    ----------
    A : list (list (float))
        Given coefficient matrix.
    b : list (float)
        Given constant vector.

    Returns
    -------
    root, ops, msg : list (float), int, String
        The root and the operation count with error string.
    """

    # initialize values
    t_ops = 0                           # total number of operations
    a = np.array(A, dtype=np.float)     # coefficient matrix as numpy array
    b = np.array(b, dtype=np.float)     # coefficient matrix as numpy array

    l, u, ops = get_LU_with_ones_in_L(a)
    t_ops += ops
    y, ops = get_root_of_L(l, b)
    t_ops += ops
    x, ops = get_root_of_U(u, y)
    t_ops += ops

    return x.tolist(), t_ops, None