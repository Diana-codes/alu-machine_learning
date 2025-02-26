#!/usr/bin/env python3
"""Function to calculate the mean and covariance of a dataset"""


import numpy as np


def mean_cov(X):
    """
    Calculates the mean and covariance matrix of a dataset

    Parameters:
    X (numpy.ndarray): A 2D array of shape(n, d) containing the dataset, where:
        - n is the number of data points
        - d is the number of dimensions in each data point

    Raises:
    TypeError: If X is not a 2D numpy.ndarray
    ValueError: If n is less than 2

    Returns:
    tuple: A Tuple containing:
    - mean(numpy.ndarray): The mean of the dataset, of 1D array of shape (1,d)
    - cov(numpy.ndarray): covariance mat of dataset, of 2D array of shape(d,d)
    """
    # Check if X is a 2D numpy array
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    if X.shape[0] < 2:
        raise ValueError("X must contain multiple data points")
    # calculate the mean and covariance
    n, d = X.shape
    mean = np.mean(X, axis=0, keepdims=True)
    centered_data = X - mean
    cov = np.dot(centered_data.T, centered_data) / (n - 1)
    return mean, cov
