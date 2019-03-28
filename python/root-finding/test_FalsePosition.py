from modules import FalsePosition
from decimal import Decimal
import math

xi = 0          # initial value
xf = 1          # final value
step = 1e0      # step-size of bracket
xmax = 1e2      # maximum x-value
err = 1e-6      # relative error threshold
def fn(x):   
    """
    Given function.
    """
    return math.exp(Decimal(x)*2) - math.exp(Decimal(x)) - 2

# find root in a given bracket using False Position Method
root, ic, msg = FalsePosition.find_root_in_bracket(fn, xi, xf, err)
if root != None:
    print("False Position Method:\n\tRoot in bracket [{xi}, {xf}]: {x0}\n\tFunction Value: {fx0}\n\tIterations: {ic}".format(xi=xi, xf=xf, x0=root, fx0=fn(root), ic=ic))
else:
    print("False Position Method:\n\tNo root found with given initial values.\n\t", msg)

# find all roots using False Position Method
roots, ic, msg = FalsePosition.find_all_roots(fn, step, xmax, err)
if len(roots) != 0:
    print("False Position Method:\n\tAll Roots: {x0}\n\tIterations: {ic}".format(x0=roots, ic=ic))
else:
    print("False Position Method:\n\tNo root found with given initial values.\n\t", msg)