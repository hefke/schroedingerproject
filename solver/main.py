import equation_solver as eq
import os.path


if os.path.exists('schroedinger.inp') == True:
    fname_full = 'schroedinger.inp'
else:
    directory_input_dat = input('enter the potential directory: ')
    fname_full = os.path.join(directory_input_dat, 'schroedinger.inp')
        
mass, xMin, xMax, nPoint, EV_first, EV_last, interpolation_type, potential_declerations = eq.read_input(fname_full)
x_values, potential, drei = eq.potential_discret(xMin, xMax, nPoint, interpolation_type, potential_declerations)
eq.solve_schroedinger(nPoint, mass, xMin, xMax, EV_first, EV_last, x_values, potential)