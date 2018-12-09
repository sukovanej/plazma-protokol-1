from collections import deque
import numpy as np

def inv_matrix(m):
    """
    I didnt like the original implementation. Since the np.linalg.inv function is
    raising an exception is it IMHO better to handle the errors with try-except block
    rather then by if-else block.
    """
    try:
        return np.linalg.inv(m)
    except np.linalg.LinAlgError as e:
        return e

print(inv_matrix(np.array([[0, 0], [0, 0]])))
print(inv_matrix(np.array([[1, 0], [0, 1], [1, 1]])))

"""
result:
    Singular matrix
    Last 2 dimensions of the array must be square
"""

def _inv_matrix(m):
    if np.linalg.matrix_rank(m) > 10:
        return "Rank of the matrix is greater then 10"

    try:
        return np.linalg.inv(m)
    except np.linalg.LinAlgError as e:
        return e


def rotate(l, n):
    """helper function for generating independent rows of the matrix"""

    d = deque(l)
    d.rotate(n)
    return d


regular_matrix = [rotate(range(0, 11), value) for value in range(0, 11)]

print(_inv_matrix(np.array(regular_matrix)))

"""
result:
    Rank of the matrix is greater then 10
"""
