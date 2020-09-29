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

def test_averrage_above_zero_negative_input():
    with pytest.raises(ValueError):
        S1.average_above_zero([-1,-1]) == 2
        
def test_max_value_all_positive():
    assert S1.max_value([1,2,3]) == (3,2)
    
def test_max_value_all_negative():
    assert S1.max_value([-1,-2,-3]) == (-1,0)
    
def test_max_value_neg_and_post():
    assert S1.max_value([-1,2,15]) == (15,2)

def test_reverse_table_pair_table():
    assert S1.reverse_table([1,2,3,4]) == [4,3,2,1]
    
def test_reverse_table_impair_table():
    assert S1.reverse_table([1,2,3,4,5]) == [5,4,3,2,1]
    
import numpy as np
def test_roi_bbox():
    H=1000
    W=1000
    n = np.zeros((H,W),dtype=np.uint8)
    n[45:200,70:91] = 1
    assert np.prod(S1.roi_bbox(n).all() == np.array([70,45,90,199]).all())

def test_roi_bbox_different():
    H=1000
    W=1000
    d = np.zeros((H,W),dtype=np.uint8)
    d[38:150,70:91] = 1
    assert not np.prod(S1.roi_bbox(d) == np.array([70,45,90,199]))

def test_random_fill_sparse():
    n = np.full((20,20),[""],dtype=str)
    val = 5
    assert np.where(S1.random_fill_sparse(n,val)=='X')[0].shape[0]==val
    
def test_random_fill_sparse_false():
    n = np.full((20,20),[""],dtype=str)
    val = 5
    assert np.where(S1.random_fill_sparse(n,val+1)=='X')[0].shape[0]!=val
    
def test_remove_whitespace_phrase():
    assert S1.remove_whitespace("yomonbrocomment ça va")=="yomonbrocommentçava"

def test_shuffle_():
    assert S1.shuffle([1,2,3,4,5,6,7,8,9,10,11,12]) != [1,2,3,4,5,6,7,8,9,10,11,12]


