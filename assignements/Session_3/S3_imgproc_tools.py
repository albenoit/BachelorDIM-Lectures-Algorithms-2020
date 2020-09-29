# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 09:00:56 2020

@author: vanhouta
"""

import cv2 
import numpy as np 

img_gray=cv2.imread('img/AsDePique.jpg',0) 
img_bgr=cv2.imread('img/AsDePique.jpg',1) 
img = cv2.imread('img/AsDePique.jpg')
#display the matrix shapes
print("Gray levels image shape = "+str(img_gray.shape))
print("BGR image shape = "+str(img_bgr.shape))
#display the loaded images
#☺cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)
cv2.waitKey()


def invert_colors_manual(img):
    '''
        This function invert the color of img
        Args:
            img: img to need to invert
        Returns the inverted img
    '''
    img_out = np.zeros(img.shape, dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                img_out[i,j,k]=255-img[i,j,k]
    cv2.imshow('img_out',img_out)
    cv2.waitKey()
    return True

def invert_colors_numpy(img):
    '''
        This function invert the color of img
        Args:
            img: img to need to invert
        Returns the inverted img
    '''
    img_out = np.zeros(img.shape, dtype=np.uint8)
    img_out = 255 - img
    cv2.imshow('img_out',img_out)
    cv2.waitKey()
    return True

def invert_colors_opencv(img):
    '''
        This function invert the color of img
        Args:
            img: img to need to invert
        Returns the inverted img
    '''
    img_out = cv2.bitwise_not(img)
    cv2.imshow('img_out',img_out)
    cv2.waitKey()
    return True

def inv_gray_levels(img:np.ndarray):
    '''test data type, expecting uint8'''
    '''if img is None:
        raise ValueError('Expected an uint8')
    if img.dtype != np.dtype(np.uint8):
        raise ValueError('Expected uint8 typed nd array')
    if isinstance(img, np.ndarray):
        raise ValueError('Expected an nd array')'''
    if img.dtype!=np.dtype(np.uint8):
        raise TypeError('Expected uint8 typed nd array')
    return 255-img

def threshold_image_manual(img):
    img_out = np.zeros(img.shape, dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                if(img[i,j,k] <= 127):
                    img_out[i,j,k]=0
                else:
                    img_out[i,j,0]=255
                    img_out[i,j,1]=255
                    img_out[i,j,2]=255
    cv2.imshow('img_out',img_out)
    cv2.waitKey()
    return True


threshold_image_manual(img)
'''invert_colors_manual(img)'''



        
