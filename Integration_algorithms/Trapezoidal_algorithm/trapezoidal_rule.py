from typing import Callable, Union
import numpy as np


def trapezoidal_integration(f: Callable[[Union[np.ndarray, float]], Union[np.ndarray, float]],
                            lower_lim: float, upper_lim: float, divisions: int) -> float:
    """
    Perform trapezoidal integration on a function f
    Args:
        f (Callable[[float], float]): Function to be integrated, taking a single float and returning a float.
        lower_lim (float): Lower limit of integration.
        upper_lim (float): Upper limit of integration.
        divisions (int): Number of divisions to use in integration.
    Returns:
        float: Integral of f from lower_lim to upper_lim.
    Raises:
        ValueError: If divisions is not a positive integer or if upper_lim is not greater than lower_lim.
    """
    if divisions <= 0:
        raise ValueError("Number of divisions must be a positive integer.")
    if upper_lim <= lower_lim:
        raise ValueError("Upper limit must be greater than lower limit.")

    h = (upper_lim - lower_lim) / divisions
    x_points: np.ndarray = np.linspace(lower_lim + h, upper_lim - h, divisions - 1)
    integral = (f(lower_lim) + f(upper_lim)) / 2 + np.sum(f(x_points))

    return integral * h

