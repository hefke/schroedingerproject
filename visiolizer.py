#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 15:12:08 2018

@author: dennis
"""

import argparse
import matplotlib.pyplot as plt
import sglpackage.readresults as readresults
import sglpackage.plotter as plotter

_DESCRIPTION = 'hier könnte ihre werbung stehen'
_PARSER = argparse.ArgumentParser(description=_DESCRIPTION)

_MSG = 'Directory (default: .)'
_PARSER.add_argument('-d', '--directory', default='', help=_MSG)

_MSG = 'scalingfactor (default: 1.0)'
_PARSER.add_argument('-f', '--scalingfactor', type=float, metavar='NUM',
                     default=1.0, help=_MSG)

_MSG = 'limits in order'
_PARSER.add_argument('-l', '--limits', default=[None, None, None, None], help=_MSG, type=float,
                     nargs='+')

ARGS = _PARSER.parse_args()
DATADIREC = ARGS.directory
LIMITS = ARGS.limits
SCALINGNUMBER = ARGS.scalingfactor

readresults.check(DATADIREC)

THEDATA = readresults.readthedata(potdirec=DATADIREC, wfuncsdirec=DATADIREC,
                                  energiedirec=DATADIREC, expvdirec=DATADIREC)

plt.figure(figsize=[14, 9])

plt.subplot(1, 2, 1)
plotter.mainplot(potinput=THEDATA[0], energieinput=THEDATA[1],
                 funcinput=THEDATA[2], expvinput=THEDATA[3],
                 prefactor=SCALINGNUMBER, limitinput=LIMITS)

plt.subplot(1, 2, 2)
plotter.plotsigma(energieinput=THEDATA[1], expvinput=THEDATA[3])
plt.savefig('plot.pdf', dpi=400, bbox_inches='tight')
