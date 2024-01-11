#!/usr/bin/python3
"""
Module to multiply two matrices using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy

    Args:
    - m_a: First matrix (list of lists)
    - m_b: Second matrix (list of lists)

    Returns:
    - Resulting matrix as a NumPy array
    """
    matrix_a = np.array(m_a)
    matrix_b = np.array(m_b)

    result = np.matmul(matrix_a, matrix_b)
    return result
