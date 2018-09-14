"""
Module to test the sduation solver for 6 examples
"""

#!/usr/bin/env python3
import numpy as np
import sglpackage.solver_definitions as sd

def test_harm_osz():
    """
    Tests eigenvalues and potential for the example of a harmonic oszilator
    """
    file = "tests/harm_osz/schroedinger.inp"
    x_min, x_max, n_point, ev_first, ev_last, interp_type, potential_decl, alpha = sd.read_inp(file)
    potential_dat = sd.potential_discret(x_min, x_max, n_point, interp_type, potential_decl)
    eigenvektors, eigenvalues = sd.solve_wavefuncs(n_point, ev_first, ev_last, potential_dat, alpha)
    sd.solve_expvalues(ev_first, ev_last, potential_dat, eigenvektors)
    potential_exp = np.loadtxt("tests/harm_osz/potential.exp")
    eigenvalues_exp = np.loadtxt("tests/harm_osz/eigenvalues.exp")
    assert np.all(eigenvalues-eigenvalues_exp < 1e-10)
    assert np.all(potential_dat-potential_exp < 1e-10)

def test_inf_well():
    """
    Tests eigenvalues and potential for the example of a infinite well
    """
    file = "tests/inf_well/schroedinger.inp"
    x_min, x_max, n_point, ev_first, ev_last, interp_type, potential_decl, alpha = sd.read_inp(file)
    potential_dat = sd.potential_discret(x_min, x_max, n_point, interp_type, potential_decl)
    eigenvektors, eigenvalues = sd.solve_wavefuncs(n_point, ev_first, ev_last, potential_dat, alpha)
    sd.solve_expvalues(ev_first, ev_last, potential_dat, eigenvektors)
    potential_exp = np.loadtxt("tests/inf_well/potential.exp")
    eigenvalues_exp = np.loadtxt("tests/inf_well/eigenvalues.exp")
    assert np.all(eigenvalues-eigenvalues_exp < 1e-10)
    assert np.all(potential_dat-potential_exp < 1e-10)

def test_finite_well():
    """
    Tests eigenvalues and potential for the example of a finite well
    """
    file = "tests/finite_well/schroedinger.inp"
    x_min, x_max, n_point, ev_first, ev_last, interp_type, potential_decl, alpha = sd.read_inp(file)
    potential_dat = sd.potential_discret(x_min, x_max, n_point, interp_type, potential_decl)
    eigenvektors, eigenvalues = sd.solve_wavefuncs(n_point, ev_first, ev_last, potential_dat, alpha)
    sd.solve_expvalues(ev_first, ev_last, potential_dat, eigenvektors)
    potential_exp = np.loadtxt("tests/finite_well/potential.exp")
    eigenvalues_exp = np.loadtxt("tests/finite_well/eigenvalues.exp")
    assert np.all(eigenvalues-eigenvalues_exp < 1e-10)
    assert np.all(potential_dat-potential_exp < 1e-10)

def test_double_well_linear():
    """
    Tests eigenvalues and potential for the example of a linear double well
    """
    file = "tests/double_well_linear/schroedinger.inp"
    x_min, x_max, n_point, ev_first, ev_last, interp_type, potential_decl, alpha = sd.read_inp(file)
    potential_dat = sd.potential_discret(x_min, x_max, n_point, interp_type, potential_decl)
    eigenvektors, eigenvalues = sd.solve_wavefuncs(n_point, ev_first, ev_last, potential_dat, alpha)
    sd.solve_expvalues(ev_first, ev_last, potential_dat, eigenvektors)
    potential_exp = np.loadtxt("tests/double_well_linear/potential.exp")
    eigenvalues_exp = np.loadtxt("tests/double_well_linear/eigenvalues.exp")
    assert np.all(eigenvalues-eigenvalues_exp < 1e-10)
    assert np.all(potential_dat-potential_exp < 1e-10)

def test_double_well_cubic():
    """
    Tests eigenvalues and potential for the example of a cubic double well
    """
    file = "tests/double_well_cubic/schroedinger.inp"
    x_min, x_max, n_point, ev_first, ev_last, interp_type, potential_decl, alpha = sd.read_inp(file)
    potential_dat = sd.potential_discret(x_min, x_max, n_point, interp_type, potential_decl)
    eigenvektors, eigenvalues = sd.solve_wavefuncs(n_point, ev_first, ev_last, potential_dat, alpha)
    sd.solve_expvalues(ev_first, ev_last, potential_dat, eigenvektors)
    potential_exp = np.loadtxt("tests/double_well_cubic/potential.exp")
    eigenvalues_exp = np.loadtxt("tests/double_well_cubic/eigenvalues.exp")
    assert np.all(eigenvalues-eigenvalues_exp < 1e-10)
    assert np.all(potential_dat-potential_exp < 1e-10)

def test_asym_well():
    """
    Tests eigenvalues and potential for the example of a asymetric well
    """
    file = "tests/asym_well/schroedinger.inp"
    x_min, x_max, n_point, ev_first, ev_last, interp_type, potential_decl, alpha = sd.read_inp(file)
    potential_dat = sd.potential_discret(x_min, x_max, n_point, interp_type, potential_decl)
    eigenvektors, eigenvalues = sd.solve_wavefuncs(n_point, ev_first, ev_last, potential_dat, alpha)
    sd.solve_expvalues(ev_first, ev_last, potential_dat, eigenvektors)
    potential_exp = np.loadtxt("tests/asym_well/potential.exp")
    eigenvalues_exp = np.loadtxt("tests/asym_well/eigenvalues.exp")
    assert np.all(eigenvalues-eigenvalues_exp < 1e-10)
    assert np.all(potential_dat-potential_exp < 1e-10)
