#!/usr/bin/env python3
"""Calculates the correlation matrix"""

import numpy as np


def correlation(C):
    """
    Calculates the correlation matrix

    Parameters:
    d - number of dimensions
    C (numpy array): The covariance matrix of shape(d,d)

    Raises:
    TypeError: If C is not a numpy.ndarray
    ValueError: If C does not have shape(d, d)

    Returns:
    numpy.ndarray: The correlation matrix of shape(d, d)
    """

    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")
    d = C.shape[0]
    corr = np.zeros((d, d))
    for i in range(d):
        for j in range(d):
            corr[i, j] = C[i, j] / np.sqrt(C[i, i] * C[j, j])
    return corr
