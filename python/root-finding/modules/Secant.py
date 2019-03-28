"""
A collection of methods to find roots of a univariate function using Secant Method.
"""

__all__ = ["find_root_uni"]
    
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

    # initialize values
    ic = 0

    # check initial values
    if (fn(xi) == 0):
        return xi, ic, None
    if (fn(xf) == 0):
        return xf, ic, None

    # iterate till maximum iteration is reached or relative error reaches threshold
    while True: 
        ic += 1

        # check iteration threshold
        if (ic >= imax):
            return None, ic, "Maximum iterations reached."

        # no root if function values are same
        if (fn(xi) == fn(xf)):
            return None, ic, "Function values are equal."

        # get intersection point
        xint = xf - fn(xi) * (xf - xi) / (fn(xf) - fn(xi))

        # check relative error
        curr_diff = abs(xint - xi)
        max_diff = abs(xi) * err
        xi = xf
        xf = xint
        if (curr_diff < max_diff):
            return xf, ic, None

    return xi, ic, None