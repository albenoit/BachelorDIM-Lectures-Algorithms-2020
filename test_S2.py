# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:02:38 2020

@author: viardcrl
"""

import pytest as pt
import S1_algotools as s1

def test_average_above_zero():
    table = s1.average_above_zero([-1,-5,-3,-4,-9,-5])
    assert table == 0
