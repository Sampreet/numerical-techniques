"""
A collection of methods to find the roots of univariate functions.
"""

__all__ = ["bisection", "false_position", "newton_raphson", "secant"]

def bisection(f, xi, xf, et=1e-6):
    """
    Find the (approximate) root of a given function using Bisection Method.

    Parameters
    ----------
    f : function
        Given function.
    xi : float
        Initial value of the selected bracket.
    xf : float
        Final value of the selected bracket.
    et : float (optional)
        Threshold of relative error.

    Returns
    -------
    root, ic : float, int
        The root and the iteration count.
    """

    ic = 0

    # check initial values
    if (f(xi)*f(xf) > 0):
        return None, ic
    elif (f(xi) == 0):
        return xi, ic
    elif (f(xf) == 0):
        return xf, ic

    # iterate till relative error reaches threshold
    while True: 
        ic += 1

        # get mean
        xm = (xi + xf) / 2

        # check relative error
        curr_diff = abs(xm - xi)
        max_diff = abs(xi) * et
        if (curr_diff < max_diff):
            return xi, ic

        # update bracket
        if (f(xi)*f(xm) < 0):
            xf = xm
        elif (f(xm) == 0):
            xi = xm
            return xm, ic
        else:
            xi = xm

    return xi, ic

def false_position(f, xi, xf, et=1e-6):
    """
    Find the (approximate) root of a given function using False Position Method.

    Parameters
    ----------
    f : function
        Given function.
    xi : float
        Initial value of the selected bracket.
    xf : float
        Final value of the selected bracket.
    et : float (optional)
        Threshold of relative error.

    Returns
    -------
    root, ic : float, int
        The root and the iteration count.
    """

    ic = 0

    # check initial values
    if (f(xi)*f(xf) > 0):
        return None, ic
    elif (f(xi) == 0):
        return xi, ic
    elif (f(xf) == 0):
        return xf, ic

    # iterate till relative error reaches threshold
    while True: 
        ic += 1

        # get intersection point
        xint = xi - f(xi) * (xi - xf) / (f(xi) - f(xf))

        # check relative error
        curr_diff = abs(xint - xi)
        max_diff = xi * et
        if (curr_diff < max_diff):
            return xi, ic

        # update bracket
        if (f(xi)*f(xint) < 0):
            xf = xint
        elif (f(xint) == 0):
            xi = xint
            return xi, ic
        else:
            xi = xint

    return xi, ic
    
def newton_raphson(f, df, xi, et=1e-6, mi=1e6):
    """
    Find the (approximate) root of a given function using Newton-Raphson Method.

    Parameters
    ----------
    f : function
        Given function.
    df : function
        Derivative of the given function.
    xi : float
        Initial point of selection.
    et : float (optional)
        Threshold of relative error.
    mi : int (optional)
        Maximum number of iterations to consider.

    Returns
    -------
    root, ic : float, int
        The root and the iteration count.
    """

    ic = 0

    # check initial values
    if (f(xi) == 0):
        return xi, ic

    # iterate till relative error reaches threshold
    while True: 
        ic += 1

        # no root if derivative is zero
        if df(xi) == 0:
            return None, ic

        # get intersection point
        xint = xi - f(xi) / df(xi) 

        # check relative error
        curr_diff = abs(xint - xi)
        max_diff = xi * et
        xi = xint
        if (curr_diff < max_diff):
            return xi, ic
        
        # check iteration threshold
        if (ic > mi):
            return None, ic

    return xi, ic
    
def secant(f, xi, xf, et=1e-6, mi=1e6):
    """
    Find the (approximate) root of a given function using Secant Method.

    Parameters
    ----------
    f : function
        Given function.
    xi : float
        Initial value of the selected bracket.
    xf : float
        Final value of the selected bracket.
    et : float (optional)
        Threshold of relative error.
    mi : int (optional)
        Maximum number of iterations to consider.

    Returns
    -------
    root, ic : float, int
        The root and the iteration count.
    """

    ic = 0

    # check initial values
    if (f(xi) == 0):
        return xi, ic
    if (f(xf) == 0):
        return xf, ic

    # iterate till relative error reaches threshold
    while True: 
        ic += 1

        # no root if function values are same
        if (f(xi) == f(xf)):
            return None, ic

        # get intersection point
        xint = xf - f(xi) * (xf - xi) / (f(xf) - f(xi))

        # check relative error
        curr_diff = abs(xint - xi)
        max_diff = xi * et
        xi = xf
        xf = xint
        if (curr_diff < max_diff):
            return xf, ic

        # check iteration threshold
        if (ic > mi):
            return None, ic
    return xi, ic
    