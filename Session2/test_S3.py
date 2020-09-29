# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 09:01:12 2020

@author: albentmp
"""

import S3_imgproc_tools as sa
import pytest
import numpy as np

#def test_my_addition_Right():
#    assert sa.my_addition(10,2) == 12
    
def test_invert_colors_manual_numpy_isNone():
    with pytest.raises(AttributeError):
        sa.invert_colors_manual_numpy(None)
        
def test_invert_colors_manual_numpy_isntNDArray():
    with pytest.raises(AttributeError):
        sa.invert_colors_manual_numpy(1)
      
def test_invert_colors_manual_numpy_isntUint8():
    with pytest.raises(TypeError):
        sa.invert_colors_manual_numpy(np.zeros((2,2), dtype=np.float32))

#def test_invert_colors_manual_numpy_processOK():
    #vérifier le type d'image_input (uint8?) (nombre de cannaux?)
    #image_input.dtype('uint8')
'''
def test_invert_colors_manual_numpy_testResultat():
    assert sa.invert_colors_manual([255,128,128,0]) == [0,127,127,255]
'''
  