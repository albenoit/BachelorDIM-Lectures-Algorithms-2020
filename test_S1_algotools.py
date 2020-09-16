import S1_algotools as S1
import pytest
import numpy as np

def test_max_value_OK():
    assert S1.max_value([0, 10, 20]) == 20

def test_max_value_exception():
    with pytest.raises(ValueError):
        S1.max_value([])

#------------------------average_above_zero
        
def test_average_above_zero_OK():
    assert S1.average_above_zero([0, -10, 20, 40]) == 30

def test_average_above_zero_exception_1():
    with pytest.raises(ValueError):
        S1.average_above_zero([0, -10, -20, -40])
        
def test_average_above_zero_exception_2():
    with pytest.raises(ValueError):
        S1.average_above_zero([])

#------------------------reverse_table
        
def test_reverse_table_OK():
    assert S1.reverse_table([1,2,3,4]) == [4,3,2,1]

def test_reverse_table_exception():
    with pytest.raises(ValueError):
        S1.reverse_table([])
        
#------------------------roi_bbox
        
def test_roi_bbox_OK():
    H = 12
    L = 10
    matrix = np.zeros((H,L))
    matrix[0:2, 7:9] = np.ones((2,2))
    matrix[2:4, 3:5] = np.ones((2,2))*2
    position = np.zeros((4,2))
    position[0:1, 1:2] = 3
    position[1:2, 1:2] = 8
    position[2:3, 0:1] = 3
    position[2:3, 1:2] = 3
    position[3:4, 0:1] = 3
    position[3:4, 1:2] = 8
    tab = S1.roi_bbox(matrix)
    
    assert np.prod(tab == position)
    
    
    
    
    
    
    
    
    