

def method(f, x0, xn, n=100):
    print(f"\nSimpson 1/3 Rule of Integration:")
    print(120 * "=")
    
    h = (xn - x0) / (2*n)
    
    a = x0
    b = xn
    
    I = 0
    
    for i in range(0, 2*n + 1):
        xi = a + i * h
        
        if i in [0, 2*n]:
            I += f(xi)
        elif i % 2 == 0:
            I += 2 * f(xi)
        else:
            I += 4 * f(xi)
    
    I *= h / 3
    print(f"I = {I}")
    
    print(120 * "=")
    