from scipy.interpolate import interp1d, lagrange
    
from scipy.stats import linregress
from scipy.optimize import curve_fit


def linear_interpolation_method(x, y):
    print("\nPython Built-in Methods")
    print(120 * "=")
    
    f = interp1d(x, y, 'quadratic')
    print(f(53))

    print(120 * "=")
        
    
def lagrange_interpolation_method(x, y):
    print("\nPython Built-in Methods")
    print(120 * "=")
    
    L = lagrange(x, y)
    print(L)
    print(L(50))

    print(120 * "=")
    

def linear_regression(x, y):
    print("\nPython Built-in Methods")
    print(120 * "=")
    
    result = linregress(x, y)
    print(f"y = {result.slope} * x + {result.intercept}")
    
    print(120 * "=")
    
    
def curve_fitting(f, x, y):
    print("\nPython Built-in Methods")
    print(120 * "=")
    
    a,b = curve_fit(f, x, y)
    print(a)
    
    print(120 * "=")

