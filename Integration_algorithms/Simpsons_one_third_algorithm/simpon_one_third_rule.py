from typing import Callable, Union
import numpy as np


def simpsons_one_third(f: Callable[[Union[float, np.ndarray]], Union[float, np.ndarray]],
                       lower_lim: float, upper_lim: float, n: int) -> float:
    """
    Approximates the integral of f from a to b using Simpson's 1/3 rule.

    Parameters
    ----------
    f : Callable[Union[float, np.ndarray], Union[float, np.ndarray]]
        The function to integrate.
    lower_lim : float
        The lower limit of integration.
    upper_lim : float
        The upper limit of integration.
    n : int
        The number of sub-intervals to use in the approximation.

    Returns
    -------
    float
        The approximate value of the integral.

    Raises
    ------
    ValueError
        If n is odd or lower_lim >= upper_lim.
    """
    if n % 2 != 0:
        raise ValueError("n (Number of sub-intervals) must be even")
    if lower_lim >= upper_lim:
        raise ValueError("Lower limit must be less than upper limit")

    # Calculate the width of each sub-interval
    h: float = (upper_lim - lower_lim) / n

    x_values = np.linspace(lower_lim, upper_lim, n+1)  # Array of x-values

    odd_sum = np.sum(f(x_values[1:n:2]))  # Sum of f(x) for odd indices
    even_sum = np.sum(f(x_values[2:n-1:2]))  # Sum of f(x) for even indices

    # Initialise and return final answer
    integral: float = f(lower_lim) + f(upper_lim) + 4 * odd_sum + 2 * even_sum
    return h / 3 * integral  # Multiply by h/3


