#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2020-02-03
# Updated: 2020-02-03

"""Example code to find Least Squares Fit using root_finding -> GaussianElimination module."""

# add path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'python')))

# dependencies
import math
from modules.root_finding import GaussianElimination

# Basic function
print("\nLeast Squares Fit using Gaussian Elimination Method: Basic")

# input
X = [-1.2,  -1.0,   -0.8,   -0.6,   -0.4,   -0.2,   0.0,    0.2,    0.4,    0.6]
Y = [-2,    1.0,    2.0,    3.0,    6.0,    9.0,    15.0,   9.0,    6.0,    3.0]

# number of data points
N = len(X)
# degree of polynomial
n = 11
# generate coefficient matrix 
A = []
for i in range(n + 1):
    row = []
    for j in range(n + 1):
        temp = 0
        for k in range(N):
            temp += X[k]**(i + j)
        row.append(temp/N)
    A.append(row)
# generate constant vector
b = []
for j in range(n + 1):
    temp = 0
    for k in range(N): 
        temp += X[k]**j * Y[k]
    b.append(temp/N)

print(A)
print(b)

# function
root, ops, msg = GaussianElimination.get_solution_basic(A, b, True)

print('Solution:\n---------')

# output
if root != None:
    print("\tRoot: {x}\n\tElement-wise Operations: {ops}".format(x=root, ops=ops))

    # S_r
    S_r = 0
    for i in range(N):
        temp = Y[i]
        for j in range(n + 1):
            temp -= root[j]*X[i]**j
        S_r += temp**2
    print('\tS_r: {}'.format(S_r))

    # S_t
    y_m = sum(Y)/N
    S_t = 0
    for i in range(N):
        S_t += (Y[i] - y_m)**2
    print('\tS_t: {}'.format(S_t))

    # correlation coefficient
    r = math.sqrt((S_t - S_r)/S_t)
    print('\tr: {}'.format(r))
else:
    print("\n\t{msg}.\n\tElement-wise Operations: {ops}".format(msg=msg, ops=ops))