"""
A collection of techniques to find eigenfunctions of the Harmonic Oscillator model using scipy.integrate.odeint.
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

def get_solutions(range_x, range_psi_0, range_dpsidx_0, range_eps, step_size_x=1e-2, step_size_psi_0=1, step_size_dpsidx_0=1, step_size_eps=1e-2, margin_zero=1e-2, display=False, debug=True):
    '''
    Main function to get the solutions of the Harmonic Oscillator model for the given parameters

    Parameters
    ----------
    range_x : float
        Range of the x-axis 
    range_psi_0 : float
        Range of the initial value psi(0)
    range_dpsidx_0 : float
        Range of the initial value psi'(0)
    range_eps : float
        Range of the dimensionless energy
    step_size_x : float (optional)
        Precision of the x-axis (default is 1e-2)
    step_size_psi_0 : float (optional)
        Step size for iteration of the initial value psi(0) (default is 1)
    step_size_dpsidx_0 : float (optional)
        Step size for iteration of the initial value psi'(0) (default is 1)
    step_size_eps : float (optional)
        Step size for iteration of the dimensionless energy (default is 1e-2)
    margin_zero : float (optional)
        Margin of error to consider while checking the zero of the wavefunction (default is 1e-2)
    display : boolean (optional)
        Option to display the plots during iteration (default is False)
    debug : boolean (optional)
        Option to debug the iteration process (default is True)

    Returns
    -------
    sol : array (array (float))
        Array containing the solution arrays with elements as psi(0), psi'(0) and epsilon values
    '''

    if display:
        plt.show()
        axes = plt.gca()
        axes.set_xlim(-1* range_x, range_x)
        axes.set_ylim(-2, 2)
        line, = axes.plot([], [], 'r-')
        plt.xlabel("x")
        plt.ylabel("psi")
        plt.title("Harmonic Oscillator")

    # initialize variables
    sol = []
    ops = 0

    if debug:
        print("Starting iterations...")

    for i in range(0, int(range_psi_0/step_size_psi_0) + 1):
        psi_0 = i * step_size_psi_0
        for j in range(0, int(range_dpsidx_0/step_size_dpsidx_0) + 1):
            dpsidx_0 = j * step_size_dpsidx_0
            if (psi_0 == 0 and dpsidx_0 == 0):
                continue
            for k in range(0, int(range_eps/step_size_eps) + 1):
                eps = k * step_size_eps
                # update iteration number
                ops += 1
                # prepare the vector for scipy.integrate.odeint
                U_0 = [psi_0, dpsidx_0]
                # get solution using scipy.integrate.odeint
                X, Y = get_ODE_solution(range_x, step_size_x, U_0, eps)
                # if the ends of the obtained solution are close to zero, accept it as a solution of the Harmonic Oscillator
                if (abs(Y[-1]) < margin_zero and abs(Y[0]) < margin_zero):
                    sol.append([psi_0, dpsidx_0, eps])

                if display:
                    line.set_xdata(X)
                    line.set_ydata(Y)
                    plt.suptitle("psi(0) = {psi_0} (d/dx)psi(0)={dpsidx_0} epsilon={eps}".format(psi_0=psi_0, dpsidx_0=dpsidx_0, eps=eps))
                    plt.draw()
                    plt.pause(1e-6)

                if debug:
                    print("\rIteration #{ops}:\tpsi(0) = {psi_0}\t(d/dx)psi(0)={dpsidx_0}\tepsilon={eps}".format(ops=ops, psi_0=psi_0, dpsidx_0=dpsidx_0, eps=eps), end="")

    if debug:
        print("\r....................................................................................................")
        print("{ops} iterations completed. {num} solutions obtained.".format(ops=ops, num=len(sol)))
    return sol

def display_solutions(sol, range_x, step_size_x=1e-2, debug=True):
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
    debug : boolean (optional)
        Option to debug the plotting process (default is True)
    '''

    if debug:
        print("Plotting solutions...")
        print("\tGraph #\t|\tpsi(0)\t|(d/dx)psi(0)\t|\tepsilon")

    for i in range(0, len(sol)):
        if debug:
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

    if debug:
        print("{num} graphs plotted.".format(num=len(sol)))