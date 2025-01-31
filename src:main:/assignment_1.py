import numpy as np  # Import numpy for advanced mathematical functions

# Approximation algorithm using iteration formula
def compute_square_root(x0, tol=0.000001):
    iter = 0
    diff = x0
    X = x0

    print(f"{iter} : {X}")

    while diff >= tol:
        iter += 1
        y = X

        X = (X / 2) + (1 / X)
        print(f"{iter} : {X}")
        diff = abs(X - y)

    print(f"\nConvergence after {iter} iterations")
    return X


# Bisection method utilizing intermediate value theorem
def bisection_method(f, a, b, tol, max_iterations):
    if f(a) * f(b) >= 0:
        raise ValueError("Function values at a and b must have opposite signs.")

    no_iterations = 0

    while abs(b - a) > tol and no_iterations < max_iterations:
        no_iterations += 1  # Counts number of times while loop loops
        new_pt = (a + b) / 2

        if f(a) * f(new_pt) < 0:  # Check if new point is negative or positive to assign upper(b) and lower bound(a).
            b = new_pt
        else:
            a = new_pt

    if abs(b - a) <= tol:
        print(f"Success: Root found at {new_pt} after {no_iterations} iterations.")
        return new_pt
    else:
        print("FAILURE: Maximum number of iterations reached.")
        return None


# Fixed point iteration based on fixed point theorem
def fixed_point_iteration(g, p0, TOL, N0):
    i = 1
    while i <= N0:
        p = g(p0)
        if abs(p - p0) < TOL:
            print(f"SUCCESS: Fixed point is {p} (found in {i} iterations)")
            return p
        i += 1
        p0 = p
    print("FAILURE: Maximum number of iterations reached")
    return None


# Newton-Raphson method
def newton_raphson(f, df, p0, TOL, N0):
    i = 1
    while i <= N0:
        f_p0 = f(p0)
        df_p0 = df(p0)

        if df_p0 == 0:
            print("FAILURE: Derivative is zero. No solution found.")  # Would not work based on the formula this method uses
            return None

        p = p0 - f_p0 / df_p0
        if abs(p - p0) < TOL:
            print(f"SUCCESS: Root is {p} (found in {i} iterations)")
            return p
        i += 1
        p0 = p  # Update initial approximation after each iteration
    print("FAILURE: Maximum number of iterations reached")
    return None


def main():
    print("This program helps you solve mathematical problems using different algorithms.")

    while True:
        # Display menu
        print("\nPlease choose an algorithm:")
        print("1. Compute Square Root (Approximation Algorithm)")
        print("2. Find Root of a Function (Bisection Method)")
        print("3. Find Fixed Point of a Function (Fixed-Point Iteration)")
        print("4. Find Root of a Function (Newton-Raphson Method)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            # Approximation Algorithm (Compute Square Root)
            print("\nYou selected the Approximation Algorithm.")
            x0 = float(input("Enter the initial approximation (x0): "))
            result = compute_square_root(x0)
            print(f"The computed square root of 2 is: {result}")

        elif choice == "2":
            # Bisection Method
            print("\nYou selected the Bisection Method.")
            user_function = input("Enter f(x): ")
            a = float(input("Enter the left endpoint (a): "))
            b = float(input("Enter the right endpoint (b): "))
            tol = float(input("Enter the error tolerance (tol): "))
            max_iterations = int(input("Enter the maximum number of iterations: "))

            # Define the function f(x) using numpy
            def f(x):
                return eval(user_function, {"x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan,
                                           "exp": np.exp, "log": np.log, "sqrt": np.sqrt})

            try:
                root = bisection_method(f, a, b, tol, max_iterations)
                if root is not None:
                    print(f"The approximate root is: {root}")
            except ValueError as e:
                print(e)

        elif choice == "3":
            # Fixed-Point Iteration
            print("\nYou selected Fixed-Point Iteration.")
            user_function = input("Enter g(x): ")
            p0 = float(input("Enter the initial approximation (p0): "))
            TOL = float(input("Enter the error tolerance (TOL): "))
            N0 = int(input("Enter the maximum number of iterations (N0): "))

            # Define the function g(x) using numpy
            def g(x):
                return eval(user_function, {"x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan,
                                           "exp": np.exp, "log": np.log, "sqrt": np.sqrt})

            result = fixed_point_iteration(g, p0, TOL, N0)
            if result is not None:
                print(f"Fixed point found: {result}")

        elif choice == "4":
            # Newton-Raphson Method
            print("\nYou selected the Newton-Raphson Method.")
            user_function = input("Enter f(x): ")
            derivative_function = input("Enter f'(x): ")
            p0 = float(input("Enter the initial approximation (p0): "))
            TOL = float(input("Enter the error tolerance (TOL): "))
            N0 = int(input("Enter the maximum number of iterations (N0): "))

            # Define the function f(x) and its derivative f'(x) using numpy
            def f(x):
                return eval(user_function, {"x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan,
                                           "exp": np.exp, "log": np.log, "sqrt": np.sqrt})

            def df(x):
                return eval(derivative_function, {"x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan,
                                                 "exp": np.exp, "log": np.log, "sqrt": np.sqrt})

            result = newton_raphson(f, df, p0, TOL, N0)
            if result is not None:
                print(f"Root found: {result}")

        elif choice == "5":
            print("Exiting program.")
            break  # Exit the loop

        else:
            print("Invalid choice. Please select a number from 1 to 5.")


# Run the program
if __name__ == "__main__":
    main()
