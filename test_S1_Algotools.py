# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:11:11 2020

@author: fuchsca
"""

import S1_algotools as S1

def test_alea_integers():
    assert S1.alea(5) == 4
    

def test_max_value():
    mytab = [1,58,67,1054]
    assert S1.max_value(mytab) == 1054
    
    