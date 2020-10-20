# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:11:11 2020

@author: fuchsca
"""
import numpy as np
import S1_algotools as S1

#---------------------------Global var

myTestTab = [1,58,67,1054]
myTestMatriceChar = np.zeros((10,10))
myImage = np.zeros((12,10))
myImage[6:8,5:7] = np.ones((2,2))
myImage[1:3,2:4] = np.ones((2,2))*2

#---------------------------

#---------------------------test alea
def test_alea_integers_Ok():
    assert S1.alea(5) == 4

def test_alea_integers_Exception():
    with pytest.raises(ValueError):
        S1.reverse_table([])
#---------------------------test max value
def test_max_value():
    
    assert S1.max_value(myTestTab) == 1054

#---------------------------test_average_above_zero
def test_average_above_zero():
    
    assert S1.average_above_zero(myTestTab) == 295
    
#---------------------------test_reverse_table
def test_reverse_table():
    
    assert S1.reverse_table(myTestTab) == [1054,67,58,1]
#---------------------------test_random_array_filling
def test_random_array_filling():
    table = S1.random_array_filling(myTestMatriceChar,10)
    assert np.size(np.argwhere(table))/2 == 10
#---------------------------test_roi_bbox 
'''def test_roi_bbox():'''
    
#---------------------------test_random_array_filling
def test_remove_whitespace():  
    assert S1.remove_whitespace("te     s t") == "test"
#---------------------------test_roi_bbox 
    
    