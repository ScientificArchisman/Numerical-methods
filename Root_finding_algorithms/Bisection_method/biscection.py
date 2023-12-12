def bisection_method(f, lower_lim: float, high_lim: float, tolerance: float = 1e-8, iterations: int = 1000) -> float:
    """ This function implements the bisection method to find the root of
      a function f(x) in the interval [lower_lim, high_lim] with a 
      tolerance of tolerance.
    Args:
        f (function): The function for which we want to find the root.
        lower_lim (float): The lower limit of the interval.
        high_lim (float): The upper limit of the interval.
        tolerance (float, optional): The tolerance of the method. Defaults to 1e-8.
        iterations (int, optional): The maximum number of iterations. Defaults to 1000.
    Returns:
        float: The root of the function.
    Raises:
        ValueError: If the root is not in the interval.
        ValueError: If the maximum number of iterations was reached.
    """
    # Check if the root is in the interval
    if f(lower_lim) * f(high_lim) >= 0:
        raise ValueError("The root is not in the interval.")
      
    # Initialize the variables
    middle_val = (lower_lim + high_lim) / 2

    # Iterate until the root is found
    # We check for 3 conditions for robustness:
    # 1. The function value is smaller than the tolerance
    # 2. The maximum number of iterations was reached
    # 3. The lower limit is smaller than the upper limit
    while (abs(f(middle_val)) > tolerance) and (iterations > 0) and (lower_lim < high_lim):
        # Check if the root is in the left or right half of the interval
        if f(lower_lim) * f(middle_val) < 0:
            high_lim = middle_val  # Set the new upper limit
        else:
            lower_lim = middle_val  # f(lower_lim) * f(middle_val) > 0
        # Calculate the new middle value
        middle_val = (lower_lim + high_lim) / 2
        iterations -= 1  # Decrease the number of iterations
    if iterations == 0:
        raise ValueError("The maximum number of iterations was reached.")
    return middle_val