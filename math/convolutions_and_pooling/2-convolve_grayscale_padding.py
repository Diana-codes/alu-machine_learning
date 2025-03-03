#!/usr/bin/env python3
"""Performs valid convolution on grayscale
images with custom padding"""

import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    Performs valid convolution on grayscale images
    with custom padding
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
    -padding is a tuple of (ph, pw)
        -ph: padding for the height of the image
        -pw: padding for the width of the image
        image should be padded with 0's

    Returns:
    a numpy.ndarray containing the convolved images
    """
    m, h, w = images.shape[0], images.shape[1], images.shape[2]
    kh, kw = kernel.shape[0], kernel.shape[1]
    ph, pw = padding[0], padding[1]
    output_width = int(w - kw + (2 * pw) + 1)
    output_height = int(h - kh + (2 * ph) + 1)
    convolved = np.zeros((m, output_height, output_width))
    # pad the images with zeros
    npad = ((0, 0), (ph, ph), (pw, pw))
    imagesp = np.pad(images, pad_width=npad,
                     mode='constant', constant_values=0)
    # the convolution operation
    for i in range(output_height):
        for j in range(output_width):
            image = imagesp[:, i: i + kh, j: j + kw]
            convolved[:, i, j] = np.sum(
                np.multiply(image, kernel), axis=(1, 2))
    return convolved
