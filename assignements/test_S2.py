import S1_algotools as tFile
import pytest

# Average above zero function
def test_average_above_zero_with_only_positive_numbers():
    assert tFile.average_above_zero([2,3,4]) == 3

def test_average_above_zero_with_positive_and_negative_numbers():
    assert tFile.average_above_zero([2,-3,4,-8,3]) == 3

def test_average_above_zero_with_only_negative_numbers():
    with pytest.raises(ValueError):
        tFile.average_above_zero([-2,-3,-4,-8,-3])

def test_average_above_zero_with_char_in_tab_error():
    with pytest.raises(Exception):
        tFile.average_above_zero(['azerty',-3,-4,-8,-3])

def test_average_above_zero_with_no_tab_error():
    with pytest.raises(Exception):
        tFile.average_above_zero('azerty')

def test_average_above_zero_with_empty_error():
    with pytest.raises(Exception):
        tFile.average_above_zero('')

# Max Values function
def test_max_value_with_only_positive_numbers():
    assert tFile.max_value([1,10,2,8,11]) == (4,11) #Only positive numbers

def test_max_value_with_only_negative_numbers():
    assert tFile.max_value([-1,-10,-2,-8,-11]) == (0,-1) #Only negative numbers

def test_max_value_with_positive_and_negative_numbers():
    assert tFile.max_value([1,10,2,8,-11]) == (1,10) #With positive and negative numbers

def test_max_value_with_char_in_tab_error():
    with pytest.raises(Exception):
        tFile.max_value(['azerty',-3,-4,-8,-3])

# Reverse table V1 function
def test_reserse_table_V1():
    assert tFile.reverse_table([1,10,2,8,11]) == [11,8,2,10,1]

def test_reserse_table_V2():
    assert tFile.reverse_table_V2([1,10,2,8,11]) == [11,8,2,10,1]

def test_reserse_table_V3():
    assert tFile.reverse_table_V3([1,10,2,8,11]) == [11,8,2,10,1]