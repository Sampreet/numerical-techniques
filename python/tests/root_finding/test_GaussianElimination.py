#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-04-07
# Updated: 2019-12-22

"""Module to test root_finding -> GaussianElimination module."""

# dependencies
import unittest

from modules.root_finding import GaussianElimination

class TestRootFindingGaussianElimination(unittest.TestCase):
    """Tests for root_finding -> GaussianElimination module."""

    def test_find_root_using_upper_triangle(self):
        """Function to test find_root_using_upper_triangle."""

        print("\nGaussian Elimination Method: Upper-Triangular")

        # input
        A = [[4, 0, 2, 1], [3, 2, 2, 0], [2, 1, 1, 2], [1, 3, 2, 0]]
        b = [3, -1, 2, -4]

        # function
        root, ops, msg = GaussianElimination.find_root_using_upper_triangle(A, b)

        # output
        if root != None:
            print("\tRoot: {x}\n\tOperations: {ops}".format(x=root, ops=ops))
        else:
            print("\t{msg}.\n\tOperations: {ops}".format(msg=msg, ops=ops))

# start tests
if __name__ == '__main__':
    unittest.main()