# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:10:38 2020

@author: albentmp
"""

import S1_algotools as sa
import pytest

def test_my_addition_Right():
    assert sa.my_addition(10,2) == 12
    
def test_my_addition_negative():
    assert sa.my_addition(-1,2) == 1
    
def test_my_addition_Error():
    with pytest.raises(TypeError):
        sa.my_addition("a",1)


def test_average_below_zero():
    assert sa.average_below_zero([1,2,5,4]) == 3
    
def test_average_below_zero_Error():
    with pytest.raises(ValueError):
        sa.average_below_zero([0,0,0])
        
def test_average_below_zero_Error_negative():
    with pytest.raises(ValueError):
        sa.average_below_zero([-1])
        

def test_reverse_table_Right():
    assert sa.reverse_table([1,2,3,4,5,6,7,8,9]) == [9,8,7,6,5,4,3,2,1]
    
import numpy as np
def test_roi_bbox_Right():
    W = 100
    H = 100
    Xin = np.zeros((H,W),dtype=float)    
    for c in range(10,51):
        for l in range(15,31):
            Xin[l,c] = 1
    #assert sa.roi_bbox(Xin) == np.array([[15,10],[15,50],[30,10],[30,50]])
    assert sa.roi_bbox(Xin) == (15,30,10,50)
            

def test_random_fill_sparse_Right():
    count = 2
    W = 5
    H = 5
    Xin = np.zeros((H,W),dtype=str)
    filled_mat = sa.random_fill_sparse(Xin,count)
    assert np.where(filled_mat == "X")[0].shape[0] == count
    

def test_remove_whitespace_Right():
    assert sa.remove_whitespace("b o n j o u r") == "bonjour"
    
def test_remove_whitespace_SeveralSpaces():
    assert sa.remove_whitespace("b              onjour ") == "bonjour"
    
    
def test_shuffle_Right():
    assert sa.shuffle([1,2,3,4,5]) != [1,2,3,4,5]
    
         
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            