import S1_algotools as S1
import pytest

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