"""
A collection of methods to find roots of a univariate function using Secant Method.
"""

__all__ = ["find_root_uni"]

from decimal import Decimal
    
def find_root_uni(fn, xi, xf, err=1e-6, imax=1e6):
    """
    Find the (approximate) root of a given function using Secant Method.

    Parameters
    ----------
    fn : function
        Given function of x.
    xi : float
        Initial value of the selected bracket.
    xf : float
        Final value of the selected bracket.
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
    xf = Decimal(xf)
    err = Decimal(err)
    imax = Decimal(imax)

    # initialize values
    ic = Decimal(0)

    # check initial values
    if (Decimal(fn(xi)) == 0):
        return float(xi), ic, None
    if (Decimal(fn(xf)) == 0):
        return float(xf), ic, None

    # iterate till relative error reaches threshold
    while True: 
        ic += 1

        # no root if function values are same
        if (Decimal(fn(xi)) == Decimal(fn(xf))):
            return None, ic, "Function values are equal."

        # get intersection point
        xint = xf - Decimal(fn(xi)) * (xf - xi) / (Decimal(fn(xf)) - Decimal(fn(xi)))

        # check relative error
        curr_diff = abs(xint - xi)
        max_diff = abs(xi) * err
        xi = xf
        xf = xint
        if (curr_diff < max_diff):
            return float(xf), ic, None

        # check iteration threshold
        if (ic > imax):
            return None, ic, "Maximum iterations reached."
    return float(xi), ic, None