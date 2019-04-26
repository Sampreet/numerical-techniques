"""
HarmonicOscillator1D
====================
Created on 2019-04-13 by Sampreet Kalita

Functionality
-------------
A collection of functions to find solutions of the 1-D Harmonic Oscillator model using scipy.integrate.odeint.
Generates solutions for different values of the dimension-less energy in a given range of x.

Code Improvements
-----------------
Update #4 (2019-04-26): Changed to derivative-based adaptation instead of value-based. Minor fixes.

Update #3 (2019-04-23): Implemented 'adaptive' wag-the-dog by increasing precision and implementing directionality. Removed 'for' loops for psi_0 and dpsidx_0.

Update #2 (2019-04-18): Alloted unit step-size for psi_0 and dpsidx_0.

Update #1 (2019-04-16): Separated get_solutions and display_solutions functions.
"""

__all__ = ["get_solutions", "display_solutions"]

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def model(U, x, eps):
    '''
    The Dimensionless Harmonic Oscillator model for the Schrodinger Equation - (d/dx)((d/dx)psi) = (x^2 - epsilon)psi

    Parameters
    ----------
    U : array
        Array containing the initial values - psi(0) and psi'(0)
    x : float
        Dimensionless position
    eps : float
        Dimensionless energy

    Returns
    -------
    model : array
        The array containing psi'(0) and it's representation
    '''

    return [U[1], ((x * x) - eps) * U[0]]

def get_ODE_solution(range_x, step_size_x, U_0, eps):
    '''
    Helper function to get the solution of an ODE

    Parameters
    ----------
    range_x : float
        Range of the x-axis
    step_size_x : float
        Precision of the x-axis
    U_0 : array
        Array containing the initial values - psi(0) and psi'(0)
    eps : float
        Dimensionless energy to pass into the model function

    Returns
    -------
    X, Y : np.array (float), np.array (float)
        Arrays containing the x and psi(x) values
    '''

    # positive x-axis
    X_pos = np.linspace(0, range_x, int(range_x/step_size_x))
    U_pos = odeint(model, U_0, X_pos, (eps,))
    # negative x-axis
    X_neg = np.linspace(0, -1 * range_x, int(range_x/step_size_x))
    U_neg = odeint(model, U_0, X_neg, (eps,))
    # reverse negative values and catenate
    X = np.concatenate((np.flip(X_neg), X_pos))
    Y = np.concatenate((np.flip(U_neg[:, 0]), U_pos[:, 0]))

    return X, Y

