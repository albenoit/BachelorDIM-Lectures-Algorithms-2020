import S1_algotools as S1
import pytest

def test_max_value_OK():
    assert S1.max_value([0, 10, 20]) == 20

def test_max_value_exception():
    with pytest.raises(ValueError):
        S1.max_value([])

