from typing import List, Union


def tensor_product(matrix1: List[List[Union[int, float]]], matrix2: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """ Calculate the tensor m2_rowsroduct of two matrices
    Args:
        matrix1 (List[List[Union[int, float]]]): The first matrix.
        matrix2 (List[List[Union[int, float]]]): The second matrix.
    Returns:
        List[List[Union[int, float]]]: The tensor m2_rowsroduct of the two matrices."""
    # Get the dimensions of matrices A and B
    m1_rows, m1_cols = len(matrix1), len(matrix1[0])
    m2_rows, m2_cols = len(matrix2), len(matrix2[0])

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(m1_cols * m2_cols)] for _ in range(m1_rows * m2_rows)]

    # Calculate the tensor m2_rowsroduct
    for i in range(m1_rows):
        for j in range(m1_cols):
            for k in range(m2_rows):
                for l in range(m2_cols):
                    result[i*m2_rows + k][j*m2_cols + l] = A[i][j] * B[k][l]

    return result