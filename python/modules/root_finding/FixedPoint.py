#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-03-26
# Updated: 2019-12-22

"""Module to find roots of a function using Fixed Point Method."""
    
def find_root_uni(g, xi, et=1e-6, imax=1e6):
    """
    Find the (approximate) root of a given function using Fixed Point Method.

    Parameters
    ----------
    g : function
        Modified function prepared as g(x) = x modified from the given function f(x).
    xi : float
        Initial value of the function.
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
    if (g(xi) == xi):
        return xi, ic, "Root found"

    # iterate till maximum iterations is reached or relative error reaches threshold
    while True: 
        ic += 1

        # check iteration threshold
        if (ic >= imax):
            return None, ic, "Maximum iterations reached."

        # update value
        xnew = g(xi)

        # check relative error
        curr_diff = abs(xnew - xi)
        max_diff = abs(xi) * et
        xi = xnew
        if (curr_diff < max_diff):
            return xi, ic, "Approx. root found"

    return xi, ic, "Root found"