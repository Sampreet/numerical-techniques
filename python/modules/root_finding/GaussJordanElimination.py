#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-04-07
# Updated: 2020-01-15

"""Module to find solutions of a system of linear equations using Gauss-Jordan Elimination Method."""

# dependencies
import numpy as np

def find_root_basic(A, b, debug):
    """
    Find the root of a given system of linear equations represented as A*x = b using Gauss-Jordan Elimination Method.

    Parameters
    ----------
    A : list (list (float))
        Given coefficient matrix.
    b : list (float)
        Given constant vector.
    debug : boolean
        Option to display steps.

    Returns
    -------
    root, ops, msg : float, int, String
        The root and the operation count with error string.
    """

    # initialize values
    ops = 0                             # number of operations
    dim = len(b)                        # number of variables

    # display
    if debug:
        print("Input\n-------")
        print("Matrix A:\t{A}".format(A=A))
        print("Vector b:\t{B}".format(B=b))

    # check if matrix is singular
    if (np.linalg.det(A) == 0):
        # display
        if debug: 
            print("Determinant is zero")

        return None, ops, "Determinant is zero"

    # form upper-triangular matrix
    for j in range(0, dim):
        # pivot element
        divisor = A[j][j]
        if divisor == 0:
            # display
            if debug: 
                print("Pivot element is zero")

            return None, ops, "Pivot element is zero"

        A[j] = [ele/divisor for ele in A[j]]
        b[j] /= divisor
        ops += dim + 1
        # elimination step
        for i in range(j+1, dim):
            multiplier = A[i][j]
            for k in range(0, dim):
                A[i][k] -= A[j][k] * multiplier 
            b[i] -= b[j] * multiplier 
                
            # update operations 
            ops += dim

        # display
        if debug:
            print("\nElimination step #{j}\n-------------------".format(j=j))
            print("Matrix A:\t{A}".format(A=A))
            print("Vector b:\t{b}".format(b=b))

        for i in range(0, j):
            multiplier = A[i][j]
            for k in range(j, dim):
                A[i][k] -= A[j][k] * multiplier 
            b[i] -= b[j] * multiplier 
                
            # update operations 
            ops += dim - j

        # display
        if debug:
            print("\nReduction step #{j}\n-------------------".format(j=j))
            print("Matrix A:\t{A}".format(A=A))
            print("Vector b:\t{b}".format(b=b))

    # display
    if debug:
        print("\nCompleted\n---------\n")

    return b, ops, "Solution obtained"

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

    return Ainv.tolist(), ops, "Inverse found"


            
