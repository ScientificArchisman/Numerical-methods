from typing import List, Union
from copy import deepcopy as deep

# First we need to define a function that adds two matrices together.
def matrix_add(matrix1 : List[List[Union[int, float]]], matrix2 : List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """ Multiplies two matrices together.
    Args:
        matrix1 (List[List[Union[int, float]]]): The first matrix.
        matrix2 (List[List[Union[int, float]]]): The second matrix.
    Returns:
        List[List[Union[int, float]]]: The sum of the two matrices.
    Raises:
        ValueError: If the dimensions of the two matrices are not equal.
        ValueError: If the first matrix is not a rectangular matrix.
        ValueError: If the second matrix is not a rectangular matrix."""
    
    m1_rows, m1_cols = len(matrix1), len(matrix1[0])
    m2_rows, m2_cols = len(matrix2), len(matrix2[0])

    if m1_rows != m2_rows or m1_cols != m2_cols:
        raise ValueError("The dimensions of the two matrices must be equal.")
    
    for row in matrix1:
        if len(row) != m1_cols:
            raise ValueError("The first matrix must be a rectangular matrix.")
        
    for row in matrix2:
        if len(row) != m2_cols:
            raise ValueError("The second matrix must be a rectangular matrix.")

    result = deep(matrix1)
    for row in range(m1_rows):
        for col in range(m1_cols):
            result[row][col] += matrix2[row][col]
    return result


# Now we can define the divide and conquer matrix multiplication function.
def DC_matrix_mul(matrix1: List[List[Union[int, float]]], matrix2: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """ Multiply matrices using the divide and conquer method. 
    Works for matrices of size 2^n x 2^n.
    Args:
        matrix1 (List[List[Union[int, float]]]): The first matrix.
        matrix2 (List[List[Union[int, float]]]): The second matrix.
    Returns:
        List[List[Union[int, float]]]: The product of the two matrices.
    Raises:
        ValueError: If the dimensions of the two matrices are not equal.
        ValueError: If the first matrix is not a rectangular matrix.
        ValueError: If the second matrix is not a rectangular matrix."""
    m1_rows, m1_cols = len(matrix1), len(matrix1[0])
    m2_rows, m2_cols = len(matrix2), len(matrix2[0])

    # Check if the matrices have shapes which are a power of 2.
    def is_power_of_2(n):
        return (n != 0) and (n & (n - 1) == 0)
    
    if not all(is_power_of_2(x) for x in [m1_rows, m1_cols, m2_rows, m2_cols]):
        raise ValueError("The dimensions of the matrices must be a power of 2.")
    if m1_cols != m2_rows or m1_rows != m1_cols or m2_rows != m2_cols:
        raise ValueError("Matrices must be square and dimensions must match.")
    
    # Base case
    if m1_rows == 1:
        return [[matrix1[0][0] * matrix2[0][0]]]
    
    # Split matrices into quarters
    def split(X):
        """ Split matrix into quarters."""
        return [
            [X[i][:len(X)//2] for i in range(len(X)//2)],
            [X[i][len(X)//2:] for i in range(len(X)//2)],
            [X[i][:len(X)//2] for i in range(len(X)//2, len(X))],
            [X[i][len(X)//2:] for i in range(len(X)//2, len(X))]
        ]
    # Split matrices into quarters
    a11, a12, a21, a22 = split(matrix1)
    b11, b12, b21, b22 = split(matrix2)

    # Recursive calls for submatrices
    c11 = matrix_add(DC_matrix_mul(a11, b11), DC_matrix_mul(a12, b21))
    c12 = matrix_add(DC_matrix_mul(a11, b12), DC_matrix_mul(a12, b22))
    c21 = matrix_add(DC_matrix_mul(a21, b11), DC_matrix_mul(a22, b21))
    c22 = matrix_add(DC_matrix_mul(a21, b12), DC_matrix_mul(a22, b22))

    # Combine subproducts
    top = [c11[i] + c12[i] for i in range(len(c11))]
    bottom = [c21[i] + c22[i] for i in range(len(c21))]
    # each row in top and bottom is a list, so we need to add them together
    return top + bottom