def regular_falsi(f, lower_lim:float, upper_lim:float, n_iter: int = 1000, tol:float = 1e-6, 
                  verbose:bool = True, noise:float = 1e-8) -> float:
    """Find the root of a function using the regular falsi method.
    Args:
        f: Function to find the root of.
        lower_lim: Lower limit of the interval. The function has negative value at this point.
        upper_lim: Upper limit of the interval. The function has positive value at this point.
        n_iter: Maximum number of iterations. Defaults to 1000.
        tol: Tolerance of the solution. Defaults to 1e-6.
        verbose: If True, print the number of iterations and the root. Defaults to True.
        noise: Small value added to the false position to avoid division by zero. Defaults to 1e-8.
    Returns:
        The root of the function.
    """
    if f(lower_lim) * f(upper_lim) > 0:
        if f(lower_lim) == 0:
            return lower_lim # If the lower limit is a root, return it
        else:
            # If the function has the same sign at the limits, the root is not in the interval
            raise ValueError("The function must have opposite signs at the limits.")
    
    for iter in range(n_iter):
        # Calculate the false position
        ## Check if the denominator is zero
        false_position = lower_lim - (f(lower_lim) * (lower_lim - upper_lim)) / (f(lower_lim) - f(upper_lim))

        # Check if the root is found
        try:
            new_f = f(false_position)
        ## If the denominator is zero, add a small value to the false position to avoid division by zero
        except ZeroDivisionError:
            false_position += noise
            new_f = f(false_position)
        if abs(new_f) < tol:
            if verbose:
                print(f"Found root at {false_position} after {iter} iterations.")
            return false_position
        
        # Check if the sign of f(lower_lim) and f(false_position) are the same
        elif f(false_position) * f(lower_lim) < 0:
            upper_lim = false_position # if sign is different, the root is in the interval [lower_lim, false_position]
        else:
            lower_lim = false_position # if sign is the same, the root is in the interval [false_position, upper_lim]

    raise ValueError(f"Could not find root after {n_iter} iterations.")

