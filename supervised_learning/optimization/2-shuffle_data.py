#!/usr/bin/env python3
"""
Function shuffles the data points in two matrices
"""


import numpy as np


def shuffle_data(X, Y):
    """
    Shuffles the data points in two matrices

    Args:
    X(numpy.ndarray): shape(m, nx)
        m: data points number
        nx: features number
    Y(numpy.ndarray): shape(m, ny)
        m: data points number
        ny: features number

    Returns:
    shuffled X and Y matrices
    """
    s = np.random.permutation(X.shape[0])
    return X[s], Y[s]
