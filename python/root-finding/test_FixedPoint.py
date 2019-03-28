from modules import FixedPoint
from decimal import Decimal 

xi = 1          # initial value
err = 1e-6      # relative error threshold
imax = 1e6      # maximum number of iterations to consider
def g(x):       
    """
    Modified function for the demo function f(x) = x^2 - 5
    """
    return 2 + 1 / (Decimal(x) + 2)

# find root using Fixed Point Method
root, ic, msg = FixedPoint.find_root_uni(g, xi, err, imax)
if root != None:
    print("Fixed Point Method:\n\tRoot: {x0}\n\tFunction Value: {fx0}\n\tIterations: {ic}".format(x0=root, fx0=g(root) - Decimal(root), ic=ic))
else:
    print("Fixed Point Method:\n\tNo root found.\n\t{msg}\n\tIterations: {ic}".format(ic=ic, msg=msg))