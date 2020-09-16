# -*- coding: utf-8 -*-
import pytest 
"""
Created on Wed Sep 16 14:21:21 2020

@author: tapiev
"""
import S1_algotools as S1

def test_averrage_above_zero_positive():
    assert S1.average_above_zero([1,2]) == 1.5
    
def test_averrage_above_zero_positive_and_negative():
    assert S1.average_above_zero([-1,2]) == 2

def test_myaddition_wrong_input():
    with pytest.raises(ValueError):
        S1.average_above_zero([-1,-1]) == 2