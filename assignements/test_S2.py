import S1_algotools as S1
import numpy as np
import pytest

nbr_list = [1, -5, 3]
h = 12
w = 10
mtrx = np.zeros((h, w))
mtrx[0:1, 3:5] = np.ones(1)
mtrx[2:5, 1:3] = np.ones(1)

def test_average_above_zero():
    assert S1.average_above_zero(nbr_list) == 2.0

def test_max_value():
    assert S1.max_value(nbr_list) == 2

def test_reverse_table():
    assert S1.reverse_table(nbr_list) == [3, -5, 1]

def test_roi_bbox_2():
    assert S1.roi_bbox_2(mtrx) == (1, 4, 4, 0)

def test_average_above_zero_typeerror():
    with pytest.raises(TypeError):
        S1.average_above_zero(['a'])

def test_average_above_zero_negative():
    with pytest.raises(ZeroDivisionError):
        S1.average_above_zero([-1])