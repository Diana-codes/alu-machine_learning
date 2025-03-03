#!/usr/bin/env python3
"""Performs valid convolution on grayscale
images with channels"""

import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """
    Performs valid convolution on grayscale images
    with channels
    Args:
    -images(numpy.ndarray) containing multiple
    grayscale images with shape(m, h, w, c):
        -m: number of images
        -h: height in pixels of the images
        -w: width in pixels of the images
        -c: number of channels in the image
    -kernel(numpy.ndarray) containing the kernel
    for the convolution with shape(kh, kw, c):
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
    nw = int(((w - kw + (2 * pw)) / sw) + 1)
    nh = int(((h - kh + (2 * ph)) / sh) + 1)
    convolved = np.zeros((m, nh, nw))
    npad = ((0, 0), (ph, ph), (pw, pw), (0, 0))
    imagesp = np.pad(images, pad_width=npad,
                     mode='constant', constant_values=0)
    for i in range(nh):
        x = i * sh
        for j in range(nw):
            y = j * sw
            image = imagesp[:, x:x + kh, y:y + kw, :]
            convolved[:, i, j] = np.sum(np.multiply(image, kernel),
                                        axis=(1, 2, 3))
    return convolved
