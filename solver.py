#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main script, which uses the functions provided by the sglpackage to read in the information
from the input file and calculates the discretized potential, eigenfunctions, eigenvalues
and expectation values for the x-coordinate."""

import argparse
import sglpackage.solver_definitions as sd

_DESCRIPTION = 'View the user documentation for more information'
_PARSER = argparse.ArgumentParser(description=_DESCRIPTION)

_MSG = 'Directory (default: same as the scripts directory)'
_PARSER.add_argument('-d', '--directory', default='', help=_MSG)
ARGS = _PARSER.parse_args()

FNAME = ARGS.directory + 'schroedinger.inp'

X_MIN, X_MAX, N_POINT, EV_FIRST, EV_LAST, INTERP_TYPE, POTENTIAL_DECL, ALPHA = sd.read_inp(FNAME)
POTENTIAL_DAT = sd.potential_discret(X_MIN, X_MAX, N_POINT, INTERP_TYPE, POTENTIAL_DECL)
EIGENVEKTORS, EIGENVALUES = sd.solve_wavefuncs(N_POINT, EV_FIRST, EV_LAST, POTENTIAL_DAT, ALPHA)
sd.solve_expvalues(EV_FIRST, EV_LAST, POTENTIAL_DAT, EIGENVEKTORS)
