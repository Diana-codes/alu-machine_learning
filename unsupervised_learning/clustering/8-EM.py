#!/usr/bin/env python3
"""
This module contains a function that performs the expectation maximization
for a GMM
"""
import numpy as np
initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization


def expectation_maximization(X, k, iterations=1000, tol=1e-5, verbose=False):
    """
    Performs the expectation maximization for a GMM
    X: numpy.ndarray (n, d) containing the data set
    k: positive integer containing the number of clusters
    iterations: positive integer containing the maximum number of iterations
    tol: non-negative float containing tolerance of the log likelihood
    verbose: boolean that determines if you should print information
    Returns:
        pi: numpy.ndarray (k,) containing the priors for each cluster
        m: numpy.ndarray (k, d) containing the centroid means
        S: numpy.ndarray (k, d, d) containing the covariance matrices
        g: numpy.ndarray (k, n) containing the probabilities
        log_likelihood: the log likelihood of the model
        or None, None, None, None, None on failure
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None, None, None

    if not isinstance(k, int) or k <= 0:
        return None, None, None, None, None

    if not isinstance(iterations, int) or iterations <= 0:
        return None, None, None, None, None

    if not isinstance(tol, float) or tol < 0:
        return None, None, None, None, None

    if not isinstance(verbose, bool):
        return None, None, None, None, None

    pi, m, S = initialize(X, k)
    if pi is None:
        return None, None, None, None, None

    log_likelihood_prev = 0

    for i in range(iterations):
        g, log_likelihood = expectation(X, pi, m, S)
        if g is None:
            return None, None, None, None, None

        if verbose and (i % 10 == 0):
            print("Log Likelihood after {} iterations: {}".format(
                i, round(log_likelihood, 5)))

        if abs(log_likelihood - log_likelihood_prev) <= tol:
            if verbose:
                print("Log Likelihood after {} iterations: {}".format(
                    i, round(log_likelihood, 5)))
            break

        log_likelihood_prev = log_likelihood

        pi, m, S = maximization(X, g)
        if pi is None:
            return None, None, None, None, None

    else:
        g, log_likelihood = expectation(X, pi, m, S)
        if g is None:
            return None, None, None, None, None
        if verbose:
            print("Log Likelihood after {} iterations: {}".format(
                iterations, round(log_likelihood, 5)))

    return pi, m, S, g, log_likelihood
