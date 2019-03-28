from modules import NewtonRaphson
from decimal import Decimal
import math

xi = 1          # initial value
err = 1e-6      # relative error threshold
imax = 1e6      # maximum number of iterations to consider
def fn(x):   
    """
    Given function.
    """
    return math.exp(Decimal(x)*2) - math.exp(Decimal(x)) - 2

def df(x): 
    """
    Derivative of given function.
    """
    return 2*math.exp(Decimal(x)*2) - math.exp(Decimal(x))

# find root in a given bracket using Newton-Raphson Method
root, ic, msg = NewtonRaphson.find_root_uni(fn, df, xi, err, imax)
if root != None:
    print("Newton-Raphson Method:\n\tRoot with initial value {xi}: {x0}\n\tFunction Value: {fx0}\n\tIterations: {ic}".format(xi=xi, x0=root, fx0=fn(root), ic=ic))
else:
    print("Newton-Raphson Method:\n\tNo root found with given initial value.\n\t{msg}\n\tIterations: {ic}".format(msg=msg, ic=ic))