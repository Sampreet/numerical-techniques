#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-04-07
# Updated: 2020-01-30

"""Module to obtain solutions of a system of linear equations using Gauss-Jordan Elimination Method."""

# dependencies
import numpy as np

def get_solution_basic(A, b, debug):
    """
    Obtain the solution for a given system of linear equations represented as A*x = b using Gauss-Jordan Elimination Method.

    Parameters
    ----------
    A : list
        Given coefficient matrix.
    b : list
        Given constant vector.
    debug : boolean
        Option to display steps.

    Returns
    -------
    sol, ops, msg : float, int, String
        The solution and the operation count with status string.
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
    for j in range(dim):
        # pivot element
        divisor = A[j][j]
        if divisor == 0:
            # display
            if debug: 
                print("Pivot element is zero")

            return None, ops, "Pivot element is zero"

        A[j] = [ele/divisor for ele in A[j]]
        b[j] /= divisor

        # update operations 
        ops += dim + 1

        # elimination step
        for i in range(j+1, dim):
            multiplier = A[i][j]
            for k in range(dim):
                A[i][k] -= A[j][k] * multiplier 
            b[i] -= b[j] * multiplier 
                
            # update operations 
            ops += dim

        # display
        if debug:
            print("\nElimination step #{j}\n-------------------".format(j=j))
            print("Matrix A:\t{A}".format(A=A))
            print("Vector b:\t{b}".format(b=b))
            
        # reduction step
        for i in range(j):
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

def get_inverse(A, debug):
    """
    Obatin the inverse of a given matrix.

    Parameters
    ----------
    A : list
        Given matrix.
    debug : boolean
        Option to display steps.

    Returns
    -------
    Ainv, ops, msg : float, int, String
        The inverse and the operation count with status string.
    """

    # initialize values
    ops = 0
    size = len(A[0])
    Ainv = [[1 if i==j else 0 for i in range(size)] for j in range(size)]

    # check if determinant is zero
    if (np.linalg.det(A) == 0):
        return None, ops, "Determinant is zero."

    # form upper-triangular matrix
    for j in range(size):
        # get divisor
        divisor = A[j][j]
        if (divisor != 0):
            A[j] = [ele / divisor for ele in A[j]]
            Ainv[j] = [ele / divisor for ele in Ainv[j]]

            # update operations 
            ops += size + 1

        # elimination step
        for i in range(j+1, size):
            multiplier = A[i][j]
            for k in range(size):
                A[i][k] -= A[j][k] * multiplier 
                Ainv[i][k] -= Ainv[j][k] * multiplier 
                
            # update operations 
            ops += size + 1

        # display
        if debug:
            print("\nElimination step #{j}\n-------------------".format(j=j))
            print("Matrix A:\t{A}".format(A=A))
            print("Matrix A_inv:\t{A_inv}".format(A_inv=Ainv))

    # form identity matrix
    for i in range(size):
        for j in range(size - 1 - i + 1, size):
            multiplier = A[size - i - 1][j]
            for k in range(size):
                A[size - i - 1][k] -= A[j][k] * multiplier 
                Ainv[size - i - 1][k] -= Ainv[j][k] * multiplier 
                
            # update operations 
            ops += size + 1

        # display
        if debug:
            print("\nReduction step #{i}\n-------------------".format(i=i))
            print("Matrix A:\t{A}".format(A=A))
            print("Matrix A_inv:\t{A_inv}".format(A_inv=Ainv))

    return Ainv, ops, "Inverse obtained"


            
