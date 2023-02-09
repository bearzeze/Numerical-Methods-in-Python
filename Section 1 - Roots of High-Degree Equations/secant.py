import math

def root_finding_method(f, epsilon=1E-5):
    print("\nSecant Method")
    print(120 * "=")
    
    print("Input two initial values: ")
    x_1 = float(input("x_1 = "))
    x_2 = float(input("x_2 = "))
    counter = 0
    
    while True:
        counter += 1
        x_new = x_2 - (x_2 - x_1) / (f(x_2) - f(x_1)) * f(x_2)
        
        if abs(f(x_new)) < epsilon:
            print(f"\nRoot solution of the equation f(x) = 0 is x = {x_new} \nIt took {counter} iterations.")
            break
        else:
            x_1 = x_2
            x_2 = x_new
            
        if counter > 1E6:
            print(f"No roots of the equation f(x) = 0 between the initial values x1 = {x_1} and x2 = {x_2}")
            
    print(120 * "=")