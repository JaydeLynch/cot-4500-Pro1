
import pytest
from src.main.assignment_1 import compute_square_root, bisection_method, fixed_point_iteration, newton_raphson

# Test cases for compute_square_root
def test_compute_square_root():
    # Test square root of 2
    result = compute_square_root(1.0)
    assert abs(result - 1.414213) < 0.000001  # Check if result is close to sqrt(2)

    # Test square root of 4
    result = compute_square_root(2.0)
    assert abs(result - 2.0) < 0.000001  # Check if result is close to sqrt(4)


# Test cases for bisection_method
def test_bisection_method():
    # Define a simple function: f(x) = x^2 - 4
    def f(x):
        return x**2 - 4

    # Test root finding for f(x) = x^2 - 4 in [1, 3]
    result = bisection_method(f, 1.0, 3.0, 0.000001, 100)
    assert abs(result - 2.0) < 0.000001  # Root should be close to 2.0


# Test cases for fixed_point_iteration
def test_fixed_point_iteration():
    # Define a simple function: g(x) = (x + 2/x) / 2
    def g(x):
        return (x + 2 / x) / 2

    # Test fixed point iteration for g(x)
    result = fixed_point_iteration(g, 1.0, 0.000001, 100)
    assert abs(result - 1.414213) < 0.000001  # Fixed point should be close to sqrt(2)


# Test cases for newton_raphson
def test_newton_raphson():
    # Define a simple function: f(x) = x^2 - 4
    def f(x):
        return x**2 - 4

    # Define its derivative: f'(x) = 2x
    def df(x):
        return 2 * x

    # Test Newton-Raphson for f(x) = x^2 - 4
    result = newton_raphson(f, df, 3.0, 0.000001, 100)
    assert abs(result - 2.0) < 0.000001  # Root should be close to 2.0


# Run tests
if __name__ == "__main__":
    pytest.main()
