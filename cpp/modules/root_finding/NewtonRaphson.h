// Authors: Sampreet Kalita
// Created: 2020-01-12
// Updated: 2020-01-12

/* Module to find roots of a function using Newton-Raphson Method. */
 
#ifndef _NEWTONRAPHSON_H_
#define _NEWTONRAPHSON_H_

class NewtonRaphson
{
    public:
        // constants
        static const int NO_CONFIRMED_ROOT;
        static const int FOUND_ROOT;
        static const int FOUND_APPROX_ROOT;
        static const int MAX_ITER_REACHED;
        static const int DERIVATIVE_ZERO;
        
        // functions                    
        int find_root_uni(double (*fn)(double), double (*df)(double), double xi, double et, int imax, double *root, int *ic);
}; // NewtonRaphson

#endif // _NEWTONRAPHSON_H_