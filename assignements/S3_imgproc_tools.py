import cv2
import numpy as np

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

img_gray=cv2.imread("trou_noir.jpg",0)
img_bgr=cv2.imread("trou_noir.jpg",1)
img_bgr_reversed = invert_colors_opencv(cv2.imread("trou_noir.jpg",1))

cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)
cv2.imshow("BGR image inverted", img_bgr_reversed)
cv2.waitKey()
