import matplotlib.pyplot as plt

def letsplot(namestring, energieinput, ifpot, ifexpv, iffunc, potinput, expvinput, funcinput,
             prefactor=1.0, limitinput=[None, None, None, None]):
    
        """Function used for plotting the results produced by the solver. In particular:
            the discretized Potential and Eigenstates, the Eigenenergies and the expected vales of X
        
        args:
            namestring : Headline of the created plot
            energieinput : array-like input with all the Eigenenergie-values, shape = (N)
            potinput : array-like input with the discretized Potential and the corresponding
                x-values as the first entry, shape = (2,npoint)
            expvinput : array-like input with the calculated expected values and X blur
                shape = (2,N)
            funcinput : array-like input which contains the discretized Eigenfunctons and their
                corresponding X values as the first entry, shape = (N+1,npoint)
            ifpot, ifexpv, iffunc: only if one of the variables is True, the corresponding data is plotted
            prefactor : scaling factor of the plotted Eigenfunctions (optional)
            limitinput : array-like input which contains the boundries of the plot
                [xmin, xmax, ymin, ymax] in that order (optional)
                
        returns:
            the selected plotted data.
            DOES NOT create a custom figure """
            
        plt.xlabel('location $\t{x}$ in Bohr', size = 18)
        plt.ylabel('energie $\t{E}$ in Hartree', size = 18)
        
        ax = plt.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        
        if not limitinput == [None, None, None, None]:
            plt.axis(xmin = limitinput[0], xmax = limitinput[1], ymin = limitinput[2], ymax = limitinput[3])
        
        if iffunc == True:
            for jj in range(0, len(energieinput)):
                plt.axhline(y = energieinput[jj], color = 'gray')
            
            for jj2 in range(0, len(energieinput)):
                plt.plot(funcinput[0], prefactor*funcinput[jj2+1] + energieinput[jj2],
                         color = 'blue')
        
        plt.title(namestring, size = 22)
        
        if ifpot == True:
            plt.plot(potinput[0], potinput[1], color = 'green')
        
        if ifexpv == True:
            for jj3 in range(0, len(energieinput)):
                plt.plot(expvinput[0][jj3], energieinput[jj3], style = 'x', color = 'red')
        return

def plotsigma(expvinput, energieinput):
    
        """ Plots the calculated X blur, with an offset depending on the corresponding Eigenstate.
        
        args:
            expvinput : array-like input with the calculated expected values and X blur
                shape = (2,N)
            energieinput : array-like input with all the Eigenenergie-values, shape = (N)
            
        returns:
            the plotted X blur data.
            DOES NOT create a figure """
    
        plt.xlabel('location $\t{x}$ in Bohr', size = 18)
        plt.ylabel('energie $\t{E}$ in Hartree', size = 18)
        
        ax = plt.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
    
        for ii in range(0, len(energieinput)):
            plt.plot(expvinput[1][ii], energieinput[ii], style = 'x', color = 'purple')
        plt.title('$\sigma_{x}$', size = 22)
        return
    