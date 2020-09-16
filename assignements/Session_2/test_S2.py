# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:37:36 2020

@author: vanhouta
"""
import function as functest


def test_answer():
    assert functest.func(3) == 4
    
def test_answer2():
    assert functest.func(14) == 15
    
print(functest.func(4))
