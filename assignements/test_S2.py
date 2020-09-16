import S1_algotools as tFile
import pytest

def test_average_above_zero_with_only_positive_numbers():
    assert tFile.average_above_zero([2,3,4]) == 3

def test_average_above_zero_with_positive_and_negative_numbers():
    assert tFile.average_above_zero([2,-3,4,-8,3]) == 3

def test_average_above_zero_with_only_negative_numbers():
    with pytest.raises(ValueError):
        tFile.average_above_zero([-2,-3,-4,-8,-3])
