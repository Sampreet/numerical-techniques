#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-08-07
# Updated: 2019-12-22

"""Module to find the integration of a given function using Runge-Kutta Method."""

def integrate_with_RK4(fn, xi, xf, ss=1e-6):
    """
    Find the integration of a given function in a given interval using Runge-Kutta Method.

    Parameters
    ----------
    fn : function
        Given function of x.
    xi : float
        Initial x-value of the selected interval.
    xf : float
        Final x-value of the selected interval.
    ss : float (optional)
        Step size of integration.

    Returns
    -------
    inte, sc, msg : list, int, String
        The integration and the step count with error string.
    """