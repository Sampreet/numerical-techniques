#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2020-02-09
# Updated: 2020-02-09

"""Example code for Nonlinear Regression using root_finding -> GaussianElimination module."""

# add path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'python')))

# dependencies
import math

from modules.root_finding import GaussJordanElimination

# Basic function
print("\nNonlinear Regression using Gauss-Newton Method: Basic")

# input
X = [0.0,   0.5,    1.0,    1.5,    2.0,    2.5,    3.0,    3.5,    4.0,    4.5]
Y = [0.00,  0.27,   0.52,   0.68,   0.77,   0.89,   0.91,   0.96,   1.09,   1.13]

# initial values
A_i = [1, 1]

# relative error
et = 1e-4

imax = 1e4
debug = False

# function
def f(x, A):
    return A[0]*(1 - math.exp(-A[1]*x))

# partial derivatives
def dfdA(x, A):
    res = []
    res.append(1 - math.exp(-A[1]*x))
    res.append(A[0]*x*math.exp(-A[1]*x))

    return res

# number of data points
N = len(X)

# number of coefficients 
n = len(A_i)

ic = 0
status = 0
while(True):
    ic += 1

    print('\nIteration #\t{}'.format(ic))
    print('-----------')

    # generate difference vector for Y
    D = [Y[i] - f(X[i], A_i) for i in range(N)]

    # generate partial derivative matrix
    Z = [dfdA(X[i], A_i) for i in range(N)]

    if debug:
        print('Matrix Z:\t{}'.format(Z))
        print('Vector D:\t{}'.format(D))

    # compute coefficient matrix
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            temp = 0
            for k in range(N):
                temp += Z[k][i]*Z[k][j]
            row.append(temp)
        A.append(row)
    
    # compute constant vector
    B = []
    for i in range(n):
        temp = 0
        for k in range(N): 
            temp += Z[k][i]*D[k]
        B.append(temp)
    
    if debug:
        print('Matrix A:\t{}'.format(A))
        print('Vector B:\t{}'.format(B))

    # get inverse matrix
    Ainv, ops, msg = GaussJordanElimination.get_inverse(A, debug)

    if Ainv == None:
        print("\n\t{msg}.\n\tElement-wise Operations: {ops}".format(msg=msg, ops=ops))
        break 

    # compute difference vector for coefficients
    Delta_A = []
    for i in range(n):
        temp = 0
        for k in range(n): 
            temp += Ainv[i][k]*B[k]
        Delta_A.append(temp)
    
    if debug:
        print('Matrix A_inv:\t{}'.format(Ainv))
        print('Vector Delta_A:\t{}'.format(Delta_A))
    
    A_f = [A_i[i] + Delta_A[i] for i in range(n)]
    Et = [abs((A_f[i] - A_i[i])/A_f[i]) for i in range(n)]

    print('Coefficients: {}'.format(A_f))
    print('Errors: {}'.format(Et))

    check = [1 if Et[i] < et else 0 for i in range(n)]
    if sum(check) == n:
        status = 1
        break
    
    if ic > imax: 
        status = 2
        break

    A_i = A_f

if status != 0:
    print('\nSolution:\n---------')

    # nonlinear coefficients
    print('\tCoefficients:\t{}'.format(A_i))

    # S_r
    S_r = 0
    for i in range(N):
        S_r += (Y[i] - f(X[i], A_i))**2
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
    print('\tSolution not obtained\n---------')


