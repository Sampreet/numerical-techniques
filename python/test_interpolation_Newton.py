from interpolation import Newton

# given data-points and observations
X = [1.2, 1.3, 1.4, 1.5]
Y = [1.063, 1.091, 1.119, 1.145]
x = 1.35

# find interpolated value using Newton Interpolation
B, y, msg = Newton.find_value_with_degree_3(X, Y, x)
if y != None:
    print("Newton Interpolation Method:\n\tCoefficients: {B}\n\tValue: {y}".format(B=B, y=y))
else:
    print("Newton Interpolation Method:\n\tCould not interpolate value.\n\t{msg}".format(msg=msg))