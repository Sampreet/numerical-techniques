#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-04-07
# Updated: 2019-12-22

"""Module to predict a value at a specified point using a given data-set via Newton Interpolation Formula."""

# dependencies
import numpy as np

def find_f(X, Y, n, i):
    """
    Find the coefficient values via recursion.

    Parameters
    ----------
    X : list (float)
        List of data points.
    Y : list (float)
        List of observations.
    n : int
        Number of elements in the functional.
    i : int
        Highest index of the functional elements.

    Returns
    -------
    f : float
        The functional value after recursive calculation.
    """
    if i==0:
        return Y[0]
    if n==2:
        # calculate the final value
        return (Y[i] - Y[i-1]) / (X[i] - X[i-1]) 
    else:
        # forward to next recursion
        return (find_f(X, Y, n-1, i) - find_f(X, Y, n-1, i-1)) / (X[i] - X[0]) 

def find_value_with_degree_3(X, Y, x):
    """
    Find the interpolated value at a specified point for the given data-set.

    Parameters
    ----------
    X : list (float)
        List of data points.
    Y : list (float)
        List of observations
    x : float
        Point at which value is to be interpolated

    Returns
    -------
    B, y, msg : list(float), float, float, int, String
        The list of coefficients and the interpolated value with the error string.
    """

    # initialize the values
    dim = len(X)                        # number of observations
    b = np.zeros(dim, dtype=np.float)   # coefficients as numpy array
    y = 0                               # the interpolated value

    # calculate the coefficients using the recursive function
    for i in range(0, dim):
        b[i] = find_f(X, Y, i + 1, i)

    # find the interpolated value at the given point
    for i in range(0, dim):
        temp_y = b[i]
        for j in range(0, i):
            temp_y *= (x - X[j])
        y += temp_y

    return b.tolist(), y, None