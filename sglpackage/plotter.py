"""
This module contains all of the functions used to plot the results of the solver.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt

def mainplot(energieinput, potinput, expvinput, funcinput,
             limitinput, prefactor=1.0):

    """
    Function used for plotting the results produced
    by the solver. In particular:
    the discretized potential, the eigenstates,
    the eigenenergies and the expectation values of X.

    .. note:: the wavefunctions and the expectation values of X will \
    both be plotted with an offset depending on the corresponding eigenenergie value. \
    If the number of wavefunctions or expectation values exceeds the number of \
    eigenenergie values, an "list index out of range"-error will be raised.

    Args:
        energieinput : array-like input with all the eigenenergie-values, shape = (N)
        potinput : array-like input with the discretized Potential and the corresponding \
        x-values as the first entry, shape = (2, npoint)
        expvinput : array-like input with the calculated expected values \
        as the first entry, shape = (2, N)
        funcinput : array-like input which contains the discretized Eigenfunctons and \
        their corresponding X values as the first entry, shape = (N+1, mpoint)
        limitinput : array-like input which contains the boundries of the plot \
        [xmin, xmax, ymin, ymax] in that particular order
        prefactor : scaling factor of the plotted eigenfunctions (optional)
    **return**:
        One plot of all the mentioned data.
    """

    plt.xlabel('location $\t{x}$ in Bohr', size=18)
    plt.ylabel('energie $\t{E}$ in Hartree', size=18)

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    if limitinput != [None, None, None, None]:
        plt.axis(xmin=limitinput[0], xmax=limitinput[1], ymin=limitinput[2], ymax=limitinput[3])

    for jj in range(0, len(energieinput)):
        plt.axhline(y=energieinput[jj], color='gray')

    for jj2 in range(0, len(energieinput)):
        plt.plot(funcinput[0], prefactor*funcinput[jj2+1] + energieinput[jj2], color='blue')

    plt.plot(potinput[0], potinput[1], color='green')

    for jj3 in range(0, len(energieinput)):
        plt.plot(expvinput[0][jj3], energieinput[jj3], marker='x', color='red')

    plt.title('potential, eigenstates, expectation values of x', size=22)
    return

def plotsigma(expvinput, energieinput):
    """
    Plots the calculated X blur, with an offset depending
    on the corresponding Eigenstate.

    Args:
        expvinput : array-like input with the X position blur as the second entry \
        shape = (2, N)
        energieinput : array-like input with all the eigenenergie-values, shape = (N)
    **return**:
        the plotted X blur data.
    """

    plt.xlabel('location $\t{x}$ in Bohr', size=18)
    plt.ylabel('energie $\t{E}$ in Hartree', size=18)

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    for ii in range(0, len(energieinput)):
        plt.plot(expvinput[1][ii], energieinput[ii], marker='x', color='purple')
    plt.title('$\sigma_{x}$', size=22)
    return

def readthedata(potdirec='', wfuncsdirec='', energiedirec='', expvdirec=''):
    """
    This function reads the data files provided by the solver script, it is
    meant to be used along with the mainplot function because the read function
    and the input of the plot function have share the same format.

    .. note:: the function expects the files to be named exactly 'potential.dat', \
    'energies.dat', 'wavefuncs.dat' and expvalues.dat'. If the files are named \
    differently or are not in the stated directory, an "FileNotFoundError" is raised.

    Args:
        potdirec: direction of the potential data
        wfuncsdirec: direction of the functions data
        energiedirec: direction of the energies data
        expvdirec: direction of the expvalues data

    **return**:
        one array with all the data

    """
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
    """
    Checks for common error's which might occur while trying to
    open the data files provided by the solver script.

    Args:
        direcinput: the directory of the data files \
        (potential.dat, energies.dat, wfuncs.dat and expvalues.dat).
    **return**:
        A brief report for the user.
    """
    try:
        open(direcinput + 'potential.dat', 'r')
        open(direcinput + 'energies.dat', 'r')
        open(direcinput + 'wavefuncs.dat', 'r')
        open(direcinput + 'expvalues.dat', 'r')

    except FileNotFoundError:
        print('data missing')
        print('add -h to view options')
        sys.exit(1)

    else:
        print('data succesfully read')
        print('')
    return
