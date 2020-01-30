#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2020-01-12
# Updated: 2020-01-30

"""Example code to use root_finding -> NewtonRaphson module."""

# add path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'python')))

# dependencies
import math

from modules.root_finding import NewtonRaphson

def fn(x):
    """
    Demo univariate function for testing. 
    f(x) = - D/x^2 - A/B*e^(-x/B) + 6*C/x^7
    
    Parameters
    ----------
    x : float
        Value of the variable.
    """

    # coefficients
    A = 728.0
    B = 0.317
    C = 0.486
    D = -8.99 * 1.6

    # function
    fx = - D / x**2 - A / B * math.exp(- x / B) + 6 * C / x**7

    return fx

def df(x):
    """
    Derivative of the demo univariate function. 
    df(x)/dx = 2*D/x^3 + A/B^2*e^(-x/B) - 42*C/x^8
    
    Parameters
    ----------
    x : float
        Value of the variable.
    """

    # coefficients
    A = 728.0
    B = 0.317
    C = 0.486
    D = -8.99 * 1.6

    # function
    dfx = 2 * D / x**3 + A / B**2 * math.exp(- x / B) - 42 * C / x**8

    return dfx

print("\nNewton-Raphson Method: Univariate")

# input
xi = 1          # initial value
et = 1e-3       # relative error threshold
imax = 1e6      # maximum number of iterations to consider

# function
root, ic, msg = NewtonRaphson.find_root_uni(fn, df, xi, et, imax)

# output
if root != None:
    print("\n\tInitial value: {xi}\n\tRoot: {x}\n\tFunction value: {fx}\n\tIterations: {ic}".format(xi=xi, x=root, fx=fn(root), ic=ic))
else:
    print("\n\t{msg}.".format(msg=msg))