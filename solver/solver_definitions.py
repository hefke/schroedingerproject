"""
This module contains all function to solve the schroedinger equation
"""
import numpy as np
import scipy as sp
from scipy import interpolate


def read_inp(filename):
    """
    Reads all information from the input file and saves them as variables

    Args:
        filename: Name of the input file containing the specification of the problem

    Returns:
        x_min: minimal x-value
        x_max: maximal x-value
        n_point: number of points between x_min and x_max
        ev_first: first eigenvalue to be printed
        ev_last: last eigenvalue to be printed
        interp_type: type of interpolation
        potential_decl: array of points defining the potnetial
        alpha: constant used fpr the calculation of eigenvalues
    """

    data = []
    lines = open(filename, "r").readlines()
    for line in lines:
        line = line.partition("#")[0]
        line = line.strip()
        data.append(line.split())
    data = np.array(data)
    mass = float(data[0][0])
    x_min = float(data[1][0])
    x_max = float(data[1][1])
    n_point = int(data[1][2])
    ev_first = int(data[2][0])
    ev_last = int(data[2][1])
    interp_type = str(data[3][0])
    interp_number = int(data[4][0])
    potential_decl = np.zeros([interp_number, 2])
    for ii in range(interp_number):
        potential_decl[ii] = potential_decl[ii]+np.asarray(data[ii+5], dtype=float)
    alpha = 1/(mass*(((x_max-x_min)/n_point)**2))

    return x_min, x_max, n_point, ev_first, ev_last, interp_type, potential_decl, alpha


def potential_discret(x_min, x_max, n_point, interp_type, potential_decl):
    """
    discretises the potential by using linear/cubic/polynomial interpolation and saves the results
    into a file potential.dat

    Args:
        x_min: minimal x-value
        x_max: maximal x-value
        n_point: number of points between x_min and x_max
        interp_type: type of interpolation
        potential_decl: array of points defining the potnetial

    Returns:
        potential_dat: array of the x_values in the first column
        and the y-values of the potential in the second column
    """
    x_values = np.linspace(x_min, x_max, n_point)
    if interp_type == "linear":
        potential = np.interp(x_values, potential_decl[:, 0], potential_decl[:, 1])
    elif interp_type == "polynomial":
        potential = interpolate.barycentric_interpolate(potential_decl[:, 0],
                                                        potential_decl[:, 1], x_values)
    elif interp_type == "cspline":
        potential = interpolate.CubicSpline(potential_decl[:, 0],
                                            potential_decl[:, 1], bc_type="natural")(x_values)
    potential_dat = np.array(list(zip(x_values, potential)))
    np.savetxt("potential.dat", potential_dat)
    return potential_dat

def solve_wavefuncs(n_point, ev_first, ev_last, potential_dat, alpha):
    """
    Calculates the wavefunctions and energies by expressing the Hamilton-Operator as
    Matrix and solving its eigenvalue problem and saving eingenvalues and
    eigenfunctions in the files energies.dat and wavefuncs.dat

    Args:
        n_point: number of points between x_min and x_max
        mass: mass of the particle
        x_min: minimal x-value
        x_max: maximal x-value
        ev_first: first eigenvalue to be printed
        ev_last: last eigenvalue to be printed

    Returns:
        eigenvektors: calculated eigenvektros representing the energies
        eigenvalues: calculated eigenvalues of the problem
    """
    potential = potential_dat[:, 1:]
    main_diag = potential+np.ones(n_point)*alpha
    side_diag = np.ones(n_point-1)*alpha/2
    matrix = np.diag(main_diag)-np.diag(side_diag, 1)+np.diag(side_diag, -1)
    eigenvalues, eigenvektors = sp.linalg.eigh(matrix, eigvals=(ev_first-1, ev_last-1))

    wafefuncs_dat = np.zeros((n_point, ev_last+1))
    wafefuncs_dat[:, 0] = potential_dat[:, 0]
    wafefuncs_dat[:, 1:] = eigenvektors
    np.savetxt("energies.dat", eigenvalues)
    np.savetxt("wavefuncs.dat", wafefuncs_dat)
    return eigenvektors, eigenvalues

def solve_expvalues(ev_first, ev_last, potential_dat, eigenvektors):
    """
    Calculates the expectation values of the x-variable and the postition
    blur and saves them into the file expvalues.dat.

    Args:
        ev_first: first eigenvalue to be printed
        ev_last: last eigenvalue to be printed
        potential_dat: array of the potential-coordinates
        eigenvektors: eigenvektros representing the energies of the potential
    """
    x_values = potential_dat[:, 0]
    number_ev = ev_last-ev_first
    expvalues_x = np.zeros(number_ev+1)
    expvalues_x_square = np.zeros(number_ev+1)
    position_blur = np.zeros(number_ev+1)

    for jj in range(number_ev+1):
        expvalues_x[jj] = np.sum((x_values*eigenvektors[:, jj]**2))
        expvalues_x_square[jj] = np.sum((x_values**2*eigenvektors[:, jj]**2))
        position_blur[jj] = (expvalues_x_square[jj]-expvalues_x[jj]**2)**(0.5)
    expvalues_dat = np.zeros((number_ev+1, 2))
    expvalues_dat[:, 0] = expvalues_x
    expvalues_dat[:, 1] = position_blur
    np.savetxt("expvalues.dat", expvalues_dat)
