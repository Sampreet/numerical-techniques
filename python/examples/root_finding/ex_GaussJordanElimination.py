#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2020-01-15
# Updated: 2020-01-15

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
root, ops, msg = GaussJordanElimination.find_root_basic(A, b, True)

# output
if root != None:
    print("\tRoot: {x}\n\tElement-wise Operations: {ops}".format(x=root, ops=ops))
else:
    print("\t{msg}.\n\tElement-wise Operations: {ops}".format(msg=msg, ops=ops))
