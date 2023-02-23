from scipy.integrate import quad, dblquad, nquad

def integration(f, x0, xn):
    print("\nPython Built-in Methods")
    print(120 * "=")
    
    I = quad(f, x0, xn)
    print(f"I = {I[0]}, error = {I[1]}")
    
    print(120 * "=")
    

def double_integration(f, x0, xn, y0, yn, n=50):
    print("\nPython Built-in Methods")
    print(120 * "=")
    
    I = dblquad(f, x0, xn, lambda y:y0, lambda y:yn)
    print(f"I = {I[0]}, error = {I[1]}")
    print(120 * "=")