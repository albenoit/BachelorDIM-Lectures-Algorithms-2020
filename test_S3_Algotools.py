# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:44:29 2020

@author: fuchsca
"""
import pytest
import S3_imgproc_tools as S3
import cv2
import numpy as np

     
def test_innv_gray_levels_tuNone():
    with pytest.raises(AttributeError):
        S3.innv_gray_levels(None)
def test_innv_gray_levels_tuarray():
    with pytest.raises(AttributeError):
        S3.innv_gray_levels(1)
def test_innv_gray_levels_tuuint8():
    with pytest.raises(TypeError):
        S3.innv_gray_levels(np.zeros((2.2),dtype=np.float32))

            


   


