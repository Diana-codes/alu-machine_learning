#!/usr/bin/env python3
"""Performs valid convolution on grayscale images"""

import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Performs valid convolution on grayscale images

    Args:
    -images(numpy.ndarray) containing multiple
    grayscale images with shape(m, h, w):
        -m: number of images
        -h: height in pixels of the images
        -w: width in pixels of the images
    -kernel(numpy.ndarray) containing the kernel
    for the convolution with shape(kh, kw):
        -kh: height of the kernel
        -kw: width of the kernel

    Returns:
    a numpy.ndarray containing the convolved images
    """
    m, h, w = images.shape[0], images.shape[1], images.shape[2]
    kh, kw = kernel.shape[0], kernel.shape[1]
    output_width = w - kw + 1
    output_height = h - kh + 1
    convolved = np.zeros((m, output_height, output_width))
    for i in range(output_height):
        for j in range(output_width):
            image = images[:, i:(i + kh), j:(j + kw)]
            convolved[:, i, j] = np.sum(
                np.multiply(image, kernel), axis=(1, 2))
    return convolved
