#!/usr/bin/env python3
"""Performs valid convolution on grayscale
images with custom padding"""

import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
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
        if 'same', performs a same convolution
        if 'valid', performs a valid convolution
    -stride is a tuple of (sh, sw)
        -sh: stride for the height of the image
        -sw: stride for the width of the image

    Returns:
    a numpy.ndarray containing the convolved images
    """
    m, h, w = images.shape[0], images.shape[1], images.shape[2]
    kh, kw = kernel.shape[0], kernel.shape[1]
    sh, sw = stride[0], stride[1]
    if padding == 'same':
        pw = int(((w - 1) * sw + kw - w) / 2) + 1
        ph = int(((h - 1) * sh + kh - h) / 2) + 1
    elif padding == 'valid':
        ph = 0
        pw = 0
    else:
        pw = padding[1]
        ph = padding[0]
    output_width = int(((w - kw + (2 * pw)) / sw) + 1)
    output_height = int(((h - kh + (2 * ph)) / sh) + 1)
    convolved = np.zeros((m, output_height, output_width))
    # pad the images with zeros
    npad = ((0, 0), (ph, ph), (pw, pw))
    imagesp = np.pad(images, pad_width=npad,
                     mode='constant', constant_values=0)
    # the convolution operation
    for i in range(output_height):
        x = i * stride[0]
        for j in range(output_width):
            y = j * sw
            image = imagesp[:, x: x + kh, y: y + kw]
            convolved[:, i, j] = np.sum(
                np.multiply(image, kernel), axis=(1, 2))
    return convolved
