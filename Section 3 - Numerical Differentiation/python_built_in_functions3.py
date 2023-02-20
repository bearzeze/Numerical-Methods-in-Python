from scipy.misc import derivative
import numpy as np
import matplotlib.pyplot as plt


def central_derivative(f_ana, x, h=0.01,):
    print("\nPython Built-in Methods")
    print(120 * "=")
    
    dfc1 = derivative(func=f_ana, x0=x, dx=h, n=1)
    dfc2 = derivative(func=f_ana, x0=x, dx=h, n=2)

    # Plotting    
    plt.figure(1)
    plt.plot(x, f_ana(x),'k-', x, dfc1, 'b--', x, dfc2, 'r-.')
    plt.grid()
    plt.legend(["f(x)", "f'(x)", "f''(x)"])
    plt.title("Central Finite Differentiation")
    plt.show()

    print(120 * "=")