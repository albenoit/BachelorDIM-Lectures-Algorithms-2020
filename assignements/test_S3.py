# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:52:59 2020

@author: ceriatik
"""

import pytest
import S3_imgproc_tools as S3
import numpy as np

def test_invert_colors_manual_tuNone():
    with pytest.raises(AttributeError):
        S3.invert_colors_manual(None)
        
def test_invert_colors_manual_tuArray():
    with pytest.raises(AttributeError):
        S3.invert_colors_manual(1)
        
def test_invert_colors_manual_tuuint8():
    with pytest.raises(TypeError):
        S3.invert_colors_manual(np.zeros(2,2), dtype=np.float32)
        
def test_innv_color_manual_Array():
    with pytest.raises(AttributeError):
        S3.invert_colors_manual(1)

def test_innv_color_manual():
    img_in = np.array([[[0,255,0], [0,255,0], [0,255,0]],
                [[0,255,128], [0,255,128], [0,255,128]],
                [[0,128,255], [0,128,255], [0,128,255]]],dtype=np.uint8)
    img_out = np.array([[[255,0,255], [255,0,255], [255,0,255]],
                [[255,0,127], [255,0,127], [255,0,127]],
                [[255,127,0], [255,127,0], [255,127,0]]],dtype=np.uint8)
    assert np.prod(S3.invert_colors_manual(img_in) == np.array(img_out))

def test_invert_colors_opencv_is_empty():
    with pytest.raises(TypeError):
        S3.invert_colors_opencv()

def test_invert_colors_numpy_no_img_out():
    img_in = np.array([[[0,255,0], [0,255,0], [0,255,0]],
                [[0,255,128], [0,255,128], [0,255,128]],
                [[0,128,255], [0,128,255], [0,128,255]]],dtype=np.uint8)
    img_out = np.array([[[255,0,255], [255,0,255], [255,0,255]],
                [[255,0,127], [255,0,127], [255,0,127]],
                [[255,127,0], [255,127,0], [255,127,0]]],dtype=np.uint8)
    with pytest.raises(TypeError):
        np.prod(S3.invert_colors_manual(img_in) == np.array())