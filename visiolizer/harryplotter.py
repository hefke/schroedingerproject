import matplotlib.pyplot as plt

def letsplot(namestring, energieinput, ifpot, ifexpv, iffunc, potinput, expvinput, funcinput,
             prefactor=1.0, limitinput=[None, None, None, None]):
    
        plt.xlabel('x in Bohr', size = 18)
        plt.ylabel('energie in Hartree', size = 18)
        
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
        plt.xlabel('x in Bohr', size = 18)
        plt.ylabel('energie in Hartree', size = 18)
        
        ax = plt.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
    
        for ii in range(0, len(energieinput)):
            plt.plot(expvinput[1][ii], energieinput[ii], style = 'x', color = 'purple')
        plt.title('sigma', size = 22)
        return
    