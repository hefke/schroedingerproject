import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# .... energien: energies
#..... potentiale: discrpot
#..... eigenfunktionen: wfuncs


energiedataname = input("enter the name of the energie datei: ")
funcdataname = input("enter the name of the function datei: ")
potdataname = input("enter the name of the potential datei: ") 


# datei musst be in the same ordner
def energies(inputstring):
    completefilename = inputstring + '.dat'
    energieslist = []
    energiespandas = pd.read_table(completefilename, delim_whitespace = True,
                         header = None, skiprows = 0)
    for ii in range(0, 15):
        energieslist.append(energiespandas[0][ii])
    return energieslist

    
def potential(inputstring3):
    completefilename3 = inputstring3 + '.dat'
    discrpotpandas = pd.read_table(completefilename3, delim_whitespace = True,
                               header = None, skiprows = 0)
    discrpotarray = np.empty((2, len(discrpotpandas)), dtype = float)
    for ii2 in range(0, 2):
        for ii3 in range(0, len(discrpotpandas)):
            discrpotarray[ii2][ii3] = discrpotpandas[ii2][ii3]
    return discrpotarray


#aaa = potential(potdataname)


def eigenfunctions(inputstring2):
    completefilename2 = inputstring2 + '.dat'
    wfuncpandas = pd.read_table(completefilename2, delim_whitespace = True,
                           header = None, skiprows = 0)
    funcarray = np.empty((len(list(wfuncpandas)), len(wfuncpandas)),
                         dtype = float)
    for ii4 in range(0, len(list(wfuncpandas))):
        for ii5 in range(0, len(wfuncpandas)):
            funcarray[ii4][ii5] = wfuncpandas[ii4][ii5]
    return funcarray

# ... diskretisierten x-werte sind jeweils in den discrpotarray und funcarray enthalten
#______________________________________________________________________________________

eee = energies(energiedataname)
ppp = potential(potdataname)
fff = eigenfunctions(funcdataname)

def plotthatshit(namestring, potinput, funcinput, energieinput, prefactor=1.0):
        plt.figure(figsize = [14,9])
        plt.xlabel('x in Bohr', size = 18)
        plt.ylabel('energie in Hartree', size = 18)
        
        ax = plt.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        plt.axis(xmin = -2.5, xmax = 2.5, ymin = -0.5, ymax = 8)
        
        plt.plot(potinput[0], potinput[1], label = 'potential', color = 'black')
        for jj in range(0, len(energieinput)):
            plt.axhline(y = energieinput[jj], color = 'gray')
        
        for jj2 in range(0, len(energieinput)):
            plt.plot(funcinput[0], prefactor*funcinput[jj2+1] + energieinput[jj2],
                     label = 'eigenfunctions', color = 'blue')
        plt.title(namestring, size = 22)
        plt.savefig(namestring + '.pdf', dpi=400, bbox_inches='tight')
        plt()
        return

dateiname = input('enter the title you want: ')
    
plotthatshit(dateiname, ppp, fff, eee, prefactor=16)
        

