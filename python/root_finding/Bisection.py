"""
A collection of methods to find roots of a univariate function using Bisection Method.
"""

__all__ = ["find_root_in_bracket", "find_all_roots"]

def find_root_in_bracket(fn, xi, xf, err=1e-6):
    """
    Find the (approximate) root of a given function in a given bracket using Bisection Method.

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

    # initialize values
    ic = 0

    # check initial values
    if (fn(xi) * fn(xf) > 0):
        return None, ic, "No root confirmed in given interval."
    elif (fn(xi) == 0):
        return xi, ic, None
    elif (fn(xf) == 0):
        return xf, ic, None

    # iterate till relative error reaches threshold
    while True: 
        ic += 1

        # get mean
        xm = (xi + xf) / 2

        # check relative error
        curr_diff = abs(xm - xi)
        max_diff = abs(xi) * err
        if (curr_diff < max_diff):
            return float(xi), ic, None

        # update bracket
        if (fn(xi) * fn(xm) < 0):
            xf = xm
        elif (fn(xm) == 0):
            xi = xm
            return xi, ic, None
        else:
            xi = xm

    return xi, ic, None

def find_all_roots(fn, step=1e0, xmax=1e6, err=1e-6):
    """
    Find the (approximate) root of a given function using Bisection Method.

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

    # initialize values
    ic = 0
    xi = 0
    xf = step
    roots = []

    while True:
        # search in (+)ve x-axis
        root, ii, msg = find_root_in_bracket(fn, xi, xf, err)
        if root != None: 
            roots.append(root)
            ic += ii
        else:
            ic += 1

        # search in (-)ve x-axis
        root, ii, msg = find_root_in_bracket(fn, 0 - xi, 0 - xf)
        if root != None: 
            roots.append(root)
            ic += ii
        else:
            ic += 1

        # stop if maximum value of x is reached
        if (xi >= xmax):
            break

        # update brackets
        xi += step
        xf += step

    return list(set(roots)), ic, None