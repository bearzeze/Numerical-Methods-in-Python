def method(f, x0, xn, y0, yn, n=50):
    print(f"\nDouble Integration:")
    print(120 * "=")
    
    nx = 10
    ny = 10
    
    hx = (xn - x0) / nx
    hy = (yn - y0) / ny
    
    I = 0
    for i in range(0, ny + 1):
        yi = y0 + i * hy
        
        if i in [0, ny]:
            coeff_x = 1
            
        elif i % 2 != 0:
            coeff_x = 4
            
        else:
            coeff_x = 2
            
        for j in range (0, nx + 1):
            xj = x0 + j * hx
            
            if j in [0, nx]:
                coeff_y = 1
                
            elif j % 2 != 0:
                coeff_y = 4
                
            else:
                coeff_y = 2
        
            I += coeff_x * coeff_y * f(xj, yi)
    
    I *= hx / 3 * hy / 3
    
    print(f"I = {I}")
    print(120 * "=")
    