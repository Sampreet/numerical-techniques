#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2020-01-30
# Updated: 2020-01-30

"""Example code to use root_finding -> GaussSeidelIteration module."""

# add path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'python')))

# dependencies
from modules.root_finding import GaussSeidelIteration

# Basic function
print("\nGauss-Seidel Iteration Method")

# input
A = [[1.0, 2.0, 1.0], [2.0, 6.0, -2.0], [-1.0, -3.0, 1.0]]
b = [1.0, 5.0, 2.0]
A = [[3.0, 7.0, 13.0], [1.0, 5.0, 3.0], [12.0, 3.0, -5.0]]
b = [76.0, 28.0, 1.0]
A = [[12.0, 3.0, -5.0], [1.0, 5.0, 3.0], [3.0, 7.0, 13.0]]
b = [1.0, 28.0, 76.0]

x = [0, 0, 0]
lamb = 1.0
imax = 1e5
et = 1e-2

# function
root, ops, msg = GaussSeidelIteration.get_solution_basic(A, b, x, lamb, imax, et, True)

# output
if root != None:
    print("\n\tRoot: {x}\n\tElement-wise Operations: {ops}".format(x=root, ops=ops))
else:
    print("\n\t{msg}.\n\tElement-wise Operations: {ops}".format(msg=msg, ops=ops))
