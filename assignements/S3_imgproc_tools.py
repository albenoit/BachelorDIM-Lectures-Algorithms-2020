# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 8:35:16 2020
@author: cuvellin
"""

import cv2
import numpy as np


IMG_PATH = 'P:/bg/bg.jpg'

img=cv2.imread(IMG_PATH)

def invert_colors_manual(input_img) :
    '''
    This function will only rely on raw python with loops
    
    Parameters:
        input_img
    Returns:
        matrix
    '''
    img_out = np.zeros(input_img.shape, dtype=np.uint8)
    for row in range(input_img.shape[0]) :
        for col in range(input_img.shape[1]) :
            for channel in range(input_img.shape[2]):
                img_out[row, col, channel] = 255 - input_img[row, col, channel]
                
    return img_out

def invert_colors_numpy(input_img) :
    '''
    This function will rely on the Numpy operators to do the job
    
    Parameters:
        input_img
    Returns:
        matrix
    '''
    return (255-input_img)
   
   
invert_manual_img = invert_colors_manual(img)
invert_img = invert_colors_numpy(img)

cv2.imshow('invert_manual_img', invert_manual_img)
cv2.imshow('input', invert_img)
cv2.waitKey()