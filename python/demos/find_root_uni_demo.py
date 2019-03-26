import sys
sys.path.append(".")
from modules import find_root_uni as rfu
import math 

xi = 0          # initial value
xf = 1          # final value
et = 1e-6       # error threshold
mi = 1e6        # iteration threshold
def f1(x):      # demo function 1
    return math.exp(2*x) - math.exp(x) - 2
def df1(x):     # demo derivative 1
    return 2*math.exp(2*x) - math.exp(x)

# find root using Bisection Method
root, ic = rfu.bisection(f1, xi, xf, et)
if root != None:
    print("Bisection Method:\n\tRoot: {x0}\n\tFunction Value: {fx0}\n\tIterations: {ic}".format(x0=root, fx0=f1(root), ic=ic))
else:
    print("Bisection Method:\nNo root found in the given interval.\n")

# find root using False Position Method
root, ic = rfu.false_position(f1, xi, xf, et)
if root != None:
    print("False Position Method:\n\tRoot: {x0}\n\tFunction Value: {fx0}\n\tIterations: {ic}".format(x0=root, fx0=f1(root), ic=ic))
else:
    print("False Position Method:\tNo root found in the given interval.")

# find root using Newton-Raphson Method
root, ic = rfu.newton_raphson(f1, df1, xi, et, mi)
if root != None:
    print("Newton-Raphson Method:\n\tRoot: {x0}\n\tFunction Value: {fx0}\n\tIterations: {ic}".format(x0=root, fx0=f1(root), ic=ic))
else:
    print("Newton-Raphson Method:\tNo root found.\n\tIterations: {ic}".format(ic=ic))

# find root using Secant Method
root, ic = rfu.secant(f1, xi, xf, et, mi)
if root != None:
    print("Secant Method:\n\tRoot: {x0}\n\tFunction Value: {fx0}\n\tIterations: {ic}".format(x0=root, fx0=f1(root), ic=ic))
else:
    print("Secant Method:\tNo root found.\n\tIterations: {ic}".format(ic=ic))