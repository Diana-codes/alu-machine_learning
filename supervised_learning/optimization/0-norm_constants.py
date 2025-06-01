#!/usr/bin/env python3
"""
Function calculates the normalization constants of a matrix
"""

import numpy as np


def normalization_constants(X):
    """
    Calculates the normalization constants of a matrix

    Args:
    X(numpy.ndarray): shape(m, nx)
        m: number of data points
        nx: number of features

    Returns:
    mean and std of each feature
    """
    return X.mean(axis=0), X.std(axis=0)
