#!/usr/bin/env python3
"""Creates a function to return transpose of a matrix"""


def matrix_transpose(matrix):
    """Returns transpose of a matrix"""
    transpose = [[matrix[j][i] for j in range(len(matrix))]
                 for i in range(len(matrix[0]))]
    return transpose
