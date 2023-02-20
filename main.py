import sys 
import os
PATH  = "D:/Kursevi/Programming Numerical Methods in Python"

sys.path.append(os.path.join(PATH, 'Section 1 - Roots of High-Degree Equations'))
import iteration_method, newton_raphson, bisection, regula_falsi, secant, python_built_in_functions1

sys.path.append(os.path.join(PATH, 'Section 2 - Interpolation and Curve Fitting'))
import linear_interpolation, lagrange_interpolation, newton_interpolation, linear_regression, polynomial_approximation, python_built_in_functions2

sys.path.append(os.path.join(PATH, 'Section 3 - Numerical Differentiation'))
import finite_differences, python_built_in_functions3

import numpy as np
import scipy
import random
import math
import matplotlib.pyplot as plt
 
 
def main():
    section_3_differentiation()
 

def section_3_differentiation():
    f = lambda x: 0.1 * x**5 - 0.2 * x**3 + 0.1 * x - 0.2
    
    x = np.linspace(0, 1, 100);
    
    python_built_in_functions3.central_derivative(f, x)
    

def section_2_intepolation_and_curve_fitting():
    time = [0, 20, 40, 60, 80, 100]
    temperature = [26, 48.6, 61.6, 71.2, 74.8, 75.2]
    
    python_built_in_functions2.lagrange_interpolation_method(time, temperature)
    
    x1 = [3, 4, 5, 6, 7, 8]
    y1 = [0, 7, 17, 26, 35, 45]
    
    python_built_in_functions2.linear_regression(x1, y1)
    
    x2 = [0, 1, 2, 3, 4, 5]
    y2 = [2, 8, 14, 28, 39, 62]
    
    f = lambda x, a0, a1, a2: a0 + a1 * x + a2 * x ** 2
    
    python_built_in_functions2.curve_fitting(f, x2, y2)
    
 
def section_1_roots_finding():
    
    some_function = lambda x : x**2 + (math.cos(x))**2 - 4 * x
    
    python_built_in_functions2.fsolve_root_finding_method(f=y)

    # Function for which is calculating single root
    def y(x):
        return 2*x**2 - 5*x + 3

    def f(x):
        return x**2 + (math.cos(x))**2 - 4 * x
    
    x = range(-50, 50)
    y = []
    
    for value in x:
        y.append(round(-2.3 * value**2 + 6.6 * value + 273, 7))
    
    plt.figure(1)
    plt.plot(x, y)
    plt.grid()
    plt.show()
    
main()
