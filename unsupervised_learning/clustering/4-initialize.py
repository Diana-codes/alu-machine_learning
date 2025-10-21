#!/usr/bin/env python3
"""
This module contains a function that
initializes variables for a Gaussian Mixture Model
"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans


def initialize(X, k):
    """
    initializes variables for a Gaussian Mixture Model
    X: numpy.ndarray (n, d) containing the dataset
        - n no. of data points
        - d no. of dimensions for each data point
    k: positive integer - the number of clusters
    return:
        - pi: numpy.ndarray (k,) containing priors for each cluster
        initialized to be equal
        - m: numpy.ndarray (k, d) containing centroid means for each cluster,
        initialized with K-means
        - S: numpy.ndarray (k, d, d) covariance matrices for each cluster,
        initialized as identity matrices
    """
    # Validate X first, before unpacking shape
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None
    
    # Validate k
    if not isinstance(k, int) or k <= 0:
        return None, None, None
    
    # Now it's safe to unpack shape
    n, d = X.shape
    
    # Check if k is larger than n
    if k > n:
        return None, None, None
    
    pi = np.full((k,), 1 / k)
    m, _ = kmeans(X, k)
    S = np.tile(np.identity(d), (k, 1, 1))
    
    return pi, m, S
