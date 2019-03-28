from modules import Bisection
from decimal import Decimal

xi = 0.5        # initial value
xf = 2          # final value
step = 1e0      # step-size of bracket
xmax = 1e3      # maximum x-value
err = 1e-6      # relative error threshold
def fn(x):   
    """
    Given function.
    """
    return Decimal(x)**3 + 94*Decimal(x)**2 - 389*Decimal(x) + 294

# find root in a given bracket using Bisection Method
root, ic, msg = Bisection.find_root_in_bracket(fn, xi, xf, err)
if root != None:
    print("Bisection Method:\n\tRoot in bracket [{xi}, {xf}]: {x0}\n\tFunction Value: {fx0}\n\tIterations: {ic}".format(xi=xi, xf=xf, x0=root, fx0=fn(root), ic=ic))
else:
    print("Bisection Method:\n\tNo root found with given initial values.\n\t", msg)

# find all roots using Bisection Method
roots, ic, msg = Bisection.find_all_roots(fn, step, xmax, err)
if len(roots) != 0:
    print("Bisection Method:\n\tAll Roots: {x0}\n\tIterations: {ic}".format(x0=roots, ic=ic))
else:
    print("Bisection Method:\n\tNo root found with given initial values.\n\t", msg)