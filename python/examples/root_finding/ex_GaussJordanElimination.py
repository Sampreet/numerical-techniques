#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2020-01-15
# Updated: 2020-01-30

"""Example code to use root_finding -> GaussJordanElimination module."""

# add path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'python')))

# dependencies
from modules.root_finding import GaussJordanElimination

# Basic function
print("\nGauss-Jordan Elimination Method: Basic")

# input
A = [[1.0, 2.0, 1.0], [2.0, 6.0, -2.0], [-1.0, -3.0, 1.0]]
b = [1.0, 5.0, 2.0]
A = [[2.0, 1.0, 7.0], [3.0, 2.0, 1.0], [1.0, 3.0, 0.0]]
b = [15.0, 14.0, 9.0]

# function
root, ops, msg = GaussJordanElimination.get_solution_basic(A, b, True)

# output
if root != None:
    print("\n\tRoot: {x}\n\tElement-wise Operations: {ops}".format(x=root, ops=ops))
else:
    print("\n\t{msg}.\n\tElement-wise Operations: {ops}".format(msg=msg, ops=ops))

# Inverse function
print("\nGauss-Jordan Elimination Method: Inverse")

A = [[      1,      2,      3,      4,      5,      6   ],
    [       7,      2,      8,      9,      10,     11  ],
    [       12,     13,     3,      14,     15,     16  ],
    [       17,     18,     19,     4,      20,     21  ],
    [       22,     23,     24,     25,     5,      26  ],
    [       27,     28,     29,     30,     31,     6   ]]

Ainv, ops, msg = GaussJordanElimination.get_inverse(A, True)

# output
if Ainv != None:
    print("\n\tInverse: {M}\n\tElement-wise Operations: {ops}".format(M=Ainv, ops=ops))
else:
    print("\n\t{msg}.\n\tElement-wise Operations: {ops}".format(msg=msg, ops=ops))
