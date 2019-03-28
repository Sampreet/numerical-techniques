from modules import NewtonRaphson
import math

xi = 1          # initial value
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

# find root in a given bracket using Newton-Raphson Method
root, ic, msg = NewtonRaphson.find_root_uni(fn, df, xi, err, imax)
if root != None:
    print("Newton-Raphson Method:\n\tRoot with initial value {xi}: {x0}\n\tFunction Value: {fx0}\n\tIterations: {ic}".format(xi=xi, x0=root, fx0=fn(root), ic=ic))
else:
    print("Newton-Raphson Method:\n\tNo root found with given initial value.\n\t{msg}\n\tIterations: {ic}".format(msg=msg, ic=ic))

def f(X):
    return (X[0])**3 - (X[1])**2 + 1

def g(X):
    return (X[0])**2 - 2*X[0] + X[1]**3 - 2

def dfdx(X):
    return 3*(X[0])**2

def dfdy(X):
    return (-2)*(X[1])

def dgdx(X):
    return 2*(X[0]) - 2

def dgdy(X):
    return 3*X[1]**2

xi = 1
yi = 1

# find root in a given bracket using Newton-Raphson Method
roots, ic, msg = NewtonRaphson.find_root_multi([f, g], [[dfdx,dfdy],[dgdx,dgdy]], [xi, yi], err=1e-6, imax=10)
if root != None:
    print("Newton-Raphson Method:\n\tRoot with initial value ({xi}, {yi}): {roots}\n\tFunction Value: ({f}, {g})\n\tIterations: {ic}".format(xi=xi, yi=yi, roots=roots, f=f(roots), g=g(roots), ic=ic))
else:
    print("Newton-Raphson Method:\n\tNo root found with given initial value.\n\t{msg}\n\tIterations: {ic}".format(msg=msg, ic=ic))