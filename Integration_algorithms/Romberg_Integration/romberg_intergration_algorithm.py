from typing import Callable
import numpy as np


def romberg_integration(f: Callable[[float], float], a: float, b: float,
                        tol=1e-6, max_iterations: int = 10) -> float:
    """
    Compute the integral of a function f over the interval [a, b] using Romberg Integration.

    Parameters:
    f (callable): The function to integrate. It must be a function of a single variable.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    tol (float): Tolerance for convergence. Default is 1e-6.
    max_iterations (int): Maximum number of iterations to perform. Default is 10.

    Returns:
    float: Approximated integral of the function f from a to b.

    Raises:
    ValueError: If the number of iterations exceeds the maximum limit.

    Notes:
    The function uses an adaptive approach, increasing the order of the Romberg table until
    the desired accuracy (tolerance) is achieved or the maximum number of iterations is reached.
    """

    # Initialize the Romberg table with zeros
    R = np.zeros((max_iterations, max_iterations), dtype=float)

    # First estimate with the Trapezoidal Rule (0th column of Romberg table)
    R[0, 0] = (f(a) + f(b)) * (b - a) / 2

    # Iterate to fill the Romberg table
    for i in range(1, max_iterations):
        # Trapezoidal Rule refinement
        h = (b - a) / (2 ** i)
        sum_f = np.sum(f(a + np.arange(1, 2 ** i, 2) * h))
        R[i, 0] = R[i - 1, 0] / 2 + h * sum_f

        # Richardson extrapolation
        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4 ** j - 1)

        # Check for convergence
        if i > 0 and abs(R[i, i] - R[i - 1, i - 1]) < tol:
            return R[i, i]

    # Raise an error if convergence not reached within max iterations
    raise ValueError("Romberg integration did not converge within the maximum number of iterations")