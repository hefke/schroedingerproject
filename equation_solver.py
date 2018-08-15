# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def read_input(filename):
    """
    Solves a linear system of equations (Ax = b) by Gauss-elimination

    Args:
        filename: Name of the input file containing the specification of the problem

    Returns:
        mass: mass of the 
        xMin
        xMax
        nPoint
        EV_first
        EV_last
        interpolation_type
        interpolation_numbers
        potential_declerations
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
    nPoint = float(data[1][2])
    EV_first = float(data[2][0])
    EV_last = float(data[2][1])
    interpolation_type = str(data[3][0])
    interpolation_numbers = float(data[4][0])
    potential_declerations=np.zeros([len(data)-5, 2])
    for ii in range(0, len(data)-5):
        potential_declerations[ii]=potential_declerations[ii]+np.asarray(data[ii+5], dtype=float)

    return mass, xMin, xMax, nPoint, EV_first, EV_last, interpolation_type, interpolation_numbers, potential_declerations
