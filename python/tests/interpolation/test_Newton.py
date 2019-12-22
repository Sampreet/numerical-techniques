#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-04-07
# Updated: 2019-12-22

"""Module to test interpolation -> Newton module."""

# dependencies
import unittest

from modules.interpolation import Newton

class TestInterpolationNewton(unittest.TestCase):
    """Tests for interpolation -> Newton module."""

    def test_find_value_with_degree_3(self):
        """Function to test find_value_with_degree_3."""

        print("\nNewton Interpolation:")

        # input
        X = [1.2, 1.3, 1.4, 1.5]
        Y = [1.063, 1.091, 1.119, 1.145]
        x = 1.35

        # function
        B, y, msg = Newton.find_value_with_degree_3(X, Y, x)

        # output
        if y != None:
            print("\tCoefficients: {B}\n\tValue: {y}".format(B=B, y=y))
        else:
            print("\t{msg}.".format(msg=msg))

# start tests
if __name__ == '__main__':
    unittest.main()