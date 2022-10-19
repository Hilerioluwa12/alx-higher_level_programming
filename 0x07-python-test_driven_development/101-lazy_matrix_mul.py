#!/usr/bin/pythonn3
"""
Function that return the multiplication of two matrices
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Args
       m_a: matrix
       m_b: matrix

    Return
       the multiplication of the two matrices
    """
    import numpy as np

    return(np.matmul(m_a, m_b))
