#!/usr/bin/env python3
"""Performs pooling on images"""

import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """
    Performs pooling on images
    Args:
    -images(numpy.ndarray) containing multiple
    grayscale images with shape(m, h, w, c):
        -m: number of images
        -h: height in pixels of the images
        -w: width in pixels of the images
        -c: number of channels in the image
    -kernel(numpy.ndarray) containing the kernel
    for the convolution with shape(kh, kw):
        -kh: height of the kernel
        -kw: width of the kernel
    -stride is a tuple of (sh, sw)
        -sh: stride for the height of the image
        -sw: stride for the width of the image
    -mode indicates the type of pooling
        -max: max pooling
        -avg: average pooling

    Returns:
    a numpy.ndarray containing the convolved images
    """
    c = images.shape[3]
    m, h, w = images.shape[0], images.shape[1], images.shape[2]
    kh, kw = kernel_shape[0], kernel_shape[1]
    sh, sw = stride[0], stride[1]
    nw = int(((w - kw) / stride[1]) + 1)
    nh = int(((h - kh) / stride[0]) + 1)
    pooled = np.zeros((m, nh, nw, c))
    for i in range(nh):
        x = i * stride[0]
        for j in range(nw):
            y = j * stride[1]
            image = images[:, x:x + kh, y:y + kw, :]
            if mode == 'max':
                pooled[:, i, j, :] = np.max(image, axis=(1, 2))
            else:
                pooled[:, i, j, :] = np.average(image, axis=(1, 2))
    return pooled
