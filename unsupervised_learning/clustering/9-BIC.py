#!/usr/bin/env python3
"""
This module contains a function that finds the best number of clusters
for a GMM using the Bayesian Information Criterion
"""
import numpy as np
expectation_maximization = __import__('8-EM').expectation_maximization


def BIC(X, kmin=1, kmax=None, iterations=1000, tol=1e-5, verbose=False):
    """
    Finds the best number of clusters for a GMM using the BIC
    X: numpy.ndarray (n, d) containing the data set
    kmin: positive integer containing the minimum number of clusters
    kmax: positive integer containing the maximum number of clusters
    iterations: positive integer containing the max number of iterations
    tol: non-negative float containing the tolerance for the EM algorithm
    verbose: boolean that determines if EM should print information
    Returns:
        best_k: the best value for k based on its BIC
        best_result: tuple containing pi, m, S
        log_likelihoods: numpy.ndarray containing the log likelihood
                         for each cluster size tested
        bics: numpy.ndarray containing the BIC value for each cluster size
        or None, None, None, None on failure
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None, None

    if not isinstance(kmin, int) or kmin <= 0:
        return None, None, None, None

    n, d = X.shape

    if kmax is None:
        kmax = n

    if not isinstance(kmax, int) or kmax <= 0:
        return None, None, None, None

    if kmin >= kmax:
        return None, None, None, None

    if not isinstance(iterations, int) or iterations <= 0:
        return None, None, None, None

    if not isinstance(tol, float) or tol < 0:
        return None, None, None, None

    if not isinstance(verbose, bool):
        return None, None, None, None

    num_tests = kmax - kmin + 1
    log_likelihoods = np.zeros(num_tests)
    bics = np.zeros(num_tests)
    results = []

    for k in range(kmin, kmax + 1):
        pi, m, S, g, log_likelihood = expectation_maximization(
            X, k, iterations, tol, verbose)

        if pi is None:
            return None, None, None, None

        results.append((pi, m, S))
        idx = k - kmin
        log_likelihoods[idx] = log_likelihood

        p = k * d + k * d * (d + 1) / 2 + k - 1
        bic = p * np.log(n) - 2 * log_likelihood
        bics[idx] = bic

    best_idx = np.argmin(bics)
    best_k = best_idx + kmin
    best_result = results[best_idx]

    return best_k, best_result, log_likelihoods, bics
