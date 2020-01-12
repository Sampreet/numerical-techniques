// Authors: Sampreet Kalita
// Created: 2020-01-12
// Updated: 2020-01-12

/* Example code to use  root_finding -> NewtonRaphson module. */

// dependencies
#include <cmath>
#include <iostream>

#include "..\..\modules\root_finding\NewtonRaphson.h"

// namespace
using namespace std;

/** 
 * Demo univariate function for testing.
 * f(x) = - D/x^2 - A/B*e^(-x/B) + 6*C/x^7
 * 
 * @param[in]   x
 *                  Value of the variable.
 * 
 * @return      fx
 *                  Value of the function at x.
 */
double fn(double x) {
    // coefficients
    double  A = 728.0, 
            B = 0.317, 
            C = 0.486, 
            D = -8.99 * 1.6;

    // function
    double fx = - D / pow(x, 2) - A / B * exp(- x / B) + 6 * C / pow(x, 7);

    return fx;
}

/** 
 * Derivative of the demo univariate function.
 * df(x)/dx = 2*D/x^3 + A/B^2*e^(-x/B) - 42*C/x^8
 * 
 * @param[in]   x
 *                  Value of the variable.
 * 
 * @return      fx
 *                  Value of the function at x.
 */
double df(double x) {
    // coefficients
    double  A = 728.0, 
            B = 0.317, 
            C = 0.486, 
            D = -8.99 * 1.6;

    // function
    double dfx = 2*D / pow(x, 3) + A / pow(B, 2) * exp(- x / B) - 42 * C / pow(x, 8);

    return dfx;
}

// main program
int main() {
    cout << "Newton-Raphson Method: Univariate" << endl;

    // input
    double xi = 1;      // initial value
    double et = 1e-3;   // relative error threshold
    int imax = 1e6;     // maximum number of iterations to consider

    // method class
    NewtonRaphson mod;

    // output
    double root;
    int ic;
    int status = mod.find_root_uni(fn, df, xi, et, imax, &root, &ic);

    // display
    if (status == mod.FOUND_ROOT || status == mod.FOUND_APPROX_ROOT) {
        cout << "\tInitial value: " << xi << endl;
        cout << "\tRoot: " << root << endl;
        cout << "\tFunction value: " << fn(root) << endl;
        cout << "\tIterations: " << ic << endl;
    }
    else {
        if (status == mod.NO_CONFIRMED_ROOT) { 
            cout << "No confirmed root with initial value " << xi << endl;
        }
        if (status == mod.MAX_ITER_REACHED) { 
            cout << "Max. iterations reached with initial value " << xi << endl;
        }
        if (status == mod.DERIVATIVE_ZERO) { 
            cout << "Derivative function is zero with initial value " << xi << endl;
        }
    }
    return 0;
}