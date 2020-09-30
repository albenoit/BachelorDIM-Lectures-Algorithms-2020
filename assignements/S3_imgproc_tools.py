# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 8:35:16 2020
@author: cuvellin
"""

import cv2
import numpy as np

# IMG_PATH = 'P:/bg/bg.jpg'
#IMG_PATH = 'C:/Users/VM Nathan/Documents/LPDIM/BachelorDIM-Lectures-Algorithms-2020/img/one_pixel_red.jpg'

# img = cv2.imread(IMG_PATH)
img = np.array([[[0, 0, 254]]], dtype=np.uint8)

print("img")
print(img)


def invert_colors_manual(input_img):
    """
    This function will only rely on raw python with loops

    Parameters:
        input_img
    Returns:
        matrix
    """
    if not hasattr(input_img, 'dtype') or input_img.dtype != np.dtype(np.uint8):
        raise TypeError('expected uint8 typed nd array')

    img_out = np.zeros(input_img.shape, dtype=np.uint8)
    for row in range(input_img.shape[0]):
        for col in range(input_img.shape[1]):
            for channel in range(input_img.shape[2]):
                img_out[row, col, channel] = 255 - input_img[row, col, channel]

    return img_out


def invert_colors_numpy(input_img):
    """
    This function will rely on the Numpy operators to do the job

    Parameters:
        input_img
    Returns:
        matrix
    """
    '''
    if input_img is None:
        raise AttributeError('expected an uint8 nd array')
    if not(isinstance(input_img, np.ndarray)):
        raise TypeError('expected an nd array')
    '''
    if not hasattr(input_img, 'dtype') or input_img.dtype != np.dtype(np.uint8):
        raise TypeError('expected uint8 typed nd array')

    return 255 - input_img


def invert_colors_opencv(input_img):
    return cv2.bitwise_not(input_img)


def threshold(img: np.ndarray):
    threshold_value = 128
    if not hasattr(img, 'dtype') or img.dtype != np.dtype(np.uint8):
        raise TypeError('expected uint8 typed nd array')
    return img > threshold_value

"""
invert_manual_img = invert_colors_manual(img)
invert_img = invert_colors_numpy(img)
invert_opencv = invert_colors_opencv(img)

# cv2.imshow('invert_manual_img', invert_manual_img)
cv2.imshow('input', invert_img)
cv2.imshow('invert opencv', invert_opencv)

threshold_img = threshold(img)
threshold_img_disp = threshold_img.astype(np.uint8) * 255
cv2.imshow('threshold_img', threshold_img_disp)
cv2.waitKey()
"""
