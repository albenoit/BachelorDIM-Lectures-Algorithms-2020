import S1_algotools as algo
import pytest

tab = [1,9,3,4,5,6,7,8,2]
tab_under_zero = [0,-1,-3,-2]

def test_average():
    assert algo.average_above_zero(tab) == 5
    with pytest.raises(ValueError):
        assert algo.average_above_zero(tab_under_zero)

def test_max_value():
    assert algo.max_value(tab) == 9
#test
def test_get_index_max_value():
    assert algo.get_index_max_value(tab) == 2