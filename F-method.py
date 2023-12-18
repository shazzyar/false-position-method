def false_position_method(func, a, b, tol=1e-6, max_iter=100):
    """
    Solves for the root of a function using the false position method.

    Parameters:
    - func: The target function.
    - a, b: Initial interval [a, b] where the root is assumed to be.
    - tol: Tolerance for the convergence criterion.
    - max_iter: Maximum number of iterations.

    Returns:
    - root: Approximation of the root.
    - iter_count: Number of iterations performed.
    """
    iter_count = 0

    while iter_count < max_iter:
        # Calculate the function values at the endpoints of the interval
        fa = func(a)
        fb = func(b)

        # Calculate the new approximation using the false position formula
        c = (a * fb - b * fa) / (fb - fa)

        # Calculate the function value at the new approximation
        fc = func(c)

        # Check for convergence
        if abs(fc) < tol:
            return c, iter_count

        # Update the interval based on the sign of fc
        if fc * fa < 0:
            b = c
        else:
            a = c

        iter_count += 1

    # If the maximum number of iterations is reached without convergence
    raise ValueError("False position method did not converge within the maximum number of iterations.")

# Example usage:
def target_function(x):
    return x**3 - 6*x**2 + 11*x - 6

try:
    root, iterations = false_position_method(target_function, 0, 2)
    print(f"Root: {root}")
    print(f"Iterations: {iterations}")
except ValueError as e:
    print(e)