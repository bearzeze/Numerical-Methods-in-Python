def method(f, x0, xn, n=100):
    print(f"\nTrapezodial Rule of Integration:")
    print(120 * "=")
    
    # Number of strips    
    n = 100
    # Step
    h = (xn - x0) / n
    
    # Bounding value of intervals
    a = x0
    b = xn
    
    # Area
    I = 1/2 * (f(a) + f(b))
    
    # from second to second-to last element
    for i in range(1, n):
        I += f(a + i * h)
    
    I *= h
    
    print(f"I = {I}")
    
    print(120 * "=")
    
    
    
    