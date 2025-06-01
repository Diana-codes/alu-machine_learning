#!/usr/bin/env python3
"""
Function calculates the weighted moving average of a dataset
"""


import numpy as np


def moving_average(data, beta):
    """
    Calculates the weighted moving average

    Args:
    data: list of data to calculate the moving average
    beta: weight used for the moving average

    Returns:
    a list containing the moving averages of data
    """
    v = 0
    result = []
    for x in range(len(data)):
        v = beta * v + (1 - beta) * data[x]
        b = 1 - (beta ** (x + 1))
        result.append(v / b)
    return result
