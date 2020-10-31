# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:15:52 2020

@author: polletb
"""
import S1_algotools as algo
import pytest as pt
import numpy as np

#---------------------------------------------------------------------------------------------#
#-----------------------------------------   Algo 1   ----------------------------------------#
#---------------------------------------------------------------------------------------------#

def test_average_above_zero_correct_value_positif():
    assert algo.average_above_zero([10.0,20.0]) == 15.0
    
def test_average_above_zero_correct_value_positif_negatif():
    assert algo.average_above_zero([-10.0,20.0]) == 5

def test_average_above_zero_value_negatif():
    assert algo.average_above_zero([-10.0, -20.0]) == -15.0

def test_average_above_zero_value_positif_None():
    with pt.raises(Exception):
        algo.average_above_zero([None, 20.0])
        
def test_average_above_zero_value_negatif_None():
    with pt.raises(Exception):
        algo.average_above_zero([None, -20.0])
        
def test_average_above_zero_value_positif_negatif_None():
    with pt.raises(Exception):
        algo.average_above_zero([None, 10.0, -20.0])
    
def test_average_above_zero_empty():
    with pt.raises(Exception):
        algo.average_above_zero([])

#---------------------------------------------------------------------------------------------#
#-----------------------------------------   Algo 2   ----------------------------------------#
#---------------------------------------------------------------------------------------------#

def test_max_value_correct_value_positif():
    assert algo.max_value([10.0, 20.0, 30.0]) == (30.0, 2)

def test_max_value_correct_value_negatif():
    assert algo.max_value([-10.0, -20.0, -30.0]) == (-10.0, 0)
    
def test_max_value_correct_value_positif_negatif():
    assert algo.max_value([-10.0, 20.0, -30.0]) == (20.0, 1)

def test_max_value_value_positif_None():
    with pt.raises(Exception):
        algo.max_value([None, 20.0])
        
def test_max_value_value_negatif_None():
    with pt.raises(Exception):
        algo.max_value([None, -20.0])
        
def test_max_value_value_positif_negatif_None():
    with pt.raises(Exception):
        algo.max_value([None, 10.0, -20.0])
    
def test_max_value_empty():
    with pt.raises(Exception):
        algo.max_value([])
        
#---------------------------------------------------------------------------------------------#
#-----------------------------------------   Algo 3   ----------------------------------------#
#---------------------------------------------------------------------------------------------#

def test_reverse_table_correct_value_positif():
    assert algo.reverse_table([10.0, 20.0, 30.0]) == [30.0,20.0,10.0]

def test_reverse_table_correct_value_negatif():
    assert algo.reverse_table([-10.0, -20.0, -30.0]) == [-30.0,-20.0,-10.0]
    
def test_reverse_table_correct_value_positif_negatif():
    assert algo.reverse_table([-10.0, 20.0, -30.0]) == [-30.0, 20.0, -10.0]
    
def test_reverse_table_correct_value_string():
    assert algo.reverse_table(['aa', 'bb', 'cc']) == ['cc', 'bb', 'aa']
    
def test_reverse_table_correct_value_tuple():
    with pt.raises(Exception):
        algo.reverse_table((25,2))
    
#---------------------------------------------------------------------------------------------#
#-----------------------------------------   Algo 4   ----------------------------------------#
#---------------------------------------------------------------------------------------------#
@pt.fixture
def zero_numpy():
    zero_numpy = np.zeros((10,10), dtype=float)
    return zero_numpy     
    
@pt.fixture
def zero_numpy_with_one(zero_numpy):
    zero_numpy[2:5, 2:5] = np.ones((3,3), dtype=float)
    return zero_numpy


def test_roi_bbox_correct_value(zero_numpy_with_one, zero_numpy):
    assert algo.roi_bbox(zero_numpy) == ((zero_numpy_with_one) , ([2, 2], [4, 4]))
    
#---------------------------------------------------------------------------------------------#
#-----------------------------------------   Algo 5   ----------------------------------------#
#---------------------------------------------------------------------------------------------#
@pt.fixture
def empty_numpy():
    empty_numpy = np.empty((10,10), dtype=str)
    return empty_numpy  
    
    
def test_random_fill_sparse(empty_numpy):
    fill_table = algo.random_fill_sparse(empty_numpy, 5)
    assert np.where(fill_table == "X")[0].shape[0] == 5

