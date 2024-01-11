#!/usr/bin/python3
"""
Function to multiply two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices

    Args:
        m_a (list of lists): First matrix
        m_b (list of lists): Second matrix

    Returns:
        list of lists: Resulting matrix after multiplication

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists
                   If an element in the matrices is not an integer or a float
                   If m_a or m_b is not a rectangle
        ValueError: If m_a or m_b is empty or can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    if any(not isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    rows_a, cols_a = len(m_a), len(m_a[0])
    rows_b, cols_b = len(m_b), len(m_b[0])

    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
