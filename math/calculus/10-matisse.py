#!/usr/bin/env python3
"""Calculates deivative of a polynomial"""


def poly_derivative(poly):
    """
    calculates the derivative of the given polynomial

    Parameters:
        poly (list): list of coefficients representing a polynomial
            the index of the list represents the power of x
            the coefficient belongs to

    Returns:
        a new list of coefficients representing the derivative
        [0], if the derivate is 0
        None, if poly is not valid
    """
    if type(poly) is not list or len(poly) < 1:
        return None
    for coefficient in poly:
        if type(coefficient) is not int and type(coefficient) is not float:
            return None
        derivative = []  # list of derivative coefficients
        for power, coefficient in enumerate(poly):
            if power == 0:
                continue
            derivative.append(power * coefficient)
        while len(derivative) > 1 and derivative[-1] == 0:
            derivative.pop()
        if not derivative:
            return [0]
        return derivative
