import cv2
import numpy as np

def invert_colors_manual_old(input_img):
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

def invert_colors_manual(input_img):
    '''
    
    This function reverse the color of an image 
    Parameters:
        input_img: an image
    Returns: a reversed image 
    
    '''
    '''
    if input_img is None:
        raise ValueError('expected an uint8 nd array')
    if not(isinstance(input_img, np.ndarray)):
        raise TypeError('expected an nd array')
    '''
    if input_img.dtype!=np.dtype(np.uint8):
        raise TypeError('expected uint8 typed nd array')
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


'''
Image Thresholging
'''

def threshold_image_manual(img:np.ndarray) :
    '''
    
    This function will only rely on raw python with loop without the use of
    any external library. It takes as input a loaded image and returns the
    transformed image.

    '''
    
    threshold_value = 128
    if img.dtype!=np.dtype(np.uint8):
        raise TypeError ('expected uint8typs nd array')
    return img>threshold_value

img=cv2.imread("trou_noir.jpg",0)
img_thresholded=threshold_image_manual(img)

img_threshold_disp=img_thresholded.astype(np.uint8)*255
cv2.imshow('seuilled image', img_threshold_disp)
cv2.waitKey()
