# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:48:25 2020

@author: polletb
"""

import numpy as np
import cv2


img_gray=cv2.imread('code.png', 0) #load an image in gray levels
img_bgr=cv2.imread('code.png', 1) #load an image in Blue Green Red

print("Gray levels image shape = "+str(img_gray.shape))
print("BGR image shape = "+str(img_bgr.shape))
#display the loaded images

#cv2.imshow("Gray levels image", img_gray)
#cv2.imshow("BGR image", img_bgr)


#Invert manual
def invert_color_manual(input_img:np.ndarray):
    '''
    Invert color image manual
    Parameters:
            input_img: np.ndarray
    Returns :
        ndarray with image invert
    '''
    output_img = np.zeros(input_img.shape, dtype=np.uint8)
    
    if input_img.dtype != np.dtype(np.uint8):
        raise TypeError('not an uint8 nd array')

    """for row in range (input_img.shape[0]):
        for col in range (input_img.shape[1]):
            for channel in range (input_img.shape[2]):
                output_img[row, col, channel] = 255 - input_img[row, col, channel]"""
    
    output_img = 255 - input_img
                
    return output_img

"""img_invert = invert_color_manual(img_bgr)
cv2.imshow("Invert image manual", img_invert)"""

def invert_colors_numpy(input_img:np.ndarray):
    '''
    Invert color image with numpy
    Parameters:
            input_img: np.ndarray
    Returns :
        np.array with image invert
    '''
    if input_img.dtype != np.dtype(np.uint8):
        raise TypeError('not an uint8 nd array')
    
    array = np.array(input_img, np.uint8)
    return ~array

"""img_invert = invert_colors_numpy(img_bgr)
cv2.imshow("Invert image numpy", img_invert)"""

def invert_colors_opencv(input_img:np.ndarray):
    '''
    Invert color with opencv
    Parameters:
            input_img: np.ndarray
    Returns :
        array with image invert
    '''
    if input_img.dtype != np.dtype(np.uint8):
        raise TypeError('not an uint8 nd array')
    
    return cv2.bitwise_not(input_img)

"""img_invert = invert_colors_numpy(img_bgr)
cv2.imshow("Invert image opencv", img_invert)"""



def thresholding_manual(input_img:np.ndarray):
    '''
    Thresholding image manual
    Parameters:
            input_img: np.ndarray
    Returns :
        array with image thresholding
    '''
    output_img = np.zeros(input_img.shape, dtype=np.uint8)
    
    return output_img

def thresholding_numpy(input_img:np.ndarray):
    '''
    Thresholding image numpy
    Parameters:
            input_img: np.ndarray
    Returns :
        np.array with image thresholding
    '''
    threshold_value = 128   
    return input_img>threshold_value

img_thresholding = thresholding_numpy(img_bgr)
img_thresholding_display = img_thresholding.astype(np.uint8)*255
cv2.imshow("Thresholding image", img_thresholding_display)

cv2.waitKey()

