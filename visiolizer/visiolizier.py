import matplotlib.pyplot as plt
import readresults
import plotter
import decider

factorstring = input('enter a scalingfactor (1 for default): ')
scalingnumber = float(factorstring)

limitlist = decider.limits
decidelist = decider.decision
picturename = decider.namestring

thedata = readresults.readthedata(pot = decidelist[3], wfuncs = decidelist[0],
                                  energie = decidelist[1], expv = decidelist[2])

#______________________________________________________________________________

if decidelist[2] == False:
    plt.figure(figsize = [14,9])
    
    plotter.letsplot(namestring = picturename, energieinput = thedata[1],
                                prefactor = scalingnumber, limitinput = limitlist,
                                funcinput = thedata[2], ifpot = decidelist[3], 
                                ifexpv = decidelist[2], potinput = thedata[0], 
                                expvinput = thedata[3], iffunc = decidelist[0])
    
    plt.savefig('plot.pdf', dpi = 400, bbox_inches = 'tight')

"""Only if the user decides to plot the expected X values, one figure with 
    two subplots is created """

if decidelist[2] == True:
    plt.figure(figsize = [14,9])
    
    plt.subplot(1, 2, 1)
    plotter.letsplot(namestring = picturename, energieinput = thedata[1],
                                prefactor = scalingnumber, limitinput = limitlist,
                                funcinput = thedata[2], ifpot = decidelist[3], 
                                ifexpv = decidelist[2], potinput = thedata[0], 
                                expvinput = thedata[3], iffunc = decidelist[0])
    
    plt.subplot(1, 2, 2)
    plotter.plotsigma(energieinput = thedata[1], expvinput = thedata[3])
    
    plt.savefig('plot.pdf', dpi = 400, bbox_inches = 'tight')
    