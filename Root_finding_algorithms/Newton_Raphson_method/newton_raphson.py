def newton_raphson(f, x0, h: float = 1e-5, max_iter:int = 1000, tol:float = 1e-5) -> float:
    """ The Newton-Raphson method for finding roots of a function.
    Args:
        f : A function whose derivative is required
        x0(float) : The initial guess for the root. 
            NOTE: This is a very important parameter and 
                 can affect the convergence of the algorithm
        h(float) : Step size for calculating the derivative
        max_iter(int) : Maximum number of iterations
        tol(float) : Tolerance for convergence
    Returns:
        x : The estimated root of the function
    """
    # First we define the derivative function
    def df(f, x:float, h:float) -> float:
        """Calculate the derivative of a function f
        Args:
            f : The function to calculate the derivative of
            x(float) : The point at which to calculate the derivative
            h(float) : The step size to use
        Returns:
            (float): The derivative at point x"""
        return (f(x + h) - f(x - h))/(2 * h) # The central difference formula

    # Algorithm starts iteratively
    for _ in range(max_iter):
        x_new : float = x0 - f(x0)/df(f, x0, h)  # The Newton-Raphson step

        if (abs(x_new - x0) < tol) or (abs(f(x_new)) < tol):  # Stopping condition
            """we implemented two stopping conditions
            1. If the difference between the new and old estimate is less than the tolerance
            2. If the function evaluated at the new estimate is less than the tolerance
            this increases the robustness of the algorithm. The second condition prevents
            the algorithm from oscillating around the root."""
            return x_new  # Return the estimate
        x0 = x_new  # Update the guess

    # If max_iters are exhausted, raise an error
    raise ValueError(f"Could not converge to root in {max_iter} iterations. Last estimate is {x0}")


