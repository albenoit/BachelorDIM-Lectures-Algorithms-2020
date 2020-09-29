# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:07:51 2020

@author: bouvaran
"""
import pytest
import numpy as np
import S3_imgproc_tools as imgroc

"""Draft de Test uni"""
def test_invert_color_TuNone():
    with pytest.raises(AttributeError):
       imgroc.invert_colors_manual(None)

def test_invert_color_TuAray():
    with pytest.raises(AttributeError):
        imgroc.invert_colors_manual(1)
        
def test_invert_color_TuUint8():
    with pytest.raises(TypeError):
        imgroc.invert_colors_manual(np.zeros((2,2),dtype=np.float32))
    
def test_invert_color_TuProcessOk():
    imgroc.invert_colors_manual(np.zeros((2,2,2),dtype=np.uint8))
