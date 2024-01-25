from typing import List, Union
from copy import deepcopy as deep
import sys
from pathlib import Path

current_dir = Path().resolve()
subdir_add = current_dir / "Matrix_operations" / "matrix_addition"
subdir_sub = current_dir / "Matrix_operations" / "matrix_subtraction"

# Add subfolder to sys.path
if str(subdir_add) not in sys.path:
    sys.path.append(str(subdir_add))

if str(subdir_sub) not in sys.path:
    sys.path.append(str(subdir_sub))

# Import modules from matrix subfolders
from matrix_addition import matrix_add
from matrix_subtraction import matrix_subtract


def Strassen_multiply(matrix1: List[List[Union[int, float]]], matrix2: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
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

    P = Strassen_multiply(matrix_add(a11, a22), matrix_add(b11, b22))
    Q = Strassen_multiply(matrix_add(a21, a22), b11)
    R = Strassen_multiply(a11, matrix_subtract(b12, b22))
    S = Strassen_multiply(a22, matrix_subtract(b21, b11))
    T = Strassen_multiply(matrix_add(a11, a12), b22)
    U = Strassen_multiply(matrix_subtract(a21, a11), matrix_add(b11, b12))
    V = Strassen_multiply(matrix_subtract(a12, a22), matrix_add(b21, b22))

    # Combine submatrices into 4 quadrants of the result matrix
    C11 = matrix_add(matrix_subtract(matrix_add(P, S), T), V)
    C12 = matrix_add(R, T)
    C21 = matrix_add(Q, S)
    c22 = matrix_add(matrix_subtract(matrix_add(P, R), Q), U)

    # Combine submatrices into one result matrix
    top = [C11[i] + C12[i] for i in range(len(C11))]
    bottom = [C21[i] + c22[i] for i in range(len(C21))]
    return top + bottom


if __name__ == "__main__":
    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [5, 6, 7, 8]]
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [5, 6, 7, 8]]

    print(Strassen_multiply(matrix1, matrix2))