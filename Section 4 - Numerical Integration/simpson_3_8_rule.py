

def method(f, x0, xn, n=100):
    print(f"\nSimpson 3/8 Rule of Integration:")
    print(120 * "=")
    n = 6
    
    h = (xn - x0) / (n)
    
    a = x0
    b = xn
    
    I = f(a) + f(b)
    
    for i in range(1, n, 3):
        I += 3 * (f(a + i * h) + f(a + (i + 1) * h))
    
    for i in range(3, n, 3): 
        I += 2 * f(a + i * h)
           
    I *= h * 3 / 8
    print(f"I = {I}")
    print(120 * "=")
    