#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-04-07
# Updated: 2020-01-14

"""Module to find solutions of a system of linear equations using Gaussian Elimination Method."""

def find_root_basic(A, b, debug):
    """
    Find the root of a given system of linear equations represented as A*x = b using Upper-Triangular Gaussian Elimination Method.

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

    # form upper-triangular matrix
    for j in range(0, dim):
        # pivot element
        divisor = A[j][j]
        if divisor == 0:
            # display
            if debug: 
                print("Pivot element is zero")

            return None, ops, "Pivot element is zero"

        # elimination step
        for i in range(j+1, dim):
            multiplier = A[i][j]
            for k in range(0, dim):
                A[i][k] -= A[j][k] * multiplier / divisor
            b[i] -= b[j] * multiplier / divisor
                
            # update operations 
            ops += dim

        # display
        if debug:
            print("\nElimination step #{j}\n-------------------".format(j=j))
            print("Matrix A:\t{A}".format(A=A))
            print("Vector b:\t{b}".format(b=b))

    # find root by reverse substitution
    for i in range(0, dim):
        for j in range(dim - i, dim):
            b[dim - 1 - i] -= A[dim - 1 - i][j] * b[j]
            
            # update operations 
            ops += 1
        
        divisor = A[dim - 1 - i][dim - 1 - i]
        if divisor == 0:
            # display
            if debug: 
                print("Martix is singular")

            return None, ops, "Martix is singular"
        
        # divide by element
        b[dim - 1 - i] /= divisor
        
        # update operations 
        ops += 1
                
        # display
        if debug:
            print("\nBack substitution step #{i}\n-------------------------".format(i=i))
            print("Vector b:\t{b}".format(b=b))

    # display
    if debug:
        print("\nCompleted\n---------\n")

    return b, ops, "Solution obtained"

def find_root_pivot(A, B, debug):
    """
    Find the root of a given system of linear equations represented as A*X = B using Upper-Triangular Gaussian Elimination Method.

    Parameters
    ----------
    A : list (list (float))
        Given coefficient matrix.
    B : list (float) or list (list (float))
        Given constant vector or matrix.
    debug : boolean
        Option to display steps.

    Returns
    -------
    root, ops, msg : float, int, String
        The root and the operation count with error string.
    """

    # initialize values
    ops = 0                             # number of operations
    dim_x = len(A)                      # number of variables

    # if B is a 1D vector, make it a matrix
    if not type(B[0]) == list:         
        B = [[ele] for ele in B]

        # update operations
        ops += dim_x

    dim_n = len(B[0])                   # number of systems

    # display
    if debug:
        print("Input\n-------")
        print("Matrix A:\t{A}".format(A=A))
        print("Matrix B:\t{B}".format(B=B))

    # form upper-triangular matrix
    for j in range(0, dim_x):
        # scale elements
        scales = []
        for i in range(j, dim_x):
            maxi_i = max([abs(ele) for ele in A[i]])

            # if all elements are zero
            if maxi_i == 0: 
                # display
                if debug: 
                    print("Martix is singular")

                return None, ops, "Martix is singular"  
            
            # update scales
            scales.append(A[i][j]/maxi_i)

            # update operations
            ops += dim_x
        
        # display
        if debug:
            print("Scales:\t{}".format(scales))

        # check for largest element
        index = j
        maxi = 0
        for i in range(0, dim_x - j):
            if abs(scales[i]) > maxi:
                index = j + i
                maxi = scales[i]

            # update operations
            ops += 1
            
        if index != j:
            # swap rows of coefficient matrix
            temp_row = A[index]
            A[index] = A[j]
            A[j] = temp_row

            # swap rows of constant matrix
            temp_row = B[index]
            B[index] = B[j]
            B[j] = temp_row

            # display
            if debug:
                print("Swapped row #{j} with row #{index}".format(j=j, index=index))

            # update operations
            ops += 6

        # pivot element
        divisor = A[j][j]
        if divisor == 0:
            # display
            if debug: 
                print("Pivot element is zero")

            return None, ops, "Pivot element is zero"

        # elimination step
        for i in range(j+1, dim_x):
            multiplier = A[i][j]
            for k in range(0, dim_x):
                A[i][k] -= A[j][k] * multiplier / divisor
            for k in range(0, dim_n):
                B[i][k] -= B[j][k] * multiplier / divisor
                
            # update operations 
            ops += dim_x + dim_n

        # display
        if debug:
            print("\nElimination step #{j}\n-------------------".format(j=j))
            print("Matrix A:\t{A}".format(A=A))
            print("Matrix B:\t{B}".format(B=B))

    # find root by reverse substitution
    for i in range(0, dim_x):
        for k in range(0, dim_n):
            for j in range(dim_x - i, dim_x):
                B[dim_x - 1 - i][k] -= A[dim_x - 1 - i][j] * B[j][k]
                
                # update operations 
                ops += 1
            
            divisor = A[dim_x - 1 - i][dim_x - 1 - i]
            if divisor == 0:
                # display
                if debug: 
                    print("Martix is singular")

                return None, ops, "Martix is singular"
            
            # divide by element
            B[dim_x - 1 - i][k] /= divisor
            
            # update operations 
            ops += 1
                
        # display
        if debug:
            print("\nBack substitution step #{i}\n-------------------------".format(i=i))
            print("Matrix B:\t{B}".format(B=B))

    # display
    if debug:
        print("\nCompleted\n---------\n")

    return B, ops, "Solutions obtained"


            
