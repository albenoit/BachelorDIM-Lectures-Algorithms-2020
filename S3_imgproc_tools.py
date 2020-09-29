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

def invert_colors_numpy(input_img : np.ndarray) :
  image = np.asarray(input_img)
  nb_lignes,nb_colonnes,_ = image.shape
  image_sortie = np.copy(image)
  image_sortie = 255-image
  return image_sortie
  #for row in range img.shape[0]
  #  for col in range img.shape[1]
  #     for channel in range img.shape[2]

cv2.imshow("Default",img_8k)   
cv2.imshow("Test_Invert",invert_colors_numpy(img_8k))  
cv2.waitKey()