# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import cv2
import numpy as np



#cv2.imshow('Titre',img_gray)
#cv2.waitKey()

'''
This function invert the colours of the image using the '255 - img' trick,
the optimal solution from a python perspective
@param : input_img (ndarray) is an image
@return : a ndarray, the image with inverted colours
'''
def invert_colors_manual(input_img):
    return 255 - input_img
    
'''
This function invert the colours of the image
@param : input_img (ndarray) is an image
@return : a ndarray, the image with inverted colours
'''
def invert_colors_manual2(input_img):
    img_out = np.zeros(img.shape, dtype = np.uint8) #On créer une image vide
    
    #On parcours tous les pixels
    for row in range(input_img.shape[0]): #Ligne
        for col in range(input_img.shape[1]): #Colonne
            for channel in range(img.shape[2]): #Filtre (1: Bleu; 2: Vert; 3: Rouge)
                img_out[row, col, channel] = 255 - input_img[row, col, channel] #On inverse la couleur
    return img_out
            
#Test:  
img_gray = cv2.imread('C:/Users/TEMP/Desktop/algo/img.jpg',0)
    
img = cv2.imread('C:/Users/TEMP/Desktop/algo/img.jpg',1)
print("BGR image shape = "+str(img.shape))
print(img.shape[0])

print(img[0,0])

imgResultat = invert_colors_manual2(img)
cv2.imshow('Titre', imgResultat)
cv2.waitKey()

