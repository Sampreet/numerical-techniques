#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-03-26
# Updated: 2019-12-22

"""Module to test root_finding -> NewtonRaphson module."""

# dependencies
import math
import unittest

from modules.root_finding import NewtonRaphson

class TestRootFindingNewtonRaphson(unittest.TestCase):
    """Tests for root_finding -> NewtonRaphson module."""

    def fn(self, x):
        """
        Demo univariate function for testing. 
        
        Parameters
        ----------
        x : float
            Value of the variable.
        """

        return math.exp(x*2) - math.exp(x) - 2

    def df(self, x):
        """
        Derivative of the demo univariate function. 
        
        Parameters
        ----------
        x : float
            Value of the variable.
        """

        return 2*math.exp(x*2) - math.exp(x)

    def f(self, X):
        """
        First demo multivariate function for testing. 
        
        Parameters
        ----------
        X : list
            List of values of the variables.
        """

        return (X[0])**3 - (X[1])**2 + 1

    def g(self, X):
        """
        Second demo multivariate function for testing. 
        
        Parameters
        ----------
        X : list
            List of values of the variables.
        """

        return (X[0])**2 - 2*X[0] + X[1]**3 - 2

    def dfdx(self, X):
        """
        Derivative of the first demo multivariate function with respect to first variable. 
        
        Parameters
        ----------
        X : list
            List of values of the variables.
        """
        
        return 3*(X[0])**2

    def dfdy(self, X):
        """
        Derivative of the first demo multivariate function with respect to second variable. 
        
        Parameters
        ----------
        X : list
            List of values of the variables.
        """
        
        return (-2)*(X[1])

    def dgdx(self, X):
        """
        Derivative of the second demo multivariate function with respect to first variable. 
        
        Parameters
        ----------
        X : list
            List of values of the variables.
        """
        
        return 2*(X[0]) - 2

    def dgdy(self, X):
        """
        Derivative of the second demo multivariate function with respect to second variable. 
        
        Parameters
        ----------
        X : list
            List of values of the variables.
        """
        
        return 3*X[1]**2

    def test_find_root_uni(self):
        """Function to test find_root_uni."""

        print("\nNewton-Raphson Method: Univariate")

        # input
        xi = 1          # initial value
        et = 1e-6       # relative error threshold
        imax = 1e6      # maximum number of iterations to consider

        # function
        root, ic, msg = NewtonRaphson.find_root_uni(self.fn, self.df, xi, et, imax)

        # output
        if root != None:
            print("\tInitial value: {xi}\n\tRoot: {x}\n\tFunction Value: {fx}\n\tIterations: {ic}".format(xi=xi, x=root, fx=self.fn(root), ic=ic))
        else:
            print("\t{msg}.".format(msg=msg))

    def test_find_root_multi(self):
        """Function to test find_root_multi."""

        print("\nNewton-Raphson Method: Multivariate")

        # input
        xi = 1          # initial value of first variable
        yi = 1          # initial value of second variable
        em = 1e-6       # error margin
        imax = 1e3      # maximum number of iterations to consider

        # function
        root, ic, msg = NewtonRaphson.find_root_multi([self.f, self.g], [[self.dfdx, self.dfdy],[self.dgdx, self.dgdy]], [xi, yi], em, imax)

        # output
        if root != None:
            print("\tInitial value: {xi}\n\tRoot: {X}\n\tFirst function Value: {f}\n\tSecond function Value: {g}\n\tIterations: {ic}".format(xi=xi, X=root, f=self.f(root), g=self.g(root), ic=ic))
        else:
            print("\t{msg}.".format(msg=msg))

# start tests
if __name__ == '__main__':
    unittest.main()