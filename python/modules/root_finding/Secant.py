#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-03-26
# Updated: 2020-01-12

"""Module to find roots of a univariate function using Secant Method."""
    
def find_root_uni(fn, xi, xf, et=1e-6, imax=1e6):
    """
    Find the (approximate) root of a given function using Secant Method.

    Parameters
    ----------
    fn : function
        Given function of x.
    xi : float
        Initial value of the selected bracket.
    xf : float
        Final value of the selected bracket.
    et : float (optional)
        Threshold of relative error.
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
    if (fn(xf) == 0):
        return xf, ic, "Root found"

    # iterate till maximum iteration is reached or relative error reaches threshold
    while True: 
        ic += 1

        # check iteration threshold
        if (ic >= imax):
            return None, ic, "Maximum iterations reached"

        # no root if function values are same
        if (fn(xi) == fn(xf)):
            return None, ic, "Function values are equal"

        # get intersection point
        xint = xf - fn(xi) * (xf - xi) / (fn(xf) - fn(xi))

        # check relative error
        curr_diff = abs(xint - xi)
        max_diff = abs(xi) * et
        xi = xf
        xf = xint
        if (curr_diff < max_diff):
            return xf, ic, "Approx. root found"
        
        # check value at xf
        if (fn(xf) == 0):
            return xf, ic, "Root found"

    return xi, ic, "Root found"