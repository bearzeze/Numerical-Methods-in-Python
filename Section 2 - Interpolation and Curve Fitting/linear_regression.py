import math
import numpy as np
import matplotlib.pyplot as plt

# Using loops
def method_1(x, y):
    
    n = len(x)
    
    y_avg = 0
    x_avg = 0
    x_i_squared = 0
    x_i_y_i = 0
    y_i = 0
    x_i = 0
    for i in range(n):
        y_avg += y[i]
        x_avg += x[i]
        x_i_squared += x[i]**2
        x_i += x[i]
        y_i += y[i]
        x_i_y_i += x[i] * y[i]
        
    y_avg /= n
    x_avg /= n
    
    a = (y_avg * x_i_squared - x_avg * x_i_y_i) / (x_i_squared - n * x_avg**2)
    b = (x_i_y_i - x_avg * y_i) / (x_i_squared - n * x_avg**2)
    
    a = round(a, 4)
    b = round(b, 4)
    
    right_side = f"+ {b}"
    if b < 0:
        right_side = f"- {abs(b)}"
    elif b == 0:
        right_side = ""
    
    print(f"Linear approximation for the given data is described by formula: \ny = {a}*x {right_side}")
    
# Using numpy
def method_2(x, y):
    n = len(x)
    
    x = np.array(x, float)
    y = np.array(y, float)
    
    x_avg = np.mean(x)
    y_avg = np.mean(y)
    x_i_squared = np.sum(x**2)
    x_i_y_i = np.sum(x*y)
    x_i = np.sum(x)
    y_i = np.sum(y)
    
    a = (y_avg * x_i_squared - x_avg * x_i_y_i) / (x_i_squared - n * x_avg**2)
    b = (x_i_y_i - x_avg * y_i) / (x_i_squared - n * x_avg**2)
    
    a = round(a, 4)
    b = round(b, 4)
    
    right_side = f"+ {b}x"
    if b < 0:
        right_side = f"- {abs(b)}"
    elif b == 0:
        right_side = ""
    
    print(f"Linear approximation for the given data is described by formula: \ny = {a} {right_side}")
    
    linear_approx_plot(x, y, a, b)
    

def linear_approx_plot(x, y, a, b):
    plt.plot(x, y, 'bo')
    
    y_approx = a + b * x
    plt.plot(x,y_approx, 'r-', linewidth=2.0)
    plt.title(f"y = {a} + {b}x")
    plt.show()