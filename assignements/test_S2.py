# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:38:37 2020

@author: derbaghc
"""

import S1_algotools as main
import numpy as np
import pytest

def test_average():
    assert main.average_above_zero([1,2,3]) == 2
    
def test_max_value():
    assert main.max_value([1,2,5,48,3]) == (48, 3)
   
def test_reverse_table():
    assert main.reverse_table([1, 2, 3]) == [3,2,1]

@pytest.fixture
def input_image():
    rows = 5
    cols = 5
    input_image = np.zeros((rows, cols))   
    input_image[1:3,2:5] = np.ones((2, 3))
    return input_image

def test_roi_bbox(input_image):
    assert main.roi_bbox(input_image) == ([[1, 2], [1, 4]], [[2, 4], [2, 2]])
    
def test_alea():
    assert main.alea(5)
    
@pytest.fixture
def empty_tab():
    empty_tab = np.empty((5, 5), dtype=str)
    return empty_tab
    
def test_random_fill_sparse(empty_tab):
    filled_mat = main.random_fill_sparse(empty_tab, 4)
    #on compte le nb de X pour vérifier que cela correspond au nb indiqué
    assert np.where(filled_mat == "X")[0].shape[0] == 4
    
