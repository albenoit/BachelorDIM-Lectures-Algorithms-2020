# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:13:29 2020

@author: vibertvg
"""
import pytest
import S1_algotools as tobetested


    
    

def test_average_int_positive():
    assert tobetested.average_above_zero([10,5,15])==10
    

def test_average_int_negative():
    with pytest.raises(ValueError):
        tobetested.average_above_zero([-10,-5,-15,0])
    
def test_average_int_negative_and_zeros():
    with pytest.raises(ValueError):
        tobetested.average_above_zero([-10,-5,-15,0])
        
def test_average_float_positive():
    assert tobetested.average_above_zero([10.2,9.8])==10
    
def test_average_float_negative_and_zeros():
    with pytest.raises(ValueError):
        tobetested.average_above_zero([-10.5,-5.5,-15.5,0.5])

def test_average_float_int_positive():
    assert tobetested.average_above_zero([10.2,10,9.8])==10
    
"""
    Max value
"""


def test_max_value_positive():
    assert tobetested.max_value([10,15])==15
    

"""
    Reverse table
"""


def test_reverse_chars():
    with pytest.raises(TypeError):
        tobetested.max_value([2,'a'])==['a',2]
        
        
"""
    mapping matrice
"""

def test_map_mat():
    assert tobetested.create_image_matrice([1,1])
