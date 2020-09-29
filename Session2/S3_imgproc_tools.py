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
This function invert the colours of the image
@param : input_img (ndarray) is an image
@return : a ndarray, the image with inverted colours
'''
def invert_colors_manual(input_img):
    img_out = np.zeros(img.shape, dtype = np.uint8) #On créer une image vide
    
    #On parcours tous les pixels
    for row in range(input_img.shape[0]): #Ligne
        for col in range(input_img.shape[1]): #Colonne
            for channel in range(img.shape[2]): #Filtre (1: Bleu; 2: Vert; 3: Rouge)
                img_out[row, col, channel] = 255 - input_img[row, col, channel] #On inverse la couleur
    return img_out

'''
This function invert the colours of the image using the '255 - img' trick,
the optimal solution from a python perspective
@param : input_img (ndarray) is an image
@return : a ndarray, the image with inverted colours
'''
def invert_colors_manual_numpy(input_img):
    #test data type, expecting uint8
    '''
    if input_img is None:
        raise AttributeError('expected an uint8 nd array')
    if not isinstance(input_img, np.ndarray):
        raise AttributeError('expected an nd array')
    '''
    if input_img.dtype != np.dtype(np.uint8):
        raise TypeError('expected uint8 nd array')
        
    return 255 - input_img

'''
This function threshold the image (make every dark pixel into black colour; and every light pixel into white colour)
@param: input_img (ndarray) is an image
@return : a ndarray, the image in black and white only (0 or 255 value)
'''
def threshold_image_manual(input_img):
    img_out = np.zeros(img.shape, dtype = np.uint8) #On créer une image vide
    
    #On parcours tous les pixels
    for row in range(input_img.shape[0]): #Ligne
        for col in range(input_img.shape[1]): #Colonne
            avgColour = 0
            for channel in range(img.shape[2]): #Filtre (1: Bleu; 2: Vert; 3: Rouge)
                avgColour = avgColour + input_img[row, col, channel]
            avgColour = avgColour / 3 #On fait la moyenne des trois couleurs
            valueCouleur = 0 #Si la moyenne est 'claire', alors on colore le pixel en noir
            if(avgColour > (255/2)): #Si la moyenne est 'claire', alors on colore le pixel en blanc
                valueCouleur = 255
                for i in range(3):
                    img_out[row, col, i] = valueCouleur #Coloration (des trois cannaux)
    return img_out


#Test:  
#img_gray = cv2.imread('C:/Users/TEMP/Desktop/algo/img.jpg',0)
    
img = cv2.imread('C:/Users/TEMP/Desktop/algo/img.jpg',1)
#print("BGR image shape = "+str(img.shape))
#print(img.shape[0])

#print(img[0,0])

#img = cv2.imread(np.zeros([5,5,3]))

#imgResultat = invert_colors_manual_numpy(img)

imgResultat = threshold_image_manual(img)
cv2.imshow('Titre', imgResultat)
cv2.waitKey()

