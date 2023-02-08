import math

# 2x^2 - 5x + 3 = 0
def root_finding_method_1():
    print("\nNewton-Raphson Method")
    print(80 * "=")
    # Initial value
    x_0 = 78423;
    counter = 0
    
    x = x_0
    while True:
        counter += 1
        # Function value in that point
        f_x = 2 * x**2 - 5 * x + 3
        
        # First derivative
        f_x_derivative = 4 * x - 5
        
        x_new = x - f_x / f_x_derivative
        if abs(x_new - x) < 0.000001:
            print(f"Root solution of the equation 2*x^2 - 5*x + 3 = 0 is x = {round(x_new, 5)} \nIt took {counter} iterations.")
            break
        
        x = x_new
        
    print(80 * "=" + "\n")
    
    

# x^2 + cos^2(x) - 4x = 0
def root_finding_method_2():
    print("\nExample 2")
    print(80 * "=")
    # Initial value
    x_0 = 2;
    counter = 0
    
    x = x_0
    while True:
        counter += 1
        
        # Function value in that point
        f_x = x**2 +  math.cos(x)**2 - 4 * x
        
        # First derivative
        f_x_derivative = 2 * x - 2 * math.cos(x) * math.sin(x) - 4
        
        x_new = x - f_x / f_x_derivative
        if abs(x_new - x) < 0.000001:
            print(f"Root solution of the equation x**2 +  cos(x)**2 - 4 * x = 0 is x = {round(x_new, 5)} \nIt took {counter} iterations.")
            break
        
        x = x_new
    print(80 * "=" + "\n")
    
    