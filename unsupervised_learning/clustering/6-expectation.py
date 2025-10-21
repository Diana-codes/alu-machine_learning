#!/usr/bin/env python3
"""
This module contains a function that calculates the expectation step
in the EM algorithm for a GMM
"""
import numpy as np
pdf = __import__('5-pdf').pdf


def expectation(X, pi, m, S):
    """
    Calculates the expectation step in the EM algorithm for a GMM
    X: numpy.ndarray (n, d) containing the data set
    pi: numpy.ndarray (k,) containing the priors for each cluster
    m: numpy.ndarray (k, d) containing the centroid means for each cluster
    S: numpy.ndarray (k, d, d) containing the covariance matrices
    return:
        g: numpy.ndarray (k, n) containing the posterior probabilities
           for each data point in each cluster
        l: the total log likelihood
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None

    if not isinstance(pi, np.ndarray) or len(pi.shape) != 1:
        return None, None

    if not isinstance(m, np.ndarray) or len(m.shape) != 2:
        return None, None

    if not isinstance(S, np.ndarray) or len(S.shape) != 3:
        return None, None

    n, d = X.shape
    k = pi.shape[0]

    if m.shape[0] != k or m.shape[1] != d:
        return None, None

    if S.shape[0] != k or S.shape[1] != d or S.shape[2] != d:
        return None, None

    if not np.isclose(np.sum(pi), 1):
        return None, None

    # Calculate the probability density for each cluster
    # g will be (k, n) where g[i, j] is the likelihood of point j in cluster i
    g = np.zeros((k, n))

    for i in range(k):
        # Calculate PDF for cluster i
        P = pdf(X, m[i], S[i])
        if P is None:
            return None, None
        # Multiply by prior
        g[i] = pi[i] * P

    # Calculate the total likelihood for each point (sum over clusters)
    total_likelihood = np.sum(g, axis=0)

    # Calculate log likelihood
    l = np.sum(np.log(total_likelihood))

    # Normalize to get posterior probabilities
    g = g / total_likelihood

    return g, l
