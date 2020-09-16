# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:15:52 2020

@author: polletb
"""
import S1_algotoolspy

def test_average_above_zero():
    assert S1_algotoolspy.average_above_zero([10.0,20.0]) == 15.0