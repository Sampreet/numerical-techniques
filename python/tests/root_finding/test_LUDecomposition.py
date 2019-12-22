#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-04-07
# Updated: 2019-12-22

"""Module to test root_finding -> LUDecomposition module."""

# dependencies
import unittest

from modules.root_finding import LUDecomposition

class TestRootFindingLUDecomposition(unittest.TestCase):
    """Tests for root_finding -> LUDecomposition module."""

    def test_find_root_with_ones_in_L(self):
        """Function to test find_root_with_ones_in_L."""

        print("\nLU Decomposition Method: 1s in Lower Triangular Matrix")

        # input
        A = [[2, 4, -6], [1, 3, 1], [2, -4, -2]]
        b = [-8, 10, -12]

        # function
        root, ops, msg = LUDecomposition.find_root_with_ones_in_L(A, b)

        # output
        if root != None:
            print("\tRoot: {x}\n\tOperations: {ops}".format(x=root, ops=ops))
        else:
            print("\t{msg}.\n\tOperations: {ops}".format(msg=msg, ops=ops))

# start tests
if __name__ == '__main__':
    unittest.main()