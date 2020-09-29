# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:48:56 2020

@author: fuchsca
"""

import cv2
import numpy as np

img_gray=cv2.imread('fond-gris.jpg',0)
img_bgr=cv2.imread('voiture.jpg',1)

print("Gray levels image shape ="+ str(img_gray.shape))
print("BGR image shape= "+str(img_bgr.shape))

cv2.imshow("gra levels image",img_gray)
cv2.imshow("BGR image",img_bgr)
cv2.waitKey()
