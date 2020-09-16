# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:13:01 2020

@author: cuvellin
"""

import pytest
import S1_algotools as test

def test_average_above_zero_add_intergers():
    Tab = [4,2,45,-4,14,-95,-4,2,87,-56,65,1,3]
    assert test.average_above_zero(Tab) == 24.77777777777778
    
def test_average_above_zero_only_negative_numbers():
    Tab = [-4,-95,-4,-56]
    with pytest.raises(ValueError):
        test.average_above_zero(Tab) == 24.77777777777778