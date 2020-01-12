#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-03-26
# Updated: 2020-01-12

"""Module to test root_finding -> Secant module."""

# dependencies
import math
import unittest

from modules.root_finding import Secant

class TestRootFindingSecant(unittest.TestCase):
    """Tests for root_finding -> Secant module."""

    def fn(self, x):
        """
        Demo univariate function for testing. 
        
        Parameters
        ----------
        x : float
            Value of the variable.
        """

        return math.exp(x*2) - math.exp(x) - 2

    def test_find_root_uni(self):
        """Function to test find_root_uni."""

        print("\nSecant Method: Univariate")

        # input
        xi = 1          # initial value
        xf = 3          # initial value
        et = 1e-6       # relative error threshold
        imax = 1e6      # maximum number of iterations to consider

        # function
        root, ic, msg = Secant.find_root_uni(self.fn, xi, xf, et, imax)

        # output
        if root != None:
            print("\tInitial values: {xi} and {xf}\n\tRoot: {x}\n\tFunction Value: {fx}\n\tIterations: {ic}".format(xi=xi, xf=xf, x=root, fx=self.fn(root), ic=ic))
        else:
            print("\t{msg}.".format(msg=msg))

# start tests
if __name__ == '__main__':
    unittest.main()