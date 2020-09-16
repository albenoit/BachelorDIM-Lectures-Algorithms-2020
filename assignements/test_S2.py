import S1_algotools as tobetested
import pytest

def test_myaddition_integers():
    assert tobetested.my_addition(10, 2) == 12

def test_myaddition_intergers_2():
    assert tobetested.my_addition(-1, 2) == 1

def test_myaddition_wrong_inpute():
    with pytest.raises(TypeError):
        tobetested.my_addition('a', 4)


