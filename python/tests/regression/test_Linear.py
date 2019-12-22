#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-04-07
# Updated: 2019-12-22

"""Module to test regression -> Linear module."""

# dependencies
import unittest

from modules.regression import Linear

class TestRegressionLinear(unittest.TestCase):
    """Tests for regression -> Linear module."""

    def test_get_straight_line_for_data(self):
        """Function to test get_straight_line_for_data."""

        print("\nLinear Regression:")

        # input
        X = [1.0, 3.0, 4.0, 6.0, 8.0, 9.0, 11.0]
        Y = [1.0, 2.0, 4.0, 4.0, 5.0, 7.0, 8.0]

        # function
        m, c, msg = Linear.get_straight_line_for_data(X, Y)

        # output
        if m != None:
            print("\tSlope: {m}\n\tY-intercept: {c}".format(m=m, c=c))
        else:
            print("\t{msg}.".format(msg=msg))

# start tests
if __name__ == '__main__':
    unittest.main()