"""This module contains routines for reading in the data
provided by the solver"""

import sys
import numpy as np

def readthedata(potdirec='', wfuncsdirec='', energiedirec='', expvdirec=''):
    """function which reads the data provided by the solver

    input:
        potdirec = direction of the potential data
        wfuncsdirec = direction of the functions data
        energiedirec = direction of the energies data
        expvdirec = direction of the expvalues data

    output:
        one array with all the data"""

    inputstring = potdirec + 'potential.dat'
    potergebnis = np.loadtxt(fname=inputstring).transpose()

    inputstring2 = wfuncsdirec + 'wavefuncs.dat'
    wfuncergebnis = np.loadtxt(fname=inputstring2).transpose()

    inputstring3 = energiedirec + 'energies.dat'
    energiesergebnis = np.loadtxt(fname=inputstring3).transpose()

    inputstring4 = expvdirec + 'expvalues.dat'
    expvergebnis = np.loadtxt(fname=inputstring4).transpose()

    return potergebnis, energiesergebnis, wfuncergebnis, expvergebnis

def check(direcinput):
    """Checks for common error which might occur while trying to
    open the data files

    input:
        direcinput: the directory of the data
    output: brief report of the check """
    try:
        open(direcinput + 'potential.dat', 'r')
        open(direcinput + 'energies.dat', 'r')
        open(direcinput + 'wavefuncs.dat', 'r')
        open(direcinput + 'expvalues.dat', 'r')

    except FileNotFoundError:
        print('data missing')
        print('add -h for further options')
        sys.exit(1)

    else:
        print('data succesfully read')
        print('')
    return
