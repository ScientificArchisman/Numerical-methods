from typing import List, Tuple, Union


def newton_forward_interpolation(x: List[Union[int, float]], y: List[Union[int, float]],
                                 target: Union[int, float]) -> Tuple[int, List[Union[int, float]]]:
    """
    Find the Newton polynomial through the points (x, y) and return its value at target.
    Args:
        x: The x-coordinates of the points.
            NOTE: The points must be equally spaced.
        y: The y-coordinates of the points.
        target: The points to evaluate the polynomial at.
    Returns:
        result(int, float): The value of the Newton polynomial through (x, y) evaluated at target.
        coefficients(List[Union[int, float]]): The coefficients of the Newton polynomial.
    """

    # Check that the input arrays have the same length
    if len(x) != len(y):
        raise ValueError("The arrays x and y must have the same length.")

    if target > x[-1] or target < x[0]:
        raise ValueError("The point t must be in the interval [x_0, x_n].")

    # Check for equally space data points
    h: float = x[1] - x[0]
    for i in range(1, len(x) - 1):
        if x[i + 1] - x[i] != h:
            raise ValueError("The points must be equally spaced.")

    # Initialize the polynomial
    coefficients = y.copy()  # The coefficients of the polynomial

    # Loop over the differences
    for i in range(1, len(x)):
        # Update the polynomial
        # Note that the coefficients are overwritten
        for j in range(len(x) - i):
            # Compute the jth coefficient
            coefficients[j] = (coefficients[j + 1] - coefficients[j]) / (i * h)

    # Evaluate the polynomial at t
    result = coefficients[0]
    cumulative_product = 1  # The product term (x - x_0)(x - x_1)...(x - x_n)
    for i in range(1, len(x)):
        cumulative_product *= (target - x[i - 1])  # Update the product term
        result += coefficients[i] * cumulative_product  # Update the result
    return result, coefficients