def get_solutions(eps_min, eps_max, step_size_eps_ini=1e-2, step_size_eps_max=1e-6, threshold_eps=1, threshold_zero=1e-4, range_x=5, step_size_x=1e-2, display=False, debug=False):
    '''
    Main function to get the solutions of the Harmonic Oscillator model for the given parameters

    Parameters
    ----------
    eps_min : float
        Starting value of the dimensionless energy, epsilon
    eps_max : float
        Ending value of epsilon
    step_size_eps_ini : float (optional)
        Initial step-size for iteration of epsilon (default is 1e-2)
    step_size_eps_max : float (optional)
        Maximum step-size for iteration of epsilon (default is 1e-6)
    threshold_eps : float (optional)
        Threshold to decrease step-size of epsilon (default is 1)
    threshold_zero : float (optional)
        Threshold to consider a zero of the wavefunction (default is 1e-2)
    range_x : float (optional)
        Range of the x-axis (default is 5)
    step_size_x : float (optional)
        Precision of the x-axis (default is 1e-2)
    display : boolean (optional)
        Option to display the plots during iteration (default is False)
    debug : boolean (optional)
        Option to debug the iteration process (default is False)

    Returns
    -------
    sol : array (array (float))
        Array containing the solution arrays with elements as psi(0), psi'(0) and epsilon values
    '''

    if display:
        # initialize the figure
        plt.show()
        axes = plt.gca()
        axes.set_xlim(-1* range_x, range_x)
        axes.set_ylim(-2, 2)
        line, = axes.plot([], [], 'r-')
        plt.xlabel("x")
        plt.ylabel("psi")
        plt.title("Harmonic Oscillator")

    # initialize variables
    sol = []    # solution array
    ops = 0     # iteration count

    print("Starting iterations...")

    for i in range(0, 2):
        psi_0 = i 
        dpsidx_0 = (psi_0 + 1) % 2
        for j in range(0, int((eps_max - eps_min)/step_size_eps_ini) + 1):
            eps = eps_min + j * step_size_eps_ini
            # prepare the vector for scipy.integrate.odeint
            U_0 = [psi_0, dpsidx_0]
            # get solution using scipy.integrate.odeint
            X, Y = get_ODE_solution(range_x, step_size_x, U_0, eps)
            
            # if the end values are both near the threshold for change of step size
            if (abs(Y[-1]) < threshold_eps and abs(Y[0]) < threshold_eps):
                # initialize multiplier to decrease step size
                multiplier = 1e-1
                temp_ops = 0
                temp_eps = eps
                # keep track of previous derivative near the tail
                dydx_prev = (abs(Y[0]) - abs(Y[1]))/abs(X[0]-X[1])
                # while step size is more than maximum step size for epsilon
                while (temp_eps < eps + step_size_eps_ini and abs(multiplier*step_size_eps_ini) >= step_size_eps_max):
                    # update iteration count
                    temp_ops += 1
                    # get solution using scipy.integrate.odeint
                    X, Y = get_ODE_solution(range_x, step_size_x, U_0, temp_eps)

                    if debug:
                        print("\rDebug: Iteration #{ops}:\tpsi(0) = {psi_0}\t(d/dx)psi(0) = {dpsidx_0}\tepsilon = {eps}\tpsi({range_x}) = {psi_x}".format(ops=ops + temp_ops, psi_0=psi_0, dpsidx_0=dpsidx_0, eps=temp_eps, range_x=range_x, psi_x=Y[0]), end="\t\t\t\n")

                    # if the ends of the obtained solution are close to zero, accept it as a solution of the Harmonic Oscillator
                    if (abs(Y[-1]) < threshold_zero and abs(Y[0]) < threshold_zero):

                        if debug:
                            print("\rDebug: Solution: \tpsi(0) = {psi_0}\t(d/dx)psi(0) = {dpsidx_0}\tepsilon = {eps}\tpsi({range_x}) = {psi_x}".format(psi_0=psi_0, dpsidx_0=dpsidx_0, eps=temp_eps, range_x=range_x, psi_x=Y[0]), end="\t\t\t\n")

                        # update the array
                        sol.append([psi_0, dpsidx_0, temp_eps])
                        break

                    if display:
                        # update the figure
                        line.set_xdata(X)
                        line.set_ydata(Y)
                        plt.suptitle("psi(0) = {psi_0} (d/dx)psi(0)={dpsidx_0} epsilon={eps}".format(psi_0=psi_0, dpsidx_0=dpsidx_0, eps=temp_eps))
                        plt.draw()
                        plt.pause(1e-6)

                    print("\rIteration #{ops}:\tpsi(0) = {psi_0}\t(d/dx)psi(0) = {dpsidx_0}\tepsilon = {eps}".format(ops=ops + temp_ops, psi_0=psi_0, dpsidx_0=dpsidx_0, eps=temp_eps), end="\t\t\t")

                    # calculate the current derivative at the tail
                    dydx_curr = (abs(Y[0]) - abs(Y[1]))/abs(X[0]-X[1])
                    # if current derivative is more than previous, increase precision and reverse iteration direction
                    if dydx_prev < dydx_curr:
                        if temp_ops != 2:
                            multiplier *= 1e-1
                        multiplier *= -1
                    # update values
                    temp_eps += multiplier * step_size_eps_ini
                    dydx_prev = dydx_curr

                    if debug and not (temp_eps < eps + step_size_eps_ini and abs(multiplier) > 1e-6):
                        print("\rDebug: Maximum iterations completed for epsilon = {}.".format(eps), end="\t\t\t\n")
                # update iteration count
                ops += temp_ops
            else:
                # update iteration count
                ops += 1

                if display:
                    # update the figure
                    line.set_xdata(X)
                    line.set_ydata(Y)
                    plt.suptitle("psi(0) = {psi_0} (d/dx)psi(0)={dpsidx_0} epsilon={eps}".format(psi_0=psi_0, dpsidx_0=dpsidx_0, eps=eps))
                    plt.draw()
                    plt.pause(1e-6)

                print("\rIteration #{ops}:\tpsi(0) = {psi_0}\t(d/dx)psi(0) = {dpsidx_0}\tepsilon = {eps}".format(ops=ops, psi_0=psi_0, dpsidx_0=dpsidx_0, eps=eps), end="\t\t\t")

    print("\r....................................................................................................")
    print("{ops} iterations completed. {num} solutions obtained.".format(ops=ops, num=len(sol)))
    plt.close()
    return sol

def display_solutions(sol, range_x, step_size_x=1e-2):
    '''
    Helper function to display the solutions obtained using the main function

    Parameters
    ----------
    sol : array (array (float))
        Array containing the solution arrays with elements as psi(0), psi'(0) and epsilon values
    range_x : float
        Range of the x-axis 
    step_size_x : float (optional)
        Precision of the x-axis (default is 1e-2)
    '''

    print("Plotting solutions...")
    print("\tGraph #\t|\tpsi(0)\t|(d/dx)psi(0)\t|\tepsilon")

    for i in range(0, len(sol)):
        print("\t{num}\t|\t{psi_0}\t|\t{dpsidx_0}\t|\t{eps}".format(num=i+1, psi_0=sol[i][0], dpsidx_0=sol[i][1], eps=sol[i][2]))
        eps = sol[i][2]
        # prepare the vector for scipy.integrate.odeint
        U_0 = [sol[i][0], sol[i][1]]
        # get solution using scipy.integrate.odeint
        X, Y = get_ODE_solution(range_x, step_size_x, U_0, eps)
        # plot solution
        plt.xlabel("x")
        plt.ylabel("psi")
        plt.title("Harmonic Oscillator")
        plt.suptitle("psi(0) = {} (d/dx)psi(0) = {} epsilon = {}".format(sol[i][0], sol[i][1], sol[i][2]))
        plt.plot(X, Y)
        plt.show()

    print("{num} graphs plotted.".format(num=len(sol)))