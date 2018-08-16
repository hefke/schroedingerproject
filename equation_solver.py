# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import scipy as sp


def read_input(filename):
    """
    Reads all information from the input file and saves them as variables

    Args:
        filename: Name of the input file containing the specification of the problem

    Returns:
        mass: mass of the particle
        xMin: minimal x-value
        xMax: maximal x-value
        nPoint: number of points between xMin and xMax
        EV_first: first eigenvalue to be printed
        EV_last: last eigenvalue to be printed
        interpolation_type: type of interpolation
        interpolation_numbers: number of points defining the potential
        potential_declerations: array of points defining the potnetial
    """
    file = open(filename, "r")
    data = []
    lines = file.readlines()
    for line in lines:
        line=line.partition("#")[0]
        line=line.strip()
        data.append(line.split())
    file.close()
    data=np.array(data)
    mass = float(data[0][0])
    xMin = float(data[1][0])
    xMax = float(data[1][1])
    nPoint = int(data[1][2])
    EV_first = float(data[2][0])
    EV_last = float(data[2][1])
    interpolation_type = str(data[3][0])
    interpolation_numbers = int(data[4][0])
    potential_declerations=np.zeros([len(data)-5, 2])
    for ii in range(0, len(data)-5):
        potential_declerations[ii]=potential_declerations[ii]+np.asarray(data[ii+5], dtype=float)

    return mass, xMin, xMax, nPoint, EV_first, EV_last, interpolation_type, interpolation_numbers, potential_declerations


def potential_discret(xMin, xMax, nPoint, interpolation_type, potential_declerations):
    """
    discretises the potential by using linear/cubic/polynomial interpolation and saves the results into a file potential.dat 

    Args:
        xMin: minimal x-value
        xMax: maximal x-value
        nPoint: number of points between xMin and xMax
        interpolation_type: type of interpolation
        potential_declerations: array of points defining the potnetial

    """
    x_values=np.linspace(xMin, xMax, nPoint)
    if interpolation_type=="linear":
        y_values=np.interp(x_values, potential_declerations[:,0], potential_declerations[:,1])
    elif interpolation_type=="polynomial":
        y_values=sp.interpolate.barycentric_interpolate(potential_declerations[:,0], potential_declerations[:,1], x_values)
    elif interpolation_type=="cspline":
        y_values=sp.interpolate.CubicSpline(potential_declerations[:,0], potential_declerations[:,1])(x_values)
            
            
    potential_dat=np.array(list(zip(x_values, y_values)))
    np.savetxt("potential.dat", potential_dat)






















