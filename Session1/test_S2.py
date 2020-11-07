# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:10:38 2020

@author: albentmp
"""

import S1_algotools as sa
import S1_dice as dice
import pytest

# ----- my_addition ----- #
'''
Test if 10 + 2 = 12
'''
def test_my_addition_Right():
    assert sa.my_addition(10,2) == 12

'''
Test if -1 + 2 = 1
'''
def test_my_addition_negative():
    assert sa.my_addition(-1,2) == 1

'''
Test in case we don't put an integer in parameters
Expecting a TypeError
'''
def test_my_addition_Error():
    with pytest.raises(TypeError):
        sa.my_addition("a",1)


# ----- average_below_zero ----- #
'''
Test with a good list, expecting a result of 3
'''
def test_average_below_zero():
    assert sa.average_below_zero([1,2,5,4]) == 3

'''
Test in case the list contains only 0
Expecting a ValueError
'''
def test_average_below_zero_Error():
    with pytest.raises(ValueError):
        sa.average_below_zero([0,0,0])

'''
Test in case the list contains a negative value
Expecting a ValueError
'''
def test_average_below_zero_Error_negative():
    with pytest.raises(ValueError):
        sa.average_below_zero([-1])
        
# ----- reverse_table ----- #
'''
Test which reverse correctly a list
Expecting [9,8,7,6,5,4,3,2,1] from [1,2,3,4,5,6,7,8,9]
'''
def test_reverse_table_Right():
    assert sa.reverse_table([1,2,3,4,5,6,7,8,9]) == [9,8,7,6,5,4,3,2,1]
    
import numpy as np
# ----- roi_bbox ----- #
'''
Test which find out the extremities of a square which countains every square
Expecting (15,30,10,50)
'''
def test_roi_bbox_Right():
    W = 100
    H = 100
    Xin = np.zeros((H,W),dtype=float)    
    for c in range(10,51):
        for l in range(15,31):
            Xin[l,c] = 1
    #assert sa.roi_bbox(Xin) == np.array([[15,10],[15,50],[30,10],[30,50]])
    assert sa.roi_bbox(Xin) == (15,30,10,50)
            
# ----- random_fill_sparse ----- #
'''
Count the number of X and compare it to the number put in parameters
Expecting it to be egual
'''
def test_random_fill_sparse_Right():
    count = 2
    W = 5
    H = 5
    Xin = np.zeros((H,W),dtype=str)
    filled_mat = sa.random_fill_sparse(Xin,count)
    assert np.where(filled_mat == "X")[0].shape[0] == count
    
# ----- remove_whitespace ----- #
'''
Test to see if the function remove every whitespace
Expecting "bonjour" without whitespace
'''
def test_remove_whitespace_Right():
    assert sa.remove_whitespace("b o n j o u r") == "bonjour"

'''
Test to see if the funcion every whitespace even if they are beside to each other
Expecting "bonjour" without whitespace
'''
def test_remove_whitespace_SeveralSpaces():
    assert sa.remove_whitespace("b              onjour ") == "bonjour"
    
# ----- shuffle ----- #
'''
Test if the list is suffled, so that it isn't as before
Expecting something different from the input
'''
def test_shuffle_Right():
    assert sa.shuffle([1,2,3,4,5]) != [1,2,3,4,5]

# ---- alea ---- #
'''
Test if the function bring a number between 0 and the value input
Exepecting a number between 0 and 10
'''
def test_alea_Right():
    result = sa.alea(10)
    assert result <= 10 and result >= 0
         
# ----- sort_selective ----- #
'''
Test if the function order the list from input
Expecting [1, 3, 3, 7, 9, 10, 15] from [10, 15, 7, 1, 3, 3, 9]
'''
def test_sort_selective_Right():
    assert dice.sort_selective([10, 15, 7, 1, 3, 3, 9]) == [1, 3, 3, 7, 9, 10, 15]

'''
Test if the function order the list if the list contains only the same numbers
Expecting [1,1,1,1,1] from [1,1,1,1,1]
'''
def test_sort_selective_SameNumbers():
    assert dice.sort_selective([1,1,1,1,1]) == [1,1,1,1,1]

'''
Test if the function order the list when it contains negative values
Expecting [-2,-3,5,6] from [5,-3,-2,6]
'''
def test_sort_selective_negativeValues():
    assert dice.sort_selective([5,-3,-2,6]) == [-2,-3,5,6]

# ---- sort_bubble ----- #
'''
Test if the function order the list from input
Expecting [1, 3, 3, 7, 9, 10, 15] from [10, 15, 7, 1, 3, 3, 9]
'''
def test_sort_bubble_Right():
    assert dice.sort_bubble([10, 15, 7, 1, 3, 3, 9]) == [1, 3, 3, 7, 9, 10, 15]
            
'''
Test if the function order the list if the list contains only the same numbers
Expecting [1,1,1,1,1] from [1,1,1,1,1]
'''
def test_sort_bubble_SameNumbers():
    assert dice.sort_bubble([1,1,1,1,1]) == [1,1,1,1,1]            
            
            
            
            
            
            
            
            
            
            
            
            
            
