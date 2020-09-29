# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:48:25 2020

@author: polletb
"""

import numpy as np
import cv2


img_gray=cv2.imread('code.png',0) #load an image in gray levels
img_bgr=cv2.imread('code.png',1) #load an image in Blue Green Red

print("Gray levels image shape = "+str(img_gray.shape))
print("BGR image shape = "+str(img_bgr.shape))
#display the loaded images

#cv2.imshow("Gray levels image", img_gray)
#cv2.imshow("BGR image", img_bgr)


#Invert manual
def invert_color_manual(input_img):
    output_img = np.zeros(input_img.shape, dtype=np.uint8)
    
    for row in range (input_img.shape[0]):
        for col in range (input_img.shape[1]):
            for channel in range (input_img.shape[2]):
                output_img[row, col, channel] = 255 - input_img[row, col, channel]
    
    """ or output_img = 255 - input_img """
                
    return output_img

"""img_invert = invert_color_manual(img_bgr)
cv2.imshow("Invert image manual", img_invert)"""

def invert_colors_numpy(input_img):
    array = np.array(input_img, np.uint8)
    return ~array

"""img_invert = invert_colors_numpy(img_bgr)
cv2.imshow("Invert image numpy", img_invert)"""

def invert_colors_opencv(input_img):   
    return cv2.bitwise_not(input_img)

"""img_invert = invert_colors_numpy(img_bgr)
cv2.imshow("Invert image opencv", img_invert)"""

cv2.waitKey()

