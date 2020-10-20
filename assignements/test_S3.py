# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:26:31 2020

@author: vibertvg
"""
import pytest
import numpy as np
import S3_imgproc_tools as S3

def test_invert_colors_manual_uint8():
    with pytest.raises(TypeError):
        S3.invert_colors_manual(np.zeros((2,2,3),dtype=np.bool))