#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-03-26
# Updated: 2019-12-22

"""Module to test root_finding -> FixedPoint module."""

# dependencies
import unittest

from modules.root_finding import FixedPoint

class TestRootFindingFixedPoint(unittest.TestCase):
    """Tests for root_finding -> FixedPoint module."""

    def g(self, x):
        """
        Modified function for the demo function f(x) = x^2 - 5
        
        Parameters
        ----------
        x : float
            Value of the variable.
        """

        return  2 + 1 / (x + 2)

    def test_find_root_uni(self):
        """Function to test find_root_uni."""

        print("\nFixed Point Method: Univariate")

        # input
        xi = 1        # initial value
        et = 1e-6       # relative error threshold
        imax = 1e6      # maximum number of iterations to consider

        # function
        root, ic, msg = FixedPoint.find_root_uni(self.g, xi, et, imax)

        # output
        if root != None:
            print("\t{msg}: {x}\n\tFunction Value: {gx}\n\tIterations: {ic}".format(msg=msg, x=root, gx=self.g(root), ic=ic))
        else:
            print("\t{msg}.".format(msg=msg))

# start tests
if __name__ == '__main__':
    unittest.main()