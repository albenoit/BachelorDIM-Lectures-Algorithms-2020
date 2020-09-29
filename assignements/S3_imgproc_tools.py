# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:45:28 2020

@author: derbaghc
"""

import cv2
import numpy as np 

# =============================================================================
# Déclaration des variables
# =============================================================================
img_gray=cv2.imread('image_test_little.jpg', 0)
img_rgb=cv2.imread('image_test_little.jpg', 1)

print("Gray levels image shape  - " + str(img_gray.shape ))
print("RGB levels image shape  - " + str(img_rgb.shape ))

print(img_rgb[1, 1, 2])

#cv2.imshow('Gray levels image', img_gray)
#cv2.imshow('RGB levels image', img_rgb)
#cv2.waitKey()


# =============================================================================
# Fonctions et déclarations des fonctions
# =============================================================================
def invert_colors_manual(input_image):
    '''
    Fonction qui inverse les couleurs d'une image (image négative)
    parameters : input_image
    return : inverted_img
    '''
    ##Pire solution pour Python (besoin de beaucoup de ressources)
    inverted_img = np.zeros(input_image.shape, dtype=np.uint8)
    for x in range(input_image.shape[0]):
        for y in range(input_image.shape[1]):
            for color in range(input_image.shape[2]):
                inverted_img[x, y, color] = 255 - input_image[x, y, color]
    return inverted_img 
    
    

def invert_colors_numpy(input_image):
    '''
    Fonction qui inverse les couleurs d'une image (image négative)
    parameters : input_image
    return : inverted_img
    '''
    inverted_img = 255 - input_image
    return inverted_img



def invert_colors_opencv(input_image):
    '''
    Fonction qui inverse les couleurs d'une image (image négative)
    parameters : input_image
    return : inversed_img
    '''
    inverted_img = cv2.bitwise_not(input_image)
    return inverted_img
    
img_test = invert_colors_manual(img_rgb)
cv2.imshow('Negative img', img_test)
cv2.waitKey()

