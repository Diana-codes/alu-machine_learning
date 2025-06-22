#!/usr/bin/env python3
"""
Function creates a dataframe from a numpy array
"""


import string
import pandas as pd


def from_numpy(array):
    """
    Creates a pandas dataframe from a numpyndarray
    Args:
    - array: np.ndarray that should be used to create
      pd.Dataframe
    - columns of the pd.Dataframe should be labeled in
    in alphabetical order and capitalized
    Returns:
    new dataframe
    """
    num_columns = array.shape[1]

    # Generate the column labels (A, B, C, ...)
    columns = [chr(65 + i) for i in range(num_columns)]

    # Create the DataFrame
    df = pd.DataFrame(array, columns=columns)
F
    return df
