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
        
        
def test_invert_colors_manual_process():
    