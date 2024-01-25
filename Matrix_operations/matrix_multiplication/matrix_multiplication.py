from typing import List, Union

def matrix_multiply(matrix1 : List[List[Union[int, float]]], matrix2 : List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """ Multiplies two matrices together.
    Args:
        matrix1 (List[List[Union[int, float]]]): The first matrix.
        matrix2 (List[List[Union[int, float]]]): The second matrix.
    Returns:
        List[List[Union[int, float]]]: The product of the two matrices.
    Raises:
        ValueError: If the number of columns in the first matrix is not equal to the number of rows in the second matrix.
        ValueError: If the first matrix is not a rectangular matrix.
        ValueError: If the second matrix is not a rectangular matrix."""
    m1_rows, m1_cols = len(matrix1), len(matrix1[0])
    m2_rows, m2_cols = len(matrix2), len(matrix2[0]) 

    if m1_cols != m2_rows:
        raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    
    for row in matrix1:
        if len(row) != m1_cols:
            raise ValueError("The first matrix must be a rectangular matrix.")
    
    for row in matrix2:
        if len(row) != m2_cols:
            raise ValueError("The second matrix must be a rectangular matrix.")
    
    product = [[0 for _ in range(m2_cols)] for _ in range(m1_rows)]
    for m1_row in range(m1_rows):
        for m2_col in range(m2_cols):
            for m2_row in range(m2_rows):
                product[m1_row][m2_col] += matrix1[m1_row][m2_row] * matrix2[m2_row][m2_col]
    return product


