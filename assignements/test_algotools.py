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