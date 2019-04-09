from modules import LUDecomposition

# given matrix
A = [[2, 4, -6], [1, 3, 1], [2, -4, -2]]
# given constants
b = [-8, 10, -12]

# find root using LU Decomposition Method
root, ops, msg = LUDecomposition.solve_with_ones_in_L(A, b)
if root != None:
    print("LU Decomposition Method:\n\tRoot: {root}\n\tOperations: {ops}".format(root=root, ops=ops))
else:
    print("LU Decomposition Method:\n\tNo roots exist.\n\t{emsg}\n\tOperations: {ops}".format(msg=msg, ops=ops))