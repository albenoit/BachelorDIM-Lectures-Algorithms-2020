# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 09:54:47 2020

@author: polletb
"""

import S3_imgproc_tools as algo
import pytest as pt
import numpy as np
import cv2

img_bgr=cv2.imread('code.png',1)
img_bgr_invert=cv2.imread('codeInvert.png',1)


def test_path_img():
       assert cv2.imread('code.png',1) is not None
       

#---------------------------------------------------------------------------------------------#
#-----------------------------------------   Algo 1   ----------------------------------------#
#---------------------------------------------------------------------------------------------#

def test_invert_manual_img_bgr_None():
    with pt.raises(AttributeError):
        algo.invert_color_manual(None)
    
def test_invert_manua_img_bgr_type():
    with pt.raises(AttributeError):
        algo.invert_color_manual(1)
    
def test_invert_manua_img_bgr_uint8():
    with pt.raises(TypeError):
        algo.invert_color_manual(np.zeros((2,2),dtype=np.float32))
        
def test_invert_manua_img_bgr_result():
    assert algo.invert_color_manual(img_bgr).all() == img_bgr_invert.all()
    
#---------------------------------------------------------------------------------------------#
#-----------------------------------------   Algo 2   ----------------------------------------#
#---------------------------------------------------------------------------------------------#

def test_invert_numpy_img_bgr_None():
    with pt.raises(AttributeError):
        algo.invert_colors_numpy(None)
    
def test_invert_numpy_img_bgr_type():
    with pt.raises(AttributeError):
        algo.invert_colors_numpy(1)
    
def test_invert_numpy_img_bgr_uint8():
    with pt.raises(TypeError):
        algo.invert_colors_numpy(np.zeros((2,2),dtype=np.float32))
        
def test_invert_numpy_img_bgr_result():
    assert algo.invert_colors_numpy(img_bgr).all() == img_bgr_invert.all()

#---------------------------------------------------------------------------------------------#
#-----------------------------------------   Algo 3   ----------------------------------------#
#---------------------------------------------------------------------------------------------#
    
def test_invert_opencv_img_bgr_None():
    with pt.raises(AttributeError):
        algo.invert_colors_opencv(None)
    
def test_invert_opencv_img_bgr_type():
    with pt.raises(AttributeError):
        algo.invert_colors_opencv(1)
    
def test_invert_opencv_img_bgr_uint8():
    with pt.raises(TypeError):
        algo.invert_colors_opencv(np.zeros((2,2),dtype=np.float32))
        
def test_invert_opencv_img_bgr_result():
    assert algo.invert_colors_opencv(img_bgr).all() == img_bgr_invert.all()