import Function as algo
import pytest
import numpy as np
H=18
W=18
Xin = np.zeros((H,W),dtype=float)
Xin[4:7,2:4]=np.ones((1,1))
for c in range(12,14):
    for l in range(13,15):
        Xin[l,c]=1
testTable=[1,3,5,7,9,2,4,6,8]
testTable2=[-13,-57,92,-46,8]

def test_answer():
    assert algo.onemore(3) == 4

def test_myaddition_intergers_1():
    assert algo.my_addition(10,2) == 12

def test_myaddition_intergers_2():
    assert algo.my_addition(-1,2) == 1

def test_myaddition_wrong_input():
    with pytest.raises(TypeError):
        algo.my_addition('a',2)

def test_average_above_zero():
    assert algo.average_above_zero(testTable) == 5.625

# def test_average_above_zero2():
#     with pytest.raises(TypeError):
#         algo.average_above_zero(testTable2)

def test_max_value():
    assert algo.max_value(testTable) == (9,4)

def test_reverse_table():
    assert algo.reverse_table(testTable) == [8, 6, 4, 2, 9, 7, 5, 3, 1]

# def roi_bbox():
#     assert algo.roi_bbox(Xin) == [2 4 13 14]