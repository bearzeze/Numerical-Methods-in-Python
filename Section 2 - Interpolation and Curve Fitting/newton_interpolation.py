import math
import numpy as np


def method(x_values, y_values):
    x_target = float(input("Enter number: "))
    
    m = len(x_values)
    n = m - 1
    
    y_matrix = divided_differences_table(x_values, y_values)
    
    # Polynomial coefficients are diagonal elements of the matrix
    a_coeff = np.diag(y_matrix)
    
    y_target = a_coeff[0]
    for i in range(1, m):
        product = 1
        for j in range(0, i):
            product *= (x_target - x_values[j])
            
        y_target += product * a_coeff[i]
    
    print(f"For x = {x_target}, y = {y_target}, using {n}. degree polynomial Newton's interpolation.")

    
    
def divided_differences_table(x, y):
    m = len(x)
    y_matrix = np.zeros((m, m))
    
    # First column of the divided differences table is the whole y data
    y_matrix[:, 0] = y
    
    for j in range(1, m):
        for i in range(j, m):
            y_matrix[i, j] = (y_matrix[i, j - 1] - y_matrix[j - 1, j - 1]) / (x[i] - x[j - 1])
      
    
    return y_matrix
        