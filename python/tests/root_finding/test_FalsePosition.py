#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-03-26
# Updated: 2019-12-22

"""Module to test root_finding -> FalsePosition module."""

# dependencies
import math
import unittest

from modules.root_finding import FalsePosition

class TestRootFindingFalsePosition(unittest.TestCase):
    """Tests for root_finding -> FalsePosition module."""

    def fn(self, x):
        """
        Demo univariate function for testing. 
        
        Parameters
        ----------
        x : float
            Value of the variable.
        """

        return math.exp(x*2) - math.exp(x) - 2

    def test_find_root_in_interval(self):
        """Function to test find_root_in_interval."""

        print("\nFalse Position Method: Root in Interval")

        # input
        xi = 0          # initial value
        xf = 1          # final value
        et = 1e-6       # relative error threshold

        # function
        root, ic, msg = FalsePosition.find_root_in_interval(self.fn, xi, xf, et)

        # output
        if root != None:
            print("\tInterval: [{xi}, {xf}]\n\t{msg}: {x}\n\tFunction Value: {fx}\n\tIterations: {ic}".format(xi=xi, xf=xf, msg=msg, x=root, fx=self.fn(root), ic=ic))
        else:
            print("\t{msg}.".format(msg=msg))

    def test_find_all_roots(self):
        """Function to test find_all_roots."""

        print("\nFalse Position Method: All Roots")

        # input
        xmin = -1e2     # minimum x-value
        xmax = 1e2      # maximum x-value
        step = 1e0      # step-size of interval
        et = 1e-6       # relative error threshold

        # function
        roots, ic = FalsePosition.find_all_roots(self.fn, xmin, xmax, step, et)

        if len(roots) != 0:
            print("\tAll Roots: {X}\n\tIterations: {ic}".format(X=roots, ic=ic))
        else:
            print("\tNo root found with given initial values.")

# start tests
if __name__ == '__main__':
    unittest.main()