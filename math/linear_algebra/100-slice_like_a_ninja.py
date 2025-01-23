#!/usr/bin/env python3
"""Define a function  that slices a matrix along specific axes"""


def np_slice(matrix, axes={}):
    """return the tuple"""
    slices = [slice(None)] * matrix.ndim
    for axis, slice_ in axes.items():
        slices[axis] = slice(*slice_)
    return matrix[tuple(slices)]
