from typing import List, Union
from copy import deepcopy as deep

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


if __name__ == "__main__":
    matrix1  = [[1, 2, 3], [4, 5, 6]]
    matrix2 = [[7, 8, 9], [10, 11, 12]]
    print(matrix_add(matrix1, matrix2))