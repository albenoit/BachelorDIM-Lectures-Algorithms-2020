# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:10:38 2020

@author: albentmp
"""

import S1_algotools as sa
import pytest

def test_my_addition():
    assert sa.my_addition(10,2) == 12
    
def test_my_addition_negative():
    assert sa.my_addition(-1,2) == 1
    
def test_my_addition_Error():
    with pytest.raises(TypeError):
        sa.my_addition("a",1)

