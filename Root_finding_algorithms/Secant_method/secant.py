def secant(f, x0: float, x1: float, tol: float = 1e-5, maxiter: int = 1000, 
           shift_factor: float = 0.01, vertical_case_threshold: float = 1e-12) -> float:
    """Uses the secant method to find a root of f.
    Parameters:
        f: The function to find a root of.
        x0, x1: The initial points.
        NOTE: x0 and x1 are important. If they are not chosen
        correctly, the secant method will not converge.
        tol: The tolerance for the stopping criterion. Default is 1e-5.
        maxiter: The maximum number of iterations. Default is 1000.
        shift_factor: The factor to shift x1 by when the secant line is vertical.
        vertical_case_threshold: The threshold for the difference between f(x1) and f(x0) to be considered vertical.
    Returns:
        (float) : The approximate root."""
    for _ in range(maxiter):
        """Check for the stopping criterion.
        We use both the difference and the function value because
        sometimes the difference is close to zero even when the
        function value is zero."""
        f_x1 : float = f(x1) # Store the function value for x1 for efficiency.
        f_x0 : float = f(x0) # Store the function value for x0 for efficiency.
        if abs(x1 - x0) < tol or abs(f_x1) < tol:
            return x1 # Stopping criterion met.
        # Handle the case where the secant line is vertical.
        # This is done by shifting x1 by a factor of shift_factor of the distance between x1 and x0.
        if abs(f_x1 - f_x0) < vertical_case_threshold:
            x1 = x1 + shift_factor * (x1 - x0)
            continue
        # Use the secant method formula to update x1.
        x1, x0 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0), x1

    raise ValueError(f"Secant method failed to converge after {maxiter} iterations. Last found value is {x1}")