# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:37:36 2020

@author: vanhouta
"""
import func
import pytest


def test_answer():
    assert func.plusone(3) == 4
    
def test_answer2():
    assert func.plusone(14) == 15

def test_addition_integers_1():
    assert func.addition(10,2) == 12

def test_addition_integers_2():
    with pytest.raises(TypeError):
        func.addition('a',2)
    