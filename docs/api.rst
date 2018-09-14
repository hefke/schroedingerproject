============================
sglpackage's API reference
============================

.. automodule:: sglpackage

The "plot" module
=================

.. automodule:: sglpackage.plotter
   :members:

The "solve" module
==================

.. automodule:: sglpackage.solver_definitions
   :members:

==================
user documentation
==================

Like the project's name suggests, this project's purpose is to solve the one dimensional, time
independent schroedinger equation for a given potential V. Because the potential and the mass of the
particle experiencing this potential are the main specifications of the problem, knowing them is cruicial
for solving the problem. All the information is expected to be stored in an input file named 'schroedinger.inp'.
If the information file is named differently, it has to be renamed.

**writing the schroedinger.inp file**

The upper project directory contains an example of a possible input file. It's content looks like this:

+----------------------------------------------------------------------+
|  | 4.0	   # Mass 				               |
|  | -5.0 5.0 1999 # xMin xMax nPoin			               |
|  | 1 5           # first and last eigenvalue to include in the output| 
|  | polynomial    # interpolation type 			       |
|  | 3             # nr. of interpolation points and xy declarations   |
|  | -1.0 0.5 						               |
|  | 0.0 0.0 						               |
|  | 1.0 0.5						               |
+----------------------------------------------------------------------+

For the interpolation type you have the following options: 'linear', 'polynomial' and 'cspline'.
The npoint entry will deternime the number of rows in your potential and wavefunctions data, whereas
the number of eigenvalues will determine the number of columns.

**running the solver script**

The position of the main script for solving the schroedinger equation is the upper directory of the 
project, it is executable from shell. To start the script type:

>>> ./solver.py

If the input file is in a other directory, a FileNotFoundError will be raised. In this case you 
can add the argument '-d' or '--directory' followed by the diretory which contains the input file.
For example:

>>> ./solver.py -d somedirectory/

If the file is several directories aboth, you can use '..' to indicate a directory step upwards:

>>> ./solver.py -d ../../datafolder/

**running the visiolizer script**

After executing the solver script, the generated results will be in the upper project direstory.
Like with the first script, it is possible to run the visiolizer script without having the data
files in the same directory:

>>> ./visiolizer -d somedirectory/

If you get no errors, a plot.pdf data file will be created and you have succesfully solved and plotted
the solutions of the schroedinger equation with your desired potential!
If you wish to create more fitting plots, there are a few options left:

>>> ./visioliter.py --scalingfactor NUM

where NUM is the factor, by which the plotted wavefunctions will be multiplied.

>>> ./visiolizer.py --limits XMIN XMAX YMIN YMAX

where XMIN/XMAX are the lower/upper-bound of the X-Axis of the plot and YMIN/YMAX of the Y-Axis respectively.
To view the shortcuts for those arguments, add '-h' to the execute command.

**running the tests**

To test the functionality of the solver script, tests for several potentials have been implemented.
You can run the tests by typing following command in the upper project directory:

>>> python3 -m pytest


