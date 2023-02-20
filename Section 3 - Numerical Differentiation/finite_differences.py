import numpy as np
import matplotlib.pyplot as plt
import math

def forward_method(f, x, h=0.01):
    print(f"\nForward Finite Differentiation:")
    print(120 * "=")

    x_i = x
    x_iplus1 = x_i + h
    
    first_derivative = (f(x_iplus1) - f(x_i) ) / h
    print(f"f'(x = {x}) = {first_derivative}")
    
    x_iplus2 = x_iplus1 + h
    second_derivative = (f(x_iplus2) - 2 * f(x_iplus1) + f(x_i) ) / h**2
    print(f"f''(x = {x}) = {second_derivative}")
    print(120 * "=")

    
def central_method(f_ana, x, h=0.01, f_prim_ana=None, f_second_ana=None):
    print(f"\nCentral Finite Differentiation:")
    print(120 * "=")
    
    x_i = x
    x_iminus1 = x_i - h
    x_iplus1 = x_i + h
        
    f_prim_num = ((f_ana(x_iplus1) - f_ana(x_iminus1) ) / (2 * h))
    f_second_num = ((f_ana(x_iplus1) - 2*f_ana(x_i) + f_ana(x_iminus1)) / h**2)
        
    # Converting every list to numpy array
    x = np.array(x)
    f_prim_num = np.array(f_prim_num)
    f_second_num = np.array(f_second_num)
    
    # Plotting    
    plt.figure(1)
    plt.plot(x, f_ana(x),'k-', x, f_prim_num, 'b--', x, f_second_num, 'r-.')
    plt.grid()
    plt.legend(["f(x)", "f'(x)", "f''(x)"])
    plt.title("Central Finite Differentiation")
    plt.show()
    
    print(120 * "=")
    
    
def backward_method(f, x, h=0.01):
    print(f"\nBackward Finite Differentiation:")
    print(120 * "=")

    x_i = x
    x_iminus1 = x_i - h
    
    first_derivative = (f(x_i) - f(x_iminus1) ) / h
    print(f"f'(x = {x}) = {first_derivative}")
    
    x_iminus2 = x_iminus1 - h
    
    second_derivative = (f(x_i) - 2 * f(x_iminus1) + f(x_iminus2) ) / h**2
    print(f"f''(x = {x}) = {second_derivative}")
    print(120 * "=")

    