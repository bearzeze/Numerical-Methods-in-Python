from scipy.optimize import newton, bisect, root, fsolve

def newton_root_finding_method(f):
    print("\nPython Methods")
    print(120 * "=")
    
    print("Input initial value: ")
    x_0 = float(input("x_0 = "))
    
    roots = newton(f, x_0)
    print(f"\nRoot solution of the equation f(x) = 0 is/are x = {roots}.")

    print(120 * "=")
    
    
def fsolve_root_finding_method(f):
    print("\nPython Methods")
    print(120 * "=")
    
    print("Input initial values separated by comma only: ")
    numbers = [float(x) for x in input("x_0 = ").split(',')]
    
    roots = fsolve(f, numbers)
    print(f"\nRoot solution of the equation f(x) = 0 is/are x = {roots}.")

    print(120 * "=")
    
