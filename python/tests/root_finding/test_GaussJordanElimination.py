#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-04-07
# Updated: 2020-01-15

"""Module to test root_finding -> GaussJordanElimination module."""

# dependencies
import unittest

from modules.root_finding import GaussJordanElimination

class TestRootFindingGaussJordan(unittest.TestCase):
    """Tests for root_finding -> GaussJordanElimination module."""

    def test_find_inverse(self):
        """Function to test find_inverse."""

        print("\nGauss-Jordan Elimination Method: Inverse")

        # input
        A = [[4, 1, 0], [5, -2, 4], [-2, 1, 1]]

        # function
        Ainv, ops, msg = GaussJordanElimination.find_inverse(A)

        # output
        if Ainv != None:
            print("\tInverse: {Ainv}\n\tOperations: {ops}".format(Ainv=Ainv, ops=ops))
        else:
            print("\t{msg}.\n\tOperations: {ops}".format(msg=msg, ops=ops))

# start tests
if __name__ == '__main__':
    unittest.main()