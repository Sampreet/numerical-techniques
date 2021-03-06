#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-03-26
# Updated: 2020-01-12

"""Module to find roots of a univariate function using Bisection Method."""

def find_root_in_interval(fn, xi, xf, et=1e-6):
    """
    Find the (approximate) root of a univariate function in a given interval using Bisection Method.

    Parameters
    ----------
    fn : function
        Given function of x.
    xi : float
        Initial x-value of the selected bracket.
    xf : float
        Final x-value of the selected interval.
    et : float (optional)
        Relative error threshold.

    Returns
    -------
    root, ic, msg : float, int, String
        The root and the iteration count with status message.
    """

    # initialize values
    ic = 0

    # check initial values
    if (fn(xi) * fn(xf) > 0):
        return None, ic, "No confirmed root"
    elif (fn(xi) == 0):
        return xi, ic, "Root found"
    elif (fn(xf) == 0):
        return xf, ic, "Root found"

    # iterate till relative error reaches threshold
    while True: 
        ic += 1

        # get mean
        xm = (xi + xf) / 2

        # check relative error
        curr_diff = abs(xm - xi)
        max_diff = abs(xi) * et
        if (curr_diff < max_diff):
            return xi, ic, "Approx. root found"

        # update interval
        if (fn(xi) * fn(xm) < 0):
            xf = xm
        elif (fn(xm) == 0):
            xi = xm
            return xi, ic, "Root found"
        else:
            xi = xm

    return xi, ic, "Root found"

def find_all_roots(fn, xmin=-1e6, xmax=1e6, step=1e0, et=1e-6):
    """
    Find the (approximate) roots of a univariate function using Bisection Method.

    Parameters
    ----------
    fn : function
        Given function of x.
    xmin : float (optional)
        Minimum value of x to check for roots.
    xmax : float (optional)
        Maximum value of x to check for roots.
    step : float (optional)
        Step-size for the x-axis interval.
    et : float (optional)
        Relative error threshold.

    Returns
    -------
    roots, ic : list (float), int
        List of roots and the total iteration count.
    """

    # initialize values
    ic = 0
    xi = xmin
    xf = xmin + step - step * et
    roots = []

    while True:
        # stop if maximum value of x is reached
        if (xi >= xmax):
            break

        # search for root in interval
        root, ii, msg = find_root_in_interval(fn, xi, xf, et)
        if root != None: 
            roots.append(root)
            ic += ii
            print("\t{0} in [{1}, {2}] : {3}".format(msg, xi, xf, root))
        else:
            ic += 1

        # update interval
        xi += step
        xf += step
        if xf >= xmax:
            xf = xmax

    return roots, ic