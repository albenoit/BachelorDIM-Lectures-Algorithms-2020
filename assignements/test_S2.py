# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:42:29 2020

@author: bouvaran
"""
import S1_algotools as algo
import pytest as pt
import numpy as np

tabTest = [1,2,3,4,5]
npTab = np.zeros([100,100],dtype = float)
npTab[60:85,45:55] = np.ones((25,10),dtype = float) 

#////////////////////////////////////////////
def test_average_above_zero_1():
   assert algo.average_above_zero(tabTest) == 3
       
def test_average_above_zero_2():
   with pt.raises(Exception):
       assert algo.average_above_zero([-1,2]) == 2
       
def test_average_above_zero_3():
   with pt.raises(ZeroDivisionError):
       assert algo.average_above_zero([0])
      
def test_average_above_zero_4():
   with pt.raises(TypeError):
       assert algo.average_above_zero(["n",1,2])
       
def test_average_above_zero_5():
   with pt.raises(TypeError):
       assert algo.average_above_zero([None])    
       
#////////////////////////////////////////////
def test_max_value_1():
   assert algo.max_value(tabTest) == 5
   
   
   
   


#////////////////////////////////////////////
def test_average_above_zero_1():
   assert algo.reverse_table(tabTest) == [5,4,3,2,1]
   
def test_roi_bbox_1():
   assert algo.roi_bbox(npTab)[0][0] == 60
   assert algo.roi_bbox(npTab)[0][1] == 45
   assert algo.roi_bbox(npTab)[1][0] == 84
   assert algo.roi_bbox(npTab)[1][1] == 54
   
def  test_random_fill_sparse():
    assert algo.random_fill_sparse