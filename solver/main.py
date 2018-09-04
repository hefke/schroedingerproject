"""
Main script to using functions to read information from input file
and calculates potential, eigenfunctions, eigenvalues and expectation values forthe x-coordinate
"""
import os.path
import equation_solver as eq


if os.path.exists('schroedinger.inp') is True:
    FNAME = 'schroedinger.inp'
else:
    DIR_INP_DAT = input('enter the potential directory: ')
    FNAME = os.path.join(DIR_INP_DAT, 'schroedinger.inp')

X_MIN, X_MAX, N_POINT, EV_FIRST, EV_LAST, INTERP_TYPE, POTENTIAL_DECL, ALPHA = eq.read_inp(FNAME)
POTENTIAL_DAT = eq.potential_discret(X_MIN, X_MAX, N_POINT, INTERP_TYPE, POTENTIAL_DECL)
EIGENVEKTORS, EIGENVALUES = eq.solve_wavefuncs(N_POINT, EV_FIRST, EV_LAST, POTENTIAL_DAT, ALPHA)
eq.solve_expvalues(EV_FIRST, EV_LAST, POTENTIAL_DAT, EIGENVEKTORS)
