import numpy as np
from os import path

def readthedata(pot=True, wfuncs=True, energie=True, expv=True):
    """function which reads the data provided by the solver
    
    Args:
        pot = True/False
        decides whether or not to read in the potential data
        wfuncs = True/False
        decides whether or not to read in the eigenfunctions data
        energies = True/False
        decides whether or not to read in the energies data
        expv = True/False
        decides whether or not to read in the exp-values data
    
    returns:
        one array with all the data"""
    
    if pot == True:
        if path.exists('potential.dat') == True:
            inputstring = 'potential.dat'
        if path.exists('potential.dat') == False:
            potdirectory = input('enter the potential directory: ')
            inputstring = potdirectory + 'potential.dat'
        badpotarray = np.loadtxt(fname = inputstring)
        potergebnis = badpotarray.transpose()
        
    if pot == False:
        potergebnis = 'skipped  potential'

    if wfuncs == True:
        if path.exists('wavefuncs.dat') == True:
            inputstring2 = 'wavefuncs.dat'
        if path.exists('wavefuncs.dat') == False:
            wfuncdirectory = input('enter the eigenfunctions directory: ')
            inputstring2 = wfuncdirectory + 'wavefuncs.dat'
        badfuncarray = np.loadtxt(fname = inputstring2)
        wfuncergebnis = badfuncarray.transpose()
        
    if wfuncs == False:
        wfuncergebnis = 'skipped eigenfunctions'
        
    if energie == True:
        if path.exists('energies.dat') == True:
            inputstring3 = 'energies.dat'
        if path.exists('energies.dat') == False:
            energiedirectory = input('enter the energies directory: ')
            inputstring3 =energiedirectory + 'energies.dat'
        badenergiearray = np.loadtxt(fname = inputstring3)
        energiesergebnis = badenergiearray.transpose()
        
    if energie == False:
        energiesergebnis = 'skipped energies'
        
    if expv == True:
        if path.exists('expvalues.dat') == True:
            inputstring4 = 'expvalues.dat'
        if path.exists('expvalues.dat') == False:
            expvdirectory = input('enter the exp-values directory: ')
            inputstring4 = expvdirectory + 'expvalues.dat'
        badexpvarray = np.loadtxt(fname = inputstring4)
        expvergebnis = badexpvarray.transpose()
        
    if expv == False:
        expvergebnis = 'skipped exp-values'
    return potergebnis, energiesergebnis, wfuncergebnis, expvergebnis
