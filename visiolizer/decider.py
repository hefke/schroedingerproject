"""
This modul lets the user decide what he wants to plot.

returns:
    - one limit-array with the values for the lower and upper X and Y boundries
    - one decision-array that contains the information which data to read in and plot
    - one namestring for the later headline of the plot """
    

decision_one_string = input('What do you want to plot? (enter the corresponding number)'
                       + '\n' + 'those are the options:' + '\n' + 
                       '1. nothing' + '\n' +
                       '2. energies, wavefunctions' + '\n' +
                       '3. energies, wavefunctions, exp-values' + '\n' +
                       'your pick: ')
decisiononevar = int(decision_one_string)

potentialstring = input('do you want to plot the potential?' + '\n' +
                        'enter y (yes) or n (no): ')

limitstring = input('do you want custom axis limits?' + '\n' +
                     'enter y (yes) or n (no): ')

if limitstring == 'y':
    xmin, xmax = float(input('enter xmin: ')), float(input('enter xmax: '))
    ymin, ymax = float(input('enter ymin: ')), float(input('enter ymax: '))
if limitstring == 'n':
    xmin, xmax, ymin, ymax = None, None, None, None
    
limits = [xmin, xmax, ymin, ymax]

if decisiononevar == 1:
    decision = [False, False, False]
    namestring = ' '
if decisiononevar == 2:
    decision = [True, True, False]
    namestring = 'wavefunctions'
if decisiononevar == 3:
    decision = [True, True, True]
    namestring = 'wavefunctions, expvalues'

if potentialstring == 'y' and (decisiononevar == 2 or decisiononevar == 3):
    decision.append(True)
    namestring = namestring + ', potential'
if potentialstring == 'y' and decisiononevar == 1:
    decision.append(True)
    namestring = namestring + 'potential'
if potentialstring == 'n':
    decision.append(False)
    