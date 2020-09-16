# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:37:36 2020

@author: vanhouta
"""
import func
import pytest
import numpy as np



def test_answer():
    assert func.plusone(3) == 4
    
def test_answer2():
    assert func.plusone(14) == 15

def test_addition_integers_1():
    assert func.addition(10,2) == 12

def test_addition_integers_2():
    with pytest.raises(TypeError):
        func.addition('a',2)
        
Tab = [10,10,19]
Tab2 = [-55,-8,-63]
def test_average_above_zero():
    assert func.average_above_zero(Tab) == 14.5

'''def test_average_above_zero2():
    with pytest.raises(TypeError):
        func.average_above_zero(Tab2)'''

def test_maximum_value():
      assert func.maximum_value(Tab) == (19,3)
    
def test_maximum_value_2():
      assert func.maximum_value(Tab2) == (-8,2)

def test_reverse_table():
      assert func.reverse_table(Tab) == [19,10,10]
    
      
W=150
H=200
W2 = 12
H2 = 10

Xin = np.zeros((H,W),dtype=float)
Xin2 = np.zeros((H2,W2),dtype=float)

for yXin in range(45,56):
    for xXin in range(70,91):
        Xin[xXin,yXin]=1

for yXin2 in range(7,10):
    for xXin2 in range(6,9):
        Xin2[xXin2,yXin2]=1
Xin2[5,8]=1
Xin2[7,10]=1
Xin2[9,8]=1

def test_roi_bbox():
      assert np.prod(func.roi_bbox(Xin) == np.array([45,70,55,90]))
      
def test_roi_bbox_2():
      assert np.prod(func.roi_bbox(Xin2) == np.array([7,5,10,9]))
      
chaine = "Ace Of Spades"
chaine2 = "Spyder cochon"

def test_remove_whitespace():
      assert func.remove_whitespace(chaine) == 'AceOfSpades'

def test_remove_whitespace_2():
      assert func.remove_whitespace(chaine2) == 'Spydercochon'  
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
