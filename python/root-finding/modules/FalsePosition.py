"""
A collection of methods to find roots of a univariate function using False Position Method.
"""

__all__ = ["find_root_in_bracket", "find_all_roots"]

from decimal import Decimal

def find_root_in_bracket(fn, xi, xf, err=1e-6):
    """
    Find the (approximate) root of a given function using False Position Method.

    Parameters
    ----------
    fn : function
        Given function of x.
    xi : float
        Initial x-value of the selected bracket.
    xf : float
        Final x-value of the selected bracket.
    err : float (optional)
        Relative error threshold.

    Returns
    -------
    root, ic, msg : float, int, String
        The root and the iteration count with error string.
    """

    # redefine data-type to handle large numbers
    xi = Decimal(xi)
    xf = Decimal(xf)
    err = Decimal(err)

    # initialize values
    ic = Decimal(0)

    # check initial values
    if (Decimal(fn(xi)) * Decimal(fn(xf)) > 0):
        return None, ic, "No root confirmed in given interval."
    elif (Decimal(fn(xi)) == 0):
        return float(xi), ic, None
    elif (Decimal(fn(xf)) == 0):
        return float(xf), ic, None

    # iterate till relative error reaches threshold
    while True: 
        ic += 1

        # get intersection point
        xint = xi - Decimal(fn(xi)) * (xi - xf) / (Decimal(fn(xi)) - Decimal(fn(xf)))

        # check relative error
        curr_diff = abs(xint - xi)
        max_diff = abs(xi) * err
        if (curr_diff < max_diff):
            return float(xi), ic, None

        # update bracket
        if (Decimal(fn(xi)) * Decimal(fn(xint)) < 0):
            xf = xint
        elif (Decimal(fn(xint)) == 0):
            xi = xint
            return float(xi), ic, None
        else:
            xi = xint

    return float(xi), ic, None

def find_all_roots(fn, step=1e0, xmax=1e6, err=1e-6):
    """
    Find the (approximate) root of a given function using False Position Method.

    Parameters
    ----------
    fn : function
        Given function of x.
    step : float (optional)
        Step-size for the x-axis bracket.
    xmax : float (optional)
        Maximum absolute value of x to check for roots.
    et : float (optional)
        Relative error threshold.

    Returns
    -------
    roots, ic, msg : list (float), int, String
        List of roots and the total iteration count with error string.
    """

    # redefine data-type to handle large numbers
    step = Decimal(step)
    xmax = Decimal(xmax)
    err = Decimal(err)

    # initialize values
    ic = Decimal(0)
    xi = Decimal(0)
    xf = step
    roots = []

    while True:
        # search in (+)ve x-axis
        root, ii, msg = find_root_in_bracket(fn, xi, xf, err)
        if root != None: 
            roots.append(float(root))
            ic += Decimal(ii)
        else:
            ic += 1

        # search in (-)ve x-axis
        root, ii, msg = find_root_in_bracket(fn, 0 - xi, 0 - xf)
        if root != None: 
            roots.append(float(root))
            ic += Decimal(ii)
        else:
            ic += 1

        # update brackets
        xi += step
        xf += step

        # stop if maximum value of x is reached
        if (xi > xmax):
            break

    return list(set(roots)), ic, None
    