from modules import GaussianElimination
import math

# coefficient matrix and constant vector given by A*x = b
A = [[4, 0, 2, 1], [3, 2, 2, 0], [2, 1, 1, 2], [1, 3, 2, 0]]
b = [3, -1, 2, -4]

# find root using Gaussian Elimination Method
x, ops, msg = GaussianElimination.solve_using_upper_triangle(A, b)
if x != None:
    print("Gaussian Elimination Method:\n\tRoot: {x}\n\tOperations: {ops}".format(x=x, ops=ops))
else:
    print("Gaussian Elimination Method:\n\tNo root found with given initial value.\n\t{msg}\n\tOperations: {ops}".format(msg=msg, ops=ops))