

# 2x^2 - 5x + 3 = 0
def root_finding_method_1():
    print("\nExample 1")
    print(80 * "=")
    # Initial value
    x_0 = 0;
    counter = 0

    x = x_0
    while True:
        counter += 1
        x_new = (2 * x**2 + 3) / 5
        if abs(x_new - x) < 0.000001:
            print(f"Root solution of the equation 2*x^2 - 5*x + 3 = 0 is x = {round(x_new, 5)}. \nIt took {counter} iterations.")
            break
        
        x = x_new
        
    print(80 * "=" + "\n")

    