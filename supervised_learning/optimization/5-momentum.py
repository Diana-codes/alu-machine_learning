#!/usr/bin/env python3
"""
Function updates the variable using the GD with
momentum optimization algorithm
"""


def update_variables_momentum(alpha, beta1, var, grad, v):
    """
    Updates the variable using the GD with momentum optimization algorithm

    Args:
        alpha (float): learning rate
        beta1 (float): momentum weight
        var (np.ndarray): variable to be updated
        grad (np.ndarray): gradient of var
        v (np.ndarray): the previous first moment of var

    Returns:
        np.ndarray: the updated variable and the new moment, respectively
    """
    v = beta1 * v + (1 - beta1) * grad
    var = var - alpha * v
    return var, v
