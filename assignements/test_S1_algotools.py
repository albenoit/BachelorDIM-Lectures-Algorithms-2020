# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:13:01 2020

@author: cuvellin
"""

import pytest
import S1_algotools as algotools
import numpy as np

def test_average_above_zero_add_intergers():
    Tab = [4,2,45,-4,14,-95,-4,2,87,-56,65,1,3]
    assert algotools.average_above_zero(Tab) == 24.77777777777778
    
def test_average_above_zero_only_negative_numbers():
    Tab = [-4,-95,-4,-56]
    with pytest.raises(ValueError):
        algotools.average_above_zero(Tab) == 24.77777777777778
        
def test_max_value():
    assert algotools.max_value([1,84,5,14,2,-546]) == 84
    
def test_max_value_fail():
    assert algotools.max_value([1,84,5,14,2,-546]) != 2
    
def test_random_fill_sparse():
    test = np.array([['','', 'X','X'], ['','', 'X', 'X'], ['X','','',''], ['','','X','X']])
    matrix = algotools.random_fill_sparse(test, 2)
    assert np.where(matrix == 'X')[0].shape[0] == 9
    
def test_remove_whitespace():
    assert algotools.remove_whitespace("this is a test") == "thisisatest"