# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:11:11 2020

@author: fuchsca
"""

import S1_algotools as S1

#---------------------------Global var

myTestTab = [1,58,67,1054]

#---------------------------

#---------------------------test alea
def test_alea_integers():
    assert S1.alea(5) == 4

#---------------------------test max value
def test_max_value():
    
    assert S1.max_value(myTestTab) == 1054

#---------------------------test_average_above_zero
def test_average_above_zero():
    
    assert S1.average_above_zero(myTestTab) == 295
    
#---------------------------test_reverse_table
def test_reverse_table():
    
    assert S1.reverse_table(myTestTab) == [1054,67,58,1]