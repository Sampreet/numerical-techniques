from modules import Secant
import math

xi = 1          # initial value
xf = 3          # initial value
err = 1e-6      # relative error threshold
imax = 1e6      # maximum number of iterations to consider
def fn(x):   
    """
    Given function.
    """
    return math.exp(x*2) - math.exp(x) - 2

def df(x): 
    """
    Derivative of given function.
    """
    return 2*math.exp(x*2) - math.exp(x)

# find root using Secant Method
root, ic, msg = Secant.find_root_uni(fn, xi, xf, err, imax)
if root != None:
    print("Secant Method:\n\tRoot with initial value {xi}: {x0}\n\tFunction Value: {fx0}\n\tIterations: {ic}".format(xi=xi, x0=root, fx0=fn(root), ic=ic))
else:
    print("Secant Method:\n\tNo root found with given initial values.\n\t{msg}\n\tIterations: {ic}".format(msg=msg, ic=ic))