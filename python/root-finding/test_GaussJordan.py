from modules import GaussJordan
import math

# given matrix
A = [[4, 1, 0], [5, -2, 4], [-2, 1, 1]]

# find root using Gauss Jordan Method
Ainv, ops, msg = GaussJordan.find_inverse(A)
if Ainv != None:
    print("Gauss Jordan Method:\n\tInverse: {Ainv}\n\tOperations: {ops}".format(Ainv=Ainv, ops=ops))
else:
    print("Gauss Jordan Method:\n\tNo inverse exist.\n\t{msg}\n\tOperations: {ops}".format(msg=msg, ops=ops))