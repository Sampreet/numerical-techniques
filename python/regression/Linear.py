"""
A Linear Regression library to fit a straight line for a given data-set.
"""

__all__ = ["get_straight_line_from_data"]

def get_straight_line_from_data(X, Y):
    """
    Find the straight line equation for the given data-set.

    Parameters
    ----------
    X : list (float)
        List of data points.
    Y : list (float)
        List of observations

    Returns
    -------
    m, c, msg : float, float, int, String
        The slope and y-intercept of the straight line with the error string.
    """

    # initialize the values
    n = len(X)                  # number of observations
    points = list(zip(X, Y))    # observation points

    # calculate summations
    sum_x = sum(X)
    sum_y = sum(Y)
    sum_x_x = sum(list(map(lambda var: var[0]*var[0], points)))
    sum_x_y = sum(list(map(lambda var: var[0]*var[1], points)))

    # calculate slope
    m = (n * sum_x_y - sum_x * sum_y) / (n * sum_x_x - sum_x * sum_x)
    # calculate y-intercept
    c = (sum_y - m * sum_x) / n

    return m, c, None