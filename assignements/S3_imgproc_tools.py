# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import cv2
import numpy as np



def invert_colors_manual(input_img):
    '''
    
    This function reverse the color of an image 
    Parameters:
        input_img: an image
    Returns: a reversed image 
    
    '''
    img_out = np.zeros(input_img.shape, dtype=np.uint8)
    for row in range(input_img.shape[0]):
       for col in range(input_img.shape[1]):      
           for channel in range(input_img.shape[2]):
               img_out[row,col,channel]=255-input_img[row,col,channel]
       
    return img_out

def invert_colors_manualv2(input_img):
    '''
    
    This function reverse the color of an image 
    Parameters:
        input_img: an image
    Returns: a reversed image 
    
    '''
    return 255-input_img

def invert_colors_numpy(input_img):
    '''
    
    This function reverse the color of an image 
    Parameters:
        input_img: an image
    Returns: a reversed image 
    
    '''
    return np.invert(input_img)

def invert_colors_opencv(input_img):
    '''
    
    This function reverse the color of an image 
    Parameters:
        input_img: an image
    Returns: a reversed image 
    
    '''
    return cv2.bitwise_not(input_img)

img_gray=cv2.imread("testimg.jpg",0)
img_bgr=cv2.imread("testimg.jpg",1)
img_bgr_reversed = invert_colors_opencv(cv2.imread("testimg.jpg",1))

cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)
cv2.imshow("BGR image inverted", img_bgr_reversed)
cv2.waitKey()

