import S1_algotools as algo
import pytest
import numpy as np
import random

np_tab_zeros = np.zeros((200,200))
np_tab = np.zeros((200,200))
np_tab[70:90,45:55] = np.ones((20,10))

tab_red = [1,2,3]
tab = [1,9,3,4,5,6,7,8,2]
tab_under_zero = [0,-1,-3,-2]

def test_average():
    assert algo.average_above_zero(tab) == 5

def test_average_2():
    with pytest.raises(TypeError):
        assert algo.average_above_zero([1,"a",2,3])

def test_average_neg():
    with pytest.raises(ValueError):
        assert algo.average_above_zero(tab_under_zero)

def test_max_value():
    assert algo.max_value(tab) == 9
#test
def test_get_index_max_value():
    assert algo.get_index_max_value(tab) == 2

def test_reverse_table():
    assert algo.reverse_table(tab_red) == [3,2,1]

def test_bounding_box_raiseError():
    with pytest.raises(ValueError):
        assert algo.bounding_box(np_tab_zeros)

def test_bounding_box():
    assert algo.bounding_box(np_tab)[0][0] == 70
    assert algo.bounding_box(np_tab)[0][1] == 45
    assert algo.bounding_box(np_tab)[1][0] == 89
    assert algo.bounding_box(np_tab)[1][1] == 54