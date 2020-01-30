#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2020-01-30
# Updated: 2020-01-30

"""Module to obtain solutions of a system of linear equations using Jacobi Iteration Method."""

# dependencies
import math

def get_solution_basic(A, b, x, lamb, imax, et, debug):
    """
    Obtain the solution for a given system of linear equations represented as A*x = b using Jacobi Iteration Method.

    Parameters
    ----------
    A : list
        Given coefficient matrix.
    b : list
        Given constant vector.
    x : list
        Initial values of the variables.
    lamb: float
        Value of the weight.
    imax : int
        Maximum number of iterations.
    et : float
        Relative error threshold.
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
    ic = 0                              # iteration counter

    # display
    if debug:
        print("Input\n-------")
        print("Matrix A:\t{A}".format(A=A))
        print("Vector b:\t{B}".format(B=b))
        print("Vector x:\t{x}".format(x=x))

    # for each row
    for i in range(dim):
        divisor = A[i][i]

        # if diagonal element is zero
        if divisor == 0:
            return None, ops, "Diagonal element is zero"

        # divide by diagonal element
        for j in range(dim):
            A[i][j] /= divisor
        
        b[i] /= divisor

        # update operations
        ops += dim + 1

    # initial iteration
    x_new = []
    # for each variable
    for i in range(dim):
        temp = b[i]
        for j in range(dim):
            if not i==j :
                temp -= A[i][j]*x[j]
        x_new.append(temp)
    
    # update solution
    x = x_new
    # update operations
    ops += dim - 1
    
    # update iteration count
    ic = 1

    # display
    if debug:
        print("\nIteration #{ic}\n-------------------".format(ic=ic))
        print("Vector x:\t{x}".format(x=x))

    while(True):
        # flag to check if relative error threshold is reached
        flag = 1

        x_new = []
        # for each variable
        for i in range(dim):
            # get new value
            curr = b[i]
            for j in range(dim):
                if i != j :
                    curr -= A[i][j]*x[j]

            # update new variable with weight
            x_new.append(lamb*curr + (1 - lamb)*x[i])

            # update operations
            ops += dim - 1 + 2

            # check relative error
            if flag == 1 and x_new[i] != 0:
                if abs((x_new[i] - x[i])/x_new[i]) > et:
                    flag = 0
        
        # update solution
        x = x_new

        # update iteration count
        ic += 1

        # display
        if debug:
            print("\nIteration #{ic}\n-------------------".format(ic=ic))
            print("Vector x:\t{x}".format(x=x))

        # check iteration threshold
        if ic > imax:
            return x, ops, "Maximum iterations reached"     

        # check flag
        if flag == 1:
            return x, ops, "Approx. solution obtained"    



            
