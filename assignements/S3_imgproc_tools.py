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




def img_to_gray(img:np.array):
    """
    This function take an image and turn it in grayscale
    Parameters:
        img: an image
    Returns:
        a grayscaled image as a ndarray

    """
    img_out = np.zeros(img.shape, dtype=np.uint8)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            moy = (int(img[row, col, 0]) +int(img[row, col, 1]) +int(img[row, col, 2]))/3
            img_out[row, col, 0]= moy
            img_out[row, col, 1]= moy
            img_out[row, col, 2] = moy
    return img_out

def threshold_image_manual(img:np.ndarray):
    """
    This function apply a threshold on the image given in params
    Parameters:
        img: an image
    Returns:
        a thresholded image as a ndarray

    """
    img = img_to_gray(img)
    threshold_value = 128
    img_out = np.zeros(img.shape, dtype=np.uint8)
    if img.dtype!=np.dtype(np.uint8):
        raise TypeError("le tableau doit être de type uint 8")
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            for channel in range(img.shape[2]):
                if (img[row, col, channel] > threshold_value  ):

                    img_out[row, col, channel] = 255
                else:
                    img_out[row, col, channel] = 0
    return img_out
def threshold_image_numpy(img:np.ndarray):
    """
    This function apply a threshold on the image given in params
    Parameters:
        img: an image
    Returns:
        a thresholded image as a ndarray

    """
    if img.dtype!=np.dtype(np.uint8):
        raise TypeError("le tableau doit être de type uint 8")
    img = img_to_gray(img)
    return  1.0 *  (img> 128)
def threshold_colors_opencv(img):
    """
    This function apply a threshold on the image given in params
    Parameters:
        img: an image
    Returns:
        a thresholded image as a ndarray

    """
    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_OTSU)
    return thresh2


#img_gray=cv2.imread("testimg.jpg",0)

#img_bgr=cv2.imread("testimg.jpg",1)
#img_bgr_reversed = threshold(cv2.imread("testimg.jpg",1))
#img_bgr_reversed = img_bgr_reversed.astype(np.uint8)*255
#cv2.imshow("Gray levels image", img_gray)
##cv2.imshow("BGR image", img_bgr)
cv2.imshow("invert_colors_manual", invert_colors_manual(cv2.imread("testimg.jpg",1)))
cv2.imshow("invert_colors_manualv2", invert_colors_manualv2(cv2.imread("testimg.jpg",1)))
cv2.imshow("invert_colors_numpy", invert_colors_numpy(cv2.imread("testimg.jpg",1)))
cv2.imshow("invert_colors_opencv", invert_colors_opencv(cv2.imread("testimg.jpg",1)))
cv2.imshow("img_to_gray", img_to_gray(cv2.imread("testimg.jpg",1)))
cv2.imshow("threshold_image_manual", threshold_image_manual(cv2.imread("testimg.jpg",1)))
cv2.imshow("threshold_image_numpy", threshold_image_numpy(cv2.imread("testimg.jpg",1)))
cv2.imshow("threshold_colors_opencv", threshold_colors_opencv(cv2.imread("testimg.jpg",0)))
cv2.waitKey()

#the tests are 
