# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:46:49 2020

@author: bouvaran
"""
import cv2
import numpy as np

img_gray=cv2.imread('imgAlgoPyth.jpg',0)
img_bgr=cv2.imread('imgAlgoPyth.jpg',1)


def invert_colors_manual(input_img):
    """ Une façon de le faire en détail mais pas opti"""
    newImg=np.zeros(input_img.shape, dtype=np.uint8)
    for row in range(input_img.shape[0]):
        for col in range(input_img.shape[1]):
            for channel in range(input_img.shape[2]):
                newImg[row,col,channel] = 255-input_img[row,col,channel]
    return newImg


def invert_colors_numpy(input_img):
    newImg = 255-input_img
    return newImg


def invert_colors_opencv(input_img):
    return ~input_img



"""Déclaration des fonction"""
img_invert          = invert_colors_manual(img_bgr)   
img_invertNP        = invert_colors_numpy(img_bgr)   
img_invertOpenCV    = invert_colors_numpy(img_bgr)   

"""Afichage des images"""
cv2.imshow('Gray levels image'  , img_gray)
cv2.imshow('bgr image'          , img_bgr)
cv2.imshow('Invert image'       , img_invert)
cv2.imshow('InvertNP image'     , img_invertNP)
cv2.imshow('InvertOpenCv image' , img_invertOpenCV)

cv2.waitKey()






