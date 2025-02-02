#!/usr/bin/env python3
"""Calculates the sum of squares of n natural numbers"""


def summation_i_squared(n):
    """
    Calculates the sum of the squares of the first n natural numbers
    Utilizes Faulhaber's formula for power of 2:
    sum of i^2 from i=1 to n = (n * (n + 1) * (2n + 1)) / 6
    """
    if type(n) is not int or n < 1:
        return None
    sigma_sum = (n * (n + 1) * ((2 * n) + 1)) / 6
    return int(sigma_sum)
