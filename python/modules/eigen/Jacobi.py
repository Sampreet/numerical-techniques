#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2020-02-13
# Updated: 2020-02-17

"""Module to obtain eigenvalues and eigenvectors using Jacobi's Method."""

# dependencies
import math

def get_mat_product(A, B):
    """
    Function to obtain the product (C) of two matrices (A*B).

    Parameters
    ----------
    A : list
        First matrix.
    B : list
        Second matrix.

    Returns
    -------
    C : list
        Product matrix.
    """

    # check compatibility
    if len(A[0]) != len(B):
        return None

    # multiply matrices
    C = []
    for i in range(len(A)):
        temp_row = []
        for j in range(len(B[0])):
            # element-wise multiplication
            temp_ele = 0
            for k in range(len(A[0])):
                temp_ele += A[i][k]*B[k][j]
            temp_row.append(temp_ele)
        C.append(temp_row)
    
    # return product matrix
    return C


def get_eigens(A, et=1e-6, imax=1e6, debug=True):
    """
    Obtain the eigenvalues and eigenvectors of a symmetric matrix A using Jacobi's Method.

    Parameters
    ----------
    A : list
        Given symmetric matrix.
    et : float (optional)
        Threshold of relative error.
    imax : int (optional)
        Maximum number of iterations to consider.
    debug : boolean
        Option to display steps.

    Returns
    -------
    eig_val, eig_vec, ic, msg : float, int, String
        The eigenvalues and the eigenvectors and the iteration count with status string.
    """

    # initialize values
    dim = len(A)                        # dimension of the eigenvector
    ic = 0                              # iteration counter

    # display
    if debug:
        print("Input\n-------")
        print("Matrix A:\t{A}".format(A=A))

    # initial diagonal matrix
    D = [[A[i][j] for j in range(dim)] for i in range(dim)]
    # initial rotation matrix
    R = [[1 if i==j else 0 for j in range(dim)] for i in range(dim)]

    # iterate until error threshold or max number of iterations is reached
    while(True):
        # get indices of maximum off-diagonal element
        temp_max = D[0][1] if D[0][1] >= 0 else -D[0][1]
        p = 0
        q = 1
        for i in range(dim - 1):
            for j in range(i + 1, dim):
                temp_abso = D[i][j] if D[i][j] > 0 else -D[i][j]
                if temp_abso > temp_max:
                    temp_max = temp_abso
                    p = i
                    q = j

        if temp_max < et or ic >= imax:
            break 

        # start iteration
        ic += 1
        if debug:
            print('\nIteration #\t{}\n-----------'.format(ic))
            
        # form currrent rotation matrix
        theta = math.pi/4
        if D[q][q] != D[p][p]:
            ratio = 2*D[p][q]/(D[q][q] - D[p][p])
            theta = 0.5*math.atan(ratio)
        c = math.cos(theta)
        s = math.sin(theta)
        temp_R = [[1 if i==j else 0 for j in range(dim)] for i in range(dim)]
        temp_R[p][p] = c
        temp_R[p][q] = s
        temp_R[q][p] = -s
        temp_R[q][q] = c
        
        # total rotation matrix
        R = get_mat_product(temp_R, R)

        # form current diagonal matrix
        temp_D = [[D[i][j] for j in range(dim)] for i in range(dim)]
        temp_D[p][q] = 0
        temp_D[q][p] = 0
        temp_D[p][p] = c**2*D[p][p] + s**2*D[q][q] - 2*c*s*D[p][q]
        temp_D[q][q] = s**2*D[p][p] + c**2*D[q][q] + 2*c*s*D[p][q]
        for j in range(dim):
            if j != p and j != q:
                temp_D[j][p] = c*D[j][p] - s*D[j][q]
                temp_D[p][j] = temp_D[j][p]
                temp_D[j][q] = c*D[j][q] + s*D[j][p]
                temp_D[q][j] = temp_D[j][q]
        
        # update diagonal matrix
        D = [[temp_D[i][j] for j in range(dim)] for i in range(dim)]
        
        if debug:
            print('Matrix R: {}'.format(R))
            print('Matrix D: {}'.format(D))
            
    # eigenvalues and eigenvectors
    eig_val = [D[i][i] for i in range(dim)]
    eig_vec = [[R[j][i] for j in range(dim)] for i in range(dim)]

    return eig_val, eig_vec, ic, 'Eigenvalues and eigenvectors obtained'
                    



            
