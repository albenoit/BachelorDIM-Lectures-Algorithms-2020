# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:48:56 2020

@author: fuchsca
"""

import cv2
import numpy as np

#img_gray=cv2.imread('fond-gris.jpg',0)
#img_bgr=cv2.imread('voiture.jpg',1)
img_8k=cv2.imread('8k.jpg',1)


#print("Gray levels image shape ="+ str(img_gray.shape))

#print("BGR image shape= "+str(img_bgr.shape))

#cv2.imshow("gra levels image",img_gray)
#cv2.imshow("BGR image",img_bgr)
#cv2.waitKey()

def invert_colors_manual(input_img : np.ndarray) :
  image = np.asarray(input_img)
  nb_lignes,nb_colonnes,_ = image.shape
  image_sortie = np.copy(image)
  for ligne in range(nb_lignes):
    for col in range(nb_colonnes):
     for i in range(3):
      image_sortie[ligne,col,i] = 255 - image_sortie[ligne,col,i]
  return image_sortie

  #for row in range img.shape[0]
  #  for col in range img.shape[1]
  #     for channel in range img.shape[2]
  
  # En C 50* plus rapide : char * img_out;
  # En C : char * buffer;
  #  int cpt,maxcpt = ;
  #  img_out[cpt] = 255-img[cpt]
  # for(cpt=0; cpt<maxcpt;cpt++)
  
  # En C 50* plus rapide : char * img_out;
  # En C : char * buffer;
  #  int cpt,maxcpt = ;
  #  
  # for(cpt=max; ---cpt;)
  #  img_out[cpt] = 255-*img++

def invert_colors_numpy(input_img : np.ndarray) :
 
  image_sortie = np.copy(image)
  image_sortie = 255-image
  return image_sortie

def invert_colors_opencv(input_img : np.ndarray) :
  
  image_sortie = cv2.bitwise_not(input_img)
  
  return image_sortie

def innv_gray_levels(img :np.ndarray):   

    if img.dtype!=np.dtype(np.uint8):
        raise TypeError('expected an uint8 typed nd array')
    return 255-img


def threshold(img:np.ndarray):
    
    threshold_value = 128
    if img.dtype!=np.dtype(np.uint8):
            raise TypeError('expected uint8 typed nd array')
    return img<threshold_value

    
img = cv2.imread('voiture.jpg',1)
img_thresholded = threshold(img)
img_thresholded_disp = img_thresholded.astype(np.uint8)*40
cv2.imshow('seuille image',img_thresholded_disp)
cv2.waitKey()     

#cv2.imshow("Default",img_8k)   
#cv2.imshow("Test_Invert",invert_colors_opencv(img_8k))  
#cv2.waitKey()