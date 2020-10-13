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

#print("Gray levels image shape  - " + str(img_gray.shape ))
#print("RGB levels image shape  - " + str(img_rgb.shape ))+
#print(img_rgb[1, 1, 2])

#cv2.imshow('Gray levels image', img_gray)
#cv2.imshow('RGB levels image', img_rgb)
#cv2.waitKey()


# =============================================================================
# Déclencheurs d'erreurs
# =============================================================================
def type_errors(img):
    '''
    Fonction qui renvoie des erreurs si le type n'est pas bon
    parameters : img
    return : 
    '''
    ##testé implicitement quand on init le paramètre
    '''
    if img is None:
        raise ValueError('expected an uint8 nd array')
    if not(isinstance(img, np.ndarray)):
        raise TypeError('expected a nd array')
    '''
    if img.dtype!=np.dtype(np.uint8):
        raise TypeError('expected uint8 typed nd array')
        

# =============================================================================
# Fonctions d'inversion et déclarations
# =============================================================================
def invert_colors_manual(input_image):
    '''
    Fonction qui inverse les couleurs d'une image (image négative)
    parameters : input_image
    return : inverted_img
    '''
    ##Pire solution pour Python (besoin de beaucoup de ressources)
    type_errors(input_image)
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
    type_errors(input_image)
    inverted_img = 255 - input_image
    return inverted_img



def invert_colors_opencv(input_image):
    '''
    Fonction qui inverse les couleurs d'une image (image négative)
    parameters : input_image
    return : inversed_img
    '''
    type_errors(input_image)
    inverted_img = cv2.bitwise_not(input_image)
    return inverted_img

#img_test = invert_colors_manual(img_rgb)
#cv2.imshow('Negative img', img_test)
#cv2.waitKey()


# =============================================================================
# Fonctions de seuil
# =============================================================================
def threshold_image_manual(input_img):
    '''
    Fonction qui renvoie une image binaire : on définit un seuil et quand on 
    passe au dessus de ce seuil -> tout passe en blanc et inversement quand on 
    passe en dessous du seuil -> tout passe en noir
    parameters : input_image
    return : output_image
    ''' 
    type_errors(input_img)
    threshold = 128
    for row in range(input_img.shape[0]):
        for col in range(input_img.shape[1]):
            for color in range(input_img.shape[2]):
                print(input_img.shape[2])
                if color > threshold:
                    input_img[color] = 255
                if color < threshold:
                    input_img[color] = 0 
    return input_img

img_test = threshold_image_manual(img_rgb)
cv2.imshow('Threshold img', img_test)
cv2.waitKey()


    
