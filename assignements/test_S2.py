# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:42:29 2020

@author: bouvaran
"""
import S1_algotools as algo
tabTest = [1,2,3,4,5,6,7,8,9]

def test_average_above_zero():
   assert algo.average_above_zero(tabTest) == 5
   
def test_max_value():
   assert algo.max_value(tabTest) == 9

def test_average_above_zero_1():
   assert algo.reverse_table(tabTest) == [9,8,7,6,5,4,3,2,1]