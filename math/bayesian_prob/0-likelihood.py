#!/usr/bin/env python3
"""
Calculates the likelihood of a patient
who takes drugs to develop severe side effects
"""

import numpy as np


def likelihood(x, n, P):
    """
    the likelihood of a patient who takes drugs to develop severe side effects

    parameters:
    x: the number of patients that develop severe side effects
    n: the total number of patients observed
    P: the probability of a patient developing severe side effects

    Raises:
    ValueError if:
        - n is not a positive integer
        - x is not an integer >= 0 || integer == 0 and x is greater than n
        - P is not in the range[0, 1]

    TypeError: P is not a 1D array(d,)

    Returns:
    1D array containing the likelihood of getting severe side effects
    """
    if type(n) != int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) != int or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
            )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    numerator = np.math.factorial(n)
    denominator = np.math.factorial(x) * np.math.factorial(n - x)
    coefficient = numerator / denominator
    X = coefficient * (P ** x) * ((1 - P) ** (n - x))
    return X
