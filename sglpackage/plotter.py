#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:10:39 2018

@author: dennis
"""

import matplotlib.pyplot as plt

def mainplot(energieinput, potinput, expvinput, funcinput,
             limitinput, prefactor=1.0):

    """Function used for plotting the results produced
    by the solver. In particular:
    the discretized Potential and Eigenstates,
    the Eigenenergies and the expected vales of X

    input:
        namestring : Headline of the created plot
        energieinput : array-like input with all the Eigenenergie-values, shape = (N)
        potinput : array-like input with the discretized Potential and the corresponding
            x-values as the first entry, shape = (2,npoint)
        expvinput : array-like input with the calculated expected values and X blur
            shape = (2,N)
        funcinput : array-like input which contains the discretized Eigenfunctons and their
            corresponding X values as the first entry, shape = (N+1,npoint)
        prefactor : scaling factor of the plotted Eigenfunctions (optional)
        limitinput : array-like input which contains the boundries of the plot
            [xmin, xmax, ymin, ymax] in that order (optional)

    output:
        One plot of the """

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

    plt.title('potential', size=22)
    return

def plotsigma(expvinput, energieinput):
    """ Plots the calculated X blur, with an offset depending
    on the corresponding Eigenstate.

    input:
        expvinput : array-like input with the calculated expected values and X blur
        shape = (2,N)
        energieinput : array-like input with all the Eigenenergie-values, shape = (N)

    output:
        the plotted X blur data."""

    plt.xlabel('location $\t{x}$ in Bohr', size=18)
    plt.ylabel('energie $\t{E}$ in Hartree', size=18)

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    for ii in range(0, len(energieinput)):
        plt.plot(expvinput[1][ii], energieinput[ii], marker='x', color='purple')
    plt.title('$\sigma_{x}$', size=22)
    return
