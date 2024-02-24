import numpy as np 

# Factorise a matrix into L and U
def factorise_LU(matrix: np.ndarray) -> np.ndarray:
    """Factorise a matrix into L and U
    Args:
        matrix(np.ndarray): The matrix to factorise
    Returns:
        (np.ndarray): The lower triangular matrix and the upper triangular matrix"""
    n = matrix.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(n):
        L[i, i] = 1
        for j in range(i, n):
            U[i, j] = matrix[i, j] - np.sum(L[i, :i] * U[:i, j])
        for j in range(i + 1, n):
            L[j, i] = (matrix[j, i] - np.sum(L[j, :i] * U[:i, i])) / U[i, i]
    return L, U