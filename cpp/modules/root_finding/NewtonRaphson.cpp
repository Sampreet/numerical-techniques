// Authors: Sampreet Kalita
// Created: 2020-01-12
// Updated: 2020-01-12

/* Module to find roots of a function using Newton-Raphson Method. */

// dependencies
#include <cmath>

#include "NewtonRaphson.h"

// public constants
const int NewtonRaphson::NO_CONFIRMED_ROOT  = 0;
const int NewtonRaphson::FOUND_ROOT         = 1;
const int NewtonRaphson::FOUND_APPROX_ROOT  = 2;
const int NewtonRaphson::MAX_ITER_REACHED   = 3;
const int NewtonRaphson::DERIVATIVE_ZERO    = 4;

/*
 * Find the (approximate) root of a univariate function
 * using the Newton-Raphson Method.
 *  
 * @param[in]   fn  
 *                  Given function in x.
 * @param[in]   df 
 *                  Derivative of the function in x.
 * @param[in]   xi  
 *                  Initial x-value of the selected bracket.
 * @param[in]   et  
 *                  Relative error threshold.
 * @param[in]   imax
 *                  Maximum number of iterations to consider.
 * 
 * @return      status
 *                  Status of the root:
 *                      0:  No confirmed root.
 *                      1:  Found root.
 *                      2:  Found approx. root.
 *                      3:  Max. iterations reached.
 *                      4:  Derivative function is zero.
 */
int NewtonRaphson::find_root_uni(double (*fn)(double), double (*df)(double), double xi, double et, int imax, double *root, int *ic) {
    // variables
    double xint, curr_diff, max_diff;

    // initialize values
    *ic = 0;

    // check initial values
    if ((*fn)(xi) == 0) {
        *root = xi;
        return FOUND_ROOT;
    }

    // iterate till maximum iterations is reached or
    // relative error reaches threshold
    while (true) {
        // increment counter
        *ic = *ic + 1;

        // check iteration threshold
        if (*ic >= imax) {
            return MAX_ITER_REACHED;
        }

        // no root if derivative is zero
        if ((*df)(xi) == 0) {
            return DERIVATIVE_ZERO;
        }

        // get intersection point
        xint = xi - (*fn)(xi) / (*df)(xi);

        // check relative error
        curr_diff = std::abs(xint - xi);
        max_diff = std::abs(xi) * et;

        xi = xint;
        if (curr_diff < max_diff) {
            *root = xi;
            return FOUND_APPROX_ROOT;
        }
    
        // check value at xi
        if ((*fn)(xi) == 0) {
            *root = xi;
            return FOUND_ROOT;
        }
    }

    *root = xi;
    return FOUND_ROOT;
} //find_root_uni