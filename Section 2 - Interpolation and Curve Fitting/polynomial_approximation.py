import numpy as np
import matplotlib.pyplot as plt


def method(x, y):
    m = len(x)
    
    x = np.array(x, float)
    y = np.array(y, float)
    
    n = int(input("Enter degree of polynomial curve fitting: "))
    
    A = np.zeros((n + 1, n + 1))
    b = np.zeros((n + 1, 1))
    
    for i in range(len(A)):
        for j in range(len(A)):
            
            if i == j and i == 0:
                A[0, 0] = m
                continue
            
            A[i, j] = np.sum(x**(i + j))
        
        b[i] = np.sum(x**i * y)


    # Now A * a = b, can be applied to get a vector of coefficients
    a = np.linalg.solve(A, b)
    a = np.round(a, 7)
    
    print("T\nhe polynomial which is used for curve fitting is:",)
    function_str = "f(x) = "
    for i in range(len(a)):
        
        if round(a[i, 0], 3) == 0:
            continue
        
        # First coeff is without x
        if i == 0:
           function_str += f"{round(a[0, 0], 3)}"
           continue
        
        # Positive coeff
        if a[i] > 0:
            function_str += f" + {round(a[i, 0], 3)}"
        
        # Negative coeff
        else:
            function_str += f" - {abs(round(a[i, 0], 3))}"
            
        if i == 1:
            function_str += " * x"
        else:
            function_str += f" * x ^ {i}"
            
    print(f"{function_str}\n")
    
    plotting(a, function_str, x, y)


def plotting(coeff, function_str, x_data, y_data):
    plt.plot(x_data, y_data, 'bo')
    
    x_approx = np.c_[x_data]
    y_approx = np.zeros((len(x_data), 1))
    
    for i, x in enumerate(x_approx):
        y_approx[i] = np.sum(coeff * np.c_[x ** np.arange(coeff.shape[0])])
    
    print(y_approx)
        
    
    plt.plot(x_approx, y_approx, 'r-', linewidth=2.0)
    plt.title(f"{function_str}")
    plt.grid()
    plt.show()