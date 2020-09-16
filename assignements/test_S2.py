# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:42:29 2020

@author: bouvaran
"""
import S1_algotools as algo

tabTest = [1,2,3,4,5,6,7,8,9]

def test_algo():
   assert algo.average_above_zero(tabTest) == 5