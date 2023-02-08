import sys 
import os
PATH  = "D:/Kursevi/Programming Numerical Methods in Python"
sys.path.append(os.path.join(PATH, 'Section 2 - Roots of High-Degree Equations'))
sys.path.append(os.path.join(PATH, 'Section 3 - Interpolation and Curve Fitting'))


import iteration_method, newton_raphson, bisection, regula_falsi, secant, python_functions
import linear_interpolation, lagrange_interpolation

import numpy as np
import scipy
import random
import math
import matplotlib.pyplot as plt

 
 
def main():
    section_3_intepolation_and_curve_fitting()
 

def section_3_intepolation_and_curve_fitting():
    
    time = [0, 20, 40, 60, 80, 100]
    temperature = [26, 48.6, 61.6, 71.2, 74.8, 75.2]
    
    
    lagrange_interpolation.method(x_values=time, y_values=temperature, degree=5)
 
 
def section_2_roots_finding():
    
    funkcija = lambda x : x**2 + (math.cos(x))**2 - 4 * x
    
    python_functions.fsolve_root_finding_method(f=y)

    # Function for which is calculating single root
    def y(x):
        return 2*x**2 - 5*x + 3

    def f(x):
        return x**2 + (math.cos(x))**2 - 4 * x

    
def plotting():
    x = range(-50, 50)
    y = []
    
    for value in x:
        y.append(round(-2.3 * value**2 + 6.6 * value + 273, 7))
    
    plt.figure(1)
    plt.plot(x, y)
    plt.grid()
    plt.show()
    
main()
