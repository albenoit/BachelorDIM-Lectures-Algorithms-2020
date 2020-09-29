# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 09:02:46 2020

@author: vibertvg
"""
import numpy as np
import cv2

def invert_colors_manual(img):
    
    img_out=np.zeros(img.shape, dtype=np.uint8)    
    for row in range (img.shape[0]):
        for col in range (img.shape[1]):
             for channel in range (img.shape[2]):
                 img_out[row,col,channel]=25-img[row,col,channel]
    return img_out



img_url = 'Magician.png'
img_reversed=cv2.imread(img_url,1)
cv2.imshow("BGR image", invert_colors_manual(img_reversed))
cv2.waitKey()

"""
img_gray=cv2.imread(img_url,0)
img_bgr=cv2.imread(img_url,1)

cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)
"""


