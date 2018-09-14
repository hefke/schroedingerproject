#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This executeable script uses the sglpackage.plotter and matplotlib.pyplot
modules to create"""

import argparse
import matplotlib.pyplot as plt
import sglpackage.plotter as plotter

_DESCRIPTION = 'View the user documentation for more information'
_PARSER = argparse.ArgumentParser(description=_DESCRIPTION)

_MSG = 'Directory (default: same as the scripts directory)'
_PARSER.add_argument('-d', '--directory', default='', help=_MSG)

_MSG = 'Scalingfactor (default: 1.0)'
_PARSER.add_argument('-f', '--scalingfactor', type=float, metavar='NUM',
                     default=1.0, help=_MSG)

_MSG = 'Axis limits in order: xmin xmax ymin ymax seperated by whitespace'
_PARSER.add_argument('-l', '--limits', default=[None, None, None, None],
                     help=_MSG, type=float, nargs='+')

ARGS = _PARSER.parse_args()
if len(ARGS.limits) != 4:
    _PARSER.error('Either give no values or exactly four')

DATADIREC = ARGS.directory
LIMITS = ARGS.limits
SCALINGNUMBER = ARGS.scalingfactor

plotter.check(DATADIREC)

THEDATA = plotter.readthedata(potdirec=DATADIREC, wfuncsdirec=DATADIREC,
                              energiedirec=DATADIREC, expvdirec=DATADIREC)

plt.figure(figsize=[14, 9])

plt.subplot(1, 2, 1)
plotter.mainplot(potinput=THEDATA[0], energieinput=THEDATA[1],
                 funcinput=THEDATA[2], expvinput=THEDATA[3],
                 prefactor=SCALINGNUMBER, limitinput=LIMITS)

plt.subplot(1, 2, 2)
plotter.plotsigma(energieinput=THEDATA[1], expvinput=THEDATA[3])
plt.savefig('plot.pdf', dpi=400, bbox_inches='tight')
