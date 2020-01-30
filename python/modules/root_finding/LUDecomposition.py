#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-04-07
# Updated: 2020-01-30

"""Module to obtain solutions of a system of linear equations using LU Decomposition Method."""

# dependencies
import math

def get_solution_L(L, b, debug):
    """
    Obtain the solution for the Lower-Triangular matrix.

    Parameters
    ----------
    L : list
        Lower-triangular matrix
    debug : boolean
        Option to display steps.

    Returns
    -------
    y, ops : list, int
        The solution with the operation count.
    """

    # initialize values
    ops = 0                             # number of operations
    dim = len(b)                        # number of variables
    y = [0 for i in range(dim)]         # the solution array

    for i in range(dim):
        # multiply matrix rows and substitute elements of y
        prod_sum = 0
        for j in range(i):
            prod_sum += L[i][j] * y[j]
                
            # update operations
            ops += 1
        y[i] = (b[i] - prod_sum) / L[i][i]
                
        # update operations
        ops += 1

    # display
    if debug:
        print("\nSolution of L\n-------------------")
        print("Vector y:\t{y}".format(y=y))

    return y, ops
    
def get_solution_U(U, y, debug):
    """
    Obtain the solution for the Upper-Triangular matrix.

    Parameters
    ----------
    U : list
        Upper-triangular matrix
    debug : boolean
        Option to display steps.

    Returns
    -------
    x, ops : list, int
        The solution with the operation count.
    """

    # initialize values
    ops = 0                             # number of operations
    dim = len(y)                        # number of variables
    x = [0 for i in range(dim)]         # the solution array

    for i in range(dim):
        # multiply matrix rows and back-substitute elements of x
        prod_sum = 0
        for j in range(i):
            prod_sum += U[dim - 1 - i][dim - 1 - j] * x[dim - 1 - j]
            ops += 1
        x[dim - 1 - i] = (y[dim - 1 - i] - prod_sum) / U[dim - 1 - i][dim - 1 - i]
                
        # update operations
        ops += 1

    # display
    if debug:
        print("\nSolution of U\n-------------------")
        print("Vector x:\t{x}".format(x=x))

    return x, ops

def get_LU_basic_OnesInL(A, debug):
    """
    Obtain the Lower-Triangular and Upper-Triangular matrices of a given matrix using Basic LU Decomposition with ones in L.

    Parameters
    ----------
    A : list
        Given coefficient matrix.
    debug : boolean
        Option to display steps.

    Returns
    -------
    L, U, ops : list, list, int
        The lower-triangular and upper-triangular matrices along with the operation count.
    """

    # initialize values
    ops = 0                             # number of operations
    dim = len(A)                        # number of variables
    # lower-triangular matrix
    L = [[1 if i==j else 0 for j in range(dim)] for i in range(dim)]
    # upper-triangular matrix
    U = [[1 if i==j else 0 for j in range(dim)] for i in range(dim)]                    
    # for each column
    for j in range(dim):
        # find the elements in each row of U
        for i in range(j + 1):
            prod_sum = 0
            for k in range (i):
                prod_sum += L[i][k] * U[k][j]

                # update operations
                ops += 1

            U[i][j] = A[i][j] - prod_sum
                
            # update operations
            ops += 1

        # find the elements in each row of L
        for i in range(j + 1, dim):
            prod_sum = 0
            for k in range (j):
                prod_sum += L[i][k] * U[k][j]

                # update operations
                ops += 1

            L[i][j] = (A[i][j] - prod_sum) / U[j][j]
                
            # update operations
            ops += 1

        # display
        if debug:
            print("\nFormation step #{j}\n-------------------".format(j=j))
            print("Matrix L:\t{L}".format(L=L))
            print("Matrix U:\t{U}".format(U=U))

    return L, U, ops

def get_solution_basic(A, b, debug):
    """
    Obtain the solution for a given system of linear equations represented as A*x = b using Basic LU Decomposition Method.

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
    sol, ops, msg : list (float), int, String
        The solution and the operation count with error string.
    """

    # initialize values
    t_ops = 0                           # total number of operations

    # display
    if debug:
        print("Input\n-------")
        print("Matrix A:\t{A}".format(A=A))
        print("Vector b:\t{B}".format(B=b))

    # get L and U
    L, U, ops = get_LU_basic_OnesInL(A, debug)
    t_ops += ops
    # get solution of L
    y, ops = get_solution_L(L, b, debug)
    t_ops += ops
    # get solution of U
    x, ops = get_solution_U(U, y, debug)
    t_ops += ops

    return x, t_ops, "Solution obtained"

def get_LU_Cholesky(A, debug):
    """
    Obtain the Lower-Triangular matrix of a symmetric positive definitive matrix using Cholesky Decomposition.

    Parameters
    ----------
    A : list
        Given matrix.
    debug : boolean
        Option to display steps.

    Returns
    -------
    L, U, ops : list, list, int
        The lower-triangular and upper-triangular matrices along with the operation count.
    """

    # initialize values
    ops = 0                             # number of operations
    dim = len(A)                        # number of variables
    # lower-triangular matrix
    L = [[0 for j in range(dim)] for i in range(dim)]

    # for each row
    for k in range(dim):
        # for each element of the row other than the k-th element
        for i in range(k):
            prod_sum = 0
            # find the sum of previous elements of that row 
            # multiplied by previous elements of k-th row
            for j in range(i):
                prod_sum += L[i][j]*L[k][j]

                # update operations
                ops += 1

            # update that element
            L[k][i] = (A[k][i] - prod_sum)/L[i][i]

            # update operations 
            ops += 2

        sq_sum = 0
        # find the sum of squares of elements in the k-th row
        # other than the k-th element 
        for j in range(k):
            sq_sum += L[k][j]**2

            # update operations 
            ops += 1
        
        # update the k-th element
        L[k][k] = math.sqrt(A[k][k] - sq_sum)

    # display
    if debug:
        print("Matrix L:\t{L}".format(L=L))

    # upper-triangular matrix
    U = [[L[j][i] for j in range(dim)] for i in range(dim)]

    return L, U, ops

def get_solution_Cholesky(A, b, debug):
    """
    Obtain the solution for a given system of linear equations represented as A*x = b where A is a symmetric positive definite matrix using Cholesky Decomposition.

    Parameters
    ----------
    A : list (list (float))
        Given matrix.
    b : list (float)
        Given constant vector.
    debug : boolean
        Option to display steps.

    Returns
    -------
    sol, ops, msg : list (float), int, String
        The solution and the operation count with error string.
    """

    # initialize values
    t_ops = 0                           # total number of operations

    # display
    if debug:
        print("Input\n-------")
        print("Matrix A:\t{A}".format(A=A))
        print("Vector b:\t{B}".format(B=b))

    # get L and U
    L, U, ops = get_LU_Cholesky(A, debug)
    t_ops += ops
    # get solution of L
    y, ops = get_solution_L(L, b, debug)
    t_ops += ops
    # get solution of U
    x, ops = get_solution_U(U, y, debug)
    t_ops += ops

    return x, t_ops, "Solution obtained"