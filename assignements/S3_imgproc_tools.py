# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 09:02:46 2020

@author: vibertvg
"""
import numpy as np
import cv2

def invert_colors_manual(img):
    """
        Function who return an image with reversed color without using numpy
        Parameters:
            img : image to process
        Returns:
            img_out: return image with reversed color
    """
    img_out=np.zeros(img.shape, dtype=np.uint8)    
    for row in range (img.shape[0]):
        for col in range (img.shape[1]):
             for channel in range (img.shape[2]):
                 img_out[row,col,channel]=25-img[row,col,channel]
    return img_out


def invert_colors_manualV2(img):
    """
        Function who return an image with reversed color without using numpy
        Parameters:
            img : image to process
        Returns:
            return image with reversed color
    """
    return 255-img


def invert_colors_numpy(img):
    """
        Function who return an image with reversed color using numpy
        Parameters:
            img : image to process
        Returns:
            return image with reversed color
    """
    return np.invert(img)


def invert_colors_opencv(img):
    """
        Function who return an image with reversed color using OpenCv
        Parameters:
            img : image to process
        Returns:
            return image with reversed color
    """
    
    return cv2.bitwise_not(img - 255)


img_url = 'Magician.png'
img_reversed=cv2.imread(img_url,1)
cv2.imshow("BGR image", invert_colors_numpy(img_reversed))
cv2.waitKey()



"""
img_gray=cv2.imread(img_url,0)
img_bgr=cv2.imread(img_url,1)

cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)
"""


