# -*- coding: utf-8 -*-
import pytest 
import numpy as np
"""
Created on Tue Sep 29 10:39:08 2020

@author: tapiev
"""

import S3_imgproc_tools as S3


def test_invert_colors_manual():
    img_in = np.array([[[0,255,0], [0,255,0], [0,255,0]],
                [[0,255,128], [0,255,128], [0,255,128]],
                [[0,128,255], [0,128,255], [0,128,255]]])
    img_out = np.array([[[255,0,255], [255,0,255], [255,0,255]],
                [[255,0,127], [255,0,127], [255,0,127]],
                [[255,127,0], [255,127,0], [255,127,0]]])
    assert np.prod(S3.invert_colors_manual(img_in) == np.array(img_out))
    
def test_innv_gray_levels_None():
    with pytest.raises(AttributeError):
        S3.innv_gray_levels(None)
def test_innv_gray_levels_Array():
    with pytest.raises(AttributeError):
        S3.innv_gray_levels(1)
def test_innv_gray_levels_uint8():
    with pytest.raises(TypeError):
        S3.innv_gray_levels(np.zeros((2,2),np.dtype(np.bool)))
        
def test_innv_gray_levels_working():
    img_in = np.array([[[0,255,0], [0,255,0], [0,255,0]],
                [[0,255,128], [0,255,128], [0,255,128]],
                [[0,128,255], [0,128,255], [0,128,255]]])
    img_out = np.array([[[255,0,255], [255,0,255], [255,0,255]],
                [[255,0,127], [255,0,127], [255,0,127]],
                [[255,127,0], [255,127,0], [255,127,0]]])
    img_out.dtype=np.uint8
    img_in.dtype=np.uint8
    assert np.prod(S3.innv_gray_levels(img_in) == np.array(img_out))