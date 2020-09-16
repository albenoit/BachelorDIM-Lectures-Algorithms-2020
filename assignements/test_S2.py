# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:21:21 2020

@author: tapiev
"""
import imp

foo = imp.load_source('S1_algotools', 'S1_algotools.py')



def test_answer():
    assert foo.average_above_zero([1,2]) == 1.5
    