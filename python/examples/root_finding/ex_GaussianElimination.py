#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2020-01-14
# Updated: 2020-01-30

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
A = [[      1,      2,      3,      4,      5,      6   ],
    [       7,      2,      8,      9,      10,     11  ],
    [       12,     13,     3,      14,     15,     16  ],
    [       17,     18,     19,     4,      20,     21  ],
    [       22,     23,     24,     25,     5,      26  ],
    [       27,     28,     29,     30,     31,     6   ]]
b = [       6,      5,      4,      3,      2,      1   ]

# function
root, ops, msg = GaussianElimination.get_solution_basic(A, b, True)

# output
if root != None:
    print("\n\tRoot: {x}\n\tElement-wise Operations: {ops}".format(x=root, ops=ops))
else:
    print("\n\t{msg}.\n\tElement-wise Operations: {ops}".format(msg=msg, ops=ops))

# Advanced function with partial pivoting
print("\nGaussian Elimination Method: Partial Pivoting")

# input
A = [[1.0, 2.0, 2.0], [3.0, 6.0, -1.0], [1.0, 3.0, 1.0]]
B = [21.0, 7.0, 15.0]
A = [[1.0, 1.0, 1.0], [1.0, 2.0, -1.0], [1.0, -2.0, 1.0]]
B = [[4.0, 3.0, 2.0], [3.0, 7.0, 8.0], [1.0, -3.0, -10.0]]
A = [[      1,      2,      3,      4,      5,      6   ],
    [       7,      2,      8,      9,      10,     11  ],
    [       12,     13,     3,      14,     15,     16  ],
    [       17,     18,     19,     4,      20,     21  ],
    [       22,     23,     24,     25,     5,      26  ],
    [       27,     28,     29,     30,     31,     6   ]]
B = [       [6],      [5],      [4],      [3],      [2],      [1]   ]

# function
root, ops, msg = GaussianElimination.get_solution_pivot(A, B, False)

# output
if root != None:
    print("\n\tRoot: {x}\n\tElement-wise Operations: {ops}".format(x=root, ops=ops))
else:
    print("\n\t{msg}.\n\tElement-wise Operations: {ops}".format(msg=msg, ops=ops))