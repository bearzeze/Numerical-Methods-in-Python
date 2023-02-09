import math

# Example 1:
def root_finding_method(f, epsilon=1E-5):
    
    print("\nBisection Method")
    print(120 * "=")
    
    print("Input two initial values: ")
    x_01 = float(input("x_1 = "))
    x_02 = float(input("x_2 = "))
    
    x_left = x_01
    x_right =  x_02
    counter = 0
    
    while True:
        x_mid = (x_right + x_left) / 2
        
        f_left = f(x_left)
        f_right = f(x_right)
        f_mid = f(x_mid)
        
        counter += 1
        
        if abs(f_mid) < epsilon:
            print(f"\nRoot solution of the equation f(x) = 0 is x = {x_mid} \nIt took {counter} iterations.")
            break   
         
        elif f_left * f_mid < 0:
            x_right = x_mid
            
        elif f_mid *  f_right< 0:
            x_left = x_mid
        
        else:
            print(f"No roots (or there are even roots) of the equation f(x) = 0 between the initial values x1 = {x_01} and x2 = {x_02}")
            while True:
                choice = input("Do you want to try with new values? [Y/N]  ")
                if choice.lower() in ["yes", "y"]:
                    root_finding_method(f)
                    return None
                elif choice.lower() in ["no", "n"]:
                    break
            break     
                     
    print(120 * "=")

