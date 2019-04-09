from modules import Linear

# given data-points and observations
X = [1.0, 3.0, 4.0, 6.0, 8.0, 9.0, 11.0]
Y = [1.0, 2.0, 4.0, 4.0, 5.0, 7.0, 8.0]

# find straight line using Linear Regression
m, c, msg = Linear.get_straight_line_from_data(X, Y)
if m != None:
    print("Linear Regression:\n\tSlope: {m}\n\tY-intercept: {c}".format(m=m, c=c))
else:
    print("Linear Regression:\n\tCould not fit straight line.\n\t{msg}".format(msg=msg))