# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:37:36 2020

@author: vanhouta
"""
import function as functest
import sys
#from Session_1 import Exo_1 as funcS1
sys.path.insert(1, '../Session_1')

#import S1_algotools as funcS1


def test_answer():
    assert functest.func(3) == 4
    
def test_answer2():
    assert functest.func(14) == 15
    
'''def test_average_above_zero():
    Tab = [1,5,9,8,7,5,9,6,7,2]
    assert funcS1.average_above_zero(Tab) == 6.444444444444445'''