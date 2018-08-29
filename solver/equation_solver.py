import numpy as np
import scipy as sp



def read_input(filename):
    """
    Reads all information from the input file and saves them as variables

    Args:
        filename: Name of the input file containing the specification of the problem

    Returns:
        mass: mass of the particle
        xMin: minimal x-value
        xMax: maximal x-value
        nPoint: number of points between xMin and xMax
        EV_first: first eigenvalue to be printed
        EV_last: last eigenvalue to be printed
        interpolation_type: type of interpolation
        interpolation_numbers: number of points defining the potential
        potential_declerations: array of points defining the potnetial
    """
    file = open(filename, "r")
    data = []
    lines = file.readlines()
    for line in lines:
        line=line.partition("#")[0]
        line=line.strip()
        data.append(line.split())
    file.close()
    data=np.array(data)
    mass = float(data[0][0])
    xMin = float(data[1][0])
    xMax = float(data[1][1])
    nPoint = int(data[1][2])
    EV_first = int(data[2][0])
    EV_last = int(data[2][1])
    interpolation_type = str(data[3][0])
    interpolation_number = int(data[4][0])
    potential_declerations=np.zeros([interpolation_number, 2])
    for ii in range(0, len(data)-5):
        potential_declerations[ii]=potential_declerations[ii]+np.asarray(data[ii+5], dtype=float)

    return mass, xMin, xMax, nPoint, EV_first, EV_last, interpolation_type, potential_declerations


def potential_discret(xMin, xMax, nPoint, interpolation_type, potential_declerations):
    """
    discretises the potential by using linear/cubic/polynomial interpolation and saves the results into a file potential.dat 

    Args:
        xMin: minimal x-value
        xMax: maximal x-value
        nPoint: number of points between xMin and xMax
        interpolation_type: type of interpolation
        potential_declerations: array of points defining the potnetial
    """
    x_values=np.linspace(xMin, xMax, nPoint)
    if interpolation_type=="linear":
        y_values=np.interp(x_values, potential_declerations[:,0], potential_declerations[:,1])
    elif interpolation_type=="polynomial":
        y_values=sp.interpolate.barycentric_interpolate(potential_declerations[:,0], potential_declerations[:,1], x_values)
    elif interpolation_type=="cspline":
        y_values=sp.interpolate.CubicSpline(potential_declerations[:,0], potential_declerations[:,1])(x_values)
            
            
    potential_dat=np.array(list(zip(x_values, y_values)))
    np.savetxt("potential.dat", potential_dat)
    return x_values, y_values

def solve_schroedinger(nPoint, mass, xMin, xMax, EV_first, EV_last, x_values, potential):
    """
    Calculates the wavefunctions and energies by expressing the Hamilton-Operator as Matrix and solving its eigenvalue problem and saves them into a file.
    Also it calculates the expectation values of the x-variable and the postition blur and saves them into a file.
    
    Args:
        nPoint: number of points between xMin and xMax
        mass: mass of the particle
        xMin: minimal x-value
        xMax: maximal x-value
        EV_first: first eigenvalue to be printed
        EV_last: last eigenvalue to be printed
    """
    Delta=(xMax-xMin)/nPoint
    alpha=1/(mass*(Delta**2))
    matrix=np.diag(potential+np.ones(nPoint)*alpha)-np.diag(np.ones(nPoint-1)*alpha/2, 1)-np.diag(np.ones(nPoint-1)*alpha/2, -1)
    eigenvalues, eigenvektors = sp.linalg.eigh(matrix, eigvals=(EV_first-1, EV_last-1))

    wafefuncs_dat=np.zeros((nPoint, EV_last+1))
    wafefuncs_dat[:,0]=x_values
    wafefuncs_dat[:,1:]=eigenvektors
    np.savetxt("energies.dat", eigenvalues)
    np.savetxt("wavefuncs.dat", wafefuncs_dat)
    number_EV=EV_last-EV_first
    
    expvalues_x=np.zeros(number_EV+1)
    expvalues_x_square=np.zeros(number_EV+1)
    position_blur=np.zeros(number_EV+1)

    for jj in range(number_EV+1):
        expvalues_x[jj]=np.sum((x_values*eigenvektors[:,jj]**2))
        expvalues_x_square[jj]=np.sum((x_values**2*eigenvektors[:,jj]**2))
        position_blur[jj]=(expvalues_x_square[jj]-expvalues_x[jj]**2)**(0.5)
    expvalues_dat=np.zeros((number_EV+1, 2))
    expvalues_dat[:,0]=expvalues_x
    expvalues_dat[:,1]=position_blur
    np.savetxt("expvalues.dat", expvalues_dat)