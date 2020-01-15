#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2020-01-14
# Updated: 2020-01-15

"""Example code to use root_finding -> GaussianElimination module."""

# add path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'python')))

# dependencies
from modules.root_finding import GaussianElimination

# Basic function
print("\nGaussian Elimination Method: Basic")

# input
A = [[2.0, 3.0, 1.0], [3.0, 3.0, -5.0], [-1.0, 4.0, 2.0]]
b = [25.0, -9.0, 30.0]
A = [[1.0, 2.0, 2.0], [3.0, 6.0, -1.0], [1.0, 3.0, 1.0]]
b = [21.0, 7.0, 15.0]
A = [[1.0, 1.0, 7.0], [3.0, 2.0, 1.0], [1.0, 3.0, 0.0]]
b = [12.0, 14.0, 9.0]

# function
root, ops, msg = GaussianElimination.find_root_basic(A, b, True)

# output
if root != None:
    print("\tRoot: {x}\n\tElement-wise Operations: {ops}".format(x=root, ops=ops))
else:
    print("\t{msg}.\n\tElement-wise Operations: {ops}".format(msg=msg, ops=ops))

# Advanced function with partial pivoting
print("\nGaussian Elimination Method: Partial Pivoting")

# input
A = [[1.0, 2.0, 2.0], [3.0, 6.0, -1.0], [1.0, 3.0, 1.0]]
B = [21.0, 7.0, 15.0]
A = [[1.0, 1.0, 1.0], [1.0, 2.0, -1.0], [1.0, -2.0, 1.0]]
B = [[4.0, 3.0, 2.0], [3.0, 7.0, 8.0], [1.0, -3.0, -10.0]]

# function
root, ops, msg = GaussianElimination.find_root_pivot(A, B, True)

# output
if root != None:
    print("\tRoot: {x}\n\tElement-wise Operations: {ops}".format(x=root, ops=ops))
else:
    print("\t{msg}.\n\tElement-wise Operations: {ops}".format(msg=msg, ops=ops))
