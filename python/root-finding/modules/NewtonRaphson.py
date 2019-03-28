"""
A collection of methods to find roots of a function using Newton-Raphson Method.
"""

__all__ = ["find_root_uni"]

from decimal import Decimal
    
def find_root_uni(fn, df, xi, err=1e-6, imax=1e6):
    """
    Find the (approximate) root of a given univariate function using Newton-Raphson Method.

    Parameters
    ----------
    fn : function
        Given function of x.
    df : function
        Derivative of the given function of x.
    xi : float
        Initial point of selection.
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
    if (Decimal(fn(xi)) == 0):
        return float(xi), ic, None

    # iterate till relative error reaches threshold
    while True: 
        ic += 1

        # no root if derivative is zero
        if Decimal(df(xi)) == 0:
            return None, ic, "Derivative is zero."

        # get intersection point
        xint = xi - Decimal(fn(xi)) / Decimal(df(xi))

        # check relative error
        curr_diff = abs(xint - xi)
        max_diff = abs(xi) * err
        xi = xint
        if (curr_diff < max_diff):
            return float(xi), ic, None
        
        # check iteration threshold
        if (ic > imax):
            return None, ic, "Maximum iterations reached."

    return float(xi), ic, None