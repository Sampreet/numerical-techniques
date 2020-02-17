#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2020-02-13
# Updated: 2020-02-17

"""Example code to find eigenvalues and eigenvectors using eigen -> Jacobi module."""

# add path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'python')))

# dependencies
import math
from modules.eigen import Jacobi

# Basic function
print("\nEigenvalues and Eigenvectors using Jacobi Method")

# input
A = [[  2,      math.sqrt(3)    ],
    [   math.sqrt(3),   4       ]]
A = [[  4,      2,      2,      1   ],
    [   2,      -3,     1,      1   ],
    [   2,      1,      3,      1   ],
    [   1,      1,      1,      2   ]]
A = [[  4,      2,      1,      0,      0,      0,      0,      0,      0,          0   ],
    [   2,      4,      2,      1,      0,      0,      0,      0,      0,      0   ],
    [   1,      2,      4,      2,      1,      0,      0,      0,      0,      0   ],
    [   0,      1,      2,      4,      2,      1,      0,      0,      0,      0   ],
    [   0,      0,      1,      2,      4,      2,      1,      0,      0,      0   ],
    [   0,      0,      0,      1,      2,      4,      2,      1,      0,      0   ],
    [   0,      0,      0,      0,      1,      2,      4,      2,      1,      0   ],
    [   0,      0,      0,      0,      0,      1,      2,      4,      2,      1   ],
    [   0,      0,      0,      0,      0,      0,      1,      2,      4,      2   ],
    [   0,      0,      0,      0,      0,      0,      0,      1,      2,      4   ]]

eig_val, eig_vec, ic, msg = Jacobi.get_eigens(A, 1e-4, 1e4, True)

# output
if eig_val != None:
    print("\n{msg} after {ic} iterations:\n\tEigenvalues: {eig_val}\n\tEigenvectors: {eig_vec}".format(msg=msg, ic=ic, eig_val=eig_val, eig_vec=eig_vec))
else:
    print('\n\t{msg}.')