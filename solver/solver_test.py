#!/usr/bin/env python3
import equation_solver as eq
import numpy as np

def test_harm_osz():
    mass, xMin, xMax, nPoint, EV_first, EV_last, interpolation_type, potential_declerations = eq.read_input("tests/harm_osz/schroedinger.inp")
    x_values, potential, potential_dat = eq.potential_discret(xMin, xMax, nPoint, interpolation_type, potential_declerations)
    eigenvalues = eq.solve_schroedinger(nPoint, mass, xMin, xMax, EV_first, EV_last, x_values, potential)
    potential_exp=np.loadtxt("tests/harm_osz/potential.exp")
    eigenvalues_exp=np.loadtxt("tests/harm_osz/eigenvalues.exp")
    assert np.all(eigenvalues-eigenvalues_exp<1e-10)
    assert np.all(potential_dat-potential_exp<1e-10)

def test_inf_well():
    mass, xMin, xMax, nPoint, EV_first, EV_last, interpolation_type, potential_declerations = eq.read_input("tests/inf_well/schroedinger.inp")
    x_values, potential, potential_dat = eq.potential_discret(xMin, xMax, nPoint, interpolation_type, potential_declerations)
    eigenvalues = eq.solve_schroedinger(nPoint, mass, xMin, xMax, EV_first, EV_last, x_values, potential)
    potential_exp=np.loadtxt("tests/inf_well/potential.exp")
    eigenvalues_exp=np.loadtxt("tests/inf_well/eigenvalues.exp")
    assert np.all(eigenvalues-eigenvalues_exp<1e-10)
    assert np.all(potential_dat-potential_exp<1e-10)
    
def test_finite_well():
    mass, xMin, xMax, nPoint, EV_first, EV_last, interpolation_type, potential_declerations = eq.read_input("tests/finite_well/schroedinger.inp")
    x_values, potential, potential_dat = eq.potential_discret(xMin, xMax, nPoint, interpolation_type, potential_declerations)
    eigenvalues = eq.solve_schroedinger(nPoint, mass, xMin, xMax, EV_first, EV_last, x_values, potential)
    potential_exp=np.loadtxt("tests/finite_well/potential.exp")
    eigenvalues_exp=np.loadtxt("tests/finite_well/eigenvalues.exp")
    assert np.all(eigenvalues-eigenvalues_exp<1e-10)
    assert np.all(potential_dat-potential_exp<1e-10)
    
def test_double_well_linear():
    mass, xMin, xMax, nPoint, EV_first, EV_last, interpolation_type, potential_declerations = eq.read_input("tests/double_well_linear/schroedinger.inp")
    x_values, potential, potential_dat = eq.potential_discret(xMin, xMax, nPoint, interpolation_type, potential_declerations)
    eigenvalues = eq.solve_schroedinger(nPoint, mass, xMin, xMax, EV_first, EV_last, x_values, potential)
    potential_exp=np.loadtxt("tests/double_well_linear/potential.exp")
    eigenvalues_exp=np.loadtxt("tests/double_well_linear/eigenvalues.exp")
    assert np.all(eigenvalues-eigenvalues_exp<1e-10)
    assert np.all(potential_dat-potential_exp<1e-10)
    
def test_double_well_cubic():
    mass, xMin, xMax, nPoint, EV_first, EV_last, interpolation_type, potential_declerations = eq.read_input("tests/double_well_cubic/schroedinger.inp")
    x_values, potential, potential_dat = eq.potential_discret(xMin, xMax, nPoint, interpolation_type, potential_declerations)
    eigenvalues = eq.solve_schroedinger(nPoint, mass, xMin, xMax, EV_first, EV_last, x_values, potential)
    potential_exp=np.loadtxt("tests/double_well_cubic/potential.exp")
    eigenvalues_exp=np.loadtxt("tests/double_well_cubic/eigenvalues.exp")
    assert np.all(eigenvalues-eigenvalues_exp<1e-10)
    assert np.all(potential_dat-potential_exp<1e-10)
    
def test_asym_well():
    mass, xMin, xMax, nPoint, EV_first, EV_last, interpolation_type, potential_declerations = eq.read_input("tests/asym_well/schroedinger.inp")
    x_values, potential, potential_dat = eq.potential_discret(xMin, xMax, nPoint, interpolation_type, potential_declerations)
    eigenvalues = eq.solve_schroedinger(nPoint, mass, xMin, xMax, EV_first, EV_last, x_values, potential)
    potential_exp=np.loadtxt("tests/asym_well/potential.exp")
    eigenvalues_exp=np.loadtxt("tests/asym_well/eigenvalues.exp")
    assert np.all(eigenvalues-eigenvalues_exp<1e-10)
    assert np.all(potential_dat-potential_exp<1e-10)