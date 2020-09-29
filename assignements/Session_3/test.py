# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:15:26 2020

@author: vanhouta
"""

import cv2 
import numpy as np 
import pytest
import S3_imgproc_tools as funcimg

def test_inv_gray_levels_tuNone():
    with pytest.raises(ValueError):
        funcimg.inv_gray_levels(None)
        
def test_inv_gray_levels_tuArray():
    with pytest.raises(ValueError):
        funcimg.inv_gray_levels(1)

def test_inv_gray_levels_tuuint8():
    with pytest.raises(ValueError):
        funcimg.inv_gray_levels(np.zeros((2,2),dtype=np.float))

def test_inv_gray_levels_tuuint8():
    ''' A faire '''