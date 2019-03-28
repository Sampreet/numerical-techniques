"""
A collection of methods to find roots of a function using Newton-Raphson Method.
"""

__all__ = ["find_root_uni"]

from decimal import Decimal
    
def find_root_uni(g, xi, err=1e-6, imax=1e6):
    """
    Find the (approximate) root of a given function using Fixed Point Method.

    Parameters
    ----------
    g : function
        Modified function prepared as g(x) = x modified from the given function f(x).
    xi : float
        Initial value of the function.
    err : float (optional)
        Threshold of relative error.
    imax : int (optional)
        Maximum number of iterations to consider.

    Returns
    -------
    root, ic, msg : float, int, String
        The root and the iteration count with error string.
    """

    # redefine data-type to handle large numbers
    xi = Decimal(xi)
    err = Decimal(err)
    imax = Decimal(imax)

    # initialize values
    ic = Decimal(0)

    # check initial values
    if (Decimal(g(xi)) == xi):
        return float(xi), ic, None

    # iterate till relative error reaches threshold
    while True: 
        ic += 1

        # update value
        xnew = Decimal(g(xi))

        # check relative error
        curr_diff = abs(xnew - xi)
        max_diff = abs(xi) * err
        xi = xnew
        if (curr_diff < max_diff):
            return float(xi), ic, None

        # check iteration threshold
        if (ic > imax):
            return None, ic, "Maximum iterations reached."
    return xi, ic, None