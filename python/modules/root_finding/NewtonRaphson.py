#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-03-26
# Updated: 2020-01-12

"""Module to find roots of a function using Newton-Raphson Method."""

# dependencies
import numpy as np
    
def find_root_uni(fn, df, xi, et=1e-6, imax=1e6):
    """
    Find the (approximate) root of a given univariate function using Newton-Raphson Method.

    Parameters
    ----------
    fn : function
        Given function of x.
    df : function
        Derivative of the given function of x.
    xi : float
        Initial point of selection.
    et : float (optional)
        Relative error threshold.
    imax : int (optional)
        Maximum number of iterations to consider.

    Returns
    -------
    root, ic, msg : float, int, String
        The root and the iteration count with error string.
    """

    # initialize values
    ic = 0

    # check initial values
    if (fn(xi) == 0):
        return xi, ic, "Root found"

    # iterate till maximum iteration is reached or relative error reaches threshold
    while True: 
        ic += 1
        
        # check iteration threshold
        if (ic >= imax):
            return None, ic, "Maximum iterations reached"

        # no root if derivative is zero
        if df(xi) == 0:
            return None, ic, "Derivative is zero"

        # get intersection point
        xint = xi - fn(xi) / df(xi)

        # check relative error
        curr_diff = abs(xint - xi)
        max_diff = abs(xi) * et
        xi = xint
        if (curr_diff < max_diff):
            return xi, ic, "Approx. root found"
        
        # check value at xi
        if (fn(xi) == 0):
            return xi, ic, "Root found"

    return xi, ic, "Root found"

def find_root_multi(Fn, Dn, X, em=1, imax=1e6):
    """
    Find the (approximate) root of a given system of multivariate function using Newton-Raphson Method.

    Parameters
    ----------
    Fn : list (function)
        Given set of equations.
    Dn : list (list (function))
        Partial derivative equations of the given set.
    X : list (float)
        Initial point of selection.
    em : float (optional)
        Error margin.
    imax : int (optional)
        Maximum number of iterations to consider.

    Returns
    -------
    root, ic, msg : float, int, String
        The root and the iteration count with error string.
    """

    # initialize values
    ic = 0

    # iterate till maximum error is reached or relative error reaches threshold
    while True:
        ic += 1
        
        # check iteration threshold
        if (ic >= imax):
            return X, ic, "Maximum iteration reached"

        # check convergence
        is_converging = True
        for i in range(0, len(Dn)):
            if sum(list(map(lambda dn: dn(X), Dn[i]))) > em:
                is_converging = False
                break
        if (is_converging):
            return X, ic, None
        
        # obtain partial jacobian matrices for each variable 
        Det_D = list(map(lambda index: get_jacobian_determinant(Fn, Dn, X, index), list(range(0, len(Fn) + 1))))

        # check if denominator is zero
        if Det_D[0] == 0:
            return None, ic, "Denominator is zero"

        # update values
        for i in range(0, len(X)):
            X[i] = X[i] - Det_D[i+1]/Det_D[0]

    return X, ic, None

def get_jacobian_determinant(Fn, Dn, X, index):
    """
    Get the determinant of a partial Jacobian matrix of a given set of equations.
    
    Parameters
    ----------
    Fn : list (function)
        Given set of equations.
    Dn : list (list (function))
        Partial derivative equations of the given set.
    X : list (float)
        Initial point of selection.
    index : int
        Index of the variable for which the determinant is to be calculated.

    Returns
    -------
    det: float
        Value of the determinant
    """

    # initialize values
    mat = []

    for i in range(0, len(Fn)):
        temp = []

        for j in range(0, len(Fn)):
            # if the column is same, take the functional value
            if j == index - 1:
                temp.append(Fn[i](X))
            
            # else take the partial derivate value
            else:
                temp.append(Dn[i][j](X))

        mat.append(temp)

    # reconvert the array to numpy array
    mat = np.array(mat)

    # return determinant of matrix
    return np.linalg.det(mat)
                