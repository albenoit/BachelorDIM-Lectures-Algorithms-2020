# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:21:21 2020

@author: tapiev
"""
import importlib
importlib.import_module("S1_algotools")

def test_answer():
    assert average_above_zero([1,2]) == 1.5