import cv2 """ importer open cv : pip install numpy cv2 """
import numpy as np

myImage = ('')

img = cv2.imread (myImage)

print ('input image shape', img.shape)

cv2.imshow('input', img)
cv2.waitKey()


"""
design a function invert_colors_manual(input_img : ndarray) : returns ndarray.
This function will only rely on raw python with loops without the use of
any external library. It takes as input a loaded image and returns the
transformed image.
"""

def invert_colors_manual (input_img) :
    img_out = np.zeros(img.shape, dtype = np.uint8)
    for row in range (img.shape[0]) :
        for col in range (img.shape[1]) :
            for channel in range (img.shape[2]) :
                img_out[row, col, channel] = 255 - input_img[row, col, channel]
    return img_out

invert_manual_img = invert_colors_manual(img)

cv2.imshow('invert_colors_manual', invert_manual_img)
cv2.waitKey()



"""
design a similar function called invert_colors_numpy(input_img : ndarray)returns ndarray.
This function will rely on the Numpy operators to do the job.
"""

def invert_colors_numpy(input_img) :
    return (255 - input_img)

invert_numpy_img = invert_colors_numpy(img)

cv2.imshow('invert_colors_numpy', invert_numpy_img)
cv2.waitKey()



def threshold(img:np.ndarray) :
    """
    if img is None :
        raise ValueError ('excepted an uint8 nd array')
    if not(isinstance(img, nd.ndarray)) :
        raise TypeError ('excepted an nd array')
    """
    threshold_value = 128 ''' in range [0; 255]'''
    if img.stype!=np.dtype(np.uint8)  :
        raise TypeError ('excepted uint8 typed nd array')
    return img>threshold_value

img = cv2.imread (myImage)
img_threshold = threshold(img)

img_threshold_disp = img_thresholded.astype(np.uint8)*255
cv2.imshow('seuilled image', img_threshold_disp)
cv2.waitKey()


"""
prof
"""


def inv_gray_levels(img) :
    """
    if img is None :
        raise ValueError ('excepted an uint8 nd array')
    if not(isinstance(img, nd.ndarray)) :
        raise TypeError ('excepted an nd array')
    """
    if img.stype!=np.dtype(np.uint8)  :
        raise TypeError ('excepted uint8 typed nd array')
    return 255 - img

import pytest

def test_innv_gray_levels_tuNone() :
    with pytest.raise (AttributeError) :
        inv_gary_levels(None)

def test_innv_gray_levels_tuArray() :
    with pytest.raise (AttributeError) :
        inv_gary_levels(1)

def test_innv_gray_levels_tuuint8() :
    with pytest.raise (TypeError) :
        inv_gary_levels(np.zeros((2, 2), dtype=np.float32))

def test_innv_gray_levels_tuprocess() :
    ''' TODO '''
        
def test_innv_gray_levels_tuprocessOK() :
    
