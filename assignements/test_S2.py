import pytest
import cv2
import numpy as np
import S1_algotools as s1

"""
   Test Average_above_zero 

"""

def test_average_above_zero():
    assert s1.average_above_zero([5, 7]) == 6

def test_average_above_zero_not_a_list():
    with pytest.raises(TypeError):
        s1.average_above_zero(6)

def test_average_above_zero_empty_list():
    with pytest.raises(ValueError):
        s1.average_above_zero([])

def test_averrage_above_zero_negative_input():
    with pytest.raises(ValueError):
        s1.average_above_zero([-1,-1]) == 6


"""
   Test Max value 

"""
def test_max_value():
    assert s1.max_value([1,7,3,-6,5,2] ) == (7,1)

def test_max_value_not_a_list():
    with pytest.raises(TypeError):
        s1.max_value(3)

def test_max_value_not_a_number():
    with pytest.raises(TypeError):
        s1.max_value('a')


"""
   Test Reverse table

"""

def test_reverse_table():
    assert s1.reverse_table([1,2,3,4,5,6,7]) == [7,6,5,4,3,2,1]

def test_reverse_table_value_not_a_number():
    with pytest.raises(TypeError):
        s1.max_value('a')

def test_reverse_table_not_a_list():
    with pytest.raises(TypeError):
        s1.reverse_table(3)

"""
    Test Bounding Box
"""

def test_roi_bbox():
    H=1000
    W=1000
    n = np.zeros((H,W),dtype=np.uint8)
    n[45:200,70:91] = 1
    assert np.prod(s1.roi_bbox(n).all() == np.array([70,45,90,199]).all())

def test_roi_bbox_not_an_array():
    with pytest.raises(TypeError):
        s1.roi_bbox()

def test_roi_bbox_modification():
    H=200
    W=800
    d = np.zeros((H,W),dtype=np.uint8)
    d[45:123,54:70] = 1
    assert not np.prod(s1.roi_bbox(d) == np.array([70,45,90,199]))

"""
    Test Random fill sparse
"""

def test_random_fill_sparse():
    n = np.full((10,10),[""],dtype=str)
    val = 3
    assert np.where(s1.random_fill_sparse(n,val)=='X')[0].shape[0]==val


def test_random_fill_sparse_too_much_cross():
    n = np.full((10,10),[""],dtype=str)
    val = 10000
    with pytest.raises(ValueError):
     s1.random_fill_sparse(n,val)

"""
    Test Remove whitespace
"""

def test_remove_whitespace():
    assert s1.remove_whitespace('Hey Coucou') == 'HeyCoucou'

def test_remove_whitespace_without_space():
    assert s1.remove_whitespace('HeyCoucou') == 'HeyCoucou'

def test_remove_whitespace_not_a_char():
    with pytest.raises(TypeError):
        s1.remove_whitespace(1)

def test_remove_whitespace_empty_string():
    with pytest.raises(ValueError):
        s1.remove_whitespace('')

"""
    Test Selective sort
"""

def test_sort_selective():
    assert s1.sort_selective([4,9,1,5]) == [1,4,5,9]

def test_sort_selective_is_empty():
     with pytest.raises(TypeError):
        assert s1.sort_selective()

def test_sort_selective_is_false():
        assert s1.sort_selective([3,2,1]) != [1,3,2]

"""
    Test Bubble sort
"""

def test_sort_bubble():
    assert s1.sort_bubble([4,9,1,5]) == [1,4,5,9]

def test_sort_selective_not_a_number():
     with pytest.raises(TypeError):
        assert s1.sort_selective('a')

def test_sort_selective_failure():
     with pytest.raises(TypeError):
        assert s1.sort_selective(1)