#!/usr/bin/env python3
"""
Function normalizes(standardizes) a matrix
"""


import numpy as np


def normalize(X, m, s):
    """
    Normalizes a matrix

    Args:
    X(numpy.ndarray): shape(d, nx)
        d: number of data points
        nx: number of features
    m(numpy.ndarray): mean of all features of X
    s(numpy.ndarray): standard deviation of all features of X

    Returns:
    normalized X matrix
    """
    return (X - m) / s
