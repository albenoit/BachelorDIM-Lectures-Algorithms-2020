# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:45:28 2020

@author: derbaghc
"""

import cv2
import numpy as np 

img_gray=cv2.imread('image_test_little.jpg', 0)
img_rgb=cv2.imread('image_test_little.jpg', 1)

print("Gray levels image shape  - " + str(img_gray.shape ))
print("RGB levels image shape  - " + str(img_rgb.shape ))

print(img_rgb[1, 1, 2])

#cv2.imshow('Gray levels image', img_gray)
#cv2.imshow('RGB levels image', img_rgb)
#cv2.waitKey()


'''
Fonction qui inverse les couleurs d'une image. Si elle est en RGB -> nuances 
de gris et inversement
parameters : input_image
return : inversed_img

'''
def invert_colors_manual(input_image):
    ##Pire solution pour Python (besoin de beaucoup de ressources)
    inversed_img = np.zeros(input_image.shape, dtype=np.uint8)
    
    '''for x in range(input_image.shape[0]):
        for y in range(input_image.shape[1]):
            for color in range(input_image.shape[2]):
                inversed_img[x, y, color] = 255 - input_image[x, y, color]
    cv2.imshow('Negative image', inversed_img)'''
    
    ## Version optimale
    inversed_img = 255 - input_image
    cv2.imshow('Negative image', inversed_img)
        
        
        
   
invert_colors_manual(img_rgb)     