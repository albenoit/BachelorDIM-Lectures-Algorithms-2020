# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:02:38 2020

@author: viardcrl
"""

import pytest as pt
import S1_algotools as s1
import numpy as np

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 1 ------------------------------#
#------------------------------------------------------------------------#

def test_average_above_zero_0():
    assert s1.average_above_zero([2,2]) == 2

def test_average_above_zero_1():
    with pt.raises(ZeroDivisionError):
         s1.average_above_zero([0])
    
def test_average_above_zero_2():
    with pt.raises(Exception):
        assert s1.average_above_zero([-1, 2]) == 2
    
def test_average_above_zero_3():
    with pt.raises(TypeError):
         s1.average_above_zero(['n'])
         
def test_average_above_zero_4():
    with pt.raises(TypeError):
         s1.average_above_zero([None])
         
#------------------------------------------------------------------------#
#------------------------------ EXERCISE 2 ------------------------------#
#------------------------------------------------------------------------#
    
def test_max_value_0():
    assert s1.max_value([1,5,3,4,9,5]) == 4
    
def test_max_value_1():
    assert s1.max_value([1.4,5.3,3.2,4.5,9.9,5.2]) == 4
    
def test_max_value_2():
    with pt.raises(TypeError):
        assert s1.max_value([1,5,'n'])
    
def test_max_value_3():
    with pt.raises(TypeError):
        assert s1.max_value([2,None])
        
def test_max_value_4():
    assert s1.max_value([0,0,0,0,0]) == 0
        
#------------------------------------------------------------------------#
#------------------------------ EXERCISE 3 ------------------------------#
#------------------------------------------------------------------------#
        
def test_reverse_table_0():
    assert s1.reverse_table([1,5,3,4,9,5]) == [5,9,4,3,5,1]
    
def test_reverse_table_1():
    assert s1.reverse_table([0,0,0,0,0]) == [0,0,0,0,0]
    
def test_reverse_table_2():
    with pt.raises(TypeError):
        assert s1.reverse_table([1,5,'n'])
    
def test_reverse_table_3():
    with pt.raises(TypeError):
        assert s1.reverse_table([2,None])
        
def test_reverse_table_4():
    assert s1.reverse_table([1.1,2,9,4.2]) == [4.2,9,2,1.1]
    
#------------------------------------------------------------------------#
#------------------------------ EXERCISE 4 ------------------------------#
#------------------------------------------------------------------------#
    
@pt.fixture
def zero_numpy():
    zero_numpy = np.zeros((10,10), dtype=float)
    return zero_numpy

@pt.fixture
def zero_numpy_with_one(zero_numpy):
    zero_numpy[2:5, 2:5] = np.ones((3,3), dtype=float)
    return zero_numpy

def test_roi_bbox(zero_numpy_with_one, zero_numpy):
    assert s1.roi_bbox(zero_numpy) == ([2,2],[4,4])